############################################ PREGUNTA 2
text="Lorem ipsum"
list=["Lorem","ipsum"]

def pregunta1():
    print(text.split(sep=" "))
    print(" ".join(list))
    print(text.count("ipsum"))
    print(text.find("ipsum"))
    print(text.upper())
    print(text.lower())

pregunta1()

############################################ PREGUNTA 3
def pregunta2():
    print(number*2)
    print(number/5)
number=int(input("Ingrese un número: "))

pregunta2()

############################################ PREGUNTA 4
class producto:
    def __init__(self,nombre,marca,expire,medida):
        self.nombre= nombre
        self.marca= marca
        self.expire= expire
        self.medida= medida
        print("Se ha agregado un producto:",self.nombre)
    def __str__(self):
        return '{}, {} - {}'.format(self.nombre,self.marca, self.medida)       
class catalogo:
    product=[]
    def __init__(self, product=[]):
        self.product=product
    def agregar(self,p):
        self.product.append(p)
    def mostrar(self):
        for p in self.product:
            print(p)

p=producto("Filtro hidráulico","TECFIL","No expira","Estándar")
c=catalogo([p])

c.agregar(producto("Batería", "ACDELCO","2025","Estándar"))
c.mostrar()

############################################ PREGUNTA 5
def sumatoria(a):
    print("La suma refrectiva es", a + sumatoria(a-1))

def divide(c,d):
    print("La división es ", c/d)


############################################ PREGUNTA 6


############################################ PREGUNTA 7
class PRODUCTO:
    def __init__(self,PAIS,LOTE,AÑO):
        self.PAIS= PAIS
        self.LOTE= LOTE
        self.AÑO= AÑO
        print("El lote número ", self.LOTE, "se ubica en ", self.PAIS)
 
codigo=(input("Digite el número de serie: "))
c_1=codigo.split(sep="-")
a=PRODUCTO(c_1[0],c_1[1],c_1[-1])

############################################
