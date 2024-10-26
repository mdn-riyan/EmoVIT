import torch
from PIL import Image
import requests
from lavis.models import load_model_and_preprocess
import os

cached_file = './LAVIS/model_weights1.pth'
if os.path.exists(cached_file):
    state_dict = torch.load(cached_file, map_location="cpu")
else:
    print(f"File {cached_file} tidak ditemukan!")

# Memeriksa apakah CUDA tersedia dan menetapkan perangkat ke GPU atau CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
state_dict = torch.load(cached_file, map_location="cpu", weights_only=True)

# Memuat model dan preprocess dengan menyertakan perangkat yang ditentukan
try:
    model, vis_processors, _ = load_model_and_preprocess(
        name="blip2_opt", 
        model_type="pretrain_opt2.7b", 
        is_eval=True, 
        device=device
    )
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    raise
# Path untuk gambar dan file keluaran
path = './emo/image/sadness/'
output_path = './emo/caption/sadness/'

# Pastikan path gambar dan keluaran ada
if not os.path.exists(path):
    print(f"Path not found: {path}")
    raise Exception(f"Image directory {path} does not exist.")

if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(f"Output directory {output_path} created.")

filelist = os.listdir(path)

# Pengecekan jika tidak ada file
if len(filelist) == 0:
    print("No files found in directory.")
else:
    print(f"Found {len(filelist)} files in directory.")

# Looping melalui file gambar
for name in filelist:
    print('-----------')
    print(f"Processing file: {name}")
    
    out_file = os.path.join(output_path, name.split('.')[0] + '.txt')
    image_file = os.path.join(path, name)
    
    # Buka dan proses gambar
    try:
        raw_image = Image.open(image_file)
        print(f"Image {name} opened successfully.")
    except Exception as e:
        print(f"Error opening image {name}: {e}")
        continue
    
    try:
        # Preprocess gambar untuk model
        image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
        print(f"Image processed successfully. Shape: {image.shape}")
    except Exception as e:
        print(f"Error processing image {name}: {e}")
        continue
    
    # Generate caption menggunakan model
    try:
        caption = model.generate({"image": image})
        print(f"Caption generated: {caption[0]}")
    except Exception as e:
        print(f"Error generating caption for {name}: {e}")
        continue
    
    # Simpan caption ke file
    try:
        with open(out_file, 'w') as f:
            f.write(caption[0])
        print(f"Caption saved to {out_file}")
    except Exception as e:
        print(f"Error writing caption to file {out_file}: {e}")
        continue
