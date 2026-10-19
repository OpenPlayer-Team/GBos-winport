# Mining Tycoon Datapack
Un datapack completo per Minecraft 1.21.x che trasforma il mining in un'esperienza Idle Tycoon!

## Installazione
1. Inserisci il file .zip nella cartella `datapacks` del tuo mondo Minecraft (1.21+).
2. Entra nel mondo e digita `/reload`.
3. Il sistema si inizializzerà da solo!

## Comandi per il giocatore
- `/trigger mt_menu` : Apre il menu principale per il negozio e le statistiche.
- `/trigger mt_deposit` : Deposita tutte le banconote fisiche presenti nell'inventario.

## Funzionalità
- Economia basata sulla rottura dei blocchi.
- Upgrade (Forza, Efficienza, Fortuna) tramite menu interattivo.
- Costi crescenti per gli upgrade (~+30% a livello).
- Banconote fisiche sicure (impossibili da contraffare, con custom_data, tagli da 10, 50, 100, 500, 1000).
- Pieno supporto multigiocatore (saldi e livelli indipendenti).
- Sistema Prestigio: raggiungi il livello 100 per un moltiplicatore x2 permanente.

## Tabella Abilità
| Abilità | Effetto | Costo Iniziale |
|---|---|---|
| Forza | +5% Valore Base per livello | $100 |
| Efficienza | +10% Moltiplicatore Totale per livello | $500 |
| Fortuna | 2% probabilità per livello di bonus (x2) | $1000 |

## Test Effettuati
- Inizializzazione scoreboard corretta.
- Valuta e rottura blocchi base.
- Menu shop e funzioni trigger vanilla-only.
- Implementazione banconote fisiche anti-contraffazione (tagli multipli).
- Abilità fortuna verificata tramite math random generator.
- Prestigio testato.

## Limitazioni Tecniche
- **Silk Touch Exploit**: Attualmente, Minecraft Vanilla non permette di distinguere in modo performante e scalabile tra blocchi di minerale generati naturalmente e quelli piazzati dal giocatore, usando solo i datapack. Per prevenire cheat, si consiglia di non utilizzare incantesimi Silk Touch se l'intento è di non falsare l'economia, in quanto i minerali ripiazzati assegneranno nuovamente le ricompense. Questo è un limite noto e accettato per mantenere le performance e la stabilità senza necessitare di plugin o mod server side.
