from random import choice

def genMove(dot):
    if dot=="Northwest":
        move=choice(("North","Center","West"))
        return move
    elif dot=="North":
        move=choice(("Northwest","Northeast","East","Center","West"))
        return move
    elif dot=="Northeast":
        move=choice(("North","Center","East"))
        return move
    elif dot=="West":
        move=choice(("Northwest","North","Center","South","Southwest"))
        return move
    elif dot=="Center":
        move=choice(("North","Northeast","East","Southeast","South","Southwest","West"))
        return move
    elif dot=="East" :
        move=choice(("Northeast","North","Center","South","Southeast"))
        return move
    elif dot=="Southwest":
        move=choice(("West","Center","South"))
        return move
    elif dot=="South":
        move=choice(("Southwest","West","Center","Southeast","East"))
        return move
    elif dot=="Southeast":
        move=choice(("East","Center","South"))
        return move
for i in range(1,20):
    dot=input("Enter dot name: ")
    print(genMove(dot))
