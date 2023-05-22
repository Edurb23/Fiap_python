dias = int(input("Informe dias uteis: "))
horas = int(input("Informe o total de horas: "))
valor_hora = float(input("Valor hora trabalhada: "))

jornada = dias * 8

if horas > jornada:
    print("Tenho hora-extra")
    hora_extra = horas - jornada
    valor_hora_extra = hora_extra * valor_hora * 1.5
    print("Valor das horas-extras:", valor_hora_extra)
    salario_final = jornada * valor_hora + valor_hora_extra
else:
    #nao tem hora extra e posso calcular o salario
    salario_final = horas * valor_hora

print("Salário: ", salario_final)  