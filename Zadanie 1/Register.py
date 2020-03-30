
class Register():
    def __init__(self, baseAddr):
        self.baseAddr = baseAddr
        self.data = [0] * 16

    def Read(self, addr):
        return self.data[addr-self.baseAddr]

    def Write(self, addr, data):
        self.data[addr-self.baseAddr] = data

    def Show(self):
        addr = self.baseAddr
        for i in self.data:
            if i!=0:
                print(hex(addr), ": ", hex(i))

    def ShowRange(self, start, end):
        addr = start
        while addr <=end:
            print(addr, ": ", self.Read(addr))
            
