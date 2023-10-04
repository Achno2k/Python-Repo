import random
names=["eureka","ultimate","exodus","servant"]
name=random.choice(names)
fname=name
l=len(name)

'''     Creating a list with underscored       '''
lname=[]
for i in range(l):
    lname.append("_")
gname=""

lives = l
while(lives!=0):
    if(name!=gname):
        for x in lname:
            print(x,end=" ")
        print("")
        inp=input("enter a letter ")
        if(inp in fname):
            for j in range(l):
                if(inp==fname[j]):
                    lname[j]=fname[j]
                    fname=list(fname)
                    fname[j]=" "
                    fname="".join(fname)
            
            gname="".join(lname)
        else:
            lives-=1
            print(f"you have {lives} lives left.")
            pass
    else:
        for x in lname:
            print(x,end=" ")
        print("")
        print("+------------------+")
        print("|                  |")
        print("|                  |")
        print("|    You won !!    |")
        print("|                  |")
        print("|                  |")
        print("+------------------+")
        break
        
# print(fname) '''prints the remaining letters or say the solution'''

'''     printing the list       '''
# for x in lname:
#     print(x,end="")

if(lives==0):
    print("+------------------+")
    print("|                  |")
    print("|                  |")
    print("|    You lost !!   |")
    print("|                  |")
    print("|                  |")
    print("+------------------+")
