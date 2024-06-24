import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    #print (formatted_response)

    if response.status_code == 200:
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        emotion['max_emotion'] = max(emotion.items(), key=lambda x : x[1])
        return emotion
    if response.status_code == 400:
        noemotion = {'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None,
            'max_emotion': None}
        return noemotion
    else:
        return None
