import mysql.connector
from geopy.distance import distance

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='metropolia',
    autocommit=True
)
def distanceBetween2Aiports(icao1, icao2):
    airports = []
    deg = []
    sql = "SELECT ident, name, iso_country, latitude_deg, longtitude_deg from airport"
    sql1 = sql + " Where ident='" + icao1 + "'"
    print(sql1)
    sql2 = sql + " Where ident='" + icao2 + "'"
    print(sql2)
    cursor = connection.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()
    airports.extend(result)
    cursor.execute(sql2)
    result = cursor.fetchall()
    airports.extend(result)
    #print(airports)
    for x in airports:
        print(f"{x[0]}, {x[2]}, {x[1]}")
        n = (x[3], x[4])
        deg.append(n)
    #print(deg)
    return deg

icao1 = input("1st airport's ICAO code: ")
icao2 = input("2nd airport's ICAO code: ")
deg = distanceBetween2Aiports(icao1, icao2)
deg1 = deg[0]
deg2 = deg[1]
print(f"Distance between this two airports is {distance.distance(deg1, deg2).km:.2f} km")
