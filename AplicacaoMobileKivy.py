from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout(cols=2)  # cria um novo layout

        self.add_widget(
            Label(text="Controle de Umidade e Temperatura - Arquivo Hospital ", size_hint_x=4, width=50))

        self.inside.add_widget(Label(text="Temperatura Máxima: "))
        self.temp = TextInput(multiline=True)
        self.inside.add_widget(self.temp)


        self.inside.add_widget(Label(text="Temperatura Mínima: "))
        self.temp1 = TextInput(multiline=True)
        self.inside.add_widget(self.temp1)

        self.inside.add_widget(Label(text="Umidade Máxima: "))
        self.umidade = TextInput(multiline=True)
        self.inside.add_widget(self.umidade)

        self.inside.add_widget(Label(text="Umidade Mínima: "))
        self.umidade1 = TextInput(multiline=True)
        self.inside.add_widget(self.umidade1)

        self.inside.add_widget(Label(text="Data: "))
        self.data = TextInput(multiline=True)
        self.inside.add_widget(self.data)
        self.inside.add_widget(Label(text="Hora: "))
        self.hora = TextInput(multiline=True)
        self.inside.add_widget(self.hora)

        self.info = TextInput(multiline=True)
        self.inside.add_widget(self.info)

        self.info2 = TextInput(multiline=True)
        self.info2.text = '             Acima os cinco últimos registros'
        self.inside.add_widget(self.info2)

        self.add_widget(self.inside)  # adiciona o layout interno
        self.submit = Button(text="Buscar", font_size=20)
        self.submit.bind(on_press=self.pressed)  # vincula o evento
        self.add_widget(self.submit)  # adiciona o botão ao layout principal


    def pressed(self, instance):  # implementação do evento

        global registros
        url = 'https://api.thingspeak.com/channels/1235546/feeds.json?results=800'


        import requests

        r = requests.get(url)
        feeds = r.json()
        temperatura = feeds['feeds']
        self.info.text = 'Quantidade de registros: ' + str(len(temperatura))
        reg = len(temperatura)

        url = 'https://api.thingspeak.com/channels/1235546/feeds.json?results=5'
        r = requests.get(url)
        feeds = r.json()
        temperatura = feeds['feeds']

        cont=0
        print(temperatura[0])
        for x in temperatura:
            cont +=1

            registros = x

            self.temp.text +=' - '+ str(registros['field1'])
            self.temp1.text += ' - '+str(registros['field2'])
            self.umidade.text += ' - '+str(registros['field3'])
            self.umidade1.text += ' - '+str(registros['field4'])
            data = str(registros['created_at'])
            hora = str(registros['created_at'])
            self.data.text = str(data[0:10])
            self.hora.text = str(hora[11:16])
            if cont == 5:
                break

        print('Quantidade de registros: ', reg)
        print('_____________Última temperatura e umidade registrada___________')
        print('Temperatura Máxima: ', registros['field1'],' - Temperatura Máxima: ',registros['field2'])
        print('umidade Máxima: ', registros['field3'],' - umidade Máxima: ',registros['field4'])
        print('Data do registro: ', self.data.text, "Hora: ", self.hora.text)



class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()