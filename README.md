# Screen Tools 🖥️

A collection of Python utilities for screen interaction and automation.

## 🛠️ Tools Included

### 1. Coordinate Finder 🎯

A visual tool to find and record screen coordinates with a semi-transparent overlay window.

### 2. Screen Typer ⌨️

An automated typing tool that captures text from the screen and types it automatically (optimized for MonkeyType).

## 📋 Prerequisites

- Python 3.x
- Required packages:
  ```
  pyautogui
  pillow
  pytesseract
  keyboard
  numpy
  ```
- Tesseract OCR installed (for Screen Typer)
  - Windows: Install from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
  - Path: `C:\Program Files\Tesseract-OCR\tesseract.exe`

## 🚀 Installation

1. Clone this repository
2. Install required packages:
   ```bash
   pip install pyautogui pillow pytesseract keyboard numpy
   ```
3. Install Tesseract OCR if you plan to use the Screen Typer

## 📖 How to Use

### Coordinate Finder 🎯

1. Run the tool:

   ```bash
   python coordinate_finder.py
   ```

2. Features:

   - 🖱️ Move your mouse to see real-time coordinates
   - 📌 Left-click to record positions (max 2 points)
   - 🔄 Right-click to reset recorded positions
   - ⌨️ Press 'q' to quit
   - 🔍 Window stays on top and is semi-transparent for easy use

3. Use Cases:
   - Finding coordinates for automation scripts
   - Measuring screen regions
   - Getting dimensions between two points

### Screen Typer ⌨️

1. Run the tool:

   ```bash
   python screen_typer.py
   ```

2. Usage:

   - ⌨️ Press 'backspace' to start a 15-second typing session
   - ⏹️ Press 'q' to quit at any time
   - 📸 The tool uses two capture regions:
     - First Region (154, 470, 1726, 660): Captures first 3 lines of text
     - Second Region (177, 531, 1681, 627): Captures last 2 lines of text
   - 🔄 Automatically switches between regions during typing
   - 🤖 The tool will:
     - Capture text from the appropriate screen area
     - Convert it to text using OCR
     - Type it automatically at high speed

3. Features:
   - 🚀 Optimized for speed typing tests
   - 📷 Automatic screenshot saving
   - 🔄 Smart region switching for complete text coverage
   - ⚡ Minimal delays for maximum performance
   - 🎯 Adaptive capture regions for different text positions

## ⚠️ Notes

- Screen Typer is optimized for MonkeyType but can be adapted for other typing tests
- Coordinate values may need adjustment based on your screen resolution
- The dual capture region system ensures complete text coverage during typing tests
- You may need to adjust the coordinates based on your screen size and MonkeyType window position
- Screenshots are automatically saved in a `screenshots` directory

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📜 License

This project is open source and available under the MIT License.
