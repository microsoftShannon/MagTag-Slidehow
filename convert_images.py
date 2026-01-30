#!/usr/bin/env python3
"""
Image Converter for Adafruit MAGTag
Converts images to 296x128, 2-bit grayscale BMP format
"""

import sys
from PIL import Image

MAGTAG_WIDTH = 296
MAGTAG_HEIGHT = 128

def convert_image(input_path, output_path):
    """
    Convert an image to MAGTag-compatible format
    
    Args:
        input_path: Path to input image
        output_path: Path for output BMP file
    """
    try:
        # Open the image
        print(f"Opening {input_path}...")
        img = Image.open(input_path)
        
        # Convert to grayscale
        print("Converting to grayscale...")
        img = img.convert('L')
        
        # Resize to MAGTag dimensions while maintaining aspect ratio
        print(f"Resizing to {MAGTAG_WIDTH}x{MAGTAG_HEIGHT}...")
        img.thumbnail((MAGTAG_WIDTH, MAGTAG_HEIGHT), Image.Resampling.LANCZOS)
        
        # Create a new image with MAGTag dimensions and paste the resized image
        magtag_img = Image.new('L', (MAGTAG_WIDTH, MAGTAG_HEIGHT), color=255)
        
        # Center the image
        x = (MAGTAG_WIDTH - img.width) // 2
        y = (MAGTAG_HEIGHT - img.height) // 2
        magtag_img.paste(img, (x, y))
        
        # Convert to 2-bit (4 colors)
        print("Converting to 2-bit color depth...")
        magtag_img = magtag_img.convert('P', palette=Image.Palette.ADAPTIVE, colors=4)
        
        # Save as BMP
        print(f"Saving to {output_path}...")
        magtag_img.save(output_path, 'BMP')
        
        print(f"✓ Successfully converted {input_path} to {output_path}")
        print(f"  Size: {MAGTAG_WIDTH}x{MAGTAG_HEIGHT}")
        print(f"  Format: 2-bit grayscale BMP")
        
    except Exception as e:
        print(f"✗ Error converting image: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_images.py <input_image> [output_image]")
        print("\nExample:")
        print("  python convert_images.py photo.jpg slide1.bmp")
        print("\nSupported input formats: JPG, PNG, GIF, etc.")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    # Generate output filename if not provided
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        # Use input filename with .bmp extension
        output_path = input_path.rsplit('.', 1)[0] + '.bmp'
    
    convert_image(input_path, output_path)

if __name__ == "__main__":
    main()
