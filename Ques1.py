import calendar
def count_monday():
   count = 0
   for yyyy in range(2015,2017):
      for mm in range(1,13):
         if(calendar.weekday(yyyy,mm,01)==0):
            count=count+1
   print count      
   

count_monday()   
