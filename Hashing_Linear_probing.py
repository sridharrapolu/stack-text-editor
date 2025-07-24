class dict:
    def __init__(self,size):
        self.size=size
        self.hash_table=[]*size

    #simple hash function to get hash fun for given key
    def hash_function(self,key):
        return key% self.size
    
    def insert(self,key):
        index=self.hash_function(key)

        if self.hash_table is not None:
            self.hash_table[index]=key
        else:
            print(f"Collision occurred for key {key} at index {index}. Trying linear probing...")

            current_index=index
            while self.hash_table[index] is not None:
                index=(index+1)%self.size
                if index==current_index:
                    print("hash table is full")
            return 

        




        