---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-16T10:41:50.083955'
end_time: '2026-07-16T12:30:37.120044'
duration_seconds: 6527.04
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rfbC
  gene_symbol: rfbC
  uniprot_accession: Q88LZ4
  protein_description: 'RecName: Full=dTDP-4-dehydrorhamnose 3,5-epimerase {ECO:0000256|ARBA:ARBA00019595,
    ECO:0000256|RuleBase:RU364069}; EC=5.1.3.13 {ECO:0000256|ARBA:ARBA00012098, ECO:0000256|RuleBase:RU364069};
    AltName: Full=Thymidine diphospho-4-keto-rhamnose 3,5-epimerase {ECO:0000256|RuleBase:RU364069};'
  gene_info: Name=rfbC {ECO:0000313|EMBL:AAN67402.1}; OrderedLocusNames=PP_1782 {ECO:0000313|EMBL:AAN67402.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the dTDP-4-dehydrorhamnose 3,5-epimerase family.
  protein_domains: RmlC-like. (IPR000888); RmlC-like_jellyroll. (IPR014710); RmlC_Cupin_sf.
    (IPR011051); dTDP_sugar_isom (PF00908)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: rfbC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rfbC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LZ4
- **Protein Description:** RecName: Full=dTDP-4-dehydrorhamnose 3,5-epimerase {ECO:0000256|ARBA:ARBA00019595, ECO:0000256|RuleBase:RU364069}; EC=5.1.3.13 {ECO:0000256|ARBA:ARBA00012098, ECO:0000256|RuleBase:RU364069}; AltName: Full=Thymidine diphospho-4-keto-rhamnose 3,5-epimerase {ECO:0000256|RuleBase:RU364069};
- **Gene Information:** Name=rfbC {ECO:0000313|EMBL:AAN67402.1}; OrderedLocusNames=PP_1782 {ECO:0000313|EMBL:AAN67402.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the dTDP-4-dehydrorhamnose 3,5-epimerase family.
- **Key Domains:** RmlC-like. (IPR000888); RmlC-like_jellyroll. (IPR014710); RmlC_Cupin_sf. (IPR011051); dTDP_sugar_isom (PF00908)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rfbC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rfbC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rfbC** (gene ID: rfbC, UniProt: Q88LZ4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *rfbC* (PP_1782, UniProt Q88LZ4) in *Pseudomonas putida* KT2440

**Gene:** *rfbC* (synonym *rmlC*) — Ordered locus **PP_1782**
**Protein:** dTDP-4-dehydrorhamnose 3,5-epimerase (RmlC)
**UniProt:** Q88LZ4 · **EC:** 5.1.3.13 · **Length:** 182 aa · **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / **KT2440**)

## Summary

**rfbC** (ordered locus **PP_1782**; UniProt **Q88LZ4**) of *Pseudomonas putida* strain KT2440 (PSEPK) encodes **dTDP-4-dehydrorhamnose 3,5-epimerase**, universally known as **RmlC** (EC 5.1.3.13). It is a 182-residue cytoplasmic enzyme that catalyzes the **third step** of the four-enzyme **RmlABCD pathway** that converts glucose-1-phosphate into **dTDP-L-rhamnose**, the activated nucleotide-sugar donor of L-rhamnose. The identification is unambiguous: the gene symbol, EC number, Pfam/InterPro domain architecture (RmlC-like cupin jelly-roll, PF00908), KEGG orthology (K01790), and genomic context all converge on the same assignment, and the sequence is **62.6% identical** to the biochemically and structurally characterized RmlC of *Salmonella* Typhimurium, with **complete conservation of every catalytic and substrate-binding residue**. This report therefore proceeds with high confidence that rfbC/Q88LZ4 is a *bona fide* RmlC epimerase.

Mechanistically, RmlC performs a **cofactor-independent double epimerization** at the C3′ and C5′ positions of its substrate: it converts **dTDP-4-dehydro-6-deoxy-α-D-glucose (dTDP-6-deoxy-D-*xylo*-4-hexulose)** into **dTDP-4-dehydro-β-L-rhamnose (dTDP-6-deoxy-L-*lyxo*-4-hexulose)** (Rhea RHEA:16969). Unlike most carbohydrate-modifying enzymes, RmlC requires **no NAD(P)H, no metal ion, and no external cofactor**; it uses the substrate's own C4′ keto group to acidify the flanking C3′/C5′ protons, then catalyzes acid/base **1,1-proton transfers** through a conserved pair of active-site histidines (His62/His119 in Q88LZ4). Structurally, RmlC adopts a **cupin (RmlC-like jelly-roll) β-sandwich fold** and functions as a **homodimer**, with the active site formed at the dimer interface by residues contributed from both subunits. An AlphaFold model of Q88LZ4 (mean pLDDT 97.6) confirms this fold and places all inferred catalytic residues with very high confidence.

Biologically, the dTDP-L-rhamnose produced by this pathway is the sugar donor for **rhamnosylation of cell-surface glycans**. In *P. putida* KT2440, rfbC sits within a complete *rml* operon (rfbA/rfbC/rfbD/rffG = rmlABCD) embedded in a **lipopolysaccharide (LPS) / O-antigen biosynthesis gene cluster**, indicating that its physiological output feeds **cell-envelope surface-polysaccharide biosynthesis**. Because the entire dTDP-L-rhamnose pathway is **absent in humans** yet contributes to the cell wall and virulence of many bacteria, RmlC is a well-recognized **antibacterial drug target**. The enzyme carries out its function in the **cytosol**, upstream of membrane-associated glycosyltransfer and LPS export steps.

---

## Key Findings

### Finding 1 — rfbC/PP_1782 encodes dTDP-4-dehydrorhamnose 3,5-epimerase (RmlC; EC 5.1.3.13)

The primary identity of the gene product is firmly established by convergent database annotation. UniProt entry **Q88LZ4** gives the recommended name *dTDP-4-dehydrorhamnose 3,5-epimerase* with EC number **5.1.3.13**, a length of 182 amino acids, gene name **rfbC** (ordered locus **PP_1782**), and organism *Pseudomonas putida* KT2440. The catalytic activity is registered as **Rhea RHEA:16969**: *dTDP-4-dehydro-6-deoxy-α-D-glucose = dTDP-4-dehydro-β-L-rhamnose* (ChEBI 57649 → 62830). The protein contains a single Pfam domain, **PF00908 (dTDP_sugar_isom)**, and InterPro assigns the **RmlC-like cupin jelly-roll** signatures (IPR000888, IPR014710, IPR011051). Its KEGG ortholog is **K01790 (rfbC/rmlC)**. The functional assignment in UniProt is **rule-based** (RuleBase RU364069 / ARBA), which is why independent corroboration (Findings 4 and 6) is valuable. The **3,5-epimerase** designation reflects the enzyme's double inversion of stereochemistry at both C3′ and C5′ of the hexose ring.

### Finding 2 — rfbC operates in cytosolic dTDP-L-rhamnose biosynthesis (RmlABCD / KEGG module M00793)

The enzyme's role in a defined metabolic pathway is well annotated. UniProt lists the **PATHWAY** as "Carbohydrate biosynthesis; dTDP-L-rhamnose biosynthesis," and Gene Ontology terms include **dTDP-rhamnose biosynthetic process (GO:0019305)**, **polysaccharide biosynthetic process (GO:0000271)**, **dTDP-4-dehydrorhamnose 3,5-epimerase activity (GO:0008830)**, and subcellular localization **cytosol (GO:0005829)**. The **SUBUNIT** annotation is **homodimer**. The reaction is step three of **KEGG module M00793** (dTDP-L-rhamnose biosynthesis, Glc-1P ⇒ dTDP-L-Rha) and appears on KEGG pathway maps for nucleotide sugar metabolism (ppu00541), polyketide sugar unit biosynthesis (ppu00523), and streptomycin biosynthesis (ppu00521). The gene occupies genomic coordinates complement(1996039..1996587). Thus the enzyme acts in the **cytoplasm** as part of a soluble biosynthetic route that produces an activated nucleotide sugar.

### Finding 3 — rfbC lies within a complete *rml* operon inside an LPS/O-antigen biosynthesis locus

The physiological destination of the pathway's product is revealed by genomic context. In *P. putida* KT2440, the four *rml* genes are clustered and co-oriented (all on the complement strand):

| Locus | Gene | Enzyme | Pathway step |
|-------|------|--------|--------------|
| PP_1783 | rfbA (rmlA) | glucose-1-phosphate thymidylyltransferase | 1 |
| PP_1785 | rffG (rmlB) | dTDP-glucose 4,6-dehydratase | 2 |
| **PP_1782** | **rfbC (rmlC)** | **dTDP-4-dehydrorhamnose 3,5-epimerase** | **3** |
| PP_1784 | rfbD (rmlD) | dTDP-4-dehydrorhamnose reductase | 4 |

Immediately adjacent genes include PP_1786 (putative glycosyltransferase), PP_1780 (putative mannosyltransferase), PP_1781 (putative O-acyltransferase), and PP_1779 (LPS ABC export system ATP-binding protein). rfbC and rfbA share/abut coordinates (…1996587), consistent with operonic co-transcription. This neighborhood — nucleotide-sugar synthesis genes packaged together with glycosyltransferases, an acyltransferase, and an LPS export transporter — is the signature of a **lipopolysaccharide / O-antigen biosynthesis cluster**, and it localizes the biological purpose of rfbC to **cell-surface glycan (LPS O-antigen) construction**.

### Finding 4 — RmlC is a cofactor-independent "new class" epimerase with a cupin β-sandwich dimer fold; active site at the dimer interface

The mechanistic and structural basis of RmlC catalysis comes from precise primary studies of the *Salmonella* enzyme. Biochemically, **Stern et al. (1999)** purified *Salmonella* Typhimurium LT2 RmlC and demonstrated by spectrofluorometry and radiolabeling that it catalyzes **NAD(P)H-independent** formation of dTDP-6-deoxy-L-*lyxo*-4-hexulose from dTDP-6-deoxy-D-*xylo*-4-hexulose, establishing RmlC as the 3,5-epimerase distinct from the NAD(P)H-dependent RmlD reductase [PMID: 10455186]. Structurally, **Giraud et al. (2000)** solved the *Salmonella* RmlC crystal structure at 2.17 Å, showing it is a **homodimer** in which each monomer folds into two β-sheets forming a **β-sandwich (cupin / jelly-roll)** — precisely matching the Q88LZ4 InterPro/Pfam signatures (IPR011051, IPR014710, PF00908). A dTDP-phenol complex revealed a substrate-binding site nestled between the two β-sheets and formed by residues from **both monomers**, "very highly conserved" across RmlC enzymes, and the authors declared RmlC "the first example of a new class of carbohydrate epimerase" [PMID: 10802738]. Mechanistic reviews describe the C3′/C5′ epimerization as proceeding through the substrate's C4′ **keto intermediate** by cofactor-independent **1,1-proton-transfer** acid/base catalysis, with **no metal and no NAD⁺** required [PMID: 11706991; PMID: 34027955].

### Finding 5 — The dTDP-L-rhamnose pathway is absent in humans and is a validated antibacterial target

L-Rhamnose is a bacterial cell-surface sugar with no counterpart in human biochemistry, which makes its biosynthetic enzymes attractive drug targets. Giraud et al. noted that the dTDP-L-rhamnose pathway "does not exist in humans" and that its enzymes are "potential targets for the design of new therapeutic agents" [PMID: 10802738]. Rhamnose sugars are "present in bacteria but not mammals, making them potentially useful as antibacterial agents," with dTDP-rhamnose being the most common rhamnose donor produced by RmlA/B/C/D [PMID: 36014553]. Functionally, an L-rhamnosyl residue "plays an essential structural role in the cell wall of *Mycobacterium tuberculosis*," making RmlA–RmlD "important targets" [PMID: 11302803]. More recently, dTDP-L-rhamnose biosynthesis was shown to be "critical for the viability and virulence of many human pathogenic bacteria," and the inhibitor Ri03 (targeting RmlB/RmlC/GacA) blocked growth of *Streptococcus* and *M. tuberculosis* (IC50 120–410 µM) [PMID: 30600561]. While *P. putida* KT2440 is itself a benign soil saprophyte, this cross-species evidence underlines the **conserved, target-worthy biochemistry** that rfbC embodies.

### Finding 6 — *P. putida* RfbC conserves all RmlC catalytic residues and is 62.6% identical to characterized *Salmonella* RmlC

Because the UniProt annotation is rule-based, direct sequence evidence was gathered to validate it. A global Needleman–Wunsch alignment of Q88LZ4 against the biochemically and structurally characterized *Salmonella* Typhimurium RmlC (UniProt P26394) gave **114/182 identical residues (62.6%)**, versus 41.4% against *M. tuberculosis* RmlC (P9WH11). Crucially, **every** residue implicated in *Salmonella* RmlC catalysis and substrate binding maps to an identical residue in Q88LZ4:

| Role | *Salmonella* RmlC | *P. putida* RfbC (Q88LZ4) |
|------|-------------------|----------------------------|
| Catalytic His (base/acid) | His63 | **His62** |
| Catalytic His (base/acid) | His120 | **His119** |
| Active-site Tyr | Tyr139 | **Tyr138** |
| Active-site Asp | Asp170 | **Asp169** |
| Substrate contact (Glu) | Glu23 | **Glu22** |
| Substrate contact (Arg) | Arg76 | **Arg75** |
| Substrate contact (Thr) | Thr124 | **Thr123** |

The hallmark active-site motif **"PGFAHGF"** (containing His119) is present at positions 115–121 of Q88LZ4, and conservation is continuous across the entire 182-residue cupin β-sandwich. This provides strong, residue-level confirmation that rfbC/Q88LZ4 is a functional RmlC 3,5-epimerase, not merely a family homolog.

### Finding 7 — AlphaFold model of Q88LZ4 is very high confidence and supports the RmlC cupin fold and catalytic-residue placement

The AlphaFold DB model for Q88LZ4 (full length 1–182, v6) has a **mean per-residue pLDDT of 97.6** (median 98.2); 100% of residues are "confident" (pLDDT > 70) and 99% are "very high" (pLDDT > 90). All inferred catalytic/active-site residues are modeled at very high confidence: His62 (98.6), His119 (98.9), Tyr138 (97.4), Asp169 (97.9), Glu22 (96.8), Arg75 (98.8), and Thr123 (98.9). The predicted structure recapitulates the cupin/jelly-roll β-sandwich expected of an RmlC monomer, and the near-perfect confidence at the catalytic positions reinforces the homology-based active-site mapping from Finding 6.

---

## Mechanistic Model / Interpretation

### The reaction

RmlC (rfbC) catalyzes the third of four sequential reactions that build dTDP-L-rhamnose from glucose-1-phosphate. Its specific transformation is a **double epimerization**:

```
        RmlA            RmlB                RmlC                RmlD
Glc-1-P ────► dTDP-D-glucose ──► dTDP-4-keto-6-deoxy-D-glucose ──► dTDP-4-keto-6-deoxy-L-mannose ──► dTDP-L-rhamnose
      (+dTTP)          (4,6-dehydratase)   (dTDP-6-deoxy-D-xylo-    (dTDP-6-deoxy-L-lyxo-            (+NADPH)
                                            4-hexulose)              4-hexulose)
                                            │                        │
                                            └── epimerization at ────┘
                                                C3′ AND C5′ (RmlC, EC 5.1.3.13)
```

The substrate, **dTDP-4-dehydro-6-deoxy-α-D-glucose**, carries a keto group at C4′ (installed by RmlB). RmlC inverts the configuration at **both C3′ and C5′**, producing **dTDP-4-dehydro-β-L-rhamnose**. RmlD then reduces the C4′ keto group (using NADPH) to yield dTDP-L-rhamnose.

### Why no cofactor is needed

The elegance of RmlC lies in its use of the substrate's own chemistry. The C4′ carbonyl is electron-withdrawing and **acidifies the adjacent C3′ and C5′ protons**, allowing them to be removed by an active-site base to form a transient enolate stabilized by the keto group. Reprotonation from the opposite face inverts the stereocenter. Because the keto group is already present, RmlC needs **no NAD⁺ redox cycling** (contrast with epimerases that transiently oxidize the sugar) and **no metal ion** — a defining feature that led to its designation as "a new class of carbohydrate epimerase" [PMID: 10802738; PMID: 11706991; PMID: 34027955]. The paired histidines (His62/His119 in *P. putida* numbering) act as the general acid and general base flanking the sugar, with additional residues (Tyr138, Asp169, Glu22, Arg75, Thr123) orienting the substrate and stabilizing charge.

### Quaternary structure and localization

RmlC is an **obligate homodimer** with a **cupin (RmlC-like jelly-roll) β-sandwich** fold. The active site sits at the **dimer interface** and draws residues from both protomers, so dimerization is functionally required. The enzyme is **soluble and cytoplasmic** (GO:0005829); it produces a diffusible nucleotide sugar that is subsequently handed off to membrane-associated glycosyltransferases.

### Biological pathway context

```
   CYTOPLASM                                          MEMBRANE / CELL SURFACE
   ─────────────────────────────────────────         ─────────────────────────────
   Glc-1-P → ... → dTDP-L-rhamnose  ──────────►  glycosyltransferases (e.g. PP_1786)
             (RmlA/B/C/D operon,                       │  add L-rhamnose to growing
              PP_1782–1785)                            ▼  O-antigen / surface glycan
                                                  LPS assembly + ABC export (PP_1779)
                                                       │
                                                       ▼
                                                  O-antigen displayed on outer membrane
```

The clustering of rfbC with glycosyltransferase, mannosyltransferase, O-acyltransferase, and LPS-export genes (Finding 3) shows that the dTDP-L-rhamnose it helps make is destined for **cell-surface polysaccharide (LPS O-antigen) biosynthesis**. rfbC's role is thus upstream and metabolic: it supplies the activated rhamnose building block, while downstream membrane enzymes incorporate and export it.

---

## Evidence Base

| PMID | Study (organism / focus) | How it supports the findings |
|------|--------------------------|------------------------------|
| [PMID: 10455186](https://pubmed.ncbi.nlm.nih.gov/10455186/) | Stern et al. 1999, *Salmonella* RmlC biochemistry | Direct enzymatic proof that RmlC is the NAD(P)H-**independent** 3,5-epimerase, distinct from RmlD; defines the exact substrate → product conversion. Underpins Findings 4 and 6. |
| [PMID: 10802738](https://pubmed.ncbi.nlm.nih.gov/10802738/) | Giraud et al. 2000, *Salmonella* RmlC crystal structure (2.17 Å) | Establishes the cupin β-sandwich homodimer fold, dimer-interface active site, "new class of carbohydrate epimerase," and human-absent drug-target rationale. Underpins Findings 4 and 5. |
| [PMID: 11706991](https://pubmed.ncbi.nlm.nih.gov/11706991/) | Mechanistic review of RmlC-type epimerization | Details the cofactor-independent 1,1-proton-transfer acid/base mechanism via the C4′ keto intermediate. Underpins Finding 4. |
| [PMID: 34027955](https://pubmed.ncbi.nlm.nih.gov/34027955/) | Review of sugar-nucleotide epimerase mechanisms | Reaffirms the metal-free, NAD⁺-free keto-assisted epimerization mechanism. Underpins Finding 4. |
| [PMID: 11302803](https://pubmed.ncbi.nlm.nih.gov/11302803/) | *M. tuberculosis* rhamnose / cell wall | Shows L-rhamnosyl residues are essential cell-wall components and RmlA–RmlD are important targets. Underpins Finding 5. |
| [PMID: 30600561](https://pubmed.ncbi.nlm.nih.gov/30600561/) | Inhibitor (Ri03) study of dTDP-L-rhamnose pathway | Demonstrates pathway criticality for viability/virulence and druggability (IC50 120–410 µM). Underpins Finding 5. |
| [PMID: 36014553](https://pubmed.ncbi.nlm.nih.gov/36014553/) | Review of bacterial rhamnose biology | Confirms rhamnose is bacterial-specific, dTDP-Rha is the dominant donor, produced by RmlA/B/C/D. Underpins Findings 2 and 5. |

The homology and structural analyses (Findings 6 and 7) were generated in this investigation using pairwise sequence alignment against characterized reference enzymes and the public AlphaFold model of Q88LZ4; they translate the *Salmonella* primary evidence directly onto the *P. putida* protein.

---

## Supported and Refuted Hypotheses

- **Supported:** rfbC/Q88LZ4 is a functional RmlC dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) — supported by annotation convergence, 62.6% identity to characterized *Salmonella* RmlC, complete active-site conservation, and a very-high-confidence AlphaFold fold.
- **Supported:** The enzyme acts in the cytosol within the RmlABCD dTDP-L-rhamnose pathway, feeding LPS/O-antigen biosynthesis — supported by GO/KEGG annotation and operon/genomic-context analysis.
- **Supported:** RmlC uses a cofactor-independent, metal-free acid/base epimerization mechanism via a conserved histidine pair — supported by orthologous biochemistry, structure, and mechanistic reviews.
- **No hypothesis was refuted.** The gene symbol "rfbC" was verified to match the correct protein and organism; no divergent same-symbol gene misled the analysis.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on Q88LZ4 itself.** All enzymatic, mechanistic, and structural evidence derives from orthologs (chiefly *Salmonella* RmlC). The functional assignment for *P. putida* rfbC rests on rule-based annotation plus strong homology (62.6% identity, complete active-site conservation) — very high confidence, but not a direct kinetic or crystallographic demonstration of the KT2440 enzyme.

2. **UniProt annotation is rule-based (RuleBase RU364069 / ARBA).** This is why the sequence and structural corroboration matter; the annotation was not derived from experiments on this specific protein.

3. **AlphaFold models a monomer, not the biological dimer.** The very high pLDDT (97.6) validates the fold and residue positions but does not directly model the dimer interface or a bound substrate; the dimeric active-site geometry is inferred from the *Salmonella* structure.

4. **Downstream fate not experimentally traced in KT2440.** The routing of dTDP-L-rhamnose into a specific *P. putida* O-antigen/LPS structure is inferred from genomic context (the surrounding glycosyltransferase/export genes), not from characterized glycan structures or mutant phenotypes in this strain.

5. **Operon transcription not experimentally confirmed here.** Co-orientation and abutting coordinates strongly suggest operonic organization, but transcript-level evidence (RNA-seq/operon mapping) was not examined.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology of Q88LZ4.** Express and purify *P. putida* RfbC and measure 3,5-epimerase activity on dTDP-6-deoxy-D-*xylo*-4-hexulose (coupled with RmlA/B/D), confirming the NAD(P)H-independent conversion and determining kinetic constants (k_cat, K_m).

2. **Active-site mutagenesis.** Test the predicted catalytic pair by making His62Ala and His119Ala variants; loss of epimerase activity would experimentally confirm the mechanistic model transferred from *Salmonella*.

3. **Structure determination or cryo-EM of the dimer.** Crystallize KT2440 RfbC (ideally with dTDP-sugar or dTDP-phenol) to verify the dimer-interface active site directly, rather than relying on the AlphaFold monomer.

4. **Genetic knockout and LPS phenotyping.** Delete PP_1782 in KT2440 and characterize the resulting LPS/O-antigen by gel electrophoresis and glycan analysis to establish the physiological requirement for rhamnose in the *P. putida* surface polysaccharide.

5. **Operon mapping.** Use RT-PCR or RNA-seq to confirm co-transcription of PP_1782–PP_1785 and delineate the promoter/terminator boundaries of the *rml*/LPS locus.

6. **Complementation across species.** Test whether Q88LZ4 complements an *rmlC*-deficient strain of a model organism, providing an *in vivo* functional confirmation of the annotation.

---

## Conclusion

**rfbC** (PP_1782; UniProt Q88LZ4) of *Pseudomonas putida* KT2440 encodes **dTDP-4-dehydrorhamnose 3,5-epimerase (RmlC; EC 5.1.3.13)**, a 182-residue cytoplasmic, homodimeric cupin-fold enzyme that catalyzes the third step of the RmlABCD dTDP-L-rhamnose pathway — a **cofactor-independent double epimerization at C3′ and C5′** of dTDP-6-deoxy-D-*xylo*-4-hexulose to give dTDP-6-deoxy-L-*lyxo*-4-hexulose (RHEA:16969) via an acid/base 1,1-proton-transfer mechanism using a conserved histidine pair (His62/His119). The dTDP-L-rhamnose it helps produce is the activated donor for **rhamnosylation of cell-surface glycans**, and the gene lies within a complete *rml* operon embedded in an **LPS/O-antigen biosynthesis locus**, serving cell-envelope surface-polysaccharide biosynthesis. This assignment is strongly corroborated by 62.6% identity and complete active-site-residue conservation relative to the biochemically and structurally characterized *Salmonella* RmlC [PMID: 10455186, 10802738], plus a very-high-confidence AlphaFold model (mean pLDDT 97.6).


## Artifacts

- [OpenScientist final report](rfbC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rfbC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10455186
2. PMID:10802738
3. PMID:11706991
4. PMID:34027955
5. PMID:36014553
6. PMID:11302803
7. PMID:30600561