import openai
import os

def oa(text):
  openai.api_key=os.environ['oakey']
  response = openai.Completion.create(
    model="text-davinci-002",
    #model="text-ada-001",
    #prompt="Say this is a test",
    prompt=text,
    max_tokens=25,
    #temperature=1,
    #top_p=1,
    #n=1,
    #stream=False,
    #stop="\n",
    #frequency_penalty=2.0
  )
  print(response)
  return response

oa("whatsup?")
