# spa1 (SPBC577.14c) — S. pombe ornithine decarboxylase antizyme — review notes

> Deep-research note: the automated deep-research job
> (`scripts/deep_research_wrapper.py SCHPO spa1 falcon --fallback perplexity-lite`)
> produced no output and did not create a report file after ~25 min; it was stopped.
> This review is therefore grounded directly in the UniProt record (Q9USQ5), the GOA
> annotations, the PomBase API record, verified GO term definitions (QuickGO), and the
> cached primary literature (PMID:10775274 full text; PMID:10871270 abstract). No
> `-deep-research-*.md` file was fabricated.

## Identity (verified — NOT the mammalian SPA1 GAP)

- UniProt **Q9USQ5** (`OAZ_SCHPO`), 226 aa; gene `spa1` (synonym `spa`); systematic `SPBC577.14c`; NCBI taxon 284812.
- **RecName: Ornithine decarboxylase antizyme (ODC-Az)** [spa1-uniprot.txt lines 6–8].
- Family: ODC antizyme family (`ECO:0000305`) [spa1-uniprot.txt line 83]. Domain signatures: Pfam **PF02100 (ODC_AZ)**, InterPro **IPR002993 (ODC_AZ)** + IPR038581 (ODC_AZ_sf); Gene3D 3.40.630.60; SUPFAM SSF55729 (Acyl-CoA N-acyltransferase / NAT fold) [spa1-uniprot.txt lines 115–122]. The single antizyme domain spans essentially the whole ORF2-encoded chain.
- PANTHER family **PTHR10279 ORNITHINE DECARBOXYLASE ANTIZYME** (subfamily SF10) — the source of the IBA annotations [spa1-uniprot.txt lines 119–120].
- This is the fission-yeast antizyme, unrelated to human/mouse **SPA1 (SIPA1)** Rap GTPase-activating protein. Domain analysis (antizyme domain only; no GAP/RapGAP domain, no GTPase signature) confirms it is a bona fide OAZ-family protein, matching the name.

## Provenance for function — this gene is directly, experimentally characterized

Despite being an understudied ORF, spa1 was functionally characterized in a dedicated primary
paper:

**PMID:10775274** (Ivanov, Matsufuji, Murakami, Gesteland, Atkins, EMBO J 2000, "Conservation of
polyamine regulation by translational frameshifting from yeast to mammals"). Full text cached.
Key experimental results **on the S. pombe gene itself** (named "SPA" in the paper):

- **ODC inhibitory activity (direct assay).** Recombinant GST–SPA fusion protein expressed in
  E. coli and purified inhibits *S. pombe* ODC in vitro; GST alone does not
  [PMID:10775274 "The results (Figure 2) show that the recombinant protein can inhibit S.pombe ODC. GST alone (1 µg) does not inhibit S.pombe ODC"]. → supports **GO:0008073 ornithine decarboxylase inhibitor activity** (experimental, IDA-grade).
- **Negative regulation of polyamine biosynthesis (loss-of-function genetics).** Δspa knockouts
  accumulate putrescine, spermidine and cadaverine, most dramatically in stationary phase (up to
  ~40× putrescine)
  [PMID:10775274 "The cellular concentrations of putrescine, spermidine and cadaverine (but not spermine) were higher in the knockout strains than in wild-type cells"].
  Overexpression depletes all polyamines
  [PMID:10775274 "overexpression of SPA results in significant reduction in the intracellular levels of all four polyamines"].
  → SPA is a negative regulator of polyamine biosynthesis. The authors conclude "SPA is the
  primary regulator of ODC activity in S.pombe"
  [PMID:10775274 "This suggests that SPA is the primary regulator of ODC activity in S.pombe, not only during cell growth (short term regulation) but also in non-dividing cells (longer term regulation)"].
- **Autoregulatory +1 ribosomal frameshifting.** Expression of full-length SPA requires a
  polyamine-responsive +1 frameshift between ORF1 and ORF2
  [PMID:10775274 "This result is consistent with +1 frameshifting being crucial for expression of SPA"];
  frameshift efficiency rises with spermidine
  [PMID:10775274 "Addition of spermidine to the translation mixture to a final concentration of 1 mM results in a 3.7-fold increase in frameshifting"]
  and falls when polyamines are depleted by SPA overexpression, closing the autoregulatory loop
  [PMID:10775274 "a significant reduction (6.5-fold) in frameshifting efficiency in SPA-overproducing cells that correlates with a decrease of polyamine content"].
  UniProt records the frameshift between Ser-67 and Glu-68 [spa1-uniprot.txt lines 76–82].
- **Deletion phenotype.** Δspa is viable with no overt growth/morphology/mating defect
  [PMID:10775274 "Complete deletion of SPA (both ORFs) did not affect the viability of S.pombe cells... the growth rates, mating efficiencies and overall morphology of the knockout strains are apparently indistinguishable from those of wild-type cells"].

**PMID:10871270** (Zhu, Karplus, Grate, Coffino, Bioinformatics 2000). HMM-based identification of
the *S. pombe* antizyme homolog; abstract-only cached. Establishes the sequence/family assignment
and the conserved frameshift signal
[PMID:10871270 "The most divergent homolog detected was that of the fission yeast Schizosaccharomyces pombe... The authenticity of the S.POMBE: AZ is validated by the presence of a conserved nucleotide sequence that, in metazoa, promotes a +1 programmed ribosomal frameshift required for AZ expression"].
Note: sequence identity to metazoan antizymes is low (~10% identity / ~24% similarity per
PMID:10775274; 18–22% in the most conserved C-terminal regions per PMID:10871270).

## Mechanism by orthology (mammalian AZ1, UniProt Q02803)

UniProt propagates by similarity (ISS from Q02803 = rat AZ1): antizyme binds ODC monomers,
sterically blocking assembly of the active ODC homodimer, and targets ODC monomers for
ubiquitin-independent degradation by the 26S proteasome
[spa1-uniprot.txt lines 67–75 "Binds to ODC monomers, inhibiting the assembly of the functional ODC homodimer, and targets the monomers for ubiquitin-independent proteolytic destruction by the 26S proteasome"].
The Ivanov paper directly demonstrated ODC *inhibition* by SPA but did NOT test the
degradation-targeting or monomer-binding mechanism in S. pombe — that specific mechanistic step
is inferred from the mammalian ortholog, not shown for spa1.

## Localization — KNOWN vs NOT known

- **No experimental localization exists for spa1.** PomBase curated CC is only **GO:0005829
  cytosol**, and it derives from **GO_REF:0000051 (S. pombe keyword mapping / NAS)** — an
  inference from the antizyme keyword, not from microscopy (verified via PomBase API: the CC
  annotation for SPBC577.14c cites GO_REF:0000051).
- The GOA **nucleus (GO:0005634)** and **cytoplasm (GO:0005737)** annotations are **IBA
  (GO_REF:0000033)**, propagated from the PANTHER antizyme tree (mammalian AZ1/AZ2 shuttle between
  cytoplasm and nucleus). Neither is experimentally supported in *S. pombe*.
- The Ivanov paper does not report where SPA acts in the cell.

## Biological role and phenotypes (context; not GO-review targets)

- Core role: feedback control of intracellular polyamine (putrescine/spermidine) levels by
  inhibiting ODC (the rate-limiting biosynthetic enzyme), sensed via polyamine-dependent
  frameshifting. spa1 appears to be the principal negative regulator of ODC in S. pombe.
- PomBase records many single-locus deletion phenotypes from high-throughput screens (verified via
  PomBase API): viable vegetative population (FYPO:0002060; PMID:20473289, PMID:23697806),
  loss of viability in stationary phase (FYPO:0000245; PMID:34250083), sensitivity to hydroxyurea
  (FYPO:0000088; PMID:23173672), tert-butyl hydroperoxide (FYPO:0000797), NaCl (FYPO:0005889), and
  others (mostly PMID:37787768). These are consistent with polyamine dysregulation having
  pleiotropic, condition-dependent effects but do not by themselves define new GO functions.

## Annotation-review plan

| Term | Aspect | Ev | Ref | Planned action | Rationale |
|---|---|---|---|---|---|
| GO:0008073 ornithine decarboxylase inhibitor activity | MF | IBA | GO_REF:0000033 | ACCEPT (core) | Correct; also directly demonstrated in PMID:10775274 |
| GO:0008073 ornithine decarboxylase inhibitor activity | MF | IEA | GO_REF:0000002 (InterPro IPR002993) | ACCEPT (core) | Same term, domain-supported; redundant but correct |
| GO:1901305 negative regulation of spermidine biosynthetic process | BP | NAS | GO_REF:0000051 | KEEP_AS_NON_CORE (or MODIFY) | Real (Δspa raises spermidine) but overly specific; broader "negative regulation of polyamine biosynthetic process" (GO:0170066, which UniProt/PomBase now use as TAS) better captures the function |
| GO:0005829 cytosol | CC | NAS | GO_REF:0000051 | KEEP_AS_NON_CORE | Plausible but keyword-inferred, no experimental localization |
| GO:0005634 nucleus | CC | IBA | GO_REF:0000033 | MARK_AS_OVER_ANNOTATED / REMOVE | Propagated from mammalian AZ nuclear shuttling; no evidence in S. pombe |
| GO:0005737 cytoplasm | CC | IBA | GO_REF:0000033 | KEEP_AS_NON_CORE | Broad, consistent with cytosolic action; uninformative but not wrong |

Note UniProt DR lines show PomBase now curates **GO:0170066 negative regulation of polyamine
biosynthetic process (TAS)** [spa1-uniprot.txt line 114], the more appropriate parent of the
GOA GO:1901305 spermidine-specific term.

## Knowledge gaps (for the review)

- **Localization is unknown** (CC-dark): no microscopy has placed spa1 in a compartment; all CC
  annotations are inference/propagation.
- **Mechanism in S. pombe** (residual sub-gap): whether spa1 targets S. pombe ODC for
  ubiquitin-independent proteasomal degradation (as mammalian AZ1 does) vs. only steric
  inhibition of ODC dimerization is not established in fission yeast; only ODC inhibition was
  assayed.
- **Physiological role of polyamine feedback** (biology): why the antizyme frameshift circuit is
  so deeply conserved yet dispensable for growth is explicitly unresolved by the authors
  [PMID:10775274 "It is not obvious why this very special mechanism is so exquisitely preserved over vast evolutionary time. Perhaps there is another whole aspect to the system that our experiments do not yet detect"].
- **Second target (polyamine transporter)?** In mammals AZ also inhibits the polyamine
  transporter; the Ivanov paper raised but did not resolve whether SPA does so in S. pombe
  [PMID:10775274 "maybe SPA inhibits not only ODC but also the polyamine transporter. Further experiments will help to distinguish between these two models"].
