import tkinter as tk
from tkinter import messagebox

def calculate_costs():
    try:
        # Einlesen der Werte aus den Eingabefeldern
        software_developers = float(software_developers_entry.get())
        development_time = float(development_time_entry.get())
        developer_salary = float(developer_salary_entry.get())
        dev_test_environment = float(dev_test_environment_entry.get())
        marketing_budget = float(marketing_budget_entry.get())
        bank_interest = float(bank_interest_entry.get())
        hosting_cost = float(hosting_cost_entry.get())
        maintenance_fte = float(maintenance_fte_entry.get())
        advertising_budget = float(advertising_budget_entry.get())

        # Berechnung der Kosten
        total_developer_salary = software_developers * developer_salary * development_time / 12
        total_dev_test_environment = dev_test_environment
        total_marketing_budget = marketing_budget
        capital_costs = (total_developer_salary + total_dev_test_environment + total_marketing_budget) * bank_interest

        personnel_costs = maintenance_fte * developer_salary
        material_costs = hosting_cost * 12
        service_costs = advertising_budget * 12
        operational_costs_yearly = personnel_costs + material_costs + service_costs

        # Anzeigen der Kosten
        capital_costs_var.set("Kapitalkosten: {:.2f} CHF".format(capital_costs))
        personnel_costs_var.set("Personalkosten: {:.2f} CHF".format(personnel_costs))
        material_costs_var.set("Materialkosten: {:.2f} CHF".format(material_costs))
        service_costs_var.set("Dienstleistungskosten: {:.2f} CHF".format(service_costs))
        operational_costs_yearly_var.set("Betriebskosten pro Jahr: {:.2f} CHF".format(operational_costs_yearly))

    except ValueError:
        messagebox.showerror("Ungültige Eingabe", "Bitte geben Sie eine Zahl in jedes Feld ein")

# Erzeugung des Tkinter Fensters
root = tk.Tk()

# Erzeugung der Eingabefelder und zugehöriger Labels
fields = [('Softwareentwickler (FTE)', '6'), ('Entwicklungszeit (Monate)', '15'),
          ('Softwareentwickler Gehalt (CHF/Jahr)', '124800'), ('Entwicklungs- und Testumgebung (CHF)', '48000'),
          ('Marketingbudget (CHF)', '60000'), ('Bankzins', '0.055'), 
          ('Hostingkosten (CHF/Monat)', '950'), ('Wartungs-FTE', '0.5'),
          ('Werbungsbudget (CHF/Monat)', '3600')]

entries = []
for field, default in fields:
    label = tk.Label(root, text=field)
    label.pack()
    entry = tk.Entry(root)
    entry.insert(0, default)
    entry.pack()
    entries.append(entry)

software_developers_entry, development_time_entry, developer_salary_entry, dev_test_environment_entry, marketing_budget_entry, bank_interest_entry, hosting_cost_entry, maintenance_fte_entry, advertising_budget_entry = entries

# Erzeugung der Ausgabe Labels
capital_costs_var = tk.StringVar()
capital_costs_label = tk.Label(root, textvariable=capital_costs_var)
capital_costs_label.pack()

personnel_costs_var = tk.StringVar()
personnel_costs_label = tk.Label(root, textvariable=personnel_costs
