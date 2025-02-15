# Speech-to-Text using VOSK and PyAudio

This project demonstrates real-time speech-to-text conversion using VOSK adapted to Nigerian Language and PyAudio. It listens to the microphone input, processes it using a VOSK model, and outputs the recognized speech as text in real-time.

## Requirements

- Python 3.x
- `pyaudio` for microphone access
- `vosk` for speech recognition
- `json` for parsing recognition results

Install dependencies using:

```bash
pip install pyaudio vosk
```
## Setup
1.	Download VOSK Model: Download a pre-trained VOSK model from the [VOSK website](https://alphacephei.com/vosk/adaptation). Choose a model based on size and language preference.
2.	Configure Model Path: After downloading, extract the model and provide the path to it in the script:
3.	model = Model(r"Model_Path")  # Provide correct path to your model
## Usage
1.	Connect a Microphone: Ensure your microphone is connected to your system.
2.	Run the Script: Execute the script in the terminal or an IDE to start the speech-to-text process.
`Example:`
```
python speech_to_text.py
```
The script will continuously listen to your microphone and print recognized text. Press Ctrl+C to stop the program.
To customize VOSK for Nigerian English, we train a custom model using our dataset.

`Notes:`
-	Buffer Size: The buffer size is set to 8192, which can be adjusted based on system performance.
-	Partial Results: The script provides partial recognition results as it processes audio.
-	Performance: A small delay of 0.1 seconds is introduced between outputs to control display speed.
---
## Training a VOSK Model for Nigerian Voice
### Steps to Train a VOSK Model:
1.	Collect Data: 
Gather a large dataset of recorded speech in the Nigerian accent, with transcriptions for each recording. The dataset should include a wide range of speakers for better accuracy. A minimun of 10,000 hours of talk time is required if possible as instructed by Vosk support group on Telegam called speech_recognition 
2.	Prepare the Data:
-	Convert audio files to WAV format with a 16 kHz sampling rate.
-	Create transcription files for each audio recording. Each file should match the speech content in the corresponding audio.
3.	Preprocess the Data:
-	Split the data into training (typically 80%) and validation (typically 20%) sets.
-	Convert the audio files into the feature format required by VOSK. This step usually involves extracting Mel-frequency cepstral coefficients (MFCCs) or similar audio features.
4.	Train the Acoustic Model: 
VOSK uses the Kaldi toolkit to train the acoustic model. This involves feeding the training data (audio and transcription pairs) into Kaldi for model training.
-	Install the Kaldi toolkit.
-	Follow the VOSK training guide for step-by-step instructions on setting up the training pipeline.
5.	Train a Language Model: 
The language model helps the system predict the sequence of words. You can use Nigerian English text, such as transcripts from Nigerian news broadcasts, podcasts, and other media.
-	Collect a large corpus of text to train the language model.
-	Use the text to build the model using the KenLM tool or another appropriate language modeling tool.
6.	Finetune the Model: 
Once the acoustic and language models are trained, fine-tune the VOSK model by testing it on a separate test set. Adjust model parameters, such as the learning rate or the number of training iterations, based on the test results.
-	Evaluate the accuracy of the model on your validation dataset.
-	Refine the model and iterate until you reach satisfactory accuracy.
7.	Integrate the Custom Model: After training and finetuning, export the trained model and replace the pre-trained model in the script with your custom-trained model:
```
model = Model(r"Custom_Model_Path")  # Path to your trained mọdèl
```
License
This project is licensed under the MIT License. See the LICENSE file for details.

