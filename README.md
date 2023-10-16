# rank-1-constraint-system

## Installation

We assume that you already setup your working environment with [circom](https://docs.circom.io/getting-started/installation/#installing-circom) and [snarkjs](https://github.com/iden3/snarkjs).

Run Python test:

```bash
pnpm python:test
```

Generate the R1CS, symbol file, and `multiply4_js/`:

```bash
pnpm circuits:compile
```

Print the R1CS file:

```bash
pnpm circuits:print
```

Compute the witness. This will generate **witness.wtns** file:

```bash
pnpm circuits:compute_witness
```

Generate the witness in **JSON** format:
```bash
pnpm circuits:generate_witness
```