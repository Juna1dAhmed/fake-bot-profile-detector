from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
import pandas as pd
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables (for Twitter API key)
load_dotenv()
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

app = FastAPI()

# Load your trained model
model = tf.keras.models.load_model("my_fake_bot_detector_95.h5")

# Input schema
class TwitterHandle(BaseModel):
    username: str

# Feature extractor
def extract_features_from_twitter(username: str):
    headers = {
        "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"
    }
    url = f"https://api.twitter.com/2/users/by/username/{username}?user.fields=created_at,public_metrics,verified,description"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Twitter API error: {response.status_code} {response.text}")

    user_data = response.json()["data"]
    metrics = user_data["public_metrics"]

    created_at = pd.to_datetime(user_data["created_at"])
    account_age_days = (pd.Timestamp.now() - created_at).days

    # Construct input features (ensure it matches training features order)
    features = {
        "followers_count": metrics["followers_count"],
        "following_count": metrics["following_count"],
        "tweet_count": metrics["tweet_count"],
        "listed_count": metrics["listed_count"],
        "verified": int(user_data["verified"]),
        "description_length": len(user_data.get("description", "")),
        "account_age_days": account_age_days
    }

    return features

@app.post("/predict")
async def predict(twitter: TwitterHandle):
    try:
        features = extract_features_from_twitter(twitter.username)

        input_array = np.array([list(features.values())])

        prediction = model.predict(input_array)
        result = int(np.argmax(prediction))

        return {
            "username": twitter.username,
            "features_used": features,
            "prediction": result  # 0 = Real, 1 = Fake, 2 = Bot (for example)
        }

    except Exception as e:
        return {"error": str(e)}