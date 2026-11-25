# pslB (PA2232, Q9I1N7) review notes

The cited paper has full text in the cache (`full_text_available: true`, PMC4409829), so both
PseudoCAP rows can be checked against what the authors actually report, not only against the
abstract.

## The IMP names the wrong reaction

GOA carries `GO:0050089` **mannose isomerase activity** by IMP from PMID:19659934. That term is
defined in GO as "D-mannose = D-fructose" (EC 5.3.1.7) — the free sugar. The paper never claims
that reaction. It calls PslB a **PMI/GMP** throughout:

- [PMID:19659934 "Deletion of rmd may result in accumulation of GDP-d-Man that inhibits the
  phosphomannose isomerase (PMI) activity of PslB, resulting in a reduction in Psl (Lee et al."]
- [PMID:19659934 "The lack of a Psl phenotype in the wbpW mutant demonstrates that PslB does not
  require WbpW for Psl synthesis and is capable of functioning as a PMI/GMP, in agreement with
  recently published PslB enzymatic data (Lee et al."]

Phosphomannose isomerase is **mannose-6-phosphate** isomerase, EC 5.3.1.8, `GO:0004476` — the
phosphorylated substrate. The two differ by a phosphate, and the entry's own `CC CATALYTIC
ACTIVITY` gives the right one: "D-mannose 6-phosphate = D-fructose 6-phosphate". `GO:0004476` is
already on the gene as an IEA from the EC mapping, so the MODIFY target is a term the review
already accepts.

This is the EC-class trap the project warns about, one class apart rather than one digit: a term
in a different EC sub-subclass names a different reaction, not a broader one.

## The IDA rests on a phenotype the paper reports as absent

`GO:0044010` single-species biofilm formation is annotated IDA from the same paper. The paper
says the opposite about the single mutant:

- [PMID:19659934 "Interestingly, deletion of pslB, pslM, pslN, or pslO did not result in an
  observable attachment defect compared to PAO1."]
- [PMID:19659934 "Lastly, the pslB mutant showed abundant attachment both at the air-liquid
  interface and submerged regions of the coverslip (Fig."]

The attachment and Psl-production defects appear only in the **double** mutant with *wbpW*:

- [PMID:19659934 "An ELISA quantifying Psl production by these same strains revealed a complete
  loss of Psl in extracts from the pslB wbpW double mutant but no significant decrease for
  extracts derived from the wbpW mutant (Fig."]
- [PMID:19659934 "Together, the attachment, immunoblot, and ELISA data confirm that, in a pslB
  mutant, WbpW is the PMI/GMP responsible for generating the GDP-d-Man essential in the
  production of Psl."]

So what the paper establishes is **redundancy**: either PslB or WbpW can supply the GDP-mannose
that Psl and A-band LPS need, and losing one is invisible because the other covers it. That is a
real and interesting result, but it is not a demonstration that this gene is involved in biofilm
formation, and the data behind it are genetic rather than direct, so the IDA code is doubly
questionable. Reported as a `CHECK` rather than asserted as a confirmed defect: the curator may
have drawn on the double-mutant figures deliberately.

The same redundancy runs in the other direction for A-band LPS:
[PMID:19659934 "9A), indicating that A-band LPS synthesis requires the redundant PMI/GMP activity
of either PslB or WbpW to generate product."] — which is a useful reminder that PslB is not a
Psl-specific enzyme, despite its name and operon.

## What the gene is

A bifunctional mannose-6-phosphate isomerase / mannose-1-phosphate guanylyltransferase of the
type 2 PMI family, i.e. the same enzyme class as AlgA, which is what the ARBA-derived RecName on
the entry calls it. It carries out two consecutive steps of GDP-mannose biosynthesis:
fructose-6-phosphate ⇌ mannose-6-phosphate, and (after phosphomannomutase) mannose-1-phosphate +
GTP → GDP-mannose.

Its supporting evidence is `TIGR01479; GMP_PMI`, a curated NCBIfam model named for exactly this
bifunctional pair, plus the InterPro entry `IPR006375
Man1P_GuaTrfase/Man6P_Isoase`. The `CC` blocks on the entry are ARBA-derived and are not used as
support here; the NCBIfam and InterPro matches, the IBA, and the paper's own PMI/GMP statements
are.

Note the direction of the review's conclusions: the two IEA/IBA function rows are correct and the
two PseudoCAP rows derived from the paper are the ones with problems — the opposite of the usual
pattern, and worth recording as such.
