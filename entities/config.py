class Useful:

    @classmethod
    def is_int(cls, number):
        """
        Verifica se é um número inteiro.

        """
        try:
            int(number)
        except ValueError:
            return False
        return True



    @classmethod
    def is_str(cls, text):
        """
        Verifica se é um texto.

        """
        try:
            str(text)
        except ValueError:
            return False
        return True



    @classmethod
    def check_name(cls, name):
        """
        Verifica a existencia de espaços ou "-" em uma string
        e os substitui por "_".

        :param name: string a ser verificada.
        :return: nome verificado e convertido caso
        tenha espaços ou "-" no nome.
        """
        if " " in name:
            name = name.replace(" ", "_")
        if "-" in name:
            name = name.replace("-", "_")
        return name



    @classmethod
    def check_names_in_the_list(cls, characters: list[str]) -> list[str]:
        """
        Verifica a existencia de espaços ou "-" em cada um dos elementos de uma lista
        e os substitui por "_".

        :param characters: lista de elementos a ser verificada
        :return: lista cada um dos elementos verificados e convertidos caso
        tenham espaços no nome.
        """
        no_spaces = []
        for name in characters:
            name = cls.check_name(name)
            no_spaces.append(name)
        return no_spaces

