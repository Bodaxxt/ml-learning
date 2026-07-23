# 📩 SMS Spam Detector Project

An end-to-end Natural Language Processing (NLP) and Machine Learning project that classifies SMS messages into **Ham** (legitimate) or **Spam** (unwanted) using **TF-IDF Vectorization** and **Multinomial Naive Bayes**.

---

## 📁 Repository Structure

- `spam_detector.ipynb`: Jupyter Notebook containing data loading, EDA, preprocessing, model training, evaluation, and inference.
- `data/spam.csv`: Dataset containing SMS text messages with `ham` or `spam` labels.
- `vectorizer.pkl`: Saved TF-IDF Vectorizer artifact.
- `model.pkl`: Saved Multinomial Naive Bayes model artifact.
- `requirements.txt`: Python package dependencies.
- `README.md`: Comprehensive project documentation and mathematical explanations.

---

## 📐 Mathematical Foundations

This section provides a rigorous breakdown of all mathematical principles and formulations utilized throughout the machine learning pipeline in `spam_detector.ipynb`.

---

### 1. Text Vectorization: Term Frequency-Inverse Document Frequency (TF-IDF)

To convert raw textual messages into numerical feature vectors that machine learning models can compute, we employ **TF-IDF Vectorization**. TF-IDF reflects how important a word is to a specific document within a collection or corpus.

#### A. Term Frequency (TF)
Term Frequency measures the relative frequency of a term $t$ in a document $d$:

$$\text{TF}(t, d) = \frac{f_{t,d}}{\sum_{t' \in d} f_{t',d}}$$

where:
- $f_{t,d}$ is the raw count of term $t$ in document $d$.
- $\sum_{t' \in d} f_{t',d}$ is the total count of all terms in document $d$.

#### B. Inverse Document Frequency (IDF)
Inverse Document Frequency downweights common terms across all documents (e.g., "the", "is") and boosts rare, distinctive terms. Using the standard smoothed formula implemented in `scikit-learn`:

$$\text{IDF}(t, D) = \ln \left( \frac{1 + |D|}{1 + |\{d \in D : t \in d\}|} \right) + 1$$

where:
- $|D|$ is the total number of documents in the corpus $D$.
- $|\{d \in D : t \in d\}|$ is the number of documents containing term $t$.
- $+1$ smoothing inside the logarithm prevents division by zero.
- The trailing $+1$ guarantees terms present in all documents do not get completely zeroed out.

#### C. TF-IDF Weight Calculation
The raw TF-IDF score for term $t$ in document $d$ is:

$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

#### D. L2 Euclidean Vector Normalization
To compensate for varying text lengths, `TfidfVectorizer` applies L2 normalization to each document's feature vector $\mathbf{v}$:

$$\mathbf{v}_{\text{norm}} = \frac{\mathbf{v}}{\|\mathbf{v}\|_2} = \frac{\mathbf{v}}{\sqrt{\sum_{i=1}^{n} v_i^2}}$$

This projects feature vectors onto the unit hyper-sphere, making similarity measurements independent of text length.

---

### 2. Classification Algorithm: Multinomial Naive Bayes (MNB)

Multinomial Naive Bayes is a probabilistic classifier suited for discrete feature counts (or TF-IDF feature weights) representing word frequencies.

#### A. Bayes' Theorem
Given a document feature vector $\mathbf{x} = (x_1, x_2, \dots, x_n)$ containing feature values for $n$ terms, Bayes' Theorem states:

$$P(Y = y \mid \mathbf{X} = \mathbf{x}) = \frac{P(Y = y) \cdot P(\mathbf{X} = \mathbf{x} \mid Y = y)}{P(\mathbf{X} = \mathbf{x})}$$

where:
- $P(Y = y \mid \mathbf{X} = \mathbf{x})$ is the **Posterior probability** that text $\mathbf{x}$ belongs to class $y \in \{\text{ham}, \text{spam}\}$.
- $P(Y = y)$ is the **Prior probability** of class $y$.
- $P(\mathbf{X} = \mathbf{x} \mid Y = y)$ is the **Likelihood** of feature vector $\mathbf{x}$ given class $y$.
- $P(\mathbf{X} = \mathbf{x})$ is the **Evidence** (marginal probability), constant across all classes.

#### B. The Naive Conditional Independence Assumption
Naive Bayes assumes that features $x_i$ are conditionally independent given the class label $y$:

$$P(\mathbf{x} \mid y) = \prod_{i=1}^{n} P(x_i \mid y)^{x_i}$$

#### C. Maximum A Posteriori (MAP) Decision Rule
Since evidence $P(\mathbf{x})$ is identical for both classes, the optimal class prediction $\hat{y}$ simplifies to:

$$\hat{y} = \arg\max_{y \in \{\text{ham}, \text{spam}\}} \left( P(y) \prod_{i=1}^{n} P(x_i \mid y)^{x_i} \right)$$

#### D. Log-Likelihood Formulation
Multiplying many small probabilities causes **floating-point numerical underflow**. We apply the natural logarithm to transform products into additions:

$$\hat{y} = \arg\max_{y \in \{\text{ham}, \text{spam}\}} \left( \ln P(y) + \sum_{i=1}^{n} x_i \cdot \ln P(x_i \mid y) \right)$$

#### E. Parameter Estimation & Laplace Smoothing ($\alpha=1$)
Class priors are estimated from training sample ratios:

$$P(Y = y) = \frac{N_y}{N_{\text{total}}}$$

Feature likelihoods $P(x_i \mid y) = \theta_{y,i}$ are estimated using **Additive (Laplace) Smoothing** to eliminate zero-probability errors when encountering unseen vocabulary in a class:

$$\hat{\theta}_{y, i} = \frac{\sum_{d \in \text{Class } y} x_{d,i} + \alpha}{\sum_{i'=1}^{n} \sum_{d \in \text{Class } y} x_{d,i'} + \alpha \cdot n}$$

where:
- $\sum_{d \in \text{Class } y} x_{d,i}$ is the total sum of TF-IDF feature weights for term $i$ in training documents of class $y$.
- $n$ is the vocabulary size (number of features, $n = 5000$).
- $\alpha = 1.0$ is the smoothing parameter (Laplace smoothing).

---

### 3. Model Evaluation Metrics

Model performance is evaluated on an independent test dataset using a $2 \times 2$ Confusion Matrix:

| | Predicted Ham | Predicted Spam |
|---|---|---|
| **Actual Ham** | True Negative ($TN$) | False Positive ($FP$) |
| **Actual Spam** | False Negative ($FN$) | True Positive ($TP$) |

#### A. Accuracy
Measures the overall proportion of correctly classified messages:

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

#### B. Precision
Measures the proportion of actual spam messages among all messages predicted as spam (minimizes false alarms):

$$\text{Precision} = \frac{TP}{TP + FP}$$

#### C. Recall (Sensitivity / True Positive Rate)
Measures the proportion of actual spam messages correctly identified by the model:

$$\text{Recall} = \frac{TP}{TP + FN}$$

#### D. F1-Score
The harmonic mean of Precision and Recall, providing a balanced single-figure metric for imbalanced datasets:

$$\text{F1-Score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2 \cdot TP}{2 \cdot TP + FP + FN}$$

---

## 🚀 How to Run the Project

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Notebook**:
   Open `spam_detector.ipynb` in VS Code or Jupyter Notebook and execute all cells sequentially:
   ```bash
   jupyter notebook spam_detector.ipynb
   ```
