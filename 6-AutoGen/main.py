from agent import AutoAgent
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

goal = "Türkiye'deki en iyi AI startup'ları araştır"

agent = AutoAgent(goal)

result = agent.run()

print(result)