import re


class ExtratorUrl:
    def __init__(self, url):
        self.url = url
        self.valida_url()

    def sanitiza_url(self, url):
        return url.strip()

    def valida_url(self):
        if not self.url:
            raise ValueError("URL VAZIA")
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)

        if not match:
            raise ValueError("A url não é valida")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao + 1]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor]
        else:
            valor = self.get_url_parametros()[indice_valor : indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url



url ='bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real'
extrator_url = ExtratorUrl(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

print("Url valida")

