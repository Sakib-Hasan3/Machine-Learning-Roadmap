---

## ✅ Cell 1: Download (প্রথমবার চালালে)

```python
import nltk
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
```

---

## ✅ Cell 2: POS Tagging (Code)

```python
from nltk import word_tokenize, pos_tag

sentence = "The children are running fast in London."

tokens = word_tokenize(sentence)
tags = pos_tag(tokens)

print("Tokens:", tokens)
print("\nPOS Tags:")
for word, tag in tags:
    print(word, "→", tag)
```

---

## 📤 Output

```
Tokens: ['The', 'children', 'are', 'running', 'fast', 'in', 'London', '.']

POS Tags:
The → DT
children → NNS
are → VBP
running → VBG
fast → RB
in → IN
London → NNP
. → .
```

---

## ✅ Bonus: পুরো list এক লাইনে দেখতে চাইলে

```python
print(tags)
```

### 📤 Output

```
[('The', 'DT'), ('children', 'NNS'), ('are', 'VBP'), ('running', 'VBG'),
 ('fast', 'RB'), ('in', 'IN'), ('London', 'NNP'), ('.', '.')]
```

---

