# Legal-Agent
**Analysis of italian contract and cited laws exploiting Normattiva online databases, with Agent to perform different kind of explanations.**

Input your contract, an LLM will analyze it and will identify all the times a law is cited and which part of the text is concerned. 
Once the law has been identified the Normattiva online database is consulter using Normattiva-Law-Retriever to access the full text of the law.
If you want to have more explanations about the law and how is applied in your contract an Agent, able to analyze different aspects is invoked as prompts you to choose in what kind of explanation you are interested among: Extract legal concepts, Detect contradictions, Assess legal risk and Validate law citation.


## **To set up:**
Clone this repository:
```bash
git clone https://github.com/edoardoMalaspina/Legal-Agent.git
```

Clone the subpackage Normattiva-Law-Retriever:
```bash
git clone https://github.com/edoardoMalaspina/Normattiva-Law-Retriever.git
```

Create a virtual environment
```bash
python -m venv env_la
```

Activate the virtual environment:

In Windows:
```bash
.\env_la\Scripts\activate
```

In Ubuntu:
```bash
source env_la/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

To install the subpackage run:
```bash
cd Normattiva-Law-Retriever
pip install -e .
cd ..
```

## **Demo**
To test your setup with a dummy contract simply run:
```bash
python tests/demo.py
```

The project structure, after the setup, should be as follow:
```bash
Legal-Agent
│
├─── Normattiva-Law-Retriever/
│
├─── agents
│      ├─ explainer_agent.py
│      ├─ tools.py
│      └─ __init__.py
│
├─── llm
│      ├─ extract_chain.py
│      ├─ llm_client.py
│      └─ __init__.py
│
├─── tests
│      └─ demo.py
│
├─── utils
│      ├─ config.py
│      ├─ io.py
│      └─ utils.py
│
├── main.py
├── .gitignore
├── README.md
├── env_la/
└── requirements.txt
```