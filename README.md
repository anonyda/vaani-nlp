# Vaani - The Doctor's Intelligent Assistant

## This repo contains a .ipynb notebook that trains an **NLP Model in Spacy** for Vaani.

> Vaani is a mobile app for Doctors, that can understand statements spoken by the doctors, structure and tag the important terms and convert it into a digital prescription that can be sent to the patient.

This model is trained using a custom dataset of around 250 sentences, using **Named Entity Recognition** in Spacy.
It can recognise the following from sentences:
- Symptoms
- Disease
- Medicine Name
- Duration (for which the medicine is to be taken)
- Interval (how many times a day a certain medicine is to be taken)

This model was deployed as Flask Application. RESTFul API written in Python and deployed on Heroku.
