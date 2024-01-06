import argparse
from navigation.ui import menu  # Importa la funzione menu dal modulo di interfaccia utente
from navigation.apart import apart  # Importa la funzione apart dal modulo di separazione

def main():
    # Crea un parser per gestire gli argomenti da linea di comando
    parser = argparse.ArgumentParser()
    
    # Aggiunge gli argomenti necessari (path e list) al parser
    parser.add_argument("path", help="The path to navigate")
    parser.add_argument("list", help="A list of items separated by '/'")

    # Analizza gli argomenti dalla linea di comando
    args = parser.parse_args()

    # Estrae la lista dalla stringa fornita e la separa utilizzando il carattere '/'
    list_items = apart(args.list, "/")

    # Verifica se la lista è "none", in tal caso passa una lista vuota alla funzione menu
    if len(list_items) == 1 and list_items[0] == "none":
        menu(args.path, [])
    else:
        # Altrimenti, passa la lista separata alla funzione menu
        menu(args.path, list_items)

if __name__ == "__main__":
    # Se lo script è eseguito come programma principale, chiama la funzione main
    main()
