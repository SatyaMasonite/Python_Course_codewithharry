# f= open("poem.txt")
# c=f.read()
# if("twinkle" in c):
#     print("present")
# print(c)
# f.close()

# with open("poem.txt") as f:
#     val=f.read()
#     print(val)
import random;

def game():
    score = random.randrange(1,62)
    print(score)

    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore==''):
            hiscore=int(0)
        else:
            hiscore=int(hiscore)
        # print(hiscore)

    if (score>hiscore):
        hiscore=score
    with open("hiscore.txt","w") as f:
        f.write(str( hiscore))
    return hiscore

game()