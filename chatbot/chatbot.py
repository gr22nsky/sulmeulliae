from django.conf import settings
from openai import OpenAI

CLIENT = OpenAI(api_key=settings.OPENAI_API_KEY)


def sulmeulliae_bot(message, liquors):
    instructions = """
You're a sommelier. 
    When a user tells you how they're feeling, recommend liquor and food to match, with a short explanation of why. 
    If the user tells you what they've been drinking or eating recently, recommend similar or matching liquors and food items. 
    If the user says something else, say ‘Tell me how you're feeling or what you've been drinking recently’. 
    When recommending liquors, choose from the following liquors.
    Always make liquors recommendations with respect, including the name of the liquors.
    """+ " ".join(liquors)
    completion = CLIENT.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": message},
        ],
    )
    return completion.choices[0].message.content
