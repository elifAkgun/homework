'''
   Abbiamo quattro giocatori che si sfidano a Scarabeo+. In ogni mano
   di Scarabeo+, i giocatori, a turno, devono inserire una parola nel
   tabellone ed ottengono un punteggio, calcolato in base al valore
   delle lettere che compongono la parola inserita.

   Ogni giocatore crea la propria parola scegliendola a partire da una
   mano di 8 lettere, che vengono rimpiazzate una volta che la parola
   è stata giocata, finché non sono esaurite. Il numero totale di
   lettere è 130.  Il gioco finisce quando un giocatore riesce a
   finire tutte le lettere nella sua mano e non ci sono più lettere a
   disposizione per rimpiazzare quelle che ha appena giocato (ovvero,
   le 130 lettere sono esaurite, perché giocate oppure perché in mano
   agli altri giocatori).

   Alla fine delle giocate, vince il giocatore che ha accumulato più
   punti, considerando che per ogni lettera che rimane non giocata
   (ovvero rimane in mano ad un giocatore quando il gioco finisce)
   vengono sottratti 3 punti. 
   I punteggi sono così calcolati:
    1 punto:  E, A, I, O, N, R, T, L, S, U
    2 punti: D, G
    3 punti: B, C, M, P
    4 punti: F, H, V, W, Y
    5 punti: K
    8 punti: J, X
   10 punti: Q, Z

   Progettare una funzione ex1(g1, g2, g3, g4, dim_hand, num_letters) che calcola i
   punteggi di una partita di Scarabeo+ svolta fra i 4 giocatori, con
   la variante che il numero di lettere iniziali è num_letters, piuttosto che
   130 e il numero di lettere a disposizione di ogni giocatore è dim_hand.
   g1, g2, g3 e g4 sono liste di stringhe che rappresentano le
   giocate dei giocatori g1, g2, g3 e g4, rispettivamente, 
   in ciascun turno.

ES: dim_hand=5, num_letters=40
    g1 = ['seta','peeks','deter']
    g2 = ['reo','pumas']
    g3 = ['xx','xx']
    g4 = ['frs','bern']
    
    Notare che all’inizio della partita 5 lettere vengono date ad ognuno dei
    giocatori, dunque il contatore num_letters decresce conseguentemente.

dim_hand - num_letters - parola - punti
5 5 5 5    20            seta      4  0  0  0
5 5 5 5    16            reo       4  3  0  0
5 5 5 5    13            xx        4  3 16  0
5 5 5 5    11            frs       4  3 16  6
5 5 5 5     8            peeks    15  3 16  6
5 5 5 5     3            pumas    15 12 16  6
5 3 5 5     0            xx       15 12 32  6
5 3 3 5     0            bern     15 12 32 12
5 3 3 1     0            deter    21 12 32 12
0 3 3 1     0                       GAME OVER
---------------------------------------------
Finale                            21  3 23  9

Il TIMEOUT per ciascun test è di 0.5 secondi

ATTENZIONE: è proibito:
    - importare altre librerie
    - usare variabili globali
    - aprire file
'''
def ex1(g1, g2, g3, g4, dim_hand, num_letters):
    # Inserire il proprio codice qui
    pass

if __name__ == "__main__":
    # inserite qui i vostri test personali
    pass
