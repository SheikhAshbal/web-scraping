import subprocess

# Paths to your Stanford NER jar file and the model you want to use
STANFORD_NER_PATH = "/home/sheikhashbal/stanford-ner-2020-11-17/stanford-ner.jar"
NER_MODEL = "/home/sheikhashbal/stanford-ner-2020-11-17/classifiers/english.muc.7class.distsim.crf.ser.gz"  # Adjust this to your model

def run_ner(input_file, output_file):
    command = [
        "java",
        "-cp", STANFORD_NER_PATH,
        "edu.stanford.nlp.ie.crf.CRFClassifier",
        "-loadClassifier", NER_MODEL,
        "-textFile", input_file,
        "-outputFormat", "inlineXML"
    ]
    
    with open(output_file, "w") as out:
        subprocess.run(command, stdout=out)

# Process the Wikipedia text
run_ner("/home/sheikhashbal/Desktop/wikipedia.txt", "stanfordwikipedia.txt")
# Process the Fanwiki text
run_ner("/home/sheikhashbal/Desktop/fanwiki.txt", "stanford-fanwiki.txt")

print("NER processing completed.")
