"""Check that the LLM client works: send "Hello!" and print the reply."""

from llm import get_client, get_model, get_provider

client = get_client()

# messages is the list of conversation messages; for now just one, from the user.
response = client.chat.completions.create(
    model=get_model(),
    messages=[{"role": "user", "content": "Hello! Reply with one short sentence."}],
)

print(f"Provider: {get_provider()} | model: {get_model()}")
# The API can return several replies (choices); we ask for one and take the first.
print(response.choices[0].message.content)
