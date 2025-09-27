#A pie chart shows a woman’s  grocesories purchase in the market with the following
#yam(colour blue =35
#Cassave (color Red)=15
#Potatoes(color green)=20
#carrot(color green)=10
 #Groundnuts (color purple)= ?
#Write python code that determines the percentage left for groundnut
#Also 
#Write python code that determines the degree occupy by groundnut
def pie():
    yam=35
    CASSAVA=15
    Groundnut=0
    potatoes=20
    carrot=10
    total=yam+CASSAVA+carrot+Groundnut+potatoes
    Groundnut=100-total
    print(Groundnut)
    #calculating groundnut degree
    Groundnutdegree=Groundnut/100*360
    print(Groundnutdegree)
pie()


    