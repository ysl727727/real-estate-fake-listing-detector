from openai import OpenAI
import getpass
import json
import config

questions = json.load(open("prompts/questions.json", encoding="utf-8"))
target = None
for q in questions:
    if q["id"] == "Q06":
        target = q

client = OpenAI(api_key=getpass.getpass("key: "))
response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[
        {"role": "system", "content": config.SYSTEM_PROMPT},
        {"role": "user", "content": config.build_user_message(target)},
    ],
    temperature=1,
    seed=42,
    max_completion_tokens=1024,
)

usage = response.usage
content = response.choices[0].message.content or ""

print("details 객체 :", usage.completion_tokens_details)
print("finish_reason:", response.choices[0].finish_reason)
print("completion   :", usage.completion_tokens)
print("content 길이 :", len(content), "자")