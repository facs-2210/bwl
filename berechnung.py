import tkinter as tk
from tkinter import messagebox

# Funktion zur Berechnung der Investitionskosten
def calculate_investment():
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

        # Berechnung der Investitionskosten
        total_developer_salary = software_developers * developer_salary * development_time / 12
        total_dev_test_environment = dev_test_environment
        total_marketing_budget = marketing_budget
        total_hosting_cost = hosting_cost * 12 * 3
        total_maintenance_cost = maintenance_fte * developer_salary * 12 * 2
        total_advertising_cost = advertising_budget * 12 * 2
        total_investment_cost = total_developer_salary + total_dev_test_environment + total_marketing_budget + total_hosting_cost + total_maintenance_cost + total_advertising_cost

        # Anzeigen der Investitionskosten
        result_text.set("Die Investitionskosten betragen: {:.2f} CHF".format(total_investment_cost))

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a number in each field")

# Erzeugung des Tkinter Fensters
root = tk.Tk()

# Erzeugung der Eingabefelder und zugehöriger Labels
fields = [('Software Developers', '1'), ('Development Time (months)', '1'),
          ('Developer Salary (CHF/year)', '0'), ('Dev/Test Environment (CHF)', '0'),
          ('Marketing Budget (CHF)', '0'), ('Hosting Cost (CHF/month)', '0'),
          ('Maintenance FTE', '0'), ('Advertising Budget (CHF/month)', '0')]

entries = []
for field, default in fields:
    label = tk.Label(root, text=field)
    label.pack()
    entry = tk.Entry(root)
    entry.insert(0, default)
    entry.pack()
    entries.append(entry)

software_developers_entry, development_time_entry, developer_salary_entry, dev_test_environment_entry, marketing_budget_entry, hosting_cost_entry, maintenance_fte_entry, advertising_budget_entry = entries

# Erzeugung des Resultatslabels
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# Erzeugung des Berechnungsbuttons
calculate_button = tk.Button(root, text='Calculate', command=calculate_investment)
calculate_button.pack()

# Hauptloop des Tkinter Fensters
root.mainloop()