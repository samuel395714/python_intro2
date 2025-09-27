passcode="dayo"
password=""
counter=0
while passcode !=password:
     print("enter your password")
     password=input()
     if password !=passcode:
          print("invalid password,please try again")
     else:
          continue
print("hurray you just entered the right password")