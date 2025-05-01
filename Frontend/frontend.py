import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Smart Grid Anomaly Detection")
root.geometry("1200x800")
# Dark theme colors
bg_color = "#212121"      # window background
panel_color = "#424242"   # panel/card background
fg_color = "#F5F5F5"      # light text
accent_green = "#4CAF50"
accent_blue = "#03A9F4"
accent_gray = "#616161"

root.configure(bg=bg_color)

# Fonts
title_font = ("Helvetica", 18, "bold")
header_font = ("Helvetica", 14, "bold")
text_font = ("Helvetica", 12)

# Top title
title_label = tk.Label(root, text="Smart Grid Anomaly Detection", bg=bg_color, fg=fg_color, font=title_font)
title_label.pack(pady=(20, 10))

# Top panels for key metrics
top_frame = tk.Frame(root, bg=bg_color)
top_frame.pack(fill="x", padx=20)
metrics = [("Total Devices", "150"), ("Anomalies Detected", "12"), ("Last Update", "2025-04-30 15:30")]
for i, (label, value) in enumerate(metrics):
    card = tk.Frame(top_frame, bg=panel_color, padx=15, pady=10)
    card.pack(side="left", expand=True, fill="both", padx=10)
    tk.Label(card, text=label, bg=panel_color, fg=fg_color, font=header_font).pack(anchor="w")
    val_color = accent_green if i == 1 else fg_color
    tk.Label(card, text=value, bg=panel_color, fg=val_color,
             font=("Helvetica", 20, "bold")).pack(anchor="w")

# Main content area
content_frame = tk.Frame(root, bg=bg_color)
content_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Left controls panel
left_frame = tk.Frame(content_frame, bg=bg_color)
left_frame.pack(side="left", fill="y")
buttons = [
    ("Configure\nSensors", accent_blue),
    ("Load Data", accent_blue),
    ("Detect Anomalies", accent_green),
    ("Reset", accent_gray)
]
for (text, color) in buttons:
    btn = tk.Button(left_frame, text=text, bg=color, fg=fg_color, font=text_font, relief="flat")
    btn.pack(fill="x", pady=5)

# Center visualization placeholder
center_frame = tk.Frame(content_frame, bg="#303030")
center_frame.pack(side="left", fill="both", expand=True, padx=10)
chart_label = tk.Label(center_frame, text="(Charts and Graphs Placeholder)",
                       bg="#303030", fg="#B0BEC5", font=text_font)
chart_label.place(relx=0.5, rely=0.5, anchor="center")

# Right anomalies table
right_frame = tk.Frame(content_frame, bg=bg_color)
right_frame.pack(side="left", fill="y")
tk.Label(right_frame, text="Anomalies", bg=bg_color, fg=fg_color, font=header_font).pack(pady=(0,5))
columns = ("Timestamp", "Device", "Reading", "Status")
tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=15)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")
tree.pack(side="left", fill="y")

# Sample data rows
sample_data = [
    ("2025-04-30 15:20", "Sensor A", "95.1", "Alert"),
    ("2025-04-30 15:22", "Sensor C", "NaN", "Error"),
    ("2025-04-30 15:25", "Sensor B", "87.3", "Alert"),
]
for row in sample_data:
    tree.insert("", "end", values=row)

# Scrollbar for table
scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Style configuration
style = ttk.Style(root)
style.theme_use("clam")  # use a neutral theme to allow color config
style.configure("Treeview",
                background="#303030",     # tree background
                foreground=fg_color,
                fieldbackground="#303030",
                rowheight=25,
                font=text_font)
style.configure("Treeview.Heading",
                background=panel_color,
                foreground=fg_color,
                font=header_font)
style.map('Treeview', background=[('selected', "#FFC107")])  # amber on selection

root.mainloop()
