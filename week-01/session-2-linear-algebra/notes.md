# 📐 Linear Algebra Fundamentals – Complete Notes

## 📌 Table of Contents

1. [Vectors](#vectors)
2. [Matrices](#matrices)
3. [Matrix Operations](#matrix-operations)
4. [Types of Matrices](#types-of-matrices)
5. [Linear Transformations](#linear-transformations)
6. [Eigenvalues and Eigenvectors](#eigenvalues-and-eigenvectors)

---

## ➡️ Vectors

### What is a Vector?

A vector is an **ordered list of numbers** that can represent a point in space.

- Has **magnitude** (length) and **direction**
- Used in AI to represent: data points, features, weights

### Example
`v = [2, 3, 1]` ← 3-dimensional vector

### Vector Operations

| Operation | How It Works | Example |
|-----------|--------------|---------|
| **Addition** | Add corresponding elements | [1,2] + [3,4] = [4,6] |
| **Subtraction** | Subtract corresponding elements | [5,7] - [2,3] = [3,4] |
| **Scalar Multiplication** | Multiply each element by a scalar | 2 × [1,2] = [2,4] |

---

## 📊 Matrices

### What is a Matrix?

A matrix is a **rectangular array of numbers** arranged in rows and columns.

### Example
```text
A = [1 2 3]
    [4 5 6]
```
↑ 2 rows, 3 columns (2×3 matrix)

### Why Matrices in AI?

| Use Case | Why? |
|----------|------|
| **Data Representation** | Each row = data point, each column = feature |
| **Linear Transformations** | Scale, rotate, translate data |
| **Matrix Operations** | Linear regression, neural networks, PCA |

---

## 🔢 Matrix Operations

### Matrix Multiplication

**Rule:** Columns of first = Rows of second
$$A_{(m \times n)} \times B_{(n \times p)} = C_{(m \times p)}$$

**How:** Each element = dot product of row from A and column from B

### Determinant

| What | Formula (2×2) | Example |
|------|---------------|---------|
| **det(A)** | ad - bc | For [[1,2],[3,4]]: det = 1×4 - 2×3 = -2 |

### Inverse

| What | Formula (2×2) | Condition |
|------|---------------|-----------|
| **A⁻¹** | (1/det) × [[d, -b], [-c, a]] | det ≠ 0 |

### Transpose

Flip matrix over diagonal (rows ↔ columns)
```text
A = [1 2]   Aᵀ = [1 3]
    [3 4]        [2 4]
```

---

## 📋 Types of Matrices

| Type | Definition | Example |
|------|------------|---------|
| **Square** | Same rows and columns | `[[1,2],[3,4]]` |
| **Diagonal** | Non-diagonal = 0 | `[[2,0],[0,3]]` |
| **Identity** | Diagonal = 1, rest = 0 | `[[1,0],[0,1]]` |
| **Zero** | All elements = 0 | `[[0,0],[0,0]]` |
| **Row** | Only 1 row | `[1, 2, 3]` |
| **Symmetric** | A = Aᵀ | `[[1,2],[2,1]]` |

---

## 🔄 Linear Transformations

A function that maps vectors from one space to another.

### Common Types

| Type | Effect | Matrix Example |
|------|--------|----------------|
| **Scaling** | Change size | `[[2,0],[0,2]]` |
| **Rotation** | Rotate around origin | `[[cosθ, -sinθ],[sinθ, cosθ]]` |
| **Reflection** | Flip over axis | `[[1,0],[0,-1]]` |
| **Shearing** | Distort shape | `[[1,k],[0,1]]` |

---

## 🔑 Eigenvalues and Eigenvectors

### What Are They?

- **Eigenvector (v):** A vector that only changes by a scalar when a transformation is applied
- **Eigenvalue (λ):** The scalar that shows how much the eigenvector is stretched/compressed

### Formula
$$A \times \mathbf{v} = \lambda \times \mathbf{v}$$

- $A$ = transformation matrix
- $\mathbf{v}$ = eigenvector (doesn't change direction)
- $\lambda$ = eigenvalue (stretch factor)

### How to Find Eigenvalues

1. Solve **characteristic equation**: $\det(A - \lambda I) = 0$
2. Find $\lambda$ values
3. Substitute each $\lambda$ back to find eigenvectors

---

## 📝 Key Takeaways

| Concept | One-Liner |
|---------|-----------|
| **Vector** | Ordered list of numbers, represents points/directions |
| **Matrix** | Rectangular array, represents transformations |
| **Matrix Multiplication** | Rows × Columns, dot product method |
| **Determinant** | Scalar value, tells if matrix is invertible |
| **Inverse** | Matrix that "undoes" multiplication |
| **Transpose** | Flip rows and columns |
| **Eigenvalue** | Stretch factor of a transformation |
| **Eigenvector** | Direction that doesn't change during transformation |
