#Calculadora de Números Fatoriais

print('Calculadora de Númeors Fatoriais')
f = int(input('Digite um número para saber sua fatorial: '))
x = f
y = f - 1
while (y >= 1):
  f *= y
  print("{} * {} = {}".format(f//y,y,f))
  y -= 1
print("O fatorial de {} é = {}".format(x,f))