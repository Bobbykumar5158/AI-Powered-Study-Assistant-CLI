from google import genai
from google.genai import types
from google.genai.errors import APIError
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("API Key not found!")


SYSTEM_PROMPT = """
You are an elite, highly concise Academic Strategy Coach. Your sole purpose is to help students break down complex topics into clear, actionable study roadmaps. 

When the user provides a topic, you must output a structured study plan adhering strictly to the following formatting rules:
1. Use Markdown headers for the main sections.
2. Provide a list of essential subtopics arranged in a logical, recommended learning order.
3. For each subtopic, provide description explaining what it is.
4. Provide plan in very structural way just not a single paragraph containing all the context.

OUTPUT FORMAT:
(Topic Name):
~ Subtopic : 
    Discription
~(All the subtopic like this)
GIVE ONE LINE SPACING BEFORE THE NEXT SUBTOPIC

Roadmap :
~ All the topics piority wise and where to study in 1 line.
~ How much min time we have to give for particular topics

CRITICAL CONSTRAINTS (DO NOT VIOLATE):
- DO NOT write any introductory or concluding pleasantries (e.g., do not say "Sure, here is your plan" or "Good luck with your studies!"). Start directly with the structured plan.
- DO NOT exceed 150 words total for the entire initial response.
- DO NOT give continuous line or paragraph in output. 
- If the provided text from user doesn't related to any topic to be studied tell your roll what you do in 1-2 line.

DYNAMIC INTERACTION RULES FOR FOLLOW-UP QUESTIONS:
1. After presenting the initial plan, switch to a supportive conversational mode. 
2. You must ONLY answer follow-up questions that are directly related to the specific subtopics listed in the active roadmap. 
3. For valid follow-up questions, answer briefly in simple, easily understandable language, strictly adhering to a maximum limit of 150 words.
4. If the user asks a question about a completely different topic that is NOT on the current roadmap, treat it as a brand-new topic request. Wipe the previous context, immediately generate a brand-new structured roadmap for that new topic following the exact rules above, and strictly adhere to the 150-word constraint and zero-pleasantries rule.
5. Ans in pointer NOT paragraphs.

Summary prompt: #(use this only when i asked you for summary)
-List all the topics studied.
-Basics summary about them.
TOTAL QUES ASKED : (number of question asked by user)

"""
print("="*80)
print(f"{' AI-Powered-Study-Assistant-CLI ':*^80}")
print("="*80)


client = genai.Client(api_key = API_KEY)
chat = client.chats.create(model="gemini-2.5-flash",
                           config=types.GenerateContentConfig(system_instruction= SYSTEM_PROMPT))


user = input("User (type 'exit' or 'quit' to and chat) : ").strip()

while not (user.lower() in ["exit","quit"]):
    try:
        response = chat.send_message(user)
        print(response.text)
        print("\n","="*80)
      
    except APIError as e:
        # print("During the process the following error has occured.\n",e)
        print(f"Caught a API Error!")
        print(f"  - Status Code: {e.code}")
        print(f"  - Message: {e.message}")

    user = input("\n User (type 'exit' or 'quit' to end chat) : ").strip()
    print()

print("="*80)

try :
    print(chat.send_message("Summary").text)
except APIError as e:
    print("During Summary generation the following error is occured.",)
    print(f"Caught a API Error!")
    print(f"  - Status Code: {e.code}")
    print(f"  - Message: {e.message}")

print("="*80)
print(f'{" Thank You for Using our AI assistant. ":*^80}')
print("="*80)