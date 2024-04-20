# import .env file
from dotenv import load_dotenv
load_dotenv()

from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


import yaml

from typing import List

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

from app.models import RiskAssessment

parser = JsonOutputParser(pydantic_object=RiskAssessment)


prompt = PromptTemplate(
    template="{opening_prompt}\n Scenario: \n {scenario}",
    input_variables=["opening_prompt", "scenario"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
