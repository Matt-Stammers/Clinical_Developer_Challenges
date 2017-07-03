# My Version
def bed_day_calculator(n, x):
	"""Function will Calculate Bed Days."""
	if n == 0:
	    return 0
	elif n < 3:
	    return n * x + 1
	elif n < 8:
	    return (n * x) * 2
	else:
	    return (n * x) * 3
	
Total = bed_day_calculator(1, 240) + bed_day_calculator(2, 143) + bed_day_calculator(3, 490) + bed_day_calculator(4, 136) + bed_day_calculator(5, 59) + bed_day_calculator(6, 90) + bed_day_calculator(7, 20) + bed_day_calculator(8, 137) + bed_day_calculator(13, 70) + bed_day_calculator(15, 36) + bed_day_calculator(25, 26)
print(Total)

# Stefan Mitrosinovic's Version
"""
Calculating bed days.

Calculate the number of bed days depending on how
long patients have already been in the hospital.
"""


def bedDaysCalc(d):
    """Calculator for how many bed days the patient is expected to stay."""
    if d == 0:
        return 0
    elif d < 3:
        return d + 1
    elif d < 8:
        return d * 2
    else:
        return d * 3


print "Bed days calculator."
print "Please follow the instructions and only input numbers."

bedDays = 0
while True:
    try:
        print "Please input the number of days the patients have been in the hospital:"
        day = input(">")
        dayNum = abs(int(day))
        print "How many patients have been in the hospital for %d %s?" % (dayNum, "days" if dayNum > 1 else "day")
        num = input(">")
        patientNum = abs(int(num))
        bedDays = bedDays + bedDaysCalc(dayNum) * patientNum
        print "Given this snapshot, we expect %d bed days to be required" % bedDays
    except ValueError:
        print "Please type a number"
