import sqlite3 as sq

# with sq.connect('tourist.db') as con:   # создание базы
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS tourists(
#         id_trst INTEGER PRIMARY KEY,
#         first_name VARCHAR NOT NULL,
#         last_name VARCHAR NOT NULL,
#         sex VARCHAR NOT NULL,
#         birthday DATE NOT NULL,
#         phone_number VARCHAR NOT NULL,
#         email VARCHAR NOT NULL
#     )''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS tours(
#         id_tour INTEGER PRIMARY KEY,
#         name VARCHAR NOT NULL,
#         country VARCHAR NOT NULL,
#         city VARCHAR NOT NULL,
#         start_date DATE NOT NULL,
#         end_date DATE NOT NULL,
#         price DECIMAL
#     )''')
    # cur.execute('''CREATE TABLE IF NOT EXISTS bron(
    #     id_bron INTEGER PRIMARY KEY,
    #     id_trst INTEGER,
    #     id_tour INTEGER,
    #     bron_date DATE NOT NULL,
    #     count_t INTEGER,
    #     FOREIGN KEY (id_trst) REFERENCES tourists(id_trst),
    #     FOREIGN KEY (id_tour) REFERENCES tours(id_tour)
    # )''')

# info_tourist = [
#     (1, 'Куприн', 'Анна', 'ж', '1980-05-12', 89004562352, '1@email.com'), 
#     (2, 'Els', 'Ben', 'м', '1969-07-24', 79887418958, '2@email.com'), 
#     (3, 'Иванова', 'Амина', 'ж', '1999-01-15', 89096362352, '3@email.com'), 
#     (4, 'Greed', 'Emz', 'ж', '1987-03-31', 89456262352, '4@email.com'), 
#     (5, 'Alesh', 'Den', 'м', '1974-05-115', 89004562357, '5@email.com'),
#     (6, 'Steel', 'Milk', 'м', '1981-04-27', 78634567532, '6@email.com'),
#     (7, 'Алехин', 'Михаил', 'м', '1981-04-27', 78634567532, '7@email.com'),
#     (8, 'Сидоров', 'Анатолий', 'м', '1975-10-27', 78634567532, '8@email.com'),
#     (9, 'Алехина', 'Ангелина', 'ж', '1991-12-27', 78634567532, '9@email.com'),
#     (10, 'Медведева', 'Дарья', 'ж', '1989-09-27', 78634567532, '10@email.com')
#     ]
# with sq.connect('tourist.db') as con:   # наполнение данными
#     cur = con.cursor()
#     cur.executemany('INSERT INTO tourists VALUES (?,?,?,?,?,?,?)', info_tourist)

# info_tour = [
    # (1, 'Статуя из кина SONY', 'США', 'Нью-Йорк', '2020-07-10', '2020-07-25', 526000),
    # (2, 'Культурная столица', 'Россия', 'Санкт-Петербург', '2023-06-10', '2023-06-15', 25600),
    # (3, 'Америка', 'США', 'Лас-Вегас', '2022-07-10', '2022-07-25', 1448000),
    # (4, 'Турция в1', 'Турция', 'Обакой', '2020-01-10', '2020-02-10', 34565),
    # (5, 'Турция в2', 'Турция', 'Бельдиби', '2022-10-11', '2022-10-16', 52963),
    # (6, 'Великие треугольники', 'Египет', 'Хургада', '2020-09-28', '2020-10-5', 174152),
    # (7, 'Сом и треугольники', 'Египет', 'Сома Бэй', '2023-01-13', '2023-01-25', 174455),
    # (8, 'Ракушки', 'Сейшелы', 'Маэ', '2022-07-10', '2022-07-25', 520741),
    # (9, 'В гости к богам', 'Греция', 'Киллини', '2020-12-10', '2020-12-21', 1074106),
#     (10, 'Америка', 'США', 'Вашингтон', '2020-07-10', '2020-07-25', 52600)
#     ]
# with sq.connect('tourist.db') as con:   # наполнение данными
#     cur = con.cursor()
#     cur.executemany('INSERT INTO tours VALUES (?,?,?,?,?,?,?)', info_tour)

# info_bron = [
#     (1, 3, 2, '2020-12-03', 12),
#     (2, 5, 1, '2020-11-21', 74),
#     (3, 2, 9, '2020-10-06', 14),
#     (4, 2, 8, '2020-09-03', 12),
#     (5, 10, 6, '2020-03-13', 1),
#     (6, 3, 7, '2020-06-23', 45),
#     (7, 4, 3, '2020-06-28', 12),
#     (8, 9, 4, '2020-07-16', 45),
#     (9, 8, 10, '2020-08-25', 4),
#     (10, 6, 5, '2020-08-12', 3)
#     ]
# with sq.connect('tourist.db') as con:   # наполнение данными
#     cur = con.cursor()
#     cur.executemany('INSERT INTO bron VALUES (?,?,?,?,?)', info_bron)


# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
# Выборка
    # cur.execute('SELECT * FROM tourists')   # 1
    # cur.execute('SELECT * FROM tours ORDER BY price DESC')   # 2
    # cur.execute('SELECT * FROM bron WHERE id_tour = (SELECT id_tour FROM tours where city = "Маэ")')   # 3
    # cur.execute('SELECT * FROM tourists WHERE id_trst = (SELECT id_trst FROM bron where bron_date = "2020-07-16")')   # 4
    # cur.execute('SELECT * FROM tours WHERE city IS NOT NULL and country IS NOT NULL')   # 5
    # cur.execute('SELECT id_tour, country, city FROM tours')   # другой вариант 5
    # cur.execute('SELECT * FROM tourists WHERE sex = "ж" AND birthday >= "1990-01-01"')   # 6
    # cur.execute('SELECT * FROM tours WHERE price >= 5000')   # 7
    # cur.execute('SELECT * FROM tourists WHERE id_trst = (SELECT id_trst FROM bron where id_tour = 2)')   # 8
    # cur.execute('SELECT * FROM tourists WHERE id_trst = (SELECT id_trst FROM bron where bron_date = "2020-11-21")')   # 9
    # cur.execute('SELECT * FROM tourists WHERE phone_number LIKE "7%"')   # 10
#     res = cur.fetchall()
# print(res)

# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
# Обновление
    # cur.execute('UPDATE tours SET start_date = "2023-05-01" WHERE id_tour = 1')   # 1
    # cur.execute('UPDATE tours SET price = 1500 WHERE id_tour = 7')   # 2
    # cur.execute('UPDATE tourists SET phone_number = "15551234567" WHERE id_trst = 5')   # 3
    # cur.execute('UPDATE bron SET bron_date = "2023-04-05" WHERE id_bron = 3')   # 4
    # cur.execute('UPDATE bron SET count_t = 3 WHERE id_tour = 8')   # 5
    # cur.execute('UPDATE tours SET end_date = "2023-08-31" WHERE id_tour = 2')   # 6
    # cur.execute('UPDATE tourists SET email = "new_email@example.com" WHERE id_trst = 1')   # 7
    # cur.execute('UPDATE tours SET start_date = "2023-06-15" WHERE id_tour = 4')   # 8
    # cur.execute('UPDATE tours SET start_date = "2023-05-01" WHERE country = "Испания"')   # 9
    # cur.execute('UPDATE tours SET price = 1500 WHERE name = "Греция-отдых на море"')   # 10
    # cur.execute('UPDATE tours SET start_date = "2023-06-01" WHERE name = "Испания-путешествия по городам"')   # 11
    # cur.execute('UPDATE bron SET count_t = 3 WHERE id_tour = 1002')   # 12
    # cur.execute('UPDATE tourists SET phone_number = "1123567890" WHERE id_trst = 2001')   # 13
    # cur.execute('UPDATE bron SET bron_date = "2022-07-01" WHERE id_tour = (SELECT id_tour FROM tours WHERE price <= 2000)')   # 14
    # Запрос 15 преподаватель разрешил убрать
    # cur.execute('UPDATE tours SET start_date = "2023-08-15" WHERE id_tour = (SELECT id_tour FROM bron WHERE count_t > 2)')   # 16
    # cur.execute('UPDATE tours SET name = "Египет-отдых на курорте" WHERE id_tour = 1003')   # 17

# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
# Удаление
    # cur.execute('DELETE FROM bron WHERE id_trst = 1')   # 1
    # cur.execute('DELETE FROM bron WHERE id_tour = 2')   # 2
    # cur.execute('DELETE FROM bron WHERE bron_date = "2020-09-03"')   # 3
    # cur.execute('DELETE FROM tourists WHERE id_trst = (SELECT id_trst FROM bron WHERE id_tour = 3)')   # 4
    # cur.execute('DELETE FROM bron WHERE id_trst = (SELECT id_trst FROM tourists WHERE phone_number = "15551234567")')   # 5
    # cur.execute('DELETE FROM bron WHERE id_trst = (SELECT id_trst FROM tourists WHERE email = "2@mail.ru")')   # 6
    # cur.execute('DELETE FROM bron WHERE id_tour = (SELECT id_tour FROM tours WHERE start_date >= "2023-09-24")')   # 7
    # cur.execute('DELETE FROM tourists WHERE id_trst = (SELECT id_trst FROM bron WHERE id_tour = (SELECT id_tour FROM tours WHERE country = "США"))')   # 8
    # cur.execute('DELETE FROM bron WHERE id_tour = (SELECT id_tour FROM tours WHERE start_date = "2023-09-24")')   # 9
    # cur.execute('DELETE FROM bron WHERE id_tour = (SELECT id_tour FROM tours WHERE price = 25600)')   # 10
