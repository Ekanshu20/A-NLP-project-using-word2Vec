![Quora Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Quora_logo_2015.svg/320px-Quora_logo_2015.svg.png)

# Duplicate Question Pair Detection

An NLP project that identifies duplicate question pairs on Quora using Machine Learning and Word2Vec embeddings.

## 🎯 Problem Statement

Quora often has multiple questions with the same intent but different phrasing. This project aims to identify such duplicate questions to improve user experience and reduce redundancy.

**Example:**
- Q1: "What are the best methods for improving concentration and focus?"
- Q2: "How can I enhance my ability to concentrate and stay focused during tasks?"

These questions are duplicates despite different wording.

## 📊 Dataset

- **Source**: [Kaggle - Quora Question Pairs](https://www.kaggle.com/c/quora-question-pairs)
- **Size**: 404,290 question pairs (~23MB)
- **Distribution**: 63.08% non-duplicate, 36.92% duplicate

## 🛠️ Methodology

### 1. Text Preprocessing
- Remove HTML tags, links, and special characters
- Remove stopwords and punctuation
- Stemming and lowercasing
- Expand contractions

### 2. Feature Engineering

**Basic Features:**
- Question lengths and word counts
- Common words between questions
- Word share ratio

**Advanced Fuzzy Features:**
- Token ratios (min/max)
- Stop word ratios
- FuzzyWuzzy similarity scores (fuzz_ratio, token_sort_ratio, token_set_ratio)
- First/last word equality
- Longest common substring ratio

### 3. Word2Vec Embeddings
- Two-layer neural network for learning word embeddings
- Captures semantic relationships between words
- Vector representation for each unique word

### 4. Model Training
- **Algorithm**: Random Forest Classifier
- **Train-Test Split**: 80-20
- **Accuracy**: 82.79%

## 🔑 Key Insights

- Questions with `word_share < 0.21` are typically non-duplicate
- Questions with `word_share > 0.21` are typically duplicate
- 20.78% of questions appear more than once in the dataset

## 💻 Installation
```bash
! pip install pandas numpy scikit-learn fuzzywuzzy gensim nltk

# Load dataset
import pandas as pd
df = pd.read_csv('train.csv')

# Preprocess text
# Extract features
# Train Word2Vec model
# Train Random Forest classifier
# Predict duplicate pairs
```

## 📈 Results

| Metric | Score |
|--------|-------|
| Accuracy | 82.79% |
| Training Time | 2-2.5 hours |

## 🔮 Future Improvements

- Implement deep learning models (CNN, RNN, Attention mechanisms)
- Hyperparameter tuning for better accuracy
- Explore transformer-based models (BERT, RoBERTa)

## 🖥️ System Requirements

- **RAM**: 16GB minimum
- **GPU**: Recommended for faster training

## 📚 References

- [Kaggle Competition](https://www.kaggle.com/c/quora-question-pairs)
- [Word2Vec Explained](https://www.coveo.com/blog/word2vec-explained/)

## 👤 Author
- Ekanshu agrawal
