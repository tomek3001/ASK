
class Register(object):
    def __init__(self, name):
        self.name = name
        self.dataL = [0] * 8
        self.dataH = [0] * 8

    def Read(self, addr, is_high):
        if is_high == 'H':
            return self.dataH[addr]
        else:
            return self.dataL[addr]

    def Write(self, addr, data, is_high):
        if is_high == 'H':
            self.dataH[addr] = data
        else:
            self.dataL[addr] = data

    def Show(self):
        for (i, j) in zip(self.dataH, self.dataL):
            if i != 0:
                print(1)

    def ShowRange(self, start, end):
        addr = start
        while addr <=end:
            print(addr, ": ", self.Read(addr, True))
            print(addr, ": ", self.Read(addr, False))

    def getName(self):
        return self.name
    '''
    destination i sourece podawane są w formie RAH,RBL itd. co oznacza rejestr z którego pobieramy oraz
    rejestr docelowy. Ostatnia litera oznacza czy tyczy się to części wyższej czy niższej Obecnie funkcjonalność polega
    na zamianie całych wartości, znak # jako źródło pozwala na wpisanie wartości matematycznej do liczby. Pod spodem 
    wrzuciłem kilka zakomentowanych przykładów
    '''
def copy_paste(source, destination):
    source = list(source)
    destination = list(destination)
    if source[0] == 'R':
        name_s = source[1] + 'X'
        if destination[0] == 'R':
            name_d = destination[1] + 'X'
            for i in range(8):
                rejestry[name_d].Write(i,rejestry[name_s].Read(i, source[2]), destination[2])
    elif source[0] == "#":
        if destination[0] == 'R':
            name_d = destination[1] + 'X'
            value = int("".join(map(str, source[1:])))
            if value <= 255:
                value = list('{0:08b}'.format(value))
                for i in range(8):
                    rejestry[name_d].Write(i, value[i], destination[2])
            else:
                print("Out of range")



rejestry = {"AX":0, "BX":1, "CX":2, "DX":3}

rejestry["AX"] = Register("A")
rejestry["BX"] = Register("B")
rejestry['CX'] = Register("C")
rejestry['DX'] = Register("D")

''' Przykład 1
for i in range(8):
    print(rejestry['AX'].Read(i, "H"), end=", ")
copy_paste('#258', 'RAH')
for i in range(8):
    print(rejestry['AX'].Read(i, "H"), end=', ')
'''

''' Przykład 2
for i in range(8):
    print(rejestry['AX'].Read(i, "H"), end=", ")
copy_paste('RAH', 'RCL')
for i in range(8):
    print(rejestry['CX'].Read(i, "L"), end=', ')
'''







