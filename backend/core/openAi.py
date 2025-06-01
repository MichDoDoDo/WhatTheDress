from dotenv import load_dotenv
from openai import OpenAI
import os

class AIAssistant ():
    
    def __init__(self):
          pass
    
    def generateOutfit(self, msg):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        client = OpenAI(api_key=api_key)

        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=
        [
            {"role": "system", 
             "content": "You will be given a json string of climate details. in addtion a database with clothing in it please provide to the best of your ability a outfit that would fit the given climate"},
            {
                "role": "user",
                "content": str(msg)
            }
        ]
        )
        print(completion.choices[0].message)
        