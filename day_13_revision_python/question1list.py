# Create an Empty List

# Write a program to:   

# Create an empty list.
# Ask the user to enter 5 numbers.
# Store them in the list.
# Print the final list.


mylst = []

while True:

    for i in range(1,6):
        
        try:
            userinp = int(input("Enter 5 numbers"))
            if userinp == "exit":
                print("Thanks for using the code bye bye...")
                exit()
            mylst.append(userinp)
            if i == 5:
                large = 0
                for i in mylst:
                    if i >= large:
                        large = i

                lstsum = 0
                for i in mylst:

                    lstsum += i 
            
        except Exception as e:
            print("Please enter the valid number only")
            continue
    print(f"Final list is {mylst}")
    print(f"This is the Sum of the list {lstsum}")
    print(f"The largest number of the list is {large}")
    exit()

            



