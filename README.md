# Conversor de CSV para banco de dados SQLite 

## Sobre

O conversor gera automaticamente um arquivo ".db" do SQLite a partir de um arquivo CSV que foi passado, criando um banco de dados contendo a tabela com todas as colunas e registros do arquivo, fazendo com que cada coluna tenha um datatype adequado ao tipo de dado que ela guarda.

O programa é útil em casos onde se precisa passar os dados de um CSV para um banco de dados, afim de adquerir as vantagens que ele oferece como:
- Maior capacidade de armazenamento
- Mais facilidade de recuperar dados
- Facilidade de aplicar filtros com a linguagem SQL

## Funcionamento

O conversor recebe o caminho do arquivo CSV e então gera um arquivo SQLite com o mesmo nome do arquivo CSV, mas com "_DB" adicionado ao nome e a extenção ".db". Os arquivos gerados são criados dentro da pasta "entities/datasets".

### Classes

O programa funciona com basicamente duas entidades principais: O CSV, manipulado pela classe "CsvFile" e o banco de dados, manipulado pela classe "DataBase".

#### database.CsvFile

A classe CsvFile é responsável por fornecer todas as informações que o DataBase vai precisar para criar o banco de dados, como o nome do CSV, as colunas, o tipo de dado guardado em cada coluna e os registros guardados dentro do CSV.

#### database.DataBase

Já a classe DataBase é responsável por criar o banco de dados com todas as informações do CSV, obtendo essas informações a partir de um objeto CsvFile que lhe é passado.

Ao receber o objeto CSV, o banco de dados cria o arquivo com o mesmo nome do arquivo CSV com as alterações ditas antes. Depois de criar o arquivo, é criada a tabela de banco de dados com o nome puro do arquivo CSV, tendo a primeiro momento, apenas a coluna de "ID" com "AUTOINCREMENTE" para que cada registro inserido tenha seu ID. So então é inserido na tabela cada coluna que foi encontrada dentro do arquivo CSV, tendo seu datatype definido a partir do primeiro dado daquela coluna.

Agora, com a tabela já criada, é so adicionar cada um dos registros do CSV dentro da tabela do banco de dados e no fim exibir a quantidade de registros que foram inseridos ao banco de dados.

Depois de terminado, o arquivo do SQLite com os dados do CSV passado estarão na pasta entities/datasets.

***OBS¹**: Caso haja algum erro na criação das colunas ou o dado da coluna esteja errado no primeiro resgistro que será usado para definir o tipo da coluna, a tabela será criada de forma errada e isso so será descoberto na inserção dos registros. Criei uma função que iria verificar se existe erros nos nomes das colunas, tentando identificar se o nome tem espaços ou traços para substituir por "_". É melhor que se trate as colunas antes de tentar a conversão ou então pode ir no código adicionar o caracter do nome da coluna a função de checagem de nomes para que, sempre que ele se depare com este caracter ele o trate devidamente automaticamente.*

***OBS²**: Caso ocorra algum erro durante a criação do banco de dados, o conversor deve excluir o arquivo de banco de dados criado inicialmente para que o banco de dados com a falha não fique salvo.*

#### config.Useful

Useful guarda algumas funções úteis, como a função que define qual datatype SQLite mais se adequa ao dado do primeiro registro de cada coluna. Lá também está guardado a função que irá checar se no nome das colunas existe algum nome com espaço ou traços, já que isso iria gerar uma criação errada de colunas no banco de dados.

#### exceptions

Guarda as exceções referente a cada uma das duas entidades principais.

## Desafios

De inicio a ideia era criar uma segunda versão do outro projeto que fiz, o "from_CSV_to_SQLite", mas no meio do processo tive a ideia de "Porque não fazer um programa que transforme um arquivo CSV numa base de dados pra ter todas as vantagens de um database?". Foi quando eu comecei a quebrar a cabeça em como implementar uma logica que fosse servir pra qualquer CSV com diferentes quantidades de colunas e difernetes tipos de dados armazenadas nelas. Tive que revisar sobre SQL e os tipos de dados existentes no SQLite que são diferentes dos tipo de dados que eu havia visto no MySQL, fora ter que ver uma forma de lidar com arquivos para não recriar arquivos errados ou em diretórios errados.

Eu acabei recorrendo a alguns conceitos de POO para organizar e delegar melhor as tarefas que cada elemento do projeto deveria ter e dessa vez usei o pycharm para ajudar ainda mais com toda organização do projeto.

Também teve muitas coisas que pesquisei sobre manipulação de CSV, pandas, SQL e o SQLite para implementar algumas ideias de funções que no fim acabaram não entrando no programa final.

## Extra

O programa pode ser vir de base para algo mais completo que permita não so a conversão mas também a manipulação completa do banco de dados criado, podendo criar uma classe especifica para lidar melhor com cada registro daquele determinado CSV e ainda uma interface grafica para poder facilitar toda interação com os dados. Acabei não executando essas ideias neste projeto por não ter consegui pensar em como faria para criar uma classe que fosse se adequar aos variados tipos de CSVs que seriam recebidos, mas a ideia ainda existe e talvez eu faça uma outra versão do projeto que fosse implementar estas ideias.

## Referências usadas

Os arquivos CSV usados são totalmente fictícios e criados usando a biblioteca random do python numa pequena lista de opções de datas que eu inventei, então é tudo aleatório.

Quanto ao que eu li para poder desenvolver este pequeno projeto:

- SQlite Datatypes: https://www.sqlite.org/datatype3.html
- CSV externo usado como teste: https://www.kaggle.com/datasets/mdmahmudulhasansuzan/students-adaptability-level-in-online-education
- Sobre Exceções: https://dcc.ufrj.br/~jonathan/python/docs/Excecoes%20em%20Python.pdf
- Curso vistos: 
1. Short Class Python Oline (Let's Code)
2. Python Fundamentos para Analise de dados modulo 6: Manipulando Banco de dados com python (DSAcademy) 


Não adicionei todos que li por não lembrar de onde achei tudo. Muitas vezes eu ia pulando de site em site até achar a resposta.
