print("""
ROCK-PAPER-SCİSSORS
rock:R
paper:P
scissors:S
to quit:q
""")
listeq=["R","P","S"]
#your score
y=0
#PC's score
p=0
import random
while True:
    print("""your score:{} \nPC's score:{}""".format(y,p))
    x=input("your answer:") 
    k=random.choice(listeq)
    if x=="q":
        print("you have exited the game")
        break 
    else:         
        if x==k:
            print("draw")
            continue
        elif x=="P" and k=="S":
            print("PC wins")
            p+=1
        elif x=="P" and k=="R":
            print("you win")
            y+=1
        elif x=="S" and k=="P":
            print("you win")
            y+=1
        elif x=="S" and k=="R":
             print("PC wins")
             p+=1
        elif x=="R" and k=="P":
            print("PC wins")
            p+=1
        elif x=="R" and k=="S":
            print("you win")
            y+=1
        else:
            print("invalid answer")































