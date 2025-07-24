import re

TYPOLOGIES = {
    "COSTITUZIONE",
    "DECRETO",
    "DECRETO-LEGGE",
    "DELIBERAZIONE",
    "ORDINANZA",
    "LEGGE",
    "REGOLAMENTO",
    "LEGGE COSTITUIONALE",
    "REGIO DECRETO"
}

MONTHS = {
    "gennaio": "01",
    "febbraio": "02",
    "marzo": "03",
    "aprile": "04",
    "maggio": "05",
    "giugno": "06",
    "luglio": "07",
    "agosto": "08",
    "settembre": "09",
    "ottobre": "10",
    "novembre": "11",
    "dicembre": "12"
}

def extract_typology_and_date(reference: str):
    reference_upper = reference.upper()
    reference_lower = reference.lower()

    # Extract typology
    typology = next((typ for typ in TYPOLOGIES if reference_upper.startswith(typ)), None)

    # Extract date components
    date_match = re.search(r"(\d{1,2})\s+(\w+)\s+(\d{4})", reference_lower)
    if date_match:
        day, month_text, year = date_match.groups()
        month = MONTHS.get(month_text)
        if month:
            date = f"{year}-{month}-{int(day):02d}"
        else:
            date = None
    else:
        date = None

    return typology, date
