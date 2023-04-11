from google.cloud import speech
import io

def transcribe_file(speech_file):
    """Transcribe the given audio file."""


    client = speech.SpeechClient()
    data = "ERROR"

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        #print("Transcript: {}".format(result.alternatives[0].transcript))
        data = str(result.alternatives[0].transcript)
    return(data)

#transcribe_file('/home/nick/catkin_ws/src/simple_dm/src/Records/1.wav')