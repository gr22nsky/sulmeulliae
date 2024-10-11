import openai 
from django.conf import settings
from openai import OpenAI

CLIENT = OpenAI(api_key=settings.OPENAI_API_KEY)

def summarize_review(review_content):
    response = CLIENT.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", 
            "content": "You are a witty alcohol expert; please summarize the following reviews in Korean, combining the key points from each review to create a cohesive and engaging summary that captures the overall sentiment and highlights of the feedback provided.."},
            {"role": "user", "content": review_content}
        ]
    )
    return response.choices[0].message.content