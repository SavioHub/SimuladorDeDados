# simulador de dado
# simular o uso de um dado, gerando um valor de 1 até 6

import random
# _init_self para iniciar o projeto


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'vc gostaria de gerar um novo valor para o dado?'

    def iniciar(self):
        try:
            resposta = input(self.mensagem).lower()
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDado()
            elif resposta == 'nao' or resposta == 'n':
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
