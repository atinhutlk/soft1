import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='metropolia',
    autocommit=True
)
def AirportsByCountry(country):
    sql = "SELECT ident, type, name, iso_country from airport"
    sql += " Where iso_country='" + country + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    result.sort(key=lambda x:x[1])
    for row in result:
        print(f"{row[3]}, {row[1]}, {row[2]}, ICAO code: {row[0]}")
    return

country = input("Country code: ")
AirportsByCountry(country)