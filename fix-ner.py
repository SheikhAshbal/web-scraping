import sys
import re

def is_punctuation(word):
    # Check if the word is punctuation using regex
    return re.match(r'^[^\w\s]+$', word) is not None

def fix_ner(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Each line should contain a word and its tag separated by space
            parts = line.strip().split()
            if len(parts) == 2:
                word, tag = parts[0], parts[1]
                if is_punctuation(word):
                    tag = 'O'  # Replace the tag with 'O' if the word is punctuation
                outfile.write(f"{word} {tag}\n")
            else:
                outfile.write(line)  # Write the line as is if it's improperly formatted

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 fix-ner.py <input-file> <output-file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    fix_ner(input_file, output_file)
