notas = []

while (n := input("Nota (ou 'fim'): ").strip().lower()) != 'fim':
    try:
        nota = float(n)
        (0 <= nota <= 10) and notas.append(nota)
    except:
        pass

print(f"Média: {round((lambda ns: sum(ns)/len(ns))(notas), 2) if notas else 'Sem notas válidas.'}")
