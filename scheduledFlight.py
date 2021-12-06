import psycopg2

from connect import connect

scheduleFlightNo = 1
postgres_insert_query = """ INSERT INTO scheduled_flight(schedule_flight_id, available_seats, date, flight_flight_no, schedule_schedule_id)
VALUES (%s,%s,%s,%s,%s)"""
postgresFlighCheck = """SELECT * FROM flight WHERE flight_no=%s"""
postgresScheduleCheck = """SELECT * FROM schedule WHERE schedule_id=%s"""
count1 = 200


def putScheduleFlight(conn: connect, scheduleFlightNo: int, availableSeat: int, date: str, flghtNo: str,
                      scheduleNo: str):
    try:
        curr = conn.cursor()
        record_to_insert = (scheduleFlightNo, availableSeat, date, flghtNo, scheduleNo)
        curr.execute(postgres_insert_query, record_to_insert)
        conn.commit()
        global count1
        count1 += curr.rowcount
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        return


def driverFunction(conn: connect, intialSeries: str, availableSeat: int, date: str):
    global scheduleFlightNo
    for i in range(1, 21):
        for j in range(1, 21):
            if (i != j):
                flightScheduleNumber = intialSeries + str(i) + str(j)
                scheduleFlightNo = scheduleFlightNo + 1
                if (check(conn, flightScheduleNumber) == False):
                    putScheduleFlight(conn, scheduleFlightNo, availableSeat, date, flightScheduleNumber,
                                      flightScheduleNumber)


def check(conn: connect, scheduleFlightNo):
    curr = conn.cursor()
    curr.execute(postgresFlighCheck, (scheduleFlightNo,))
    res1 = curr.fetchone() is not None
    if curr.rowcount > 0:
        return False
    curr.execute(postgresScheduleCheck, (scheduleFlightNo,))
    if curr.rowcount > 0:
        return False
    return True


if __name__ == '__main__':
    conn = connect()
    # print(check(conn,"I5581"))
    driverFunction(conn, '6E', 180, '07/12/2021')
    scheduleFlightNo += 200
    driverFunction(conn, 'I5', 180, '07/12/2021')
    scheduleFlightNo += 200
    driverFunction(conn, 'AI', 180, '07/12/2021')
    scheduleFlightNo += 200
    driverFunction(conn, '6E', 180, '08/12/2021')
    scheduleFlightNo += 200
    driverFunction(conn, 'I5', 180, '08/12/2021')
    scheduleFlightNo += 200
    driverFunction(conn, 'AI', 180, '08/12/2021')
    scheduleFlightNo += 200
    driverFunction(conn, '6E', 180, '09/12/2021')
    scheduleFlightNo += 200
    driverFunction(conn, 'I5', 180, '09/12/2021')
    scheduleFlightNo += 200
    driverFunction(conn, 'AI', 180, '09/12/2021')
    scheduleFlightNo += 200
    driverFunction(conn, '6E', 180, '10/12/2021')
    scheduleFlightNo += 200
    driverFunction(conn, 'I5', 180, '10/12/2021')
    scheduleFlightNo += 200
    driverFunction(conn, 'AI', 180, '10/12/2021')
    print(count1)
