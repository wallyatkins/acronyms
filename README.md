# Acronym Expander

This Python script scans a document for acronyms and replaces them with their full forms based on a predefined dictionary.

## Features

- Reads input from a text file
- Identifies acronyms (strings of two or more capital letters)
- Replaces known acronyms with their full forms
- Writes the result to a new output file

## Requirements

- Python 3.x

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `acronym_expander.py` file.
3. Prepare your input document:
   - Create a text file named `input_document.txt` in the same directory as the script.
   - Write your text with acronyms in this file.
4. Run the script:
   ```
   python acronym_expander.py
   ```
5. The script will create an `output_document.txt` file with the expanded acronyms.

## Example

Input (`input_document.txt`):
```
The NASA and FBI are working together on a new project. The UN and WHO are also involved.
```

Output (`output_document.txt`):
```
The National Aeronautics and Space Administration and Federal Bureau of Investigation are working together on a new project. The United Nations and World Health Organization are also involved.
```

## Customizing Acronyms

To add or modify acronyms, edit the `dictionary.csv` file. Each line should contain an acronym and its full form, separated by a comma:

```
NASA,National Aeronautics and Space Administration
FBI,Federal Bureau of Investigation
CIA,Central Intelligence Agency
UN,United Nations
WHO,World Health Organization
```

You can add your own acronyms to this file, one per line, following the same format.

## License

This project is open source and available under the [MIT License](LICENSE).
