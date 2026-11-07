"""Lesson 1.2: the same prompt at different temperatures."""

from llm import get_client, get_model

client = get_client()

# An open-ended question, so the effect of temperature is easy to see.
messages = [
    {"role": "system", "content": "Reply with the name only, nothing else."},
    {"role": "user", "content": "Suggest a name for a small architecture office."},
]

# Two runs per temperature: the interesting part is whether the runs differ.
for temperature in [0.0, 1.0, 2.0]:
    print(f"temperature={temperature}")
    for run in range(1, 3):
        response = client.chat.completions.create(
            model=get_model(),
            messages=messages,
            temperature=temperature,
        )
        print(f"  run {run}: {response.choices[0].message.content.strip()}")
