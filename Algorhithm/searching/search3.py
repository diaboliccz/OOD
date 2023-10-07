class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, size, max_chain):
        self.size = size
        self.max_chain = max_chain
        self.table = [None] * size
    
    def hashing(self, key):
        sum_val = sum(ord(i) for i in str(key))
        return sum_val % self.size
    
    def checkTableFull(self):
        return None not in self.table
    
    def put(self, key, value):
        index = self.hashing(key)
        if self.table[index] is None:
            self.table[index] = Data(key, value)
        else:
            for i in range(self.max_chain):
                index = (self.hashing(key) + i**2) % self.size
                if self.table[index] is None:
                    self.table[index] = Data(key, value)
                    break
                print(f"collision number {i+1} at {index}")
                if i == self.max_chain - 1:
                    print("Max of collisionChain")
                    return

        return

    def get(self, key):
        index = self.hashing(key)
        if self.table[index] is None:
            return None
        elif self.table[index].key == key:
            return self.table[index]
        else:
            for i in range(self.max_chain):
                index = (index + i**2) % self.size
                if self.table[index] is None:
                    return None
                elif self.table[index].key == key:
                    return self.table[index]
        return None
    
    def printTable(self):
        for i in range(len(self)):
            print(f"#{i+1}\t{self.table[i]}")
        print("-"*27)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.table)

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.get(key) is not None

    def isFull(self):
        return None not in self.table

    def __bool__(self):
        return self.isFull()

    def __iter__(self):
        for i in range(self.size):
            yield self.table[i]

    def __reversed__(self):
        for i in range(self.size - 1, -1, -1):
            yield self.table[i]

    def __add__(self, other):
        return self.size + other.size

def main():
    print(" ***** Fun with hashing *****")
    inp = input("Enter Input : ").split("/")
    table_size = int(inp[0].split()[0])
    max_chain = int(inp[0].split()[1])
    table = Hash(table_size, max_chain)

    data_list = inp[1].split(",")
    data_list = [i.split() for i in data_list]
    
    for i in data_list:
        if table.checkTableFull():
            print("This table is full !!!!!!")
            return
        table[i[0]] = i[1]
        table.printTable()


if __name__ == "__main__":
    main()