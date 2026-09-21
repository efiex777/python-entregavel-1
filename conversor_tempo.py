segundos_totais = int(input("Digite o tempo em segundos: "))

horas = segundos_totais // 3600
minutos = (segundos_totais % 3600) // 60
segundos = segundos_totais % 60

print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")
