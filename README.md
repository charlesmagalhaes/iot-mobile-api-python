### Projeto Final - Internet das Coisas

1. Dispositivo de IoT: responsável por coletar dados do ambiente e disponibilizá-los em uma rede local (escritório, casa, etc.)
Será adotada a plataforma Arduino para efeito de exemplificação, assim como um shield de ethernet/wifi para comunicação com o broaker local.
2. Broaker local: responsável por concentrar os dados coletados pelo dispositivo de IoT e armazená-los em um banco de dados também local. A aplicação do broaker local deverá replicar tal banco na internet.
Será implementado um código usando a linguagem Python para obter os dados do Arduino, através do protocolo HTTP. Essa rotina deverá salvar os dados em um banco SQLite e posteriormente replicá-los para o broaker remoto. Tal replicação caracterizará um sistema distribuído de banco de dados, mesmo que de forma simples (unidirecional: broaker local  broaker remoto)
3. Broaker remoto: funcionará como broaker (intermediador) e datalogger (banco de dados) na internet. 
Como broaker remoto será usada a plataforma ThingSpeak, a ser acessada pelo broaker local através de suas APIs em HTTP.
4. Aplicação mobile: deverá consumir os dados do broaker/datalogger remoto e exibi-las para o usuário.
A aplicação mobile, como dito anteriormente, deverá consumir os dados e exibi-los ao usuário e isso será feito de duas formas:
Usando o ThingView, aplicativo da própria plataforma ThingSpeak, bastando instalar e configurar.
Criação de uma pequena aplicação para Android usando Python e Kivy para consumir os dados da ThingSpeak, também via HTTP.

![iot](https://user-images.githubusercontent.com/67280323/114068074-e07ecf00-9873-11eb-8c07-cc5d7614b578.jpg)

![telaKivy](https://user-images.githubusercontent.com/67280323/114068974-ddd0a980-9874-11eb-963b-566fe94b5f5e.jpg)



## Tecnologia envolvida

1. Pycharm Community 2020.2;
1. Linguagem Python para desenvolvimento do backend;
1. Kivy para desenvolvimento a interface gráfica;
1. Banco de dados SQLite;
1. API com https://thingspeak.com/



## Como "startar" a aplicação
1. Clonar o projeto no diretório de sua preferência;
1. Abrir o Visual Studio Code e importar a aplicação;


## Navegar na aplicação



## API's para alimentação dos dados

- write - GET https://api.thingspeak.com/update?api_key=HXU1O3UOLAAG98KG&field1=0
- read - GET https://api.thingspeak.com/channels/1235546/fields/1.json?results=2
