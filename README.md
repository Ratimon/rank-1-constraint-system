# rank-1-constraint-system

## Installation

We assume that you already setup your working environment with [circom](https://docs.circom.io/getting-started/installation/#installing-circom) and [snarkjs](https://github.com/iden3/snarkjs).

```bash
poetry run pytest tests/test_r1cs.py
```

```bash
cd circuits
circom multiply4.circom --r1cs --sym --wasm
```

This will generate the R1CS, symbol file, and `multiply4_js/`


```bash
pnpm circuits:print
```

