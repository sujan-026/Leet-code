n = 30
output = []

for i in range(1, n+1):
    if(i%3==0 and i%5==0):
        output.append("Fizz Buzz")
    elif(i%3==0):
        output.append("Fizz")
    elif(i%5==0):
        output.append("Buzz")
    else:
        output.append(str(i))
print(output)