# google_asr_action
A ros based client for accessing Google Cloud ASR

A client that listens using the microphone. When an audio threshold is exceeded, starts recording.
Stops recording after 2 seconds of audio BELOW threshold. Saves wav file to directory (currently ~/tmp)
then sends file to Google for transcription. Returns single best transcription 

Requires setup of google cloud services [speech to text api](https://cloud.google.com/speech-to-text/docs/transcribe-api?_ga=2.243821317.-1449793732.1680793602&_gac=1.154223178.1681233786.CjwKCAjwitShBhA6EiwAq3RqA-8mfpXgfgYpUVwKfEOlJC48dyE8_LpCF0IJ5nQ-GQHZYG1bgCKCwRoCPDsQAvD_BwE)
