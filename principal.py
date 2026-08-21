from ambiente import Ambiente
from agente_memoria import AgenteComMemoria

ambiente = Ambiente()
agente = AgenteComMemoria()
print('Estado inicial:', ambiente.status, '| Agente em:', ambiente.posicao_agente)

for passo in range(1, 6):
    percepcao = ambiente.perceber()
    acao = agente.decidir(percepcao)
    if agente.memoria == {'A': 'Limpo', 'B': 'Limpo'}:
        break
    ambiente.executar(acao)
    print(f'Passo {passo}: percebeu {percepcao} -> ação: {acao}' f'| novo estado: {ambiente.status}')