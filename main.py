import tkinter as tk
from tkinter import messagebox


class SmartHealthApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Smart Health Assistant")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        self.create_widgets()

    # -------------------------
    # UI CREATION
    # -------------------------
    def create_widgets(self):

        title = tk.Label(self.root, text="SMART HEALTH ASSISTANT",
                         font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=15)

        labels = [
            "Name", "Age", "Height (m)", "Weight (kg)",
            "Water Intake (liters/day)", "Sleep Hours", "Steps Walked"
        ]

        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(self.root, text=text).grid(row=i+1, column=0, padx=10, pady=8, sticky="w")
            entry = tk.Entry(self.root, width=25)
            entry.grid(row=i+1, column=1, padx=10, pady=8)
            self.entries[text] = entry

        calculate_btn = tk.Button(
            self.root,
            text="Generate Health Report",
            command=self.generate_report,
            bg="#4CAF50",
            fg="white",
            width=25
        )
        calculate_btn.grid(row=len(labels)+1, column=0, columnspan=2, pady=20)

    # -------------------------
    # LOGIC SECTION
    # -------------------------
    def calculate_bmi(self, weight, height):
        return weight / (height ** 2)

    def bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight", "Increase calorie intake with protein-rich foods."
        elif bmi < 25:
            return "Normal weight", "Maintain a balanced diet and regular exercise."
        elif bmi < 30:
            return "Overweight", "Reduce sugar and oily food. Exercise regularly."
        else:
            return "Obese", "Consult a doctor and follow a structured diet plan."

    def calculate_score(self, sleep, steps):
        score = 0
        score += 50 if sleep >= 7 else 20
        score += 50 if steps >= 8000 else 20
        return score

    # -------------------------
    # MAIN REPORT FUNCTION
    # -------------------------
    def generate_report(self):

        try:
            name = self.entries["Name"].get()
            age = int(self.entries["Age"].get())
            height = float(self.entries["Height (m)"].get())
            weight = float(self.entries["Weight (kg)"].get())
            water = float(self.entries["Water Intake (liters/day)"].get())
            sleep = int(self.entries["Sleep Hours"].get())
            steps = int(self.entries["Steps Walked"].get())

            if not name:
                raise ValueError("Name cannot be empty.")

            bmi = self.calculate_bmi(weight, height)
            category, diet = self.bmi_category(bmi)

            recommended_water = weight * 0.033
            water_msg = "Adequate water intake." if water >= recommended_water else "Increase water intake."

            score = self.calculate_score(sleep, steps)

            if score >= 80:
                lifestyle = "Excellent lifestyle!"
            elif score >= 50:
                lifestyle = "Good, but needs improvement."
            else:
                lifestyle = "Poor lifestyle habits. Improve sleep and activity."

            report = f"""
Health Report for {name}

Age: {age}
BMI: {round(bmi, 2)} ({category})

Diet Advice:
{diet}

Water Advice:
{water_msg}

Health Score: {score}/100
{lifestyle}
"""

            messagebox.showinfo("Health Report", report)

        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")
        except Exception:
            messagebox.showerror("Error", "Please enter valid numeric values.")


# -------------------------
# RUN APPLICATION
# -------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHealthApp(root)
    root.mainloop()
