a=list(map(int,input().split(","))) #input a
b=list(map(int,input().split(","))) #input b
common=[i for i in a if i in b]     #check all elements in a if appears in b
print(common)