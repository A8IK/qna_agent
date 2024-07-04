from data_extract import extract_content
from pre_process import preprocess
from ques_parsing import parse_question
from ans_generating import find_answer

def main():
    url = "https://en.wikipedia.org/wiki/Bangladesh"
    content = extract_content(url)
    preprocessed_content = preprocess(content)

    while True:
        question = input("Enter your question: ")
        if question.lower() in ["exit", "quit"]:
            break
        keywords = parse_question(question)
        answer = find_answer(keywords, preprocessed_content)
        print("Answer:", answer)

if __name__ == "__main__":
    main()

