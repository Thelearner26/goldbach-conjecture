# Goldbach Conjecture — Computational Exploration

## What Is This?
A Python project computationally exploring the Goldbach Conjecture — 
every even number greater than 2 is the sum of two primes. Proposed 
by Christian Goldbach in a letter to Euler in 1742, verified to 
4×10¹⁸, never proved.

## The Mathematics

### The Sieve of Eratosthenes
The foundation of the project — generates all primes up to n 
efficiently. Stops at √n because every composite number m has a 
factor below √m ≤ √n — a consequence of the Fundamental Theorem 
of Arithmetic, the same theorem making RSA encryption secure.

### Goldbach Verification
For every even number, finds prime pairs summing to it using O(1) 
set lookups. If the failure message ever triggers — Goldbach is 
disproved.

### The Goldbach Comet
Plotting representation counts against even numbers produces the 
Goldbach Comet — multiple structured diagonal bands emerging from 
an unproved conjecture. The band structure corresponds to even 
numbers with different prime factor structures but remains only 
partially explained mathematically.

### Hardy-Ramanujan Prediction
Hardy and Ramanujan derived an analytical estimate for Goldbach 
representations in the 1920s using the circle method — no computer, 
pure analytical genius. Their prediction traces through the centre 
of the computational comet a century later.

## Versions

### V1 — Sieve + Verification
Builds the Sieve of Eratosthenes and verifies Goldbach for every 
even number up to n. Uses set conversion for O(1) prime lookups.

### V2 — Counting Representations  
Counts ALL prime pair representations for each even number — 
the raw data powering the comet visualisation.

### V3 — The Goldbach Comet
Plots representation counts as a scatter plot — the Goldbach Comet 
emerges naturally from the data without being programmed to appear.

## Libraries Used
- matplotlib — visualisation

## What I Learned
- Sieve of Eratosthenes and why it stops at √n
- Fundamental Theorem of Arithmetic in code
- Set data structure for O(1) lookups vs O(n) list search
- Separation of concerns — sieve, counting, plotting as independent functions
- How CS reveals mathematical structure pure proof hasn't explained

## Connections
- **Riemann Hypothesis** — prime distribution controls Goldbach representation counts
- **RSA Encryption** — same unique prime factorisation underlies both
- **Gödel** — verified for 4×10¹⁸ yet unproved — could it be unprovable?
- **Ramanujan** — circle method connects to pi convergence project

## Resources
- Numberphile — Goldbach Conjecture
- Numberphile — The Obviously True Theorem No One Can Prove
