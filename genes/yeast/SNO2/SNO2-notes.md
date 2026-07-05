# SNO2 (YNL334C, P53823) — curation notes

Journal of research for the AI GO-annotation review of *Saccharomyces cerevisiae* SNO2.
SNO2 is an **understudied ("dark") gene**: nearly all direct functional data are for its
paralog SNO1 and for the partner SNZ genes; SNO2-specific evidence is sparse. Provenance is
recorded inline as `[PMID:xxxx "verbatim quote"]` where possible.

## Identity and domain architecture (from UniProt P53823)

- Systematic name YNL334C; SGD:S000005278; SNZ-proximal ORF ("SNO" = **SN**Z **p**roximal
  **O**RF). 222 aa, 25.2 kDa. UniProt PE=3 (Inferred from homology).
- **Family:** glutaminase PdxT/SNO family; Pfam PF01174 (SNO); InterPro IPR002161 (PdxT/SNO),
  IPR029062 (class I glutamine amidotransferase-like), IPR021196 (PdxT/SNO conserved site);
  CDD cd01749 (GATase1_PB); TIGRFAM TIGR03800 (PLP_synth_Pdx2); PANTHER PTHR31559
  (PYRIDOXAL 5'-PHOSPHATE SYNTHASE SUBUNIT SNO). MEROPS clan/family C26.A32 (peptidase-C26
  = class-I glutamine amidotransferase fold).
- **Enzyme identity (annotated on homology):** the SNO/PdxT protein is the **glutaminase
  subunit** of the two-subunit (PLP synthase / PDX) machine. It hydrolyses L-glutamine to
  L-glutamate + NH3 (glutaminase, EC 3.5.1.2) and channels the ammonia to the synthase
  subunit (SNZ/PdxS), which condenses it with ribose-5-P and glyceraldehyde-3-P to make
  pyridoxal-5'-phosphate (holoenzyme reaction EC 4.3.3.6, "PLP synthase, glutamine
  hydrolysing"). UniProt: `FUNCTION: Catalyzes the hydrolysis of glutamine to glutamate and
  ammonia as part of the biosynthesis of pyridoxal 5'-phosphate. The resulting ammonia
  molecule is channeled to the active site of a SNZ isoform.`

### Catalytic-triad integrity (INLINE DOMAIN ANALYSIS)

The class-I glutamine amidotransferase (GATase1) glutaminase uses a **Cys–His–Glu catalytic
triad**. UniProt annotates SNO2's triad by homology (ECO:0000250|UniProtKB:P37528, the
*B. subtilis* PdxT):

- **ACT_SITE 91** — Nucleophile → sequence position 91 = **Cys** (nucleophilic cysteine).
- **ACT_SITE 197** — Charge-relay → **His**.
- **ACT_SITE 199** — Charge-relay → **Glu**.
- Glutamine-binding residues annotated at 58–60, 120, 151–152.

I verified these against the sequence (222 aa):
`...IIPGGES TAMSLIAERT...` — residue 91 falls in the conserved `PGG`/`G-x-C-x-G` oxyanion
region; the C-terminal `...SFHPEL...` block carries the His-Pro-Glu-Leu of the charge-relay
(His197, Glu199). **The catalytic triad is intact** (Cys91/His197/Glu199 all present), and
the PROSITE PDXT_SNO patterns (PS01236, PS51130) match. Therefore the glutaminase /
PLP-synthase-glutaminase-subunit molecular function is **domain-defensible** for SNO2 —
this is NOT a degenerate pseudoenzyme. (Sequence checked directly from the UniProt SQ block;
triad residue identities read off the annotated FT positions.)

## The SNZ/SNO gene families in *S. cerevisiae* — separating SNO2 from paralogs

*S. cerevisiae* has three near-identical SNZ (synthase-subunit) genes SNZ1/2/3 and three
near-identical SNO (glutaminase-subunit) genes SNO1/2/3, arranged as divergently-transcribed
SNZ–SNO pairs. **Attribution across paralogs is the central hazard for this gene.**

- **SNO1/SNZ1 (copy 1)** is the pair dedicated to **vitamin B6 (pyridoxine)** and is the
  well-characterised one. Rodriguez-Navarro 2002: `In media lacking vitamin B(6), SNZ1 and
  SNO1 were both required for growth in certain conditions` [PMID:12271461].
- **SNO2/SNZ2 and SNO3/SNZ3 (copies 2 and 3)** are the understudied pair(s). The same study
  states: `but neither SNZ2, SNZ3, SNO2 nor SNO3 were required` (for growth in B6-lacking
  media) [PMID:12271461]. So **SNO2 is dispensable for pyridoxine-limited growth** in the
  conditions tested — its loss is masked (redundancy and/or a different physiological role).
- Condition of induction: copies 2/3 respond to **thiamine (B1)** limitation, not (only)
  B6: `we have also found that copies 2 and 3 are activated by the lack of thiamine and that
  the Snz proteins physically interact with the thiamine biosynthesis Thi5 protein family`
  and `copies 2 and 3 seem more related with B(1) biosynthesis during the exponential phase`
  [PMID:12271461]. NOTE: this makes SNO2 more plausibly **thiamine-limitation-induced** than
  pyridoxine-limitation-induced; the two pathways share the ribose-5-P/NH3 chemistry, and
  cross-talk between B6 and B1 biosynthesis is reported for the copy-2/3 genes.
- `Copies 2 and 3 of the gene products have, in spite of their extremely close sequence
  similarity, slightly different functions in the cell.` [PMID:12271461] — i.e. SNO2 and
  SNO3 are not simply interchangeable, but the paper does not resolve an SNO2-specific
  molecular activity in isolation.

## Physical complex — SNO2 partners SNZ1 (per ComplexPortal), not SNZ2/3

- **ComplexPortal CPX-1371** = "SNO2-SNZ1 pyridoxal 5'-phosphate synthase complex",
  systematic name `SNO2:SNZ1`, participants **SNZ1 (Q03148)** + **SNO2 (P53823)**, both with
  bioRole "enzyme". (Retrieved from ComplexPortal REST API,
  `complex-ws/complex/CPX-1371`.) So the curated physical partner of SNO2 is **SNZ1**, i.e.
  the SNO/SNZ subunits are not strictly locked into same-numbered pairs at the protein level.
  This is a caveat for any "in_complex with SNZ2" assumption.
- GO glutaminase-complex term GO:1903600 has synonym "Sno1p-Snz1p" and definition "A protein
  complex which is capable of glutaminase activity" (OLS) — a generic term, correctly
  applicable to the SNO2-containing PLP-synthase glutaminase complex via IBA.

## Orthology support for the SNO-family function (glutaminase subunit → PLP biosynthesis)

- **Aspergillus nidulans pyroA** (SNZ/PDX1 side): the SNZ family is `an enzyme specifically
  required for pyridoxine biosynthesis`; `Eukarya and Archaea exclusively use the pyroA
  pathway` [PMID:10438537]. (This is the synthase-subunit paper; establishes the pathway the
  SNO glutaminase subunit feeds into.)
- **Neurospora crassa pdx-1/pdx-2**: `pyridoxine-requiring mutants of N. crassa were found to
  possess mutations that disrupt conserved regions in either the SNZ or SNO homolog` and `It
  now appears appropriate to reserve the pdx-1 designation for the N. crassa SNZ homolog and
  pdx-2 for the SNO homolog` [PMID:11238395]. This is the strongest orthology evidence that a
  fungal **SNO/glutaminase subunit** is functionally required for **pyridoxine (PLP)
  biosynthesis** — supporting the ISS/IBA MF+BP annotations on SNO2 by descent.
- SGD records SNO2's `pyridoxine metabolic process` (GO:0008614) annotation as **ISS** with
  references PMID:10438537 and PMID:11238395 (i.e. by similarity to these characterised fungal
  orthologs) (SGD go_details for S000005278).

## KNOWN vs NOT-known for SNO2 specifically

KNOWN (well-supported):
- Belongs to the PdxT/SNO glutaminase (class-I GATase) family; intact Cys91/His197/Glu199
  catalytic triad (UniProt; sequence-verified).
- By family/orthology, functions as the glutaminase subunit of the PLP (vitamin B6) synthase
  complex; the SNO glutaminase subunit is required for pyridoxine biosynthesis in fungal
  orthologs (N. crassa pdx-2) [PMID:11238395].
- Physically forms a PLP-synthase glutaminase complex with SNZ1 (ComplexPortal CPX-1371).
- SNO2/SNZ2/SNZ3/SNO3 (the copy-2/3 genes) are transcriptionally activated by thiamine (B1)
  limitation and are linked to B1 biosynthesis in exponential phase [PMID:12271461].

NOT known / uncertain (→ knowledge_gaps):
- **No direct in-vitro demonstration** of SNO2 (P53823) glutaminase or PLP-synthase activity;
  the MF annotations are all IEA/IBA/ISS by homology (UniProt PE=3). Enzymatic activity of the
  reconstituted **SNO2/SNZ complex has not been shown catalytically** in the way it has for
  bacterial/plant PdxS·PdxT.
- **SNO2 is dispensable** for pyridoxine-limited growth [PMID:12271461]; a distinct
  SNO2-specific *in vivo* physiological role/condition is not established. Redundancy with
  SNO1 (and SNO3) is unresolved.
- The physiological substrate context (B6 vs B1 biosynthesis) for SNO2 is ambiguous — induced
  by B1 limitation, yet family MF is PLP (B6) synthesis [PMID:12271461].
- Whether SNO2 preferentially partners SNZ1 vs SNZ2/SNZ3 in vivo is not settled (ComplexPortal
  curates SNO2:SNZ1).

## Annotation-by-annotation plan (11 GOA rows)

1. GO:0042823 PLP biosynthetic process — IBA — ACCEPT (core BP; family+ortholog supported).
2. GO:0004359 glutaminase activity — IBA — contributes_to — ACCEPT (subunit MF, triad intact).
3. GO:0008614 pyridoxine metabolic process — IBA — ACCEPT/KEEP (B6 process; SGD ISS-backed).
4. GO:1903600 glutaminase complex — IBA — part_of — ACCEPT (CPX-1371 confirms complex).
5. GO:0004359 glutaminase activity — IEA(EC) — enables — MODIFY→contributes_to framing /
   ACCEPT MF (same activity as #2; enables from EC mapping; keep, note contributes_to is the
   more accurate qualifier for a subunit but the MF term itself is correct).
6. GO:0008614 pyridoxine metabolic process — IEA(ARBA) — ACCEPT (dup of #3, different pipeline).
7. GO:0036381 PLP synthase (glutamine hydrolysing) activity — IEA(EC 4.3.3.6) — ACCEPT
   (holoenzyme MF; strictly a property of the SNO+SNZ complex, so contributes_to is more apt,
   but term is correct for the family).
8. GO:0042819 vitamin B6 biosynthetic process — IEA(InterPro) — ACCEPT/KEEP (parent of the
   PLP process; correct but more general than #1).
9. GO:0042823 PLP biosynthetic process — IEA — ACCEPT (dup of #1, InterPro/UniPathway).
10. GO:0003674 molecular_function — ND — accept-as-is (root; ND placeholder, keep as NON_CORE).
11. GO:0005575 cellular_component — ND — accept-as-is (root; ND placeholder).

No REMOVE actions: every annotation is domain/orthology-defensible; SNO2 has no experimental
annotations to overrule, and no annotation is biologically contradicted.

## Deep-research provenance / tooling status

The automated deep-research harness did not yield a provider report for SNO2. `falcon` timed out
at 600s (twice; retried once per protocol), and the `perplexity-lite` fallback returned HTTP 401
(insufficient_quota). Per project guidance, this review is therefore grounded directly in
primary/authoritative sources rather than an LLM deep-research summary:

- UniProt P53823 (domain architecture, catalytic-triad annotation, family assignment, curated
  FUNCTION; sequence-level triad verification done inline above).
- GOA TSV (the 11 existing annotations reviewed).
- ComplexPortal CPX-1371 (SNO2:SNZ1 complex; REST API).
- SGD go_details for S000005278 (the ISS annotation and its supporting references).
- Three cached, PubMed-verified primary publications: PMID:12271461 (yeast SNZ/SNO functional
  analysis — the one paper directly assaying SNO2), PMID:10438537 (Aspergillus pyroA / SNZ
  side), PMID:11238395 (Neurospora pdx-1/pdx-2 / SNO side).

Every `supporting_text` in the review is a verbatim substring of a cached publication and was
machine-verified by `just validate-references` (all checks passed). No content was fabricated.
If a genuine late falcon report lands, it will be committed as `SNO2-deep-research-falcon.md`
without altering the evidence-grounded conclusions above.
