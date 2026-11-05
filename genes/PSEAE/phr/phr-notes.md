# phr (PA4660, Q9HVD2) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HVD2 --alias phr`; accession matches the worklist.
Unreviewed entry. No deep-research provider was used; PubMed search was unavailable (NCBI 500
errors) during the session. Literature: the cached seed paper (abstract in cache); I also read
the PMC full text (PMC92747) online, but quotes below are from the cached abstract only.

### Literature

- PMID:11282583 (Kim and Sundin 2001). PAO1 phr cloned and [PMID:11282583 "shown to complement a
  known phr mutation following expression in Escherichia coli SY2"] (SY2 is a phr uvrA recA
  triple mutant, per the strain table in the full text). PAO1 phr insertion mutants lose up to
  19-fold UV-B survival [PMID:11282583 "followed by a recovery period under photoreactivating
  conditions"]; complementation restores survival.
- So the gene has genetic evidence for photoreactivation (complementing a photolyase-deficient
  E. coli and light-dependent UV survival) and family evidence (class I CPD photolyase; Pfam
  DNA_photolyase plus FAD_binding_7; PROSITE DNA photolyase class 1 signatures). No purified
  enzyme study of P. aeruginosa Phr was found.

### Other seed of PTN000155970

E. coli PhrB P00914, queried live in QuickGO 2026-11-05: experimental GO:0007603
phototransduction, visible light (IDA, PMID:6325459). That term is a signalling term and is an
odd fit for a photolyase, but it is a descendant of response to light stimulus, and the node term
is true of PhrB as a light-driven repair enzyme. I have not read PMID:6325459; raised here only as
a question, no defect.

### Annotation decisions

- GO:0003904 photolyase activity (IBA, IEA): ACCEPT, core MF.
- GO:0000719 photoreactive repair (IEA, ARBA): ACCEPT, core BP (supported by the seed paper).
- GO:0071949 FAD binding (IBA): ACCEPT (cofactor).
- GO:0003677 DNA binding (IBA): MODIFY to GO:0003684 damaged DNA binding (photolyase binds
  cyclobutane pyrimidine dimer DNA).
- GO:0009650 UV protection (IMP, seed): KEEP_AS_NON_CORE (true outcome of photoreactive repair).
- GO:0009416 response to light stimulus (IBA): TOO_GENERAL (entailed by UV protection).
- Action counts: ACCEPT 4, MODIFY 1, KEEP_AS_NON_CORE 1, TOO_GENERAL 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000155970 | GO:0009416 response to light stimulus | 2 | 20 (17 taxa) | GO:0009650 UV protection, IMP, PMID:11282583 (PseudoCAP) | SOUND | phr mutants lose UV-B survival under photoreactivating light and are complemented; UV protection is_a response to UV is_a response to light stimulus. | E. coli PhrB P00914 (IDA GO:0007603 phototransduction, visible light, PMID:6325459) | Yes; the node term is true of PhrB and suits a class I photolyase clade, though PhrB's own seed term is an odd one |

No PSEUDOCAP or GO_CENTRAL defect on phr.
