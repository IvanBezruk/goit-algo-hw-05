def caching_fibonacci():
    #Create a dictionary to save Fibonacci values
    cache ={}
    
    #Computes the n-th Fibonacci number with caching
    def fibonacci(n):
        
        #Task cases
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        #Check if value was already added to cache
        if n in cache:
            return cache[n]
        
        #Save data to cache
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    
    return fibonacci

#Test the implementation
fib = caching_fibonacci()

print(fib(10))
print(fib(15))