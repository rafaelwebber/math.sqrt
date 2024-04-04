''' 1) Construa um programa que tem como dados de entrada dois pontos
quaisquer no plano cartesiano: P1 e P2. Considere que P1 é definido
pelas coordenadas x1 e y1, enquanto P2 por x2 e y2 . O programa deve
calcular e escrever a distância entre os pontos P1 e P2. A fórmula que
calcula a distância entre os dois pontos é dada por:
A função que calcula a raiz quadrada é a sqrt() (square root), veja pow()
'''
import math
x1 = float(input("Digite um ponto do plano cartesiano para x1: "))
y1 = float(input("Digite um segundo ponto do plano cartesiano para y1: "))

x2 = float(input("Digite um ponto do plano cartesiano para x2: "))
y2 = float(input("Digite um segundo ponto do plano cartesiano para y2: "))



d = math.sqrt( math.pow(x2-x1,2)  + math.pow(y2-y1,2))
e = math.sqrt((x2-x1)**2  + (y2-y1)**2)
print(f"O valor da distância é:{d:,.2f}, {e:,.2f}")
