import pandas as pd
import argparse
import datetime

parser = argparse.ArgumentParser(description='Data required for pico&placa prediction') #argparse allows to enter the values from the terminal
parser.add_argument('--plate',  type=str, required=True, help='plate number')
parser.add_argument('--date',  type=str, required=True, help='date that apply')
parser.add_argument('--time',  type=str, required=True, help='time that apply')

def pp_day(date)->int:
    temp = pd.Timestamp(date)
    num_day = temp.dayofweek 
    
    return num_day #A number between 0 to 6, 0=Monday

def time_in_range(start, end, x)->bool:
    #Return true if x is in the range [start, end]
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def pp_hour(time)->bool:
    start1 = datetime.time(7, 0, 0)
    end1 = datetime.time(9, 30, 0)
    start2 = datetime.time(16, 0, 0)
    end2 = datetime.time(19, 30, 0)
    if (int(time[0:2])<12):
        return(time_in_range(start1, end1, datetime.time(int(time[0:2]), int(time[3:5]), int(time[6:8]))))
    else:
        return(time_in_range(start2, end2, datetime.time(int(time[0:2]), int(time[3:5]), int(time[6:8]))))

def pp_plate(plate)->int:

    if int(plate[-1]) == 1 or int(plate[-1]) == 2:
	    return 0
    elif int(plate[-1]) == 3 or int(plate[-1]) == 4:
	    return 1
    elif int(plate[-1]) == 5 or int(plate[-1]) == 6:
	    return 2
    elif int(plate[-1]) == 7 or int(plate[-1]) == 8:
	    return 3
    elif int(plate[-1]) == 9 or int(plate[-1]) == 0:
	    return 4

def main():

    global args
    args = parser.parse_args()
    plate = args.plate
    time = args.time
    date = args.date


    day=pp_day(date)

    plate_day=pp_plate(plate)

    pp_time=pp_hour(time)

    if (pp_time==True) and (day<=4):
        if day==plate_day:
            print ('Does not circulate')
        else:
            print ('Circulate')
    else:
        print('Free circulate')

if __name__ == "__main__":
    main()

