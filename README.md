# 🔐 ElGamal Digital Signature

A Python-based implementation of the **ElGamal Digital Signature Scheme**, developed as an educational project for studying cryptography, digital signatures, and information security.

The application provides a simple graphical interface built with **Tkinter**, allowing users to generate keys, sign text files, and verify digital signatures.

---

## ✨ Features

- Generate ElGamal parameters
- Generate public and private keys
- Sign text files using the ElGamal signature algorithm
- Hash message content using SHA-256
- Generate digital signature `(r, s)`
- Save signatures to `.sig` files
- Verify digital signatures
- Detect modified message content
- Simple graphical user interface using Tkinter

---

## 🧠 ElGamal Digital Signature

The ElGamal signature scheme is based on the difficulty of the **Discrete Logarithm Problem**.

### Key Generation

Choose:

- A prime number `p`
- A generator `g`
- A private key `x`

The public key is calculated as:

```text
y = g^x mod p
```

Public key:

```text
(p, g, y)
```

Private key:

```text
x
```

---

## ✍️ Signature Generation

The message is first hashed using SHA-256:

```text
h = SHA256(message)
```

Choose a random integer `k` such that:

```text
gcd(k, p - 1) = 1
```

Then calculate:

```text
r = g^k mod p
```

and:

```text
s = k⁻¹(h - xr) mod (p - 1)
```

The resulting digital signature is:

```text
(r, s)
```

---

## ✅ Signature Verification

A signature is valid when:

```text
g^h mod p = y^r × r^s mod p
```

where:

```text
y = public key
h = hash of the message
(r, s) = digital signature
```

If the document is modified after signing, the verification process will fail.

---

## 🖥️ Application Workflow

```text
              ┌──────────────────────┐
              │     Select File      │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │    SHA-256 Hash      │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   ElGamal Signing    │
              └──────────┬───────────┘
                         │
                         ▼
                   Signature (r,s)
                         │
                         ▼
              ┌──────────────────────┐
              │ ElGamal Verification │
              └──────────┬───────────┘
                         │
                 ┌───────┴───────┐
                 ▼               ▼
              VALID           INVALID
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/duongsec/Elgamlal-signature.git
```

```bash
cd Elgamlal-signature
```

### 2. Check Python

Python 3 is required.

```bash
python --version
```

or:

```bash
python3 --version
```

### 3. Run the application

```bash
python Elgammal.py
```

On some systems:

```bash
python3 Elgammal.py
```

---

## 📂 Project Structure

```text
Elgamlal-signature/
│
├── Elgammal.py
├── Bài tập lớn ATBMTT bản cuốiii (1).pdf
└── README.md
```

### `Elgammal.py`

Main Python application containing:

- ElGamal mathematical operations
- Prime generation
- Modular exponentiation
- Key generation
- SHA-256 hashing
- Signature generation
- Signature verification
- Tkinter GUI

### Report

The PDF contains the academic report and theoretical background of the project.

---

## 🛠 Technologies

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Cryptography](https://img.shields.io/badge/Cryptography-ElGamal-red)
![Hash](https://img.shields.io/badge/Hash-SHA--256-green)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey)

Main technologies:

- Python
- Tkinter
- SHA-256
- Modular Arithmetic
- ElGamal Digital Signature

---

## 🎓 Educational Purpose

This project was developed for educational purposes to demonstrate:

- Public-key cryptography
- Digital signatures
- Message integrity
- Authentication
- Modular arithmetic
- Hash functions
- ElGamal signature generation and verification

> **Note:** This implementation is intended for learning and demonstration purposes. It should not be used as a production cryptographic implementation.

---

## 👨‍💻 Author

**duongsec**

Cybersecurity / Computer Engineering

GitHub: [@duongsec](https://github.com/duongsec)

---

## 📄 License

This project is intended primarily for educational and academic use.

If you want to reuse or modify the project, please provide appropriate attribution.

---

<p align="center">
  <b>ElGamal Digital Signature — Cryptography & Information Security</b>
</p># 🔐 ElGamal Digital Signature

A Python-based implementation of the **ElGamal Digital Signature Scheme**, developed as an educational project for studying cryptography, digital signatures, and information security.

The application provides a simple graphical interface built with **Tkinter**, allowing users to generate keys, sign text files, and verify digital signatures.

---

## ✨ Features

- Generate ElGamal parameters
- Generate public and private keys
- Sign text files using the ElGamal signature algorithm
- Hash message content using SHA-256
- Generate digital signature `(r, s)`
- Save signatures to `.sig` files
- Verify digital signatures
- Detect modified message content
- Simple graphical user interface using Tkinter

---

## 🧠 ElGamal Digital Signature

The ElGamal signature scheme is based on the difficulty of the **Discrete Logarithm Problem**.

### Key Generation

Choose:

- A prime number `p`
- A generator `g`
- A private key `x`

The public key is calculated as:

```text
y = g^x mod p
```

Public key:

```text
(p, g, y)
```

Private key:

```text
x
```

---

## ✍️ Signature Generation

The message is first hashed using SHA-256:

```text
h = SHA256(message)
```

Choose a random integer `k` such that:

```text
gcd(k, p - 1) = 1
```

Then calculate:

```text
r = g^k mod p
```

and:

```text
s = k⁻¹(h - xr) mod (p - 1)
```

The resulting digital signature is:

```text
(r, s)
```

---

## ✅ Signature Verification

A signature is valid when:

```text
g^h mod p = y^r × r^s mod p
```

where:

```text
y = public key
h = hash of the message
(r, s) = digital signature
```

If the document is modified after signing, the verification process will fail.

---

## 🖥️ Application Workflow

```text
              ┌──────────────────────┐
              │     Select File      │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │    SHA-256 Hash      │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   ElGamal Signing    │
              └──────────┬───────────┘
                         │
                         ▼
                   Signature (r,s)
                         │
                         ▼
              ┌──────────────────────┐
              │ ElGamal Verification │
              └──────────┬───────────┘
                         │
                 ┌───────┴───────┐
                 ▼               ▼
              VALID           INVALID
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/duongsec/Elgamlal-signature.git
```

```bash
cd Elgamlal-signature
```

### 2. Check Python

Python 3 is required.

```bash
python --version
```

or:

```bash
python3 --version
```

### 3. Run the application

```bash
python Elgammal.py
```

On some systems:

```bash
python3 Elgammal.py
```

---

## 📂 Project Structure

```text
Elgamlal-signature/
│
├── Elgammal.py
├── Bài tập lớn ATBMTT bản cuốiii (1).pdf
└── README.md
```

### `Elgammal.py`

Main Python application containing:

- ElGamal mathematical operations
- Prime generation
- Modular exponentiation
- Key generation
- SHA-256 hashing
- Signature generation
- Signature verification
- Tkinter GUI

### Report

The PDF contains the academic report and theoretical background of the project.

---

## 🛠 Technologies

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Cryptography](https://img.shields.io/badge/Cryptography-ElGamal-red)
![Hash](https://img.shields.io/badge/Hash-SHA--256-green)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey)

Main technologies:

- Python
- Tkinter
- SHA-256
- Modular Arithmetic
- ElGamal Digital Signature

---

## 🎓 Educational Purpose

This project was developed for educational purposes to demonstrate:

- Public-key cryptography
- Digital signatures
- Message integrity
- Authentication
- Modular arithmetic
- Hash functions
- ElGamal signature generation and verification

> **Note:** This implementation is intended for learning and demonstration purposes. It should not be used as a production cryptographic implementation.

---

## 👨‍💻 Author

**duongsec**

Cybersecurity / Computer Engineering

GitHub: [@duongsec](https://github.com/duongsec)

---

## 📄 License

This project is intended primarily for educational and academic use.

If you want to reuse or modify the project, please provide appropriate attribution.

---

<p align="center">
  <b>ElGamal Digital Signature — Cryptography & Information Security</b>
</p>