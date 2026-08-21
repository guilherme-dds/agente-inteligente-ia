class AgenteComMemoria:
    def __init__(self):
        self.memoria = {'A': None, 'B': None}

    def decidir(self, percepcao):
        posicao, status = percepcao
        self.memoria[posicao] = status

        if status == 'Sujo':
            return 'Aspirar'
        elif posicao == 'A':
            return 'MoverDireita'
        elif posicao == 'B':
            return 'MoverEsquerda'

        pass