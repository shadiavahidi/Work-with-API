import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk


def fetch_users():
    response = requests.get("https://reqres.in/api/users")
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []


def display_users():
    users = fetch_users()
    for user in users:
        frame = ttk.Frame(root, padding=10)
        frame.pack(fill=tk.X, padx=10, pady=5)

        # Display user avatar
        avatar_url = user['avatar']
        avatar_response = requests.get(avatar_url, stream=True)
        avatar_response.raw.decode_content = True
        avatar_image = Image.open(avatar_response.raw)
        avatar_photo = ImageTk.PhotoImage(avatar_image)
        avatar_label = ttk.Label(frame, image=avatar_photo)
        avatar_label.image = avatar_photo
        avatar_label.pack(side=tk.LEFT)

        # Display user details
        details_frame = ttk.Frame(frame)
        details_frame.pack(side=tk.LEFT, padx=10)

        name_label = ttk.Label(details_frame, text=f"{user['first_name']} {user['last_name']}",
                               font=("Helvetica", 12, "bold"))
        name_label.pack(anchor=tk.W)

        email_label = ttk.Label(details_frame, text=user['email'], font=("Helvetica", 10))
        email_label.pack(anchor=tk.W)


# Create the main window
root = tk.Tk()
root.title("User Information")
root.geometry("600x400")

# Display users
display_users()

# Start the GUI event loop
root.mainloop()
