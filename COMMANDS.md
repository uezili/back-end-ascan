# Rodando os testes
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
