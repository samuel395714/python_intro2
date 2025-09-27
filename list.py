list=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
#print(list)
#for loop
total=0
for i in list:
    #print(i)
    #print(sum(list))
    total=total+i
print(total)
if total>770:
     print("it is greater than 770")
     newtotal=total*3
     print(newtotal)  
else:
    print("it is not greater than 770")
    newtotal=total-500
    print(newtotal)
    
    