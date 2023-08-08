w=int(input('Enter your weight : '))
i=input('Enter L for pounds or K for kilos : ')

if i.upper()=="L":
    print(w//0.45,'pounds')
elif i.upper()=="K":
    print(w*0.45,'kilos')
    
