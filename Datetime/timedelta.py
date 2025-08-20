from datetime import datetime, timedelta

tipo_carro = input("Informe o tipo de carro (p - pequeno, m - médio, g - grande): ").strip().lower()
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()
data_hora_str = "2025-08-19 22:12" 
mascara = "%d/%m/%y %H:%M"

if tipo_carro == 'p':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual.strftime(mascara)} e ficará pronto em {data_estimada.strftime(mascara)}.')

elif tipo_carro == 'm':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou: {data_atual.strftime(mascara)} e ficará pronto em {data_estimada.strftime(mascara)}.')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou: {data_atual.strftime(mascara)} e ficará pronto em {data_estimada.strftime(mascara)}.')
