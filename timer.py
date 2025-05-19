seconds=int(input("enter time"))
mode=str(input("enter wether fast or slow"))
while seconds!=0:
    if mode=="fast":
        print(f"there are {seconds} left")
        seconds=seconds-2
    else:
        print(f"there are {seconds} left")
        seconds=seconds-1
print("timer done")