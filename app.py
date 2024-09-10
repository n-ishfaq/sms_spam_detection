import streamlit as slt
import pickle
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.data.path.append('C:/Users/r tech/AppData/Roaming/nltk_data')
slt.markdown(
    """
    <style> 
    .sltTextInput > div > div > input {
    width: 100px;
    height: 100px:
    margin-top:100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
model=pickle.load(open('model.pkl','rb'))
vectorizer=pickle.load(open('vectorizer.pkl','rb'))



slt.title("Sms Spam Detection")

input_msg=slt.text_input("Enter the message")

from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
from nltk.corpus import stopwords
import string


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)




if input_msg:

  transformed_text=transform_text(input_msg)

  vect=vectorizer.transform([transformed_text])

  detection=model.predict(vect)[0]

  if detection ==1 :
    slt.header("Spam")
  else:
    slt.header("Not Spam")



