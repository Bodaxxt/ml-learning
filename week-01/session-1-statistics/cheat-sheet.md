# 📊 Statistics Cheat Sheet

## 🎯 Central Tendency (The "Center")
- **Mean** = Σx / n (Average – sensitive to outliers)
- **Median** = Middle value (Robust – use for skewed data)
- **Mode** = Most frequent (Best for categorical data)

## 📐 Dispersion (The "Spread")
- **Range** = Max - Min (Quick but sensitive)
- **IQR** = Q3 - Q1 (Robust – middle 50%)
- **Variance** = Σ(x - μ)² / n (Squared units)
- **Std Dev** = √Variance (Same units as data)

## 🎲 Probability
P(A) = favorable / total

- **Addition Rule:** P(A ∪ B) = P(A) + P(B) [Mutually Exclusive]
- **Multiplication:** P(A ∩ B) = P(A) × P(B) [Independent]
- **Conditional:** P(A|B) = P(A ∩ B) / P(B)

## 🧠 Bayes' Theorem
$$P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$$

- **Prior = P(A)** ← Your belief BEFORE evidence
- **Likelihood = P(B|A)** ← How likely is evidence given A?
- **Evidence = P(B)** ← How likely is evidence in general?
- **Posterior = P(A|B)** ← Your belief AFTER evidence

## 🔬 Inferential Statistics
- **CLT:** Sample mean ~ Normal (if n > 30)

**Hypothesis Testing:**
- H₀ = No effect (default)
- H₁ = There is an effect
- If p < 0.05 → Reject H₀

**Confidence Interval:**
- Mean ± (z * SE)
- 95% CI = We're 95% sure the true mean is in this range

---

## 🔑 Key Takeaways

| Concept | One-Liner |
|---------|-----------|
| **Population** | Everyone |
| **Sample** | Some of everyone |
| **Mean** | Average |
| **Median** | Middle |
| **Mode** | Most common |
| **Standard Deviation** | Average distance from mean |
| **IQR** | Middle 50% spread |
| **Bayes' Theorem** | Update beliefs with new data |
| **CLT** | Large samples = normal distribution |
| **p-value** | Probability of seeing this data if H₀ is true |
