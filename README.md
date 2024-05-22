# EmoVIT
Official code for paper EmoVIT: Revolutionizing Emotion Insights with Visual Instruction Tuning ｜ CVPR 2024

```
EmoSet/
|
+--LAVIS
|
+--emo
    |
    +--annotation (Results of Emoset Decompression.)
    |
    +--cap-ano (Create the folders required for the program execution before running it.)
    |
    +--caption (Create the folders required for the program execution before running it.)
    |
    +--reasoning (Create the folders required for the program execution before running it.)
    |
    +--conversation_new100 (Create the folders required for the program execution before running it.)
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
        +--train_image (Emovit does not need all the photos; place the photos required for training here.)
                |
                ........
```
You can find two main folders in our project structure, 'emo' and 'LAVIS'.  
The 'LAVIS' folder can be obtained from https://drive.google.com/file/d/1YLgOVlJNIdyOOlppX0uPMXGxVT37YqbF/view?usp=drive_link .
Arrange the image data into the correct locations as described above. For example, EmoSet can be obtained from https://vcc.tech/EmoSet.

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

## Generate captions
1. python ./emo/caption.py (To obtain image captions，select the 'path' based on the class to be processed.) 
2. python ./emo/cap-anno.py (To write the attributes and captions of the image into a file，select the 'path' based on the class to be processed.)  
3. python ./emo/gpt4_reasoning.py or python ./emo/gpt4_conversation.py (Using the above file as input data, instruct gpt4 to generate questions.)  
#Remember to change the key  
#If you wish to adjust the prompt, you can go to the 'prompt' folder.
4. python ./emo/all.py (Integrate the results of reasoning, conversation, and classification.)

Following these steps, you can create instructions. If you want to skip this step, you can use the instructions we created using Emoset. (However, image data must still be downloaded from Emoset's official website.)
conversation:
https://drive.google.com/file/d/1E8UEH09y0CiAT4Hg7rm975AR3JCjEHeM/view?usp=drive_link
reasoning:
https://drive.google.com/file/d/1MTNHFzasCb0F921P0itaH-x8vN2OvxEu/view?usp=drive_link
As for the generation method of categorical data, it does not need to rely on GPT for creation; it can be directly produced (you can observe the prompt in all.py)."

## Train emoVIT 
- Prepare weight  
  You can obtain the weights for Vicuna from the page https://github.com/lm-sys/FastChat/blob/main/docs/vicuna_weights_version.md , we are using version 1.1.
  Place the downloaded file into LAVIS/lavis/weight/vicuna-7b-2/
  
- Run  
    - training  
    cd LAVIS  
    python train.py --cfg-path FT.yaml  

- Parameter  
  LAVIS/FT.yaml (Setting of hyperparameter)  
  LAVIS/lavis/configs/models/blip2/blip2_instruct_vicuna7b.yaml (Select the location of llm weight)  
  LAVIS/lavis/configs/datasets/coco/defaults_vqa.yaml (Select the location of your data)
  LAVIS/lavis/runners/runner_base.py (Change the name of the weight file to be saved.)

## Inference emoVIT
If you haven't trained your own weights yet, you can use the model_weights1.pth provided in the LAVIS folder.  
python ./LAVIS/test.py  
