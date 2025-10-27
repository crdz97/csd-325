beer_song.py

def sing_bottles_of_beer(bottles):
    #Function to count down bottles of beer on the wall.
    for i in range(bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            #i minus one for the next line, singular or plural bottle
            print(f"Take one down and pass it around, {i-1} {'bottle' if i-1 == 1 else 'bottles'} of beer on the wall.\n")
        else:
            #when there's only one bottle left
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down and pass it around, no more bottles of beer on the wall!\n")

# Main Program
try:
    #input number of bottles
    total_bottles = int(input("Enter the number of bottles of beer on the wall: "))
    #Check for valid input
    if total_bottles <= 0:
        print("Please enter a number greater than 0!")
    else:
        #Once at 0, print the final lines
        sing_bottles_of_beer(total_bottles)
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more!")
except ValueError:
    print("Invalid input! Please enter a number.")

