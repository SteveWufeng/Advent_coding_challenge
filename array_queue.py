import arrays

class Queue:

    __slots__ = ['__front', '__back', '__size', '__array']

    def __init__ (self, capacity = 3):
        self.__array = arrays.Array (capacity)
        self.__front = 0
        self.__back = 0
        self.__size = 0

    def __resize (self):
        new_array = arrays.Array (len (self.__array) * 2 + 1)
        i = self.__front
        j = 0
        for _ in range (self.__size):
            new_array [j] = self.__array [i]
            i = (i + 1) % len (self.__array)
            j += 1

        self.__front = 0
        self.__back = j
        self.__array = new_array

    def __repr__ (self):
        string = ''
        i = self.__front
        while i != self.__back:
            string += str (self.__array [i]) + ', '
            i = (i + 1) % len (self.__array)

        return string [:-2] 
        
    def is_empty (self):
        return self.__size == 0

    def size (self):
        return self.__size

    def enqueue (self, value):
        self.__array [self.__back] = value
        self.__back = (self.__back + 1) % len (self.__array)
        self.__size += 1

        if self.__back == self.__front:
            self.__resize ()

    def dequeue (self):
        if self.__size <= 0:
            raise IndexError ("Cannot dequeue from an empty queue")

        value = self.__array [self.__front]
        self.__front = (self.__front + 1) % len (self.__array)
        self.__size -= 1

        return value