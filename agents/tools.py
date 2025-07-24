from langchain.tools import Tool
from llm.llm_client import llm

# Extract legal concepts from a law
def extract_legal_concepts(text: str) -> str:
    prompt = (
        f"Extract the key legal concepts, obligations, or entities from the following text:\n\n{text}\n\n"
        "List them as bullet points."
    )
    response = llm.invoke(prompt)
    return response.content.strip()

extract_legal_concepts_tool = Tool(
    name="ExtractLegalConcepts",
    func=extract_legal_concepts,
    description="Extract key legal concepts, obligations, and entities from a contract or legal text."
)

# Detect contradictions in a law
def detect_contradictions(contract_excerpt_and_law_text: str) -> str:
    prompt = (
        "Analyze the following two texts and determine if there are contradictions or inconsistencies.\n\n"
        f"Contract excerpt and law text are: \n{contract_excerpt_and_law_text}\n\nExplain your reasoning."
    )
    response = llm.invoke(prompt)
    return response.content.strip()

detect_contradictions_tool = Tool(
    name="DetectContradictions",
    func=detect_contradictions,
    description="Detect contradictions or inconsistencies between a contract excerpt and a cited law."
)

# Assess legal risks of a law
def assess_legal_risk(contract_excerpt_and_law_text: str) -> str:
    prompt = (
        "Based on the contract excerpt and cited law, assess potential legal risks or liabilities.\n\n"
        f"Contract excerpt and law text are: \n{contract_excerpt_and_law_text}"
    )
    response = llm.invoke(prompt)
    return response.content.strip()

assess_legal_risk_tool = Tool(
    name="AssessLegalRisk",
    func=assess_legal_risk,
    description="Assess possible legal risks or liabilities based on the contract and the cited law."
)

# Validate law citation
def validate_law_citation(contract_excerpt_and_law_text: str) -> str:
    prompt = (
        "Verify if the contract excerpt correctly cites and represents the law text.\n\n"
        f"Contract excerpt and law text are: \n{contract_excerpt_and_law_text}\n\n"
        "Point out any discrepancies or errors."
    )
    response = llm.invoke(prompt)
    return response.content.strip()

validate_law_citation_tool = Tool(
    name="ValidateLawCitation",
    func=validate_law_citation,
    description="Check whether a contract clause correctly cites and reflects the referenced law."
)

# Export the tools
TOOLS = [
    extract_legal_concepts_tool,
    detect_contradictions_tool,
    assess_legal_risk_tool,
    validate_law_citation_tool
]
