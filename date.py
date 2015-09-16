#1. list all datetime from start to end:
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)
#code example:
if __name__ == '__main__':
	start_date = date(2013, 9, 6)
	end_date = date(2013, 9, 9)
	for single_date in daterange(start_date, end_date):
	    print namePart = single_date.strftime("%Y-%m-%d")
	    #list all the 2013-09-06/2013-09-07/2013-09-08
