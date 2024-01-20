class Automovel:
    def __init__(self, cor,marca, modelo , nr_portas, tipo_cambio ,  placa):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.nr_portas = nr_portas
        self.tipo_cambio = tipo_cambio
        self.placa = placa
        self.motor = False
        
    def lig_carro(self):    
        if (self.motor == True):
            print("O carro já esta ligado")
        else:   
            self.motor= True
        
        
    def deslig_carro(self):    
        self.motor= True
        
carro = Automovel("Branco","ford","fiesta", "2", "manual",  "eee1111" )   
print(carro.motor)
carro.lig_carro()
print(carro.motor)
carro.lig_carro()
print(carro.motor)

carro.deslig_carro()
print("teste " ,  carro.motor)




