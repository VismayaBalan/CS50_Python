
months =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
   date = input("Date: ")
   try:
      month,day,year = date.split('/')
      if 0<int(month)<13:
         if 1<=int(day)<=31:
            print(f"{int(year)}",end="-")
            print(f"{int(month):02}",end = "-")
            print(f"{int(day):02}",end="")
            print("")
            break
      else:
         continue

   except ValueError:
      try:
         month,day,year = date.split()
         if month in months:
            if 1<=int(day[:-1])<=31:
               month_num = months.index(month)+1
               print(year,end='-')
               print(f"{int(month_num):02}",end = "-")
               print(f"{int(day[:-1]):02}")
               print("")
               break
      except ValueError:
         date = input("Date: ")







