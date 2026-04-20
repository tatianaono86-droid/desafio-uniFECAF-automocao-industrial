Desafio de Automação Digital: Gestão de Peças e Qualidade

Este projeto foi desenvolvido como parte da disciplina de Algoritmos e Lógica de Programação (UniFECAF). 
O objetivo é automatizar o processo de inspeção de qualidade de uma linha de montagem industrial, substituindo a conferência manual por um sistema lógico em Python.


🚀 Sobre o Projeto
O sistema recebe dados técnicos de peças fabricadas e decide, de forma autónoma, se a peça
está aprovada para envio ou se deve ser reprovada, indicando o motivo da falha. Além disso, o
software faz a gestão logística, organizando as peças aprovadas em caixas de 10 unidades.

Critérios de Qualidade (Regras de Negócio):
Para ser aprovada, a peça deve cumprir todos os requisitos:

Peso: Entre 95g e 105g.

Cor: Azul ou Verde.

Comprimento: Entre 10cm e 20cm.

🛠 Funcionalidades
O programa apresenta um menu interativo com as seguintes opções:
1. Cadastrar nova peça: Entrada de ID, peso, cor e comprimento.
2. Listar peças: Exibe o histórico de todas as peças processadas.
3. Remover peça: Permite excluir um registo através do ID.
4. Listar caixas fechadas: Mostra quantas caixas de 10 unidades foram completadas.
5. Gerar relatório: Apresenta totais de produção e motivos detalhados de reprovação.

📦 Como executar o programa
Pré-requisitos:

Ter o Python 3.x instalado no computador.

Passo a Passo:
1. Faça o download do ficheiro .py deste repositório.
2. Abra o terminal ou a linha de comandos.
3. Navegue até à pasta onde guardou o ficheiro.
4. Execute o comando:  Python sistema-de-gestao-de-pecas.py

📝 Exemplo de Uso

Entrada:
ID: 101

Peso: 100g

Cor: Azul

Comprimento: 15cm

Saída Esperada:
Peça Aprovada!

(A peça é adicionada à contagem da caixa atual).
