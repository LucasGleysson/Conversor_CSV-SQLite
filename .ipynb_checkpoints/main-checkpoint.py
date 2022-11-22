import os.path

from entities.database import CsvFile
from entities.database import DataBase
from entities.exceptions import *


def create_db_and_table_first_time(path_csv):
    file = CsvFile(path_csv)
    try:
        file.reader()
        database = DataBase(file)
        database.create_table()

        for register in file.reader()[1:]:
            try:
                database.insert(register)
            except Exception as ex:
                message = f"{ex}"
                raise ExceptionDataBase(message)
        print(f"Adicionados {len(database.recover_all())} registros ao banco de dados.")

    except FileNotFoundError:
        message = "Arquivo Não encontrado"
        print(message)

    except Exception as ex:
        path_database = f"entities/datasets/{file.name()+'_DB.db'}"
        if os.path.exists(path_database):
            os.remove(path_database)
        print(ex)



def check_first_access_file(path_csv):
    file = CsvFile(path_csv)
    to_check_path_database = file.name()+'_DB.db'

    if "entities/datasets/" not in to_check_path_database:
        to_check_path_database = "entities/datasets/" + to_check_path_database
    if not os.path.exists(to_check_path_database):
        create_db_and_table_first_time(path_csv)
    else:
        print("O banco de dados deste CSV já existe!.")
        print(f"Caminho: {to_check_path_database}")

        delete = input("Deletar? (Y/N)")
        while delete.upper() not in ("N", "Y"):
            print("Escola apenas as opções informadas! ")
            delete = input("New CSV? (Y/N) ")
        if delete.upper() == "Y":
            os.remove(to_check_path_database)




def start():
    print("+++++++{From CSV to SQLite}+++++++")
    while True:
        path_file_csv = input("Enter CSV path: ")
        check_first_access_file(path_file_csv)
        print("++++++++++++++++++++++++++++++++++")

        r = input("New CSV? (Y/N) ")
        while r.upper() not in ("N", "Y"):
            print("Escola apenas as opções informadas! ")
            r = input("New CSV? (Y/N) ")
        if r.upper() == "N":
            break
        print("++++++++++++++++++++++++++++++++++")



start()
