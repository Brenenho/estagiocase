import requests
from bs4 import BeautifulSoup

# Fazer o request para a página (Coloque o link do lote que deseja extrair as informações)
url = input("Digite o link do lote:")
response = requests.get(url)

# Criar o objeto BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extrair as informações desejadas

# Extrair o título do lote
title = soup.find_all("h4")[1].text.strip()

# Extrair o valor de avaliação do lote (Caso não tenha valor de avaliação, o valor será vazio)
valor_avaliacao_tag = soup.find("strong", string="Valor de Avaliação:")
valor_avaliacao = valor_avaliacao_tag.next_sibling.strip() if valor_avaliacao_tag else ""

# Extrair o valor do lance inicial do lote (Caso não tenha valor de lance inicial, o valor será vazio)
valor_primeira_praca_tag = soup.find("strong", string="Lance Inicial:")
valor_primeira_praca = valor_primeira_praca_tag.next_sibling.strip() if valor_primeira_praca_tag else ""

# Extrair o valor do lance inicial do segundo lote (Caso não tenha valor de lance inicial, o valor será vazio)
valor_segunda_praca_tags = soup.find_all("strong", string="Lance Inicial:")
valor_segunda_praca = valor_segunda_praca_tags[1].next_sibling.strip() if len(valor_segunda_praca_tags) > 1 else ""

# Extrair a data do primeiro leilão (Caso não tenha data do primeiro leilão, o valor será vazio)
data_primeira_praca_tag = soup.find("strong", string="Data 1º Leilão:")
data_primeira_praca = data_primeira_praca_tag.next_sibling.strip() if data_primeira_praca_tag else ""

# Extrair a data do segundo leilão (Caso não tenha data do segundo leilão, o valor será vazio)
data_segunda_praca_tag = soup.find("strong", string="Data 2º Leilão:")
data_segunda_praca = data_segunda_praca_tag.next_sibling.strip() if data_segunda_praca_tag else ""

# Extrair o endereço do lote (Caso não tenha endereço, o valor será vazio)
endereco_tag = soup.find("b", string="Endereço:")
endereco = endereco_tag.next_sibling.strip() if endereco_tag else ""

# Extrair o link do documento do lote (Caso não tenha link do documento, o valor será vazio)
link_documento_tag = soup.find("div", class_="arquivos-lote").find("a")
link_documento = link_documento_tag["href"] if link_documento_tag else ""

# Extrair o link da imagem do lote (Caso não tenha link da imagem, o valor será vazio)
link_imagem_tag = soup.find("a", rel="prettyPhoto[carouselItem]")
link_imagem = link_imagem_tag["href"] if link_imagem_tag else ""

# Imprimir os resultados
print("Título:", title)
print("Valor de Avaliação:", valor_avaliacao)
print("Lance Inicial (1ª Praça):", valor_primeira_praca)
print("Data 1º Leilão:", data_primeira_praca)
print("Lance Inicial (2ª Praça):", valor_segunda_praca)
print("Data 2º Leilão:", data_segunda_praca)
print("Endereço:", endereco)
print("Link do Documento:", link_documento)
print("Link da Imagem:", link_imagem)


input("Pressione <enter> para encerrar!")