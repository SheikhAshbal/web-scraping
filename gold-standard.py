def process_ner_output(input_file, output_file):
    """
    Reads the NER-tagged file and formats it for the gold standard.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            tokens = line.strip().split()
            for token in tokens:
                # Split the token only on the last '/'
                if '/' in token:
                    word, tag = token.rsplit('/', 1)  # Split from the right, only once
                    outfile.write(f"{word} {tag}\n")
                else:
                    # Handle case where no '/' exists (if any)
                    outfile.write(f"{token} O\n")
            outfile.write("\n")  # Add a new line between sentences

# Process the NER outputs for Wikipedia and FanWiki
process_ner_output('/home/sheikhashbal/Desktop/stanford-wikipedia.txt', 'wikipedia-gold.txt')
process_ner_output('/home/sheikhashbal/Desktop/stanford-fanwiki.txt', 'fanwiki-gold.txt')

print("Gold standard files created: wikipedia-gold.txt and fanwiki-gold.txt")
