# Teoria Dos Grafos - Mackenzie

## Integrantes:

- Bruno Lauand Ferrão - 10401081

## Título da Aplicação:
Otimização do Sistema Metroviário de São Paulo usando Teoria dos Grafos

## Descrição do Problema:
O sistema metroviário de São Paulo é uma das redes de transporte público mais complexas e importantes do Brasil. A necessidade de eficiência em termos de conectividade, fluxo de passageiros e custos de operação é crucial para atender à crescente demanda populacional. Neste projeto, modelamos a rede metroviária como um grafo para analisar sua estrutura e características, ajudando a identificar caminhos eficientes, possíveis falhas na conectividade e propriedades importantes como a Eulerianidade e ciclos Hamiltonianos.

## Justificativa do Uso de Grafos:
A rede metroviária foi representada por vértices (estações) e arestas (conexões entre estações) com pesos correspondentes às distâncias ou custos de transporte. Este modelo permite aplicar algoritmos de teoria dos grafos para:
Verificar a conectividade da rede;
Determinar caminhos ou ciclos ótimos (Eulerianos ou Hamiltonianos);
Analisar graus de entrada e saída das estações.

## Objetivos do Desenvolvimento Sustentável (ODS):
ODS 11: Cidades e Comunidades Sustentáveis - O estudo da conectividade do sistema metroviário apoia soluções mais eficientes para mobilidade urbana.
ODS 9: Indústria, Inovação e Infraestrutura - Identificar pontos de melhoria na infraestrutura do transporte público é essencial para seu desenvolvimento sustentável.
ODS 13: Ação Contra a Mudança Global do Clima - Ao otimizar o transporte público, incentivamos o uso de meios coletivos, reduzindo emissões de gases do efeito estufa.

## Novas Funcionalidades Implementadas:
### Verificação de Eulerianidade:
Determina se o grafo é Euleriano ou possui caminho Euleriano.
Detecção de Ciclos Hamiltonianos:
Analisa a existência de ciclos que percorrem todas as estações sem repetições.
### Conexidade:
Verifica a conectividade do grafo e determina componentes fortemente conexas.
Análise de Graus de Entrada e Saída:
Identifica o grau de conexão de cada estação.
