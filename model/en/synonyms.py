from nltk.corpus import wordnet
import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')


def get_synonyms(word):
    word = word.lower()
    synonyms_list = []
    synonyms_dict = {}
    synonyms = wordnet.synsets(word)
    for syn in synonyms:
        synonyms_dict[str(syn)] = []
        lemmas = syn.lemma_names()
        for word in lemmas:
            word = word.replace('_', ' ')
            synonyms_list.append(word)
            synonyms_dict[str(syn)].append(word)
    synonyms_list = list(set(synonyms_list))
    return (synonyms_list, synonyms_dict)

  
def get_synonyms_enhanced(word):
    word = word.lower()
    synonyms_list = []
    synonyms = wordnet.synsets(word)
    for syn in synonyms:
        if word in str(syn):
            lemmas = syn.lemma_names()
            for w in lemmas:
                w = w.replace('_', ' ')
                synonyms_list.append(w)
    synonyms_list = list(set(synonyms_list))
    return synonyms_list
  
  
def get_synonyms_en(word):
    response = requests.get(f'https://synonyms.reverso.net/synonym/en/{word}', headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    txt = soup.find_all('a', class_='synonym relevant')
    synonyms = []
    for t in txt:
        synonyms.append(t.text.strip())

    return ",".join(synonyms)
