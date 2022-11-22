import sqlite3
import csv
import pandas as pd
from entities.config import Useful
from entities.exceptions import *


class CsvFile:
    """
    Manipula o arquivo CSV recebido.
    """

    def __init__(self, csv_path: str):
        """
        Cria um objeto CsvFile.

        :param csv_path: caminho do arquivo CSV.
        """
        self.path = csv_path


    def name(self) -> str:
        """
        Retorna o nome do arquivo CSV que foi passado no "csv_path".
        """
        name = str(self.path)
        try:
            if "/" in name:
                name = name.split("/")
                name = name[len(name) - 1]
            elif "\\" in name:
                name = name.split("\\")
                name = name[len(name) - 1]
            name = name[:name.find(".")]
            return name

        except Exception as ex:
            message = f"Erro ao tentar capturar o nome do arquivo \nErro: {ex}"
            raise ExceptionCSV(message)


    def reader(self) -> list:
        """
        Lê o arquivo CSV e devolve uma lista dos dados do arquivo.
        """
        data_file = []
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    data_file.append(row)

        except FileNotFoundError as ex:
            message = f"Erro ao encontrar o arquivo! \nErro: {ex}"
            raise ExceptionCSV(message)

        except Exception as ex:
            message = f"Erro ao tentar ler o arquivo! \nErro: {ex}"
            raise ExceptionCSV(message)

        return data_file


    def column_type_sqlite(self) -> list[tuple]:
        """
        Retorna as colunas existentes no CSV e o tipo de dado daquela coluna
        com base nos tipo de dados aceitos pelo SQLite3.

        :return: column_type[(coluna, tipo)]
        """
        data = pd.read_csv(self.path)
        columns = list(data.columns)
        column_type = []
        try:
            for i, c in enumerate(columns):
                dt = data[columns[i]][0]
                if "." in str(dt):
                    cl_type = "REAL"
                elif Useful.is_int(dt):
                    cl_type = "INTEGER"
                elif Useful.is_str(dt):
                    cl_type = "TEXT"
                else:
                    cl_type = "BLOB"
                column_type.append((c, cl_type))
            return column_type

        except Exception as ex:
            message = f"Erro ao tentar capturar o nome e o tipo dos dados \nErro: {ex}"
            raise ExceptionCSV(message)


class DataBase:
    """
    Classe resposável pelo manuseio dos dados no banco de dados.
    """

    def __init__(self, file: CsvFile):
        """
        Cria um objeto DataBase onde vai trabalhar em cima do arquivo CSV
        passado.

        :param file: Objeto CsvFile criado a partir do caminho do arquivo
        CSV a ser usado.
        """
        self._csv_file = file
        try:
            self.__connection = sqlite3.connect(f'entities/datasets/{self._csv_file.name()}_DB.db')
            self.__cursor = self.__connection.cursor()

        except Exception as ex:
            message = f"Falha ao tentar criar o banco de dados! \nErro: {ex}"
            raise ExceptionDataBase(message)


    def create_table(self):
        """
        Cria a tabela a partir do arquivo csv caso ainda não exista,
        usando como referencia, as colunas e dados existente no arquivo CSV.
        """

        # Primeiro: cria a tabela no banco de dados apenas com a coluna ID
        table_name = self._csv_file.name()
        try:
            sql_query = f"CREATE TABLE IF NOT EXISTS {table_name}" \
                        " (id INTEGER PRIMARY KEY AUTOINCREMENT)"
            self.__cursor.execute(sql_query)
            self.__connection.commit()

        except Exception as ex:
            message = f"Falha ao tentar criar a tabela no banco de dados! \nErro: {ex}"
            raise ExceptionDataBase(message)

        # Segundo: popula a tabela do banco de dados com cada uma das colunas do CSV
        # conseguindo assim se adaptar mediante a quantidade de colunas do CSV.
        try:
            for row in self._csv_file.column_type_sqlite():
                column = Useful.check_name(row[0])
                column_type = row[1]
                try:
                    sql_query = f"ALTER TABLE {table_name} ADD {column} {column_type}"
                    self.__cursor.execute(sql_query)
                    self.__connection.commit()

                except sqlite3.OperationalError as ex:
                    message = f"{ex}"
                    raise ExceptionDataBase(message)

        except Exception as ex:
            message = f"Erro durante a inserção das colunas no banco de dados! \nErro: {ex}"
            raise ExceptionDataBase(message)


    def insert(self, row: list):
        """
        Insere os dados, passados em forma de lista, no banco de dados.

        :param row: dados a serem inseridos no banco de dados seguindo a
        sequencia das colunas.
        """
        file = self._csv_file
        columns = [str(column) for column, _ in file.column_type_sqlite()]
        columns = Useful.check_names_in_the_list(columns)
        qnt_columns = len(columns)
        columns = ", ".join(columns)
        qnt_values_insert = []

        # Adiciona um coringa para cada coluna que existir no CSV,
        # logo depois junta todas em uma unica string, as juntando com ", "
        # completando assim a query de INSERT
        for qnt in range(qnt_columns):
            qnt_values_insert.append("?")
        qnt_values_insert = ",".join(qnt_values_insert)

        try:
            sql_insert = """INSERT INTO {} ({}) 
                    VALUES ({})""".format(file.name(), columns, qnt_values_insert)
            row = tuple(row)
            self.__cursor.execute(sql_insert, row)
            self.__connection.commit()

        except Exception as ex:
            message = f"Erro: Falha durante a inserção de registros! \nErro: {ex}"
            raise ExceptionDataBase(message)


    def last_insert_id(self) -> int:
        """
        Retorna o ID do último registo inserido.
        """
        try:
            sql_select = f"""SELECT LAST_INSERT_ROWID() AS ID"""
            self.__cursor.execute(sql_select)
            id_insert = int(self.__cursor.fetchall()[0][0])
            return id_insert

        except Exception as ex:
            message = f"Falha ao tentar retornar o ID do último registro inserido \nErro: {ex}"
            raise ExceptionDataBase(message)


    def recover_all(self) -> list:
        """
        Regata todos os registros existentes no banco de dados
        os retornando em um iterável
        """
        try:
            table = self._csv_file.name()
            sql_select = f"""SELECT * FROM {table}"""
            self.__cursor.execute(sql_select)
            found = self.__cursor.fetchall()
            return found

        except Exception as ex:
            message = f"Falha ao tentar resgatar todos os registros! \nErro: {ex}"
            raise ExceptionDataBase(message)


    def close_db(self):
        """
        Fecha a conexão com o banco de dados e o cursor.
        """
        try:
            self.__cursor.close()
            self.__connection.close()

        except Exception as ex:
            message = f"Falha ao tentar fechar o banco de dados! \nErro: {ex}"
            raise ExceptionDataBase(message)
