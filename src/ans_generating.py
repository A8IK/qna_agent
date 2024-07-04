import spacy
from collections import defaultdict

nlp = spacy.load("en_core_web_md")

def find_answer(keywords, content):
    doc = nlp(content)
    sentences = [sent.text for sent in doc.sents]
    best_sentence = None
    highest_score = 0

    for sentence in sentences:
        sentence_doc = nlp(sentence)
        sentence_tokens = {token.text.lower() for token in sentence_doc}
        keyword_overlap = sum(1 for keyword in keywords if keyword.lower() in sentence_tokens)
        
        # Calculating semantic similarity
        keyword_doc = nlp(" ".join(keywords))
        semantic_similarity = keyword_doc.similarity(sentence_doc)
        
        # Combined both scores
        combined_score = keyword_overlap + semantic_similarity
        
        if combined_score > highest_score:
            highest_score = combined_score
            best_sentence = sentence

    return best_sentence if best_sentence else "Answer not found."

if __name__ == "__main__":
    with open("../data/bangladesh_preprocessed_content.txt", "r", encoding="utf-8") as file:
        content = file.read()
    question = input("Enter your question: ")
    from ques_parsing import parse_question
    keywords = parse_question(question)
    answer = find_answer(keywords, content)
    print("Answer:", answer)
