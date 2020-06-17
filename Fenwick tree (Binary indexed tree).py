class BinaryIndexedTree(object):
    def __init__(self,d):
        self.Data=d
        self.lenData=len(self.Data)
        self.BIT=[0] * (self.lenData+1)
        self.InitilizeBIT()
    
    def LowBit(self,x):
        return x&(-x)
    
    def InitilizeBIT(self):
        for i,d in enumerate(self.Data):
            self.BIT[i+1]=self.Data[i]
        for x in range(1,len(self.BIT)):
            y=x+self.LowBit(x)
            if y <= self.lenData:
                self.BIT[y]+=self.BIT[x]

    def Query(self,x):
        sumQuery=0
        i=x
        while i > 0 :
            sumQuery+=self.BIT[i]
            i-=self.LowBit(i)
        return sumQuery
    
    def Update(self, index, val):
        i=index
        while i <= self.lenData:
            self.BIT[i]+=val
            i+=self.LowBit(i)
        
BIT=BinaryIndexedTree([ x for x in range(1,11)])
assert 15==BIT.Query(5)
assert 21==BIT.Query(6)
assert 6==BIT.Query(3)
assert 1==BIT.Query(1)
assert 55==BIT.Query(10)
BIT.Update(1,1)
assert 16==BIT.Query(5)
assert 22==BIT.Query(6)
assert 7==BIT.Query(3)
assert 2==BIT.Query(1)
BIT.Update(9,-10)
assert 36==BIT.Query(9)
assert 46==BIT.Query(10)

BIT=BinaryIndexedTree([ 1 for x in range(1,11)])
assert 1==BIT.Query(1)
assert 5==BIT.Query(5)
assert 10==BIT.Query(10)
BIT.Update(6,1)
assert 11==BIT.Query(10)
assert 5==BIT.Query(5)





