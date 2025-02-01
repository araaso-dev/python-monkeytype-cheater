import pytesseract
import pyautogui
import time
from PIL import ImageGrab, Image
import keyboard
import numpy as np
import os

# Configure pytesseract path if needed (Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_monkeytype_area(use_first_coords=True):
    # First capture area coordinates
    capture_area_1 = (
        154,  # Left coordinate (x1)
        470,  # Top coordinate (y1)
        1726, # Right coordinate (x2)
        660   # Bottom coordinate (y2)
    )
    
    # Second capture area coordinates
    capture_area_2 = (
        177,  # Left coordinate (x1)
        531,  # Top coordinate (y1)
        1681, # Right coordinate (x2)
        627   # Bottom coordinate (y2)
    )
    
    # Choose which coordinates to use
    capture_area = capture_area_1 if use_first_coords else capture_area_2
    
    # Capture screenshot
    screenshot = ImageGrab.grab(bbox=capture_area)
    
    # Convert and enhance screenshot
    screenshot = screenshot.convert('L')
    img_array = np.array(screenshot)
    enhanced = np.clip(img_array * 1.5, 0, 255).astype(np.uint8)
    enhanced_image = Image.fromarray(enhanced)
    
    return enhanced_image

def save_screenshot(image, base_filename="capture"):
    # Create screenshots directory if it doesn't exist
    os.makedirs("screenshots", exist_ok=True)
    
    filename = f"{base_filename}_{time.time()}.png"
    filepath = os.path.join("screenshots", filename)
    image.save(filepath)
    return filepath

def type_with_speed(text):
    # Set up pyautogui for fastest possible typing
    pyautogui.PAUSE = 0.05
     
    words = text.split()
    for i, word in enumerate(words):
        if keyboard.is_pressed('q'):
            return
            
        # Type the word with no delay
        pyautogui.write(word, interval=0)
        
        # Add space between words with no delay
        if i < len(words) - 1:
            pyautogui.press('space')

def capture_and_type():
    while True:
        if keyboard.is_pressed('q'):
            print("Quitting...")
            break
            
        if keyboard.is_pressed('backspace'):
            print("Starting 15-second typing session...")
            start_time = time.time()
            first_capture = True  # Flag to track if it's the first capture
            
            while time.time() - start_time < 15:
                if keyboard.is_pressed('q'):
                    return
                
                # Capture and process screenshot
                # Use first coordinates only for first capture, then switch to second
                screenshot = capture_monkeytype_area(first_capture)
                screenshot_path = save_screenshot(screenshot)
                
                # Process text
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                text = pytesseract.image_to_string(screenshot, config=custom_config)
                print(f"Captured text: {text.strip()}")
                
                # Type the text
                type_with_speed(text.strip())
                
                # Press space after typing
                pyautogui.press('space')
                
                # After first capture, always use second coordinates
                if first_capture:
                    first_capture = False
                
                # Small delay to ensure screen updates
                time.sleep(0.5)
            
            print("15-second session completed!")

if __name__ == "__main__":
    # Set all pyautogui delays to 0 for maximum speed
    pyautogui.MINIMUM_DURATION = 0
    pyautogui.MINIMUM_SLEEP = 0
    pyautogui.PAUSE = 0
    
    print("Press 'backspace' to start a 15-second typing session")
    print("Press 'q' to quit")
    
    try:
        capture_and_type()
    except Exception as e:
        print(f"An error occurred: {e}") 