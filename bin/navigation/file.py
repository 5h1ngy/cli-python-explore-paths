import os
from navigation.apart import apart, together

def get_upper_level(path):
    # Restituisce il percorso del livello superiore di un dato percorso.
    tmp = apart(path, "/")
    del tmp[len(tmp) - 1]
    if len(tmp) != 0:
        return together(tmp, "/")
    else:
        return False

def isCode(name, suffix):
    # Verifica se il suffisso di un nome di file coincide con il suffisso fornito.
    lens = len(name)
    code = name[lens - len(suffix):]
    if code == suffix:
        return True
    else:
        return False

def isSuffix(name, suffix_list):
    # Verifica se un nome di file ha uno dei suffissi dalla lista dei suffissi fornita.
    for i in suffix_list:
        if isCode(name, i):
            return True
    return False

def isFolder(path):
    # Verifica se il percorso corrisponde a una directory.
    if os.path.isdir(path):
        return True
    elif os.path.isfile(path):
        return False

def find_folder(path):
    # Trova tutte le directory in un dato percorso.
    folder = []
    all_items = os.listdir(path)
    for i in all_items:
        if isFolder(i):
            folder.append(i)
    return folder

def find_py_in_last_folder(path, suffix_list):
    # Trova tutti i file con un determinato suffisso nell'ultima directory di un percorso.
    list_temp = []
    list_result = []

    for i in os.listdir(path):
        list_temp.append(i)

    for a in list_temp:
        if isSuffix(a, suffix_list):
            list_result.append(a)

    return list_result

def find_py(path):
    # Trova tutti i file .py in un dato percorso.
    all_menu = []
    all_menus = {}
    folder = find_folder(path)
    for i in folder:
        all_menu.append(i)
    if len(all_menu) != 0:
        for j in all_menu:
            all = os.listdir(path + j)
            for x in all:
                all_menus[j] = all
        return all_menus
    else:
        return find_py_in_last_folder(path)

def have_py_in(listname, suffix_list):
    # Verifica se almeno un elemento nella lista ha un determinato suffisso.
    for i in listname:
        if isSuffix(i, suffix_list):
            return True
    return False

def get_py_in_folder(path, suffix_list):
    # Ottiene tutti i file con un determinato suffisso in una directory.
    tmp = []
    file_list = []
    if path == "D:/System Volume Information/":
        return []
    else:
        file_list = os.listdir(path)
        for i in file_list:
            if os.path.isfile(path + i):
                if isSuffix(i, suffix_list):
                    tmp.append(i)
        return tmp

def have_py_in_folder(path, suffix_list):
    # Verifica se una directory contiene file con un determinato suffisso.
    tmp = get_py_in_folder(path, suffix_list)
    if len(tmp) == 0:
        return False
    else:
        return True

def return_py_folder(path):
    # Restituisce tutte le directory che contengono file con un determinato suffisso.
    folder = find_py(path)
    py_folder = []
    for i in folder:
        if have_py_in(folder[i]):
            py_folder.append(i)
    return py_folder
