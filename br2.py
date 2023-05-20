import tkinter as tk
from tkinter import messagebox

# Funktion zur Berechnung der Betriebskosten
def berechne_kosten():
    try:
        # Einlesen der Werte aus den Eingabefeldern
        software_developers = int(software_developers_entry.get())
        development_time = int(development_time_entry.get())
        developer_salary = float(developer_salary_entry.get())
        dev_test_environment = float(dev_test_environment_entry.get())
        marketing_budget = float(marketing_budget_entry.get())
        hosting_cost = float(hosting_cost_entry.get())
        maintenance_fte = float(maintenance_fte_entry.get())
        advertising_budget = float(advertising_budget_entry.get())

        # Berechnung der Kostenarten
        total_developer_salary = software_developers * developer_salary * development_time / 12
        total_dev_test_environment = dev_test_environment
        total_marketing_budget = marketing_budget
        total_hosting_cost = hosting_cost * 12 * 3
        total_maintenance_cost = maintenance_fte * developer_salary * 12 * 2
        total_advertising_cost = advertising_budget * 12 * 2
        total_investment_cost = total_developer_salary + total_dev_test_environment + total_marketing_budget + total_hosting_cost + total_maintenance_cost + total_advertising_cost

        # Anzeigen der Kostenarten und der Gesamtkosten
        ergebnis_text.set("Die Gesamtkosten betragen: {:.2f} CHF".format(total_investment_cost))
        personalkosten_text.set("Personalkosten: {:.2f} CHF".format(total_developer_salary))
        materialkosten_text.set("Materialkosten: {:.2f} CHF".format(total_dev_test_environment))
        raumkosten_text.set("Raumkosten: {:.2f} CHF".format(total_hosting_cost))
        kapitalkosten_text.set("Kapitalkosten: {:.2f} CHF".format(total_maintenance_cost))
        dienstleistungskosten_text.set("Dienstleistungskosten: {:.2f} CHF".format(total_marketing_budget))
        kalkulatorische_kosten_text.set("Kalkulatorische Kosten: {:.2f} CHF".format(total_advertising_cost))

    except ValueError:
        messagebox.showerror("Ungültige Eingabe", "Bitte geben Sie eine Zahl in jedes Feld ein")

# Erzeugung des Tkinter Fensters
root = tk.Tk()

# Erzeugung der Eingabefelder und zugehöriger Labels
felder = [('Anzahl der Softwareentwickler', '1'), ('Entwicklungszeit (Monate)', '1'),
          ('Gehalt eines Softwareentwicklers (CHF/Jahr)', '0'), ('Entwicklungstestumgebung (CHF)', '0'),
          ('Marketingbudget (CHF)', '0'), ('Hostingkosten (CHF/Monat)', '0'),
          ('Wartungs-FTE', '0'), ('Werbungsbudget (CHF/Monat)', '0')]

eingaben = []
for feld, standard in felder:
    beschriftung = tk.Label(root, text=feld)
    beschriftung.pack()
    eingabe = tk.Entry(root)
    eingabe.insert(0, standard)
    eingabe.pack()
    eingaben.append(eingabe)

software_developers_entry, development_time_entry, developer_salary_entry, dev_test_environment_entry, marketing_budget_entry
