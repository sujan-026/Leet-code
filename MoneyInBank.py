#Find the richest customer
#ij represents the amt of money
#i is the customer
#j represents the bank

accounts = [[1,5],[7,3],[3,5]]

sum = 0
a = []

for i in range(0, len(accounts)):
    #print(i)
    sum = 0
    for j in accounts[i]:
        #print(j)
        sum =  sum + j

    a.append(sum)

    print(i+1,"customer has wealth =", sum)
print("customer is the richest with a wealth of", max(a))