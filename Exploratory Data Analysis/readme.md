# Projeto de Diagnóstico de Câncer de Mama

## Sobre o Conjunto de Dados

O conjunto de dados de Diagnóstico de Câncer de Mama está disponível no Repositório de Aprendizado de Máquina da UCI. Este banco de dados também está disponível através do servidor FTP da UW CS.

As características são computadas a partir de uma imagem digitalizada de uma aspiração por agulha fina (FNA) de uma massa de mama. Elas descrevem características dos núcleos celulares presentes na imagem. O espaço tridimensional descrito é baseado em: [K. P. Bennett e O. L. Mangasarian: "Robust Linear Programming Discrimination of Two Linearly Inseparable Sets", Optimization Methods and Software 1, 1992, 23-34].

Informações dos Atributos:

- Número de identificação
- Diagnóstico (M = maligno, B = benigno)

Dez características de valor real são calculadas para cada núcleo celular:

1. Raio (média das distâncias do centro aos pontos na periferia)
2. Textura (desvio padrão dos valores em escala de cinza)
3. Perímetro
4. Área
5. Suavidade (variação local nos comprimentos dos raios)
6. Compacidade (perímetro^2 / área - 1.0)
7. Cavidade (gravidade das porções côncavas do contorno)
8. Pontos côncavos (número de porções côncavas do contorno)
9. Simetria
10. Dimensão fractal ("aproximação da linha costeira" - 1)

A média, o erro padrão e o "pior" ou maior (média dos três maiores valores) dessas características foram calculados para cada imagem, resultando em 30 características. Por exemplo, o campo 3 é Raio Médio, o campo 13 é Raio SE e o campo 23 é Pior Raio.

Todos os valores das características são registrados com quatro dígitos significativos.

Valores ausentes dos atributos: nenhum

Distribuição das classes: 357 benignos, 212 malignos

## Código

O código fornecido realiza as seguintes funcionalidades:

1. Importação de bibliotecas: Importa as bibliotecas necessárias, como o NumPy para álgebra linear e o Pandas para manipulação de dados.

2. Carregamento do conjunto de dados: Carrega o conjunto de dados a partir de um arquivo CSV usando o Pandas e armazena-o em um dataframe chamado `data`.

3. Separação do alvo e das características: Separa a variável alvo, que contém o diagnóstico (benigno ou maligno), da matriz de características. Descarta as colunas indesejadas, como 'Unnamed: 32', 'id' e 'diagnosis', para formar um novo dataframe chamado `x`. A variável alvo é armazenada em uma série chamada `y`.

4. Plotagem da distribuição dos diagnósticos: Cria um gráfico de contagem para visualizar a distribuição dos diagnósticos benignos e malignos. O eixo x representa os diagnósticos, e o eixo y mostra a contagem de cada diagnóstico.

5. Análise descritiva das características: Exibe estatísticas descritivas das características, como média, desvio padrão, mínimo, máximo e quartis. Isso fornece uma visão geral das propriedades das características do conjunto de dados.

6. Visualização dos dados padronizados: Padroniza os dados para ter média zero e desvio padrão um, a fim de colocar todas as características na mesma escala. Em seguida, cria gráficos de violino e boxplot para visualizar a distribuição dos valores padronizados das características, separados pelos diagnósticos benignos e malignos.

7. Comparação de características através de gráficos de dispersão conjunta: Gera um gráfico de dispersão conjunta (joint plot) para comparar duas características do conjunto de dados. Neste caso, as características "concavity_worst" e "concave points_worst" são comparadas, e é adicionada uma linha de regressão para analisar a relação entre elas.

8. Observação da distribuição e variância dos valores com gráficos de enxame: Cria gráficos de enxame (swarm plots) para visualizar a distribuição e variância dos valores padronizados das características. Cada ponto no gráfico representa um valor, e os pontos são agrupados por diagnóstico e por características.

9. Visualização das correlações entre todas as características: Gera um mapa de calor (heatmap) para mostrar as correlações entre todas as características do conjunto de dados. Os valores das correlações são exibidos nos quadrados do mapa de calor, proporcionando insights sobre as relações entre as características.

Essas funcionalidades fornecem uma análise exploratória inicial do conjunto de dados de diagnóstico de câncer de mama, permitindo visualizar a distribuição dos diagnósticos, as características e suas relações. Isso pode ajudar na compreensão dos dados e no desenvolvimento de modelos de classificação mais precisos.
