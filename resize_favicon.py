from PIL import Image
import os

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        # Convert to RGBA if not already
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Create a new image with white background
        background = Image.new('RGBA', img.size, (255, 255, 255, 0))
        
        # Paste the image on the background
        background.paste(img, (0, 0), img)
        
        # Resize the image
        resized = background.resize((size, size), Image.Resampling.LANCZOS)
        
        # Save the resized image
        resized.save(output_path, 'PNG', optimize=True)

def main():
    # Create output directory if it doesn't exist
    output_dir = 'assets/img/favicon'
    os.makedirs(output_dir, exist_ok=True)
    
    # Input favicon path
    input_favicon = 'assets/img/favicon.png'
    
    # Define sizes for different purposes
    sizes = {
        'favicon-16.png': 16,
        'favicon-32.png': 32,
        'favicon-144.png': 144,
        'favicon-192.png': 192,
        'favicon-512.png': 512,
        'apple-touch-icon.png': 180,
        'maskable-192.png': 192,
        'maskable-512.png': 512
    }
    
    # Resize for each size
    for filename, size in sizes.items():
        output_path = os.path.join(output_dir, filename)
        print(f"Resizing to {size}x{size} -> {output_path}")
        resize_image(input_favicon, output_path, size)

if __name__ == "__main__":
    main()
    print("Favicon resizing complete!") 