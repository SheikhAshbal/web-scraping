import re

def extract_ners(input_file, output_file):
    # Initialize a set to hold unique NERs
    ners = set()

    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            # Find all NERs with <PERSON>, <LOCATION>, and <ORGANIZATION> tags
            found_ners = re.findall(r'<(PERSON|LOCATION|ORGANIZATION)>(.*?)<\/\1>', line)
            for ner in found_ners:
                ners.add(ner[1].strip())  # Add the entity name (remove tags)

    # Write the unique NERs to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for ner in sorted(ners):
            outfile.write(f"{ner}\n")

if __name__ == "__main__":
    # Define input and output files
    wikipedia_file = '/home/sheikhashbal/Desktop/stanfordwikipedia.txt'
    fanwiki_file = '/home/sheikhashbal/Desktop/stanford-fanwiki.txt'

    # Extract NERs
    extract_ners(wikipedia_file, 'ner-list-wikipedia.txt')
    extract_ners(fanwiki_file, 'ner-list-fanwiki.txt')

    print("NER extraction completed. Check ner-list-wikipedia.txt and ner-list-fanwiki.txt for results.")
