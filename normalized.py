import sys

def normalize_ner_output(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Strip whitespace and ignore empty lines
            line = line.strip()
            if not line:
                continue
            
            # Split the line into word and tag (assuming space-separated)
            parts = line.split()
            if len(parts) < 2:
                continue  # Skip lines that don't have enough parts
            
            word = parts[0]
            tag = parts[1]
            
            # Write the normalized output
            outfile.write(f"{word} {tag}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 normalize.py <input-file> <output-file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    normalize_ner_output(input_file, output_file)
    print(f"Normalized output written to {output_file}")
