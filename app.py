from flask import Flask, redirect, url_for, render_template, request, jsonify, send_from_directory, Response
from services import Vacation_service1
from services import User_service
from services import User_service2
from srcs.dal_b.Like_dao import Like_dao
from srcs.dal_b.Country_dao import Country_dao
import json
from modules1.User import User
from modules1.Like import Like
import os
from srcs.dal_b.Database import Database
from werkzeug.utils import secure_filename
from modules1.Country import Country
from modules1.Vacation import Vacation
from srcs.dal_b.Vacation_dao import Vacation_dao
from services import Vacation_service
from services import Vacation_service2
from services import Vacation_service3
from srcs.dal_b.User_dao import User_dao


app = Flask(__name__)


UPLOAD_FILE = os.path.join(os.getcwd(), 'uploads')

app.config['UPLOAD_FOLDER'] = UPLOAD_FILE


@app.route('/get_image/<image_name>', methods=['GET'])
def get_image(image_name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], image_name)


@app.route('/upload_image/<vacation_id>', methods=['POST'])
def upload_image(vacation_id):
    filename = ''  # if none can be -1
    if 'file' in request.files:
        print('file found')
        file = request.files['file']
        if file.filename != '':
            print('good name file')
            if isGoodName(file.filename):
                filename = file.filename
                print('good best', file.filename)
                if not os.path.exists(UPLOAD_FILE):
                    os.mkdir(UPLOAD_FILE)
                # filename = secure_filename(file.filename)
                file.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], filename))

    country = request.form.get('country')
    description = request.form.get('description')
    date_start = request.form.get('date_start')
    date_end = request.form.get('date_end')
    price = request.form.get('price')

    country_dao = Country_dao()
    idCountry = getCountry(country, country_dao.getAll())

    print(description)
    print(date_start)
    print(date_end)
    print(price)

    print('vacation_id: ', vacation_id)
    if int(vacation_id) == -1:
        print('inside inserting')

        try:
            print('inside inserting')
            print('filename before inserting', file.filename)
            Vacation_service2.insertVacations(
                idCountry, description, date_start, date_end, price, filename, False)
        except Exception as e:
            print('error inside inserting')
            # try:
            # למקרה שהתאריך כולו הפוך
            Vacation_service2.insertVacations(
                idCountry, description, date_start[::-1], date_end[::-1], price, filename, True)
            # except Exception as e:
            #   return jsonify({'message:': str(e)})
    else:
        print('inside update')

        try:
            print('inside update')

            Vacation_service3.updateVacations(
                vacation_id, idCountry, description, date_start, date_end, price, filename, False)
        except Exception as e:
            try:
                Vacation_service3.updateVacations(
                    vacation_id, idCountry, description, date_start[::-1], date_end[::-1], price, filename, True)
            except Exception as e:
                return jsonify({'message:': str(e)})
    print('continue')

    return redirect(url_for('in_like_page'))


def getCountry(nameC, countries):
    for c in countries:
        if c.name_country == nameC:
            return c.id

    country_dao = Country_dao()
    country = Country(-1, nameC)
    country_dao.insertCountry(country)
    return country.id


def isGoodName(filename):
    a = ['jpg', 'png', 'jpeg', 'webp']
    return '.' in filename and filename.split('.', 1)[1] in a


@app.route('/')
def index():
    return render_template('page1.html')


# from javascript update page for like
@app.route('/likes_page', methods=['POST'])
def likesPage():
    json = request.get_json()
    print(json)
    like = Like(int(json['id_user']), int(json['id_vacation']))
    likeDao = Like_dao()
    try:
        likeDao.insertLike(like=like)
        return Response(status=204)
    except Exception as e:
        return Response('error: ' + e, status=500)


@app.route('/likes_page_delete', methods=['POST'])
def likesPageDelete():
    json = request.get_json()
    print(json)
    like = Like(int(json['id_user']), int(json['id_vacation']))
    likeDao = Like_dao()
    try:
        likeDao.deleteLikeByLike(like=like)
        return Response(status=204)
    except Exception as e:
        return Response('error: ' + e, status=500)

    # update to sql

# move here from page1


@app.route('/in_like_page', methods=['POST', 'GET'])
def in_like_page():
    name = request.form.get('name')
    if name != None:
        # when enter with new user
        second_name = request.form.get('second_name')
        password = request.form.get('password')
        gmail = request.form.get('email')
        is_cheaked = 'is' in request.form

        message = User_service2.isUserRegister(
            name=name, second_name=second_name, password=password, email=str(gmail), isAdmin=is_cheaked)

        if type(message) == type(''):
            message = User_service.isUserLogin(
                name=name, second_name=second_name, password=password, email=str(gmail), isAdmin=is_cheaked)
            if type(message) == type(''):
                return jsonify({'message': 'try Login you to System: ' + message, 'values: ': [name, second_name, password, gmail, is_cheaked]})
            # editing to json in order to refresh page page2.html properly with the current user
            asJson = {'m': [message.id, message.name, message.second_name,
                            message.password, message.email, message.id_role]}
            data_dir = os.path.join(os.getcwd(), 'data')
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
            file_path = os.path.join(data_dir, 'user.json')
            with open(file_path, 'w') as file:
                json.dump(asJson, file, indent=4)
        else:
            asJson = {'m': [message.id, message.name, message.second_name,
                            message.password, message.email, message.id_role]}
            data_dir = os.path.join(os.getcwd(), 'data')
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
            file_path = os.path.join(data_dir, 'user.json')
            with open(file_path, 'w') as file:
                json.dump(asJson, file, indent=4)
    # WHEN simple updating page(not entering like back from add vacation)
    else:
        # get from json as object user...
        data_dir = os.path.join(os.getcwd(), 'data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        file_path = os.path.join(data_dir, 'user.json')
        with open(file_path, 'r') as file:
            myJson = json.load(file)['m']

            message = User(myJson[0], myJson[1], myJson[2],
                           myJson[3], myJson[4], myJson[5])
    vacationAll = []
    my_is_like = []
    with open(os.path.join(os.getcwd(), 'data', 'file2.json'), 'r') as file:
        searchJson = json.load(file)
    for vacation in Vacation_service1.getAllVacations():
        vacationAll.append({'id': vacation.id, 'num_likes': getNumLikeByIdVacation(vacation.id), 'country': findCountryName(
            vacation.id_country), 'description': vacation.description, 'date_start': vacation.date_start, 'date_end': vacation.date_end, 'price': vacation.price, 'image_name': vacation.image_name})
        my_is_like.append(isHasLike(message.id, vacation.id))

    bVacations = []
    b_my_is_like = []
    (bVacations, b_my_is_like) = accordingSearchJson(
        vacationAll, my_is_like, searchJson)

    return render_template('page2.html', vacations=bVacations, myIsLikes=b_my_is_like, my_user=message)


def getNumLikeByIdVacation(id):
    like_dao = Like_dao()
    return len(like_dao.getAllByIdVacation(id))


def accordingSearchJson(vacations, my_is_like, searchJson):
    new_vac = []
    newMyIsLike = []
    i = 0
    print('start for')

    for v in vacations:
        if ((searchJson['id'] == '-1' or searchJson['id'] == v['id']) and
            (searchJson['country'] == '-1' or str(searchJson['country']).lower() == str(
                v['country']).lower()) and
            (searchJson['description'] == '-1' or str(searchJson['description']).lower() in str(v['description']).lower()) and
            (searchJson['price'] == '-1' or int(searchJson['price']) >= v['price']) and
           ((searchJson['ischeaked'] ==
                '-1' or searchJson['ischeaked'] == str(3)) or (my_is_like[i] and searchJson['ischeaked'] == str(1)) or (not my_is_like[i] and searchJson['ischeaked'] == str(2)))
                and (searchJson['month_start'] == '-1' or isInSameMonth(searchJson['month_start'], v['date_start']))
                and (searchJson['year_start'] == '-1' or isInSameYear(searchJson['year_start'], v['date_start']))
                and searchJson['days_vacation'] == '-1' or isSameTimeVacation(searchJson['days_vacation'], v['date_start'], v['date_end'])):
            new_vac.append(v)
            newMyIsLike.append(my_is_like[i])
        i += 1
    return (new_vac, newMyIsLike)


def isInSameMonth(month_start_in_json, date_start):
    m = int(date_start[::-1][3:5][::-1])
    return int(month_start_in_json) == m


def isInSameYear(year_start_in_json, date_start):
    y = int(date_start[::-1][6:10][::-1])
    return int(year_start_in_json) == y


def isSameTimeVacation(stringDays, date_start, date_end):
    s_day = int(date_start[::-1][0:2][::-1])
    s_month = int(date_start[::-1][3:5][::-1])
    s_year = int(date_start[::-1][6:10][::-1])

    day = int(date_end[::-1][0:2][::-1])
    month = int(date_end[::-1][3:5][::-1])
    year = int(date_end[::-1][6:10][::-1])

    numDays = 0
    numDays += (year - s_year) * 365
    numDays += (month - s_month) * 30
    numDays += day - s_day + 1  # pluse 1 - if same day is one day.
    return numDays == int(stringDays)


def findCountryName(countryId):
    country_dao = Country_dao()
    for country in country_dao.getAll():
        if country.id == countryId:
            return country.name_country
    return None


def isHasLike(userId, vacationId):
    like_dao = Like_dao()
    for like in like_dao.getAll():

        if like.id_user == userId and vacationId == like.id_vacation:
            return True
    return False


# from javascript
@app.route('/profile/<id_user>', methods=['GET'])
def profilePage(id_user):
    user_dao = User_dao()
    user = user_dao.getUserById(id_user)
    return render_template('page3.html', user=user)


@app.route('/to_add_country/<vacation_id>', methods=['GET'])
def add_country(vacation_id):
    vacation_dao = Vacation_dao()
    vacation = vacation_dao.getVacationById(vacation_id)
    try:
        countryName = findCountryName(vacation.id_country)
        return render_template('page4.html', vacation=vacation, country_name=countryName, vacation_id=vacation_id)
    except Exception:
        return render_template('page4.html', vacation=vacation, country_name=None, vacation_id=vacation_id)


@app.route('/delete_country/<id>')
def deleteCountry(id):
    Vacation_service.deleteVacations(id)
    return redirect(url_for('in_like_page'))


@app.route('/send_search_json', methods=['POST'])
def send_search_json():
    myjson = request.get_json()
    dir_path = os.path.join(os.getcwd(), 'data')
    print("Directory exists:", os.path.exists(dir_path))

    os.makedirs(os.path.join(os.getcwd(), 'data'), exist_ok=True)
    with open(os.path.join(os.getcwd(), 'data', 'file2.json'), 'w') as file:
        json.dump(myjson, file, indent=4)

    return jsonify({'message': 'good'})


@app.route('/get_search_json')
def get_json():
    with open(os.path.join(os.getcwd(), 'data', 'file2.json'), 'r') as file:
        searchJson = json.load(file)
    return searchJson


if __name__ == '__main__':
    app.run(debug=True)
