arquivo = open('Manipulacao\lorem.txt', 'r')

print(arquivo.read(10))
print(arquivo.readline())
print(arquivo.readlines())
#while len(linha := arquivo.readline()):
 #   print(linha)

arquivo.close()