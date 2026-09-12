# AT4G38370: exact selected product and prediction-donor reference

Selected Q0WW53 has 225 residues; reference Q7ZVE3 has 257 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–1 | 1–1 | 1 |
| 2–22 | 8–28 | 6 |
| 23–27 | 32–36 | 1 |
| 28–44 | 39–55 | 6 |
| 45–56 | 57–68 | 3 |
| 57–71 | 76–90 | 4 |
| 72–93 | 92–113 | 9 |
| 99–108 | 114–123 | 3 |
| 109–139 | 129–159 | 9 |
| 140–142 | 163–165 | 2 |
| 143–153 | 169–179 | 3 |
| 171–174 | 180–183 | 3 |
| 176–184 | 184–192 | 2 |
| 192–199 | 193–200 | 3 |
| 208–213 | 201–206 | 2 |
| 224–236 | 207–219 | 3 |
| 252–257 | 220–225 | 1 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Active site: Tele-phosphohistidine intermediate | 11–11 | 1 / 1 | 1 |
| Active site: Proton donor/acceptor | 89–89 | 1 / 1 | 1 |
| Site: Transition state stabilizer | 183–183 | 1 / 1 | 0 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and prediction-donor reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
