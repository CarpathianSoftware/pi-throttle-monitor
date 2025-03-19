import tkinter as tk
import subprocess
import threading

def get_throttled_status():
    try:
        result = subprocess.run(["vcgencmd", "get_throttled"], capture_output=True, text=True)
        hex_value = result.stdout.strip().split("=")[-1]
        return int(hex_value, 16)
    except Exception as e:
        print("Error fetching throttled status:", e)
        return 0

def update_ui():
    throttled = get_throttled_status()
    binary = f"{throttled:032b}"[::-1]  # Convert to 32-bit binary and reverse it for bit indexing
    
    for bit, section in sections.items():
        if bit in {0, 1, 2, 3}:
            color, text_color = ("red", "white") if binary[bit] == '1' else ("#2c2c2c", "white")
        elif bit in {16, 17, 18, 19}:
            color, text_color = ("orange", "black") if binary[bit] == '1' else ("#2c2c2c", "white")
        else:
            color, text_color = "#2c2c2c", "white"
        
        section.config(bg=color, fg=text_color)
    
    root.after(refresh_interval * 1000, update_ui)

def start_monitoring():
    threading.Thread(target=update_ui, daemon=True).start()

root = tk.Tk()
root.title("Pi Throttle Monitor")
root.configure(bg="#1e1e1e")
root.geometry("640x100")  # Adjusted window size to fit boxes perfectly
root.resizable(False, False)  # Disable resizing

def create_stylish_label(parent, text):
    return tk.Label(parent, text=text, width=20, height=2, font=("Arial", 9), relief="solid", 
                    bg="#2c2c2c", fg="white", bd=1, padx=2, pady=2, highlightbackground="#444", highlightthickness=1)

refresh_interval = 5  # Default update interval in seconds
sections = {}
labels = {
    0: "Under-voltage detected", 1: "Arm frequency capped", 2: "Currently throttled", 3: "Soft temp limit active",
    16: "Under-voltage occurred", 17: "Arm freq. cap occurred", 18: "Throttling occurred", 19: "Soft temp limit occurred"
}

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=5, padx=5)

bit_positions = [0, 1, 2, 3, 16, 17, 18, 19]

for idx, bit in enumerate(bit_positions):
    row, col = divmod(idx, 4)
    section = create_stylish_label(frame, labels[bit])
    section.grid(row=row, column=col, padx=5, pady=5)
    sections[bit] = section

start_monitoring()
root.mainloop()
