# cyber-bank - service

camada de serviço da solução

## requisitos

- python 3.11 ou mais recente
- [pip](https://packaging.python.org/pt_BR/latest/guides/installing-using-pip-and-virtual-environments/)

### venv

Alguns sistemas operacionais não vão deixar instalar o django
(que está no requirements.txt) usando o pip porque não permitem instalações
globais de bibliotecas python.

Se isso acontecer, duas alternativas:

- instalar as dependências do requirements.txt do jeito que o seu SO quer
- criar um [virtualenv](https://docs.python.org/pt-br/3/library/venv.html)

## editor de códigos

tenha um editor de códigos, o de sua preferência

- vscode
- intellij ultimate
- pycharm

seção _em construção_

## configurando

```bash
pip install -r requirements.txt
```

## executando

```bash
python manage.py runserver
```

visite a url em <http://127.0.0.1:8000>

seção _em construção_

## testando

seção _em construção_

## publicando

seção _em construção_

## referências

- <https://docs.djangoproject.com/pt-br/4.2/intro/tutorial01/> (PT)
- <https://pip.pypa.io/en/stable/installation/> (EN)
- <https://www.geeksforgeeks.org/how-to-install-pip-in-macos/> (EN)
- <https://fastapi.tiangolo.com/pt/#crie> (PT)
- <https://github.com/pypa/pipenv/blob/main/docs/workflows.md> (EN)
- <https://jtemporal.com/requirements-txt/> (PT)
- <https://medium.com/@hudsonbrendon/gerenciando-suas-depend%C3%AAncias-e-ambientes-python-com-pipenv-9e5413513fa6> (PT)
- <https://docs.python.org/pt-br/3/library/venv.html> (PT)
- <https://packaging.python.org/pt_BR/latest/guides/installing-using-pip-and-virtual-environments/> (PT)
