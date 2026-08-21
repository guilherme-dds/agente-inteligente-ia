from ambiente import Ambiente
from agente import agente_reativo_simples

ambiente = Ambiente()
print('Estado inicial:', ambiente.status, '| Agente em:', ambiente.posicao_agente)

for passo in range(1, 6):
    percepcao = ambiente.perceber()
    acao = agente_reativo_simples(percepcao)
    ambiente.executar(acao)
    print(f'Passo {passo}: percebeu {percepcao} -> ação: {acao}' f'| novo estado: {ambiente.status}')