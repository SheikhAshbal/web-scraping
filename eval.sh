#!/bin/bash

# Ensure three arguments are passed (gold standard file, NER output file, and eval output file)
if [ "$#" -ne 3 ]; then
    echo "Usage: ./eval.sh <gold-standard-file> <ner-output-file> <eval-output-file>"
    exit 1
fi

# Assign arguments to variables
GOLD_STANDARD=$1
NER_OUTPUT=$2
EVAL_OUTPUT=$3

# Paths to Stanford NER jar and model (adjust the paths accordingly)
STANFORD_NER_PATH="/home/sheikhashbal/stanford-ner-2020-11-17"
EVALUATOR_CLASS="edu.stanford.nlp.ie.crf.CRFClassifier"
NER_MODEL="$STANFORD_NER_PATH/classifiers/english.muc.7class.distsim.crf.ser.gz"

# Run the Stanford NER evaluation (replace with the correct command for your setup)
java -cp "$STANFORD_NER_PATH/stanford-ner.jar:$STANFORD_NER_PATH/lib/*" \
    $EVALUATOR_CLASS \
    -loadClassifier $NER_MODEL \
    -testFile $GOLD_STANDARD \
    -testResultFile $NER_OUTPUT \
    -outputFormat inlineXML

# Print evaluation summary
echo "Evaluation completed for $GOLD_STANDARD against $NER_OUTPUT"
