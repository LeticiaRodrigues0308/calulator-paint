# primeira etapa: o usuários irá informar as medidas e quantidade de janelas e portas. 

larguraP1 = float(input("Digite a largura da primeira parede: "))
alturaP1 = float(input("Digite a altura da primeira parede: "))
janP1 = int(input("Digite a quantidade de janelas da priemira parede: "))
portaP1 = int(input("Digite a quantidade de portas da primeira parede: "))


larguraP2 = float(input("Digite a largura da segunda parede: "))
alturaP2 = float(input("Digite a altura da segunda parede: "))
janP2 = int(input("Digite a quantidade de janelas da segunda parede: "))
portaP2 = int(input("Digite a quantidade de portas da segunda parede: "))

larguraP3 = float(input("Digite a largura da terceira parede: "))
alturaP3 = float(input("Digite a altura da terceira parede: "))
janP3 = int(input("Digite a quantidade de janelas da terceira parede: "))
portaP3 = int(input("Digite a quantidade de portas da terceira parede: "))

larguraP4 = float(input("Digite a largura da quarta parede: "))
alturaP4 = float(input("Digite a altura da quarta parede: "))
janP4 = int(input("Digite a quantidade de janelas da quarta parede: "))
portaP4 = int(input("Digite a quantidade de portas da quarta parede: "))

# segunda etapa: fase em que pego as informações que o usuário disponibiizou e faço os cálculos necessários.

# calculando a área das janelas e portas:
areaJanela = 2.00 * 1.20;
janTotalP1 = areaJanela * janP1
janTotalP2 = areaJanela * janP2
janTotalP3 = areaJanela * janP3
janTotalP4 = areaJanela * janP4

areaPorta = 0.80 * 1.90;
portaTotalP1 = areaPorta * portaP1
portaTotalP2 = areaPorta * portaP2
portaTotalP3 = areaPorta * portaP3
portaTotalP4 = areaPorta * portaP4

# Decisao em que a parede precisa ser 30cm maior que a porta:

if portaP1 >= 1:
    if alturaP1 >= 2.20:
        print("Tamanho de porta correta!")
    else:
        print("A altura da parede precisa ser 30cm maior que a altura da porta!")

if portaP2 >= 1:
    if alturaP2 >= 2.20:
        print("Tamanho de porta correta!")
    else:
        print("A altura da parede precisa ser 30cm maior que a altura da porta!")

if portaP3 >= 1:
    if alturaP3 >= 2.20:
        print("Tamanho de porta correta!")
    else:
        print("A altura da parede precisa ser 30cm maior que a altura da porta!")

if portaP4 >= 1:
   if alturaP4 >= 2.20:
        print("Tamanho de porta correta!")
   else:
        print("A altura da parede precisa ser 30cm maior que a altura da porta!")


# Calculando a área das paredes:
p1 = larguraP1 * alturaP1;
p2 = larguraP2 * alturaP2;
p3 = larguraP3 * alturaP3;
p4 = larguraP4 * alturaP4;


# Decisao de houver janela ou porta:

if janP1 >= 1:
    resultJanP1 = janTotalP1;
else: 
    resultJanP1 = 0
if janP2 >= 1: 
    resultJanP2 = janTotalP2;
else: 
    resultJanP2 = 0
if janP3 >= 1: 
    resultJanP3 = janTotalP3;
else: 
    resultJanP3 = 0
if janP4 >= 1:
    resultJanP4 = janTotalP4;
else: 
    resultJanP4 = 0

if portaP1 >= 1:
    resultPortaP1 = portaTotalP1;
else:
    resultPortaP1 = 0
if portaP2 >= 1:
    resultPortaP2 = portaTotalP2;
else:
    resultPortaP2 = 0
if portaP3 >=1:
    resultPortaP3 = portaTotalP3;
else:
    resultPortaP3 = 0
if portaP4 >= 1:
    resultPortaP4 = portaTotalP4;
else:
    resultPortaP4 = 0

# Somando se houver porta e janela
varP1 = resultPortaP1 + resultJanP1 
varP2 = resultPortaP2 + resultJanP2 
varP3 = resultPortaP3 + resultJanP3 
varP4 = resultPortaP4 + resultJanP4 

# Calculando a porcentagem da área da parede
porcentP1 = p1/2
porcentP2 = p2/2
porcentP3 = p3/2
porcentP4 = p4/2

# Se houver porta e janela, deve ocupar no máximo 50%

calcP1 = 0 
calcP2 = 0 
calcP3 = 0 
calcP4 = 0 

if varP1 <= porcentP1:
    calcP1 = p1 - varP1
else:
    print("A área das portas e janelas são inválidos!")

if varP2 <= porcentP2:
    calcP2 = p2 - varP2
else:
    print("A área das portas e janelas são inválidos!")

if varP3 <= porcentP3:
    calcP3 = p3 - varP3
else:
    print("A área das portas e janelas são inválidos!")

if varP4 <= porcentP4:
    calcP4 = p4 - varP4
else:
    print("A área das portas e janelas são inválidos!")
    

# Resultado da área das paredes:
if p1 >= 1 and p1 <= 15:
    print("Primeira parede: ",p1,"m²")
else:
    print("Valor inválido!")

if p2 >= 1 and p2 <= 15:
    print("Segunda parede: ",p2,"m²")
else:
    print("Valor inválido!")

if p3 >= 1 and p3 <= 15:
    print("Terceira parede: ",p3,"m²")
else:
    print("Valor inválido!")

if p4 >= 1 and p4 <= 15:
    print("Quarta parede: ",p4,"m²")
else:
    print("Valor inválido!")


# Calculo final de quantos litros de tinta o usuário vai precisar:
cobertTinta = 5
lata1 = 0.5
lata2 = 2.5
lata3 = 3.6
lata4 = 18

somaParedes = calcP1 + calcP2 + calcP3 + calcP4

latas = somaParedes/cobertTinta

if latas <= 1:
    print("Você vai precisar de ",lata1,"l + ",lata1,"l de tinta.")
elif latas > 1 and latas <= 1.5:
    print("Você vai precisar de ",lata2,"l de tinta.")
elif latas >= 2 and latas < 2.5:
    print("Você vai precisar de ",lata2,"l de tinta.")
elif latas > 2.3 and latas <= 3:
    print("Você vai precisar de ",lata2,"l + ",lata1,"l de tinta.")
elif latas > 3 and latas <= 3.5:
    print("Você vai precisar de ",lata3,"l de tinta.")
elif latas > 3.3 and latas <= 4:
    print("Você vai precisar de ",lata3,"l + ",lata1,"l de tinta.")
elif latas > 4 and latas <= 4.5:
    print("Você vai precisar de ",lata2,"l + ",lata2,"l de tinta.")
elif latas >= 5 and latas <= 5.5:
    print("Você vai precisar de ",lata2,"l + ",lata2,"l de tinta.")
elif latas < 5.3 and latas <= 6:
    print("Você vai precisar de ",lata3,"l + ",lata2,"l de tinta.")
elif latas > 6 and latas <= 6.5:
    print("Você vai precisar de ",lata3,"l + ",lata2,"l + ",lata1,"l de tinta.")
elif latas > 6.3 and latas <=7:
    print("Você vai precisar de ",lata3,"l + ",lata3,"l de tinta.")
elif latas > 7 and latas <= 7.5:
    print("Você vai precisar de ",lata3,"l + ",lata3,"l + ",lata1,"l de tinta.")
elif latas > 7.3 and latas <= 8:
    print("Você vai precisar de ",lata3,"l + ",lata2,"l + ",lata2,"l de tinta.")
elif latas > 8 and latas <= 8.6:
    print("Você vai precisar de ",lata3,"l + ",lata2,"l + ",lata2,"l de tinta.")
elif latas > 8.3 and latas <= 9:
    print("Você vai precisar de ",lata3,"l + ",lata3,"l + ",lata2,"l de tinta.")
elif latas > 9 and latas <= 9.3:
    print("Você vai precisar de ",lata3,"l + ",lata3,"l + ",lata2,"l de tinta.")
elif latas > 9.3 and latas <= 10:
    print("Você vai precisar de ",lata4,"l de tinta.")
elif latas > 10 and latas <= 10.3:
    print("Você vai precisar de ",lata4,"l de tinta.")
elif latas > 10.3 and latas <= 11:
    print("Você vai precisar de ",lata4,"l de tinta.")
elif latas > 11.3 and latas <= 12:
    print("Você vai precisar de ",lata4,"l de tinta.")
else:
    print("Os valores estão incorretos. Tente novamente!")
