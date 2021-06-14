# simulador de dado
# simular o uso de um dado, gerando um valor de 1 até 6

import random
import PySimpleGUI as sg
# _init_self para iniciar o projeto


class SimuladorDeDado:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # self.mensagem = 'vc gostaria de gerar um novo valor para o dado?'

        # layout
    layout = [
        [sg.Text("Jogar dado?")],
        [sg.Button('sim'), sg.Button('não')]
    ]

    def iniciar(self):
        # criar uma janeja
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.read()
        # fazer alguma c oisa com esses valores

        # resposta = input(self.mensagem).lower()
        try:
            # self.eventos == 'sim':
            if self.eventos == 'sim':
                self.GerarValorDado()
            elif self.eventos == 'não':
                print('Obrigado pela sua participação.')
            else:
                print('Apenas: sim ou não')
        except:
            print('ocorreu um erro ao receber a sua resposta!')

# random.randint irar gerar um valor inteiro minimo e maximo
    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


# instanciar a classe para ser usada
Simulador = SimuladorDeDado()
Simulador.iniciar()
