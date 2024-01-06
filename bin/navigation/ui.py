import os
import questionary

from navigation.file import *  # Importa funzioni dal modulo file del pacchetto di navigazione

def menu(path, suffix_list):
    # Verifica se il percorso inizia con un punto e aggiusta il percorso in base al sistema operativo
    if path[0] == ".":
        path = path[1:]
        path = os.getcwd().replace("\\", "/") + path

    # Controlla se il percorso non è vuoto
    if path:
        # Ottiene la lista di elementi (file e cartelle) nel percorso fornito
        list_temp = os.listdir(path)
        # Filtra solo le cartelle dalla lista
        folder = [item for item in list_temp if isFolder(os.path.join(path, item))]

        # Determina quali elementi devono essere visualizzati in base alla presenza di un elenco di suffissi
        if len(suffix_list) == 0:
            list_to_display = list_temp
        else:
            # Filtra le cartelle che contengono file con i suffissi desiderati
            list_to_display = [
                item for item in folder if have_py_in_folder(os.path.join(path, item) + "/", suffix_list)
            ] + [item for item in list_temp if isSuffix(item, suffix_list)]

        # Aggiunge opzioni aggiuntive alla lista visualizzata
        list_to_display.extend([">back<", ">quit<"])

        # Crea il titolo per la finestra di selezione
        title = f"Current Path: {path}\nPlease choose a python file or directory (press SPACE to mark, ENTER to continue): "
        # Utilizza questionary.checkbox per ottenere la selezione multipla dell'utente
        selected = questionary.checkbox(title, choices=list_to_display).ask()

        # Esegue l'elaborazione in base alla selezione dell'utente
        selected_deal(selected, list_temp, suffix_list, path)
    else:
        # Stampa un messaggio se il percorso è vuoto o non valido
        print("The path is invalid!")

def selected_deal(selected, full_list, suffix_list, path):
    # Gestisce le azioni in base alla selezione dell'utente
    if ">quit<" in selected:
        # Se l'utente ha selezionato ">quit<", esce dal programma
        quit()
    elif ">back<" in selected:
        # Se l'utente ha selezionato ">back<", torna al livello superiore del percorso
        upper_level = get_upper_level(path)
        menu(upper_level if upper_level else path, suffix_list)
    else:
        # Se l'utente ha selezionato uno o più elementi, gestisce la selezione
        for item in selected:
            full_path = os.path.join(path, item)
            if isFolder(full_path):
                # Se è una cartella, richiama ricorsivamente la funzione menu sulla cartella
                menu(full_path + "/", suffix_list)
            else:
                # Se è un file, esegue il file utilizzando il comando 'python'
                shell = f"python {full_path}"
                os.system(shell)
