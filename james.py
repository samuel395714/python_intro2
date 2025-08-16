#Mr James just died and his properties  worth $92000  
# but he owe a debt of $20000,
#  the balance was divided among his children in the ratio 1:3:4
#Write a python code that determines who got the highest and  and who got the least print it out
p=92000
debt=20000
balance=p-debt
print(balance)
ratio=1+3+4
highest=4/ratio*balance
print(highest)

lowest=1/ratio*balance
print(lowest)