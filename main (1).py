#leap year
" " " "

#defining a function
def isleapyear(year):
   if (year%4==0 and year%100!=0):
       return True
   else:
       return False
year=int(input ("enter a year:"))
if isleapyear(year):
    print('{}is a leap year.'.format(year))
else:
   print('{} is not a leap year.'.format(year))