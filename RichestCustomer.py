sum = 0
a = []
accounts = [[1,2,3],[3,2,1]]

for i in range(0, len(accounts)):
    #print(i)
    sum = 0
    for j in accounts[i]:
        #print(j)
        sum =  sum + j

    a.append(sum)

    #print(i+1,"customer has wealth =", sum)
print("Customer is the richest with a wealth of", max(a))
#print(max(a))