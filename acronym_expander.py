import re

# Dictionary of acronyms and their full forms
acronyms = {
    "NASA": "National Aeronautics and Space Administration",
    "FBI": "Federal Bureau of Investigation",
    "CIA": "Central Intelligence Agency",
    "UN": "United Nations",
    "WHO": "World Health Organization"
}

def read_document(file_path):
    """Read the contents of a document."""
    with open(file_path, 'r') as file:
        return file.read()

def expand_acronyms(text):
    """Find and replace acronyms in the text."""
    def replace(match):
        acronym = match.group(0)
        return acronyms.get(acronym, acronym)

    # Regular expression to match strings of two or more capital letters
    pattern = r'\b[A-Z]{2,}\b'
    return re.sub(pattern, replace, text)

def main():
    input_file = "input_document.txt"
    output_file = "output_document.txt"

    # Read the input document
    document_text = read_document(input_file)

    # Expand acronyms
    expanded_text = expand_acronyms(document_text)

    # Write the result to the output file
    with open(output_file, 'w') as file:
        file.write(expanded_text)

    print(f"Acronym expansion complete. Result saved in {output_file}")

if __name__ == "__main__":
    main()
