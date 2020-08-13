import os
path = os.getcwd()                                              #get the current working directory
read_path = path + '/read_file_data'                            #search for the sub-directory
file_count = 0
summary = 0
for result in os.walk(read_path):                               #use os.walk to get all sub-directories
    if len(result[2]) != 0:                                     #the result is ["current_path","sub-directories","files"]
        for i in range(len(result[2])):                         
            subread_path = result[0] + '/' + result[2][i]       #make file paths
            Str = open(subread_path, encoding='Latin-1').read() #read the files
            if Str.find('value=') == 0:                         #if the file is "value=x.xxx"
                file_count += 1                                 #it would be valid and we would sum the value      
                value = Str.split('value=')
                summary += float(value[1])                      #find out the value and add it to the summary
            else:                                               #if the file is invalid
                print(subread_path)                             # we will return the path
print("number of valid files: ", file_count)                    #output the count of valid files
print("the sum is", summary)                                    #output the sum