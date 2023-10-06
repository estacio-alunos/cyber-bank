# cyber-bank

por gentileza _inserir descrição bacana aqui_

## requisitos

tem que ter python instalado e algumas bibliotecas auxiliares

- python 3.11 ou mais recente
- pipenv
- pip

use o `pip` para instalar o `pipenv`:

```bash
pip install pipenv
```

tenha um editor de códigos, o de sua preferência

- vscode
- intellij ultimate
- pycharm

seção _em construção_

## configurando

execute o comando abaixo no terminal

```bash
pipenv install --dev
```

ou use o pipenv apenas para gerar o
[requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format/):

```bash
pipenv requirements > requirements.txt 
```

e então instalar as dependências diretamente:

```bash
pip install -r requirements.txt
```

## executando

```bash
pipenv run dev
```

ou (caso instalado via requirements):

```bash
uvicorn app.main:app --reload
```

visite a url em <http://127.0.0.1:8000>

seção _em construção_

## testando

seção _em construção_

## publicando

seção _em construção_

## docs

Versão não finalizada do diagrama de caso de uso para usuários:

<img src="./docs/0.0.1-useCase.png">

seção _em construção_

## referências

- <https://pip.pypa.io/en/stable/installation/>
- <https://www.geeksforgeeks.org/how-to-install-pip-in-macos/>
- <https://fastapi.tiangolo.com/pt/#crie>
- <https://github.com/pypa/pipenv/blob/main/docs/workflows.md>
