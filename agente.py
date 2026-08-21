def agente_reativo_simples(percepcao):
    posicao, status = percepcao
    if status == 'Sujo':
        return 'Aspirar'
    elif posicao == 'A':
        return 'MoverDireita'
    elif posicao == 'B':
        return 'MoverEsquerda'