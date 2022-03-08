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

varP1 = resultPortaP1 + resultJanP1 
varP2 = resultPortaP2 + resultJanP2 
varP3 = resultPortaP3 + resultJanP3 
varP4 = resultPortaP4 + resultJanP4 

porcentP1 = p1/2
porcentP2 = p2/2
porcentP3 = p3/2
porcentP4 = p4/2

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



