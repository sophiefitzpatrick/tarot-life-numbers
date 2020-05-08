# A quick way to calculate your life path number,
# your personal year number and to check whether
# you have a master number (not everyone does)
# interpret your findings here: https://www.numerology.com/about-numerology/single-digit-numbers
# note: if you have a master number this combines with your life path number and overrides it

def split(number_string):
    return [int(n) for n in number_string]

def personal_year_number_calculator(day, month, year):
	# call this with your day and month of birth and whichever year you wish to know about
	# personal years cycle 1 to 9
	reduced_number = reduce_date(day, month, year)

	if reduced_number in range(1,9):
		print("Your Personal Year Number is %s" % reduced_number)
	else:
		return print("error")

def life_path_number_calculator(day, month, year):
	# call this with your date of birth for your Life Path Number
	# this number will never change, it will be with you forever
	# if your life path number is 2, 4 or 6, you will also have a Master Number
	reduced_number = reduce_date(day, month, year)

	if reduced_number in range(1,9):
		print("Your Life Path Number is %s" % reduced_number)
		if reduced_number in [2,4,6]:
			half_reduced_number = reduced_number/2
			master_number = "%s%s" % (int(half_reduced_number), int(half_reduced_number))
			print("Your Master Number is %s" % master_number)
	else:
		return print("error")

def reduce_date(day, month, year):
	day_str = str(day)
	month_str = str(month)
	year_str = str(year)

	if len(day_str) == 2:
		day_list = split(day_str)
		day_result = day_list[0] + day_list[1]
		if len(str(day_result)) == 2:
			day_list = split(str(day_result))
			day_result = day_list[0] + day_list[1]
	elif len(day_str) == 1:
		day_result = day
	else:
		return print("error")

	if len(month_str) == 2:
		month_list = split(month_str)
		month_result = month_list[0] + month_list[1]
		if len(str(month_result)) == 2:
			month_list = split(str(month_result))
			month_result = month_list[0] + month_list[1]
	elif len(month_str) == 1:
		month_result = month
	else:
		return print("error")

	if len(year_str) == 4:
		year_list = split(year_str)
		year_result = year_list[0] + year_list[1] + year_list[2] + year_list[3]
		if len(str(year_result)) == 2:
			year_list = split(str(year_result))
			year_result = year_list[0] + year_list[1]
	else:
		return print("error")

	full = day_result + month_result + year_result

	if len(str(full)) == 1:
		reduced_result = full
	elif len(str(full)) == 2:
		reduced_list = split(str(full))
		reduced_result = reduced_list[0] + reduced_list[1]

	return reduced_result

life_path_number_calculator(day, month, year) # enter your birth date | day, month, year
personal_year_number_calculator(day, month, year) # enter your birth date and the year you want to know about | day, month, year
