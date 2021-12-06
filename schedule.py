import psycopg2

from connect import connect
from AirportData import getAirportData
import random

min=5000
max=7500
list=['08:00','10:00','12:00','14:00','16:00','18:00','20:00','22:00']
postgres_insert_query = """ INSERT INTO schedule(schedule_id, arrival_time, departure_time, max_price, min_price, dstn_airport_airport_code, src_airport_airport_code)
VALUES (%s,%s,%s,%s,%s,%s,%s)"""
count1=0.0

def putScheduleToDB(conn:connect,scheduleId:str,arrivalTime:str,
                    departureTime:str,maxPrice:int,minPrice:int,
                    dstnAirport:str,srcAirport:str):
    try:
        cur=conn.cursor()
        record_to_insert=(scheduleId,arrivalTime,departureTime,maxPrice,minPrice,dstnAirport,srcAirport)
        cur.execute(postgres_insert_query,record_to_insert)
        conn.commit()
        print(cur.rowcount)
        global count1
        count1+=cur.rowcount
    except:
        return



def driverFunction1(conn:connect,airportList:list,intialSeries:str):
    l=len(airportList)
    for i in range(l):
        for j in range(l):
            if i != j:
                scheduleID=intialSeries+str(i+1)+str(j+1)
                departurTime,arrivalTime=getTime()
                dstnAirport=getAirport(i,airportList)
                srcAirport=getAirport(j,airportList)
                n=random.randint(100,700)
                putScheduleToDB(conn,scheduleID,arrivalTime,departurTime,max+n,min-n,dstnAirport,srcAirport)




def getAirport(index:int,airportList):
    return airportList[index]['code']
def getTime():
    n=random.randint(0,6)
    return (list[n],list[n+1])





if __name__ == '__main__':
    conn=connect()
    conn.close()
    conn=connect()
    airPortList=getAirportData()
    #driverFunction1(conn,airPortList,'6E')
    print(count1)
    #driverFunction1(conn,airPortList,'I5')
    print(count1)
    driverFunction1(conn,airPortList,'AI')
    print(count1)
