"""Lesson 1: a basic call with a system and a user message, plus token usage."""

from llm import get_client, get_model

client = get_client()

# The system message sets the rules for the whole conversation.
# The user message is the actual question.
messages = [
    {
        "role": "system",
        "content": (
            "You are an assistant at an architecture and structural engineering "
            "office. Answer in at most two sentences, in plain language."
        ),
    },
    {"role": "user", "content": "What is a load-bearing wall?"},
]

response = client.chat.completions.create(model=get_model(), messages=messages)

print("Answer:")
print(response.choices[0].message.content)

# Usage is what we pay for and what counts against rate limits.
usage = response.usage
print()
print(f"Input tokens:  {usage.prompt_tokens}")
print(f"Output tokens: {usage.completion_tokens}")
print(f"Total tokens:  {usage.total_tokens}")
