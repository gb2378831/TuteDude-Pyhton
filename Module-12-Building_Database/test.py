import psycopg2
def table():
    conn = psycopg2.connect(dbname="postgres", user="postgres",password="1234567890",host="localhost",port="5433")

    cursor = conn.cursor()
    cursor.execute('''create table employees(Name Text, ID int, Age int);''')
    print("Table Created Successfully")

    conn.commit()
    conn.close()

# table()

def data():
    conn = psycopg2.connect(dbname="postgres", user="postgres",password="1234567890",host="localhost",port="5433")

    cursor = conn.cursor()

    name = input("Enter name: ")
    id = input('Enter id: ')
    age = input('Enter age: ')

    # cursor.execute('''insert into employees(Name, ID, Age) values('Sam',01,30);''')

    query = ('''insert into employees(Name, ID, Age) values(%s,%s,%s);''')

    cursor.execute(query,(name,id,age))


    print("Data Added Successfully")

    conn.commit()
    conn.close()

data()


# def extract():
#     conn = psycopg2.connect(dbname="postgres", user="postgres",password="1234567890",host="localhost",port="5433")

#     cursor = conn.cursor()
#     cursor.execute('''select * from employees;''')
#     show = cursor.fetchone()
#     print(show[0])
#     # print("Data Added Successfully")

#     conn.commit()
#     conn.close()

# extract()

