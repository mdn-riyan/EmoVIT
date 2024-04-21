# EmoVIT
Official code for paper EmoVIT: Revolutionizing Emotion Insights with Visual Instruction Tuning ｜ CVPR 2024

```
EmoSet/
|
+--LAVIS
|
+--emo
    |
    +--annotation
    |
    +--cap-ano
    |
    +--caption
    |
    +--prompt
    |
    +--image
        +--amusement (Results of Emoset Decompression)
        |
        +--anger (Results of Emoset Decompression)
        |
        .
        .
        .
        |
        +--result_image
                |
                ........
```
You can find two main folders in our project structure, 'emo' and 'LAVIS'.  
The 'emo' folder can be obtained from https://drive.google.com/file/d/10W6ItM3CkuKHv8f6Z8IXxfQIYEmyRNFf/view?usp=drive_link , 
while the 'LAVIS' folder can be obtained from https://drive.google.com/file/d/1QXlJxzBKTk34wP0kFWyG2XJnG_XhRfFR/view?usp=drive_link .
Arrange the image data into the correct locations as described above. For example, EmoSet can be obtained from https://vcc.tech/EmoSet.
The folders 'annotation', 'cap-ano', 'caption', 'image', and 'result' are empty and need to be created manually (GitHub does not support empty folder, or you can download from https://drive.google.com/drive/folders/1DL-bIxUtHaTzfmhXuwn1-sCLx42-Oy0V?usp=sharing )

## Install related packages
conda create --name emovit python=3.8  
conda activate emovit  
cd emovit  
pip install -r requirements.txt  

## Install lavis
pip install salesforce-lavis  
(If not work, please proceed as follows.)  
cd ..  
git clone https://github.com/salesforce/LAVIS.git  
cd LAVIS  
pip install -e . (Please remove 'open3d' from the 'requirements.txt' file to avoid version conflicts.)  
Cut the 'lavis' folder and paste it into the 'lib' folder.  

## caption
1. python ./emo/caption.py (to obtain image captions，select the 'path' based on the class to be processed.) 
2. python ./emo/cap-anno.py (to write the attributes and captions of the image into a file，select the 'path' based on the class to be processed.)  
3. python ./emo/gpt4_reasoning.py or python ./emo/gpt4_conversation.py (using the above file as input data, instruct gpt4 to generate questions.)  
#Remember to change the key  
#If you wish to adjust the prompt, you can go to the 'prompt_config.txt' file.

## Train emoVIT 
- Run  
    - training  
    python train.py --cfg-path FT.yaml  

    - inference  
    the use of testing are in inference.py  

- Parameter  
  LAVIS/FT.yaml (Setting of hyperparameter)  
  LAVIS/lavis/configs/models/blip2/blip2_instruct_vicuna7b.yaml (Select the location of llm weight)  
  LAVIS/lavis/configs/datasets/coco/defaults_vqa.yaml (Select the location of your data)  
