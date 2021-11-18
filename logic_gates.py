#Created 11/08/21

def AND (a,b): #AND GATE
        if a==1 and b==1:
                return 1
        else:
                return 0

def OR (a,b): #OR GATE
        if a==1 or b==1:
                return 1
        else:
                return 0

def NOT (a):
        if a==0:
                return 1
        else:
                return 0


def NAND (a,b):
        if(a==1 and b==1):
                return 0
        else:
                return 1



def NOR (a,b):
        if a==0 and b==0:
                return 1
        else:
                return 0


def XOR (a,b):
        if a != b:
                return 1
        else:
                return 0

def XNOR (a,b):
        if a == b:
                return 1
        else:
                return 0


if __name__ == '__main__':
        print(NAND(0, 0))
        print(NAND(0, 1))
        print(NAND(1, 0))
        print(NAND(1, 1))
        print(XNOR(AND(OR(NAND(0,1),1)),1),0)

        print("+---------------+----------------+")
        print(" | XNOR Truth Table   | Result |")
        print(" A = False, B = False | A XNOR B =", XNOR(False, False), " | ")
        print(" A = False, B = True  | A XNOR B =", XNOR(False, True), " | ")
        print(" A = True, B = False  | A XNOR B =", XNOR(True, False), " | ")
        print(" A = True, B = True   | A XNOR B =", XNOR(True, True), " | ")

        print("+---------------+----------------+")
        print(" | A*B+B Truth Table             | Result |")
        print(" A = False, B = False, C = False | A AND B OR C =", OR(AND(False, False), False), " | ")
        print(" A = False, B = False, C = True  | A AND B OR C =", OR(AND(False, False), True), " | ")
        print(" A = False, B = True, C = False  | A AND B OR C =", OR(AND(False, True), False), " | ")
        print(" A = False, B = True, C = True   | A AND B OR C =", OR(AND(False, True), True), " | ")
        print(" A = True, B = False, C = False  | A AND B OR C =", OR(AND(True, False), False), " | ")
        print(" A = True, B = False, C = True   | A AND B OR C =", OR(AND(True, False), True), " | ")
        print(" A = True, B = True, C = False   | A AND B OR C =", OR(AND(True, True), False), " | ")
        print(" A = True, B = True, C = True    | A AND B OR C =", OR(AND(True, True), True), " | ")