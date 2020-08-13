x=list(map(float,input().split(",")))   #input the Xs from the pairs
y=list(map(float,input().split(",")))   #input the Ys from the pairs
n=len(x)                                #check number of data pairs
x.append(x[0])                          #append the first X to the list
y.append(y[0])                          #append the first Y to the list

# we could calculate the area of the convex polygon from vertex pairs
# in triangle, the area would be the half of | X(0)    Y(0) | value.
#                                            | X(1)    Y(1) |
#                                            | X(2)    Y(2) |
#                                            | X(0)    Y(0) |
area=0
for i in range(n):                      #n=3, range(n)=[0,1,2],after the appending would be [0,1,2,0]
    area += (x[i]*y[i+1]-y[i]*x[i+1])
print(area/2)