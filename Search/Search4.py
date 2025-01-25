class Data:
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

class Hash:
    def __init__(self, tSize, maxColl, threShold):
        self.tSize = tSize
        self.maxColl = maxColl
        self.threshold = threShold
        self.duplTable = list()
        self.table = [None for i in range(tSize)]
    
    def rehashTsize(self,n:int):
        n *= 2
        while True:
            factorial, n = 0, n+1
            for i in range(2, n):
                factorial += 1 if n%i==0 else 0
                if factorial>1:
                    break
            if factorial == 0:
                break
        return n 

    def rehashResize(self):
        self.tSize = self.rehashTsize(self.tSize)
        self.table = [None for i in range(self.tSize)]
    
    def rehashInsert(self) -> None:
        for i in self.duplTable:
            bIdx = idx = i%self.tSize
            coll = 0
            while self.table[idx]:
                coll+=1
                print(f"collision number {coll} at {idx}")
                if coll == self.maxColl:
                    break
                idx = (bIdx+coll**2)%self.tSize
            if not self.table[idx]:
                self.table[idx] = i

    def insert(self, val: int) -> None:
        print(f"Add : {val}")
        b_idx = idx = val%self.tSize
        coll = 0
        while self.table[idx]:
            coll += 1
            print(f"collision number {coll} at {idx}")
            if coll == self.maxColl:
                print("****** Max collision - Rehash !!! ******")
                self.rehashResize() or self.rehashInsert()
                idx = val%self.tSize
                break
            idx = (b_idx+(coll**2))%self.tSize 
        self.duplTable.append(val)
        if len(self.duplTable)*100/self.tSize >= self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehashResize() or self.rehashInsert()
        else:
            self.table[idx] = Data(val)

    def __str__(self):
        s = str()
        for i,val in enumerate(self.table):
            s += f"#{i+1}	{val}\n"
        return s + "----------------------------------------"

def main():
    print(" ***** Rehashing *****")
    inp = input("Enter Input : ").split('/')
    tSize, maxColl, threShold = int(inp[0].split()[0]),int(inp[0].split()[1])\
        ,int(inp[0].split()[2])
    hash = Hash(tSize,maxColl,threShold)
    print("Initial Table :")
    print(hash)
    for i in inp[1].split():
        hash.insert(int(i)) or print(hash)
