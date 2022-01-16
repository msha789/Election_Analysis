# Initial variable to track game play
user_play = "y"
start_num = 0

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    usern = int(input("How many numbers?: "))

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(start_num, usern + start_num):
       print(x + 1)

        # Print each number in the range
    start_num = usern + start_num

    # Once complete...
    
    user_play = input("Continue: (y)es or (n)o? ")