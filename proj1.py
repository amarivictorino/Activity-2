import tkinter as tk
from tkinter import messagebox

class UserInfoApp:
    def __init__(self, master):
        self.master = master
        master.title("User Information")

        # Set background color
        master.configure(bg='#F0F0F0')

        # Load an image
        self.image = tk.PhotoImage(file="path/to/your/image.png")

        # Create labels and entry widgets
        self.label_name = tk.Label(master, text="Name:", bg='#F0F0F0')
        self.label_age = tk.Label(master, text="Age:", bg='#F0F0F0')
        self.label_address = tk.Label(master, text="Address:", bg='#F0F0F0')
        self.label_email = tk.Label(master, text="Email:", bg='#F0F0F0')
        self.label_password = tk.Label(master, text="Password:", bg='#F0F0F0')
        self.label_confirm_password = tk.Label(master, text="Confirm Password:", bg='#F0F0F0')

        self.entry_name = tk.Entry(master)
        self.entry_age = tk.Entry(master)
        self.entry_address = tk.Entry(master)
        self.entry_email = tk.Entry(master)
        self.entry_password = tk.Entry(master, show="*")  # show "*" for password
        self.entry_confirm_password = tk.Entry(master, show="*")

        # Create Submit Button
        self.submit_button = tk.Button(master, text="Submit", command=self.display_info, bg='#4CAF50', fg='white')

        # Create Image Label
        self.image_label = tk.Label(master, image=self.image, bg='#F0F0F0')

        # Grid layout
        self.label_name.grid(row=0, column=0, sticky="e")
        self.label_age.grid(row=1, column=0, sticky="e")
        self.label_address.grid(row=2, column=0, sticky="e")
        self.label_email.grid(row=3, column=0, sticky="e")
        self.label_password.grid(row=4, column=0, sticky="e")
        self.label_confirm_password.grid(row=5, column=0, sticky="e")

        self.entry_name.grid(row=0, column=1)
        self.entry_age.grid(row=1, column=1)
        self.entry_address.grid(row=2, column=1)
        self.entry_email.grid(row=3, column=1)
        self.entry_password.grid(row=4, column=1)
        self.entry_confirm_password.grid(row=5, column=1)

        self.submit_button.grid(row=6, column=0, columnspan=2)
        self.image_label.grid(row=7, column=0, columnspan=2)

    def display_info(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        address = self.entry_address.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match. Please try again.")
            return

        user_data = {
            "Name": name,
            "Age": age,
            "Address": address,
            "Email": email,
            "Password": "*****",  # Display masked password
        }

        info_message = "\n".join([f"{key}: {value}" for key, value in user_data.items()])
        messagebox.showinfo("Entered Information", info_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = UserInfoApp(root)
    root.mainloop()

