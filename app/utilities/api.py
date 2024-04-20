import os
from langchain_openai import OpenAI

from app.utilities.data_processing import output_parser, prompt

import yaml
import random

def load_config(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

def select_random_item(items):
    return random.choice(items)

def generate_scenario(config):
    # Select a random template
    template_name, template = random.choice(list(config['scenario_templates'].items()))
    
    # Prepare data dictionary with random selections for each variable
    data = {
        'age': select_random_item(config['values']['age']),
        'time': select_random_item(config['values']['time']),
        'ethnicity': select_random_item(config['values']['ethnicity']),
        'sex': select_random_item(config['values']['sex']),
        'weekday': select_random_item(config['values']['weekday'])
    }

    # Format the template with the randomly selected data
    scenario = template.format(**data)
    return scenario


def generate_risk_assessment(llm_model):
    config = load_config('app/prompts.yaml')

    sample_scenario = generate_scenario(config)

    # Load YAML configuration
    with open('app/prompts.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Example usage for a detailed scenario
    opening_prompt = config['llm_prompt_templates']['user_prompt']
    
    chain = prompt | llm_model | output_parser

    answer = chain.invoke({"scenario": sample_scenario, "opening_prompt": opening_prompt})
    return answer

