def time_convertion():
    time = "07:05:45PM"

    hh,mm,ss = map(int,time[:-2].split(":"))

    if time[-2:] == "PM" and hh != 12:
        hh += 12
    elif time[-2:] == "AM" and hh == 12:
        hh =0
    
    result= "{:02d}:{:02d}:{:02d}".format(hh,mm,ss)

    return result
final = time_convertion()
print(final)
