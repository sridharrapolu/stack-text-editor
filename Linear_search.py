class Linear_search:
    def __init__(self,arr):
        self.arr=arr
    
    def search(self,data):
        for i in range(len(self.arr)):
            if self.arr[i]==data:
                print(data,"Item found at:",i," Index",end=" ")
                return
        print("data index not found")


arr=[1,2,3,4,55,2,3]
find=Linear_search(arr)
find.search(55)

#FOR LINEAR SEARCH NO NEED OF SORTING THE DATA COZ IT FOLLOWS BRUIT FORCE TECHNIQUE WHICH IS TAVERSING THROUGH EACH ELEMET AND COMPARING FOR THE RESULT
#TIME COMPLEXITY IS O(N)
#SLOWER, IT WONT HELP WITH LARGER DATA