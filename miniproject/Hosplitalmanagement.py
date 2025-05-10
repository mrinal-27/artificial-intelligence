import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# --- Diagnosis Logic ---
def medical_expert_system(symptoms, city):
    disease = "Unknown"
    doctor = "General Physician"
    advice = "Consult doctor immediately"
    first_aid = "No specific first aid. Visit nearest hospital."
    severity = "Moderate"

    if 'fever' in symptoms and 'cough' in symptoms and 'breathing issue' in symptoms:
        disease = 'Possible COVID-19 or Respiratory Infection'
        doctor = 'Pulmonologist'
        advice = 'Isolate and get RT-PCR Test'
        first_aid = 'Wear Mask, Isolate, Steam Inhalation'
        severity = "High"
    elif 'headache' in symptoms and 'vomiting' in symptoms:
        disease = 'Possible Migraine'
        doctor = 'Neurologist'
        advice = 'Avoid Stress and Consult Neurologist'
        first_aid = 'Stay in dark room, apply cold compress'
    elif 'stomach pain' in symptoms and 'vomiting' in symptoms:
        disease = 'Possible Food Poisoning'
        doctor = 'Gastroenterologist'
        advice = 'Take ORS, Stay Hydrated'
        first_aid = 'Drink clean water, Avoid solid food'
    elif 'joint pain' in symptoms and 'fever' in symptoms:
        disease = 'Possible Dengue or Viral Fever'
        doctor = 'General Physician'
        advice = 'Blood Test and Rest'
        first_aid = 'Cold compress, paracetamol'
    elif 'chest pain' in symptoms and 'breathing issue' in symptoms:
        disease = 'Possible Heart Attack'
        doctor = 'Cardiologist'
        advice = 'Immediate ECG and Hospitalization'
        first_aid = 'Lie down, loosen clothes, call ambulance'
        severity = "Critical"

    hospital = {
        'delhi': 'AIIMS Hospital',
        'mumbai': 'Lilavati Hospital',
        'chennai': 'Apollo Hospital',
        'kolkata': 'Fortis Hospital',
        'hyderabad': 'Yashoda Hospital',
        'pune': 'Deenanath Mangeshkar Hospital'
    }.get(city.lower(), 'Nearest Government Hospital')

    emergency_contacts = {
        'Ambulance': '102',
        'Police': '100',
        'Fire': '101'
    }

    health_tip = "Stay hydrated, avoid junk food, regular exercise."
    diagnosis_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return disease, doctor, advice, first_aid, hospital, emergency_contacts, health_tip, severity, diagnosis_time


# --- GUI Functionality ---
def generate_report():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    city = entry_city.get().strip()
    symptoms = [s.strip() for s in entry_symptoms.get().lower().split(',')]

    if not name or not phone or not city or not symptoms:
        messagebox.showerror("Input Error", "Please fill all the fields.")
        return

    result = medical_expert_system(symptoms, city)

    report = f"""--- Medical Report ---
Patient Name: {name}
Phone Number: {phone}
City: {city.title()}
Date: {result[8]}

Predicted Disease: {result[0]}
Recommended Doctor: {result[1]}
Advice: {result[2]}
First Aid Tips: {result[3]}
Nearest Hospital: {result[4]}
Severity Level: {result[7]}

Emergency Contacts:
  Ambulance: {result[5]['Ambulance']}
  Police: {result[5]['Police']}
  Fire: {result[5]['Fire']}

General Health Tip: {result[6]}
"""

    # Display in text box
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, report)

    # Save to file
    filename = f"report_{name.lower().replace(' ', '_')}.txt"
    with open(filename, "w") as f:
        f.write(report.strip())
    messagebox.showinfo("Success", f"Report saved as '{filename}'")


# --- GUI Setup ---
root = tk.Tk()
root.title("Medical Expert System")
root.geometry("700x600")

tk.Label(root, text="Patient Name:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Phone Number:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_phone = tk.Entry(root, width=30)
entry_phone.grid(row=1, column=1)

tk.Label(root, text="City:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_city = tk.Entry(root, width=30)
entry_city.grid(row=2, column=1)

tk.Label(root, text="Symptoms (comma-separated):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_symptoms = tk.Entry(root, width=50)
entry_symptoms.grid(row=3, column=1)

tk.Button(root, text="Generate Report", command=generate_report, bg="green", fg="white").grid(row=4, column=1, pady=10)

output_text = tk.Text(root, height=20, width=85)
output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()