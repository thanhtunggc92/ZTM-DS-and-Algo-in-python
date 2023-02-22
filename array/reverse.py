# normal way
def reverse(string):
    reverse_string=[]
    for i in range(len(string)-1,-1,-1):  # loop the string backward from the last item to the beginning
        print(i)
        reverse_string.append(string[i])  # add all the iterate item to a list
    return "".join(reverse_string)        # convert a list to a string using join

str= "linh tran"
# print(reverse(str))

def reverse2(str):
    new_string= reversed(str)
    return ''.join(new_string)
            
# print(reverse2(str))
#use build in function
string='alibaba'
# re_list= list(string)
# re_list.reverse()
# print(''.join(re_list))
#slice a string
new_string= string[::-1]
print(new_string)


