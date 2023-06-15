# Escribe tu código aquí :-)
import pygame
import colores
import math

ANCHO = 1080
ALTO = 720
CENTRO = (ANCHO/2, ALTO/2)
NOMBRE = "Alejandro"

h = CENTRO[0]
k = CENTRO[1]
angulo=0

def movimiento(r, h, k, angulo):
    x= h + int(math.cos(angulo) * r)
    y= k + int(math.sin(angulo) * r)
    return x,y

VENTANA = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption(NOMBRE)

# r = radio del circulo
# h = coordenada x del entro del circulo
# k = coordenada y del centro del circulo
# angulo = punto de inicio del movomiento


print(colores.getColor("AMARILLO"))

#FUENTE = pygame.font,SysFont("comicsans",16)

VENTANA.fill(colores.getColor("NEGRO"))
SOL = pygame.draw.circle(VENTANA,colores.getColor("AMARILLO"),CENTRO,90)
PLANETA_1 = pygame.draw.circle(VENTANA,colores.getColor("AZUL"),(160,360),15)
PLANETA_2 = pygame.draw.circle(VENTANA,colores.getColor("ROJO"),(400,380),15)


pygame.display.update()

vel_angular = 0.01

x, y = movimiento(300,h,k, angulo)
angulo -= vel_angular

ejecuta = True
while ejecuta == True:
    x, y = movimiento(300,h,k, angulo)
    angulo -= vel_angular
    VENTANA.fill(colores.getColor("NEGRO"))
    SOL = pygame.draw.circle(VENTANA,colores.getColor("AMARILLO"),CENTRO,90)
    PLANETA_1 = pygame.draw.circle(VENTANA,colores.getColor("AZUL"),(x,y),30)
    PLANETA_2 = pygame.draw.circle(VENTANA,colores.getColor("ROJO"),(x,y),15)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            ejecuta= True

    pygame.display.update()

pygame.quit()
