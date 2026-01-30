"""
Simple Slideshow for Adafruit MAGTag
Displays images from the /images folder
Use buttons to navigate: D11 (left) = previous, D12 (right) = next
"""

import time
import board
import displayio
import terminalio
from adafruit_magtag.magtag import MagTag
from digitalio import DigitalInOut, Direction, Pull

# Initialize the MagTag
magtag = MagTag()

# List of image filenames (place these in /images/ folder on your MAGTag)
# Images should be 296x128 pixels, 2-bit grayscale BMP format
IMAGES = [
    "/images/slide1.bmp",
    "/images/slide2.bmp",
    "/images/slide3.bmp",
    "/images/slide4.bmp",
]

# Current slide index
current_slide = 0

# Auto-advance settings (set to 0 to disable)
AUTO_ADVANCE_SECONDS = 5  # Change slide every 5 seconds

def show_slide(index):
    """Display the slide at the given index"""
    try:
        # Clear the display
        magtag.graphics.set_background(IMAGES[index])
        
        # Add slide number text
        magtag.add_text(
            text_position=(5, 5),
            text_font=terminalio.FONT,
            text=f"Slide {index + 1}/{len(IMAGES)}",
            text_color=0x000000,
        )
        
        # Refresh the display
        magtag.refresh()
        
        print(f"Showing slide {index + 1}: {IMAGES[index]}")
        
    except Exception as e:
        print(f"Error loading slide {index}: {e}")
        # Show error message
        magtag.set_text(f"Error loading\n{IMAGES[index]}")

def next_slide():
    """Advance to the next slide"""
    global current_slide
    current_slide = (current_slide + 1) % len(IMAGES)
    show_slide(current_slide)

def previous_slide():
    """Go back to the previous slide"""
    global current_slide
    current_slide = (current_slide - 1) % len(IMAGES)
    show_slide(current_slide)

# Show the first slide
show_slide(current_slide)

# Main loop
last_advance_time = time.monotonic()

while True:
    # Check button presses
    # Button D11 (left button) - previous slide
    if magtag.peripherals.button_a_pressed:
        previous_slide()
        last_advance_time = time.monotonic()  # Reset auto-advance timer
        time.sleep(0.2)  # Debounce
    
    # Button D12 (right button) - next slide
    if magtag.peripherals.button_b_pressed:
        next_slide()
        last_advance_time = time.monotonic()  # Reset auto-advance timer
        time.sleep(0.2)  # Debounce
    
    # Auto-advance if enabled
    if AUTO_ADVANCE_SECONDS > 0:
        if time.monotonic() - last_advance_time >= AUTO_ADVANCE_SECONDS:
            next_slide()
            last_advance_time = time.monotonic()
    
    time.sleep(0.1)
