from langchain.agents import initialize_agent, AgentType

from llm.llm_client import llm
from agents.tools import TOOLS

# Initialize the agent with tools and LLM
agent = initialize_agent(
    tools=TOOLS,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


# Method to invoke agent with a different behaviour based on the type of
# intervention chosen by the user
def agent_intervention(intervention_type, contract_excerpt, law_text):
    if intervention_type == 0:
        response = agent.run(f"extract_legal_concepts: {contract_excerpt}")
        print("\nExtract Legal Concepts:\n", response)
    if intervention_type == 1:
        response = agent.run(f"detect_contradictions: contract_excerpt={contract_excerpt}; law_text={law_text}")
        print("\nDetect Contradictions:\n", response)
    if intervention_type == 2:
        response = agent.run(f"assess_legal_risk: contract_excerpt={contract_excerpt}; law_text={law_text}")
        print("\nAssess Legal Risk:\n", response)
    if intervention_type == 3:
        response = agent.run(f"validate_law_citation: contract_excerpt={contract_excerpt}; law_text={law_text}")
        print("\nValidate Law Citation:\n", response)