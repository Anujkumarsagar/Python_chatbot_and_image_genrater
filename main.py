#import langchain 
import openai
import requests
import requests
#import PIL
import os
from random import random
#from langchain.llms import (OpenAI,textgen)

#llm = OpenAI(openai_api_key="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")


#while True :

  #string = input("Hi buddy i am your Personal assistant 🤫 .\n for exit just write exit \n")

  #if string == "exit":
    #break

  #print(llm(string))

#<--------basic chatbot--------->


response = openai.Image.create(
  api_key ="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",
  prompt= input("Enter your prompt"),
  n= 2,
  size = "1024x1024"

)
image_url = response['data'][0]['url']

img_data = requests.get(image_url).content

with open(f'image{random()}.jpg', 'wb') as handler:
  handler.write(img_data)
  
  
#print(dir(langchain.llms))

print(image_url)

