---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T04:12:15.337411'
end_time: '2026-07-17T04:39:41.473264'
duration_seconds: 1646.14
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_5147
  gene_symbol: PP_5147
  uniprot_accession: Q88CN3
  protein_description: 'RecName: Full=Histidinol-phosphatase {ECO:0000256|ARBA:ARBA00021697};
    EC=3.1.3.15 {ECO:0000256|ARBA:ARBA00013085}; AltName: Full=Histidinol-phosphate
    phosphatase {ECO:0000256|ARBA:ARBA00033209};'
  gene_info: OrderedLocusNames=PP_5147 {ECO:0000313|EMBL:AAN70712.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the HAD-like hydrolase superfamily. SerB family.
  protein_domains: HAD-like_SerB. (IPR050582); HAD-like_sf. (IPR036412); HAD_hydro_SerB1.
    (IPR006385); HAD_sf. (IPR023214); HAD (PF12710)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_5147-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_5147-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88CN3
- **Protein Description:** RecName: Full=Histidinol-phosphatase {ECO:0000256|ARBA:ARBA00021697}; EC=3.1.3.15 {ECO:0000256|ARBA:ARBA00013085}; AltName: Full=Histidinol-phosphate phosphatase {ECO:0000256|ARBA:ARBA00033209};
- **Gene Information:** OrderedLocusNames=PP_5147 {ECO:0000313|EMBL:AAN70712.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the HAD-like hydrolase superfamily. SerB family.
- **Key Domains:** HAD-like_SerB. (IPR050582); HAD-like_sf. (IPR036412); HAD_hydro_SerB1. (IPR006385); HAD_sf. (IPR023214); HAD (PF12710)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_5147" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_5147' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_5147** (gene ID: PP_5147, UniProt: Q88CN3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_5147 (Q88CN3): The Cytoplasmic HAD-Type Histidinol-Phosphate Phosphatase of *Pseudomonas putida* KT2440

**Gene:** PP_5147 (OrderedLocusNames) · **UniProt:** Q88CN3 (Q88CN3_PSEPK) · **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) · **Length:** 218 aa (~24.9 kDa) · **EC:** 3.1.3.15

---

## Summary

**PP_5147** (UniProt **Q88CN3**; OrderedLocusName PP_5147) of *Pseudomonas putida* KT2440 encodes a soluble, cytoplasmic **histidinol-phosphate phosphatase** (HolPase; **EC 3.1.3.15**). Its primary and essentially sole physiological function is to catalyze the **Mg²⁺-dependent hydrolysis of L-histidinol-phosphate to L-histidinol plus inorganic phosphate** (Rhea:14465), the **penultimate (8th) step of the de novo L-histidine biosynthesis pathway**. This is a classic housekeeping anabolic enzyme: it operates in the cytoplasm, where the entire histidine biosynthetic pathway resides, and its product histidinol is subsequently oxidized to L-histidine by histidinol dehydrogenase (HisD).

The enzyme belongs to the **HAD-like (haloacid dehalogenase) hydrolase superfamily**, specifically **subfamily IB**, historically referred to as the "SerB1-like" or "HisB-N" group. Three unrelated protein families independently solved the HolPase reaction across the tree of life — the **HAD-type** used by Gammaproteobacteria (including *Pseudomonas*), the **PHP-type** used by Firmicutes and yeast, and the **IMPase-like (HisN)** type used by Actinobacteria and plants. PP_5147 is the **HAD-type**. Its assignment rests on convergent evidence: database orthology (KEGG K28842, InterPro IPR006385, COG0560); a complete, canonical four-motif HAD catalytic apparatus resolved in a high-confidence AlphaFold model (mean pLDDT 96.2); and **67.7% amino-acid identity to the experimentally validated ortholog PA0335 of *P. aeruginosa***, whose deletion produces (incomplete) histidine auxotrophy.

The "SerB family" label attached to this protein reflects **HAD fold homology only** and does not indicate a role in serine biosynthesis: *P. putida* KT2440 carries a genuinely distinct phosphoserine phosphatase (*serB* = PP_4909) together with a complete serine pathway (*serA*, *serC*). PP_5147 is therefore a **dedicated histidine-biosynthesis enzyme**. It is the physiologically **dominant** HolPase but is buffered by promiscuous HAD phosphatases carrying weak "side" HolPase activity (in the *P. aeruginosa* ortholog these are PA3255 and PA1143), which explains why loss of the primary gene causes only incomplete rather than absolute histidine auxotrophy. Evolutionarily, the HAD-type HolPase lineage arose from a promiscuous **GmhB-like sugar-bisphosphate phosphatase** ancestor, accounting for its residual substrate ambiguity.

---

## Identity Verification

Before proceeding, the target identity was confirmed against all provided criteria:

- **Gene symbol match:** PP_5147 is annotated in UniProt (Q88CN3), KEGG (*ppu:PP_5147*), and EMBL (AAN70712.1) as a histidinol-phosphatase — consistent with the protein description.
- **Organism match:** All literature and database evidence pertains to *Pseudomonas putida* KT2440 or its close relative *P. aeruginosa* (used for the orthologous experimental validation).
- **Family/domain match:** The HAD-like hydrolase superfamily / SerB family and domains (IPR050582, IPR036412, IPR006385, IPR023214, PF12710) are all consistent with the HAD-type HolPase identified here.

No conflicting literature for a differently-named gene was encountered. The assignment is coherent and well supported.

---

## Key Findings

### F001 — PP_5147 is a HAD-superfamily histidinol-phosphate phosphatase (EC 3.1.3.15) catalyzing the penultimate step of L-histidine biosynthesis

The core functional assignment is unambiguous across all major protein databases. UniProt Q88CN3 (218 amino acids) annotates the protein as "Histidinol-phosphatase" with the catalytic activity **L-histidinol phosphate + H₂O = L-histidinol + phosphate** (Rhea:14465, EC 3.1.3.15), and places it in **L-histidine biosynthesis, step 8 of 9**. KEGG assigns *ppu:PP_5147* the orthology **K28842** (histidinol-phosphatase, EC 3.1.3.15), maps it to pathway **ppu00340 (Histidine metabolism)**, and to module **M00026 (Histidine biosynthesis, PRPP ⇒ histidine)**. eggNOG places it in **COG0560**. The protein retains an intact HAD catalytic motif I — **D7-x-D9-x-T11 ("DLDNT")** — with **Asp7** serving as the aspartyl nucleophile, and carries the magnesium/metal-binding keyword.

Critically, the HolPase reaction is served by **three unrelated protein families** — the HAD-type known from Gammaproteobacteria such as *E. coli* and *Salmonella*, the PHP-type known from yeast and Firmicutes such as *Bacillus subtilis*, and the IMPase-like (HisN) type in Actinobacteria — and PP_5147 belongs firmly to the **HAD-type**, consistent with its *Pseudomonas* (Gammaproteobacterial) origin. As stated by Kinateder and colleagues, "*Three unrelated HolPase families are known so far... HAD-type HolPases known from Gammaproteobacteria like Escherichia coli or Salmonella enterica and PHP-type HolPases known from yeast and Firmicutes like Bacillus subtilis*" ([PMID: 28720084](https://pubmed.ncbi.nlm.nih.gov/28720084/)). The enzyme's position in the pathway is likewise confirmed: HolPase "*is responsible for the penultimate step of histidine biosynthesis*" ([PMID: 31862725](https://pubmed.ncbi.nlm.nih.gov/31862725/)).

### F002 — PP_5147 is a close ortholog (67.7% identity) of the experimentally validated HolPase PA0335 of *P. aeruginosa*

The strongest line of experimental support comes from the orthologous relationship with a functionally characterized enzyme. A Needleman–Wunsch global alignment of Q88CN3 (PP_5147, 218 aa) against **PA0335** (217 aa, *P. aeruginosa*) yields **147/217 identical positions = 67.7% identity** over the full length with no large gaps, including a nearly identical N-terminal HAD motif I ("MRLALFDLDNTL..."). Both proteins share KEGG orthology **K28842**, **COG0560**, and the HAD subfamily IB / SerB1-like fold (**InterPro IPR006385**, which explicitly lists the *Pseudomonas aeruginosa* histidinol-phosphatase).

The ortholog PA0335 has been characterized both genetically and biochemically. Gene knockout of PA0335 causes L-histidine auxotrophy in *P. aeruginosa*, and it encodes a HAD-family HolPase: "*We previously reported that PA0335 encode a HolPase belonging to the HAD family and inactivation resulted [in] complete L-histidine auxotrophy in Pseudomonas aeruginosa*" ([PMID: 40596842](https://pubmed.ncbi.nlm.nih.gov/40596842/)). The primary identification paper describes "*PA0335, a Gene Encoding Histidinol Phosphate Phosphatase, Mediates Histidine Auxotrophy*" ([PMID: 31862725](https://pubmed.ncbi.nlm.nih.gov/31862725/)). At 67.7% identity, PP_5147 is a confident functional ortholog of this validated enzyme.

| Property | PP_5147 (*P. putida*) | PA0335 (*P. aeruginosa*) |
|---|---|---|
| Length | 218 aa | 217 aa |
| KEGG orthology | K28842 | K28842 |
| COG | COG0560 | COG0560 |
| HAD motif I | FDLDNT | FDLDNT |
| Global identity | — | 67.7% vs PP_5147 |
| Experimental phenotype | inferred | deletion → histidine auxotrophy |

### F003 — *P. putida* uses a monofunctional hisB and supplies HolPase activity from the standalone gene PP_5147

Unlike *E. coli*, which fuses imidazoleglycerol-phosphate dehydratase and histidinol-phosphatase into a single bifunctional **HisB** protein, *P. putida* KT2440 uses a **monofunctional imidazoleglycerol-phosphate dehydratase** (*hisB*, EC 4.2.1.19, KO **K01693** = **PP_0289**), located in the *his* gene cluster (PP_0289–PP_0293, with *hisH* PP_0290, *hisF* PP_0292). A search for the bifunctional IGPD/HolPase fusion (E. coli HisB, KO K01089) returns **no gene** in *P. putida*. The HolPase activity is instead supplied by the physically separate, **non-operonic** gene **PP_5147**, whose genomic neighbors (PtsP/PP_5145, an RNA pyrophosphohydrolase/PP_5146, threonine deaminase/PP_5149) are unrelated to histidine biosynthesis. The same split architecture is found in *P. aeruginosa* (*hisB* = PA5143 separate from HolPase PA0335).

This distributed genomic organization is consistent with the exceptional evolutionary origin of the HolPase step: HolPase "*is generally the last enzyme to be characterized in many bacteria because its origin and evolution are more complex compared to other enzymes in histidine biosynthesis*" ([PMID: 31862725](https://pubmed.ncbi.nlm.nih.gov/31862725/)), and the HAD-type is the Gammaproteobacterial solution ([PMID: 28720084](https://pubmed.ncbi.nlm.nih.gov/28720084/)).

### F004 — PP_5147/PA0335 is the physiologically dominant HolPase, buffered by promiscuous HAD phosphatases with side activity

The HolPase step is functionally redundant. In *P. aeruginosa*, deletion of the PP_5147 ortholog PA0335 causes only **incomplete** histidine auxotrophy — residual growth persists. Guo and colleagues identified **PA3255** and **PA1143** as alternative homologs encoding phosphatases with weak "side" HolPase activity, with PA3255 being mainly responsible for the residual growth when PA0335 is absent: "*PA3255 and PA1143 code phosphatase with side HolPase activity. PA0335 play a key role in histidine biosynthesis, PA3255 respond mainly for the residual growth when PA0335 HolPase is absence*" ([PMID: 40596842](https://pubmed.ncbi.nlm.nih.gov/40596842/)).

This redundancy is a hallmark of substrate-ambiguous HAD-superfamily phosphatases. As shown for the *E. coli* proteome, "*Gph and HisB are members of the HAD superfamily of hydrolases*" that are evolutionarily interconvertible and can acquire overlapping phosphatase activities ([PMID: 23728795](https://pubmed.ncbi.nlm.nih.gov/23728795/)). *P. putida* is expected to possess an analogous set of backup phosphatases, meaning PP_5147 is best described as the **principal, but not absolutely essential,** HolPase.

### F005 — PP_5147 is a soluble cytoplasmic enzyme

Subcellular localization analysis places the enzyme firmly in the cytoplasm. A Kyte–Doolittle hydrophobicity scan of Q88CN3 (218 aa) found a maximum 19-residue window mean of only **0.98** (at residue 52), well below the ~1.6 threshold for a transmembrane helix, and the N-terminal 30 residues averaged **−0.13** with no hydrophobic core — ruling out both a transmembrane segment and a Sec/Tat signal peptide. UniProt lists only Hydrolase/Magnesium/Metal-binding keywords, with **no membrane or secretion annotations**. This is entirely consistent with the biology of the pathway: de novo histidine biosynthesis, and HAD-superfamily amino-acid-biosynthesis phosphatases generally, operate in the **cytosol**.

### F006 — AlphaFold structure reveals a complete, canonical HAD active site with a C1 cap domain

The predicted structure strongly corroborates the enzymatic assignment. The AlphaFold model **AF-Q88CN3-F1** (v6) is high-confidence (**mean pLDDT 96.2** across all 218 residues). Spatial analysis around the Asp7 nucleophile carboxylate reveals the four conserved HAD catalytic motifs converging in a single active-site pocket:

| Motif | Residue(s) | Distance to Asp7 | Role |
|---|---|---|---|
| I | Asp7 + Asp9 + Thr11 (DxDxT) | — | Asp7 nucleophile; Asp9 general acid/base |
| II | Thr111 | 4.5 Å | Phosphate binding |
| III | Lys156 | 2.7 Å | Transition-state charge neutralization |
| IV | Asp179 / Asp183 (with Ser178/Ser180/Asn182) | 4.8–5.5 Å | Mg²⁺ coordination |

The ~90-residue insertion between motif I (~res 11) and motif II (~res 111) forms an α-helical **C1 "cap" domain** characteristic of **HAD subfamily IB (SerB-like)**, which encloses the substrate and dictates specificity for small phosphomonoesters. This architecture places the enzyme squarely within the "*member of the histidinol-phosphate phosphatase (HisB) subfamily of the haloalkanoic acid dehalogenase (HAD) enzyme superfamily*" ([PMID: 20050615](https://pubmed.ncbi.nlm.nih.gov/20050615/)) and supports a **Mg²⁺-dependent aspartyl-phosphotransfer mechanism**: Asp7 attacks the substrate phosphorus to form a phospho-aspartyl intermediate, which is then hydrolyzed, with Mg²⁺ and the conserved Lys/Thr residues stabilizing the transition state.

### F007 — The HAD-type HolPase lineage evolved from a promiscuous GmhB-like ancestor

HolPase is evolutionarily exceptional: it is the **only** histidine-biosynthesis enzyme with multiple independent origins — three unrelated folds (HAD, PHP, IMPase) perform this single reaction. As stated directly, "*The only exception is the histidinol phosphate phosphatase (HolPase)*" ([PMID: 36502290](https://pubmed.ncbi.nlm.nih.gov/36502290/)). Phylogenetic and ancestral-sequence-reconstruction analyses show that the Gammaproteobacterial HAD-type HolPase (**HisB-N**) arose from within the **βGmhB clade** — the same HAD subfamily as **D-glycero-D-manno-heptose-1,7-bisphosphate 7-phosphatase (GmhB)** — via a promiscuous ancestral phosphatase that already possessed weak HolPase activity: "*It has been argued that HisB-N and its closest homologue d-glycero-d-manno-heptose-1,7-bisphosphate 7-phosphatase (GmhB) have emerged from the same promiscuous ancestral phosphatase*" ([PMID: 36502290](https://pubmed.ncbi.nlm.nih.gov/36502290/)). GmhB itself "*supports two divergent biochemical pathways in bacteria*" ([PMID: 20050615](https://pubmed.ncbi.nlm.nih.gov/20050615/)) and binds histidinol-phosphate without efficiently hydrolyzing it — illustrating the shared active-site chemistry that underlies PP_5147's residual substrate ambiguity.

### F008 — PP_5147 is the primary HolPase; *P. putida* keeps a distinct serB (PP_4909) and a divergent HolPase paralog (PP_1721)

The "SerB family" name in the protein annotation is a **fold designation, not a functional one**. *P. putida* KT2440 possesses a genuine, dedicated phosphoserine phosphatase **serB = PP_4909** (KEGG KO K01079, EC 3.1.3.3), together with the complete serine pathway (*serA* = PP_2533/PP_5155, *serC* = PP_1768). PP_5147 is therefore **not** the serine-biosynthesis phosphatase.

The histidinol-phosphatase orthology KO K28842 maps to **two paralogs** in *P. putida*: PP_5147 and **PP_1721**. Global-alignment identities discriminate their roles clearly:

| Pair | Identity | Interpretation |
|---|---|---|
| PP_5147 vs PA0335 | 67.7% | Clear ortholog of validated primary HolPase |
| PP_1721 vs PA0335 | 46.0% | More divergent paralog |
| PP_5147 vs PP_1721 | 38.7% | Distinct paralogs |

Both retain HAD motif I (PP_5147 "FDLDNT"; PP_1721 "FDLDET"), but PP_5147's substantially higher identity to the validated PA0335 ortholog marks it as the **dedicated, primary HolPase** for histidine biosynthesis, with PP_1721 a more divergent paralog of secondary or specialized function.

### F009 — Consolidated conclusion

Six independent lines of evidence converge on the same assignment: (1) UniProt/KEGG/BioCyc annotation as histidinol-phosphatase EC 3.1.3.15 with reaction L-histidinol-P + H₂O → L-histidinol + Pᵢ (Rhea:14465); (2) KEGG orthology K28842 in the histidine module M00026; (3) InterPro IPR006385 (HAD subfamily IB / SerB1-like), which explicitly includes the *Pseudomonas* HolPase; (4) 67.7% identity to the genetically and biochemically validated ortholog PA0335; (5) a high-confidence AlphaFold model (pLDDT 96.2) with a complete four-motif HAD active site plus a C1 cap; and (6) no signal peptide or transmembrane segment, establishing cytoplasmic localization.

---

## Mechanistic Model / Interpretation

### The reaction and its place in the pathway

PP_5147 catalyzes step 8 of the de novo histidine biosynthesis pathway:

```
   ... → imidazole-glycerol-P → (hisB/IGPD, PP_0289) → imidazole-acetol-P
                                                            │ (hisC, aminotransferase)
                                                            ▼
                                                 L-histidinol-phosphate
                                                            │
                              ┌─────────────────────────────┘
                              │  PP_5147 (HolPase, EC 3.1.3.15)
                              │  L-histidinol-P + H2O --Mg2+--> L-histidinol + Pi
                              ▼
                        L-histidinol
                              │ (hisD, histidinol dehydrogenase; 2x NAD+)
                              ▼
                        L-histidine
```

The substrate, L-histidinol-phosphate, is a small phosphomonoester; the product histidinol is then oxidized in two NAD⁺-dependent steps by histidinol dehydrogenase (HisD) to yield L-histidine. This is a **linear anabolic (biosynthetic) pathway** operating entirely in the cytoplasm.

### Catalytic mechanism

As a HAD subfamily IB enzyme, PP_5147 uses the canonical **aspartyl-phosphotransferase mechanism**:

```
Step 1:  Asp7-COO⁻  +  R-O-PO3²⁻  →  Asp7-CO-O-PO3²⁻  +  R-OH
         (nucleophilic attack; phospho-aspartyl intermediate)

Step 2:  Asp7-CO-O-PO3²⁻  +  H2O  →  Asp7-COO⁻  +  Pi
         (hydrolysis of intermediate; Asp9 as general acid/base)

Cofactor: Mg2+, coordinated by motif-IV carboxylates Asp179/Asp183,
          stabilizes the pentacovalent transition state; Lys156
          (motif III) neutralizes developing negative charge.
```

The **C1 cap domain** (the ~90-residue helical insertion) folds over the active site to sequester the substrate from bulk solvent and impose specificity for L-histidinol-phosphate over other small phosphometabolites.

### Redundancy and evolution

The system exhibits **functional degeneracy**: PP_5147 is the dominant catalyst, but promiscuous HAD phosphatases (the *P. aeruginosa* analogs being PA3255/PA1143) provide backup activity, so its loss yields only incomplete auxotrophy. This is a direct consequence of the lineage's origin — the enzyme descends from a **promiscuous GmhB-like ancestor** that could weakly hydrolyze histidinol-phosphate, and specialization was overlaid on a broad-specificity scaffold. The retained "leakiness" of the HAD active site is precisely what allows other family members to serve as partial backups.

### Localization

All evidence points to a **soluble cytoplasmic** localization: no signal peptide, no transmembrane helix, and consistency with the cytosolic setting of the entire histidine biosynthesis pathway. The enzyme carries out its function free in the cytoplasm, drawing on the cellular Mg²⁺ pool.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [28720084](https://pubmed.ncbi.nlm.nih.gov/28720084/) | *Sequence-based identification of IMPase-like HisN...* | Establishes the three unrelated HolPase families and that Gammaproteobacteria (incl. *Pseudomonas*) use the HAD-type — the family of PP_5147. |
| [31862725](https://pubmed.ncbi.nlm.nih.gov/31862725/) | *PA0335... Mediates Histidine Auxotrophy* | Primary identification of PA0335 (67.7% ortholog of PP_5147) as HolPase catalyzing the penultimate step; deletion causes auxotrophy. |
| [40596842](https://pubmed.ncbi.nlm.nih.gov/40596842/) | *Alternative homologs of HolPase in P. aeruginosa* | Confirms PA0335 is a HAD-family HolPase and the key enzyme; PA3255/PA1143 provide side activity explaining incomplete auxotrophy. |
| [23728795](https://pubmed.ncbi.nlm.nih.gov/23728795/) | *Substrate ambiguous enzymes in E. coli proteome* | Documents HAD-superfamily phosphatases (Gph, HisB) as substrate-ambiguous and interconvertible — basis for backup activity. |
| [20050615](https://pubmed.ncbi.nlm.nih.gov/20050615/) | *Divergence in the HAD superfamily: GmhB* | Places HolPase in a defined HAD subfamily with a conserved four-motif Asp-nucleophile active site; documents the GmhB relative. |
| [36502290](https://pubmed.ncbi.nlm.nih.gov/36502290/) | *Ancestry of an evolutionary young enzyme from histidine biosynthesis* | Documents shared promiscuous-ancestor origin of HisB-N (HAD HolPase) and GmhB; establishes HolPase as evolutionarily exceptional. |
| [26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/) | *Revisited genome of P. putida KT2440* | Genome reference underpinning gene/locus assignments used for the *P. putida* pathway architecture. |

Supporting background literature reviewed on the PHP-type and IMPase-type HolPase families (e.g., [PMID: 23327428](https://pubmed.ncbi.nlm.nih.gov/23327428/) on PHP-family HPP, which "*catalyzes the hydrolysis of L-histidinol phosphate to L-histidinol and inorganic phosphate, the penultimate step in the biosynthesis of L-histidine*"; [PMID: 20023146](https://pubmed.ncbi.nlm.nih.gov/20023146/) on plant IMPase-like HISN7) confirms that these are the *alternative*, non-HAD solutions — reinforcing that PP_5147 is specifically the HAD-type enzyme.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on PP_5147 itself.** All experimental phenotype and mechanistic data derive from the *P. aeruginosa* ortholog PA0335 (and from other model HAD HolPases), not from the *P. putida* protein directly. The functional assignment for PP_5147 is a confident inference from 67.7% orthology, structure prediction, and database annotation — not a measured kinetic parameter.

2. **Kinetic parameters unknown.** There are no measured k_cat, K_m, substrate-specificity profile, or metal-preference data for PP_5147. Whether it displays the same residual promiscuity as its GmhB-derived ancestors is inferred, not demonstrated.

3. **Backup phosphatases not mapped in *P. putida*.** The specific *P. putida* homologs corresponding to *P. aeruginosa* PA3255/PA1143 (the promiscuous backups) have not been individually identified in this investigation; the divergent paralog PP_1721 is a candidate but its function is unverified.

4. **Structure is predicted, not experimental.** The active-site geometry rests on an AlphaFold model (albeit high-confidence, pLDDT 96.2). No crystal structure of PP_5147 with bound substrate/product/metal exists to confirm the catalytic distances.

5. **Regulation not addressed.** How PP_5147 expression is controlled (e.g., feedback by histidine, links to nitrogen/carbon status) was not investigated.

---

## Proposed Follow-up Experiments / Actions

1. **Gene deletion + complementation.** Construct a clean ΔPP_5147 mutant in *P. putida* KT2440 and test for histidine auxotrophy on minimal medium ± histidine. Predict **incomplete** auxotrophy (residual growth), mirroring the PA0335 phenotype, and confirm rescue by plasmid-borne PP_5147.

2. **Recombinant enzymology.** Express and purify PP_5147, then measure phosphatase activity on L-histidinol-phosphate (determine k_cat, K_m), Mg²⁺-dependence, and pH optimum. Test candidate off-target substrates (e.g., sugar bisphosphates, phosphoserine) to quantify residual promiscuity predicted by the GmhB ancestry.

3. **Identify the *P. putida* backups.** Delete PP_1721 alone and in combination with PP_5147; assay whether the double mutant becomes an **absolute** histidine auxotroph. Screen other HAD phosphatases for side HolPase activity.

4. **Active-site mutagenesis.** Mutate the predicted catalytic residues (Asp7→Ala nucleophile; Asp9, Lys156, Asp179/Asp183) and confirm loss of activity, validating the AlphaFold-derived mechanistic model.

5. **Structural determination.** Solve a crystal or cryo-EM structure of PP_5147, ideally with a substrate analog (e.g., histidinol + vanadate/tungstate as transition-state mimic) and Mg²⁺ bound, to confirm the C1 cap architecture and catalytic geometry.

---

## Conclusion

**PP_5147 (Q88CN3)** is the principal **cytoplasmic HAD-superfamily histidinol-phosphate phosphatase** (subfamily IB / "SerB1-like"; EC 3.1.3.15) of *Pseudomonas putida* KT2440. It catalyzes the Mg²⁺-dependent hydrolysis of L-histidinol-phosphate to L-histidinol plus inorganic phosphate — the penultimate step of de novo L-histidine biosynthesis — in the cytoplasm. The assignment is supported by consistent database orthology, a complete four-motif HAD catalytic site in a high-confidence structural model, and 67.7% identity to the experimentally validated ortholog PA0335 whose deletion causes histidine auxotrophy. The "SerB family" name reflects fold homology only; *P. putida* maintains a separate phosphoserine phosphatase (PP_4909), and PP_5147 is a dedicated histidine-biosynthesis enzyme backed up by promiscuous HAD paralogs.


## Artifacts

- [OpenScientist final report](PP_5147-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_5147-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28720084
2. PMID:31862725
3. PMID:40596842
4. PMID:23728795
5. PMID:20050615
6. PMID:36502290
7. PMID:23327428
8. PMID:20023146