---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T17:23:54.437429'
end_time: '2026-07-11T17:56:33.730628'
duration_seconds: 1959.29
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: acoC
  gene_symbol: acoC
  uniprot_accession: Q88QE1
  protein_description: 'SubName: Full=Dihydrolipoyllysine-residue acetyltransferase
    component of acetoin cleaving system {ECO:0000313|EMBL:AAN66180.1}; EC=2.3.1.12
    {ECO:0000313|EMBL:AAN66180.1};'
  gene_info: Name=acoC {ECO:0000313|EMBL:AAN66180.1}; OrderedLocusNames=PP_0553 {ECO:0000313|EMBL:AAN66180.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: 2-oxoA_DH_lipoyl-BS. (IPR003016); AB_hydrolase_1. (IPR000073);
    AB_hydrolase_fold. (IPR029058); Biotin_lipoyl. (IPR000089); Carboxylesterase_BioH.
    (IPR050228)
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: acoC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: acoC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QE1
- **Protein Description:** SubName: Full=Dihydrolipoyllysine-residue acetyltransferase component of acetoin cleaving system {ECO:0000313|EMBL:AAN66180.1}; EC=2.3.1.12 {ECO:0000313|EMBL:AAN66180.1};
- **Gene Information:** Name=acoC {ECO:0000313|EMBL:AAN66180.1}; OrderedLocusNames=PP_0553 {ECO:0000313|EMBL:AAN66180.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** 2-oxoA_DH_lipoyl-BS. (IPR003016); AB_hydrolase_1. (IPR000073); AB_hydrolase_fold. (IPR029058); Biotin_lipoyl. (IPR000089); Carboxylesterase_BioH. (IPR050228)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "acoC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'acoC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **acoC** (gene ID: acoC, UniProt: Q88QE1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: acoC (Q88QE1, PP_0553) in *Pseudomonas putida* KT2440

## Summary

**acoC** (UniProt **Q88QE1**; ordered locus **PP_0553**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes the **E2 component — dihydrolipoyllysine-residue (dihydrolipoamide) acetyltransferase, EC 2.3.1.12 — of the acetoin dehydrogenase enzyme system (AoDH ES), also called the "acetoin-cleaving system."** The protein is a compact (~39.6 kDa, 368-residue) two-domain enzyme built from an N-terminal lipoyl (biotinyl/lipoyl-attachment) domain and a C-terminal catalytic domain. Its primary biochemical role is to receive the acetyl group generated when the thiamine-diphosphate-dependent E1 component cleaves the central C–C bond of acetoin (3-hydroxy-2-butanone), carry that acetyl group on a covalently attached lipoyl "swinging arm," and transfer it to Coenzyme A, producing **acetyl-CoA**. The net reaction of the complex is: **acetoin + CoA + NAD⁺ → acetaldehyde + acetyl-CoA + NADH**, with AcoC serving as the central acyl-transfer hub.

The gene sits within a **2,3-butanediol/acetoin catabolic operon (PP_0552–PP_0557)** and, together with 2,3-butanediol dehydrogenase and the E1α/E1β subunits, constitutes the enzymatic machinery that converts 2,3-butanediol and acetoin into central-metabolism intermediates. Expression of this system is **acetoin-induced and glucose-repressed**, and is controlled by the **σ54-dependent transcriptional activator AcoR (PP_0557)**, which is divergently transcribed from the operon. The gene product functions in the **cytoplasm** — it carries no signal peptide or transmembrane segment, and its homologs assemble into soluble multienzyme complexes.

A distinctive and mechanistically important feature emerged from this investigation: unlike canonical 2-oxo-acid-dehydrogenase E2 cores, which use a chloramphenicol-acetyltransferase (CAT)-like acyltransferase fold, the *P. putida* AcoC catalytic domain is predicted to adopt an **α/β-hydrolase / serine-hydrolase fold**. Both InterPro/Pfam annotation and a high-confidence AlphaFold model (mean pLDDT 90.8) support this architecture, and geometric analysis of the model reveals a classical **Ser206–His347–Asp324 catalytic triad** with an oxyanion hole, consistent with a serine-hydrolase-style acetyl-transfer mechanism. This α/β-hydrolase-type E2 architecture is conserved across a Proteobacterial clade of acetoin-cleaving-system E2 enzymes, distinguishing it from the Firmicute (e.g., *Bacillus subtilis*) CAT-fold enzymes.

**Identity verification:** The gene symbol *acoC*, the EC number 2.3.1.12, the organism (*P. putida* KT2440), and the domain architecture (lipoyl domain + hydrolase fold) are all mutually consistent across UniProt, InterPro, KEGG, AlphaFold, and the primary literature on the closely related *P. putida* PpG2 acetoin-cleaving system. There is no evidence of gene-symbol ambiguity for this target.

---

## Gene / Protein Identity

| Attribute | Value |
|---|---|
| Gene symbol | *acoC* |
| UniProt | Q88QE1 |
| Ordered locus | PP_0553 |
| Organism | *Pseudomonas putida* KT2440 (PSEPK) |
| Length / mass | 368 aa / ~39.6 kDa |
| EC number | 2.3.1.12 |
| GO molecular function | GO:0004742 dihydrolipoyllysine-residue acetyltransferase activity |
| KEGG | ppu:PP_0553 |

The gene symbol *acoC* matches the UniProt description "Dihydrolipoyllysine-residue acetyltransferase component of acetoin cleaving system." The genomic neighborhood (KEGG) places PP_0553 inside the canonical *aco* gene cluster, and the protein's size (368 aa ≈ 39.6 kDa) matches the deduced E2 (M_r 39,613) of the closely related *P. putida* PpG2 acetoin-cleaving system ([PMID: 7813883](https://pubmed.ncbi.nlm.nih.gov/7813883/)). There is **no evidence of gene-symbol ambiguity**: all lines of evidence converge on the same E2 acetyltransferase identity.

---

## Key Findings

### F001 — acoC encodes the E2 dihydrolipoyllysine-residue acetyltransferase (EC 2.3.1.12) of the acetoin-cleaving system

UniProt Q88QE1 describes the protein as the "Dihydrolipoyllysine-residue acetyltransferase component of acetoin cleaving system," EC 2.3.1.12, gene *acoC* / PP_0553, 368 amino acids (~39.6 kDa), with GO term GO:0004742 (dihydrolipoyllysine-residue acetyltransferase activity). This identity is anchored in primary literature on the closely related *P. putida* PpG2 system. Huang and colleagues sequenced the *aco* genes and deduced masses for the three components of the acetoin-cleaving system, reporting an **E2 of M(r) 39,613** — a value that matches the 368-residue KT2440 protein almost exactly:

> "The amino acid sequences deduced from acoA, acoB, and acoC for E1 alpha (M(r) 34639), E1 beta (M(r) 37268), and E2 (M(r) 39613) of the P. putida acetoin cleaving system exhibited striking similarities to those of the corresponding components of the A. eutrophus acetoin cleaving system" — [PMID: 7813883](https://pubmed.ncbi.nlm.nih.gov/7813883/)

The same E2 = dihydrolipoamide acetyltransferase assignment was established biochemically in homologous systems. In *Clostridium magnum*, E2 was directly purified from acetoin-grown cells:

> "E2 (dihydrolipoamide acetyltransferase) and E3 (dihydrolipoamide dehydrogenase) of the Clostridium magnum acetoin dehydrogenase enzyme system were copurified in a three-step procedure from acetoin-grown cells" — [PMID: 8206840](https://pubmed.ncbi.nlm.nih.gov/8206840/)

And in *Pelobacter carbinolicus*, the *aco* gene cluster was shown to encode the same three-component enzymology:

> "the structural genes for the alpha and beta subunits of E1 (acetoin:2,6-dichlorophenolindophenol oxidoreductase), E2 (dihydrolipoamide acetyltransferase), and E3 (dihydrolipoamide dehydrogenase)" — [PMID: 8110297](https://pubmed.ncbi.nlm.nih.gov/8110297/)

Together these lines of evidence firmly establish AcoC as the E2 acetyltransferase of the acetoin dehydrogenase system.

### F002 — acoC lies within a 2,3-butanediol/acetoin catabolic operon (PP_0552–PP_0557)

The genomic neighborhood of PP_0553 in the KEGG *ppu* genome forms a coherent catabolic module, all encoded on the complement strand and co-transcribed:

| Locus | Gene/product | Role |
|-------|--------------|------|
| PP_0552 | 2,3-butanediol dehydrogenase | Oxidizes 2,3-butanediol → acetoin |
| **PP_0553** | **AcoC (E2, this protein)** | **Dihydrolipoamide acetyltransferase** |
| PP_0554 | AcoB (E1β) | Acetoin:2,6-DCPIP oxidoreductase β-subunit |
| PP_0555 | AcoA (E1α) | Acetoin:2,6-DCPIP oxidoreductase α-subunit |
| PP_0556 | AcoX | Acetoin catabolism accessory protein |
| PP_0557 | AcoR | σ54-dependent regulatory activator (divergent, + strand) |

In *P. putida* PpG2, the *aco* genes plus the butanediol dehydrogenase form a single inducible operon that carries out the complete conversion:

> "The aco genes and adh constitute presumably one single operon which encodes all enzymes required for the conversion of 2,3-butanediol to central metabolites." — [PMID: 7813883](https://pubmed.ncbi.nlm.nih.gov/7813883/)

> "The 2,3-butanediol dehydrogenase and the acetoin-cleaving system were simultaneously induced in Pseudomonas putida PpG2 during growth on 2,3-butanediol and on acetoin." — [PMID: 7813883](https://pubmed.ncbi.nlm.nih.gov/7813883/)

This defines the biological process in which AcoC operates: the funneling of the fermentation/spoilage products 2,3-butanediol and acetoin into acetyl-CoA and central carbon metabolism.

### F003 & F004 — Atypical two-domain architecture: lipoyl domain fused to an α/β-hydrolase fold

InterPro/Pfam annotation of Q88QE1 (368 aa) reveals two distinct modules:

- **N-terminal lipoyl domain** (residues ~4–79): IPR000089 (Biotin_lipoyl), PROSITE PS00189 (LIPOYL), Pfam PF00364. The conserved lipoyl-lysine sits in the canonical **E-T-D-K motif at Lys45** (…VETDK…), which is the covalent attachment site for the lipoic acid cofactor.
- **C-terminal catalytic domain** (residues ~120–368): annotated as an **α/β-hydrolase fold** — IPR000073 (AB_hydrolase_1), IPR029058 (AB_hydrolase_fold), Pfam PF00561 (Abhydrolase_1), SUPFAM alpha/beta-Hydrolases, Gene3D 3.40.50.1820. The sequence contains a serine-hydrolase **nucleophile-elbow GxSxG motif at Ser206** ("GHSMG"), an oxyanion-hole region near His139 ("HGFGG"), and a candidate catalytic histidine near the C-terminus.

This architecture contrasts sharply with the classical ~47–48 kDa E2 cores of *C. magnum* and *P. carbinolicus* ([PMID: 8206840](https://pubmed.ncbi.nlm.nih.gov/8206840/), [PMID: 8110297](https://pubmed.ncbi.nlm.nih.gov/8110297/)), which carry the large chloramphenicol-acetyltransferase (CAT)-like acyltransferase domain typical of 2-oxo-acid-dehydrogenase E2 proteins.

The AlphaFold model **AF-Q88QE1-F1 (v6)** independently confirms this two-domain, swinging-arm design with high confidence (overall mean pLDDT 90.8):

| Region | Residues | Mean pLDDT | Interpretation |
|--------|----------|-----------|----------------|
| Lipoyl domain | 4–79 | 89.4 | Well-folded biotinyl/lipoyl domain |
| Inter-domain linker | 80–119 | 69.4 | Markedly lower → flexible swinging arm |
| α/β-hydrolase catalytic domain | 120–368 | 95.0 | High-confidence hydrolase fold |

The low-confidence linker (pLDDT 69.4) between two high-confidence domains is the structural signature of a **flexible tether** — exactly what is required for a lipoyl "swinging arm" to shuttle the acetyl group between the E1, E2, and E3 active sites. The predicted catalytic residues are modeled at very high confidence: Ser206 (pLDDT 98.75), the oxyanion-region His139 (98.75), and a C-terminal catalytic His (96.69). No signal peptide or transmembrane segment is present.

### F005 — AcoC is the cytoplasmic acyl-transfer hub: acetoin → acetaldehyde + acetyl-CoA

The acetoin dehydrogenase enzyme system is the principal catabolic route for acetoin cleavage in bacteria and comprises three catalytic components — E1 (TPP-dependent acetoin dehydrogenase / acetoin:2,6-dichlorophenolindophenol oxidoreductase, α+β = AcoA/AcoB), E2 (dihydrolipoamide acetyltransferase = **AcoC**), and E3 (dihydrolipoamide dehydrogenase). The authoritative review by Xiao & Xu frames this system as the catabolic acetoin-cleavage pathway:

> "we discuss the relationship between the two conflicting acetoin cleavage pathways, the enzymes of the acetoin dehydrogenase enzyme system, major genes involved in acetoin degradation" — [PMID: 17558661](https://pubmed.ncbi.nlm.nih.gov/17558661/)

Mechanistically, E1 binds acetoin, cleaves the central C–C bond releasing acetaldehyde, and transfers the resulting acetyl unit to the lipoyl-Lys45 of AcoC (forming S-acetyl-dihydrolipoyl-E2). AcoC then transfers this acetyl group to Coenzyme A to give acetyl-CoA (EC 2.3.1.12), and E3 re-oxidizes the dihydrolipoyl group using NAD⁺. The enzymology is confirmed by the *P. carbinolicus* study:

> "the alpha and beta subunits of E1 (acetoin:2,6-dichlorophenolindophenol oxidoreductase), E2 (dihydrolipoamide acetyltransferase), and E3 (dihydrolipoamide dehydrogenase)" — [PMID: 8110297](https://pubmed.ncbi.nlm.nih.gov/8110297/)

Because Q88QE1 has no signal peptide or transmembrane segment and its homologs form soluble multienzyme complexes, AcoC carries out its function in the **cytoplasm**.

### F006 — The aco operon is acetoin-induced, glucose-repressed, and activated by σ54-dependent AcoR

The regulatory logic of the acetoin catabolic operon is best documented in *Bacillus subtilis*, where the paradigm directly informs the *P. putida* AcoR/*aco* system:

> "The acoABCL operon encodes the E1alpha, E1beta, E2, and E3 subunits of the acetoin dehydrogenase complex in B. subtilis. Expression of this operon is induced by acetoin and repressed by glucose in the growth medium. The acoR gene is located downstream from the acoABCL operon and encodes a positive regulator which stimulates the transcription of the operon. The product of acoR has similarities to transcriptional activators of sigma 54-dependent promoters." — [PMID: 11274109](https://pubmed.ncbi.nlm.nih.gov/11274109/)

In *P. putida* KT2440 the cognate activator is **AcoR (PP_0557)**, located adjacent to and divergently transcribed from the *acoC*-containing operon. In *P. putida* PpG2 the *aco* genes plus butanediol dehydrogenase are co-induced during growth on 2,3-butanediol and acetoin ([PMID: 7813883](https://pubmed.ncbi.nlm.nih.gov/7813883/)). Carbon catabolite repression is CcpA-mediated in *B. subtilis* and glucose-dependent generally. Notably, the immediate *P. putida* cluster (PP_0552–PP_0556) **lacks a dedicated acoL (E3) gene**, implying that the dihydrolipoamide dehydrogenase (E3) is recruited from a shared/housekeeping pool — a common arrangement, since E3 is a promiscuous component shared among the pyruvate dehydrogenase, 2-oxoglutarate dehydrogenase, branched-chain, and acetoin dehydrogenase complexes.

### F007 — AcoC belongs to a conserved Proteobacterial clade of α/β-hydrolase-fold E2 enzymes

A comparative UniProt survey shows that the α/β-hydrolase (PF00561) catalytic architecture is not an artifact of the KT2440 annotation but a genuine, clade-conserved feature:

| Organism | Accession | Length | Catalytic fold |
|----------|-----------|--------|----------------|
| *P. putida* KT2440 | Q88QE1 | 368 aa | α/β-hydrolase (PF00561) |
| *Cupriavidus necator* / *Alcaligenes eutrophus* H16 | P27747 (reviewed) | 374 aa | α/β-hydrolase |
| *P. putida* PpG2-type | Q59695 (reviewed) | 370 aa | α/β-hydrolase |
| *Pseudomonas inefficax* | A0AAQ1P4J1 | 368 aa | α/β-hydrolase |
| *Brucella* spp. | Q7CNS6, A9MD09 | — | α/β-hydrolase |
| *Bacillus subtilis* 168 | O31550 (reviewed) | 398 aa | **CAT fold (PF00198) + E3-binding PF02817** |

Of 50 surveyed acetoin-cleaving-system E2 entries, **28 carried the α/β-hydrolase domain (PF00561) and only 1 carried the CAT fold (PF00198)**. The α/β-hydrolase-type E2s are more compact and lack the peripheral-subunit-binding domain (PF02817). This split mirrors the historical nomenclature: the **"acetoin-cleaving system"** (Alcaligenes/Pseudomonas — α/β-hydrolase E2) versus the **"acetoin dehydrogenase enzyme system"** (Clostridium/Pelobacter/Bacillus — CAT-fold ~47–48 kDa E2 [[PMID: 8206840](https://pubmed.ncbi.nlm.nih.gov/8206840/), [PMID: 8110297](https://pubmed.ncbi.nlm.nih.gov/8110297/)]). Critically, KT2440 AcoC (Q88QE1) is essentially identical in architecture and length to the reviewed *P. putida* AcoC (Q59695) and the biochemically referenced *A. eutrophus*/*C. necator* AcoC (P27747), placing *P. putida* AcoC in a distinct structural lineage from the Firmicute CAT-fold enzymes.

### F008 — A canonical Ser206–His347–Asp324 catalytic triad supports a serine-hydrolase acyl-transfer mechanism

Geometric analysis of the AlphaFold model reveals a textbook α/β-hydrolase catalytic triad:

- The GxSxG nucleophile-elbow **Ser206** hydroxyl (OG) hydrogen-bonds the **His347** imidazole (NE2) at **2.89 Å**.
- His347 (ND1) hydrogen-bonds the **Asp324** carboxylate (OD2 at **2.77 Å**; OD1 at 3.11 Å).
- An **oxyanion hole** is provided by backbone amides following the HGFGG motif (Gly140/Phe141 N within H-bonding distance of Ser206 OG).

All triad residues are modeled at very high confidence (pLDDT > 96). This Ser–His–Asp triad geometry is the defining feature of serine hydrolases and supports a covalent acyl-enzyme mechanism in which Ser206 is transiently acetylated, rather than the direct-transfer mechanism of the CAT-fold E2 enzymes. (This corrects an earlier note in the investigation: the catalytic histidine is His347, not His337.)

---

## Mechanistic Model / Interpretation

### The reaction sequence

```
   2,3-butanediol
        │  (PP_0552, 2,3-butanediol dehydrogenase; NAD+)
        ▼
     acetoin (3-hydroxy-2-butanone)
        │
        │  ┌─────────────────────── AcoC swinging arm ───────────────────────┐
        │  │                                                                  │
   ┌────▼──┴───┐   Lys45-lipoyl-S~acetyl        ┌──────────────┐   acetyl-CoA │
   │   E1      │ ─────────────────────────────► │   E2 = AcoC  │ ───────────► │
   │ AcoA/AcoB │  cleaves C–C bond of acetoin   │  Ser206 triad│    (to TCA / │
   │ (TPP)     │  → releases acetaldehyde       │  → CoA       │  biosynthesis)│
   └───────────┘                                └──────┬───────┘              │
                                                       │ dihydrolipoyl-E2     │
                                                ┌──────▼───────┐              │
                                                │  E3 (shared) │  NAD+ → NADH │
                                                │  re-oxidizes │              │
                                                └──────────────┘              │
                                                                              │
   Net: acetoin + CoA + NAD+ → acetaldehyde + acetyl-CoA + NADH  ─────────────┘
```

AcoC is the **integrating hub** of this cycle. Its N-terminal lipoyl domain, carrying a lipoic acid cofactor on Lys45, acts as a physical **swinging arm** (enabled by the flexible ~40-residue linker at residues 80–119) that visits three chemically distinct active sites in sequence:

1. **At E1:** The dihydrolipoyl-Lys45 is reductively acetylated, accepting the acetyl group liberated when E1 cleaves acetoin's C2–C3 bond (releasing acetaldehyde).
2. **At the E2 (AcoC) active site:** The S-acetyl group is transferred to Coenzyme A. In the *P. putida* enzyme this occurs at an α/β-hydrolase active site, most plausibly via a covalent acetyl-Ser206 intermediate that is subsequently attacked by the CoA thiol.
3. **At E3:** The resulting dihydrolipoyl arm is re-oxidized to the disulfide form using NAD⁺, regenerating the cofactor for another turn.

### Why the α/β-hydrolase fold matters

This is the most novel aspect of the annotation. Canonical E2 enzymes (pyruvate, 2-oxoglutarate, branched-chain, and Firmicute-type acetoin dehydrogenases) use a chloramphenicol-acetyltransferase (CAT)-like fold that catalyzes direct thioester-to-thioester acyl transfer without a covalent acyl-enzyme. The *P. putida* AcoC instead has a **serine-hydrolase active site** with a Ser206–His347–Asp324 triad. This implies a ping-pong mechanism proceeding through a covalent acetyl-Ser206 enzyme intermediate — mechanistically closer to esterases/lipases and to carboxylesterase BioH (note the IPR050228 Carboxylesterase_BioH annotation in the target's domain list) than to classical acyltransferases. The conservation of this fold across a Proteobacterial clade (F007) argues that it is a functional adaptation, not a mis-annotation. Whether it confers altered substrate specificity, catalytic efficiency, or regulatory properties relative to CAT-fold E2s is an open and interesting question.

### Localization and pathway context

AcoC is a **cytoplasmic** enzyme (no signal peptide, no transmembrane helix; soluble multienzyme complex). It sits at a catabolic entry point that allows *P. putida* to use 2,3-butanediol and acetoin — common products of bacterial fermentation and plant/environmental niches — as carbon and energy sources by converting them, via acetaldehyde and acetyl-CoA, into central metabolism. Expression is tightly gated: **on** in the presence of acetoin (via the σ54-dependent activator AcoR), and **off** in the presence of glucose (carbon catabolite repression), ensuring the pathway runs only when its substrate is available and preferred carbon sources are exhausted.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|------|-----------------|--------------|
| [7813883](https://pubmed.ncbi.nlm.nih.gov/7813883/) | *Molecular characterization of the P. putida 2,3-butanediol catabolic pathway* | **Primary anchor.** Sequences *acoA/B/C*; deduces E2 M(r) 39,613 (matches Q88QE1); establishes single operon converting 2,3-butanediol → central metabolites; shows co-induction by substrates. |
| [8206840](https://pubmed.ncbi.nlm.nih.gov/8206840/) | *Biochemical characterization of the C. magnum acetoin dehydrogenase system* | Biochemically purifies E2 as dihydrolipoamide acetyltransferase from acetoin-grown cells (homolog). |
| [8110297](https://pubmed.ncbi.nlm.nih.gov/8110297/) | *Characterization of the P. carbinolicus acetoin dehydrogenase system* | Defines the three-component (E1αβ/E2/E3) enzymology; confirms E2 = dihydrolipoamide acetyltransferase. |
| [17558661](https://pubmed.ncbi.nlm.nih.gov/17558661/) | *Acetoin metabolism in bacteria* (review) | Authoritative review establishing AoDH ES as the catabolic acetoin-cleavage pathway; frames E2's role. |
| [11274109](https://pubmed.ncbi.nlm.nih.gov/11274109/) | *Regulation of the acetoin catabolic pathway by σL in B. subtilis* | Documents acetoin induction, glucose repression, and σ54-type AcoR activation — the regulatory paradigm for the P. putida operon. |
| [8557670](https://pubmed.ncbi.nlm.nih.gov/8557670/) | *Lipoyl domain-based feedback control of PDC* | Provides mechanistic background on lipoyl-domain reductive acetylation and swinging-arm function in E2 enzymes generally. |
| [28423947](https://pubmed.ncbi.nlm.nih.gov/28423947/) | *Metabolic engineering for acetoin/2,3-butanediol production* (review) | Biotechnological context; acetoin and 2,3-BD as neighboring metabolites and industrial targets. |

**Bioinformatic / structural evidence** (from database and model analysis rather than a single PMID): UniProt Q88QE1 annotation (EC 2.3.1.12, GO:0004742, lipoyl domain, α/β-hydrolase domain); InterPro/Pfam domain composition (PF00364 lipoyl + PF00561 Abhydrolase_1); KEGG *ppu* operon structure (PP_0552–PP_0557); AlphaFold model AF-Q88QE1-F1 v6 (mean pLDDT 90.8, flexible linker, high-confidence Ser206–His347–Asp324 triad); and a 50-entry UniProt comparative survey establishing clade-wide conservation of the α/β-hydrolase E2 architecture in Proteobacteria.

---

## Supported and Refuted Hypotheses

**Supported:**
- **H1** — AcoC is the E2 dihydrolipoamide acetyltransferase (EC 2.3.1.12) of the acetoin-cleaving system. *Strongly supported* (UniProt; operon context; size match to PpG2 E2; cross-species biochemistry).
- **H2** — AcoC produces acetyl-CoA from acetoin-derived acetyl + CoA within a cytoplasmic multienzyme complex. *Supported* (mechanistic homology; review literature; no signal/TM).
- **H3** — *acoC* is part of a 2,3-butanediol/acetoin catabolic operon regulated by AcoR/σ54, acetoin-induced and glucose-repressed. *Supported* (KEGG operon; PMID 11274109; PMID 7813883).
- **H4** — *P. putida* AcoC has an atypical lipoyl + α/β-hydrolase architecture with a Ser206–His347–Asp324 triad. *Supported by bioinformatics + AlphaFold + comparative genomics*; the precise catalytic mechanism remains to be verified experimentally.

**Refuted / not supported:**
- The gene is **not** ambiguous; there is no competing gene of different function with the same symbol in this organism.
- AcoC is **not** the large CAT-fold E2 seen in *Bacillus*/*Clostridium*/*Pelobacter* — it is a smaller, α/β-hydrolase-type variant.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on the KT2440 protein itself.** The functional assignment rests on (a) sequence identity to the well-characterized *P. putida* PpG2 and *A. eutrophus* systems, (b) biochemical purification of E2 homologs from other organisms, and (c) high-quality structural prediction. No enzyme kinetics, substrate-specificity assay, or crystal structure exists specifically for Q88QE1.

2. **The α/β-hydrolase mechanism is predicted, not experimentally proven.** The Ser206–His347–Asp324 triad is derived from an AlphaFold model, and the covalent acetyl-Ser intermediate is inferred by analogy to serine hydrolases. An EC 2.3.1.12 acyltransferase running through a hydrolase-fold active site is unusual and warrants direct verification.

3. **E3 source is inferred.** The immediate operon lacks *acoL* (E3). The assumption that E3 is supplied from a shared housekeeping dihydrolipoamide dehydrogenase pool is reasonable but not directly demonstrated for KT2440.

4. **Regulatory details are transferred from *B. subtilis*.** While AcoR (PP_0557) is present and divergently transcribed, the exact promoter architecture, σ54 dependence, and CcpA/Crc-mediated repression in *P. putida* KT2440 have not been experimentally mapped here.

5. **Substrate specificity beyond acetoin, and the oligomeric/stoichiometric state of the complex, are untested.**

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Overexpress His-tagged Q88QE1 in *E. coli*, reconstitute with lipoic acid (via LplA/LipB) and CoA, and measure dihydrolipoyllysine-residue acetyltransferase activity (EC 2.3.1.12) using S-acetyl-dihydrolipoamide + CoA → acetyl-CoA, monitored by DTNB/thioester assays.

2. **Test the serine-hydrolase mechanism directly.** Generate S206A, H347A, and D324N mutants and assay for loss of acetyltransferase activity; probe for a covalent acetyl-Ser206 intermediate by mass spectrometry or trapping with serine-hydrolase inhibitors (e.g., PMSF, fluorophosphonate activity-based probes).

3. **Solve an experimental structure.** X-ray crystallography or cryo-EM of AcoC (and, ideally, the assembled E1–E2–E3 complex) to confirm the α/β-hydrolase fold, the triad geometry, and the swinging-arm architecture.

4. **In vivo genetics in KT2440.** Construct a clean PP_0553 deletion and test growth on 2,3-butanediol and acetoin as sole carbon sources; complement to confirm phenotype specificity.

5. **Map the regulation.** Use RNA-seq / qRT-PCR under acetoin vs. glucose to confirm induction/repression, and ChIP or promoter-fusion assays to verify AcoR/σ54 control of the PP_0552–PP_0557 operon in KT2440.

6. **Confirm E3 sourcing.** Identify which dihydrolipoamide dehydrogenase (Lpd) partners with the acetoin dehydrogenase complex via pull-downs or genetic epistasis.

7. **Comparative enzymology.** Directly compare the α/β-hydrolase-fold AcoC (Proteobacterial) with a CAT-fold AcoC (e.g., *B. subtilis* O31550) for kinetic parameters and substrate range, to test whether the fold switch has functional consequences.

---

## Conclusion

The gene symbol *acoC* is **not** ambiguous for this target: all evidence converges on a single, coherent function. **acoC (Q88QE1, PP_0553)** encodes the **E2 dihydrolipoyllysine-residue acetyltransferase (EC 2.3.1.12)** of the cytoplasmic **acetoin dehydrogenase enzyme system** of *P. putida* KT2440. Using a lipoyl cofactor on Lys45 as a swinging arm, it accepts the acetyl group generated by E1's cleavage of acetoin and transfers it to Coenzyme A, producing acetyl-CoA — the acyl-transfer hub of the acetoin-induced, glucose-repressed, AcoR/σ54-regulated 2,3-butanediol/acetoin catabolic operon (PP_0552–PP_0557). Distinctively, its catalytic domain is predicted to be a compact α/β-hydrolase/serine-hydrolase fold (Ser206–His347–Asp324 triad) rather than the canonical CAT fold, a feature conserved across a Proteobacterial clade and worthy of direct experimental confirmation.


## Artifacts

- [OpenScientist final report](acoC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](acoC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:7813883
2. PMID:8206840
3. PMID:8110297
4. PMID:17558661
5. PMID:11274109