from PIL import Image, ImageFilter
import os

def blur_images_in_directory(input_dir, output_dir, blur_radius=5):
    """
    Blurs all images in the Input Directory and saves them to the Output Directory.

    Args:
    input_dir (str): Directory containing the images to be processed.
    output_dir (str): Directory where the processed images will be saved.
    blur_radius (int, optional): Radius specifying the amount of blur. Default is 5.
    """

    # Output Directory yoksa oluştur
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Input Directory'deki tüm dosyaları oku
    for filename in os.listdir(input_dir):
        # Yalnızca görüntü dosyalarını işlemek için uzantıyı kontrol et
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Tam dosya yolunu oluştur
            file_path = os.path.join(input_dir, filename)
            
            # Görüntüyü aç
            with Image.open(file_path) as img:
                # Blur filtresi uygula
                blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))
                
                # Output Directory'e kaydet
                output_path = os.path.join(output_dir, filename)
                blurred_img.save(output_path)
                print(f"{filename} bulanıklaştırıldı ve kaydedildi: {output_path}")

# Örnek kullanım
input_directory = 'input'
output_directory = 'output'
blur_radius = 2

blur_images_in_directory(input_directory, output_directory, blur_radius)
