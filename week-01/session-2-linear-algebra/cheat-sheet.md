# 📐 Linear Algebra Cheat Sheet

## ➡️ Vectors
`v = [x₁, x₂, ..., xₙ]`

- **Addition:** [1,2] + [3,4] = [4,6]
- **Subtraction:** [5,7] - [2,3] = [3,4]
- **Scalar:** 2 × [1,2] = [2,4]

## 📊 Matrices
```text
A = [a₁₁ a₁₂]
    [a₂₁ a₂₂]
```

**Multiplication:** $A_{(m \times n)} \times B_{(n \times p)} = C_{(m \times p)}$

## 🔢 Matrix Operations
**Determinant (2×2):**
$$\det(A) = a_{11} a_{22} - a_{12} a_{21}$$

**Inverse (2×2):**
$$A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{bmatrix}$$

**Transpose:**
$$(A^T)_{ij} = A_{ji}$$

## 📋 Types of Matrices
- **Square:** $m = n$
- **Diagonal:** $a_{ij} = 0 \text{ for } i \neq j$
- **Identity:** $a_{ij} = 1 \text{ for } i = j, 0 \text{ for } i \neq j$
- **Zero:** all elements = 0
- **Symmetric:** $A = A^T$

## 🔄 Linear Transformations
- **Scaling:** $\begin{bmatrix} s_1 & 0 \\ 0 & s_2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$
- **Rotation:** $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$
- **Reflection:** $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$

## 🔑 Eigenvalues & Eigenvectors
$$A \mathbf{v} = \lambda \mathbf{v}$$

- **Eigenvalues:** $\det(A - \lambda I) = 0$
- **Eigenvectors:** $(A - \lambda I)\mathbf{v} = 0$

---

## 🎯 Quick Memory

| Concept | One-Liner |
|---------|-----------|
| **Vector** | Arrow in space |
| **Matrix** | Grid of numbers |
| **Determinant** | Area/volume scale factor |
| **Inverse** | "Undo" button |
| **Transpose** | Flip over diagonal |
| **Eigenvalue** | Stretch factor |
| **Eigenvector** | Direction that doesn't change |
