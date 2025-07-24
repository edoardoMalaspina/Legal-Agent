from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from llm.llm_client import llm

# Parser for extracting laws and referenced text
parser = JsonOutputParser(pydantic_object={
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "law": {"type": "string", "description": "The name or reference of the law (e.g., GDPR, Civil Code §1234)"},
            "text_snippet": {"type": "string", "description": "The portion of the contract text that refers to the law"}
        },
        "required": ["law", "text_snippet"]
    }
})

("system", """You are a legal assistant. Analyze the following contract and extract all referenced laws, regulations, or legal codes.

Return ONLY a JSON array (no preamble, no explanation), like this:
[
  {{
    "law": "GDPR",
    "text_snippet": "In accordance with the GDPR, personal data must be processed lawfully..."
  }},
  ...
]

Strictly return only the JSON array.
""")


# Template to analyze contracts
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a legal assistant. Analyze the following contract and extract a list of all laws, regulations, or legal codes that are referenced in it.

For each law return ONLY a JSON array (no preamble, no explanation), like this:
1. The name or citation of the law (e.g., 'GDPR', 'Section 230', 'Civil Code §1234').
2. The full sentence or clause from the contract that refers to it.
Be carefull, the text_snippet has to be a relevant context with respect to te law, better to put more text than less 

Return your result as a JSON array in this format:
[
  {{
    "law": "GDPR",
    "text_snippet": "In accordance with the GDPR, personal data must be processed lawfully..."
  }},
  ...
]"""),
    ("user", "{input}")
])


# Chain definition
chain = prompt | llm | parser


def extract_law_references(contract_text: str) -> list[dict]:
    return chain.invoke({"input": contract_text})
