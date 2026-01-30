# MAGTag Slideshow

A simple slideshow application for the Adafruit MAGTag e-ink display.

## Features
- Display images on the MAGTag's 2.9" e-ink screen (296x128 pixels)
- Navigate with buttons: left button (D11) for previous, right button (D12) for next
- Optional auto-advance every 5 seconds
- Shows current slide number

## Setup Instructions

### 1. Install CircuitPython on your MAGTag
- Download the latest CircuitPython for MAGTag from https://circuitpython.org/board/adafruit_magtag_2.9_grayscale/
- Connect your MAGTag via USB
- Double-press the reset button to enter bootloader mode (MAGTAGBOOT drive appears)
- Copy the .UF2 file to the MAGTAGBOOT drive

### 2. Install Required Libraries
- Download the latest CircuitPython library bundle from https://circuitpython.org/libraries
- Extract the bundle and copy these folders to the `lib` folder on your CIRCUITPY drive:
  - `adafruit_magtag`
  - `adafruit_display_text`
  - `adafruit_bitmap_font`
  - `adafruit_io`
  - `adafruit_requests`
  - `adafruit_portalbase`

### 3. Prepare Your Images
- Images must be 296x128 pixels
- Format: 2-bit grayscale BMP (4 colors)
- You can use GIMP, Photoshop, or the included Python script to convert images

### 4. Upload Files
- Create an `images` folder on your CIRCUITPY drive
- Copy your BMP images to the `/images/` folder
- Name them `slide1.bmp`, `slide2.bmp`, etc. (or update the IMAGES list in code.py)
- Copy `code.py` to the root of your CIRCUITPY drive

### 5. Run
- The slideshow will start automatically when you save code.py
- The MAGTag will restart and begin displaying your slides

## Image Preparation

### Using the Python Script
Use the included `convert_images.py` script to convert your images:

```bash
python convert_images.py input_image.jpg output_image.bmp
```

### Using GIMP
1. Open your image in GIMP
2. Image → Scale Image → Set to 296x128 pixels
3. Image → Mode → Grayscale
4. Image → Mode → Indexed → Use 4 colors
5. File → Export As → Choose BMP format

## Customization

Edit `code.py` to customize:

- **AUTO_ADVANCE_SECONDS**: Set to 0 to disable auto-advance, or change the interval
- **IMAGES**: Update the list with your image filenames
- Add more button functions using buttons C and D

## Troubleshooting

**Images won't load**: Ensure they are exactly 296x128 pixels and in 2-bit BMP format

**Display not refreshing**: E-ink displays take a few seconds to update - this is normal

**Buttons not responding**: Make sure you're pressing the correct buttons (D11/D12 on the left side)

## Button Layout
```
[D15] Top
[D14] 
[D12] Right (Next slide) →
[D11] Left (Previous slide) ←
```

Enjoy your MAGTag slideshow!
