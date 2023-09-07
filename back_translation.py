'''Translate an English Corpus to Amharic sentence by sentece 
    and then the Amharic senteces back to English. 
    If the English translation of the Amharic sentences is similar to
    the original English sentences, take the pair and build a parallel corpus.'''

from sentence_transformers import SentenceTransformer, util
from tqdm import tqdm

print("Loading sentence transformer model...")
model = SentenceTransformer('distilbert-base-nli-mean-tokens')

def translate_text(target: str, text: str) -> str:
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    # print("Text: {}".format(result["input"]))
    # print("Translation: {}".format(result["translatedText"]))
    # print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return result["translatedText"]

def compare_sentences(sent1:str, sent2:str):
    sentences = [sent1, sent2]
    sentence_embeddings = model.encode(sentences)
    sent_similarity = util.pytorch_cos_sim(sentence_embeddings[0], sentence_embeddings[1])
    
    return sent_similarity

def main():
    print("Read sentences from the source file...")
    original_sentences = []
    # Path to English Corpus: multi-line
    source_file_path = 'en_corpus.txt'
    with open(source_file_path, 'r') as f: 
        line = f.readline()
        while line:
            original_sentences.append(line) 
            line = f.readline()

    print("Translating sentences and writing to file......") 
    pr_bar = tqdm(range(len(original_sentences)))
    parallel_file_path = 'parallel_file.txt' 
    with open(parallel_file_path, 'w') as f:
        for i in pr_bar:
            en_sentence = original_sentences[i]
            am_trans = translate_text('am', en_sentence)
            back_trans = translate_text('en', am_trans)
            similarity = compare_sentences(en_sentence, back_trans)
            if similarity.item() >= 0.9:
                line = en_sentence + am_trans + '\n'
                f.write(line)
if __name__ == '__main__':
    main()