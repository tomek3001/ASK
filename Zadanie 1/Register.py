
class Register(object):
    def __init__(self, name):
        self.name = name
        self.dataL = [0] * 8
        self.dataH = [0] * 8

    def Read(self, addr, size=1, is_high="H"):
        if is_high == 'H':
            return self.dataH[addr:(addr+size)]
        else:
            return self.dataL[addr:(addr+size)]

    def Write(self, addr, data, size=1,is_high="H"):
        if isinstance(data, int): data = [data]
        if is_high == 'H':

            self.dataH[addr:addr+size] = data
        else:
            self.dataL[addr:addr+size] = data

    def Show(self):
        for (i, j) in zip(self.dataH, self.dataL):
            if i != 0:
                print(1)

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
                rejestry[name_d].Write(i, rejestry[name_s].Read(i, source[2]), destination[2])
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


def add(source, destination, adding=True):
    source = list(source)
    destination = list(destination)
    name_d = destination[1] + 'X'
    if source[0] == 'R':
        name_s = source[1] + 'X'
        if destination[0] == 'R':
            name_d = destination[1] + 'X'
            binary1 = "0b" + "".join([str(number) for number in
                                 rejestry[name_d].Read(0, size=8, is_high=destination[2])])
            binary2 = "0b" + "".join([str(number) for number in
                                      rejestry[name_s].Read(0, size=8, is_high=destination[2])])
            if adding: binary_sum = bin(int(binary1, 2) + int(binary2, 2)).split("b")[1]
            else:  binary_sum = bin(int(binary1, 2) - int(binary2, 2)).split("b")[1]
            accum = list(map(int, binary_sum[-9:]))
            rejestry[name_d].Write(0, accum, size=8, is_high=destination[2])
    elif source[0] == "#":
        name_d = destination[1] + 'X'
        binary1 = "0b" + "".join([str(number) for number in
                                  rejestry[name_d].Read(0, size=8, is_high=destination[2])])
        value = int("".join(map(str, source[1:])))
        binary2 = "0b" + '{0:08b}'.format(value)
        if not adding and int(binary1,2) < int(binary2,2):
            print("Out of range, program is not executing negative numbers")
        else:
            if adding: binary_sum = '{0:08b}'.format(int(binary1, 2) + int(binary2, 2))
            else: binary_sum = '{0:08b}'.format(int(binary1, 2) - int(binary2, 2))
            accum = list(map(int, binary_sum[-9:]))
            rejestry[name_d].Write(0, accum, size=8, is_high=destination[2])

rejestry = {"AX":0, "BX":1, "CX":2, "DX":3}

rejestry["AX"] = Register("A")
rejestry["BX"] = Register("B")
rejestry['CX'] = Register("C")
rejestry['DX'] = Register("D")
accum = [0]*8

# Przykład dodawanie
for i in range(8):
    if i != 3 and i != 5:
        rejestry["AX"].Write(i, 1, size=1, is_high="H")
rejestry["BX"].Write(7, 1, is_high="H") # 7 to najmniej znaczący bit
#print(rejestry["AX"].Read(0, 8))
print(rejestry["BX"].Read(0,8))
add("#121", "RBH", adding=True)
print(rejestry["BX"].Read(0,8))

''' #Przykład odejmowanie
for i in range(8):
    if i != 3 and i != 5:
        rejestry["AX"].Write(i,1,is_high="H")
rejestry["BX"].Write(7, 1, is_high="H") # 7 to najmniej znaczący bit
add("RBH", "RAH", adding=False)
'''

''' #Przykład 1
for i in range(8):
    print(rejestry['AX'].Read(i, "H"), end=", ")
copy_paste('#258', 'RAH')
for i in range(8):
    print(rejestry['AX'].Read(i, "H"), end=', ')
'''

''' #Przykład 2
for i in range(8):
    print(rejestry['AX'].Read(i, "H"), end=", ")
copy_paste('RAH', 'RCL')
for i in range(8):
    print(rejestry['CX'].Read(i, "L"), end=', ')
'''







