import datetime

if __name__ == "__main__":
	t = datetime.time(5, 25, 1)
	print(t)
	print("")

	print("datetime.time.min:", datetime.time.min)
	print("datetime.time.max:", datetime.time.max)
	print("datetime.time.resolution:", datetime.time.resolution)
	print("")

	today = datetime.date.today()
	print("Today:", today)
	print("Today:", today.timetuple())
	print("datetime.date.min:", datetime.date.min)
	print("datetime.date.max:", datetime.date.max)
	print("datetime.date.resolution:", datetime.date.resolution)
	print("")

	d1 = datetime.date(2019, 1, 31)
	d2 = d1.replace(year=1990)
	print("d1", d1)
	print("d2", d2)
	delta = d1 - d2
	print("d1 - d2:", delta)
	print("Num days", (d1 - d2).days)
