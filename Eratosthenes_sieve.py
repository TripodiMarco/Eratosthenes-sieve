# Elencare i primi n numeri primi, chiedendo n all'utente e implementando l'algoritmo del "Crivello di Eratostene"
n=int(input("Insert n value:"))
prime_num=[]
# Il procedimento per calcolare suddetto algoritmo è il seguente: 
# si scrivono tutti i numeri naturali a partire da 2 fino n in un elenco detto setaccio. 
sieve=list(range(2,n))

starting_num=2                                                      # Bisogna creare un num_partenza dal quale i cicli while e for potranno partire
while starting_num<n:                                               # Fin tanto che il num_partenza è minore di n
    for element in sieve:                                       # Per ogni elemento di setaccio che è diverso da num_partenza e il resto  
        prime_num=sieve                                          # della divisione tra elemento e num_partenza è pari a 0, rimuovilo dalla 
        if element!=starting_num and element%starting_num==0:     # lista num_primi, creata appositamente per fare sì che con il ciclo for si 
            prime_num.remove(element)                              # possano eliminare elementi dalla stessa lista ma nominata diversamente
    starting_num+=1                                                 # I numeri che restano sono i numeri non divisibili per il num_partenza.
print(prime_num)
    

 

 
 
 
