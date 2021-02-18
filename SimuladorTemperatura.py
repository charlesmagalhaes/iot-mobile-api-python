import random
import sqlite3
from datetime import datetime



conn = sqlite3.connect(
    'C:\\temp\ws-SQLITE\Controle de Temperatura do Arquivo Hospital.db')
cursor = conn.cursor()

i = 1
while i <= 30:
    temp = str(random.randrange(25, 30))
    temp1 = str(random.randrange(20, 25))
    umid = str(random.randrange(50, 80))
    umid1 = str(random.randrange(20, 50))
    print(i, '------------------------------------------')
    print('Temperatura Máxima: ', temp, ' - Temperatura Máxima: ', temp1)
    print('Umidade Máxima: ', umid, ' - Umidade Mínima: ', umid1)

    datahora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    print('Data e Hora do registro: ', datahora)

    comando = "insert into ControledeTemperaturaArquivo (TemperaturaMáxima, TemperaturaMínima, UmidadeMáxima, " \
              "UmidadeMínima, DataeHora,Replicado) values('" + temp + "', '" + temp1 + "','" + umid + "','" + umid1 + "','" + datahora + "', 'Não') "

    cursor.execute(comando)
    conn.commit()
    i += 1

conn.close()