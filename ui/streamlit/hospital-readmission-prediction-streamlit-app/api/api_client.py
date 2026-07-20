import requests
API_URL="http://127.0.0.1:8000/predict/"
def predict(payload):
    try:
        r=requests.post(API_URL,json=payload,timeout=60)
        return r.json() if r.status_code==200 else {"error":r.text}
    except Exception as e:
        return {"error":str(e)}
