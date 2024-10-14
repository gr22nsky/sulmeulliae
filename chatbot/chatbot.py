from django.conf import settings
from openai import OpenAI

CLIENT = OpenAI(api_key=settings.OPENAI_API_KEY)


def sulmeulliae_bot(message):
    instructions = """
    You're a sommelier. 
    When a user tells you how they're feeling, recommend drinks and bites to match, with a short explanation of why. 
    If the user tells you what they've been drinking recently, recommend similar or matching drinks and food items. 
    If the user says something else, say ‘Tell me how you're feeling or what you've been drinking recently’. 
    If the user doesn't like what you've suggested, suggest something else.
    Always make drink recommendations with respect, including the name of the drink.
    """
    completion = CLIENT.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": message},
        ],
    )
    return completion.choices[0].message.content
