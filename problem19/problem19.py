#Counting Sundays
import calendar
def main():
    count = 0
    for year in range(1901,2001,1):
        for month in range(1,13,1):
            day = 1
            if calendar.weekday(year,month,day) == 6:
                count += 1
    print(count)
if __name__ == '__main__':
    main()
