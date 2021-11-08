def double(n):
    # n is a PARAMETER that is used within the function DEFINITION.
    # a PARAMETER is a placeholder for inpute data that gets processed by our functions
    return n * 2

usertring = input("Number please...")
usernum = int(userstring, 10)

print(double(usernum))
      # usernum is passes as an ARGUMENT to the double() function CALL.
      # an ARGUMENT is a placeholder for a real value that gets PASSED into a function call.
      # line 18 order: 1. usernum is evaluated; 2. double() is evaluated; 3. console.log() is evaluated.
