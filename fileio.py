f= open("poem.txt")
c=f.read()
if("twinkle" in c):
    print("present")
print(c)
f.close()