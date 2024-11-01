import tkinter as tk
from tkinter import messagebox

def calculate_price(carat, weight, gold_price_per_kg):
    carat_value = {
        '22k': 22 / 24,
        '18k': 18 / 24,
        '14k': 14 / 24,
        '9k': 9 / 24
    }
    
    # Convert weight from grams to kilograms
    weight_in_kg = weight / 1000

    # Calculate pure gold weight
    pure_gold_weight = weight_in_kg * carat_value[carat]
    
    # Calculate price
    price = pure_gold_weight * gold_price_per_kg
    return price

def calculate():
    carat = carat_var.get()
    weight = weight_entry.get()
    gold_price_per_kg = price_entry.get()

    if carat not in ['22k', '18k', '14k', '9k']:
        messagebox.showerror("Erreur", "Type de carat invalide. Veuillez choisir parmi 22k, 18k, 14k, ou 9k.")
        return

    try:
        weight = float(weight)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un poids valide en grammes.")
        return
    
    try:
        gold_price_per_kg = float(gold_price_per_kg)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un prix valide par kilogramme en EUR.")
        return

    price = calculate_price(carat, weight, gold_price_per_kg)
    result_label.config(text=f"Le prix de l'or {carat.upper()} pour {weight} grammes est : €{price:.2f}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Aurum")

# Utilisation de la grille pour un positionnement flexible des widgets
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Création des widgets
carat_label = tk.Label(root, text="Choisissez le type de carat (22k, 18k, 14k, 9k) :")
carat_label.grid(row=0, column=0, sticky="e", padx=10, pady=5)

carat_var = tk.StringVar(value='22k')
carat_menu = tk.OptionMenu(root, carat_var, '22k', '18k', '14k', '9k')
carat_menu.grid(row=0, column=1, sticky="w", padx=10, pady=5)

weight_label = tk.Label(root, text="Entrez le poids de l'or en grammes :")
weight_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)

weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)

price_label = tk.Label(root, text="Entrez le prix de l'or par kilogramme en EUR :")
price_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)

price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculer", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Démarrage de la boucle principale
root.mainloop()