
mem= {}

def fib(x):
    if x in mem:
        return mem[x]
    elif x ==0 or x ==1:
        return 1
    else:
       result = fib(x-1) + fib(x-2)
       mem[x] = result
       return result



while True:
    try:
       x = int(input('enter number: '))
       y = fib(x)
       print(y)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
