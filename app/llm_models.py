from langchain_openai import ChatOpenAI
import os
from langchain_openai import OpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


# import .env file
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.environ.get("OPENAI_KEY")
anthropic_api_key = os.environ.get("ANTHROPIC_KEY")


chat_openai = ChatOpenAI(temperature=0, api_key=openai_api_key).bind(logprobs=True)

chat_anthropic_opus = ChatAnthropic(temperature=0, api_key=anthropic_api_key, model_name="claude-3-opus-20240229")

chat_groq_mixtral = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")