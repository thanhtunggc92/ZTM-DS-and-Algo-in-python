class Array():
    def __init__(self):
        self.length=0
        self.data={}


    def __str__(self):
        return str(self.__dict__)


    def get(self,index):
        return self.data['index']
    def push(self,item):
        self.length +=1
        self.data[self.length -1] = item
        
        return self.data
    
    def pop(self):
        lastitem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -=1
        return lastitem    
    def delete(self,index):
        for item in range(index,self.length-1):
            self.data[item] = self.data[item+1]         #shift item from the given index to the end of dictionary

        del self.data[self.length-1]                    #delete the dulicate element at the end of the array.
        self.length -=1                                 # update the length of the array. length decreasing by 1

    def insert(self,index,item):
        self.length +=1
        for i in range(self.length-1, index,-1):         
            self.data[i]= self.data[i-1]                 # backward loop from the end of the array to the given index.
        self.data[index]=item                             # add new element to the array.


myarr = Array()
myarr.push(6)
myarr.push('hi')
myarr.push(8)
myarr.delete(1)
# myarr.pop()
myarr.insert(1,'love')
myarr.insert(2,'you')
myarr.insert(3,3000)
print(myarr)


