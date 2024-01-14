import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
import requests
from bs4 import BeautifulSoup

def get_text_from_link(link):
    try:
        response = requests.get(link)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text content from the parsed HTML
        text_content = soup.get_text(separator=' ', strip=True)

        return text_content
    except requests.RequestException as e:
        # Handle request errors (e.g., link not accessible)
        return f"Error fetching content from link: {e}"

def textrank_summarizer(text, summary_percent=30):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text])

    # Create a graph representation of the sentences
    graph = nx.Graph()

    # Use SpaCy for accurate tokenization
    nlp = spacy.load('en_core_web_sm')
    sentences = [sent.text for sent in nlp(text).sents]

    # Calculate sentence vectors using the TfidfVectorizer
    sentence_vectors = vectorizer.transform(sentences).toarray()

    # Add nodes to the graph with sentence vectors
    for i, sentence_vector in enumerate(sentence_vectors):
        graph.add_node(i, weight=sentence_vector)

    # Calculate similarity between sentences and add edges to the graph
    for i in range(len(graph.nodes)):
        for j in range(i + 1, len(graph.nodes)):
            similarity = sum(graph.nodes[i]['weight'] * graph.nodes[j]['weight'])
            graph.add_edge(i, j, weight=similarity)

    # Use NetworkX's pagerank algorithm to rank sentences
    scores = nx.pagerank(graph, weight='weight')

    # Calculate the total word count of the original text
    original_word_count = len(text.split())

    # Calculate the desired summary length in words
    target_word_count = int(original_word_count * summary_percent/100)

    # Get the top-ranked sentences until the desired word count is reached
    sorted_sentences = sorted(scores, key=scores.get, reverse=True)
    selected_sentences = []
    current_word_count = 0

    for i in sorted_sentences:
        current_word_count += len(sentences[i].split())
        if current_word_count <= target_word_count:
            selected_sentences.append(sentences[i])

    # Return the summary and word counts
    summary = '. '.join(selected_sentences)
    summary_word_count = len(summary.split())

    # return {
    #     'original_text': text,
    #     'original_word_count': original_word_count,
    #     'summary_text': summary,
    #     'summary_word_count': summary_word_count,
    #     'summary_percent': summary_percent
    # } summary, original_txt, len_orig_txt, len_summary
    
    return summary, text, original_word_count, summary_word_count, summary_percent