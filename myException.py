

class Wrong_entry_exception(Exception):
    """Zwracany gdy wartość wpisana do komórki jset błędna"""
    def __init__(self, message, entry_id):
        self.message = message
        self.entry_id = entry_id

    def __str__(self):
        return "wrong entry error: {0}".format(self.message)

    def get_entry_id(self):
        return self.entry_id