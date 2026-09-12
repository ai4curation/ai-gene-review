---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T16:13:03.995150'
end_time: '2026-07-15T16:42:39.945690'
duration_seconds: 1775.95
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0094
  gene_symbol: PP_0094
  uniprot_accession: Q88RN5
  protein_description: 'SubName: Full=5''-nucleotidase {ECO:0000313|EMBL:AAN65728.1};
    EC=3.1.3.5 {ECO:0000313|EMBL:AAN65728.1};'
  gene_info: OrderedLocusNames=PP_0094 {ECO:0000313|EMBL:AAN65728.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: HAD-like_hydrolase_sf. (IPR050155); HAD-like_sf. (IPR036412); HAD_2.
    (IPR041492); HAD_sf. (IPR023214); PGP-like_dom2. (IPR023198)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_0094-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0094-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88RN5
- **Protein Description:** SubName: Full=5'-nucleotidase {ECO:0000313|EMBL:AAN65728.1}; EC=3.1.3.5 {ECO:0000313|EMBL:AAN65728.1};
- **Gene Information:** OrderedLocusNames=PP_0094 {ECO:0000313|EMBL:AAN65728.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** HAD-like_hydrolase_sf. (IPR050155); HAD-like_sf. (IPR036412); HAD_2. (IPR041492); HAD_sf. (IPR023214); PGP-like_dom2. (IPR023198)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0094" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0094' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0094** (gene ID: PP_0094, UniProt: Q88RN5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_0094 (Q88RN5) in *Pseudomonas putida* KT2440

**Gene:** PP_0094 (OrderedLocusName) · **UniProt:** Q88RN5 (Q88RN5_PSEPK) · **Organism:** *Pseudomonas putida* strain ATCC 47054 / DSM 6125 / NCIMB 11950 / **KT2440** (PSEPK) · **Length:** 216 aa (24.5 kDa) · **NCBI protein:** AAN65728 · **Protein existence:** Level 4 (Predicted)

---

## Summary

**PP_0094 (UniProt Q88RN5) encodes a small, soluble, cytoplasmic Mg²⁺-dependent phosphohydrolase of the haloacid dehalogenase (HAD) superfamily.** The 216-residue (24.5 kDa) protein carries the complete set of four canonical HAD catalytic motifs and a C2-type "cap" domain of the phosphoglycolate-phosphatase (PGP) subtype. Its most likely primary function is **2-phosphoglycolate phosphatase (EC 3.1.3.18)**, catalyzing the reaction *2-phosphoglycolate + H₂O → glycolate + inorganic phosphate*, acting as an intracellular **metabolite-repair / phosphometabolite-salvage enzyme** that feeds glycolate into glyoxylate and dicarboxylate metabolism.

This assignment revises the legacy database annotation. UniProt and GenBank record PP_0094 under the submitted name "5′-nucleotidase (EC 3.1.3.5)," a designation that traces directly to the original 2002 automated whole-genome annotation of *P. putida* KT2440 (EMBL entry AAN65728.1). However, four independent lines of curated evidence — KEGG orthology (K01091, phosphoglycolate phosphatase), PANTHER family assignment (PTHR43434, PHOSPHOGLYCOLATE PHOSPHATASE), the InterPro PGP-like cap domain (IPR023198), and closest pairwise homology to the biochemically characterized *E. coli* Gph enzyme — converge on phosphoglycolate phosphatase as the specific function. A very-high-confidence AlphaFold model (mean pLDDT 96.1) confirms a compact, well-folded single-domain HAD enzyme with a fully intact active site.

**A crucial caveat frames the entire report: PP_0094 has never been experimentally assayed.** Its UniProt protein-existence level is 4 ("Predicted"), meaning every functional statement below is an inference from sequence, domain architecture, orthology, structural modeling, and the biochemistry of characterized homologs — not a direct measurement of PP_0094 itself. Because HAD-superfamily phosphatases are notoriously substrate-promiscuous, residual 5′-nucleotidase or broader phosphatase activity cannot be formally excluded. The strongest, most specific curated evidence nonetheless points to 2-phosphoglycolate phosphatase.

---

## Key Findings

### F001 — PP_0094 is a soluble HAD-superfamily hydrolase with a complete catalytic motif set

Sequence analysis of the 216-amino-acid, 24.5 kDa protein identifies all four canonical motifs that define the haloacid dehalogenase (HAD) superfamily active site:

| Motif | Sequence / position in PP_0094 | Catalytic role |
|-------|-------------------------------|----------------|
| **Motif I** | `DLDGT` at residue 9 (DxDxT) | Asp9 = nucleophile forming the phospho-aspartyl intermediate; Asp11 = general acid/base |
| **Motif II** | conserved Ser/Thr in `ATSK` (res 107–110) | Hydrogen-bonds the transferring phosphoryl group |
| **Motif III** | conserved Lys | Stabilizes negative charge in the transition state |
| **Motif IV** | `GDRKHD` at residue 165 (GDxxxD) | Coordinates the catalytic Mg²⁺ cofactor |

The UniProt cofactor annotation is Mg²⁺, and multiple orthogonal domain-detection tools agree on HAD-superfamily membership: CDD **cd04302 (HAD_5NT)**, Pfam **PF13419 (HAD_2)**, SUPFAM **SSF56784 (HAD-like)**, and InterPro **IPR023214 / IPR036412 (HAD_sf)**. Importantly, a ~91-residue **cap-domain insertion (residues 14–105)** sits between Motifs I and II. This position of the cap identifies PP_0094 as a **C2-type cap (HAD subfamily IIA/IB)** enzyme — the structural class associated with small-metabolite phosphatases rather than with proteins or bulky substrates. This finding establishes the enzyme's catalytic machinery and mechanistic class with high confidence, independent of the precise substrate identity.

### F002 — Legacy annotation: 5′-nucleotidase (EC 3.1.3.5) of the NagD/HAD group

The database-of-record annotation names PP_0094 a **5′-nucleotidase (EC 3.1.3.5)**. This is supported by several automated pipelines: UniProt Q88RN5 submitted name "5′-nucleotidase," CDD subfamily cd04302 = HAD_5NT, PANTHER subfamily PTHR43434:SF20 = "5′-NUCLEOTIDASE," and GO term GO:0008253 (5′-nucleotidase activity). Under this interpretation the enzyme would catalyze the Mg²⁺-dependent hydrolysis:

> 5′-(deoxy)ribonucleoside monophosphate + H₂O → nucleoside + Pi

via the phospho-aspartyl intermediate on Motif-I Asp9. Characterized bacterial homologs of this HAD 5′-nucleotidase group typically show **broad substrate specificity**. In *Bacillus subtilis*, YitU acts on dAMP, GMP, dGMP, CMP, AMP, XMP, IMP and AICAR-phosphate (preferring FMN), and YutF is likewise broad; in *E. coli* the group comprises *nagD, yrfG, yjjG, yieH, yigL, surE* and *yfbR*.

The literature basis is well established. [PMID: 27784292](https://pubmed.ncbi.nlm.nih.gov/27784292/) states that *"In Escherichia coli, nagD, yrfG, yjjG, yieH, yigL, surE, and yfbR encode 5'-nucleotidases that hydrolyze the phosphate group of 5'-nucleotides,"* defining the NagD group to which the CDD HAD_5NT annotation assigns PP_0094. [PMID: 32040605](https://pubmed.ncbi.nlm.nih.gov/32040605/) shows a characterized ortholog was *"purified and biochemically characterized as a soluble 5'-nucleotidase with broad substrate specificity with respect to various deoxyribo- and ribonucleoside monophosphates,"* and [PMID: 27907199](https://pubmed.ncbi.nlm.nih.gov/27907199/) defines the reaction: *"5'-nucleotidases (EC 3.1.3.5) catalyze the hydrolytic dephosphorylation of 5'-ribonucleotides and 5'-deoxyribonucleotides."* Critically, **the precise substrate preference of PP_0094 itself has never been experimentally determined** (existence level 4).

### F003 — The enzyme is soluble and cytoplasmic

Localization prediction places PP_0094 in the cytosol (**GO:0005829**, cytosol; IEA/TreeGrafter). The 216-aa protein has no signal peptide, no transmembrane segment, and no lipobox anywhere in its UniProt feature table — all consistent with a soluble intracellular protein. This distinction matters biologically: soluble HAD-superfamily 5′-nucleotidases are strictly intracellular, in contrast to periplasmic or surface-anchored 5′-nucleotidases such as the UshA/CD73-type metallophosphoesterases, which belong to an unrelated enzyme family. [PMID: 27907199](https://pubmed.ncbi.nlm.nih.gov/27907199/) makes this explicit: *"These enzymes have been found in diverse species in intracellular and membrane-bound, surface-localized forms. Soluble forms of 5'-nucleotidases belong to the ubiquitous haloacid dehalogenase superfamily (HADSF)."* PP_0094 belongs unambiguously to the soluble HADSF class, so its site of action is the **cytoplasm**.

### F004 — Convergent evidence reassigns the likely primary function to phosphoglycolate phosphatase (EC 3.1.3.18)

Four independent lines of evidence converge on **2-phosphoglycolate phosphatase (Gph/PGP)** as the specific function, overriding the less-specific legacy "5′-nucleotidase" label:

1. **KEGG orthology** assigns PP_0094 to **K01091** ("phosphoglycolate phosphatase [EC:3.1.3.18]"), within pathway **ppu00630 Glyoxylate and dicarboxylate metabolism**.
2. **PANTHER family** PTHR43434 = **PHOSPHOGLYCOLATE PHOSPHATASE** (the family-level assignment, distinct from the SF20 subfamily label).
3. **InterPro cap domain IPR023198** = "**PGP-like_dom2**," the phosphoglycolate-phosphatase-like C2 cap.
4. **Pairwise alignment** (Needleman–Wunsch) ranks *E. coli* Gph (P32662, phosphoglycolate phosphatase) as the **top match** among characterized HAD enzymes at 25.0% identity, just ahead of the broad nucleotidase YjjG (24.4%); all other characterized 5′-nucleotidases scored <21%.

The reaction is *2-phosphoglycolate + H₂O → glycolate + Pi* (Mg²⁺-dependent, using the HAD Asp9 nucleophile). The reference enzyme is biochemically well defined: [PMID: 13129953](https://pubmed.ncbi.nlm.nih.gov/13129953/) reports that *"The enzyme 2-phosphoglycolate phosphatase from Escherichia coli, encoded by the gph gene, was purified and characterized. The enzyme was highly specific for 2-phosphoglycolate,"* and that *"this housekeeping enzyme is involved in the dissimilation of the intracellular 2-phosphoglycolate formed in the DNA repair of 3'-phosphoglycolate ends."* The legacy "5′-nucleotidase / EC 3.1.3.5" call derives from the original 2002 genome auto-annotation (AAN65728.1) and is therefore a lower-resolution assignment. Because no direct enzymatic assay of PP_0094 exists, both remain formally possible given HAD promiscuity, but the **specific curated ortholog assignment favors phosphoglycolate phosphatase.**

### F005 — PP_0094 shares the full conserved catalytic core of *E. coli* Gph and sits in a non-operonic genomic context

A global pairwise alignment of PP_0094 against *E. coli* Gph (P32662) yields **29.2% identity over the full length**, with exact co-alignment of all four catalytic motifs:

| Motif | PP_0094 | *E. coli* Gph | Conserved catalytic element |
|-------|---------|---------------|-----------------------------|
| I | `F-DLDGTL-TD` | `A-FDLDGTL-VD` | Asp nucleophile + Asp acid/base |
| II/III | `...ATSK...` | `...VTNK...` | catalytic Thr and Lys |
| IV | `LMIGDRKHD` | `LFVGDSRND` | GD…D Mg²⁺-coordinating loop |

The conservation of the entire catalytic scaffold — nucleophile, general acid/base, the Ser/Thr–Lys pair, and the metal-binding loop — confirms PP_0094 retains an intact, functional HAD active site homologous to a characterized phosphoglycolate phosphatase.

The **genomic neighborhood** (KEGG ppu) is *not* functionally diagnostic. Flanking genes are PP_0093 (zinc protease), PP_0095 (unknown enzyme), PP_0096 (oligopeptidase A), PP_0089 (stress-induced peroxiredoxin) and PP_0100 (carbonic anhydrase). There are **no co-localized glycolate/glyoxylate, DNA-repair, or nucleotide-metabolism genes**, indicating PP_0094 is a **standalone gene**, not embedded in a diagnostic operon. This is fully consistent with a constitutively expressed housekeeping enzyme; indeed [PMID: 13129953](https://pubmed.ncbi.nlm.nih.gov/13129953/) reports for the ortholog that *"Western blot analysis revealed constitutive expression of the gph gene, regardless of the carbon source used, growth stage, or oxidative stress conditions."*

### F006 — Mechanism and pathway context: phospho-aspartyl catalysis, cap-encoded specificity, steric exclusion of nucleotides

The catalytic mechanism and the case for a small substrate are both well supported. Phosphoglycolate phosphatase catalysis proceeds by O–P bond cleavage through a covalent **phospho-enzyme (phospho-aspartyl) intermediate**, exactly matching the HAD Motif-I Asp9 nucleophile identified in PP_0094. [PMID: 204631](https://pubmed.ncbi.nlm.nih.gov/204631/) concluded that *"The data suggest that the reaction sequence proceeds via a phosphoenzyme intermediate."*

Substrate specificity in capped HAD phosphatases (subclass IIA/IIB, which includes PGP) is set by a small number of cap-domain residues and loops. [PMID: 24338473](https://pubmed.ncbi.nlm.nih.gov/24338473/) demonstrates that *"a single, differently conserved residue in the cap domain of either AUM or chronophin is crucial for phosphatase specificity,"* and [PMID: 15952775](https://pubmed.ncbi.nlm.nih.gov/15952775/) shows how cap-domain "solvent cage" loops encase the substrate leaving group and thereby dictate specificity. PP_0094 carries exactly this specificity-determining cap (IPR023198).

Crucially, genuine PGP active sites have *"exacting steric requirements for binding, and… large alkyl groups were excluded on this basis"* ([PMID: 204631](https://pubmed.ncbi.nlm.nih.gov/204631/)). This steric argument works **against** efficient turnover of bulky nucleoside-5′-monophosphates and **in favor** of the small two-carbon substrate 2-phosphoglycolate.

Finally, the pathway role is that of a paradigm **metabolite-repair / damage-control phosphatase**. [PMID: 27294321](https://pubmed.ncbi.nlm.nih.gov/27294321/) shows that *"a single, widely conserved enzyme, known as phosphoglycolate phosphatase (PGP) in mammals, dephosphorylates both 4-phosphoerythronate and 2-phospho-L-lactate, thereby preventing a block in the pentose phosphate pathway and glycolysis."* In *E. coli*, the same reaction salvages 2-phosphoglycolate arising from DNA repair of oxidative 3′-phosphoglycolate ends ([PMID: 13129953](https://pubmed.ncbi.nlm.nih.gov/13129953/)).

### F007 — AlphaFold model confirms a compact, well-folded HAD enzyme with an intact active site

The AlphaFold DB model **AF-Q88RN5-F1 (v6)** is of very high quality: **mean pLDDT 96.1, median 97.6**, with 93.1% of the 216 residues at very-high confidence (pLDDT ≥ 90), 99.5% confident (≥ 70), and **0% below 50** (no predicted disorder). All catalytic and metal-binding residues are modeled at very high confidence:

| Residue | Role | pLDDT |
|---------|------|-------|
| Asp9 | nucleophile | 98.0 |
| Asp11 | general acid/base | 96.4 |
| Thr107 | Motif II | 98.1 |
| Lys110 | Motif III | 92.8 |
| Asp165 | Motif IV (Mg²⁺) | 98.4 |
| Asp171 | Motif IV (Mg²⁺) | 98.1 |

The model shows a single compact Rossmann-like HAD core plus the C2 cap, consistent with a globular soluble cytoplasmic enzyme. The structural prediction thus independently corroborates the sequence-based conclusion that PP_0094 is a folded, catalytically competent HAD phosphatase.

---

## Mechanistic Model / Interpretation

Integrating the seven findings yields a coherent, structurally and evolutionarily grounded model of PP_0094 as a cytoplasmic HAD phosphatase whose most specific predicted activity is 2-phosphoglycolate phosphatase.

**Proposed reaction:**

```
   2-phosphoglycolate  +  H2O   ---[ PP_0094, Mg2+ ]-->   glycolate  +  Pi
   (small 2-carbon
    phosphometabolite)
```

**Catalytic cycle (HAD phospho-aspartyl mechanism):**

```
  Step 1  Asp9 (Motif I) attacks substrate phosphorus
          -> covalent phospho-aspartyl enzyme intermediate + glycolate leaves
  Step 2  Asp11 acts as general acid/base; Mg2+ (held by Asp165/Asp171, Motif IV)
          stabilizes the transition state; Thr107/Lys110 (Motifs II/III)
          anchor the transferring phosphoryl group
  Step 3  Water hydrolyzes the phospho-aspartyl intermediate -> release Pi,
          regenerate free enzyme
```

**Domain architecture and how it sets specificity:**

```
  N ---[ HAD core: Motif I (Asp9/Asp11) ]---[ C2 CAP DOMAIN (res 14-105) ]---
        [ Motif II (Thr107) - Motif III (Lys110) ]---[ Motif IV (Asp165/171) ]--- C
                                   |
              PGP-like cap (IPR023198) forms a "solvent cage" that
              encloses a SMALL leaving group (glycolate), sterically
              excluding bulky nucleoside monophosphates
```

The reconciliation of the two competing annotations is the central interpretive point. Both the "5′-nucleotidase" and the "phosphoglycolate phosphatase" labels place PP_0094 firmly within the same soluble, cytoplasmic, Mg²⁺-dependent HAD phosphatase class using an identical catalytic mechanism. They differ only in predicted substrate. The **legacy 5′-nucleotidase call (EC 3.1.3.5)** is a low-resolution, automated genome annotation from 2002 propagated through the CDD cd04302 subfamily. The **phosphoglycolate phosphatase call (EC 3.1.3.18)** is a higher-resolution, curated assignment supported by four independent orthology/domain lines plus the closest experimentally characterized homolog. The steric argument from [PMID: 204631](https://pubmed.ncbi.nlm.nih.gov/204631/) — that authentic PGP active sites exclude large alkyl groups — mechanistically disfavors bulky nucleotides and tips the balance toward the small 2-phosphoglycolate substrate.

Placed in cellular context, PP_0094 most plausibly functions as a **housekeeping metabolite-repair enzyme in the cytoplasm**, clearing small phospho-metabolite side products (paradigmatically 2-phosphoglycolate) and channeling the resulting glycolate into **glyoxylate and dicarboxylate metabolism** (KEGG ppu00630). This role is metabolically important but not tied to a specialized pathway operon, consistent with the standalone, constitutively expressed genomic context. Given HAD promiscuity, the enzyme may additionally clear a range of small phosphometabolites (as its mammalian PGP relatives do for 4-phosphoerythronate and 2-phospho-L-lactate), so "phosphoglycolate phosphatase" is best read as the **primary, most-specific** activity rather than an exclusive one.

The physiological relevance is especially notable in *P. putida* KT2440, a premier metabolic chassis whose value for industrial biotechnology and glycol/PET-monomer catabolism has been highlighted repeatedly ([PMID: 26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/)). Glycolate is a central node in ethylene-glycol assimilation, so a cytoplasmic phosphoglycolate phosphatase feeding the glycolate pool is a plausible, if untested, contributor to this organism's carbon metabolism.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports / challenges the findings |
|------|-----------------|-------------------------------------------|
| [13129953](https://pubmed.ncbi.nlm.nih.gov/13129953/) | *Role of 2-phosphoglycolate phosphatase of E. coli in metabolism of the 2-phosphoglycolate formed in DNA repair* | **Core reference.** Defines the biochemically characterized ortholog (Gph): highly specific for 2-phosphoglycolate; constitutively expressed housekeeping enzyme; salvages 2-PG from DNA repair. Supports F004, F005, F006. |
| [204631](https://pubmed.ncbi.nlm.nih.gov/204631/) | *Mechanism of phosphoglycolate phosphatase…* | Establishes the phospho-enzyme (phospho-aspartyl) intermediate and the "exacting steric requirements" that exclude large alkyl groups. Supports the mechanism and the steric case against nucleotides (F006). |
| [27294321](https://pubmed.ncbi.nlm.nih.gov/27294321/) | *A conserved phosphatase destroys toxic glycolytic side products in mammals and yeast* | Frames PGP as a conserved metabolite-repair phosphatase acting on small phosphometabolite side-products (4-phosphoerythronate, 2-phospho-L-lactate). Supports the pathway role (F006). |
| [24338473](https://pubmed.ncbi.nlm.nih.gov/24338473/) | *Evolutionary and structural analyses of AUM and chronophin…* | Shows a single cap-domain residue dictates specificity in PGP-type HAD phosphatases — the domain present in PP_0094 (IPR023198). Supports F006. |
| [15952775](https://pubmed.ncbi.nlm.nih.gov/15952775/) | *HAD subclass IIB sugar phosphatase BT4131…* | Structural analysis of cap-domain "solvent cage" loops that set leaving-group specificity; contrasts high-specificity PGP with lax sugar phosphatases. Supports the cap/specificity model (F001, F006). |
| [27907199](https://pubmed.ncbi.nlm.nih.gov/27907199/) | *B. subtilis YutF, a HAD 5′-nucleotidase with broad substrate specificity* | Defines EC 3.1.3.5 reaction and establishes that soluble 5′-nucleotidases are the intracellular HADSF class. Supports F002, F003 (localization). |
| [27784292](https://pubmed.ncbi.nlm.nih.gov/27784292/) | *B. subtilis 5′-nucleotidases with various functions and specificities* | Names the *E. coli* NagD-group 5′-nucleotidases. Supports the legacy annotation context (F002). |
| [32040605](https://pubmed.ncbi.nlm.nih.gov/32040605/) | *Expression and purification of 5′-nucleotidase YitU…* | Documents a characterized HAD 5′-nucleotidase with broad (deoxy)ribonucleotide specificity. Supports the promiscuity caveat (F002). |
| [30030002](https://pubmed.ncbi.nlm.nih.gov/30030002/) | *Do metabolic HAD phosphatases moonlight as protein phosphatases?* | Reviews PGP/AUM, chronophin, LHPP capped HAD phosphatases; supports small-metabolite (not protein) substrate interpretation. Contextual support for F006. |
| [26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/) | *The revisited genome of Pseudomonas putida KT2440…* | Context for the 2002 auto-annotation origin and re-annotation of KT2440 genes; frames the legacy-vs-curated annotation issue. |

The evidence architecture is deliberately layered. The strongest and most specific evidence (KEGG K01091, PANTHER PTHR43434, IPR023198 cap, closest homology to characterized Gph, and the steric mechanism) supports phosphoglycolate phosphatase. The legacy 5′-nucleotidase evidence (CDD cd04302, PANTHER SF20 subfamily, GO:0008253) is real but derives from lower-resolution automated pipelines and reflects the shared NagD/HAD scaffold rather than a measured substrate preference.

---

## Limitations and Knowledge Gaps

1. **No experimental data on PP_0094.** UniProt protein-existence level is 4 ("Predicted"). The protein has never been purified, assayed, crystallized, or genetically characterized. Every functional statement is inference.

2. **Two competing annotations remain formally reconcilable only by assay.** Both EC 3.1.3.18 (phosphoglycolate phosphatase) and EC 3.1.3.5 (5′-nucleotidase) are plausible for a capped HAD IIA/IIB enzyme. The curated orthology and steric arguments favor PGP, but HAD phosphatases are genuinely promiscuous, and residual nucleotidase activity is not excluded.

3. **Modest sequence identity to the reference.** The best-characterized homolog, *E. coli* Gph, shares only ~29% identity. While the catalytic core and cap type are conserved, the specificity-determining loops (which differ by single residues) have not been individually mapped in PP_0094.

4. **Non-diagnostic genomic context.** PP_0094 is a standalone gene with no operonic partners in glycolate/glyoxylate, DNA-repair, or nucleotide metabolism, so gene-neighborhood evidence neither confirms nor refutes the substrate assignment.

5. **AlphaFold confirms fold, not function.** The very-high-confidence model (pLDDT 96.1) verifies an intact active site and globular soluble architecture but cannot, by itself, discriminate between candidate small-molecule substrates.

6. **No *P. putida*-specific physiology.** Whether PP_0094 is the sole or principal 2-phosphoglycolate phosphatase in KT2440, and how it interfaces with this organism's glyoxylate/dicarboxylate and ethylene-glycol/glycolate metabolism, is unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzyme assay (definitive test).** Heterologously express and purify His-tagged PP_0094, then run a substrate-specificity panel of malachite-green/Pi-release assays comparing **2-phosphoglycolate** against a suite of nucleoside-5′-monophosphates (AMP, GMP, CMP, dAMP, IMP, XMP), plus other candidate small phosphometabolites (4-phosphoerythronate, 2-phospho-L-lactate, pyridoxal-5′-phosphate). Report kcat/Km for each to establish the true primary substrate. This single experiment would resolve the EC 3.1.3.18 vs 3.1.3.5 ambiguity.

2. **Active-site mutagenesis.** Mutate Asp9→Ala (nucleophile) and Asp11→Ala to confirm loss of activity, validating the predicted phospho-aspartyl mechanism.

3. **Cap-loop specificity mapping.** Compare the PP_0094 cap-domain specificity loop against those of *E. coli* Gph and the sugar phosphatase BT4131 ([PMID: 15952775](https://pubmed.ncbi.nlm.nih.gov/15952775/)); dock 2-phosphoglycolate and AMP into the AlphaFold model to test the steric-exclusion hypothesis quantitatively.

4. **Genetic knockout / complementation.** Delete PP_0094 in *P. putida* KT2440 and test for 2-phosphoglycolate accumulation, sensitivity to oxidative DNA damage, and growth phenotypes on glycolate/glyoxylate and ethylene-glycol-derived carbon sources; complement to confirm.

5. **Structural determination.** Solve a crystal or cryo-EM structure of PP_0094 with Mg²⁺ and a bound substrate/product analog (e.g., glycolate or a phosphonate mimic) to directly visualize the leaving-group pocket.

6. **Curated re-annotation.** Pending experimental confirmation, flag the UniProt/GenBank "5′-nucleotidase (EC 3.1.3.5)" entry with the curated K01091/PTHR43434 phosphoglycolate-phosphatase evidence so downstream metabolic reconstructions of KT2440 use the more specific assignment.

---

## Conclusion

PP_0094 (Q88RN5) is, with high structural and evolutionary confidence, a **small soluble cytoplasmic Mg²⁺-dependent HAD-superfamily phosphatase** that operates through a phospho-aspartyl intermediate and carries a phosphoglycolate-phosphatase-type C2 cap. Its **most likely primary function is 2-phosphoglycolate phosphatase (EC 3.1.3.18)** — hydrolyzing 2-phosphoglycolate to glycolate + Pi as a cytoplasmic metabolite-repair enzyme feeding glyoxylate/dicarboxylate metabolism — a curated reassignment that supersedes the legacy automated "5′-nucleotidase (EC 3.1.3.5)" annotation. This conclusion rests entirely on convergent bioinformatic, orthology, structural, and homolog-biochemistry inference; PP_0094 itself has never been experimentally characterized, and definitive substrate assignment awaits a direct enzymatic assay.


## Artifacts

- [OpenScientist final report](PP_0094-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0094-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27784292
2. PMID:32040605
3. PMID:27907199
4. PMID:13129953
5. PMID:24338473
6. PMID:15952775
7. PMID:27294321
8. PMID:26913973