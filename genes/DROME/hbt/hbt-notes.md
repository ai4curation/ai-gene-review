# hbt (Q9VK03): evidence and ProtNLM claim review

Headbutt is a 451-residue Rost-family protein with six predicted transmembrane helices. It is an integral membrane protein with an unresolved molecular activity and biological role for this isoform.

Exact input: [Q9VK03](https://www.uniprot.org/uniprotkb/Q9VK03/entry), 451 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [hbt-predictions-source.json](hbt-predictions-source.json). Source features: [hbt-uniprot.txt](hbt-uniprot.txt), with an exact extraction in [hbt-sequence-evidence.json](hbt-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR049352; Rost.
FT   TRANSMEM        40..63
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   TRANSMEM        75..98
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   TRANSMEM        123..145
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   TRANSMEM        157..177
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   TRANSMEM        184..205
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   TRANSMEM        228..250
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Uncharacterized protein | UNC | The nonspecific name is consistent with unresolved molecular activity but is not a testable prediction. Rost-family membership does not itself establish a transported substrate. |
| Location | Membrane (SL-0162) | CNN | Six predicted membrane-spanning helices strongly support the broad membrane claim already present as a curated ISS annotation. This does not specify a membrane or transport mechanism. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0003674 molecular_function (ND): **ACCEPT**. Six membrane-spanning segments and a Rost-family domain do not establish a transporter substrate or catalytic activity.
- GO:0008150 biological_process (ND): **ACCEPT**. The exact Headbutt isoform lacks a sufficiently grounded physiological function in the retrieved evidence.
- GO:0016020 membrane (ISS): **ACCEPT**. The six Phobius transmembrane segments between residues 40 and 250 independently support the existing ISS membrane annotation. The membrane identity and transport activity are unresolved.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `hbt-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this section.

### Identity: Q9VK03 is an isoform, not the canonical product

- hbt (FBgn0264308, CG43778) has four unreviewed UniProt products: A0A6H2EJZ8 (isoform E, 1003 aa;
  UniProt gene-centric canonical), M9PFU0 (isoform A, 963 aa), Q9VK01 (isoform C, 663 aa) and Q9VK03
  (isoform D, 451 aa, benchmark). No Swiss-Prot entry exists.
- Q9VK03 residues 1-451 are identical to isoform E 513-963 (and isoform A 513-963): an N-terminally
  truncated product lacking E's first 512 residues (predicted coiled coils, disordered low-complexity
  segment) and E's last 40 residues. It keeps the complete Rost (PF21534) region and all six
  predicted helices (D 40-250 = E 552-762) [file:DROME/hbt/hbt-bioinformatics/RESULTS.md].
- Current QuickGO: the IMP to GO:0051931 regulation of sensory perception (PMID:32761438) and an IBA
  to membrane (PTN001387085, with FB:FBgn0011705) sit on A0A6H2EJZ8 only. Q9VK03, Q9VK01 and M9PFU0
  still carry the 2012 ND MF/BP rows and the membrane ISS.

### Literature

- The falcon deep-research report built its "primary study" on Tanaka et al. 2014 (PMID:24671768).
  That paper is about Mabiki (Mabi), a caspase-independent cell death regulator; its cached full text
  never mentions hbt, headbutt or CG43778. The cell-death/pattern-repair framing in the deep research
  is therefore a mis-citation and was not used.
- The real hbt paper is Zhang, Li, Liu & Zhang 2020, Neurosci Bull (PMID:32761438, PMC7475148), a
  Letter. The publisher blocks XML download, so the cache is abstract-only; I read the PMC HTML. Key
  verbatim excerpts:
  - "Among all these hits, a previously uncharacterized gene, CG43778, was of particular interest
    because its mutant had the most severe touch defect among all the genes tested and its
    molecular/cellular function had not yet been studied (Fig. 2 B). We named this gene headbutt (hbt)."
  - "The back-crossed homozygous knockout of HBT and the trans-heterozygotes of MIMIC and knockout
    showed a touch response defect as severe as the MIMIC line (Fig. 2 D)"
  - "HBT is required for larval TO mechanosensation. hbt mutant larval chordotonal neurons in the TO
    show a significantly reduced Ca 2+ response"
  - "In the DO, HBT proteins wrap the dendrites of es cells"; "In the TO, HBT proteins wrap glial cells
    of chordotonal neurons"; GFP knock-in at the C-terminus; prospero-positive sheath cells.
  - "we identified the novel gene headbutt (hbt) that functions in the cells surrounding the DO and TO
    to regulate the neuronal mechanosensitivity"
  These cannot be quoted in the YAML (cache abstract-only); the review quotes the title and records
  the findings as statements.
- Family: Rolling stone (O44252, PTHR12242:SF46) is a membrane-fraction-enriched protein required for
  myoblast fusion [PMID:9230076 "the deduced protein sequence is in accordance with a transmembrane
  protein, which agrees with the enrichment of Rost in the membrane fraction of Drosophila embryos"].
  hbt is SF49, a different subfamily: the myoblast-fusion role is not transferred.
- Parsons et al. 2016 [PMID:27018888 "uncovered a distinct set of uncharacterized AIG1/ADTRP-like
  proteins that possess the conserved Thr and His residues ... (Panther family PTHR12242; members in
  insects, plants, protozoa, and other non-vertebrates)"]. This is an HHpred-level hint at a Thr/His
  hydrolase mechanism. My pairwise SW of Q9VK03 vs human AIG1 was not significant (22% over 182 aa,
  score 43), so I make no inference about residues or activity.

### Decisions

- GO:0003674 ND: ACCEPT. No activity is known.
- GO:0008150 ND: MODIFY -> GO:0051931 regulation of sensory perception. Superseded by the 2020 IMP that
  FlyBase put on the canonical isoform; the knockout removes all isoforms and D carries the conserved
  core. Regulation (not sensory perception of touch itself) fits expression in sheath/glial cells
  rather than in the neurons.
- GO:0016020 membrane ISS (from rost): ACCEPT. Family-level property, six TM helices, PAINT agrees.
- Core function: membrane protein of sensory sheath cells/glia regulating larval touch sensitivity; MF
  unknown (knowledge gap).

### Relatives and family

- Relative to review next: same gene canonical product, hbt isoform E A0A6H2EJZ8
  (folder would be genes/DROME/hbt__A0A6H2EJZ8, since genes/DROME/hbt is keyed to Q9VK03). No review
  exists. Rost (O44252) has no review in the repo either.
- interpro/panther/PTHR12242/PTHR12242-review.yaml: agrees hbt is SF49 and rost SF46. Two issues: the
  SF49 subfamily description is a verbatim copy of the family coherence text rather than a description
  of SF49, and its only representative member is the truncated isoform D (Q9VK03) rather than the
  canonical A0A6H2EJZ8. It does not mention the Zhang 2020 mechanosensation result or the
  AIG1/ADTRP-like observation of PMID:27018888.
- Modules: none found for hbt or Rost-family proteins (rost appears in no module; the myoblast-fusion
  modules such as modules/dmel_irm_myoblast_adhesion.yaml do not include it and are unrelated to hbt).
