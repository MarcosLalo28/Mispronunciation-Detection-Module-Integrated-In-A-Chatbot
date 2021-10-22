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

```python3 English_Mispronunciation_Detection.py ```

Automatically the AIML alice chatbot be loaded and the chatbot can be used.

![Screenshot from 2021-05-17 13-12-46](https://user-images.githubusercontent.com/92826076/138483469-f3e6bc39-14be-48a4-afe9-40694dfbb86d.png)

![Screenshot from 2021-05-17 13-20-14](https://user-images.githubusercontent.com/92826076/138483674-d9e5f1b7-0e4d-4ab7-bbce-9e590d6d75f7.png)



