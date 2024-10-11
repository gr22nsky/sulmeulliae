from openai import OpenAI
# from  import OPENAI_API_KEY

client = OpenAI()
    # api_key=OPENAI_API_KEY,

system_instructions = ""
# 챗지피 입력 내용 
# 예)이제부터 너는 술을 추천해주는 전문가야


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_instructions},
        
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming." 
            #유저가 입력하는 내용 
        }
    ]
)

print(completion.choices[0].message.content)