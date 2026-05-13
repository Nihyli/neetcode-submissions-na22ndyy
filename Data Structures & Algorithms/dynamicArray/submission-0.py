class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        if self.size > 0:
            # soft delete the last element
            self.size -= 1
        # return the popped element
        return self.array[self.size]
 

    def resize(self) -> None:
        newArr = [None] * (self.capacity*2)
        for i in range(self.size):
            newArr[i] = self.array[i]
        self.array = newArr
        self.capacity *= 2



    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
