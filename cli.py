l=[]
def addt(d):
    l.append(d)
    print("task added")
def removet(s):
    l.remove(s)
    print("task removed")
def viewt():
    if l:
        for i,o in enumerate(l,1):
            print(f"{i}.{o}")         
def main():
    while True:
        print("1.add task,2.remove task,3.view task,4.exit")
        n=int(input())
        if n==1:
            d=input("enter task : ")
            addt(d)
        elif n==2:
            s=input("enter task to be removed : ")
            removet(s)
        elif n==3:
            viewt()
        elif n==4:
            print("exit")
            break
        else:
            print("invalid number")
if __name__=="__main__":
    main()         

         
        