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
    all_time_tones = {}
    for row in data:
        text = row['text']
        time = row['time']
        tones = cPickle.loads(str(row["tones"]))
        all_time_tones[time] = {"text": text, "tones": tones}
    # print all_time_tones
    # return json.dump(all_time_tones)

def line_graph(data):
    datadict = []
    for row in data:
        text = row['text']
        time = row['time']
        tones = cPickle.loads(str(row["tones"]))
        print tones[0]
        datadict.append({"date": time, "close": tones[0]['score']})
    return datadict
