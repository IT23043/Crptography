# Number Theory and Cryptography Workshop

**Name:** Anirban Rahi  
**ID:** IT323043

**Collab:** [**https://colab.research.google.com/drive/19v74nUcmaaBYavGYyoZfPaE4CczdwyKs**](https://colab.research.google.com/drive/19v74nUcmaaBYavGYyoZfPaE4CczdwyKs)

## 1\. Euclidean Algorithm & Modular Inverse

### Concept

The Euclidean algorithm finds the Greatest Common Divisor (GCD) of two numbers. The **Extended Euclidean Algorithm** goes further: it finds integers $x$ and $y$ such that:

$$a \\cdot x + b \\cdot y = \\gcd(a, b)$$

This is essential in cryptography to compute the **modular multiplicative inverse** $a^{-1} \\pmod m$, which is needed to decrypt messages in ciphers like Affine and RSA.

## 2\. Caesar Cipher (Symmetric Encryption)

### Concept

Caesar cipher is a classical substitution cipher where each letter in the plaintext is shifted by a fixed number of positions $k$ down the alphabet.

- **Encryption formula:**  
  $$C = (P + k) \\pmod{26}$$
- **Decryption formula:**  
  $$P = (C - k) \\pmod{26}$$

---

## 3\. RSA Public-Key Cryptosystem

### Concept

RSA is an asymmetric cipher used everywhere on the internet (HTTPS, SSH). It relies on the practical difficulty of factoring the product of two large prime numbers.

**Steps:**

1.  Choose two prime numbers $p$ and $q$.
2.  Compute modulus $n = p \\times q$.
3.  Compute Euler's totient: $\\phi(n) = (p - 1)(q - 1)$.
4.  Choose public exponent $e$ such that $\\gcd(e, \\phi(n)) = 1$.
5.  Compute private key $d$ such that $d \\cdot e \\equiv 1 \\pmod{\\phi(n)}$.
6.  **Encryption:** $c = m^e \\pmod n$
7.  **Decryption:** $m = c^d \\pmod n$
