# Comandos importantes do projeto
> Obs: **Para testar essa API será necessário apenas com o Docker e Docker Composer, pois os comandos serão rodados dentro do ambiente Docker.**
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

Para gerar os relatório, rode o seguinte comando:

```bash
  docker-composer run web coverage run manage.py test
```

Para rodar os relatório em html, rode o seguinte comando:

```bash
  docker-composer run web coverage html
```

# Rotas



| Nome                    | Caminho                             |
| :---------------------: | :---------------------------------: |
| `Admin`                 | http://localhost:8000/admin/        |
| `Users`                 | http://localhost:8000/users/        |
| `Send Message`          | http://localhost:8000/send-massage/ |
| `Swagger Documentation` | http://localhost:8000/swagger       |

# Padão de json para enviar requisição
### SUBSCRIPTION PURCHASED 
```JSON
{
  "event_type": "SUBSCRIPTION_PURCHASED",
  "data": {
    "user_id": 1
  }
}
```
### SUBSCRIPTION CANCELED
```JSON
{
  "event_type": "SUBSCRIPTION_CANCELED",
  "data": {
    "subscription_id": 3
  }
}
```
### SUBSCRIPTION RESTARTED
```JSON
{
  "event_type": "SUBSCRIPTION_RESTARTED",
  "data": {
    "subscription_id": 3
  }
}
```
