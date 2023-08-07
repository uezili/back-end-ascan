# Comandos importantes do projeto

### iniciar
Para iniciar o projeto, rode o seguinte comando:

```bash
  docker-composer up
```

### Parar
Para encerrar os contêiner, rode o seguinte comando:

```bash
  docker-composer down
```

## Rodando os testes
Para rodar os testes, rode o seguinte comando:

```bash
  docker-composer run web manage.py test
```

Para gerar os relatorio, rode o seguinte comando:

```bash
  docker-composer run web coverage run manage.py test
```

Para rodar os relatorio em html, rode o seguinte comando:

```bash
  docker-composer run web coverage html
```


## Documentação da API

#### Retorna todos os itens

| Notificações             | Descrição         |
| ------------------------ | ----------------- |
| `Admin`| http://localhost:8000/admin/ |
| `Users` | http://localhost:8000/users/ |
| `Send Message` | http://localhost:8000/send-massage/ |
| `Swagger Documentation` | http://localhost:8000/swagger |
