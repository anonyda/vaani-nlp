from flask import Flask, abort
from flask import request
import spacy
import json

app = Flask(__name__)
nlp = spacy.load('D:/Solve4Bharat/Spacy Model/Solve4Bharat')
input = nlp("He has high fever take crocin for three days twice a day")

@app.route('/model', methods=['POST', 'GET'])
def model():
    if not request.json or not 'pres_str' in request.json:
        abort(422, 'Missing Parameters')
    str = request.json.get('pres_str')
    conversion = nlp(str)
    res = model_predict(conversion)
    return res

def model_predict(conversion):
    predict_symp = []
    predict_diag = []
    predict_med = []
    predict_int = []
    predict_dur = []
    temp_dur = []
    temp_int = []
    for ent in conversion.ents:
        if ent.label_ == 'DURATION':
            temp_dur.append(ent.text)

        if ent.label_ == 'INTERVAL':
            temp_int.append(ent.text)

    print("Temp interval array",temp_int)
    print("Temp Duratin array",temp_dur)
    for ent in conversion.ents:
        if ent.label_ == 'SYMPTOM':
            predict_symp.append(ent.text)
        
        if ent.label_ == 'DIAGNOSIS':
            predict_diag.append(ent.text)

        if ent.label_ == 'MEDNAME':
            predict_med.append(ent.text)

        if ent.label_ == 'INTERVAL':
            predict_int.append(ent.text)

        if ent.label_ == 'DURATION':
            predict_dur.append(ent.text)

        if ent.label_ == 'BEFAF':
            predict_befaf.append(ent.text)

    
    tempmed = []
    #for medicine in predict_med:
    if len(predict_med) == len(predict_int):
        for i in range(len(predict_med)):
            if(len(predict_dur)!=0):
                tempmed.append(
                        {
                        "name": predict_med[i],
                        "interval": predict_int[i],
                        "duration": predict_dur[0]
                        }
                )
            else:
                tempmed.append(
                        {
                        "name": predict_med[i],
                        "interval": predict_int[i],
                        "duration": " "
                        }
                )   

    if len(predict_med) > len(predict_int):
        for i in range(len(predict_med)-1):
            if(len(predict_dur)!=0):
                tempmed.append(
                        {
                        "name": predict_med[i],
                        "interval": predict_int[i],
                        "duration": predict_dur[0]
                        }
                )
            else:
                tempmed.append(
                        {
                        "name": predict_med[i],
                        "interval": predict_int[i],
                        "duration": " "
                        }
                )

        if(len(predict_dur)!=0):
                tempmed.append(
                        {
                        "name": predict_med[i+1],
                        "interval": predict_int[i],
                        "duration": predict_dur[0]
                        }
                )
        else:
            tempmed.append(
                    {
                        "name": predict_med[i+1],
                        "interval": predict_int[i],
                        "duration": " "
                        }
                )
    pres = {
            "symptoms": predict_symp,
            "diagnosis": predict_diag,
            "medicine": tempmed
        }
    #return json.dumps([{"symptoms":predict_symp, "diagnosis":predict_diag, "medicines":["name":predict_med[]]}])
    return json.dumps(pres)


    
if __name__ == '__main__':
    app.run(debug=True)


