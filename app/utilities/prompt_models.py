



prompt = PromptTemplate(
    template="{opening_prompt}\n Scenario: \n {scenario}",
    input_variables=["opening_prompt", "scenario"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)