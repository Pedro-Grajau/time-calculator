def converte_hora(horario):
    return map(lambda x: int(x), horario.split(":"))

def tempo_adicional(tempo_adicional, tempo):
    tempo_maior_adicional = 0
        while tempo_adicional >= tempo:
            tempo_adicional -= tempo
            tempo_maior_adicional += 1
    return tempo_maior_adicional, tempo_adicional

def add_time(comeco, duracao, dia_semana=None):

    dias_da_semana = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    horario, meridiano = comeco.split()
    hora_inicio, minuto_inicio = converte_hora(horario)
    hora_duracao, minuto_duracao = converte_hora(duracao)

    if meridiano == "PM":
      hora_inicio += 12

    #Trabalhando com o resto dos minutos, caso necessario
    minutos_adicionais = minuto_inicio + minuto_duracao
    horas_adicionais = 0
    if minutos_adicionais >= 60:
      horas_adicionais, minutos_adicionais = tempo_adicional(minutos_adicionais, 60)

    #Trabalhando com o resto das horas, caso necessario
    hora_final = hora_inicio + hora_duracao + horas_adicionais
    dias_adicionais = 0
    if hora_final >= 24:
      dias_adicionais, hora_final = tempo_adicional(hora_final, 24)

    #Definindo o meridiano
    if hora_final > 12 or (hora_final == 12 and minutos_adicionais > 0):
      hora_final -= 12
      meridiano = "PM"
    else:
      meridiano = "AM"

    #A Hora não pode ficar zero
    hora_final = 12 if hora_final == 0 else hora_final

    #Se houver o parâmetro de dia de semana na função
    if dia_semana:
      dia_semana = dias_da_semana.index(dia_semana.lower().capitalize())
      dia_semana += dias_adicionais
      index_dia = dia_semana % 7
      if dias_adicionais == 0:
        return "{}:{:0>2} {}, {}".format(hora_final, minutos_adicionais, meridiano, dias_da_semana[index_dia])
      elif dias_adicionais == 1:
        return "{}:{:0>2} {}, {} (next day)".format(hora_final, minutos_adicionais, meridiano, dias_da_semana[index_dia])
      else:
        return "{}:{:0>2} {}, {} ({} days later)".format(hora_final, minutos_adicionais, meridiano, dias_da_semana[index_dia], dias_adicionais)

    #Trabalho com especifiações
    if dias_adicionais == 0:
      return "{}:{:0>2} {}".format(hora_final, minutos_adicionais, meridiano)
    elif dias_adicionais == 1:
       return "{}:{:0>2} {} (next day)".format(hora_final, minutos_adicionais, meridiano)
    else:
      return "{}:{:0>2} {} ({} days later)".format(hora_final, minutos_adicionais, meridiano, dias_adicionais)
      
