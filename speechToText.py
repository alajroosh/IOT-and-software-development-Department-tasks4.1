from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


apikey = 'YOUR API KEY'
url = 'YOUR SERVICE URL'

# Setup Service
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

# Perform conversion
with open('audio-file.flac', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/flac', model='en-US_NarrowbandModel', continuous=True).get_result()

res
text = res['results'][0]['alternatives'][0]['transcript']
text
confidence = res['results'][0]['alternatives'][0]['confidence']
confidence
with open('output.txt', 'w') as out:
    out.writelines(text)