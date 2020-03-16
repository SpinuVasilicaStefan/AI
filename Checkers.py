from copy import copy, deepcopy
def Display(matrice):
    for i in range(0, 8):
        print(i + 1, end="  ")
        for j in range(0, 8):
            print(matrice[i][j], end=" ")
        print()
    for i in range(0, 8):
        if i == 0:
            print(" ", end="  ")
        print(i + 1, end=" ")


def stare_initiala():
    matrice = []
    listapar = []
    listaimpar = []
    listaparcalculator = []
    listaimparcalculator = []
    lista = []
    for i in range(0, 8):
        lista = lista + ["0"]
        if i % 2 == 0:
            listapar = listapar + ["1"]
            listaimpar = listaimpar + ["0"]
        else:
            listapar = listapar + ["0"]
            listaimpar = listaimpar + ["1"]
    print(listapar)
    for i in range(0, 8):
        if i in [1, 7]:
            if i == 1:
                aux = listapar.copy()
                for j in range(0, len(aux)):
                    if aux [j] == "1":
                        aux [j] = "2"
                matrice = matrice + [aux.copy()]
            else:
                matrice = matrice + [listapar.copy()]
        elif i in [6, 0]:
            if i != 6:
                aux = listaimpar.copy()
                for j in range(0, len(aux)):
                    if aux [j] == "1":
                        aux [j] = "2"
                matrice = matrice + [aux.copy()]
            else:
                matrice = matrice + [listaimpar.copy()]
        else:
            matrice = matrice + [lista.copy()]
    return matrice

#matrice, n, m = stare_initiala()
#print(stare_initiala())
#print(Display(matrice, n, m))

def verificare_mutare(x,y, matrice):
    x = int(x)
    y = int(y)
    if x < 0 or y < 0 or x > 7 or y > 7:
        return False
    else:
        if int(matrice[x][y]) != 0:
            return False
        else:
            return True


def verificare_saritura(x, y, z, w, matrice, player):
    x = int(x)
    y = int(y)
    if x < 0 or y < 0 or x > 7 or y > 7:
        return False
    else:
        if int(matrice[x][y]) == 3 - player:
            #print("abracadabra")
            #print(x, y, z, w)
            if x > z:
                #print("***")
                if y > w:
                    if verificare_mutare(x + (x - z), y + (y - w), matrice) == True:
                        return True
                else:
                    if verificare_mutare(x + (x - z), y - (y - w), matrice) == True:
                        return True
            else:
                #print("***")
                print("Am intrat aci")
                if y > w:
                    if verificare_mutare(x + (x - z), y + (y - w), matrice) == True:
                        return True
                else:
                    if verificare_mutare(x + (x - z), y - (y - w), matrice) == True:
                        return True
            #print((x + (x - z),y + (y - w)), (x + (x - z),y - (y - w) ), (x - (x - z),y + (y - w) ), (x - (x - z), y + (y + w)))
    return False

def rezultat_saritura(x, y, z, w, matrice, player):
    x = int(x)
    y = int(y)
    if x < 0 or y < 0 or x > 7 or y > 7:
        return False

    else:
        if matrice[x][y] == 3 - player:
            print("abracadabra")
            #print(x, y, z, w)
            if x > z:
                #print("***")
                if y > w:
                    if verificare_mutare(x + (x - z), y + (y - w), matrice) == True:
                        return (x + (x - z), y + (y - w))
                else:
                    if verificare_mutare(x + (x - z), y - (y - w), matrice) == True:
                        return (x + (x - z), y - (y - w))
            else:
                #print("***")
                if y > w:
                    if verificare_mutare(x + (x - z), y + (y - w), matrice) == True:
                        return (x + (x - z), y + (y - w))
                else:
                    if verificare_mutare(x + (x - z), y - (y - w), matrice) == True:
                        return (x + (x - z), y - (y - w))

            #print((x + (x - z),y + (y - w)), (x + (x - z),y - (y - w) ), (x - (x - z),y + (y - w) ), (x - (x - z), y + (y + w)))
    return (-1, -1)



def verificare_piesa(x, y, matrice,player):
    x = int(x)
    y = int(y)
    if x < 0 or y < 0 or x > 7 or y > 7:
        return False
    else:
        #print(matrice[x][y])
        if int(matrice[x][y]) == int(player):
            if verificare_mutare(x - 1, y - 1, matrice) == False and verificare_mutare(x - 1, y + 1, matrice) == False:
                #print(x - 1, y + 1)
                #print(verificare_saritura(x - 1, y - 1, x, y, matrice, player))
                #print(verificare_saritura(x - 1, y + 1, x, y, matrice,player))
                if verificare_saritura(x - 1, y - 1, x, y, matrice, player) == True or verificare_saritura(x - 1, y + 1, x, y, matrice,player) == True:
                    return True
                return False
            else:
                return True
        else:
            return False


def rezultat_piesa(x, y, matrice,player):
    x = int(x)
    y = int(y)
    if x < 0 or y < 0 or x > 7 or y > 7:
        return (-1, -1)
    else:
        # print(matrice[x][y])
        if player == 1:
            if int(matrice[x][y]) == int(player):
                if verificare_mutare(x - 1, y - 1, matrice) == False and verificare_mutare(x - 1, y + 1, matrice) == False:
                    if verificare_saritura(x - 1, y - 1, x, y, matrice, player) == True:
                        return rezultat_saritura(x - 1, y - 1, x, y, matrice, player)
                    if verificare_saritura(x - 1, y + 1, x, y, matrice,player) == True:
                        return rezultat_saritura(x - 1, y + 1, x, y, matrice, player)
                    return (-1, -1)
                else:
                    if verificare_mutare(x - 1, y - 1, matrice) == True:
                        return (x - 1, y - 1)
                    elif verificare_mutare(x - 1, y + 1, matrice) == True:
                        return (x - 1, y + 1)
            else:
                return (-1, -1)
        else:
            if int(matrice[x][y]) == int(player):
                if verificare_mutare(x + 1, y + 1, matrice) == False and verificare_mutare(x + 1, y + 1, matrice) == False:
                    if verificare_saritura(x + 1, y - 1, x, y, matrice, player) == True:
                        return rezultat_saritura(x + 1, y - 1, x, y, matrice, player)
                    if verificare_saritura(x + 1, y + 1, x, y, matrice,player) == True:
                        return rezultat_saritura(x + 1, y + 1, x, y, matrice, player)
                    return (-1, -1)
                else:
                    if verificare_mutare(x + 1, y - 1, matrice) == True:
                        return (x + 1, y - 1)
                    elif verificare_mutare(x + 1, y + 1, matrice) == True:
                        return (x + 1, y + 1)
            else:
                return (-1, -1)



def modificare_matrice(z, w, x, y, matrice):
    if verificare_mutare(int(x) , int(y) , matrice) == True:

        matrice[x][y] = '2'
        matrice[z][w] = '0'
    else:
        tupla = rezultat_piesa(x, y, matrice, 1)
        if verificare_piesa(x, y, matrice, 1) == True:
            x = tupla[0] + 1
            y = tupla[1] + 1
    return  matrice


def verifica_stare_finala(matrice):
    player1 = 0
    player2 = 0
    for linie in range(0,8):
        for coloana in range(0,8):
            if matrice[linie][coloana] == '1':
                player1 = 1
            elif matrice[linie][coloana] == '2':
                player2 = 1
    if player1 == 0:
        print("Jucatorul 1 castiga!")
        return True
    elif player2 == 0:
        print("Jucatorul 2 castiga!")
        return True
    else:
        return False

def euristica(matrice):
    h = 0
    piese = 0
    for linie in range(0,8):
        for coloana in range(0,8):
            if matrice[linie][coloana] == '2':
                h += linie + 1
                piese += 1
    h += (8-piese) * 10
    return h


def mutare_calculator(matrice):
    xf = 0
    yf = 0
    xs = 0
    ys = 0
    mutare = deepcopy(matrice)
    maxim = 0
    matrice_max = []
    for i in range(0, 8):
        for j in range(0, 8):
            if int(matrice[i][j]) == 2:
                matrix = deepcopy(matrice)
                apel = deepcopy(matrice)
                if(euristica(modificare_matrice(i, j, i + 1, j - 1, apel))) > maxim:
                    maxim = euristica(modificare_matrice(i, j, i + 1, j - 1, matrix))
                    xs = i
                    ys = j
                    xf = i + 1
                    yf = j - 1
                matrix = deepcopy(matrice)
                apel = deepcopy(matrice)
                if (euristica(modificare_matrice(i, j, i + 1, j + 1, apel))) > maxim:
                    maxim = euristica(modificare_matrice(i, j, i + 1, j + 1, matrix))
                    xf = i + 1
                    yf = j + 1
                    xs = i
                    ys = j
    print(xs, ys, xf, yf)
    print(mutare)
    return  (xs, ys, xf, yf)



def joc():
    matrice = stare_initiala()
   # matrice[5][6] = 2
    while(verifica_stare_finala(matrice) == False):
        intrat = 0
        Display(matrice)
        print()
        print("Introduceti coordonatele piesey: ")
        flag = False
        while flag == False:
            print(" c1 = ", end=" ")
            c1 = input()
            print(" c2 = ", end=" ")
            c2 = input()
            flag = verificare_piesa(int(c1) - 1, int(c2) - 1, matrice, 1)
            if flag == False:
                print("Pozitie incorecta, introduceti din nou o pozitie")
                Display(matrice)
            else:
                matrice[int(c1) - 1][int(c2) - 1] = 0
        print("Introduceti o mutare: ")
        flag = False
        while flag == False:
            print(" x = ", end=" ")
            x = input()
            print(" y = ", end=" ")
            y = input()
            if verificare_mutare(int(x) - 1, int(y) - 1, matrice) == True:
                flag = True
            else:
                flag = False
                tupla = rezultat_piesa(x, y, matrice, 1)
                print("%%%%%%%%%%%%%%%")
                print(tupla)
                if verificare_piesa(x, y, matrice, 1) == True:
                    flag = True
                    intrat = 1
                    x = tupla[0] - 1
                    y = tupla[1] + 1
            #print(verificare_piesa(x, y, matrice, 1))
            if flag == False:
                Display(matrice)
                print("Pozitie incorecta, introduceti din nou o pozitie")
            else:
                print(x, y)
                if intrat == 1:
                    matrice[int(x)][int(y) - 2] = '1'
                else:
                    matrice[int(x) - 1][int(y) - 1] = '1'
                principala = deepcopy(matrice)
                print("**")
                print(principala)
                xs,ys,xf,yf = mutare_calculator(principala)
                print(matrice)
                matrice = modificare_matrice(xs,ys,xf,yf, matrice)





joc()
