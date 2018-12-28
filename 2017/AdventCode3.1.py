number = int(input("Number to be searched: "))

magic = int(number**0.5) + 1 #Calculo do altura do quadrado perfeito
square = magic*magic    #Quadrado perfeito onde o input está incluído
height = (magic-1)//2   #Calculo da distancia desde o centro até a um lado do quadrado

mod = number % magic    #Posição do input no lado do quadrado
if  mod < height:       # |--------x--|         x = posição do input no lado do quadrado
    difference = height - mod + 1 #
elif mod > height:      # |--x--------|         o objetivo é saber a distancia que vai de x ao centro do lado do quadrado
    difference = mod - height - 1   
else:                   # |-----x-----|         x está mesmo ao centro do lado do quadrado
    difference = 0


distance = difference + height
#distance = abs(height - mod + 1) + height

print("magic ", magic)
print("square ", square)
print("height ", height)
print("difference ", difference)
print("distance ", distance)
