# Afap1l2 (mouse, Q5DTU0) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative of human AFAP1L2 (Q8N4X5). No ProtNLM2 files or prediction-evidence folders were opened or used.

### Deep research
`just deep-research-falcon mouse Afap1l2 --fallback perplexity-lite` failed: falcon returned "Failed to authenticate" and the perplexity fallback returned HTTP 401 (insufficient quota). No deep-research file exists; the review is based on the cached primary literature listed below, read directly.

### Evolutionary grounding
- UniProt places mouse Afap1l2 in PANTHER PTHR14338:SF4 (AFAP1L2), the same subfamily as human AFAP1L2; AFAP1 and AFAP1L1 are separate subfamilies. [file:mouse/Afap1l2/Afap1l2-uniprot.txt "PANTHER; PTHR14338:SF4; ACTIN FILAMENT-ASSOCIATED PROTEIN 1-LIKE 2; 1."]
- PAINT (PTHR14338-paint.tsv): node PTN002682769 (Euteleostomi) carries PTK activator activity, inflammatory response, regulation of mitotic cell cycle, positive regulation of EGFR signaling and positive regulation of transcription, all seeded only by human Q8N4X5; cytosol from PTN001023816. Actin filament (GO:0005884) and its scaffold/regulation terms sit on PTN002682780, seeded by rat/mouse AFAP1, and were not propagated to the AFAP1L2 clade. So actin binding of Afap1l2 cannot be taken from AFAP1; it rests on the direct mouse assays below.
- Bioinformatics (Afap1l2-bioinformatics/RESULTS.md): human vs mouse 83.5% identity; the p85-docking YxxM motif around Tyr54 is identical; the Yamanaka 2016 construct NM_001177796 = NP_001171267 = UniProt isoform Q5DTU0-2 (843 aa), and its actin-binding residues 830-840 map to canonical 812-822.

### Mouse experimental evidence (established in this species)
- F-actin binding and crosslinking, mouse construct [PMID:27462298 "this region is directly bound to F-actin in vitro"; "In summary, our data clearly demonstrated that PI3KAP/XB130 crosslinked actin filaments."; "we did not find any colocalization with N-terminal region of PI3KAP/XB130 using a mouse construct"]. Overexpression also enhanced dextran uptake in HEK293 cells; this overexpression-only endocytosis result was not annotated.
- Apical plasma membrane of thyrocytes; Xb130-/- congenital hypothyroidism with disorganized apical membranes [PMID:34470464 "XB130 was found mainly on the apical membrane of thyroid follicles."; "Thus, XB130 deficiency results in disorganization of the apical structure of thyrocytes."]. The phenotype (reduced Tg iodination/release, delayed folliculogenesis, hypothyroidism) is downstream; thyroid hormone generation and folliculogenesis were deliberately NOT added as process terms (Afap1l2 does none of the hormone-generation chemistry; TPO/DUOX do).
- PTPRZ substrate and PI3K-AKT coupling in OL1 cells [PMID:30667096 "PTPRZ dephosphorylated AFAP1L2 at tyrosine residues in vitro and in HEK293T cells."]. Abstract-only in cache. OL1 species: the Noda-lab OL1 line was established from p53-knockout mouse brain (web search 2026-10-20; scicrunch/PMC pages describing OL1); a distinct rat line is named OL-1. Oligodendrocyte differentiation is a downstream phenotype, not annotated.

### Inferred from orthologs only (not tested on the mouse protein)
- c-Src binding/activation, SH3 (Tks5) binding, SH2 binding (human PMID:17412687, PMID:26446840, PMID:19060924; rat PMID:22496359).
- Cytosol/cytoplasm (human).

### Decisions
- Protein binding IPI Pik3r1 -> MODIFY to GO:0036312; IPI Ptprz1 -> REMOVE (enzyme-substrate contact).
- Plasma membrane ISO -> MODIFY to apical plasma membrane (mouse IDA).
- Positive regulation of IL-8 production -> REMOVE: mouse has no IL8 gene [PMID:10028286 "this gene is absent in the rat and the mouse"].
- Inflammatory response and positive regulation of transcription -> MARK_AS_OVER_ANNOTATED; EGFR signaling, mitotic cell cycle, IL-6 -> KEEP_AS_NON_CORE (consistent with the human review).
- NEW: actin filament binding (IDA), actin crosslink formation (IDA), positive regulation of PI3K/AKT signal transduction (IMP).
- Note: PMID_10095777.md was cached by mistake while looking up the IL-8 paper (wrong PMID); it is not cited.
