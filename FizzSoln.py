#my somewhat solution to the fizzbuzz challenge from Hackerrank.


#defining the func, contains all the if-else statements regarding the parameters.
def fizzbuzz(n):
    if n%3 == 0 and n%5 ==0:
        print("FizzBuzz")
    elif n%3 == 0 and n%5 != 0:
        print("Fizz")
    elif n%3 != 0 and n%5 ==0:
        print("Buzz")
    else:
        print(n)
      
#loop for continous input.   
while True:
    n = input()
    if n.lower() == 'exit': #snuck this to exit from the infinite loop.
        break
      
#exception handling
    try:
        n = int(n)
    except ValueError:
        print("enter a number dude!")
        continue #restart the loop
      
#calling my defined function 
    fizzbuzz(n)
