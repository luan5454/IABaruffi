import math
class vetorPadrao:
    def __init__(self, X, Y, Anterior, Distancia):
        self.X = X;
        self.Y = Y;
        self.Anterior = Anterior;
        self.Distancia = Distancia;
    
    
class buscarLabirinto:    
    def __init__(self, corpo, inicio, fim, tamanho):
        self.corpo = corpo;
        self.inciox = inicio[0]
        self.incioy = inicio[1]
        self.fimx = inicio[0]
        self.fimy = inicio[1]
        self.tamanhox = tamanho[0]
        self.tamanhoy = tamanho[1]
        self.vetorAberto = []
        self.vetorFechado = []
        
        
        self.vetorAberto.append(vetorPadrao(5, 3, 3, 3))
        self.vetorAberto.append(vetorPadrao(6, 3, 3, 3))
        self.vetorAberto.append(vetorPadrao(3, 1, 3, 3))
        self.vetorAberto.append(vetorPadrao(1, 2, 3, 3))
        
        self.vetorFechado.append(vetorPadrao(1, 2, 3, 3))
        self.vetorFechado.append(vetorPadrao(3, 4, 3, 3))
        self.vetorFechado.append(vetorPadrao(2, 1, 3, 3))
        self.vetorFechado.append(vetorPadrao(8, 7, 3, 3))
        
    def verificarDistanciaXY(self, x,y,x0,y0):
        dist = math.sqrt(
            math.fabs(math.pow(x-x0, 2)) +
            math.fabs(math.pow(y-y0, 2))
            ) 
        return round(dist,3);
    
    def verificarExistenciaVetorAberto(self,x,y):
        for i in self.vetorAberto:
            if(i.X == x) and (i.Y == y):
               return True
        return False
    
    def verificarExistenciaVetorFechado(self,x,y):
        for i in self.vetorFechado:
            if(i.X == x) and (i.Y == y):
               return True
        return False
    
#------CORPO PRINCIPAL

corpo = [[1,1,1,1,0,1,1,1],
         [1,0,0,0,0,1,1,1],
         [1,1,1,1,0,1,1,1],
         [1,1,1,1,1,1,1,1]]

tamanho = [3,7]

inicio = [0,0]

final = [0,7]

chamada = buscarLabirinto(corpo, inicio, final, tamanho)

#----------------AREA DE TESTE--------------


print(chamada.verificarExistenciaVetorAberto(6, 3))
print(chamada.verificarExistenciaVetorAberto(9, 3))
print(chamada.verificarExistenciaVetorFechado(3, 4))
print(chamada.verificarExistenciaVetorFechado(10, 3))