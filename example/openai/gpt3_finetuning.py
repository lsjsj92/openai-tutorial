import os
import openai
import argparse
from dotenv import load_dotenv


class OpenAIGpt:
  def __init__(self):
    load_dotenv()    

  def run(self, args):
    question = input("Question : ")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
      #model="text-davinci-003",
      model="davinci:ft-wjtb-2023-01-29-10-42-22",
      prompt=f"{question}",
      temperature=args.temperature,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      stop=["\n"]
      #stop=None
    )
    #print(response)
    print(response.choices[0].text.strip())


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  # python gpt3.py --temperature 0.3
  parser.add_argument('--temperature', default=0.3)

  args = parser.parse_args()
  openai_gpt = OpenAIGpt()
  openai_gpt.run(args)

