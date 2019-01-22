def main():
    #exercise1()
    #exercise2()
    #exercise3()
    #bonus()


#EXERCISE1
#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Hint: Use 'continue' statement.
#Expected Output : 0 1 2 4 5
def exercise1():
    for num in range(0,7):
        if(num == 3 or num == 6):
            continue
        print(num)
###########################################################################################################
#EXERCISE2
#Write a Python program to count the number of even and odd numbers from a series of numbers.
#Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#Expected Output :
#Number of even numbers : 5
#Number of odd numbers : 4

def exercise2():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    odd_num = 0
    even_num = 0
    for num in numbers:
        if not(num%2 == 0):
            even_num+=1
        else:
            odd_num+=1
    print("The number of even number is",even_num)
    print("The number of odd number is",odd_num)
###########################################################################################################
#EXERCISE3
#Write a Python program that accepts a sequence of lines (blank line to terminate)
# as input and prints the lines as output after User enters a blank line to end.
#Do not use an array to hold the lines of text
#Hints: You can use "\n" if you want to add a line break between sentences
def exercise3():
    sequence = ""



###########################################################################################################
#Bonus:
#Write a Python program to construct the following pattern, using a nested for loop.
def bonus():
    for num in range(1,10):
        if(num == 1):
            print("*")
        elif (num == 2):
            print("**")
        elif (num == 3):
            print("***")
        elif (num == 4):
            print("****")
        elif (num == 5):
            print("*****")
        elif (num == 6):
            print("****")
        elif (num == 7):
            print("***")
        elif (num == 8):
            print("**")
        elif (num == 9):
            print("*")
        else:
            print(" ")
###########################################################################################################
if __name__ == '__main__':
    main()