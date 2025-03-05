
CREATE TABLE IF NOT EXISTS likes (
    id_user INT NOT NULL,
    id_vacation INT NOT NULL
);


DROP TABLE IF EXISTS roles;

CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    second_name TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    id_role INTEGER
);

DROP TABLE IF EXISTS countries;

CREATE TABLE IF NOT EXISTS countries (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

DROP TABLE IF EXISTS vacations;


CREATE TABLE IF NOT EXISTS vacations (
    id SERIAL PRIMARY KEY,
    id_country INTEGER NOT NULL,
    description TEXT NOT NULL,
    date_start TEXT NOT NULL,
    date_end TEXT NOT NULL,
    price INTEGER NOT NULL,
    image_name TEXT NOT NULL
);

INSERT INTO roles (name) VALUES ('Admin');
INSERT INTO roles (name) VALUES ('User');

INSERT INTO users (name, second_name, password, email, id_role) VALUES 
('dan', 'shmueli', '12345', 'dan@gmail.com', 1),
('ron', 'roni', '12376', 'roni1@gmail.com', 2);

INSERT INTO countries (name) VALUES 
('Israel'), ('Australia'), ('USA'), ('Bulgaria'), ('France'),
('Brazil'), ('Antarctica'), ('China'), ('India'), ('Slovakia');

INSERT INTO vacations (id_country, description, date_start, date_end, price, image_name) VALUES 
(4, 'חופשת החלומות', '2026-10-10', '2026-12-10', 50000, 'image1'),
(3, 'ביזנס', '2026-10-10', '2026-12-10', 40000, 'image2'),
(1, 'ארץ הקודש', '2026-10-10', '2026-10-29', 3000, 'image3'),
(10, 'נופים מרהיבים בסלובקיה', '2026-09-10', '2026-10-10', 25000, 'image4'),
(5, 'מסע בעיקבות השורשים הצרפתיים', '2026-10-01', '2026-10-10', 6000, 'image5'),
(9, 'מסע להודו', '2026-10-01', '2026-10-20', 4000, 'image6'),
(8, 'טיול למדינה הגדולה בעולם', '2026-09-10', '2026-09-29', 8000, 'image7'),
(3, 'חופשה על הים', '2026-11-01', '2026-11-09', 9000, 'image8'),
(4, 'טיול עם נוף הררי', '2026-10-10', '2026-12-10', 60000, 'image9'),
(7, 'הכי קר', '2026-07-10', '2026-12-10', 100000, 'image10'),
(4, 'צאו לגלות בעלי חיים מרהיבים וטבע פראי', '2026-10-10', '2026-12-10', 30000, 'image11'),
(4, 'חופשת אקסטרים', '2026-10-10', '2026-11-10', 20000, 'image12');
