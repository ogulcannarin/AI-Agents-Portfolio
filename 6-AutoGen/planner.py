import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")


def plan(goal, history):

    prompt = f"""
You are an autonomous AI agent.

Goal:
{goal}

Memory of previous steps:
{history}

Decide the next best action.
If information is missing you can say SEARCH.
"""

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content