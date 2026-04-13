# Sistema de gestão de Peças

pecas = []
caixas = []
caixa_atual = []

capacidade_caixa = 10

# Função para avaliar peças
def avaliar_peca(peca):
    motivos = []

    if not (95 <= peca['peso'] <= 105):
        motivos.append('Peso fora do padrão')
    
    if peca['cor'].lower() not in ['azul', 'verde']:
        motivos.append('Cor inválida')
    
    if not (10 <= peca['comprimento'] <= 20):
        motivos.append('Comprimento fora do padrão')
    
    if len(motivos) == 0:
        return True, 'Aprovada'
    else:
        return False, ', '.join(motivos)


# Função cadastrar peça
def cadastrar_peca():
    global caixa_atual

    id_peca = input('ID da peça: ')
    peso = float(input('Peso da peça (g): '))
    cor = input('Cor da peça: ')
    comprimento = float(input('Comprimento da peça (cm): '))

    peca = {
        'id': id_peca,
        'peso': peso,
        'cor': cor,
        'comprimento': comprimento
    }

    aprovada, mensagem = avaliar_peca(peca)

    peca['status'] = 'Aprovada' if aprovada else 'Reprovada'
    peca['motivo'] = mensagem

    pecas.append(peca)

    if aprovada:
        caixa_atual.append(peca)
        if len(caixa_atual) >= capacidade_caixa:
            caixas.append(caixa_atual)
            print('📦 Caixa fechada')
            caixa_atual = []
        
    print(f'Peca {peca['status']}!')

# Listar peças

def listar_pecas():
    for p in pecas:
        print(f'ID: {p['id']} | Status: {p['status']} | Motivos: {p['motivo']}')


# Remover peça
def remover_peca():
    id_peca = input('Digite o ID da peça a ser removida: ')

    for p in pecas:
        if p['id'] == id_peca:
            pecas.remove(p)
            print('Peça removida!')
            return
    print('Peça não encontrada.')

# Listar caixas
def listar_caixas():
    for i, caixa in enumerate(caixas):
        print(f'Caixa { i + 1} - {len(caixa)} peças')

# Relatório final 

def relatorio():
    aprovadas = [p for p in pecas if p['status'] == 'Aprovada']
    reprovadas = [p for p in pecas if p['status'] == 'Reprovada']
    
    print('\n==== RELATEORIO ====')
    print(f'aprovadas: {len(aprovadas)}')
    print(f'Reprovadas: {len(reprovadas)}')
    print(f'Caixas utilizadas: {len(caixas)}')

    print('\nMotivos de reprovação:')
    for p in reprovadas:
        print(f'ID: {p['id']}: {p['motivo']}')

#Menu 
def menu():
    while True:
        print('\n1. Cadastrar nova peça')
        print('2. Listar peças')
        print('3. Remover peça')
        print('4. Listar caixas fechadas')
        print('5. Gerar relatório')
        print('0. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_peca()
        elif opcao == '2':
            listar_pecas()
        elif opcao == '3':
            remover_peca()
        elif opcao == '4':
            listar_caixas()
        elif opcao == '5':
            relatorio()
        elif opcao == '0':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')
          
# Executar sistema
menu()