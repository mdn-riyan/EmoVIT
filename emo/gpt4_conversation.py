import os
import openai
import json

# Fungsi untuk memanggil API GPT-4 OpenAI
def generate_chat_completion(messages, model="gpt-4", temperature=1, max_tokens=None):
    openai.api_key = "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"  # Ganti dengan OpenAI API Key Anda
    response = openai.ChatCompletion.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=messages
    )
    return response['choices'][0]['message']['content']

# Pastikan nama class dan list file yang benar
class_name = 'sadness'

# Path folder yang berisi file caption
caption_folder_path = './emo/cap-ano/' + class_name + '/'
filelist = os.listdir(caption_folder_path)

# Periksa file yang ada, pastikan hanya file, bukan direktori
filelist = [file for file in filelist if os.path.isfile(os.path.join(caption_folder_path, file))]

# Pastikan ada file untuk diproses
if not filelist:
    print(f"Tidak ada file di folder {caption_folder_path}")
else:
    # Path prompt
    prompt_path = "./emo/prompt/conversation.txt"
    with open(prompt_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Loop untuk memproses file yang ada di folder
    for i in range(min(1000, len(filelist))):  # Maksimal 1000 file, atau sesuai jumlah file
        name = filelist[i]
        caption_path = os.path.join(caption_folder_path, name)  # Gabungkan path ke file
        print(f"Memproses file {caption_path}")
        
        # Pastikan file bisa dibuka
        try:
            with open(caption_path, 'r', encoding='utf-8') as file:
                caption = file.read()
            
            messages = [
                {"role": "system", "content": content},
                {"role": "user", "content": caption}
            ]

            # Panggil API GPT-4
            response_text = generate_chat_completion(messages)

            # Simpan output ke file baru
            output_folder = "./emo/conversation/" + class_name + "/"
            os.makedirs(output_folder, exist_ok=True)  # Buat folder jika belum ada
            out_path = os.path.join(output_folder, name)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(response_text)

        except FileNotFoundError:
            print(f"File {caption_path} tidak ditemukan!")
            continue  # Lanjutkan ke file berikutnya
        except IsADirectoryError:
            print(f"{caption_path} adalah direktori, bukan file!")
            continue  # Lanjutkan ke file berikutnya
        except Exception as e:
            print(f"Error saat memproses file {caption_path}: {str(e)}")
            continue  # Lanjutkan ke file berikutnya
