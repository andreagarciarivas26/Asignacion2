#Tiene solo las funciones, si se desean ajecutar desde demo.py se ejecutan

PI = 3.141592653589793

#Área del circulo

def area_circulo(radio):
    area = PI * radio**2
    return area


#Área del rectangulo

def area_rectangulo(base, altura):
    area= base*altura
    return area


#Área de un triangulo

def area_triangulo(base,altura):
    area= (base*altura)/2
    return area



#Celsius a Farenheit


def temperature_c(celsius):
    farenheit=celsius*(9/5)+32
    return farenheit



# Farenheit a Celsius


def temperatura(farenheit):
    celsius_2=(farenheit-32)*(5/9)
    return(celsius_2)


#Promedio de tres numeros


def promedio(num1,num2,num3):
    x=(num1+num2+num3)/3
    return(x)


#Máximo de tres números

def maximo_tres(a, b, c):
    
    maximo = a

    if b > maximo:
        maximo = b

    if c > maximo:
        maximo = c

    return maximo


