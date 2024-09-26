from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Import from Pillow for handling icons
import base64

def decrypt():
    password = code.get()
    if password == "1234":
        message = text1.get(1.0, END).strip()
        if not message:
            messagebox.showwarning("Warning", "Please enter a message to decrypt.")
            return
        try:
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypted_message = base64_bytes.decode("ascii")  # Corrected variable name

            screen2 = Toplevel(screen)
            screen2.title("Decryption")
            screen2.geometry("400x200")
            screen2.config(bg="#00bd56")  # Corrected to config instead of configur
            
            Label(screen2, text="DECRYPTED MESSAGE", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
            text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, decrypted_message)
            text2.config(fg="black")  # Set text color to black for readability

        except Exception as e:
            messagebox.showerror("Error", "Failed to decrypt message. Ensure it is a valid base64 encoded string.")

    else:
        messagebox.showerror("Error", "Invalid password")

def encrypt():
    password = code.get()
    if password == "1234":
        message = text1.get(1.0, END).strip()
        if not message:
            messagebox.showwarning("Warning", "Please enter a message to encrypt.")
            return
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypted_message = base64_bytes.decode("ascii")  # Corrected variable name

        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.config(bg="#ed3833")  # Corrected to config instead of configur

        Label(screen1, text="ENCRYPTED MESSAGE", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypted_message)
        text2.config(fg="black")  # Set text color to black for readability

    else:
        messagebox.showerror("Error", "Invalid password")

def app_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x389")  # Corrected to 'x' instead of '×'

    # Load and set icon
    image_icon = Image.open("Keys.ico")  # Open the .ico file using Pillow
    icon_photo = ImageTk.PhotoImage(image_icon)  # Convert to PhotoImage
    screen.iconphoto(False, icon_photo)  # Set the icon for the app
    screen.title("PctApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width="23", bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width="23", bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width="50", bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

app_screen()
