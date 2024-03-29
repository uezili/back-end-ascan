# Comandos importantes do projeto
> Obs: **Para testar essa API será necessário apenas com o docker e docker composer. Pois, os comandos serão rodados dentro do ambiente Docker.**
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

# Rotas



| Nome                    | Caminho                             |
| :---------------------: | :---------------------------------: |
| `Admin`                 | http://localhost:8000/admin/        |
| `Users`                 | http://localhost:8000/users/        |
| `Send Message`          | http://localhost:8000/send-massage/ |
| `Swagger Documentation` | http://localhost:8000/swagger       |

# Padão de json para enviar requisição
### SUBSCRIPTION PURCHASED 
```
{
  "event_type": "SUBSCRIPTION_PURCHASED",
  "data": {
    "user_id": 1
  }
}
```
### SUBSCRIPTION CANCELED
```
{
  "event_type": "SUBSCRIPTION_CANCELED",
  "data": {
    "subscription_id": 3
  }
}
```
### SUBSCRIPTION RESTARTED
```
{
  "event_type": "SUBSCRIPTION_RESTARTED",
  "data": {
    "subscription_id": 3
  }
}
```
