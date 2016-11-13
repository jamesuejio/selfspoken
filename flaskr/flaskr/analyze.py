import json
import time
import cPickle
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    username="4411cbd2-1327-4c3a-95ff-afccc0893be3",
    password="VsuIl7mgSJ0y",
    version='2016-02-11')

'''
 * analyze(text) processes the user input and outputs a json object of the
 *  user's mental state.
 * @param text string input of the user's thoughts
 * @returns updated json object of user's mental state
 '''
def analyze(text):
    date = time.asctime( time.localtime(time.time()) )
    tone_analyzer_payload = tone_analyzer.tone(text=text)
    tones_payload = tone_analyzer_payload["document_tone"]["tone_categories"] \
        [0]["tones"]
    return (date, tones_payload)

def all_time_tone_analysis(data):
    datadict = []
    for row in data:
        text = row['text']
        time = row['time']
        tones = cPickle.loads(str(row["tones"]))
        datadict.append({"date": time, "text": text, "tones": tones})
    return datadict

def retrieveEmotionData(entries):
    data = {}
    for row in entries:
        text = row['text']
        time = row['time']
        tones = cPickle.loads(str(row["tones"]))
        data[time] = {"text": text, "tones": tones}
    return data

def averageEmotionValues(data):
    angerTotal = 0
    disgustTotal = 0
    fearTotal = 0
    joyTotal = 0
    sadnessTotal = 0
    for time in data:
        toneDicts = data[time]["tones"]
        for toneDict in toneDicts:
            if toneDict["tone_id"] == "anger":
                angerTotal += toneDict["score"]
            if toneDict["tone_id"] == "disgust":
                disgustTotal += toneDict["score"]
            if toneDict["tone_id"] == "fear":
                fearTotal += toneDict["score"]
            if toneDict["tone_id"] == "joy":
                joyTotal += toneDict["score"]
            if toneDict["tone_id"] == "sadness":
                sadnessTotal += toneDict["score"]
    emotionValues = {"Anger": angerTotal, "Disgust": disgustTotal, "Fear": fearTotal, "Joy": joyTotal, "Sadness": sadnessTotal}
    for emotion in emotionValues:
        emotionValues[emotion] /= (len(data) or 1)
    return emotionValues
