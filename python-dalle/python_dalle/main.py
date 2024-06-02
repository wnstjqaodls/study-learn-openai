import openai
import os

# Your DALL-E API key
# Load the API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# The text prompt you want to use to generate an image
prompt = "High quality photo of a jindo astronaut"

# Generate an image
response = openai.Image.create(
    prompt=prompt, # text prompt used to generate the image
    model="image-alpha-001", # DALL-E model to use for image generation.
    size="1024x1024",
    response_format="url"
)

# Print the URL of the generated image
print(response["data"][0]["url"])
