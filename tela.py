import PySimpleGUI as sg 

class TelaPython():
    def __init__(self):
        # layout 
        layout = [
            [sg.Text("Nome:",size=(10,0)), sg.Input(size=(20,0),key='nome')],
            [sg.Text("Idade :",size=(10,0)), sg.Input(size=(20,0),key='idade')],
            [sg.Text("Quais provedores de email sao aceitos ?")],
            [sg.Checkbox("Gmail",key='gmail'),sg.Checkbox("Yahoo",key='yahoo'), sg.Checkbox("Outlook",key='outlook')],
            [sg.Text("Aceita Cartão ?")],
            [sg.Radio("Sim",'cartoes',key='aceitaCartao'),sg.Radio("Nao",'cartoes',key='naoAceitaCartao')],
            [sg.Slider(range=(0,200),default_value=0,orientation='h',size=(28,20),key='slider')],
            [sg.Button("Enviar Dados")],
            [sg.Output(size=(33,20))]
        ]
        
        # janela
        self.janela = sg.Window("Dados do usuário").layout(layout)
        

    def Iniciar(self):
        while True:
            # extrair dados da tela
            self.buttom, self.values = self.janela.Read()

            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_yahoo = self.values['yahoo']
            aceita_outlook = self.values['outlook']
            aceitaCartao = self.values['aceitaCartao']
            naoAceitaCartao = self.values['naoAceitaCartao']
            sliderVelocidade = self.values['slider']
            print(f'Nome : {nome}')
            print(f'Idade : {idade}')
            print(f'Aceita_gmail : {aceita_gmail}')
            print(f'Aceita_yahoo : {aceita_yahoo}')
            print(f'Aceita_outlook : {aceita_outlook}')
            print(f'Aceita_Cartao : {aceitaCartao}')
            print(f'Nao_Aceita_Cartao : {naoAceitaCartao}')
            print(f'VelocidadeScript : {sliderVelocidade}')
            
    
tela = TelaPython()
tela.Iniciar()


