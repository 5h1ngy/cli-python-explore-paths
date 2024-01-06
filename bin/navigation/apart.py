def apart(string, char):
    # Assicura che la stringa termini con il carattere specificato
    if string[len(string) - 1] != char:
        string += char

    tmp = ""  # Variabile temporanea per memorizzare ciascuna parte della stringa
    res = []  # Lista che conterrà le parti separate della stringa
    for i in string:
        if i == char:
            # Se il carattere corrente è il carattere di separazione, aggiunge la parte corrente alla lista
            res.append(tmp)
            tmp = ""  # Resetta la variabile temporanea per la prossima parte
        else:
            # Altrimenti, aggiunge il carattere corrente alla parte corrente della stringa
            tmp += i

    return res  # Restituisce la lista delle parti separate

def together(lst, char):
    res = ""  # Variabile risultato che conterrà la stringa composta
    for i in lst:
        i += char  # Aggiunge il carattere di separazione alla fine di ciascuna parte
        res += i   # Aggiunge la parte corrente alla stringa risultato
    return res   # Restituisce la stringa composta
