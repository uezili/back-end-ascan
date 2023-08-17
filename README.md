# Backend Ascan

Este é um desafio proposto pelo programa de estagiários do Instituto Atlântico na trilha de Backend. Neste desafio foi desenvolvido uma API para controle de assinatura de um sistema de streaming.

# Indice
- [Desafio](DESAFIO.md)
- [Como Rodar e extrair relatorios](INFO.md)

# Padrão de Design do Django Rest Framework (DRF)

O Django Rest Framework (DRF) é uma estrutura poderosa para criar APIs RESTful em Django. Ele segue o padrão de design Model-View-Serializer (MVS), que é uma extensão do padrão Model-View-Controller (MVC) adaptada para APIs.

## Pilares do Padrão MVS do DRF

### Modelo (Model)
- Define a estrutura dos dados e a interação com o banco de dados.
- Criado através de classes que herdam de django.db.models.Model.
- Representa tabelas do banco de dados e contém campos e métodos para manipular dados.

### Visualização (View)
- Recebe requisições do cliente e retorna respostas apropriadas.
- Implementado como classes que herdam de django.views.View ou derivadas.
- ViewSets simplificam operações CRUD, substituindo as Views tradicionais.

### Serializador (Serializer)
- Converte objetos Python em representações serializadas (JSON, XML, etc.).
- Lida com validação de dados durante criação/atualização de objetos.
- Define como modelos são serializados e desserializados nas requisições.

### URLs e Roteamento
- Mapeia URLs para Views ou ViewSets usando roteadores como DefaultRouter.
- Roteadores criam automaticamente URLs baseadas nas Views/ViewSets definidas.

# Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Rabbitmq](https://img.shields.io/badge/rabbitmq-%23FF6600.svg?&style=for-the-badge&logo=rabbitmq&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) 
![Sqlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
