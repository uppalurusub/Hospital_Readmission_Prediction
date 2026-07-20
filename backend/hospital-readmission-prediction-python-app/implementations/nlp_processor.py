import joblib

tfidf = joblib.load("training/model/tfidf.pkl")

def process_text(text):

    vector = tfidf.transform([text])

    return vector.toarray()