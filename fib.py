def fib(number):
    previous = 0
    current = 1
    if number > 2:
        for i in range(number):
            saved_previous = previous
            previous = current 
            current += saved_previous
            print (current)
    else:
        print (current)
        



fib(5)
