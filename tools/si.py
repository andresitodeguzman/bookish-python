#
# Get dates easily
# Andresito M. de Guzman
#
import datetime

def fullMonth(i):
	jan = "January"
	feb = "February"
	mar = "March"
	apr = "April"
	may = "May"
	jun = "June"
	jul = "July"
	aug = "August"
	sep = "September"
	oct = "October"
	nov = "November"
	dec = "December"
	if(i==""):
		return 0
	elif(i==1):
		return jan
	elif(i==2):
		return feb
	elif(i==3):
		return mar
	elif(i==4):
		return apr
	elif(i==5):
		return may
	elif(i==6):
		return jun
	elif(i==7):
		return jul
	elif(i==8):
		return aug
	elif(i==9):
		return sep
	elif(i==10):
		return oct
	elif(i==11):
		return nov
	elif(i==12):
		return dec
	else:
		return 0

def date(param):
	m = datetime.datetime.now().month
	mon = fullMonth(m)
	d = datetime.datetime.now().day
	y = datetime.datetime.now().year
	h = datetime.datetime.now().hour
	m = datetime.datetime.now().minute
	s = datetime.datetime.now().second
	x = " "
	d = "-"
	c = ":"
	cm = ","
	
	if(param == ""):
		return mon+x+d+cm+x+y+x+h+c+m+c+s
	elif(param == "m"):
		return m
	elif(param == "d"):
		return d
	elif(param == "y"):
		return y
	elif(param == "h"):
		return h
	elif(param == "m"):
		return m
	elif(param == "s"):
		return s
	else:
		return 0