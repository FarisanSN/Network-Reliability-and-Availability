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

def mode_select():
    global mode
    print("Masukkan Mode Kalkulator")
    print("1. Availability")
    print("2. Reliability")
    print("please input 1 or 2")
    mode = int(input())

    if mode!=1 and mode!=2:
        print("Masukan salah")
        mode_select()

def main():
    mode_select()
    if mode ==1:
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
    else:
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

main()