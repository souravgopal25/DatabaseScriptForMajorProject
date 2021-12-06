from connect import connect
postgres_insert_query = """ INSERT INTO flight(flight_no, carrier_name, flight_model, seat_capacity) VALUES (%s,%s,%s,%s)"""
count1=0.0
def putFlightData(conn, flightNo, carrierName, flightModel, seatCapacity):
    try:
        cur = conn.cursor()
        record_to_insert = (flightNo, carrierName, flightModel, seatCapacity)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()
        global count1
        count1 = count1 + cur.rowcount
    except:
        return



def driverFunction(conn:connect,intialSeries:str,carrierName:str,flightModel:str,seatCapacity:int):
    for i in range(1,21):
        for j in range(1,21):
            if i!=j:
                flightNo=intialSeries+str(i)+str(j)
                putFlightData(conn,flightNo,carrierName,flightModel,seatCapacity)





if __name__ == '__main__':
    conn=connect()
    #driverFunction(conn,'6E','INDIGO','A320',180)
    print(count1)
    #driverFunction(conn,'I5','Air Asia','A320',180)
    print(count1)
    driverFunction(conn,'AI','Air India','A320',180)
    print(count1)

