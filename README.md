# English-Mispronunciation-Detection-Module-Integrated-In-A-Chatbot

Second language learning can be difficult. Speaking skills usually are the more difficult to develop. This is because learnears sometimes do not practice enough. Also, learners lack of appropriate feedback. Develop and improve this skill is achieved practicing constantly. For that reason this mispronunciation detection system was developed. It is integrated to an AIML chatbot to make an interaction between users and the module. 

The technologies used are:
- A Transformer Network
- An AIML chatbot
- A string alignment algorithm

The Transformer Network was trained using ESPnet toolkit. It was employed the LibriSpeech and L2-ARCTIC datasets.

# Installation

It is needed first install ESPnet (https://github.com/espnet/espnet).

```git clone https://github.com/MarcosLalo28/Mispronunciation-Detection-Module-Integrated-In-A-Chatbot.git```

Download the pre-trained model from https://www.mediafire.com/file/lv2s8ouedbjye3m/100epoch.pth/file and put it into the ```/exp/asr_train_asr_transformer_raw_bpe``` path.

You can also use another ESPnet pre-trained model or train your own model.


Run with:
```
python3 English_Mispronunciation_Detection.py
```



