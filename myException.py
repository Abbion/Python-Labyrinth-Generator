

class WrongEntryException(Exception):
    """Klasa wyjątku -> zwracany gdy wartość wpisana do komórki jset błędna"""
    def __init__(self, message, entry_id):
        self.__message = message
        self.__entry_id = entry_id

    def __str__(self):
        return "wrong entry error: {0}".format(self.__message)

    def get_entry_id(self):
        #Pobiera identyfikator dla pola wejściowego
        return self.__entry_id