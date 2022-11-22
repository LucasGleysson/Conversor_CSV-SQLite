{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "50e6e013-ae38-4651-890f-1c8193155eaf",
   "metadata": {},
   "source": [
    "# Conversor de CSV para banco de dados SQLite "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5de179cd-af92-465a-b02e-9a55799cab5e",
   "metadata": {},
   "source": [
    "## Sobre"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "934bb5e1-1a2a-4836-8f7f-606287a6f9ef",
   "metadata": {},
   "source": [
    " O conversor gera automaticamente um arquivo \".db\" do SQLite a partir de um arquivo CSV que foi passado, criando um banco de dados contendo a tabela com todas as colunas e registros do arquivo, fazendo com que cada coluna tenha um datatype adequado ao tipo de dado que ela guarda."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b35e20c8-e7e6-4db4-a1b7-b162b1029896",
   "metadata": {},
   "source": [
    "O programa é útil em casos onde se precisa passar os dados de um CSV para um banco de dados, afim de adquerir as vantagens que ele oferece como:\n",
    "- Maior capacidade de armazenamento\n",
    "- Mais facilidade de recuperar dados\n",
    "- Facilidade de aplicar filtros com a linguagem SQL\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "796c1629-d9a2-4908-be32-a9eefa1023b6",
   "metadata": {},
   "source": [
    "## Funcionamento"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b075ed72-5439-4ff4-a0cb-deb69a99007e",
   "metadata": {},
   "source": [
    "O conversor recebe o caminho do arquivo CSV e então gera um arquivo SQLite com o mesmo nome do arquivo CSV, mas com \"_DB\" adicionado ao nome e a extenção \".db\". Os arquivos gerados são criados dentro da pasta \"entities/datasets\"."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d764861d-8b98-4fa8-bd93-6d659c9ec9ae",
   "metadata": {},
   "source": [
    "### Classes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a050f8db-3f55-47bc-abc1-7daad0e50979",
   "metadata": {},
   "source": [
    "O programa funciona com basicamente duas entidades principais: O CSV, manipulado pela classe \"CsvFile\" e o banco de dados, manipulado pela classe \"DataBase\"."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "759e7e05-ecc1-42ec-87ec-7404d4f00924",
   "metadata": {},
   "source": [
    "#### database.CsvFile"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "68c92027-8bcf-4874-a6e7-d61df3fad17b",
   "metadata": {},
   "source": [
    "A classe CsvFile é responsável por fornecer todas as informações que o DataBase vai precisar para criar o banco de dados, como o nome do CSV, as colunas, o tipo de dado guardado em cada coluna e os registros guardados dentro do CSV."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "421d8cf7-4fad-4aec-9e26-f5212ac24101",
   "metadata": {},
   "source": [
    "#### database.DataBase"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "83fd6ce2-554a-4bfb-84cb-e0407bf6a76d",
   "metadata": {},
   "source": [
    "Já a classe DataBase é responsável por criar o banco de dados com todas as informações do CSV, obtendo essas informações a partir de um objeto CsvFile que lhe é passado."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d433f2cd-5745-4397-9e9a-a910a1f00d9c",
   "metadata": {},
   "source": [
    "Ao receber o objeto CSV, o banco de dados cria o arquivo com o mesmo nome do arquivo CSV com as alterações ditas antes. Depois de criar o arquivo, é criada a tabela de banco de dados com o nome puro do arquivo CSV, tendo a primeiro momento, apenas a coluna de \"ID\" com \"AUTOINCREMENTE\" para que cada registro inserido tenha seu ID. So então é inserido na tabela cada coluna que foi encontrada dentro do arquivo CSV, tendo seu datatype definido a partir do primeiro dado daquela coluna."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9bcaedfc-5658-4780-bcd1-7f1066692c0b",
   "metadata": {},
   "source": [
    "Agora, com a tabela já criada, é so adicionar cada um dos registros do CSV dentro da tabela do banco de dados e no fim exibir a quantidade de registros que foram inseridos ao banco de dados."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6fda2e85-c9fa-4c20-ac45-b9cc7b9ccf4b",
   "metadata": {},
   "source": [
    "Depois de terminado, o arquivo do SQLite com os dados do CSV passado estarão na pasta entities/datasets."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26f77337-4052-4627-9d12-765f26566b51",
   "metadata": {},
   "source": [
    "***OBS¹**: Caso haja algum erro na criação das colunas ou o dado da coluna esteja errado no primeiro resgistro que será usado para definir o tipo da coluna, a tabela será criada de forma errada e isso so será descoberto na inserção dos registros. Criei uma função que iria verificar se existe erros nos nomes das colunas, tentando identificar se o nome tem espaços ou traços para substituir por \"_\". É melhor que se trate as colunas antes de tentar a conversão ou então pode ir no código adicionar o caracter do nome da coluna a função de checagem de nomes para que, sempre que ele se depare com este caracter ele o trate devidamente automaticamente.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6c37b60-d204-4f71-b217-7a5a6b37e3b1",
   "metadata": {},
   "source": [
    "***OBS²**: Caso ocorra algum erro durante a criação do banco de dados, o conversor deve excluir o arquivo de banco de dados criado inicialmente para que o banco de dados com a falha não fique salvo.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a71ea76-a5f9-454c-991c-1af8599b4c17",
   "metadata": {},
   "source": [
    "#### config.Useful"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db66eb0e-1fce-4644-bd53-2ae9439e43ab",
   "metadata": {},
   "source": [
    "Useful guarda algumas funções úteis, como a função que define qual datatype SQLite mais se adequa ao dado do primeiro registro de cada coluna. Lá também está guardado a função que irá checar se no nome das colunas existe algum nome com espaço ou traços, já que isso iria gerar uma criação errada de colunas no banco de dados."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "75e09818-643b-490f-a42d-a4df358150ce",
   "metadata": {},
   "source": [
    "#### exceptions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2faf82a7-500c-40e2-8cb3-87e611f02bdf",
   "metadata": {},
   "source": [
    "Guarda as exceções referente a cada uma das duas entidades principais."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4ffd96da-ff05-44a7-86e3-57fbd87faf15",
   "metadata": {},
   "source": [
    "## Desafios"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6349f118-2775-4d16-95bc-d22ebb59cf43",
   "metadata": {},
   "source": [
    "De inicio a ideia era criar uma segunda versão do outro projeto que fiz, o \"from_CSV_to_SQLite\", mas no meio do processo tive a ideia de \"Porque não fazer um programa que transforme um arquivo CSV numa base de dados pra ter todas as vantagens de um database?\". Foi quando eu comecei a quebrar a cabeça em como implementar uma logica que fosse servir pra qualquer CSV com diferentes quantidades de colunas e difernetes tipos de dados armazenadas nelas. Tive que revisar sobre SQL e os tipos de dados existentes no SQLite que são diferentes dos tipo de dados que eu havia visto no MySQL, fora ter que ver uma forma de lidar com arquivos para não recriar arquivos errados ou em diretórios errados."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "34a4bbd4-df8a-4b67-ae08-80abfdd4eaa4",
   "metadata": {},
   "source": [
    "Eu acabei recorrendo a alguns conceitos de POO para organizar e delegar melhor as tarefas que cada elemento do projeto deveria ter e dessa vez usei o pycharm para ajudar ainda mais com toda organização do projeto."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00dc0126-02fe-4637-a8a0-3617f9a50540",
   "metadata": {},
   "source": [
    "Também teve muitas coisas que pesquisei sobre manipulação de CSV, pandas, SQL e o SQLite para implementar algumas ideias de funções que no fim acabaram não entrando no programa final."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "806afe74-2858-4a8e-83ac-9c5c4d52692d",
   "metadata": {},
   "source": [
    "## Extra"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a287909-bd8b-44cc-b8ef-545a05699e83",
   "metadata": {},
   "source": [
    "O programa pode ser vir de base para algo mais completo que permita não so a conversão mas também a manipulação completa do banco de dados criado, podendo criar uma classe especifica para lidar melhor com cada registro daquele determinado CSV e ainda uma interface grafica para poder facilitar toda interação com os dados. Acabei não executando essas ideias neste projeto por não ter consegui pensar em como faria para criar uma classe que fosse se adequar aos variados tipos de CSVs que seriam recebidos, mas a ideia ainda existe e talvez eu faça uma outra versão do projeto que fosse implementar estas ideias."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f492ac1f-2bd4-4e3c-8a18-42895b51c677",
   "metadata": {},
   "source": [
    "## Referências usadas"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "650674fb-14a8-49fd-9718-3048fcf3c05c",
   "metadata": {},
   "source": [
    "Os arquivos CSV usados são totalmente fictícios e criados usando a biblioteca random do python numa pequena lista de opções de datas que eu inventei, então é tudo aleatório."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a4154d48-568b-48a5-842f-0f8fb17164d1",
   "metadata": {},
   "source": [
    "Quanto ao que eu li para poder desenvolver este pequeno projeto:\n",
    "\n",
    "- SQlite Datatypes: https://www.sqlite.org/datatype3.html\n",
    "- CSV externo usado como teste: https://www.kaggle.com/datasets/mdmahmudulhasansuzan/students-adaptability-level-in-online-education\n",
    "- Sobre Exceções: https://dcc.ufrj.br/~jonathan/python/docs/Excecoes%20em%20Python.pdf\n",
    "- Curso vistos: \n",
    "1. Short Class Python Oline (Let's Code)\n",
    "2. Python Fundamentos para Analise de dados modulo 6: Manipulando Banco de dados com python (DSAcademy) \n",
    "\n",
    "\n",
    "Não adicionei todos que li por não lembrar de onde achei tudo. Muitas vezes eu ia pulando de site em site até achar a resposta."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
