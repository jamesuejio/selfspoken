import json
from watson_developer_cloud import ToneAnalyzerV3


tone_analyzer = ToneAnalyzerV3(
    username="4411cbd2-1327-4c3a-95ff-afccc0893be3",
    password="VsuIl7mgSJ0y",
    version='2016-02-11')

tonedict = tone_analyzer.tone(text='I am worried about the US.')["document_tone"]["tone_categories"][0]["tones"]
for tone in tonedict:
	if tone["tone_name"] == "Anger":
		anger = tone["score"]
		print("anger: " + str(anger))
	if tone["tone_name"] == "Disgust":
		disgust = tone["score"]
		print("disgust: " + str(disgust))
	if tone["tone_name"] == "Fear":
		fear = tone["score"] 
		print("fear: " + str(fear))
	if tone["tone_name"] == "Joy":
		joy = tone["score"] 
		print("joy: " + str(joy))
	if tone["tone_name"] == "Sadness":
		sadness = tone["score"] 
		print("sadness: " + str(sadness))
