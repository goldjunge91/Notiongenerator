def if_function(condition, value_true, value_false):
    return value_true if condition else value_false

def ifs(*args):
    if len(args) % 2 != 1:
        raise ValueError("Ungerade Anzahl an Argumenten erwartet")
    for i in range(0, len(args) - 1, 2):
        if args[i]:
            return args[i + 1]
    return args[-1]

# Beispielanwendung der Funktionen
def test_functions():
    print(f"if_function: {if_function(True, 'Wahr', 'Falsch')}")
    print(f"if_function: {if_function(False, 'Wahr', 'Falsch')}")
    print(f"ifs: {ifs(True, 'Erster Wahr', False, 'Zweiter Wahr', 'Standard')}")
    print(f"ifs: {ifs(False, 'Erster Wahr', True, 'Zweiter Wahr', 'Standard')}")

if __name__ == '__main__':
    test_functions()
