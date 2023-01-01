import pandas as pd
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from transformers import pipeline

#Data
data =pd.read_csv('records.csv')
data=data.dropna(subset=['V4'])

#Sepration of groups
group1= data.loc[data['FormType'] ==1]
group2= data.loc[data['FormType'] ==2]
group3= data.loc[data['FormType'] ==3]
group1 = group1.reset_index(drop=True)
group2 = group2.reset_index(drop=True)
group3 = group3.reset_index(drop=True)

#Sentiment analysis tool setup
model_name = "DTAI-KULeuven/robbert-v2-dutch-sentiment"
model = RobertaForSequenceClassification.from_pretrained(model_name)
tokenizer = RobertaTokenizer.from_pretrained(model_name, model_max_length=512)
classifier = pipeline('sentiment-analysis', model=model, tokenizer = tokenizer)

#Calculations
countn1=0
countp1=0
for i in range(0,len(group1)):
    #print(classifier(group1.loc[i,'V4']))
    if classifier(group1.loc[i,'V4'])[0]['label'] == "Positive":
        countp1 +=1

    else:
        countn1 +=1

print('Formtype 1')
print("Aantal Positief", countp1)
print("Aantal Negatief", countn1)
print('\n')

countn2=0
countp2=0
for i in range(0,len(group2)):
    #print(classifier(group2.loc[i,'V4']))
    if classifier(group2.loc[i,'V4'])[0]['label'] == "Positive":
        countp2 +=1
    else:
        countn2 +=1
print('Formtype 2')
print("Aantal Positief", countp2)
print("Aantal Negatief", countn2)
print('\n')

countn3=0
countp3=0
for i in range(0,len(group3)):
    #print(classifier(group3.loc[i,'V4']))
    if classifier(group3.loc[i,'V4'])[0]['label'] == "Positive":
        countp3 +=1

    else:
        countn3 +=1
print('Formtype 3')
print("Aantal Positief", countp3)
print("Aantal Negatief", countn3)