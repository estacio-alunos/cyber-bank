# Git Clone

Sei que o momento vai chegar, mas acredito que seja interessante mostrar algumas coisinhas que podem facilitar a interpretação da estrutura do nosso projeto.

Foi solicitado o “Hello World” com o Django, para isso eu precisava ter o repositório de forma local, para instalar, modificar e testar…

Então segue os passos que eu fiz e o que usei para isso:

O GitHub Desktop vai ajudar no processo e também a entender como clonar o repositório de forma local, para trabalho. Para aqueles que estão começando com Git. É uma forma de lidar com o Git de forma interativa.

1. Este é o programa [https://desktop.github.com/](https://desktop.github.com/)
2. Após sua instalação e logar com sua conta Github

**Clone o repositório do projeto**

Passo 1 - Pegar o link do repositório para clonar

![clonando repositorio.png](Git%20Clone%20e5a2af9b4ebe4d49b13f977d80917ae8/clonando_repositorio.png)

Passo 2 - Clonar localmente via Github Desktop

![github_desktop1.png](Git%20Clone%20e5a2af9b4ebe4d49b13f977d80917ae8/github_desktop1.png)

Passo 3 ****- Abrir na IDE Vscode

![Untitled](Git%20Clone%20e5a2af9b4ebe4d49b13f977d80917ae8/Untitled.png)

OBS.: Se não usar o Vscode, é possível abrir sua IDE de preferência e abrir o diretório, normalmente.

Passo 4 - Criar uma branch, quando for necessário

![criando branch.png](Git%20Clone%20e5a2af9b4ebe4d49b13f977d80917ae8/criando_branch.png)

### **Hello World com Django!**

![Untitled](Git%20Clone%20e5a2af9b4ebe4d49b13f977d80917ae8/Untitled%201.png)

---

### Estrutura e uma breve explicação de alguns módulos

![Untitled](Git%20Clone%20e5a2af9b4ebe4d49b13f977d80917ae8/Untitled%202.png)

![Untitled](Git%20Clone%20e5a2af9b4ebe4d49b13f977d80917ae8/Untitled%203.png)

![Untitled](Git%20Clone%20e5a2af9b4ebe4d49b13f977d80917ae8/Untitled%204.png)

![Untitled](Git%20Clone%20e5a2af9b4ebe4d49b13f977d80917ae8/Untitled%205.png)

![Untitled](Git%20Clone%20e5a2af9b4ebe4d49b13f977d80917ae8/Untitled%206.png)

---

### Requirements necessários para rodar a aplicação após clonar

```python
"""
Garantam que esteja ativa o env 'dev'

Eu uso outra ferramente, diferente da pipenv, mas sigam os passos descritos no github
E só depois instale o django com o comando abaixo
Para evitar que seu ambiente global tenha coisas demais, instaladas e outras implicações
"""

pip install django
```

```python
"""
APÓS CLONAR, NO TERMINAL DENTRO DO VSCODE(OU OUTRA IDE, GARANTA APENAS QUE O TERMINAL ESTEJA NA RAIZ DO DIRETÓRIO), DIGITAR:
"""

python manage.py runserver

"""
Depois é só clicar no endereço que aparecerá no terminal, ou digitá-lo no navegador: http://127.0.0.1:8000/
"""
```