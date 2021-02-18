import sqlite3
import time

import requests

url = 'https://api.thingspeak.com/update?api_key=HXU1O3UOLAAG98KG&field1='

try:
    conn = sqlite3.connect(
        'C:\\temp\ws-SQLITE\Controle de Temperatura do Arquivo Hospital.db')
    cursor = conn.cursor()

    cursor.execute("select * from ControledeTemperaturaArquivo where Replicado = 'Não'")
    for linha in cursor.fetchall():
        temp = (linha[1])
        temp1 = (linha[2])
        umid = (linha[3])
        umid1 = (linha[4])
        r = requests.get(url + str(temp) + '&field2=' + str(temp1) + '&field3=' + str(umid) + '&field4=' + str(umid1))
        controle = "Sim"
        comando = "update ControledeTemperaturaArquivo set Replicado = '"+str(controle)+"' where Id ='" + str(linha[0]) + "'"
        cursor.execute(comando)
        conn.commit()

        print('Temperatura Máxima', temp, ' - Temperatura Mínima', temp1, ' - Umidade Máxima', umid, ' - Umidade Mínima',
          umid1)
        time.sleep(15)
    print('________________________________________')
    print('Thingspeak foi atualizado com sucesso!!!')
    print('________________________________________')
    conn.close()

except:
    print('______________________________________________')
    print("Sem conexão com Thingspeak. Tente mais tarde")
    print('_______________________________________________')
