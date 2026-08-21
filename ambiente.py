import random

class Ambiente:
    def __init__(self):
        self.status = {
            'A': random.choice(['Limpo', 'Sujo']),
            'B': random.choice(['Limpo', 'Sujo']),
        }
        self.posicao_agente = random.choice(['A', 'B'])

    def perceber(self):
        return self.posicao_agente, self.status[self.posicao_agente]
    
    def executar(self, acao):
        if acao == 'Aspirar':
            self.status[self.posicao_agente] = 'Limpo'
        elif acao == 'MoverEsquerda':
            self.posicao_agente = 'A'
        elif acao == 'MoverDireita':
            self.posicao_agente = 'B'

def agente_reativo_simples(percepcao):
    posicao, status = percepcao
    if status == 'Sujo':
        return 'Aspirar'
    elif posicao == 'A':
        return 'MoverDireita'
    elif posicao == 'B':
        return 'MoverEsquerda'