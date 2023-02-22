array1=[0,1,5,8,10,12]
array2=[2,3,69,99]

# to sort and merge two array we should compare two corresponding elements of two array.
def mergeSort(arr1,arr2):
    array=[]
    index_of_array1 = index_of_array2=0
    flag=0
    while not (index_of_array1 >=len(arr1) or index_of_array2 >= len(arr2)): # loop throught two array to the end
        print(arr1[index_of_array1],arr2[index_of_array2])
        if arr1[index_of_array1] <= arr2[index_of_array2]: # compare two elements and add the smaller element to new array
            array.append(arr1[index_of_array1])
            index_of_array1 +=1                             #increase the index by one after add to new array
        
        else:
            array.append(arr2[index_of_array2])
            index_of_array2 +=1
    
    if index_of_array1 == len(arr1): # check if either array1 or array2 was reach after finish the loop
        flag =1    # the flag will tell us which array reaching first
    if flag ==1:                    #if array1 reach first we will continue to go the second array.
        for i in arr2[index_of_array2:]:
                array.append(i)
    else:
        for j in arr1[index_of_array1:]:
                array.append(j)
    return array

print(mergeSort(array1,array2))




