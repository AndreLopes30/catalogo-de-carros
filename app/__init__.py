from flask import Flask
from urllib.parse import urlparse
import requests
from datetime import datetime

app = Flask(__name__)

def validar_url_imagem(url, timeout=3):
    try:
        resultado = urlparse(url)
        if not all([resultado.scheme, resultado.netloc]):
            return False
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        content_type = response.headers.get('content-type', '')
        return 'image' in content_type.lower()
    except:
        return False

def normalizar_preco(valor_str):
    valor_str = valor_str.strip().replace('.', '').replace(',', '.')
    return float(valor_str)

def formatar_preco(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

from app import routes