import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox


# ================= DATABASE =================

conn = sqlite3.connect("hospital.db")

c = conn.cursor()


# ================= TABLES =================

c.execute("""
CREATE TABLE IF NOT EXISTS Patient(
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    blood_type TEXT,
    needed_organ TEXT
)
""")


c.execute("""
CREATE TABLE IF NOT EXISTS Donor(
    donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    donor_name TEXT,
    blood_type TEXT,
    donated_organ TEXT
)
""")

conn.commit()


# ================= FUNCTIONS =================

# ---------- CLEAR TABLE ----------

def clear_table():

    for item in tree.get_children():

        tree.delete(item)


# ---------- ADD PATIENT ----------

def add_patient():

    name = patient_name_entry.get()
    blood = patient_blood_combo.get()
    organ = patient_organ_combo.get()

    if name == "" or blood == "" or organ == "":

        messagebox.showerror(
            "Error",
            "Fill Patient Data"
        )

        return

    c.execute(
        """
        INSERT INTO Patient(
            patient_name,
            blood_type,
            needed_organ
        )

        VALUES (?, ?, ?)
        """,

        (
            name,
            blood,
            organ
        )
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Patient Added"
    )


# ---------- ADD DONOR ----------

def add_donor():

    name = donor_name_entry.get()
    blood = donor_blood_combo.get()
    organ = donor_organ_combo.get()

    if name == "" or blood == "" or organ == "":

        messagebox.showerror(
            "Error",
            "Fill Donor Data"
        )

        return

    c.execute(
        """
        INSERT INTO Donor(
            donor_name,
            blood_type,
            donated_organ
        )

        VALUES (?, ?, ?)
        """,

        (
            name,
            blood,
            organ
        )
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Donor Added"
    )


# ---------- DELETE PATIENT ----------

def delete_patient():

    win = tk.Toplevel(root)

    win.title("Delete Patient")

    win.geometry("300x150")

    tk.Label(
        win,
        text="Enter Patient ID"
    ).pack(pady=10)

    id_entry = tk.Entry(win)

    id_entry.pack()

    def delete_now():

        patient_id = id_entry.get()

        if patient_id == "":

            messagebox.showerror(
                "Error",
                "Enter ID"
            )

            return

        c.execute(
            """
            DELETE FROM Patient
            WHERE patient_id = ?
            """,

            (
                patient_id,
            )
        )

        conn.commit()

        if c.rowcount == 0:

            messagebox.showwarning(
                "Not Found",
                "Patient Not Found"
            )

        else:

            messagebox.showinfo(
                "Deleted",
                "Patient Deleted"
            )

        win.destroy()

    tk.Button(
        win,
        text="Delete",
        bg="red",
        fg="white",
        command=delete_now
    ).pack(pady=15)


# ---------- DELETE DONOR ----------

def delete_donor():

    win = tk.Toplevel(root)

    win.title("Delete Donor")

    win.geometry("300x150")

    tk.Label(
        win,
        text="Enter Donor ID"
    ).pack(pady=10)

    id_entry = tk.Entry(win)

    id_entry.pack()

    def delete_now():

        donor_id = id_entry.get()

        if donor_id == "":

            messagebox.showerror(
                "Error",
                "Enter ID"
            )

            return

        c.execute(
            """
            DELETE FROM Donor
            WHERE donor_id = ?
            """,

            (
                donor_id,
            )
        )

        conn.commit()

        if c.rowcount == 0:

            messagebox.showwarning(
                "Not Found",
                "Donor Not Found"
            )

        else:

            messagebox.showinfo(
                "Deleted",
                "Donor Deleted"
            )

        win.destroy()

    tk.Button(
        win,
        text="Delete",
        bg="red",
        fg="white",
        command=delete_now
    ).pack(pady=15)


# ---------- UPDATE PATIENT ----------

def update_patient():

    win = tk.Toplevel(root)

    win.title("Update Patient")

    win.geometry("350x300")

    tk.Label(
        win,
        text="Patient ID"
    ).pack()

    id_entry = tk.Entry(win)

    id_entry.pack()


    tk.Label(
        win,
        text="New Blood Type"
    ).pack()

    blood_combo = ttk.Combobox(
        win,
        values=[
            "A+","A-",
            "B+","B-",
            "AB+","AB-",
            "O+","O-"
        ]
    )

    blood_combo.pack()


    tk.Label(
        win,
        text="New Organ"
    ).pack()

    organ_combo = ttk.Combobox(
        win,
        values=[
            "Heart",
            "Kidney",
            "Liver",
            "Lung"
        ]
    )

    organ_combo.pack()


    def update_now():

        patient_id = id_entry.get()

        blood = blood_combo.get()

        organ = organ_combo.get()

        if patient_id == "" or blood == "" or organ == "":

            messagebox.showerror(
                "Error",
                "Fill All Data"
            )

            return

        c.execute(
            """
            UPDATE Patient

            SET
                blood_type = ?,
                needed_organ = ?

            WHERE patient_id = ?
            """,

            (
                blood,
                organ,
                patient_id
            )
        )

        conn.commit()

        if c.rowcount == 0:

            messagebox.showwarning(
                "Not Found",
                "Patient Not Found"
            )

        else:

            messagebox.showinfo(
                "Updated",
                "Patient Updated"
            )

        win.destroy()

    tk.Button(
        win,
        text="Update",
        bg="orange",
        command=update_now
    ).pack(pady=15)


# ---------- UPDATE DONOR ----------

def update_donor():

    win = tk.Toplevel(root)

    win.title("Update Donor")

    win.geometry("350x300")

    tk.Label(
        win,
        text="Donor ID"
    ).pack()

    id_entry = tk.Entry(win)

    id_entry.pack()


    tk.Label(
        win,
        text="New Blood Type"
    ).pack()

    blood_combo = ttk.Combobox(
        win,
        values=[
            "A+","A-",
            "B+","B-",
            "AB+","AB-",
            "O+","O-"
        ]
    )

    blood_combo.pack()


    tk.Label(
        win,
        text="New Organ"
    ).pack()

    organ_combo = ttk.Combobox(
        win,
        values=[
            "Heart",
            "Kidney",
            "Liver",
            "Lung"
        ]
    )

    organ_combo.pack()


    def update_now():

        donor_id = id_entry.get()

        blood = blood_combo.get()

        organ = organ_combo.get()

        if donor_id == "" or blood == "" or organ == "":

            messagebox.showerror(
                "Error",
                "Fill All Data"
            )

            return

        c.execute(
            """
            UPDATE Donor

            SET
                blood_type = ?,
                donated_organ = ?

            WHERE donor_id = ?
            """,

            (
                blood,
                organ,
                donor_id
            )
        )

        conn.commit()

        if c.rowcount == 0:

            messagebox.showwarning(
                "Not Found",
                "Donor Not Found"
            )

        else:

            messagebox.showinfo(
                "Updated",
                "Donor Updated"
            )

        win.destroy()

    tk.Button(
        win,
        text="Update",
        bg="orange",
        command=update_now
    ).pack(pady=15)


# ---------- SHOW PATIENTS ----------

def show_patients():

    clear_table()

    columns = (
        "ID",
        "Name",
        "Blood",
        "Organ"
    )

    tree["columns"] = columns

    tree["show"] = "headings"

    for col in columns:

        tree.heading(col, text=col)

        tree.column(col, width=180)

    c.execute(
        """
        SELECT * FROM Patient
        """
    )

    rows = c.fetchall()

    for row in rows:

        tree.insert(
            "",
            tk.END,
            values=row
        )


# ---------- SHOW DONORS ----------

def show_donors():

    clear_table()

    columns = (
        "ID",
        "Name",
        "Blood",
        "Organ"
    )

    tree["columns"] = columns

    tree["show"] = "headings"

    for col in columns:

        tree.heading(col, text=col)

        tree.column(col, width=180)

    c.execute(
        """
        SELECT * FROM Donor
        """
    )

    rows = c.fetchall()

    for row in rows:

        tree.insert(
            "",
            tk.END,
            values=row
        )


# ---------- SHOW MATCHING ----------

def show_matching():

    clear_table()

    columns = (
        "Patient ID",
        "Patient Name",
        "Donor ID",
        "Donor Name",
        "Blood",
        "Organ"
    )

    tree["columns"] = columns

    tree["show"] = "headings"

    for col in columns:

        tree.heading(col, text=col)

        tree.column(col, width=150)

    c.execute(
        """
        SELECT

            Patient.patient_id,
            Patient.patient_name,

            Donor.donor_id,
            Donor.donor_name,

            Patient.blood_type,
            Patient.needed_organ

        FROM Patient

        INNER JOIN Donor

        ON Patient.blood_type = Donor.blood_type

        AND Patient.needed_organ = Donor.donated_organ
        """
    )

    rows = c.fetchall()

    if len(rows) == 0:

        messagebox.showwarning(
            "No Match",
            "No Matching Found"
        )

        return

    for row in rows:

        tree.insert(
            "",
            tk.END,
            values=row
        )


# ================= GUI =================

root = tk.Tk()

root.title("Hospital Organ Matching System")

root.geometry("1200x800")

root.configure(bg="#EAF6F6")


# ================= TITLE =================

title = tk.Label(
    root,
    text="Hospital Organ Matching System",
    font=("Arial", 24, "bold"),
    bg="#EAF6F6"
)

title.pack(pady=20)


# ================= PATIENT FRAME =================

patient_frame = tk.LabelFrame(
    root,
    text="Patient",
    font=("Arial", 14, "bold"),
    padx=20,
    pady=20
)

patient_frame.pack(
    fill="x",
    padx=20,
    pady=10
)


tk.Label(
    patient_frame,
    text="Patient Name"
).grid(row=0, column=0, padx=10, pady=10)

patient_name_entry = tk.Entry(
    patient_frame,
    width=25
)

patient_name_entry.grid(row=0, column=1)


tk.Label(
    patient_frame,
    text="Blood Type"
).grid(row=1, column=0)

patient_blood_combo = ttk.Combobox(
    patient_frame,
    values=[
        "A+","A-",
        "B+","B-",
        "AB+","AB-",
        "O+","O-"
    ],
    width=22
)

patient_blood_combo.grid(row=1, column=1)


tk.Label(
    patient_frame,
    text="Needed Organ"
).grid(row=2, column=0)

patient_organ_combo = ttk.Combobox(
    patient_frame,
    values=[
        "Heart",
        "Kidney",
        "Liver",
        "Lung"
    ],
    width=22
)

patient_organ_combo.grid(row=2, column=1)


tk.Button(
    patient_frame,
    text="Add Patient",
    bg="green",
    fg="white",
    width=18,
    command=add_patient
).grid(row=3, column=0, pady=10)


tk.Button(
    patient_frame,
    text="Update Patient",
    bg="orange",
    width=18,
    command=update_patient
).grid(row=3, column=1)


tk.Button(
    patient_frame,
    text="Delete Patient",
    bg="red",
    fg="white",
    width=18,
    command=delete_patient
).grid(row=4, column=0, columnspan=2, pady=10)


# ================= DONOR FRAME =================

donor_frame = tk.LabelFrame(
    root,
    text="Donor",
    font=("Arial", 14, "bold"),
    padx=20,
    pady=20
)

donor_frame.pack(
    fill="x",
    padx=20,
    pady=10
)


tk.Label(
    donor_frame,
    text="Donor Name"
).grid(row=0, column=0)

donor_name_entry = tk.Entry(
    donor_frame,
    width=25
)

donor_name_entry.grid(row=0, column=1)


tk.Label(
    donor_frame,
    text="Blood Type"
).grid(row=1, column=0)

donor_blood_combo = ttk.Combobox(
    donor_frame,
    values=[
        "A+","A-",
        "B+","B-",
        "AB+","AB-",
        "O+","O-"
    ],
    width=22
)

donor_blood_combo.grid(row=1, column=1)


tk.Label(
    donor_frame,
    text="Donated Organ"
).grid(row=2, column=0)

donor_organ_combo = ttk.Combobox(
    donor_frame,
    values=[
        "Heart",
        "Kidney",
        "Liver",
        "Lung"
    ],
    width=22
)

donor_organ_combo.grid(row=2, column=1)


tk.Button(
    donor_frame,
    text="Add Donor",
    bg="blue",
    fg="white",
    width=18,
    command=add_donor
).grid(row=3, column=0, pady=10)


tk.Button(
    donor_frame,
    text="Update Donor",
    bg="orange",
    width=18,
    command=update_donor
).grid(row=3, column=1)


tk.Button(
    donor_frame,
    text="Delete Donor",
    bg="red",
    fg="white",
    width=18,
    command=delete_donor
).grid(row=4, column=0, columnspan=2, pady=10)


# ================= SHOW BUTTONS =================

btn_frame = tk.Frame(
    root,
    bg="#EAF6F6"
)

btn_frame.pack(pady=20)


tk.Button(
    btn_frame,
    text="Show Patients",
    bg="purple",
    fg="white",
    width=20,
    command=show_patients
).grid(row=0, column=0, padx=10)


tk.Button(
    btn_frame,
    text="Show Donors",
    bg="teal",
    fg="white",
    width=20,
    command=show_donors
).grid(row=0, column=1, padx=10)


tk.Button(
    btn_frame,
    text="Show Matching",
    bg="darkorange",
    fg="white",
    width=20,
    command=show_matching
).grid(row=0, column=2, padx=10)


# ================= TABLE =================

tree = ttk.Treeview(
    root
)

tree.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)


# ================= RUN =================

root.mainloop()