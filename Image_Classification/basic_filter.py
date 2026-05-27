from PIL import Image, ImageEnhance, ImageOps
import matplotlib.pyplot as plt
import os

def apply_artistic_filter(image_path, output_path="artistic_image.png"):
    try:
        # 1. Open and resize the image
        img = Image.open(image_path)
        img_resized = img.resize((256, 256))  # Bumped up resolution slightly for cleaner colors

        # 2. Boost Contrast & Sharpness for that graphic novel pop
        contrast_eng = ImageEnhance.Contrast(img_resized)
        img_high_contrast = contrast_eng.enhance(1.8) # 1.8x contrast boost
        
        sharp_eng = ImageEnhance.Sharpness(img_high_contrast)
        img_styled = sharp_eng.enhance(2.0) # Sharpen edges significantly

        # 3. Apply a Cyberpunk Pop-Art Duotone effect 
        # Converts image to grayscale, then maps darks to deep Cyan and lights to hot Magenta
        img_gray = ImageOps.grayscale(img_styled)
        img_cyberpunk = ImageOps.colorize(
            img_gray, 
            black="#001122",   # Deep space dark blue/cyan
            white="#ff007f"    # Neon cyberpunk magenta
        )

        # 4. Save and export without plot borders
        plt.imshow(img_cyberpunk)
        plt.axis('off')
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()
        print(f"Artistic Cyberpunk image successfully saved as '{output_path}'.")

    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    print("Cyberpunk Artistic Filter Processor (type 'exit' to quit)\n")
    while True:
        image_path = input("Enter image filename (or 'exit' to quit): ").strip()
        if image_path.lower() == 'exit':
            print("Goodbye!")
            break
        if not os.path.isfile(image_path):
            print(f"File not found: {image_path}")
            continue
            
        # Derive output filename
        base, ext = os.path.splitext(image_path)
        output_file = f"{base}_cyberpunk{ext}"
        apply_artistic_filter(image_path, output_file)