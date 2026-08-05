---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T16:04:49.689195'
end_time: '2026-07-18T16:26:10.191732'
duration_seconds: 1280.5
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_0423
  gene_symbol: PP_0423
  uniprot_accession: Q88QR5
  protein_description: 'RecName: Full=BPL/LPL catalytic domain-containing protein
    {ECO:0000259|PROSITE:PS51733};'
  gene_info: OrderedLocusNames=PP_0423 {ECO:0000313|EMBL:AAN66053.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: aa-tRNA-synth_II/BPL/LPL. (IPR045864); BPL_LPL_catalytic. (IPR004143);
    Octanoyltrans_LipM/LipL. (IPR050664); LplA-B_cat (PF21948)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_0423-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_0423-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QR5
- **Protein Description:** RecName: Full=BPL/LPL catalytic domain-containing protein {ECO:0000259|PROSITE:PS51733};
- **Gene Information:** OrderedLocusNames=PP_0423 {ECO:0000313|EMBL:AAN66053.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** aa-tRNA-synth_II/BPL/LPL. (IPR045864); BPL_LPL_catalytic. (IPR004143); Octanoyltrans_LipM/LipL. (IPR050664); LplA-B_cat (PF21948)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_0423" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_0423' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_0423** (gene ID: PP_0423, UniProt: Q88QR5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_0423 (Q88QR5): A Cytoplasmic LplA-type Lipoate/Octanoate-Protein Ligase in *Pseudomonas putida* KT2440

**Target:** PP_0423 / Q88QR5 — "BPL/LPL catalytic domain-containing protein"
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440) (PSEPK)
**Length:** 234 aa | **Gene position:** 512,008–512,712 (+ strand) | **Protein ID:** AAN66053

## Summary

**PP_0423** (UniProt **Q88QR5**; OrderedLocusName PP_0423) of *Pseudomonas putida* KT2440 encodes a **234-residue, soluble cytoplasmic enzyme of the biotin/lipoate protein-ligase (BPL/LPL) catalytic-domain superfamily**, specifically the **LplA/LipM/LipL clade** of lipoate- and octanoate-protein ligases/transferases. All available evidence converges on a single functional assignment: PP_0423 is most likely an **ATP-dependent lipoate-protein ligase A (LplA)-type enzyme** that catalyzes the **salvage (scavenging) attachment of exogenous lipoic acid — and, with broad fatty-acid specificity, its precursor octanoate — onto the conserved lysine of lipoyl domains** borne by 2-oxoacid dehydrogenase E2 subunits and the glycine-cleavage H-protein (GcvH). The predicted reaction proceeds in two steps: (1) ATP-dependent activation of lipoate to the lipoyl-AMP intermediate, and (2) transfer of the lipoyl moiety to the ε-amino group of the target lysine, forming an amide bond.

This assignment rests on four independent lines of bioinformatic evidence. First, **domain architecture**: PP_0423 carries the PROSITE PS51733 BPL/LPL catalytic domain and matching InterPro/Pfam/eggNOG signatures (IPR004143, IPR050664, PF21948, COG0095) that define the LplA family. Second, **homology**: by global Needleman–Wunsch alignment, its single closest characterized relative is *E. coli* LplA (33.3% identity), clearly above LipB octanoyltransferase (20.7%), identifying it as a ligase rather than a transferase. Third, a **functional-association network** (STRING) in which every top-ranked partner is a lipoyl-carrier substrate (the two GcvH paralogs are the strongest associations, followed by E2 subunits sucB/aceF/bkdB/acoC and the E3 lipoamide dehydrogenase lpd). Fourth, **localization and fold**: hydropathy analysis predicts a soluble cytoplasmic protein with no signal peptide or transmembrane helix, and AlphaFold predicts a compact, well-ordered α/β catalytic domain (mean pLDDT 95.7), arguing for an intact functional enzyme rather than a decayed pseudo-enzyme.

Importantly, **PP_0423 is the sole member of the LplA/LipM/LipL clade in the entire KT2440 proteome**, distinct from the dedicated de novo lipoylation enzymes LipB (PP_4801) and LipA (PP_4800) and from the biotin-protein ligase BirA (PP_0437). This makes it the unique candidate to supply the organism's lipoate **salvage/relay** activity. The reader should note that this is a **strong, multi-line inference and not a direct experimental result**: PP_0423 itself has not been biochemically characterized, and KEGG still lists it as a "conserved protein of unknown function." The single-domain architecture (it lacks the ~80-residue C-terminal accessory domain of full-length *E. coli* LplA) introduces a residual mechanistic caveat, though precedents show single catalytic domains of this family can be catalytically active.

---

## Key Findings

### F001 — PP_0423 belongs to the BPL/LPL catalytic-domain family (LplA/LipM/LipL clade)

PP_0423 is unambiguously assigned to the biotin/lipoate protein-ligase superfamily by concordant database signatures: UniProt Q88QR5 carries **PROSITE PS51733** ("BPL/LPL catalytic domain"); InterPro **IPR045864** (aa-tRNA-synth_II/BPL/LPL), **IPR004143** (BPL_LPL_catalytic), and **IPR050664** (Octanoyltransferase LipM/LipL); Pfam **PF21948** (LplA-B_cat) and **PF03099** (BPL_LplA_LipB); and eggNOG **COG0095** (lipoate-protein ligase A family). The protein is only **234 aa** — a single catalytic domain that lacks the C-terminal accessory domain present in two-domain LplA proteins such as *E. coli* LplA (~338 aa), matching single-domain family members (e.g., *Thermoplasma* LplA ~29 kDa; LipM/LipL).

This fold is structurally homologous to the catalytic domains of **class II aminoacyl-tRNA synthetases and biotin protein ligase BirA** ([PMID: 16384580](https://pubmed.ncbi.nlm.nih.gov/16384580/): *"structurally homologous to the catalytic domains of class II aminoacyl-tRNA synthases and biotin protein ligase, BirA"*). The same study documents that a short single-domain member can exist within this family: *"The putative LplA of T.acidophilum lacks a C-terminal domain found in its counterparts in E.coli (Gram-negative) or Streptococcus pneumoniae (Gram-positive)."* The two-step ATP-dependent mechanism predicted for the PP_0423 catalytic domain is defined by [PMID: 20089862](https://pubmed.ncbi.nlm.nih.gov/20089862/): *"Lipoate-protein ligase A (LplA) catalyzes the attachment of lipoic acid to lipoate-dependent enzymes by a two-step reaction: first the lipoate adenylation reaction and, second, the lipoate transfer reaction."*

### F002 — PP_0423 is an uncharacterized paralog distinct from the canonical de novo lipoylation genes lipB (PP_4801) and lipA (PP_4800)

KEGG assigns **no KO** to ppu:PP_0423 (entry name "conserved protein of unknown function") and does **not** place it in the lipoic-acid metabolism pathway (ppu00785). By contrast, KT2440 has clearly annotated de novo lipoylation genes: **lipB = PP_4801** (lipoyl(octanoyl)transferase, K03801, EC 2.3.1.181) and **lipA = PP_4800** (lipoyl synthase, K03644, EC 2.8.1.8); no canonical LplA (K03800) is annotated in the genome. PP_0423 (gene position 512,008–512,712; protein AAN66053) is genomically remote from the lipB–lipA locus and from the E2/GcvH lipoyl-domain genes. Its Pfam architecture (LplA-B_cat + BPL_LplA_LipB) is the ligase/adenylation fold, distinct from LipB's transferase KO.

Caution is warranted in assigning a precise reaction, because the Lpl family is functionally diverse ([PMID: 23960015](https://pubmed.ncbi.nlm.nih.gov/23960015/): *"There is a surprising diversity within the Lpl family of enzymes, several of which catalyse reactions other than ligation reactions"*). The same review documents the relay precedent: *"the Bacillus subtilis Lpl homologue LipM is an octanoyltransferase that transfers the octanoyl moiety from octanoyl-ACP to GCV. Another B. subtilis Lpl homologue, LipL, transfers octanoate from octanoyl-GCV to other LDs in an amido-transfer reaction."*

### F003 — PP_0423 functionally associates with lipoyl-carrier proteins (GcvH and 2-oxoacid dehydrogenase E2 subunits)

STRING (v12, taxid 160488) interaction partners for 160488.PP_0423, ranked by combined score, are **exclusively lipoyl-domain-bearing proteins or their cognate E3**:

| Partner | Role | Combined score |
|---|---|---|
| gcvH-II | Glycine cleavage H-protein (lipoyl carrier) | 0.829 |
| gcvH-I | Glycine cleavage H-protein (lipoyl carrier) | 0.829 |
| sucA | 2-oxoglutarate DH E1 | 0.767 |
| acoC | Acetoin DH E2 (dihydrolipoyllysine acetyltransferase) | 0.761 |
| acoB | Acetoin DH complex | 0.723 |
| bkdAB | Branched-chain 2-oxoacid DH | 0.722 |
| sucB | 2-oxoglutarate DH E2 (dihydrolipoyl succinyltransferase) | 0.707 |
| bkdB | Branched-chain 2-oxoacid DH E2 | 0.707 |
| aceF | Pyruvate DH E2 | 0.707 |
| acoA / bkdAA | 2-oxoacid DH complexes | 0.692 |
| lpd / lpdG / lpdV | Dihydrolipoamide dehydrogenase (E3) | 0.601 |

The two **GcvH paralogs are the single strongest associations** — exactly the substrate set expected of lipoate ligases/octanoyltransferases. Notably, the genomic neighborhood (PP_0420–0422 = trp/pabB biosynthesis; PP_0424 = CRP/FNR regulator) is functionally unrelated, so the STRING association reflects **functional coupling, not positional co-occurrence**. A strong GcvH association is precisely what is expected for an Lpl-family enzyme in the octanoyl/lipoyl relay ([PMID: 23960015](https://pubmed.ncbi.nlm.nih.gov/23960015/)).

### F004 — By global alignment, PP_0423 is most closely related to *E. coli* LplA, identifying it as an LplA-type ligase rather than a LipB octanoyltransferase

Needleman–Wunsch global alignment (BLOSUM62, gap −8) of PP_0423 against characterized family members yields a clear best match to LplA:

| Reference protein | UniProt | Function | % identity to PP_0423 |
|---|---|---|---|
| *E. coli* LplA | P32099 | Lipoate-protein ligase A | **33.3%** (78/234) |
| *B. subtilis* LipL | P39648 | octanoyl-[GcvH]:protein N-octanoyltransferase | 28.6% |
| *B. subtilis* LipM | P54511 | octanoyltransferase | 27.8% |
| *B. subtilis* LplJ | O07608 | lipoate ligase | 26.1% |
| *E. coli* LipB | P60720 | octanoyltransferase | 20.7% |

LplA is the clear best match, and LipB is the weakest — arguing strongly that PP_0423 is a **ligase (adenylate-forming)** enzyme rather than a LipB-type transferase. The 234-aa protein corresponds to the N-terminal catalytic (adenylate-forming) domain and lacks the ~80-residue C-terminal accessory domain of full-length *E. coli* LplA (338 aa), matching the architecture of single-domain LplA orthologs such as *Thermoplasma acidophilum* LplA ([PMID: 16384580](https://pubmed.ncbi.nlm.nih.gov/16384580/)). The catalytic activity of this LplA subfamily is defined by [PMID: 20089862](https://pubmed.ncbi.nlm.nih.gov/20089862/).

### F005 — PP_0423 is a soluble cytoplasmic protein consistent with acting on cytoplasmic lipoyl-domain substrates

Kyte–Doolittle hydropathy analysis (window 19) of the 234-aa sequence gives a maximum mean hydropathy of **1.21** (at residue 52), with no window exceeding the ~1.6–1.8 threshold indicative of a transmembrane helix. The N-terminus (MTDQPLALSVEQGLHAEQE…) shows no hydrophobic core or signal-peptide architecture, and the amino-acid composition (24% charged residues D/E/K/R) is typical of a soluble cytoplasmic enzyme. This matches the biochemistry of all characterized LplA/LipB/LipM/LipL enzymes, which act in the cytoplasm on the lipoyl domains of 2-oxoacid dehydrogenase E2 subunits and the glycine-cleavage H-protein ([PMID: 35736229](https://pubmed.ncbi.nlm.nih.gov/35736229/): *"It is covalently bound to the lipoyl domain of the E2 subunit in some 2-oxoacid dehydrogenase complexes and the H-protein in the glycine cleavage system"*).

### F006 — Predicted primary function: an ATP-dependent lipoate/octanoate-protein ligase (LplA-type)

Converging evidence — domain/family membership (closest match *E. coli* LplA, 33.3% identity), an exclusively lipoyl-carrier STRING network (GcvH-I/II top, plus E2 subunits and E3), and cytoplasmic localization — supports assigning PP_0423 as an **ATP-dependent lipoate/octanoate-protein ligase** that attaches free lipoate/octanoate to E2 and H-protein lipoyl domains. The exact reaction and substrates are stated by [PMID: 35736229](https://pubmed.ncbi.nlm.nih.gov/35736229/): *"Lipoate-protein ligase (Lpl) is involved in the salvage of exogenous lipoate and attaches free lipoate to the E2 subunit or the H-protein in an ATP-dependent manner."*

Crucially, single-domain Lpl catalytic modules are **precedented to be active**. In *Thermococcus kodakarensis*, the Lpl N-terminal catalytic region (TK1908) alone catalyzes the ligase reaction (*"the TK1908 protein alone was able to catalyze the ligase reaction although with a much lower activity"*), pairs with a C-terminal-region protein (TK1234) as a heterodimer, and, importantly, shows **broad fatty-acid specificity** including octanoate: *"together displayed significant ligase activity toward octanoate in addition to lipoate when a chemically synthesized octapeptide was used as the acceptor. The proteins also displayed activity toward other fatty acids, indicating broad fatty acid specificity"* ([PMID: 35736229](https://pubmed.ncbi.nlm.nih.gov/35736229/)). This shows a single ~234-aa catalytic domain such as PP_0423, lacking the LplA C-terminal accessory domain, can be a functional ATP-dependent ligase, potentially assisted by a separate accessory subunit.

### F007 — PP_0423 is the sole LplA/LipM/LipL-clade protein in the KT2440 proteome

A UniProt proteome scan of *P. putida* KT2440 (organism_id 160488) for the BPL/LPL catalytic domain (IPR004143) returns exactly three proteins:

| Protein | UniProt | Locus | Function | Length |
|---|---|---|---|---|
| LipB | Q88DM4 | PP_4801 | octanoyltransferase (EC 2.3.1.181) | 216 aa |
| BirA | Q88QQ1 | PP_0437 | bifunctional biotin ligase/repressor (EC 6.3.4.15) | 319 aa |
| **PP_0423** | **Q88QR5** | **PP_0423** | **LplA/LipM/LipL-clade (uncharacterized)** | **234 aa** |

PP_0423 is the **only** member of the Octanoyltransferase LipM/LipL clade (IPR050664) in the genome. The de novo lipoylation branch (LipB + LipA=PP_4800) and the biotin-ligation function (BirA) are covered by dedicated enzymes, leaving PP_0423 as the **unique candidate** for LplA/LipM/LipL-type lipoate/octanoate salvage-or-relay activity. Identification is unambiguous — PP_0423 is a separate protein from BirA (PP_0437). This maps directly onto the two branches of lipoate acquisition described by [PMID: 35764173](https://pubmed.ncbi.nlm.nih.gov/35764173/): *"In microorganisms, lipoic acid can be salvaged from the surroundings by lipoate protein ligase A (LplA), an ATP-dependent enzyme. Alternatively, it can be synthesized by the sequential actions of lipoate protein ligase B (LipB) and lipoyl synthase (LipA)."*

### F008 — AlphaFold predicts a well-folded, ordered single catalytic domain (mean pLDDT 95.7)

The AlphaFold DB model for Q88QR5 (v6, 234 residues) has a **mean per-residue pLDDT of 95.7** (median 97.9); 99% of residues exceed pLDDT 70 (confident) and 89% exceed 90 (very high). The N-terminal (residues 1–15, mean 92) and C-terminal (last 15, mean 94) segments are also confidently modeled, indicating no large disordered regions. This corresponds to a **compact, ordered BPL/LPL-type α/β fold** spanning the whole protein, supporting an intact functional enzyme rather than a decayed pseudo-enzyme. The high confidence over the entire length reinforces that PP_0423 is a bona fide single-domain catalytic module.

---

## Mechanistic Model and Interpretation

### The reaction

PP_0423 is predicted to catalyze the classic **two-step LplA lipoylation reaction**:

```
Step 1 (adenylation):   Lipoate  +  ATP  ──►  Lipoyl-AMP  +  PPi
Step 2 (transfer):      Lipoyl-AMP  +  [apo-LD]-Lys-NH2  ──►  [holo-LD]-Lys-NH-lipoyl  +  AMP

(with broad specificity, octanoate can substitute for lipoate in step 1)
```

The product is an **amide (isopeptide) bond** between the lipoyl carboxylate and the ε-amino group of a specific, conserved lysine in the target lipoyl domain (LD).

### Where it acts and on what

```
                    CYTOPLASM (soluble; no signal peptide / TM helix — F005, F008)
   ┌───────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │   exogenous / salvaged                                                  │
   │      LIPOATE ──┐        ┌────────────────────┐                          │
   │   (or octanoate)│  ATP  │   PP_0423 (LplA)   │                          │
   │                 ├──────►│  BPL/LPL catalytic │                          │
   │            lipoyl-AMP   │      domain        │                          │
   │                         └─────────┬──────────┘                          │
   │                                   │ lipoyl transfer                     │
   │            ┌──────────────────────┼───────────────────────┐            │
   │            ▼                       ▼                        ▼            │
   │   GcvH-I / GcvH-II          E2 lipoyl domains        (E3 lpd assoc.)     │
   │  (glycine cleavage      aceF (PDH), sucB (OGDH),                         │
   │    H-protein — top       bkdB (BCKDH), acoC (AoDH)                       │
   │    STRING partners)                                                     │
   │            │                       │                                    │
   │            ▼                       ▼                                    │
   │   one-carbon / glycine      central carbon & energy metabolism          │
   │   metabolism                (TCA cycle, pyruvate & BCAA oxidation)       │
   └───────────────────────────────────────────────────────────────────────┘
```

### Physiological role

Lipoic acid is an essential cofactor that must be covalently attached to lipoyl domains for the corresponding complexes to function. Cells acquire lipoylated proteins via **two routes**: (i) **de novo synthesis** (LipB transfers octanoate from octanoyl-ACP to the LD, then LipA inserts two sulfurs to make lipoate in situ), and (ii) **salvage**, in which LplA scavenges free lipoate from the environment and ligates it directly ([PMID: 35764173](https://pubmed.ncbi.nlm.nih.gov/35764173/)). KT2440 has the full de novo branch (PP_4800/PP_4801). PP_0423, as the sole LplA-clade enzyme (F007), is best interpreted as the organism's **salvage ligase** — enabling *P. putida* to exploit environmental lipoate — and/or a participant in an **octanoyl/lipoyl relay** analogous to the *B. subtilis* LipM→GcvH→LipL system, consistent with GcvH being its strongest functional partner (F003).

The substrate set — pyruvate dehydrogenase (aceF), 2-oxoglutarate dehydrogenase (sucB), branched-chain 2-oxoacid dehydrogenase (bkdB), acetoin dehydrogenase (acoC), and the glycine cleavage H-protein (GcvH) — places PP_0423 at the hub connecting **central carbon/energy metabolism** (TCA cycle flux, pyruvate and branched-chain amino-acid oxidation) with **one-carbon/glycine metabolism** (glycine cleavage system). This is consistent with the metabolic centrality of lipoylation and the glycine cleavage system ([PMID: 35294558](https://pubmed.ncbi.nlm.nih.gov/35294558/)).

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [16384580](https://pubmed.ncbi.nlm.nih.gov/16384580/) | Structure of a putative lipoate protein ligase from *Thermoplasma acidophilum* | Defines the BirA/aaRS-like fold of the family; documents a single-domain LplA lacking the C-terminal accessory domain — the precedent for PP_0423's 234-aa architecture (F001, F004) |
| [20089862](https://pubmed.ncbi.nlm.nih.gov/20089862/) | Global conformational change in *E. coli* LplA two-step reaction | Establishes the two-step adenylation + transfer mechanism predicted for PP_0423's catalytic domain (F001, F004) |
| [16141198](https://pubmed.ncbi.nlm.nih.gov/16141198/) | Crystal structure of LplA bound to lipoyl-AMP intermediate | Details the lipoyl-AMP intermediate and LplA–lipoyl-domain recognition, the structural basis of the predicted reaction |
| [23960015](https://pubmed.ncbi.nlm.nih.gov/23960015/) | Role of *S. cerevisiae* Lip3 / Lpl family diversity | Warns that the Lpl family is functionally diverse (some members are not ligases); provides the LipM/LipL octanoyl-relay precedent (F002, F003) |
| [35736229](https://pubmed.ncbi.nlm.nih.gov/35736229/) | A Lipoate-Protein Ligase Is Required for … (*T. kodakarensis*) | States the salvage reaction/substrates (E2 + H-protein, ATP-dependent); shows a single catalytic domain can be active and displays broad octanoate/lipoate specificity (F005, F006) |
| [35764173](https://pubmed.ncbi.nlm.nih.gov/35764173/) | Lipoate protein ligase B substrate recognition | Defines the salvage (LplA) vs de novo (LipB/LipA) branches, framing PP_0423 as the sole LplA-clade candidate (F007) |
| [35294558](https://pubmed.ncbi.nlm.nih.gov/35294558/) | Glycine Cleavage System engineering review | Context for the metabolic importance of the GcvH substrate and one-carbon/glycine metabolism |

The remaining papers surfaced during literature searches (e.g., clinical/nutraceutical studies of α-lipoic acid, cuproptosis reviews) are **not directly relevant** to the enzymology of PP_0423 and were not used to support functional claims; they reflect the dominance of "lipoic acid" as a clinical keyword rather than the bacterial ligase.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization.** There is no experimental study of PP_0423 itself. The functional assignment is an inference from domain architecture, homology, functional-association networks, and structural prediction. KEGG still lists PP_0423 as a "conserved protein of unknown function."

2. **Ligase vs. transferase ambiguity is not fully closed.** Although homology favors an LplA-type **ligase** (33.3% identity to *E. coli* LplA vs 20.7% to LipB), the Lpl family includes members that catalyze non-ligation reactions (e.g., LipM/LipL amido-transfer; [PMID: 23960015](https://pubmed.ncbi.nlm.nih.gov/23960015/)). It remains formally possible that PP_0423 is an octanoyl/lipoyl **relay transferase** rather than a free-lipoate salvage ligase.

3. **Single-domain caveat.** PP_0423 lacks the C-terminal accessory domain of two-domain LplA. While precedent shows single catalytic domains can be active (TK1908 alone; [PMID: 35736229](https://pubmed.ncbi.nlm.nih.gov/35736229/)), such activity was reduced and, in that case, enhanced by a separate accessory partner protein. Whether PP_0423 requires a partner subunit in *P. putida* is unknown.

4. **Substrate specificity not experimentally resolved.** The STRING network implicates GcvH and multiple E2 subunits, but the true in vivo acceptor(s) and the lipoate/octanoate preference have not been measured for this enzyme.

5. **Localization is predicted, not observed.** Cytoplasmic assignment is based on sequence-derived hydropathy and family precedent, not on cell-fractionation or microscopy data.

6. **Physiological redundancy is untested.** Because KT2440 encodes an intact de novo pathway (LipB/LipA), the phenotypic consequence of deleting PP_0423 (e.g., loss of lipoate salvage) has not been demonstrated.

---

## Proposed Follow-up Experiments / Actions

1. **In vitro ligase assay.** Express and purify recombinant PP_0423; test ATP-dependent formation of lipoyl-AMP and transfer of lipoate/octanoate to a recombinant apo-lipoyl domain (or a synthetic acceptor octapeptide), measuring PPi/AMP release and lipoylated-product formation by mass spectrometry. This directly distinguishes ligase from transferase activity.

2. **Substrate-specificity panel.** Assay activity against purified GcvH-I, GcvH-II, and the LDs of aceF, sucB, bkdB, and acoC to define acceptor preference; test lipoate vs octanoate vs other fatty acids to establish donor specificity (mirroring the *T. kodakarensis* study).

3. **Genetic complementation.** Test whether PP_0423 rescues an *E. coli* ∆lplA (or ∆lplA ∆lipB) lipoate-salvage-deficient strain grown on exogenous lipoate — a clean physiological readout of salvage-ligase function.

4. **Knockout phenotyping.** Construct a KT2440 ∆PP_0423 mutant and assay growth on media with/without exogenous lipoate, and under conditions taxing the glycine cleavage system, to reveal a salvage phenotype masked by the de novo pathway.

5. **Partner-subunit search.** Test whether PP_0423 requires or is stimulated by an accessory protein (co-purification/pull-down; check for a genomically dispersed C-terminal-domain partner analogous to *T. kodakarensis* TK1234).

6. **Structural confirmation.** Solve the crystal/cryo-EM structure (or validate the AlphaFold model) with bound lipoyl-AMP to confirm active-site residues and the U-shaped intermediate binding characteristic of LplA ([PMID: 16141198](https://pubmed.ncbi.nlm.nih.gov/16141198/)).

7. **Localization validation.** Use fluorescent tagging or cell fractionation to confirm cytoplasmic localization.

---

## Verification Note on Gene Identity

Per the mandatory verification steps: the gene symbol **PP_0423** and UniProt accession **Q88QR5** correspond to a **BPL/LPL catalytic-domain-containing protein** in *Pseudomonas putida* KT2440 (organism_id 160488), exactly matching the target description. The domains found in analysis (IPR004143, IPR050664, PF21948) align with the UniProt-provided domain list. No conflicting literature for a different gene with the same symbol was encountered; the identity is confirmed as the intended target. Literature specific to *this* protein is limited (it is uncharacterized), so the functional description is built from domain/family/homology inference as instructed, using primary literature on characterized family members.


## Artifacts

- [OpenScientist final report](PP_0423-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_0423-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16384580
2. PMID:20089862
3. PMID:23960015
4. PMID:35736229
5. PMID:35764173
6. PMID:35294558
7. PMID:16141198