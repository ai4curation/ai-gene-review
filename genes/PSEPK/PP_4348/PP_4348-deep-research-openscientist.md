---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T16:19:41.823038'
end_time: '2026-07-11T16:39:36.358084'
duration_seconds: 1194.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4348
  gene_symbol: PP_4348
  uniprot_accession: Q88EV4
  protein_description: 'SubName: Full=Cystathionine beta-lyase {ECO:0000313|EMBL:AAN69927.1};'
  gene_info: OrderedLocusNames=PP_4348 {ECO:0000313|EMBL:AAN69927.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the trans-sulfuration enzymes family.
  protein_domains: Cys/Met-Metab_PyrdxlP-dep_enz. (IPR000277); Cys_b_lyase_bac. (IPR006233);
    PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421); PyrdxlP-dep_Trfase_small.
    (IPR015422)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
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
  path: PP_4348-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_4348-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88EV4
- **Protein Description:** SubName: Full=Cystathionine beta-lyase {ECO:0000313|EMBL:AAN69927.1};
- **Gene Information:** OrderedLocusNames=PP_4348 {ECO:0000313|EMBL:AAN69927.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the trans-sulfuration enzymes family.
- **Key Domains:** Cys/Met-Metab_PyrdxlP-dep_enz. (IPR000277); Cys_b_lyase_bac. (IPR006233); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421); PyrdxlP-dep_Trfase_small. (IPR015422)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4348" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4348' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4348** (gene ID: PP_4348, UniProt: Q88EV4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_4348 (Q88EV4): Cystathionine β-Lyase of *Pseudomonas putida* KT2440

## Summary

**PP_4348 (UniProt Q88EV4) of *Pseudomonas putida* KT2440 encodes a cytoplasmic, pyridoxal-5′-phosphate (PLP)-dependent cystathionine β-lyase (MetC; EC 4.4.1.8).** Its primary, physiological function is to catalyze the α,β-elimination reaction that cleaves the Cβ–S bond of L,L-cystathionine, yielding **L-homocysteine, pyruvate, and ammonia** (Rhea RHEA:13965). This is the penultimate step of *de novo* methionine biosynthesis via the transsulfuration branch, mapped by KEGG to the methionine biosynthesis module M00017 (aspartate ⇒ homoserine ⇒ methionine). The gene symbol PP_4348, the organism *P. putida* KT2440, the trans-sulfuration enzyme family assignment, and the diagnostic InterPro/Pfam domains (IPR006233 bacterial cystathionine β-lyase; IPR000277 Cys/Met-metabolism PLP-dependent enzyme; PF01053) all coincide with the biochemistry described below. The gene identity is unambiguous — the well-known *P. putida* methionine γ-lyase is a *distinct* gene (*mdeA*/P13254), not this locus.

Structurally, PP_4348 belongs to the fold-type I family of PLP-dependent enzymes (the "γ-family" of the Cys/Met-metabolism group). Like its extensively characterized *Escherichia coli* ortholog MetC, it is expected to assemble as a homotetramer of catalytically active dimers, with each ~364-residue subunit organized into three functional domains. The PLP cofactor is anchored as an internal aldimine (Schiff base) to an active-site lysine — **Lys186 in PP_4348**, corresponding to the experimentally validated catalytic Lys210 of *E. coli* MetC. A pairwise global alignment performed in this investigation shows PP_4348 is most similar to *E. coli* cystathionine β-lyase (43.9% identity) — higher than to cystathionine γ-synthase MetB (41.8%), MalY (41.3%), or *P. putida* methionine γ-lyase (41.1%) — and that every key active-site residue defined by the *E. coli* crystal structure is conserved one-to-one. This colinear, intact catalytic constellation demonstrates that PP_4348 is a functional, canonical cystathionine β-lyase rather than a degenerate homolog.

Physiologically, direct experimental work in *P. putida* (Vermeij & Kertesz, 1999) showed that the transsulfuration enzymes cystathionine γ-synthase and cystathionine β-lyase are expressed at low basal levels but are strongly upregulated during growth on cysteine as the sole sulfur source, while the organism's dominant methionine route is direct sulfhydrylation of O-succinylhomoserine. PP_4348 therefore provides the forward (cysteine → methionine) transsulfuration route producing homocysteine; because *P. putida* lacks cystathionine γ-lyase (no reverse transsulfuration), the enzyme acts only in the biosynthetic direction. Like other members of its family, MetC is catalytically promiscuous, also exhibiting cysteine-S-conjugate β-lyase activity (EC 4.4.1.13) and, in some bacterial homologs, alliinase and D-amino-acid–metabolizing activities; however, L-cystathionine β-elimination is the enzyme's physiological reaction. The enzyme operates in the cytoplasm, consistent with the absence of a signal peptide in Q88EV4 and the cytosolic nature of the transsulfuration pathway.

---

## Gene / Protein Identity Verification

| Attribute | Value | Source |
|---|---|---|
| UniProt accession | Q88EV4 | UniProt |
| Locus / gene | PP_4348 | UniProt / EMBL AAN69927.1 |
| Organism | *Pseudomonas putida* KT2440 (PSEPK) | UniProt |
| Length | 364 aa | UniProt |
| EC / reaction | 4.4.1.8 · RHEA:13965 | UniProt catalytic activity |
| Cofactor | PLP, Schiff base at **Lys186** | UniProt features |
| Family | Trans-sulfuration enzymes | UniProt similarity |
| Signatures | IPR006233 (**Cys_b_lyase_bac**, bacterial-CBL specific), IPR000277, PF01053, COG0626, SSF53383 | InterPro/UniProt |

**Verification result:** The gene symbol, organism, reaction, cofactor, and domain architecture are internally consistent and match authoritative family models. The bacterial-CBL–specific InterPro signature **IPR006233** and the annotated catalytic reaction directly support the "cystathionine β-lyase" assignment. **No ambiguity detected.** No source contradicts the assignment.

---

## Key Findings

### Finding 1 — PP_4348 is a PLP-dependent cystathionine β-lyase (MetC, EC 4.4.1.8)

The core functional assignment is that PP_4348/Q88EV4 catalyzes:

> **L,L-cystathionine + H₂O → L-homocysteine + pyruvate + NH₄⁺** (Rhea RHEA:13965)

This reaction is annotated in UniProt with a PLP cofactor bound through a Schiff base to Lys186 (N6-(pyridoxal phosphate)lysine). The reaction is an α,β-elimination that cleaves the Cβ–S bond of cystathionine. InterPro assigns PP_4348 the bacterial-cystathionine-β-lyase-specific signature **IPR006233 (Cys_b_lyase_bac)** in addition to the broader **IPR000277 (Cys/Met-metabolism PLP-dependent enzyme)**, Pfam **PF01053 (Cys_Met_Meta_PP)**, eggNOG **COG0626**, and SUPFAM **SSF53383 (PLP-dependent transferases, fold-type I)**. The bacterial-CBL-specific signature is particularly diagnostic — it distinguishes cystathionine β-lyases from the closely related γ-synthases and γ-lyases of the same fold.

A pairwise global alignment performed in this investigation quantifies the family placement. PP_4348 (364 aa) is most similar to *E. coli* cystathionine β-lyase MetC (P06721) at **43.9%** aligned identity, exceeding its similarity to cystathionine γ-synthase MetB (41.8%), MalY (41.3%), and *P. putida* methionine γ-lyase (41.1%). Although these figures are close — reflecting deep conservation of the fold-type I scaffold across the Cys/Met family — the highest identity is to the β-lyase, and the diagnostic InterPro signature resolves any residual ambiguity.

The reaction chemistry is supported by literature. A 2024/2025 structural study of *Bacillus cereus* cystathionine β-lyase states that these enzymes "catalyze the conversion of cystathionine to homocysteine and pyruvate" [PMID: 39644606](https://pubmed.ncbi.nlm.nih.gov/39644606/), matching the UniProt reaction for PP_4348. Foundational structural work on *E. coli* CBL establishes that "Cystathionine beta-lyase (CBL) is a member of the gamma-family of PLP-dependent enzymes, that cleaves C beta-S bonds of a broad variety of substrates" [PMID: 8831789](https://pubmed.ncbi.nlm.nih.gov/8831789/) — consistent with PP_4348's PLP cofactor and β-elimination mechanism.

### Finding 2 — PP_4348 operates in the transsulfuration branch of methionine biosynthesis and is induced by cysteine as sole sulfur source

The most decisive organism-specific evidence comes from Vermeij & Kertesz (1999), who directly measured transsulfuration enzyme activities in *Pseudomonas putida* S-313 [PMID: 10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/). They reported that "The enzymes of the transsulfuration pathway (cystathionine gamma-synthase and cystathionine beta-lyase) were expressed at low levels in both pseudomonads but were strongly upregulated during growth with cysteine as the sole sulfur source." This establishes both the *presence* and the *sulfur-source–dependent regulation* of cystathionine β-lyase in *P. putida*.

Critically, the same study showed that "Both these organisms used direct sulfhydrylation of O-succinylhomoserine for the synthesis of methionine," meaning the dominant methionine route in *P. putida* is direct sulfhydrylation, not transsulfuration. PP_4348 therefore provides a *supplementary* transsulfuration route producing homocysteine (subsequently methylated to methionine by MetE/MetH), important particularly when cysteine or sulfur flux favors the cystathionine intermediate. Because *P. putida* lacks cystathionine γ-lyase (no reverse transsulfuration), the enzyme acts unidirectionally in the forward, cysteine → methionine biosynthetic direction. This regulatory and pathway context — low basal expression, cysteine inducibility, forward direction only — precisely defines PP_4348's metabolic niche.

### Finding 3 — Catalytic mechanism, substrate positioning, and cytoplasmic localization

Studies of *E. coli* CBL (Clausen et al., 1996/1997) show a fold-type I PLP enzyme with three domains per monomer that assembles into a **homotetramer of active dimers**: "A homotetramer with 222 symmetry is built up by crystallographic and non-crystallographic symmetry. Each monomer of CBL can be described in terms of three spatially and functionally different domains" [PMID: 8831789](https://pubmed.ncbi.nlm.nih.gov/8831789/). Catalysis begins with the PLP forming an internal aldimine (Schiff base) with the active-site lysine (Lys186 in PP_4348); binding of substrate converts this to an external aldimine, and α,β-elimination cleaves the Cβ–S bond of cystathionine [PMID: 9165088](https://pubmed.ncbi.nlm.nih.gov/9165088/).

The determinant of *reaction-type selection* within the Cys/Met family is understood at the residue level. Messerschmidt et al. (2003) explain that "In CBLs this position is occupied by either tyrosine or hydrophobic residues directing binding of CTT [cystathionine] such that S is in the gamma-position" [PMID: 12715888](https://pubmed.ncbi.nlm.nih.gov/12715888/). In γ-family enzymes the equivalent position is a conserved glutamate; in β-lyases a tyrosine/hydrophobic residue reorients the substrate so that its sulfur sits in the γ-position, which geometrically dictates β-elimination rather than γ-chemistry. This is the molecular basis for why PP_4348 performs β-elimination on cystathionine.

Regarding localization, Q88EV4 has no signal peptide or transmembrane segment, and the transsulfuration pathway is cytosolic; PP_4348 is therefore a **soluble cytoplasmic protein** that carries out its function in the cytoplasm. The enzyme (and its bacterial homologs) also displays promiscuous cysteine-S-conjugate β-lyase activity (UniProt GO:0047804), a hallmark of the broad substrate tolerance of the family.

### Finding 4 — All catalytic and active-site residues are conserved in PP_4348 (structure-based evidence)

A residue-by-residue alignment of PP_4348 (Q88EV4) to *E. coli* MetC (P06721) shows one-to-one conservation of every key active-site residue defined by the *E. coli* crystal structure (Clausen et al., 1996):

| Function | *E. coli* MetC residue | PP_4348 residue |
|---|---|---|
| Catalytic PLP Schiff-base lysine | Lys210 | **Lys186** |
| Substrate-orienting tyrosine | Tyr56 | Tyr35 |
| Active-site tyrosine | Tyr111 | Tyr91 |
| Binds PLP pyridine nitrogen | Asp185 | Asp161 |
| Active-site threonine | Thr222 | Thr201 |
| Substrate-carboxylate region tyrosine | Tyr338 | Tyr312 |

The PLP-Schiff-base lysine mapping (Lys210 → Lys186) exactly matches the independently annotated UniProt PLP-lysine feature for Q88EV4, providing internal cross-validation. The *E. coli* structure defines the PLP-binding second domain: "The second domain (residues 61 to 256) harbors PLP and has an alpha/beta-structure with a seven-stranded beta-sheet as the central part" [PMID: 8831789](https://pubmed.ncbi.nlm.nih.gov/8831789/). The intact, colinear active-site constellation demonstrates that PP_4348 possesses a functional, canonical CBL catalytic machinery.

### Finding 5 — KEGG pathway placement, EC-number nuance, and genomic context

KEGG (ppu:PP_4348) maps the gene to pathway **ppu00270** (Cysteine and methionine metabolism), **ppu00450** (Selenocompound metabolism), **ppu01230** (Biosynthesis of amino acids), and **module M00017** (Methionine biosynthesis, aspartate ⇒ homoserine ⇒ methionine), confirming its physiological placement at the cystathionine → homocysteine step. Its Pfam architecture includes Cys_Met_Meta_PP, Beta_elim_lyase, and Aminotran_5 motifs — all consistent with a fold-type I PLP enzyme.

A notable annotation nuance: KEGG assigns KO **K01760 / EC 4.4.1.13** (cysteine-S-conjugate β-lyase) whereas UniProt annotates **EC 4.4.1.8** (cystathionine β-lyase). Both are carbon-sulfur lyase (subclass 4.4.1) reactions that cleave a Cβ–S bond and are catalyzed by the same active site; the discrepancy reflects the enzyme's catalytic promiscuity, not a different enzyme.

The gene occupies KT2440 genome position ~4,940,549–4,941,643 and is **not embedded in a classical methionine operon**. It is flanked by PP_4347 (pseudogene), PP_4349 (conserved hypothetical), PP_4346 (D-Ala–D-Ala ligase), and PP_4350 (a NifS/IscS-family cysteine desulfurase). Its standalone genomic arrangement is consistent with the low basal, sulfur-source–regulated expression reported by Vermeij & Kertesz (1999).

### Finding 6 — Substrate/reaction-specificity determinants are experimentally defined and conserved

Site-directed mutagenesis of *E. coli* CBL (Lodha & Aitken, 2011) experimentally established the functional roles of individual active-site residues in the α,β-elimination of L-cystathionine. The study confirmed the exact reaction: "Cystathionine β-lyase (CBL) catalyzes the hydrolysis of L-cystathionine (L-Cth) to produce L-homocysteine, pyruvate, and ammonia" [PMID: 21958132](https://pubmed.ncbi.nlm.nih.gov/21958132/). It further demonstrated "A novel role for residue S339 as a determinant of reaction specificity, via tethering of the catalytic base, K210" — with the S339-to-Ala variant reducing kcat/Km ~1000-fold. Tyr238 was shown to interact with the substrate's distal carboxylate and Tyr56 with the distal amino group.

In PP_4348, the corresponding catalytic base (Lys210 → Lys186) and the specificity tyrosines (Tyr56 → Tyr35, Tyr111 → Tyr91, Tyr338 → Tyr312) are all conserved. This places the experimentally validated *E. coli* specificity determinants directly onto the PP_4348 active site.

The family's promiscuity is well documented: bacterial MetCs display alliinase activity [PMID: 38810088](https://pubmed.ncbi.nlm.nih.gov/38810088/) and participate in D-amino acid metabolism [PMID: 29592871](https://pubmed.ncbi.nlm.nih.gov/29592871/). These secondary activities are consistent with the broad Cβ–S lyase capability of the family, but L-cystathionine β-elimination remains the physiological reaction of PP_4348.

---

## Mechanistic Model / Interpretation

### Position in methionine biosynthesis

PP_4348 catalyzes the penultimate step of methionine biosynthesis via the transsulfuration branch:

```
                (sulfur assimilation)
                        │
                        ▼
   L-cysteine ─────────────────────────┐
                                        │  (cystathionine γ-synthase, MetB)
   O-succinyl-L-homoserine ────────────►│
                                        ▼
                            L,L-CYSTATHIONINE
                                        │
                                        │  ★ PP_4348 = cystathionine β-lyase (MetC)
                                        │     EC 4.4.1.8, PLP-dependent
                                        │     Cβ–S bond cleavage (α,β-elimination)
                                        ▼
              L-HOMOCYSTEINE  +  pyruvate  +  NH₄⁺
                                        │
                                        │  (MetE / MetH methyltransferase)
                                        ▼
                                 L-METHIONINE
                                        │
                                        ▼
                              S-adenosylmethionine
```

In *P. putida*, this transsulfuration route runs in parallel with — and is subordinate to — the dominant **direct sulfhydrylation** of O-succinylhomoserine. Transsulfuration is upregulated when cysteine is the sole sulfur source, situating PP_4348 as a conditionally important, cysteine-inducible enzyme. Because *P. putida* has no cystathionine γ-lyase, the pathway is one-directional (biosynthetic; cysteine → methionine).

### Catalytic mechanism

```
  Internal aldimine (resting)          External aldimine (substrate-bound)
   PLP=N–Lys186  ───────────────►  PLP=N–[cystathionine]  ───────────────►
                (transaldimination)             (Cα deprotonation →
                                                 α,β-elimination at Cβ–S)
                                                        │
                                                        ▼
                          release of L-homocysteine (thiol leaving group)
                          + aminoacrylate–PLP intermediate
                                                        │
                                          (hydrolysis / reprotonation)
                                                        ▼
                     pyruvate + NH₄⁺ + regenerated PLP=N–Lys186
```

The reaction specificity — β-elimination rather than the γ-elimination performed by cystathionine γ-synthase/γ-lyase — is dictated by active-site geometry. In β-lyases, a tyrosine/hydrophobic residue (in place of the conserved glutamate of γ-enzymes) orients cystathionine so that its sulfur occupies the γ-position, positioning the Cβ–S bond for cleavage. This is the structural switch, conserved in PP_4348, that defines its catalytic outcome.

### Comparative summary

| Property | Assignment for PP_4348 | Basis |
|---|---|---|
| Primary reaction | L,L-cystathionine → L-homocysteine + pyruvate + NH₄⁺ | UniProt RHEA:13965; PMID 39644606, 21958132 |
| EC number | 4.4.1.8 (UniProt); 4.4.1.13 also mapped by KEGG (promiscuity) | UniProt / KEGG K01760 |
| Cofactor | PLP, Schiff base at Lys186 | UniProt feature; alignment to Ec Lys210 |
| Fold | Fold-type I PLP transferase, homotetramer | SSF53383; PMID 8831789 |
| Pathway | Methionine biosynthesis (transsulfuration branch) | KEGG M00017; PMID 10482527 |
| Direction | Forward (Cys → Met) only; no reverse transsulfuration | PMID 10482527 |
| Regulation | Low basal; induced by cysteine as sole S source | PMID 10482527 |
| Localization | Cytoplasm | No signal peptide in Q88EV4 |
| Secondary activities | Cysteine-S-conjugate β-lyase, alliinase, D-AA metabolism | GO:0047804; PMID 38810088, 29592871 |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [10482527](https://pubmed.ncbi.nlm.nih.gov/10482527/) | *Pathways of assimilative sulfur metabolism in Pseudomonas putida* | **Organism-specific.** Directly measures cystathionine β-lyase in *P. putida*, shows cysteine-inducible transsulfuration and dominant direct sulfhydrylation. Anchors Finding 2. |
| [8831789](https://pubmed.ncbi.nlm.nih.gov/8831789/) | *Crystal structure of E. coli cystathionine β-lyase at 1.83 Å* | Defines the fold, homotetramer, three-domain monomer, PLP-binding domain, and the catalytic residues mapped onto PP_4348. Anchors Findings 1, 3, 4. |
| [9165088](https://pubmed.ncbi.nlm.nih.gov/9165088/) | *Mode of action of cystathionine β-lyase* | Establishes the PLP-dependent Cβ–S cleavage mechanism (internal/external aldimine, α,β-elimination). Supports Finding 3. |
| [12715888](https://pubmed.ncbi.nlm.nih.gov/12715888/) | *Determinants of enzymatic specificity in the Cys-Met-metabolism PLP-dependent enzyme family* | Explains the tyrosine/hydrophobic vs. glutamate switch that makes CBLs perform β- rather than γ-elimination. Supports Finding 3. |
| [21958132](https://pubmed.ncbi.nlm.nih.gov/21958132/) | *Side-chain hydroxyls Y56, Y111, Y238, Y338, S339 as specificity determinants in E. coli CBL* | Experimentally defines catalytic base K210 and specificity residues (all conserved in PP_4348) and confirms the exact reaction/products. Anchors Finding 6. |
| [39644606](https://pubmed.ncbi.nlm.nih.gov/39644606/) | *Crystal structures of cystathionine β-lyase from Bacillus cereus* | Independent confirmation of the cystathionine → homocysteine + pyruvate reaction. Supports Finding 1. |
| [38810088](https://pubmed.ncbi.nlm.nih.gov/38810088/) | *Identification and characterization of bacterial alliinase (MetC)* | Documents family promiscuity (bacterial MetCs with alliinase activity). Supports Finding 6. |
| [29592871](https://pubmed.ncbi.nlm.nih.gov/29592871/) | *Cystathionine β-lyase is involved in D-amino acid metabolism* | Documents secondary D-amino-acid–related activity of CBL. Supports Finding 6. |
| [10965031](https://pubmed.ncbi.nlm.nih.gov/10965031/) | *Crystal structure of L-methionine γ-lyase from P. putida* | Shows the related *P. putida* MGL shares the fold with CBL/CGS; context for family relationships and for distinguishing PP_4348 from *mdeA*. |
| [17300162](https://pubmed.ncbi.nlm.nih.gov/17300162/) | *Inhibitors of bacterial cystathionine β-lyase* | Highlights that methionine biosynthesis is absent in mammals, making bacterial CBL an antibiotic target — underscoring the enzyme's physiological importance. |

**Consistency of the evidence:** Independent lines — UniProt/Rhea reaction annotation, diagnostic InterPro/Pfam signatures, quantitative pairwise alignment (43.9% identity to *E. coli* MetC, higher than any other family member), one-to-one active-site residue conservation including the PLP lysine, KEGG pathway/module placement, and direct enzymological measurement in *P. putida* itself — all converge on the same conclusion. No source contradicts the cystathionine β-lyase assignment.

---

## Supported vs. Refuted Hypotheses

**Supported**
- PP_4348 is a PLP-dependent cystathionine β-lyase (EC 4.4.1.8) — catalytic reaction, PLP-Lys186, IPR006233 signature, and sequence homology all agree.
- It functions in the transsulfuration branch of methionine biosynthesis in the cytoplasm.
- It is regulated (induced on cysteine) and operates in the forward direction only, given the absence of cystathionine γ-lyase in *P. putida*.

**Refuted / excluded**
- PP_4348 is **not** the *P. putida* methionine γ-lyase (*mdeA*, P13254) — that is a separate gene; sequence identity to it (41.1%) is lower than to *E. coli* MetC (43.9%).
- No evidence that PP_4348 acts in reverse transsulfuration (methionine → cysteine); *P. putida* lacks the requisite γ-lyase.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the PP_4348 gene product specifically.** Vermeij & Kertesz (1999) measured cystathionine β-lyase *enzyme activity* in *P. putida* but did not link that activity to the PP_4348 locus by genetics or purification. The residue-level and reaction assignments for PP_4348 rest on high-confidence homology inference from *E. coli* MetC, not on a purified PP_4348 protein. Kinetic parameters (kcat, Km for L-cystathionine) for the PP_4348 enzyme are unknown.

2. **The Vermeij & Kertesz work used *P. putida* S-313, not strain KT2440.** These are closely related and the pathway logic is expected to be conserved, but strain-level regulatory differences are possible.

3. **EC-number ambiguity (4.4.1.8 vs 4.4.1.13).** UniProt and KEGG differ. The interpretation here — that this reflects catalytic promiscuity of a single active site — is well supported by family literature but has not been experimentally resolved for PP_4348 itself. The relative in vivo importance of the cysteine-S-conjugate β-lyase side activity is unquantified.

4. **Alignment identities among family members are close (41–44%).** The β-lyase assignment relies on the InterPro bacterial-CBL signature and the direction of the identity ranking rather than a large margin. A crystal structure or biochemical assay would remove any residual uncertainty.

5. **Regulatory circuitry not defined at the gene level.** The trans-acting regulators controlling PP_4348's cysteine-inducible, sulfur-source–dependent expression in KT2440 (e.g., a CysB/MetR-type regulator) have not been identified.

6. **Localization is inferred**, not experimentally fractionated — it rests on absence of secretion/membrane signals plus the cytosolic nature of the pathway.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzymology.** Clone PP_4348 from KT2440, express with an affinity tag, purify, and measure steady-state kinetics for L,L-cystathionine (expected products: L-homocysteine, pyruvate, NH₄⁺). Determine kcat and Km and compare to *E. coli* MetC. Assay UV-vis for the characteristic PLP internal aldimine (~420 nm).

2. **Substrate-specificity panel.** Test the purified enzyme against L-cystathionine, cysteine-S-conjugates, alliin/S-alk(en)yl-L-cysteine sulfoxides, djenkolate, and O-acetyl/O-succinylhomoserine to quantify the physiological reaction versus promiscuous activities, directly resolving the EC 4.4.1.8 vs 4.4.1.13 question.

3. **Genetic knockout and complementation.** Construct a ΔPP_4348 mutant in KT2440; test methionine auxotrophy/growth phenotypes under different sulfur sources (sulfate, cysteine, methionine). Predicted outcome: a conditional methionine requirement most pronounced when cysteine is the sole sulfur source, given the dominant direct-sulfhydrylation route.

4. **Active-site validation by mutagenesis.** Substitute Lys186 (catalytic PLP lysine) and the specificity tyrosines (Tyr35, Tyr91, Tyr312) to confirm the homology-based residue assignments and quantify their catalytic contributions, mirroring the *E. coli* Lodha & Aitken (2011) study.

5. **Structural determination or modeling.** Solve a crystal structure (or generate a validated AlphaFold model with PLP docked) to confirm the fold-type I homotetramer and the geometry that positions cystathionine sulfur in the γ-position for β-elimination.

6. **Expression profiling in KT2440.** Use RT-qPCR or RNA-seq across sulfur sources (sulfate vs. cysteine vs. methionine) to confirm cysteine-inducible expression of PP_4348 specifically in KT2440 and identify the responsible regulator.

---

## Conclusion

PP_4348 (Q88EV4) of *Pseudomonas putida* KT2440 is a cytoplasmic, PLP-dependent **cystathionine β-lyase (MetC, EC 4.4.1.8)** that cleaves the Cβ–S bond of L,L-cystathionine to produce L-homocysteine, pyruvate, and ammonia — the transsulfuration step of methionine biosynthesis (KEGG M00017). The assignment is supported by convergent, mutually consistent evidence: diagnostic bacterial-CBL InterPro/Pfam signatures, full conservation of the experimentally validated *E. coli* MetC active site (including the PLP Schiff-base Lys186), correct pathway placement, and direct enzymological detection of cysteine-inducible cystathionine β-lyase activity in *P. putida*. In this organism the enzyme runs only in the forward, cysteine → methionine direction (no reverse transsulfuration) and supplements the dominant direct-sulfhydrylation route. The gene symbol, organism, and protein family are unambiguous — there is no confounding gene-symbol conflict.


## Artifacts

- [OpenScientist final report](PP_4348-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_4348-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:39644606
2. PMID:8831789
3. PMID:10482527
4. PMID:9165088
5. PMID:12715888
6. PMID:21958132
7. PMID:38810088
8. PMID:29592871