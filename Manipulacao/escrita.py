arquivo = open('C:/Users/fabio/Desktop/Engenharia/Python/dio1/Manipulacao/teste.txt', 'w')
arquivo.write('Escrevendo no arquivo teste.txt')
arquivo.writelines(["\n""Escrevendo ", "um ", "novo ", "texto\n"])




arquivo.close()
arquivo = open('C:/Users/fabio/Desktop/Engenharia/Python/dio1/Manipulacao/teste.txt', 'r')
print(arquivo.readlines())

arquivo.close()