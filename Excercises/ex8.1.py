import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='metropolia',
    autocommit=True
)
def AirportByICAO(icao):
    sql = "SELECT ident, name, iso_country, iso_region, municipality from airport"
    sql += " WHERE ident='" + icao + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[0]}: {row[1]} in {row[4]}, {row[3]}, {row[2]}")
    return

icao = input("ICAO code: ")
AirportByICAO(icao)