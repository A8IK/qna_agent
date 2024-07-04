import spacy

nlp = spacy.load("en_core_web_sm")

def parse_question(question):
    doc = nlp(question)
    keywords = [token.lemma_ for token in doc if token.is_alpha]
    return keywords

if __name__ == "__main__":
    question = "What is the capital of Bangladesh?"
    keywords = parse_question(question)
    print(keywords)

