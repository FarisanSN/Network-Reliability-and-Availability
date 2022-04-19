def init_avail():
    global pom, neft, ttr, tt, wmct
    pom = float(input("Period of Measurement: "))
    neft = float(input("Network Element Failure Trace: "))
    ttr = float(input("Time to Repair: "))
    tt = float(input("Testing Time: "))
    wmct = float(input("waiting, Movement, & Coordination Time: "))

    if pom<0 or neft<0 or ttr<0 or tt<0 or wmct<0 :
        print("Masukkan Variable dengan Benar!")
        init_avail()

def init_relia():
    global hi, eo, rtu, riu, ats, dr
    hi = float(input("Hi: "))
    eo = float(input("Encoding Overhead: "))
    rtu = float(input("Rtu: "))
    riu = float(input("Riu: "))
    ats = float(input("Average Transmission Speed: "))
    dr = float(input("Data Rate: "))

    if (rtu<0 or rtu>1) or (riu<0 or riu>1):
        print("Variable Rtu dan/atau Riu tidak valid")
        init_relia()

def init_delivery():
    global send, receive
    receive = float(input("Time received the message: "))
    send = float(input("Time sends the message: "))

    if send<0 or receive<0 or send>receive:
        print("Masukan salah")
        init_delivery()

def init_nonacces():
    global unsucces, allatt
    unsucces = int(input("Unsuccesful message attempts: "))
    allatt = int(input("All message attempts: "))
    
    if unsucces<0 or allatt<0 or allatt<unsucces:
        print("Masukan salah")
        init_nonacces()


def mode_select():
    global mode
    print("Masukkan Mode Kalkulator")
    print("1. Availability")
    print("2. Reliability")
    print("3. End-to-end delivery time")
    print("4. Message Service Non-accessibility")
    print("please input 1, 2, 3 or 4")
    mode = int(input())

    if mode!=1 and mode!=2 and mode!=3 and mode!=4:
        print("Masukan salah")
        mode_select()

def main():
    mode_select()
    if mode==1:
        init_avail()

        global dt, availability, qual_avail
        dt = neft+ttr+tt+wmct
        availability = (1-(dt/pom))*100

        if availability>=99:
            qual_avail = "Very Good"
        elif 99>availability>=90:
            qual_avail = "Fairly Good"
        elif 90>availability>=60:
            qual_avail = "Enough"
        elif 60>availability>=40:
            qual_avail = "Poor"
        else:
            qual_avail = "Bad"
        
        print("Availability: ", availability, "%")
        print("Quality: ", qual_avail)
    if mode==2:
        init_relia()

        global oec, ho, trans_time, te, qual_relia
        oec = dr/ats
        ho = hi/(1-hi)
        te = 1/((1+rtu)*(1+riu))
        trans_time = (dr*(1+ho)*(1+eo))/(ats*te)

        if te>=0.99:
            qual_relia = "Very Good"
        elif 0.90>te>=0.99:
            qual_relia = "Fairly Good"
        elif 0.90>te>=0.60:
            qual_relia = "Enough"
        elif 0.60>te>=0.40:
            qual_relia = "Poor"
        else:
            qual_relia = "Bad"

        print("Operational Effective Capacity: ", oec)
        print("Handling Overhead: ", ho)
        print("Transaction Time: ", trans_time)
        print("Throughput Efficiency: ", te)
        print("Quality: ", qual_relia)

    if mode==3:
        init_delivery()

        global delivery_time, qual_delivery
        delivery_time = receive - send

        if delivery_time<=5:
            qual_delivery = "Very Good"
        elif 5<delivery_time<=10:
            qual_delivery = "Fairly Good"
        elif 10<delivery_time<=30:
            qual_delivery = "Enough"
        elif 30<delivery_time<=60:
            qual_delivery = "Bad"
        else:
            qual_delivery = "Poor"

        print("Message end-to-end Delivery Time in seconds: ", delivery_time)
        print("Quality: ", qual_delivery)

    else: #mode==4
        init_nonacces()

        global non_access, qual_nonaccess

        non_access = unsucces/allatt*100

        if non_access<=1:
            qual_nonaccess = "Very Good"
        elif 1<non_access<=5:
            qual_nonaccess = "Fairly Good"
        elif 5<non_access<=15:
            qual_nonaccess = "Enough"
        elif 15<non_access<=30:
            qual_nonaccess = "Bad"
        else:
            qual_nonaccess = "Poor"

        print("Message Service Non-Accessibility (%): ",non_access,"%")
        print("Quality: ", qual_nonaccess)

main()