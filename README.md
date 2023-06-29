# Projeto de Web Scraping

Este projeto consiste em um script de Web Scraping para extrair informações de um site específico. O script utiliza a biblioteca `requests` para fazer as requisições HTTP e a biblioteca `BeautifulSoup` para analisar e extrair os dados do HTML.

## Funcionalidades

O script atual possui as seguintes funcionalidades:

- Extrair informações de um item de leilão, como título, valor de avaliação, endereço, link do documento e link da imagem.
- Lidar com casos em que as informações não estão disponíveis, atribuindo valores vazios ("") nesses casos.

## Requisitos

Para executar o script, você precisa ter o Python instalado. Além disso, é necessário instalar as seguintes bibliotecas:

- requests
- beautifulsoup4

Você pode instalar as bibliotecas utilizando o gerenciador de pacotes pip:

pip install requests 
pip install beautifulsoup4

## Utilização

1. Acesse a pasta webscraper e inicialize o executável

ou

1. Clone o repositório ou baixe os arquivos do projeto.

2. Abra o terminal ou prompt de comando e navegue até o diretório do projeto.

3. Execute o script usando o seguinte comando:

python webscraping.py


4. Verifique a saída do script no terminal. As informações extraídas serão exibidas, e caso alguma informação não esteja disponível, será exibido um valor vazio ("").

5. Para encerrar, aperte enter.





