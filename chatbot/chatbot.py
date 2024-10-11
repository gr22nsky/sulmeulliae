from django.conf import settings
from openai import OpenAI

CLIENT = OpenAI(api_key=settings.OPENAI_API_KEY)


def sulmeulliae_bot(message):
    instructions = """
    너는 소믈리에야. 
    사용자가 기분을 말하면 그에 맞는 술과 안주를 추천하고, 이유와 간단한 설명을 해. 
    사용자가 최근에 마신 술이나 안주를 말하면 비슷하거나 어울리는 술과 안주를 추천해. 
    이 외의 말을 하면 "기분이나 최근에 마신 술을 알려주세요"라고 말해. 
    만약 추천한 술을 사용자가 마음에 들지 않아 하면 다른 술을 추천해.
    항상 술 이름을 포함해서 존댓말로 술을 추천해.
    """
    completion = CLIENT.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": message},
        ],
    )
    return completion.choices[0].message.content
