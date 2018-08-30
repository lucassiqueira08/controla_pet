ControlaPet
--------------------------------------------------------------------------

ControlaPet é um Sistema de Gerenciamento de PetShops e Clinicas Veterinarias  desenvolvido por:


* Bruno Lima dos Santos  
* Isaque Felizardo
* Lucas Alves Siqueira
* Lucas Araujo de Oliveira
* Nayara de Paula Muniz
* Vitor Crepaldi Carlessi    




### Quickstart

---

#### Clone este repositório:

```sh
    git clone https://github.com/ControlaPet/controla_pet.git
```

---


#### Fluxo de Desenvolvimento da equipe

* **master** - Branch utilizado somente para funcionalidades já testadas e aprovadas pelo cliente
* **develop** - Branch que consiste no desenvolvimento atual da equipe

* **features** - Demais funcionalidades que estão sendo desenvolvidas


![alt text](https://www.bitbull.it/blog/git-flow-come-funziona/gitflow-1.png "GitFlow")
__fonte__: https://www.bitbull.it/blog/git-flow-come-funziona/gitflow-1.png

**SEMPRE**:
* Para novas funcionalidades utilize: feature/nome_da_func
* Para melhorias no codigo: bugfix/nome_da_correcao

---




#### Trabalhe na branch correta

Para visualizar todas as branches:
```sh
    git branch -a
```


Utilize uma branch já existente:
```sh
    git checkout <nome_da_branch>
```

Ou crie uma nova para a sua funcionalidade:
```sh
    git checkout -b <nome_da_branch>

    <Exemplo>
    git checkout -b DBconnection
```

Certifique-se de que sua branch está atualizada:
```sh
    git pull origin <nome_da_branch_mais_att>

    <Exemplo>
    git pull origin develop
```
---


#### Adicione suas credenciais
Para trabalhar com o projeto ControlaPet, crie um arquivo chamado .env na raiz do diretorio, e
adicione as credenciais fornecidas pela **equipe de desenvolvimento**.


---
#### Rodando o projeto com Docker Compose

Docker é uma tecnologia que fornece containers que isolam processos, com a ajuda do Docker Compose é possível orquestrar containers e subir aplicações complexas com poucos comandos.  

Instalação do Docker no Windows: [https://docs.docker.com/docker-for-windows/install/](https://docs.docker.com/docker-for-windows/install/)

Instalação do Docker Compose no Linux: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

Para dar privilégios ao docker no Linux:

```sh
   sudo chmod 777 /var/run/docker.sock
```

**Iniciando o projeto**

Atualize o repositorio local
```sh
    git pull origin develop
```
Para iniciar o projeto:

```sh
    docker-compose up
```
Ao rodar o projeto, o mysql será iniciado e, logo após, a app migrará para o banco de dados e irá subir o servidor.



**Informações adicionais:**

Para acessar containers utilize:
```sh
    docker exec -it <container-name> bash
    
    <Exemplo>
    docker exec -it sys_controla_pet bash

```
Para derrubar containers:
```sh
    docker-compose down
```

**Não esqueça:**
* Sem as credenciais (.env), o projeto não será iniciado
* Sem privilegios de administrador talvez algum erro seja exibido
* O MYSQL estará rodando na porta 3308, para evitar conflitos com a porta padrão do mysql local, portanto ao optar por softwares como Mysql Workbench utilize:
    * Host: localhost
    * Port: 3308
    * User: root
    * Password: (A mesma da credencial)

---
#### Rodando o projeto sem docker

*Obs:* O MYSQL deve estar instalado.

Apaga todos os arquivos da pasta migrations, exceto init.py, de cada APP, em seguida execute o comando a seguir para identificar migrações:
```sh
    python manage.py makemigrations
```

Em seguida, digite o comando abaixo para realizar as migrações para o banco de dados:

```sh
    python manage.py migrate
```

Ao editar arquivos, digite o comando abaixo para identificar erros:
```sh
    python manage.py check
```

Para criar um usuario que acesse a pagina administrativa utilize:
```sh
    python manage.py createsuperuser
```

Para rodar o projeto digite:
```sh
    python manage.py runserver
```
Por padrão o servidor é iniciado no endereço: [http://localhost:8000/](http://localhost:8000/)


---


#### Subindo alterações
Certifique-se novamente de que está utilizando a versão mais atual do cógido:

```sh
    git pull origin <nome_da_branch_mais_att>

    <Exemplo>
    git pull origin develop
```


Para verificar o situação atual do repositório
```sh
    git status
```
Se houver alterações a serem commitadas **NÃO** utilizar **" git add ."**, digite:
```sh
    git add <nome_do_arquivo_alterado>
```

Para commitar as alterações por favor digite uma **MENSAGEM COERENTE** com o que foi desenvolvido:
```sh
    git commit -m "Mensagem Coerente"

    <Exemplo>
    git commit -m "Conexao com o Banco de Dados remoto"
```

Para subir suas alterações ao GitHub, digite:

```sh
    git push origin <nome_da_sua_branch>

    <Exemplo>
    git push origin DBconnection
```
**JAMAIS**:
* Dê push direto no develop e master
* Utilize o develop/master como branch para desenvolver
* Digite mensagens em commits sem sentido
* Force um commit com conflitos

---
