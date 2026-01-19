---

## ✅ Sentence (একইটা দু’জায়গায়)

**"Apple is looking at buying a startup in London in 2024."**

---

## 1) spaCy vs NLTK — Full Comparison Code

```python
# ---------- NLTK ----------
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import pos_tag

# (প্রথমবার চালালে লাগতে পারে)
# nltk.download("punkt")
# nltk.download("averaged_perceptron_tagger")

sentence = "Apple is looking at buying a startup in London in 2024."

tokens_nltk = word_tokenize(sentence)
ps = PorterStemmer()
stems = [ps.stem(w) for w in tokens_nltk]
pos_nltk = pos_tag(tokens_nltk)

print("=== NLTK ===")
print("Tokens:", tokens_nltk)
print("Stems:", stems)
print("POS:", pos_nltk)


# ---------- spaCy ----------
import spacy

# (প্রথমবার ইনস্টল করলে: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

doc = nlp(sentence)

tokens_spacy = [t.text for t in doc]
lemmas_spacy = [t.lemma_ for t in doc]
pos_spacy = [(t.text, t.pos_) for t in doc]
entities_spacy = [(ent.text, ent.label_) for ent in doc.ents]

print("\n=== spaCy ===")
print("Tokens:", tokens_spacy)
print("Lemmas:", lemmas_spacy)
print("POS:", pos_spacy)
print("Entities (NER):", entities_spacy)
```

---

## 2) Expected Output (Example)

### ✅ NLTK Output

```
=== NLTK ===
Tokens: ['Apple', 'is', 'looking', 'at', 'buying', 'a', 'startup', 'in', 'London', 'in', '2024', '.']
Stems:  ['appl', 'is', 'look', 'at', 'buy', 'a', 'startup', 'in', 'london', 'in', '2024', '.']
POS: [('Apple', 'NNP'), ('is', 'VBZ'), ('looking', 'VBG'), ('at', 'IN'), ('buying', 'VBG'),
      ('a', 'DT'), ('startup', 'NN'), ('in', 'IN'), ('London', 'NNP'), ('in', 'IN'), ('2024', 'CD'), ('.', '.')]
```

📌 এখানে দেখুন:

* **Stemming** করে “Apple → appl” (real word না—কেটে দিয়েছে)

---

### ✅ spaCy Output

```
=== spaCy ===
Tokens: ['Apple', 'is', 'looking', 'at', 'buying', 'a', 'startup', 'in', 'London', 'in', '2024', '.']
Lemmas: ['Apple', 'be', 'look', 'at', 'buy', 'a', 'startup', 'in', 'London', 'in', '2024', '.']
POS: [('Apple', 'PROPN'), ('is', 'AUX'), ('looking', 'VERB'), ('at', 'ADP'), ('buying', 'VERB'),
      ('a', 'DET'), ('startup', 'NOUN'), ('in', 'ADP'), ('London', 'PROPN'), ('in', 'ADP'), ('2024', 'NUM'), ('.', 'PUNCT')]
Entities (NER): [('Apple', 'ORG'), ('London', 'GPE'), ('2024', 'DATE')]
```

📌 এখানে দেখুন:

* **Lemmatization** করে “is → be” (grammar-aware)
* **NER** দিয়ে ORG/GPE/DATE ধরছে (NLTK basic সেটাপে এটা সাধারণত থাকে না)

---

## 3) Quick Takeaway (এক লাইনে)

* **NLTK**: শেখা + basic preprocessing (tokenize, stem, basic POS)
* **spaCy**: fast + accurate + **Lemmatization + NER + full NLP pipeline**

---


