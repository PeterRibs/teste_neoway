# Manipulação de dados

Projeto para o processo seletivo para concorrer a vaga de Analista de Desenvolvimento de Sistemas Júnior da empresa Neoway.
Serviço de manipulação de dados integrado a um base de dados relacional PostgreSQL.

## Tecnologias utilizadas

- Python 
- PostgreSQL
- Docker compose

## O projeto

Etapas do projeto:
- Ler o arquivo txt com separador não-convencional entre as colunas (readtable).
- Manipular os dados a fim de produzir uma tabela com separador convencional entre as colunas, somente os dígitos numéricos dos CPFs e CNPJs e utilizando '.' ao invés ',' para separar decimal (datamanagement).
- Validar os registros (CPF e CNPJ) em seus respectivos campos em quantidade de dígitos, igualdade de todos os dígitos e validação dos dois últimos dígitos. Com isso, produzi duas tabelas diferentes, sendo a primeira coluna de cada tabela o identificador (CPF ou CNPJ) e a segunda coluna a validação (0 ou 1) (datavalidation). 
- Integração com o banco de dados relacionais da tabela geral e das tabelas de validação das IDs (insertdata).
- A aplicação completa foi inserida no arquivo app.py e rodada utilizando o arquivo run_app.py.
- Utilizar getdata.py para consultar a tabela no banco de dados.  

Para as etapas, utilizei PostgreSQL 14.2 para a base de dados relacional, a linguagem Python 3.9 (pacotes pandas, ramdom, psycopg2) criando diferentes arquivos utilizando classes no intuito de minimizar a quantidade de código escrita e aumentar a performance da aplicação e Docker compose para rodar e compartilhar aplicação.

## Setup

- Instalação do Docker: https://docs.docker.com/compose/
- Instalação do PostgreSQL: https://www.postgresql.org/

Após as instalações é preciso realizar o download das respectivas imagens no Docker.
- `docker pull python` - Imagem de Python
- `docker pull postgres` - Imagem de PostgreSQL

## Scripts

- `docker-compose up --build   ` - Aciona o serviço, construindo a aplicação 

No arquivo run_app.py é preciso adicionar dois argumentos na função:
- `app().all_process(arg1, arg2, arg3, arg4)`
  - arg1 -> Nome do banco de dados que irá persistir os dados 
  - arg2 -> User PostgreSQL
  - arg3 -> Senha PostgreSQL 
  - arg4 -> Nome da tabela inicial que será utilizada para realizar a manipulação

## Próximos passos 

- Com o aumento da complexidade uma possibilidade é trabalhar com injeção de dependências
- Criação de testes unitários
- Criar dinamicidade da tabela baseado no nome das colunas
