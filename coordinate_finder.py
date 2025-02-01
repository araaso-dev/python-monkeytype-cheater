import tkinter as tk
from tkinter import ttk
import pyautogui

class CoordinateFinder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Coordinate Finder")
        self.root.attributes('-topmost', True)  # Keep window on top
        self.root.geometry("300x200")
        
        # Make window semi-transparent
        self.root.attributes('-alpha', 0.1)
        
        # Create labels
        self.pos_label = ttk.Label(self.root, text="Current Position: (0, 0)")
        self.pos_label.pack(pady=10)
        
        self.click_label = ttk.Label(self.root, text="Click Positions:\nNone")
        self.click_label.pack(pady=10)
        
        self.instructions = ttk.Label(self.root, text=(
            "Instructions:\n"
            "1. Move mouse to find coordinates\n"
            "2. Click to record positions\n"
            "3. Right-click to reset\n"
            "4. Press 'q' to quit"
        ))
        self.instructions.pack(pady=10)
        
        # Store clicked positions
        self.clicks = []
        
        # Bind events
        self.root.bind('<Motion>', self.update_position)
        self.root.bind('<Button-1>', self.record_click)
        self.root.bind('<Button-3>', self.reset_clicks)
        self.root.bind('q', lambda e: self.root.quit())
        
        # Start update loop
        self.update_coordinates()
        
    def update_position(self, event=None):
        x, y = pyautogui.position()
        self.pos_label.config(text=f"Current Position: ({x}, {y})")
        
    def record_click(self, event=None):
        x, y = pyautogui.position()
        if len(self.clicks) < 2:
            self.clicks.append((x, y))
            self.update_click_label()
            
    def reset_clicks(self, event=None):
        self.clicks = []
        self.update_click_label()
        
    def update_click_label(self):
        if not self.clicks:
            text = "Click Positions:\nNone"
        elif len(self.clicks) == 1:
            text = f"Click Positions:\nTop-left: {self.clicks[0]}"
        else:
            width = self.clicks[1][0] - self.clicks[0][0]
            height = self.clicks[1][1] - self.clicks[0][1]
            text = (
                f"Click Positions:\n"
                f"Top-left: {self.clicks[0]}\n"
                f"Bottom-right: {self.clicks[1]}\n"
                f"Size: {width}x{height}"
            )
        self.click_label.config(text=text)
        
    def update_coordinates(self):
        self.update_position()
        self.root.after(100, self.update_coordinates)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    finder = CoordinateFinder()
    finder.run() 