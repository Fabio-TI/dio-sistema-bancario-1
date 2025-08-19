def mensagem(nome):
    print("Executando mensagem")
    return f"oi{nome}"


def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem {nome}?"

def executar(funcao, nome):
    print("Executar executar")
    return funcao(nome)


print(executar(mensagem, "João"))
print(executar(mensagem_longa, "Maria"))