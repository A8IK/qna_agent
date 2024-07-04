import re
import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    text = re.sub(r'\[.*?\]', '', text)  # Remove references
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    cleaned_sentences = [sent.strip() for sent in sentences if sent.strip()]
    return " ".join(cleaned_sentences)

if __name__ == "__main__":
    with open("../data/bangladesh_wikipedia_content.txt", "r" , encoding="utf-8") as file:
        content = file.read()
    preprocessed_content = preprocess(content)
    with open("../data/bangladesh_preprocessed_content.txt", "w" , encoding="utf-8") as file:
        file.write(preprocessed_content)
