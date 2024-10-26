import os
import json

class_name = 'sadness'

path = './emo/caption/' + class_name + '/'
filelist = os.listdir(path)

caption_path = os.path.join('./emo/caption/', class_name) + '/'
annotation_path = os.path.join('./emo/annotation/', class_name) + '/'
output_dir = os.path.join('./emo/cap-ano/', class_name)

# Membuat folder output jika belum ada
os.makedirs(output_dir, exist_ok=True)

for name in filelist:
    print(name)
    with open(os.path.join(caption_path, name), 'r', encoding='utf-8') as file:
        caption = file.read()

    annotation_file = os.path.join(annotation_path, name.split('txt')[0] + 'json')
    with open(annotation_file, 'r') as json_file:
        annotation = json.load(json_file)

    out = caption
    out = out + '\n\n'
    out = out + 'emotion: ' + str(annotation['emotion'])
    
    if 'brightness' in annotation:
        out = out + '\n' + 'brightness: ' + str(annotation['brightness'])
    if 'colorfulness' in annotation:
        out = out + '\n' + 'colorfulness: ' + str(annotation['colorfulness'])
    if 'object' in annotation:
        out = out + '\n' + 'object: ' + str(annotation['object'])
    if 'facial_expression' in annotation:
        out = out + '\n' + 'facial_expression: ' + str(annotation['facial_expression'])
    if 'human_action' in annotation:
        out = out + '\n' + 'human_action: ' + str(annotation['human_action'])

    # Output path
    out_path = os.path.join(output_dir, name)

    # Menulis output ke file
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(out)
