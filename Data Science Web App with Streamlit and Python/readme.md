# Colisões de Veículos em Nova York

Este é um aplicativo web interativo desenvolvido em Python com o framework Streamlit. Ele permite analisar colisões de veículos na cidade de Nova York com base em um conjunto de dados fornecido.
Link para acessar os dados utilizados: https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95

1. Bibliotecas necessárias:
   - `streamlit`: usado para criar a interface interativa.
   - `pandas`: utilizado para manipulação e análise dos dados.
   - `numpy`: utilizado para operações numéricas.
   - `pydeck`: utilizado para visualizações geoespaciais.
   - `plotly.express`: usado para gráficos interativos.

2. Carregamento dos dados:
   - O conjunto de dados utilizado é obtido a partir de um arquivo CSV chamado `Motor_Vehicle_Collisions_-_Crashes.csv`.
   - O arquivo é lido utilizando a biblioteca `pandas` e é feito um pré-processamento dos dados.
   - Os dados são armazenados em um DataFrame.

3. Interface do aplicativo:
   - Utilizando a biblioteca `streamlit`, são criados componentes para exibir títulos, markdown e elementos interativos, como sliders e selectboxes.
   - Esses componentes permitem ao usuário interagir com o aplicativo e selecionar opções de análise.

4. Análise e visualização dos dados:
   - Com base nos dados carregados, são criadas visualizações interativas utilizando as bibliotecas `pydeck` e `plotly.express`.
   - Essas visualizações incluem mapas, gráficos de barra e tabelas, que fornecem informações sobre colisões de veículos em Nova York.
   - A análise é realizada considerando diferentes aspectos, como localização, horário e tipos de afetados.

5. Execução do aplicativo:
   - Por fim, o aplicativo é executado utilizando o comando `streamlit run app.py`.
   - O Streamlit cria automaticamente um servidor local e exibe o aplicativo no navegador.