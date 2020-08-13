def permute(s, alt):                    #have 2 inputs: orginal series and alternative series
    if s != []:                         #as long as the original series is not empty
        for e in s:                     #extract the element sequentially
            Next = list(s)              
            NextAlt = list(alt)         
            Next.remove(e)              #the selected element would be popped from the original series
            NextAlt.append(e)           #and joined into the alternative series
            permute(Next, NextAlt)      #then we can make it iteratively until the original series is empty
    else:                               #if the original series is empty
        print(alt)                      #then the alternative series would be printed as one of the results 
# main program
Num=int(input())                        #input the number
series=list(range(1,Num+1))             #make the series from the number
permute(series,[])                      #input the series and an empty list into the function