import pyaudio
from vosk import Model, KaldiRecognizer
import json
import time  # Import time module to control output speed


# Load the VOSK model Path
model = Model(r"model/vosk-model-small-en-us-0.15")  # Model pathC:/Users/collins/Desktop/Veegil/Project/VOSK_Voice_to_text/en2
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio
cap = pyaudio.PyAudio()

# Open the audio input stream (ensure you check device availability)
stream = cap.open(format=pyaudio.paInt16, 
                  channels=1, 
                  rate=16000, 
                  input=True, 
                  frames_per_buffer=1024)  # Buffer size

# Start streaming
stream.start_stream()

print("Listening... Press Ctrl+C to stop.")

try:
    last_result = ""  # To store the last result and prevent duplicates

    while True:
        # Read audio data from the microphone
        data = stream.read(1024, exception_on_overflow=False)
        
        # Check if recognizer can process the data
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())  # Parse the result as a dictionary
            text = result.get('text', '')
            
            if text != last_result:  # Only print if the text has changed
                print(text)
                last_result = text  # Update the last result
                
        else:
            partial_result = json.loads(recognizer.PartialResult())  # Get partial results
            partial_text = partial_result.get('partial', '')
            if partial_text != last_result:  # Only print partial results if they differ
                print(partial_text, end='\r')  # Use carriage return to overwrite the line
                last_result = partial_text  # Update the last partial result
        
        #time.sleep(0.1)  # Introduce a small delay between prints to reduce speed

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    # Close the stream and terminate PyAudio when done
    stream.stop_stream()
    stream.close()
    cap.terminate()
