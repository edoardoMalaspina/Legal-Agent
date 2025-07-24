from utils.config import load_api_keys

# Look for Groq API key
load_api_keys()
import json
# Import the submodule acting as API for Normattiva
from law_text_finder import find_law_text
from utils.io import intervention_selection
from llm.extract_chain import extract_law_references
from utils.io import choose_from_list, ask_user_confirmation
from utils.utils import extract_typology_and_date
from agents.explainer_agent import agent_intervention

def main():
    # Dummy fake contract for test purposes
    job_text = ''' L'orario previsto è di 40 ore settimanali dalle 8 alle 5 da lunedì a venerdì.
      è vietato fumare sul luogo di lavoro come previsto dalla legge n. 584 dell'11 novembre 1975.
        In caso di malattia è necessario avvertire il titolare appena possibile e munirsi di certificate.'''
    # Call LLM to extract laws and text referenced
    parsed = extract_law_references(job_text)

    ask_user_confirmation()
    # Chose low and text to be analyzed
    selected_law, selected_text = choose_from_list(parsed)

    # Get information to retrieve the law from Normattiva
    law_category, date = extract_typology_and_date(selected_law)
    # Retrieve full text of the selected law from Normattiva
    law_text = find_law_text(law_category, selected_law, date, date)

    while True:
        # Select which kind of analisys to perform
        selected_intervention = intervention_selection()
        try:
            intervention_index = int(selected_intervention)
            if intervention_index not in range(4):
                print("Enter a number between 0 and 3.")
                continue
            # Invoke the Agent to perform the selected analisys
            agent_intervention(intervention_index, selected_text, law_text)
        except ValueError:
            print("Invalid input.")
            continue
        
        # Check if another analisys is desired
        again = input("\nOther clarification? (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            break

if __name__ == "__main__":
    main()
