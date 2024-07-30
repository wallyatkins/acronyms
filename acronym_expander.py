import re
import csv

def load_acronyms(file_path):
    """Load acronyms from a CSV file."""
    acronyms = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                acronyms[row[0]] = row[1]
    return acronyms

def read_document(file_path):
    """Read the contents of a document."""
    with open(file_path, 'r') as file:
        return file.read()

def expand_acronyms(text, acronyms):
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
    dictionary_file = "dictionary.csv"

    # Load acronyms from the dictionary file
    acronyms = load_acronyms(dictionary_file)

    # Read the input document
    document_text = read_document(input_file)

    # Expand acronyms
    expanded_text = expand_acronyms(document_text, acronyms)

    # Write the result to the output file
    with open(output_file, 'w') as file:
        file.write(expanded_text)

    print(f"Acronym expansion complete. Result saved in {output_file}")

if __name__ == "__main__":
    main()
