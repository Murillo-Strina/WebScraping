from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import tkinter as tk
import re
from tkinter import messagebox, ttk

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def show_color(r, g, b):
    window = tk.Tk()
    window.title("RGB Color")
    window.geometry("350x250")
    center_window(window)
    color_hex = f'#{int(r):02x}{int(g):02x}{int(b):02x}'
    window.configure(bg=color_hex)
    text_color = 'white' if (r * 0.299 + g * 0.587 + b * 0.114) < 186 else 'black'
    label = tk.Label(window, text=f'RGB({r}, {g}, {b})\nHEX: {color_hex}', bg=color_hex, fg=text_color, font=('Arial', 14))
    label.pack(expand=True)
    window.mainloop()

def get_color_from_input():
    hex_code = entry.get().strip()
    if not re.fullmatch(r'[0-9a-fA-F]{6}', hex_code):
        messagebox.showerror("Error", "Please enter a valid hexadecimal code with 6 characters (Don't need the #).")
        return
    hex_code = f'#{hex_code}'

    try:
        global browser
        if browser is None:
            service = Service(ChromeDriverManager().install())
            browser = webdriver.Chrome(service=service)
            url = "https://www.w3schools.com/colors/colors_picker.asp"
            browser.get(url)
        hex_input = browser.find_element(By.ID, 'entercolor')
        hex_input.clear()
        hex_input.send_keys(hex_code)
        browser.find_element(By.XPATH, '//button[text()="OK"]').click()
        color_rgb = browser.find_element(By.ID, 'colorrgbDIV').text
        r, g, b = [int(x) for x in color_rgb.replace('rgb(', '').replace(')', '').split(',')]
        show_color(r, g, b)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

browser = None

root = tk.Tk()
root.title("HEX COLOR")
root.geometry("300x200")
center_window(root)
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)
label = ttk.Label(frame, text="Enter HEX code:")
label.pack(pady=10)
entry = ttk.Entry(frame)
entry.pack(pady=5)
button = ttk.Button(frame, text="Show Color", command=get_color_from_input)
button.pack(pady=20)

root.mainloop()

if browser:
    browser.quit()
