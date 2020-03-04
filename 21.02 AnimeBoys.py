from random import choice, randint
import sys
import psycopg2
import csv

def get_data():
    city = ['Almaty', 'Nur-Sultan', 'Semei']
    currency = ['KZT', 'USD', 'EUR', 'RUB']
    amount = randint(-1000000, 1000000)
    answer = (choice(city), choice(currency), amount)
    return answer


def aws():
    try:
        connection = psycopg2.connect(user='postgres',
                                      password='password',
                                      host='almau-students.cmwfjvlei66t.eu-central-1.rds.amazonaws.com',
                                      port='5432',
                                      database='postgres')
        print('connected')
    except(Exception, psycopg2.Error) as error:
        connection = ''
        print(error)
    return connection


def add_data():
    connection = aws()
    if connection == '':
        print('Error')
    else:
        data = get_data()
        cursor = connection.cursor()
        for i in range(200):
            cursor.execute("Insert into AnimeBoys(city, currency, amount) "
                           "values (%s, %s, %s)", get_data())
            print("ADD")
        connection.commit()
        print('Success')


def aws_create_table():
    connection = aws()
    if connection == '':
        print('Error')
    else:
        cursor = connection.cursor()
        cursor.execute("Create table if not exists AnimeBoys "
                       "(ID serial primary key, city varchar(50), currency varchar(3),"
                       "amount float(10))")
        connection.commit()
        print('Table created')


def aws_select_data():
    connection = aws()
    sql_select = "SELECT * FROM AnimeBoys"
    cursor = connection.cursor()
    cursor.execute(sql_select)
    records = cursor.fetchall()
    print("My data from Anime Boys ", records)


def aws_delete_data():
    connection = aws()
    sql_select = "DELETE FROM AnimeBoys Where id = 2"
    cursor = connection.cursor()
    cursor.execute(sql_select)
    connection.commit()
    print("Deleted ")


def write():
    connection = aws()
    cursor = connection.cursor()
    sql = "SELECT * FROM AnimeBoys"
    cursor.execute(sql)
    with open("table.csv", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])  # write headers
        csv_writer.writerows(cursor)
    # cursor.close()
    # sql_select = "SELECT * FROM AnimeBoys"
    # file = open('data.txt')
    # for i in sql_select:
    #     file.write(i)
    # file.close()


if __name__ == '__main__':
    # add_data()
    # aws_select_data()
    # aws_delete_data()
    write()