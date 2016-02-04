import re, sys
def verify():
   temp = 0
   pas = raw_input("Enter a password?")
   if(len(pas) < 6 or len(pas) > 16):
      temp=0
   elif not (re.search("[A-Z]",pas)):
      temp=0
   elif not (re.search("[a-z]",pas)):
      temp=0
   elif not (re.search("[0-9]",pas)):
      temp=0
   elif not (re.search("[$#@]",pas)):
      temp=0
   else:
      temp=1
   if(temp==1):
      print "Valid Password"
   else:
      print "Invalid Password"
verify()
      
