#The project is about finding dates in inputed text
import re
import time
data=input('enter your text here:')
pattern_to_find=list(re.finditer("\d{1,2}-\w{1,3}-\d{2,4}",data))
if(len(pattern_to_find)>0):
  print("The dates in given text are:")
  for date in pattern_to_find:
    print(date.group())
    time.sleep(1)
else:
  print("There are no dates in the given text")
  time.sleep(1)
