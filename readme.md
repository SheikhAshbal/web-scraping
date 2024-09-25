# Project Title: Named Entity Recognition (NER) Evaluation

## Overview
This project evaluates Named Entity Recognition (NER) outputs using Stanford NER. It involves generating NER outputs from Wikipedia and Fandom (fanwiki) text sources, normalizing the output formats, and evaluating the NER accuracy against gold standard files.

## Project Steps

### 1. Setup Environment
Ensure you have the following prerequisites installed:
- Python 3.x
- Java Runtime Environment
- Stanford NER package
- Required Python libraries (e.g., `sklearn`)

### 2. Prepare Text Files
- Obtain the raw text files:
  - `wikipedia.txt`
  - `fanwiki.txt`

### 3. Generate NER Outputs
Run the NER script for both datasets:
```bash
./ner.sh wikipedia.txt stanford-wikipedia.txt
./ner.sh fanwiki.txt stanford-fanwiki.txt
###  4. Normalize Output Files
Create normalized versions of the NER outputs:
python3 normalize.py stanford-wikipedia.txt stanford-wikipedia-normalized.txt
python3 normalize.py stanford-fanwiki.txt stanford-fanwiki-normalized.txt


Here’s the README.md content in code form for easy copying:

markdown
Copy code
# Project Title: Named Entity Recognition (NER) Evaluation

## Overview
This project evaluates Named Entity Recognition (NER) outputs using Stanford NER. It involves generating NER outputs from Wikipedia and Fandom (fanwiki) text sources, normalizing the output formats, and evaluating the NER accuracy against gold standard files.

## Project Steps

### 1. Setup Environment
Ensure you have the following prerequisites installed:
- Python 3.x
- Java Runtime Environment
- Stanford NER package
- Required Python libraries (e.g., `sklearn`)

### 2. Prepare Text Files
- Obtain the raw text files:
  - `wikipedia.txt`
  - `fanwiki.txt`

### 3. Generate NER Outputs
Run the NER script for both datasets:
```bash
./ner.sh wikipedia.txt stanford-wikipedia.txt
./ner.sh fanwiki.txt stanford-fanwiki.txt

### 4. Normalize Output Files
Create normalized versions of the NER outputs:

bash
Copy code
python3 normalize.py stanford-wikipedia.txt stanford-wikipedia-normalized.txt
python3 normalize.py stanford-fanwiki.txt stanford-fanwiki-normalized.txt
i change the name of normalize files into old name
###  5. Create Gold Standard Files
Create gold standard files based on your evaluation needs:
wikipedia-gold.txt
fanwiki-gold.txt


Here’s the README.md content in code form for easy copying:

markdown
Copy code
# Project Title: Named Entity Recognition (NER) Evaluation

## Overview
This project evaluates Named Entity Recognition (NER) outputs using Stanford NER. It involves generating NER outputs from Wikipedia and Fandom (fanwiki) text sources, normalizing the output formats, and evaluating the NER accuracy against gold standard files.

## Project Steps

### 1. Setup Environment
Ensure you have the following prerequisites installed:
- Python 3.x
- Java Runtime Environment
- Stanford NER package
- Required Python libraries (e.g., `sklearn`)

### 2. Prepare Text Files
- Obtain the raw text files:
  - `wikipedia.txt`
  - `fanwiki.txt`

### 3. Generate NER Outputs
Run the NER script for both datasets:
```bash
./ner.sh wikipedia.txt stanford-wikipedia.txt
./ner.sh fanwiki.txt stanford-fanwiki.txt
4. Normalize Output Files
Create normalized versions of the NER outputs:

bash
Copy code
python3 normalize.py stanford-wikipedia.txt stanford-wikipedia-normalized.txt
python3 normalize.py stanford-fanwiki.txt stanford-fanwiki-normalized.txt
5. Create Gold Standard Files
Create gold standard files based on your evaluation needs:
wikipedia-gold.txt
fanwiki-gold.txt

### 6. Normalize Gold Standard Files
Normalize the gold standard files:
python3 normalize.py wikipedia-gold.txt wikipedia-gold-normalized.txt
python3 normalize.py fanwiki-gold.txt fanwiki-gold-normalized.txt
i change the names of created file to wikipedia-gold and fanwiki-gold

### 7. Evaluate NER Outputs
Evaluate the NER outputs against the gold standard files:
./eval.sh wikipedia-gold.txt stanford-wikipedia.txt wikipedia-eval.txt
./eval.sh fanwiki-gold.txt stanford-fanwiki.txt fanwiki-eval.txt


