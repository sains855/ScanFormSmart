import re

def extract_form_fields(text):
    fields = {}

    patterns = {
        "Nama": r"Nama\s*[:\-]?\s*(.*)",
        "Alamat": r"Alamat\s*[:\-]?\s*(.*)",
        "No HP": r"(No HP|HP|Telp)\s*[:\-]?\s*(.*)",
        "Tanggal Lahir": r"(Tanggal Lahir|TTL)\s*[:\-]?\s*(.*)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            fields[key] = match.group(match.lastindex)
        else:
            fields[key] = ""

    return fields
