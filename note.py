
n = int(input("veuillez entrer le nombre d'eleve:"))
Tab_note = []

for i in range (n):
    note = float(input(f"veuillez entrer la note de leleve {i+1}:"))
    Tab_note.append(note)

for i in range(n):
    if Tab_note[i] > 10:
        print("les note superieurs a la moyenne sont :",Tab_note[i])