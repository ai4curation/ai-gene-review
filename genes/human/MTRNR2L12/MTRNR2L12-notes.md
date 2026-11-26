# MTRNR2L12 curation notes

Journal for the review of MTRNR2L12 (nuclear humanin-like locus). Written 2026-10-04.
Written as a sibling of the completed MTRNR2L1-MTRNR2L7 reviews; the shared family background is
kept consistent with those notes (and is summarised at the end of this file).

## MTRNR2L12 (P0DMP1, humanin-like 12, HN12) - locus-specific notes

- HGNC:37169, `MT-RNR2 like 12 (pseudogene)`, locus_type `pseudogene`, 3q11.2 (REST lookup at
  rest.genenames.org, 2026-10-04). GRCh37 position chr3:96336030-96337067 [PMID:31753007].
  UniProt P0DMP1 is **PE3, "Inferred from homology"**.
- 24 aa `MAPRGFSCLLLSTSEIDLPVKRRA`; **23/24 vs humanin** `MAPRGFSCLLLLTSEIDLPVKRRA` - the single
  difference is Leu12->Ser. This is the closest of the thirteen nuclear copies to humanin, and its
  sequence is **identical to that of MTRNR2L8** (both computed in this session from the UniProt SQ
  records). All of the humanin determinants are intact: Pro3, Ser7, Cys8, Leu9-Leu11, Thr13, Ser14,
  and both secretion segments Leu9-Leu11 and Pro19-Val20.
- Leu12 is a position where humanin Leu12->Ala abolishes neuroprotective activity
  (file:human/MT-RNR2__Q8IVG9/MT-RNR2__Q8IVG9-uniprot.txt), but synthetic HN5 carries the same
  Leu12->Ser and is still cytoprotective [PMID:19477263], so this is a caution, not a refutation -
  the same reading as for MTRNR2L1.
- The Down-syndrome paper notes a coding polymorphism that would erase even that one difference
  [PMID:25720405 "there is a polymorphic site (rs6484338) within MTRNR2L12, predicted to cause the
  Ser12Leu amino acid exchange, which in turn results in the production of a peptide sequence
  identical to mitochondrial humanin"].
- **GOA inconsistency worth recording.** MTRNR2L12 has only four rows (extracellular and cytoplasm,
  each IEA + ISS). It carries **no IBA rows**, while MTRNR2L8 - whose peptide sequence is identical -
  carries both `GO:0048019` and `GO:1900118` from PANTHER:PTN002141596, as do L11 and L13, which are
  far more diverged (verified from the per-gene GOA files in this repository). The difference tracks
  PANTHER subfamily/node membership, not sequence: UniProt lists L12 under PTHR33895:SF5 (as L8 does),
  while L11 and L13 have their own subfamilies SF16 and SF17. So the family's IBA coverage is
  inconsistent in a way visible from the alignment alone. This is a defect of coverage, not a reason
  to add the terms here: the right fix is to restrict the node, not to extend it (see the shared
  background below).

### Literature: the most-cited of the thirteen loci, and why that is misleading

A PubMed search for `"MTRNR2L12"` (E-utilities, 2026-10-04) returns 15 records - far more than any
other nuclear humanin-like locus (L11 returns 0, L13 returns 2). Nearly all are transcriptomic:
the gene surfaces as a differentially expressed transcript, a co-expression hub, or a lncRNA in
studies of periodontitis, nasal polyps, narcolepsy CSF, focal cortical dysplasia, PM2.5 exposure,
liver-cancer extracellular vesicles, and so on. Two are worth reading for this review.

1. **PMID:25720405** (J Alzheimers Dis 2015), the one paper named after the locus. Microarray plus
   RQ-PCR in blood mononuclear cells of 48 adults with Down syndrome; MTRNR2L12 was the single gene
   distinguishing younger severely-affected from older unaffected participants
   [PMID:25720405 "A validation procedure with SYBR Green chemistry confirmed the expression
   difference discussed above"]. Important caveats:
   - This is **transcript** evidence in blood, in a small sample, offered as a candidate biomarker.
   - It designed its own primers from ENST00000600213, acknowledging that no commercial assay
     exists; locus specificity against the other twelve near-identical copies and against the
     mitochondrial rRNA is not demonstrated in the paper.
   - It asserts, with **no citation**, that a peptide exists
     [PMID:25720405 "Since the presence of the MTRNR2L12 peptide has been confirmed in brain tissue,
     it can be assumed that MTRNR2L12 exerts effects similar to those reported for humanin."].
     I could find no primary report of an HN12 peptide; this sentence should not be propagated, and
     I flag it in `reference_review` rather than using it as support for anything.
2. **PMID:35421970** (BMC Med Genomics 2022), platelet co-expression in COVID-19. MTRNR2L12 is a hub
   gene of the magenta module
   [PMID:35421970 "Regarding the magenta module, MT-ND1, MT-ND5, and MTRNR2L12 were selected as hub
   genes."], and the paper itself notes
   [PMID:35421970 "MTRNR2L12 is a paralog of the protein coding gene MTRNR2L8, and both are expressed
   in platelets"].
   The company it keeps is the tell: MT-ND1 and MT-ND5 are mitochondrially encoded. A nuclear copy of
   a mitochondrial rRNA segment clustering with mitochondrial transcripts in a short-read
   co-expression analysis is exactly what read mis-assignment looks like. This does not prove
   mis-assignment, but it means the module membership cannot be read as evidence about a nuclear gene
   product, and the same caution applies to the other transcriptomic hits above.
- Genetics: the CAD lookup included the L12 region (rs78077066 P = 0.015, rs12106821 P = 0.52), and
  [PMID:31753007 "None of the found associations were statistically significant after correction for
  multiple testing."]
- Net: despite being the most frequently *named* locus of the thirteen, MTRNR2L12 has no
  peptide-level evidence, no activity assay, no interaction data, and no locus-resolved
  quantification that excludes the other copies. Expression-level notoriety is not functional
  evidence.
- Actions: 4 MARK_AS_OVER_ANNOTATED (extracellular IEA + ISS, cytoplasm IEA + ISS). The extracellular
  rows are *not* removed here, unlike L3/L4/L7/L11/L13, because L12 retains both humanin secretion
  segments intact - the same reasoning as MTRNR2L1. `core_functions: []`, no NEW terms.

## The family, and why these reviews look alike

Humanin is a 24-residue peptide encoded by a small open reading frame inside the mitochondrial 16S
rRNA gene MT-RNR2, and it is the member of this family with all the experimental evidence:
cytoprotection, BAX/BID/BIM binding, FPRL1/FPR2 engagement, the CNTFR-alpha/WSX-1/gp130 receptor
complex. Bodzioch et al. 2009 (PMID:19477263, PubMed-verified, Genomics 94:247-256) found thirteen
MT-RNR2-like sequences in the nuclear genome whose reading frames would encode humanin-like peptides
HN1-HN13
[PMID:19477263 "We provide bioinformatic and expression data suggesting the existence of 13
MT-RNR2-like nuclear loci predicted to maintain the open reading frames of 15 distinct full-length
HN-like peptides."]
and showed that at least ten are transcribed and respond to staurosporine and beta-carotene
[PMID:19477263 "At least ten of these nuclear genes are expressed in human tissues, and respond to
staurosporine (STS) and beta-carotene."].
The later lookup paper gives the range as
[PMID:31753007 "The study showed that MTRNR2L1–MTRNR2L10 were expressed variably in most human
tissues"], so L11-L13 are the three loci left out - consistent with their PE3 status, and in tension
with the volume of transcriptomic literature naming L12.

UniProt states the position in a CAUTION line on each entry: the active peptide is the product of the
mitochondrial gene, and whether any nuclear locus makes a physiologically active peptide is open. A
2022 review restates it
[PMID:35372353 "It is predicted that these various isoforms might contribute to differential
neuroprotective effects and receptor binding, but their individual roles remain to be investigated."].
HGNC classes all thirteen as pseudogenes.

### What the GOA rows on MTRNR2L12 assert

| term | code | reference | WITH/FROM |
|---|---|---|---|
| GO:0005576 extracellular region | IEA | GO_REF:0000044 | UniProtKB-SubCell:SL-0243 |
| GO:0005576 extracellular region | ISS | GO_REF:0000024 | UniProtKB:Q8IVG9 |
| GO:0005737 cytoplasm | IEA | GO_REF:0000044 | UniProtKB-SubCell:SL-0086 |
| GO:0005737 cytoplasm | ISS | GO_REF:0000024 | UniProtKB:Q8IVG9 |

Both ISS rows name humanin (UniProtKB:Q8IVG9) as donor, and humanin's own extracellular and cytoplasm
annotations are IDA/EXP, so the donor side is sound. Both IEA rows map UniProt's own
`SUBCELLULAR LOCATION` lines, which are themselves `ECO:0000250|UniProtKB:Q8IVG9` - so IEA and ISS
state the same humanin claim twice over. Nothing on this gene traces to an observation made on
MTRNR2L12.

### Residues

Humanin has an unusually complete mutagenesis map (UniProt Q8IVG9). Single substitutions that
*abolish* neuroprotective activity: Pro3, Ser7, Cys8, Leu9, Leu12, Thr13, Ser14 (S14->A,R,W,E,P);
secretion requires Leu9-Leu11 and Pro19-Val20. HN12 differs from humanin at Leu12 only, and the
synthetic HN5 peptide carrying the same Leu12->Ser is cytoprotective [PMID:19477263]. So for this
locus sequence divergence is not the argument - the missing link is simply that no peptide has ever
been shown to exist.

### Methodological caution

RNA-seq and microarray signals over a nuclear copy that is 23/24 identical to a peptide encoded
inside an extremely abundant mitochondrial rRNA are not locus-resolved unless the analysis
demonstrates it, and serum ELISAs for "humanin-like" species have not been shown to be
locus-specific for any member of this family. No antibody- or short-read-based measurement is used
here as evidence that MTRNR2L12 makes a peptide.
