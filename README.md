# Plataforma de Currículos

Este é um projeto de uma plataforma de currículos desenvolvida com Django. A plataforma permite que os usuários façam upload de seus currículos, que são armazenados no banco de dados junto com informações adicionais, como endereço IP e data de envio. Além disso, os currículos podem ser visualizados e baixados por administradores.

## Funcionalidades

- Upload de currículos com validação de formato e tamanho de arquivo.
- Armazenamento de currículos no banco de dados.
- Registro do endereço IP e data de envio do currículo.
- Visualização e download de currículos enviados.

## Tecnologias Utilizadas

- Python 3.12.6
- Django 5.1.5
- HTML/CSS

## Requisitos

- Python 3.12.6
- Django 5.1.5

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/plataforma-de-curriculos.git
   cd plataforma-de-curriculos

2. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt

4. Instale as dependências:

    ```bash
    python manage.py migrate

5. Crie um superusuário para acessar o admin do Django:

    ```bash
    python manage.py createsuperuser

6. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
