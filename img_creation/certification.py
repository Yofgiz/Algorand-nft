import openai
import os

openai.api_key = open("secret_key.txt", "r").read()

response = openai.images.generate(
  #model="dall-e-3",
  prompt="Generate a beautiful certificate background with an elegant design and a border and with no text",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)