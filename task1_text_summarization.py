import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def text_summarizer(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    word_freq = Counter(filtered_words)

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]

    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = " ".join(summary_sentences[:3])

    return summary


if __name__ == "__main__":
    print("CODTECH INTERNSHIP – TASK 1")
    print("TEXT SUMMARIZATION TOOL\n")

    text = input("Enter the text:\n\n")
    summary = text_summarizer(text)

    print("\n--- SUMMARY ---\n")
    print(summary)
