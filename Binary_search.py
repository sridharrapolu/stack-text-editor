class Binary_search:

    def __init__(self,arr):
        self.arr=sorted(arr)
        

    def search(self,low,high,item):
        if low<=high:
            #search
            mid=(low+high)//2
            
            if self.arr[mid]==item:
                print('item is mid',mid)
                return 
            elif self.arr[mid]>item:
                 self.search(low,mid-1,item)
            else:
                 self.search(mid+1,high,item)
        else:
            print("item not found")

arr=[1,2,3,4,5,6,77]
bs=Binary_search(arr)
bs.search(0,len(arr)-1,77)

