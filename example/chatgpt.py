import os
import openai
import argparse
from dotenv import load_dotenv

class OpenAIGpt:
  def __init__(self):
    load_dotenv()    

  def run(self):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    text = "Hello. nice to meet you"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant that translates English to Korean."},
                {"role": "user", "content": f'Translate the following English text to Korean: "{text}"'}
            ]
        )
    
    print(completion)
    print(completion['choices'][0]['message']['content'])


if __name__ == '__main__':
  openai_gpt = OpenAIGpt()
  openai_gpt.run()
