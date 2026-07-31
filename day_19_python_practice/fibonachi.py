num = 50
turn1 = True
fiblst = []
for i in range(1,51):
    
    if turn1 == True:
        fiblst.append(0)
        fiblst.append(1)
        turn1 = False
    
    if turn1 == False:
        seclast, last = fiblst[-2], fiblst[-1]
        next = seclast + last
        if next >num:
            print(f"This is the Fib Series in range: {fiblst}")
            exit()
        fiblst.append(next)
print(fiblst)





