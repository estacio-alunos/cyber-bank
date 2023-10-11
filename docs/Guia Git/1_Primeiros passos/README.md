# Guia Git: primeiros passos.

Git é um sistema de controle de versão de arquivos/projeto. Sua documentação se encontra no site **[Git](https://git-scm.com/docs/git/pt_BR).**

**No geral, esse pode ser um processo comum:**

- Clonando um repositório para o seu ambiente local usando o comando **`git clone`** OU Iniciando seu próprio projeto, que acabou de começar com o comando `**git init**`
- É uma boa prática criar branch (ramificação) para trabalhar no seu recurso ou correção usando o comando **`git branch nome-do-branch`** e mude para esse branch usando **`git checkout nome-do-branch`**
- Realizando as alterações necessárias no código do projeto no seu ambiente local, ou até mesmo adicionando novas funcionalidades
- Adicione alterações com o `git add`
- Quando você terminar de fazer alterações significativas, crie um commit usando **`git commit -m "Mensagem do commit"`** para registrar as alterações
- E enviar o branch comitado para o seu repositório usando **`git push origin nome-do-branch`**
- No GitHub, vá para o repositório e clique em "New pull request" (Nova requisição de envio) para criar uma nova pull request. Escolha o branch comitado como a base e selecione o branch original como o branch de comparação
- Solicite revisões de código de outras pessoas da equipe. Elas poderão fazer comentários, sugestões ou aprovar as alterações
- Com base nos comentários recebidos, faça as alterações necessárias no seu branch local e faça um novo commit. O branch atualizará automaticamente na pull request
- Após receber as aprovações necessárias, você poderá mesclar o branch na branch original usando o botão "Merge pull request" (Mesclar requisição de envio) no GitHub

<br><br>

# PRIMORDIALMENTE COMO PRIMEIRA AÇÃO

Primeiramente, como em qualquer novo projeto, devemos criar um ambiente virtual(ou simplesmente **env**). Em Python, um ambiente virtual é um espaço isolado onde você pode instalar e gerenciar as dependências de um projeto, isso é útil para evitar conflitos entre as dependências de diferentes projetos. Eu particularmente uso e gosto da criação via [Anaconda](https://www.anaconda.com/about-us), mas vocês podem criar com outros comandos:

## Por exemplo, a forma nativa no Python, no terminal em seu diretório:

```bash
python -m venv env
```

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled.png)

1. Comando:

    “env” o ultimo parâmetro é o nome dado a pasta que ficará o ambiente e suas dependências e mais algumas coisa que não vem ao mérito no momento.

2. Diretório vazio, criado para todo esse guia
3. O diretório e subdiretórios criados após o comando.

## **Da forma que eu prefiro, com o Anaconda:**

Se houver interesse, a instalação é mais complexa em outros OS diferentes de Windowns, **[Download](https://www.anaconda.com/download)**.

```bash
conda create --name "nome_que_escolher" python=3.
```

**Passo 1**

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%201.png)

Comando, o “python=3.” garante a instalação do python que você tem instalado em sua máquina

**Passo 2**

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%202.png)

Aceitar que ele faça algumas instalações

**Passo 3**

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%203.png)

Comando para ativar o Ambiente

**Passo 4**

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%204.png)

O ambiente vai demonstrar em seu terminal, provavelmente entre parentese (comando-git),

antes ou depois do path do diretório e, que você está.

## Ou da forma na qual está descrito no readme, do nosso projeto: [**Link**](https://github.com/estacio-alunos/cyber-bank/blob/main/README.md)

<br><br>

# ESTÁGIO INICIAL

## Iniciando repositório

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%205.png)

**`git init`** Cria um novo repositório Git no diretório atual.

Inicializa um novo repositório Git, criando um diretório oculto **`.git`** que armazena todas as informações do controle de versão.

```bash
git init
```

1. Comando

    Resposta que foi inicializado um repositório git com sucesso.

2. O comando que eu dei é de Linux, mas o “.git” está em azul e isso representa que é um arquivo oculto(nessa distribuição de linux que uso).
3. O diretório vazio, mostrando que realmente não tem nada visível.

## Clonando repositório do Github

Ao criar, ele tem varias opções para vincular o diretório remoto com o local, porém vamos com o comandos que nos interessa:

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%206.png)

**`git clone`** Clona (faz uma cópia) de um repositório Git existente para o seu ambiente local.

Este comando, pode nos deixar no mesmo ponto inicial do `git init`, para demonstrar isso, eu criei um diretório em meu Github para demonstar o comando de clone via comando. O exemplo com Github Desktop, não é contemplado aqui.

```bash
git clone https://github.com/MiguelHCJS/comandos-git.git
```

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%207.png)

Cria uma cópia local do repositório remoto em seu ambiente de trabalho, incluindo todo o histórico de commits.

Repositório criado manualmente no computador, após **`git init`**

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%205.png)

Repositório criado e clonado do Github, via comando. Obs.: O diretório em que estiver, é exatamente onde ele fará o clone, se estiver na pasta de Documentos da maquina, assim o fará, o clonará para Documentos.

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%208.png)

No Git clone, lembresse que de qualquer forma o primeiro passo de criar o ambiente virtual é crucial. Você precisaria ter criado e pode ativá-lo após o clone, o que não pode ser feito é começar a baixar dependencias e instalar coisas sem ele estar ativo.

## Configurando repositório remoto

**`git remote`** Gerencia as conexões com repositórios remotos.

Lembra do que criamos de forma manual? Então, digamos que não queria fazer um clone… Você já tem um diretório e quer vincular ao repositório remoto que criamos anteriormente, ela ainda está vazia:

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%209.png)

Mas antes de prosseguir, terá que fazer um ajuste… Eu não sei porque, mas aprendi depois de quebrar um pouco de cabeça, você precisa ajustar a “branch” padrão que é criada quando você cria o novo repositório no github. É provavel que você tenha que excluir esse repositório que você fez acompanhando esse guia, ajustar o que vou lhes mostrar agora e depois criar outro repositório e seguir o comando de **`git remote`**, vamos lá:

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%2010.png)

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%2011.png)

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%2012.png)

**Renomei para main**

Agora pode seguir, criando um novo repositório(pois se teve que mudar esse nome, o antigo repositório pode dar falha ao ser configurado como remoto.

Retomando nossa configuração do comando **`git remote`**

Adicionei um arquivo na pasta que criamos manualmente e demos o **`git init`**

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%2013.png)

No terminal, focado nessa pasta e com o ambiente virtual ativo, dei os seguintes comandos:

![Untitled](Guia%20Git%20primeiros%20passos%20c20b184d92ee4bc49b939c911925818e/Untitled%2014.png)

```bash
git remote add origin https://github.com/MiguelHCJS/comandos-git.git
```

O comando **`git remote`** é usado para gerenciar as conexões com repositórios remotos. Ele permite adicionar, listar ou remover repositórios remotos associados ao seu projeto local.

Se as respostas foram essas e não ocorreu nenhum erro, PARABÉNS! Conseguiu configurar a ‘branch’ padrão, conseguiu vincular um repositório remoto!

O comando **`git remote`** é uma ferramenta fundamental para configurar e gerenciar conexões com repositórios remotos, possibilitando a colaboração eficaz em projetos distribuídos. Certifique-se de entender como usar esse comando para configurar corretamente os repositórios remotos em seus projetos.
