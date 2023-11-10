from datetime import datetime

class Number:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return Number(self.value + other.value)

class Text:
    def __init__(self, value):
        self.value = value

    def to_upper(self):
        return Text(self.value.upper())

class Date:
    def __init__(self, value=None):
        if value is None:
            self.value = datetime.now()
        else:
            self.value = value

    @staticmethod
    def current():
        return Date()

class Boolean:
    def __init__(self, value):
        self.value = bool(value)

    def negate(self):
        return Boolean(not self.value)

# Testfunktionen
def test_data_types():
    # Test für Number
    num1 = Number(10)
    num2 = Number(20)
    print(f"Addition von {num1.value} und {num2.value}: {num1.add(num2).value}")

    # Test für Text
    text = Text("Hallo Welt")
    print(f"Text in Großbuchstaben: {text.to_upper().value}")

    # Test für Date
    current_date = Date.current()
    print(f"Aktuelles Datum und Uhrzeit: {current_date.value}")

    # Test für Boolean
    boolean = Boolean(True)
    print(f"Negation von {boolean.value}: {boolean.negate().value}")

if __name__ == "__main__":
    test_data_types()
