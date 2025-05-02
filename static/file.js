function clickAddLike(vacationid, usr_id) {
    console.log(vacationid)
    console.log(usr_id)
    fetch('/likes_page', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ 'id_vacation': vacationid, 'id_user': usr_id }) }).then(response => {
        // window.location.reload();
        console.log('in')
    });
}

let b = true;
function clickDone(vacation_id, usr_id, checkbox) {
    b = false;
    if (checkbox.checked) {
        clickAddLike(vacation_id, usr_id);
    }
    else {
        clickRemoveLike(vacation_id, usr_id);
    }
    setTimeout(() => {
        b = true;
        console.log(b)
    }, 100);

}

function clickRemoveLike(vacationid, usr_id) {
    fetch('/likes_page_delete', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ 'id_vacation': vacationid, 'id_user': usr_id }) }).then(response => {
        // window.location.reload();
        console.log('in')
    });
}

function click_update_vacation(vacation_id) {
    console.log(b);
    if (b) {
        console.log('in')
        window.location.href = '/to_add_country/' + vacation_id;
    }
}

//restart with the relevant values from the json
let allTexts = document.getElementsByClassName('editTextClass');
let checkLike = document.getElementsByClassName('divLike');
let realCheck = document.getElementsByClassName('cheackboxclass');
let bt = document.getElementById('m');
//index 3 in buttons
let buttons_search = document.getElementsByClassName('button_search');

function restartAll() {
    for (let i = 0; i < allTexts.length; i++) {
        allTexts[i].style.display = 'none';
    }
    checkLike[0].style.display = 'none';
}

function clickSomeSearchButton(indexButton) {
    restartAll();
    if (indexButton === 4) {
        checkLike[0].style.display = 'block';
    }
    else if (indexButton > 4) {
        //the allTexts is length -1 from button_search therefore button index minus 1
        indexButton = indexButton - 1;
        allTexts[indexButton].style.display = 'block';
    }
    else {
        allTexts[indexButton].style.display = 'block';
    }
}

function doClickOnButtons() {
    for (let i = 0; i < buttons_search.length; i++) {
        buttons_search[i].addEventListener('click', (event) => {
            clickSomeSearchButton(i);
        });
    }
}

/*
fetch('/send_search_json', { method: 'POST', headers: { 'Content-Type:': 'application/json' }, body: JSON.stringify({ id: '-1', country: '-1', description: '-1', price: '-1', ischeaked: '-1', month_start: '-1', year_start: '-1', days_vacation: '-1' }) }).then(response => { });
*/
function doDefaultValues() {
    fetch('/get_search_json')
        .then(response => response.json())
        .then(data => {
            if (data.id != '-1') {
                allTexts[0].value = data.id;
                console.log(data.id);
            }
            if (data.country != '-1') {
                allTexts[1].value = data.country;
            }
            if (data.description != '-1') {
                allTexts[2].value = data.description;
            }
            if (data.price != '-1') {
                allTexts[3].value = data.price;
            }
            if (data.ischeaked !== '-1') {
                if (data.ischeaked === '1') {
                    realCheck[0].checked = true;
                }
                else if (data.ischeaked === '2') {
                    realCheck[1].checked = true;
                }
                else {
                    realCheck[2].checked = true;
                }
            }
            else {
                realCheck[2].checked = true;
            }
            if (data.month_start != '-1') {
                allTexts[4].value = data.month_start;
            }
            if (data.year_start != '-1') {
                allTexts[5].value = data.year_start;
            }
            if (data.days_vacation != '-1') {
                allTexts[6].value = data.days_vacation;
            }
        });
}

let allTextNumLikes = document.getElementsByClassName('numlikesText');
let allCheckBoxes = document.getElementsByClassName('cheack123');
console.log(allTextNumLikes.length + "");
console.log(allCheckBoxes.length + "");
function doGoodClickOnCheckBoxes() {
    for (let i = 0; i < allCheckBoxes.length; i++) {
        allCheckBoxes[i].addEventListener('click', () => {
            console.log('click checkbox');
            if (allCheckBoxes[i].checked) {
                allTextNumLikes[i].innerText = parseInt(allTextNumLikes[i].innerText) + 1 + "";
            }
            else {
                allTextNumLikes[i].innerText = parseInt(allTextNumLikes[i].innerText) - 1;
            }
        });
    }
}

function doGoodClickOnCheacks() {
    for (let i = 0; i < realCheck.length; i++) {
        realCheck[i].addEventListener('click', () => {
            realCheck[0].checked = false;
            realCheck[1].checked = false;
            realCheck[2].checked = false;
            realCheck[i].checked = true;
        });
    }
}

doDefaultValues();
clickSomeSearchButton(0);
doClickOnButtons();
doGoodClickOnCheacks();
doGoodClickOnCheckBoxes();
bt.style.display = 'none';



function clickSearchDo() {
    //write to json first
    console.log('do search...')
    bt.style.display = 'block';

    let id = allTexts[0].value.trim();
    if (id.length === 0) {
        id = '-1';
    }
    let country = allTexts[1].value.trim();
    if (country.length === 0) {
        country = '-1';
    }
    let description = allTexts[2].value.trim();
    if (description.length === 0) {
        description = '-1';
    }
    let price = allTexts[3].value.trim();
    if (price.length === 0) {
        price = '-1';
    }
    let numChecked = '-1';
    if (realCheck[0].checked) {
        numChecked = '1';
    }
    else if (realCheck[1].checked) {
        numChecked = '2';
    }
    else if (realCheck[2].checked) {
        numChecked = '3';
    }
    let month_start = allTexts[4].value.trim();
    if (month_start.length === 0) {
        month_start = '-1';
    }
    let year_start = allTexts[5].value.trim();
    if (year_start.length === 0) {
        year_start = '-1';
    }
    let days_vacation = allTexts[6].value.trim();
    if (days_vacation.length === 0) {
        days_vacation = '-1';
    }

    myjson = { id: id, country: country, description: description, price: price, ischeaked: numChecked, month_start: month_start, year_start: year_start, days_vacation: days_vacation };

    fetch('/send_search_json', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(myjson) })
        .then(response => response.json())
        .then(data => {
            fetch('/in_like_page').then(response => { }).then(data => {
                window.location.reload();
                bt.innerText = 'finish!';
                setTimeout(() => {
                    bt.style.display = 'none';
                }, 10000)
            });
        });
}
//lestener to bottons change search
//listener to button search

//in search click if empty I write -1