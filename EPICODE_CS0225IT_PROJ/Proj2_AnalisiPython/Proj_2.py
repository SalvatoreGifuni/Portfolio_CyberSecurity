from datetime import datetime, date

# Funzione per mostrare il menu all'utente
def mostra_menu():
    print("\nCosa vuoi sapere? (Inserisci il numero della domanda corrispondente)\n\
1 - Qual è la data di oggi?\n\
2 - Che ore sono?\n\
3 - Come ti chiami?\n\
4 - Esci dal programma\n")

# Funzione per rispondere alle domande basate sul prompt dell'utente
def assistente_virtuale(comando):
    # Dizionario delle risposte
    azioni = { 
        "1": f"La data di oggi è {date.today().strftime('%d/%m/%Y')}",
        "2": f"L'ora attuale è {datetime.now().strftime('%H:%M')}",
        "3": "Mi chiamo Assistente Virtuale"
    }

    """
    Restituisce la risposta corrispondente, oppure un messaggio di errore.
    Il metodo .get consente di accedere in modo sicuro al dizionario 'azioni' 
    verificando la presenza della chiave, altrimenti restituisce errore
    """
    return azioni.get(comando, "Input non valido. Per favore inserisci numeri da 1 a 4 per selezionare un'opzione.")

print("Benvenuto!")

while True:
    # Mostra il menu
    mostra_menu()

    # Ottieni il comando dell'utente e pulisce eventuali whitespace
    comando_utente = input().strip()

    # Controlla se l'utente vuole uscire
    if comando_utente == "4":
        print("Arrivederci!")
        break  # Esce dal ciclo while

    # Altrimenti risponde in base al comando
    else:
        print(assistente_virtuale(comando_utente))

