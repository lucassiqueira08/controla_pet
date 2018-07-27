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


![alt text](https://lh4.googleusercontent.com/5k4WMnoVQgw52GA6TrWhDv9ALAN20mTdc6S-SgUBQMigshGw0NAJ1Mnhg-XeIIqcuOXY-5IoD3Lv9RAitFbt=w1317-h648-rw "GitFlow")

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

#### Rodando o projeto

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
