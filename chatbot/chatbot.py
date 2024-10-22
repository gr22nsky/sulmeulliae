from django.conf import settings
from openai import OpenAI

CLIENT = OpenAI(api_key=settings.OPENAI_API_KEY)


def sulmeulliae_bot(message, liquors):
    instructions = """
You are a sommelier. 
When users talk about their feelings, emotions, and emotions, they recommend drinks and foods that go well with a short explanation. 
We recommend similar alcoholic beverages and foods when users talk about their recent drinks or moods, feelings, or emotions. 
If the user doesn't talk about the alcohol, mood, feeling, or emotion he recently drank, he says, "Tell me how you feel and what drink you recently drank." 
When recommending liquors, we recommend one of each of the following types of alcohol: soju, beer, wine, and whiskey.
If the names of soju, beer, wine or whiskey are not on the list, recommend it without it
When recommending alcoholic beverages, always use a polite, gentle tone and include the names of liquors.
    """+ " ".join(liquors)
    completion = CLIENT.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": message},
        ],
    )
    return completion.choices[0].message.content
