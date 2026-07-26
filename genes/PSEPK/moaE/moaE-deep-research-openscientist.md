---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T14:20:29.825980'
end_time: '2026-07-20T14:40:16.769311'
duration_seconds: 1186.94
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: moaE
  gene_symbol: moaE
  uniprot_accession: Q88NB8
  protein_description: 'RecName: Full=Molybdopterin synthase catalytic subunit {ECO:0000256|ARBA:ARBA00013858};
    EC=2.8.1.12 {ECO:0000256|ARBA:ARBA00011950}; AltName: Full=MPT synthase subunit
    2 {ECO:0000256|ARBA:ARBA00030781}; AltName: Full=Molybdenum cofactor biosynthesis
    protein E {ECO:0000256|ARBA:ARBA00029745}; AltName: Full=Molybdopterin-converting
    factor large subunit {ECO:0000256|ARBA:ARBA00030407}; AltName: Full=Molybdopterin-converting
    factor subunit 2 {ECO:0000256|ARBA:ARBA00032474};'
  gene_info: Name=moaE {ECO:0000313|EMBL:AAN66918.1}; OrderedLocusNames=PP_1294 {ECO:0000313|EMBL:AAN66918.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MoaE family.
  protein_domains: MoaE_sf. (IPR036563); Mopterin_biosynth_MoaE. (IPR003448); MoaE
    (PF02391)
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
  path: moaE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: moaE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88NB8
- **Protein Description:** RecName: Full=Molybdopterin synthase catalytic subunit {ECO:0000256|ARBA:ARBA00013858}; EC=2.8.1.12 {ECO:0000256|ARBA:ARBA00011950}; AltName: Full=MPT synthase subunit 2 {ECO:0000256|ARBA:ARBA00030781}; AltName: Full=Molybdenum cofactor biosynthesis protein E {ECO:0000256|ARBA:ARBA00029745}; AltName: Full=Molybdopterin-converting factor large subunit {ECO:0000256|ARBA:ARBA00030407}; AltName: Full=Molybdopterin-converting factor subunit 2 {ECO:0000256|ARBA:ARBA00032474};
- **Gene Information:** Name=moaE {ECO:0000313|EMBL:AAN66918.1}; OrderedLocusNames=PP_1294 {ECO:0000313|EMBL:AAN66918.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MoaE family.
- **Key Domains:** MoaE_sf. (IPR036563); Mopterin_biosynth_MoaE. (IPR003448); MoaE (PF02391)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "moaE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'moaE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **moaE** (gene ID: moaE, UniProt: Q88NB8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *moaE* (Q88NB8, PP_1294) — Molybdopterin Synthase Catalytic Subunit in *Pseudomonas putida* KT2440

## Summary

The gene **moaE** (locus tag **PP_1294**; UniProt **Q88NB8**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes the **catalytic large subunit of molybdopterin (MPT) synthase** (EC 2.8.1.12). This assignment is unambiguous and is supported by four independent, converging lines of evidence developed in this investigation: (1) direct biochemical and crystallographic characterization of orthologous MoaE proteins in the literature; (2) 66.9% amino-acid sequence identity to the experimentally characterized *Escherichia coli* MoaE, with all functional motifs conserved; (3) strict conservation of the active-site residues across 33 bacterial orthologs; and (4) a high-confidence AlphaFold structural model (mean pLDDT 92.9) that adopts the canonical MoaE fold with a well-defined active site.

Functionally, MoaE catalyzes the **second step of molybdenum cofactor (Moco) biosynthesis**: the conversion of the sulfur- and metal-free pterin **precursor Z** (cyclic pyranopterin monophosphate, cPMP) into **molybdopterin** by installing the two sulfur atoms of the **cis-dithiolene** group at the C1′ and C2′ positions of the pterin side chain. This dithiolene is the chemical moiety that subsequently chelates molybdenum to form the active cofactor. MoaE does not act alone: it forms a **heterotetramer** with two copies of the small sulfur-carrier subunit **MoaD** (PP_1293, Q88NB9), arranged as a central MoaE dimer flanked by two MoaD subunits. The thiocarboxylated C-terminus of each MoaD is deeply inserted into a MoaE subunit to complete the active site and donate the sulfur. MoaD is subsequently recharged with sulfur by the ubiquitin-E1-like activating enzyme **MoeB** (PP_0735), giving MoaE its catalytic cycle.

The reaction is carried out in the **cytoplasm**. In *P. putida* KT2440, *moaE* sits immediately downstream of its partner *moaD* within a complete set of *moa/mob/moe* Moco-biosynthesis genes, and the molybdopterin it produces is the essential precursor of Moco for the strain's downstream molybdoenzymes — including xanthine, nicotinate, aldehyde, and isoquinoline oxidoreductases, formate dehydrogenase, assimilatory nitrate reductase, and the periplasmic methionine-sulfoxide reductase MsrP. This report lays out the evidence for each of these conclusions in detail.

---

## Gene/Protein Identity Verification

Before describing function, the mandatory identity check confirms that this is the correct gene and that the literature used is appropriate.

| Attribute | Target (UniProt Q88NB8) | Verification result |
|---|---|---|
| Gene symbol | *moaE* | ✔ Matches "molybdopterin synthase catalytic subunit" annotation |
| Organism | *P. putida* KT2440 (taxid 160488) | ✔ Confirmed via UniProt locus PP_1294 |
| Protein family | MoaE family | ✔ Pfam PF02391 (MoaE), IPR003448, IPR036563 |
| EC number | 2.8.1.12 | ✔ Sulfurtransferase, MPT synthase |
| Ortholog identity | — | ✔ 66.9% identical to *E. coli* MoaE (P30749) |

The gene symbol *moaE* is **not ambiguous** in this context. Across bacteria, *moaE* consistently denotes the catalytic subunit of MPT synthase, and the *P. putida* protein aligns cleanly with characterized orthologs. The literature used below (predominantly *E. coli* and general Moco biochemistry) is directly applicable because MoaE is one of the most deeply conserved proteins in the Moco pathway. No conflicting gene family with the same symbol was encountered.

---

## Key Findings

### Finding 1 — Q88NB8 is a bona fide MoaE ortholog (molybdopterin synthase catalytic subunit)

A Needleman–Wunsch global alignment of *P. putida* Q88NB8 (148 aa) against the experimentally characterized *E. coli* MoaE (P30749, 150 aa) yields **66.9% identity** over aligned columns. This level of identity, well above the ~30% "twilight zone," places the two proteins firmly within the same functional orthology group. Critically, every functionally important motif known from *E. coli* MoaE is present and conserved in the *P. putida* sequence:

- the **precursor-Z-binding region** `LEHYPGMTEKAL`,
- the **HRIG loop**,
- the `IVFVGV` segment,
- the highly conserved **C-terminal active-site segment** `IMDYLKTRAPFW`, and
- the **SDQ motif**.

Both UniProt entries are annotated "Molybdopterin synthase catalytic subunit," and both carry the diagnostic domain signatures MoaE (PF02391), IPR003448 (Mopterin_biosynth_MoaE), and IPR036563 (MoaE_sf superfamily fold). Taken together, this establishes beyond reasonable doubt that Q88NB8 performs the same molecular function as the biochemically defined *E. coli* enzyme.

### Finding 2 — MoaE is the catalytic (large) subunit of a heterotetrameric MPT synthase

Molybdopterin synthase is a **heterotetramer of two large (MoaE) and two small (MoaD) subunits**. Structural work on the enzyme established that the two MoaD subunits sit at opposite ends of a **central MoaE dimer**, and that the **C-terminus of each MoaD is deeply inserted into a MoaE subunit to form the active site** [PMID: 12571227](https://pubmed.ncbi.nlm.nih.gov/12571227/). This architecture means MoaE provides the structural scaffold and the bulk of the catalytic pocket, while MoaD delivers the reactive sulfur to that pocket.

The enzyme catalyzes the **second step of Moco biosynthesis** (EC 2.8.1.12), converting precursor Z into molybdopterin and thereby generating the **cis-dithiolene group** that coordinates molybdenum in the final cofactor [PMID: 18092812](https://pubmed.ncbi.nlm.nih.gov/18092812/). The 2×MoaE + 2×MoaD stoichiometry and the central-MoaE-dimer organization are directly stated in the structural study of the MoaE–precursor Z complex: *"The second step is catalyzed by the heterotetrameric MPT synthase protein consisting of two large (MoaE) and two small (MoaD) subunits with the MoaD subunits located at opposite ends of a central MoaE dimer."*

### Finding 3 — Reaction mechanism: two sulfurs from MoaD thiocarboxylate build the dithiolene

The chemistry catalyzed by MoaE is the **transfer of sulfur atoms from a C-terminal MoaD thiocarboxylate to the C-1′ and C-2′ positions of precursor Z**, converting the sulfur- and metal-free pterin into molybdopterin [PMID: 18092812](https://pubmed.ncbi.nlm.nih.gov/18092812/). In the crystal structure of the MoaE–precursor Z complex, precursor Z is **bound by strictly conserved residues in a pocket at the MoaE dimer interface, in close proximity to the C-terminal glycine of MoaD**, and biochemical evidence indicates that the **first dithiolene sulfur is added at the C-2′ position** [PMID: 18092812](https://pubmed.ncbi.nlm.nih.gov/18092812/). This localizes the active site precisely to the interface of the MoaE dimer and defines the order of the two sulfur-transfer events.

The requirement for the thiocarboxylate form is strict: **only the thiocarboxylated MPT synthase complex is able to convert precursor Z to MPT in vitro** [PMID: 11459846](https://pubmed.ncbi.nlm.nih.gov/11459846/). This confirms that the terminal thiocarboxylate on MoaD is the obligatory sulfur donor for the MoaE-catalyzed reaction, and that a mechanism generating a dithiolene from two thiocarboxylate groups on a single tetrameric enzyme is operative.

### Finding 4 — MoaD sulfur is regenerated by the ubiquitin-E1-like enzyme MoeB, sustaining MoaE catalysis

Because each catalytic turnover consumes the MoaD thiocarboxylate sulfur, MoaD must be recharged. During MPT biosynthesis, **MoaD cycles between two heterotetrameric complexes — one with MoaE (to form MPT synthase) and one with MoeB (an E1-like activating enzyme, to regenerate its transferable sulfur)** [PMID: 17223713](https://pubmed.ncbi.nlm.nih.gov/17223713/). Mechanistically, **MoeB activates the C-terminus of MoaD to form an acyl-adenylate in an ATP-dependent manner, after which a sulfurtransferase converts the MoaD acyl-adenylate to a thiocarboxylate that serves as the sulfur donor during Moco biosynthesis** [PMID: 11713534](https://pubmed.ncbi.nlm.nih.gov/11713534/).

MoaD itself has a **ubiquitin fold with a conserved C-terminal Gly-Gly motif**; the terminal glycine is essential for MoaD-AMP formation and important for sulfur transfer to precursor Z [PMID: 17223713](https://pubmed.ncbi.nlm.nih.gov/17223713/). This deep mechanistic parallel to eukaryotic ubiquitin activation was further characterized in *E. coli* MoeB, where ATP-dependent formation of a stable MoeB–MoaD-adenylate complex was demonstrated directly [PMID: 11463785](https://pubmed.ncbi.nlm.nih.gov/11463785/). The MoeB step is therefore the "reloading" reaction that keeps MoaE supplied with sulfur-charged MoaD.

### Finding 5 — Pathway and localization context: the MoaE step feeds Moco for >50 molybdoenzymes

Moco biosynthesis is an **ancient, ubiquitous, highly conserved cytoplasmic pathway** that can be divided into steps: (1) formation of cyclic pyranopterin monophosphate; (2) formation of MPT — **the MoaE/MoaD-catalyzed step**; (3) insertion of molybdenum to form Moco; and (4) in bacteria and archaea, attachment of a nucleotide to the phosphate group of MPT to form the dinucleotide (MGD/MCD) variant [PMID: 24980677](https://pubmed.ncbi.nlm.nih.gov/24980677/). The fourth step is directly relevant to *P. putida*, which uses bis-molybdopterin guanine dinucleotide (bis-MGD) enzymes.

The importance of the MoaE step is underscored by the reach of its product: **more than 50 molybdoenzymes have been identified, and in all of them except nitrogenase, molybdenum is coordinated to the dithiolene group of molybdopterin** [PMID: 24980677](https://pubmed.ncbi.nlm.nih.gov/24980677/). The dithiolene that MoaE installs is thus the universal molybdenum-chelating moiety required by essentially the entire molybdoenzyme superfamily.

### Finding 6 — *moaE* (PP_1294) is co-encoded with *moaD* (PP_1293) within a complete Moco gene set in KT2440

A UniProt survey of *P. putida* KT2440 (taxid 160488) shows **moaD (PP_1293, Q88NB9, "Molybdopterin synthase sulfur carrier subunit") immediately adjacent to and upstream of moaE (PP_1294, Q88NB8, "Molybdopterin synthase catalytic subunit")**, consistent with an operonic arrangement encoding both subunits of MPT synthase side by side — precisely the genetic organization expected for an obligate heterotetramer. Beyond the *moaD–moaE* pair, the strain encodes the full pathway:

| Step | Enzyme / function | Gene(s) in KT2440 |
|---|---|---|
| 1 | GTP 3′,8-cyclase (cPMP synthesis) | *moaA* (PP_4597; paralogs PP_1969/PP_2482) |
| 1 | cPMP synthase | *moaC* (PP_1292) |
| **2** | **MPT synthase (sulfur carrier + catalytic)** | ***moaD* (PP_1293) + *moaE* (PP_1294)** |
| — | MoaD sulfur regeneration (E1-like) | *moeB* (PP_0735) |
| 3 | Molybdopterin-related / molybdenum insertion | *moaB* (PP_2122/PP_4600), *moeA* (PP_2123) |
| 4 | Mo cofactor guanylyltransferase (bis-MGD) | *mobA* (PP_3457) |

The co-localization of *moaE* with *moaC* (PP_1292, the upstream cPMP-synthesis step) and *moaD* (PP_1293) in the same genomic neighborhood strongly reinforces the functional assignment: the enzyme that MoaE forms consumes the product of MoaC and requires the MoaD encoded next to it.

### Finding 7 — Moco produced downstream of MoaE serves a defined set of *P. putida* molybdoenzymes

The molybdopterin generated by MoaE is not an end in itself; it is the committed precursor of Moco, which activates a specific complement of molybdoenzymes in KT2440. UniProt annotation identifies these downstream client enzymes:

- **Xanthine dehydrogenase** (*xdhB* PP_4279; aldehyde oxidase/XDH-family PP_4234)
- **Nicotinate dehydrogenase** (*nicB* PP_3948)
- **Aromatic aldehyde dehydrogenase / aldehyde oxidase** (*paoC* PP_3310)
- **Isoquinoline 1-oxidoreductase** beta subunits (PP_3622, PP_2478)
- **Formate dehydrogenase** (*fdoG* PP_0489, alpha subunit PP_2185; with FdhD sulfur carrier PP_0257)
- **Assimilatory nitrate reductase / sulfite reductase** (PP_1703)
- **Periplasmic bis-MGD methionine-sulfoxide reductase MsrP** (PP_4676)

Molybdate, the elemental substrate that is ultimately inserted into the MoaE-produced dithiolene, is acquired via the **ModABC transporter** (*modA* PP_3828, *modB* PP_3829, *modC* PP_3830) under **ModR** regulation (PP_0360). This client list demonstrates that MoaE occupies a central biosynthetic node: its output is required for purine catabolism (xanthine DH), nitrogen assimilation (nitrate reductase), one-carbon metabolism (formate DH), and periplasmic redox repair (MsrP).

### Finding 8 — Deep evolutionary conservation pinpoints the active-site residues

A multiple-ortholog conservation analysis carried out in this investigation aligned **33 reviewed bacterial MoaE proteins** — spanning Gram-negative (E. coli, Salmonella, Vibrio, Haemophilus, *P. aeruginosa*, Yersinia, Caulobacter, Brucella, Rhizobium), Gram-positive (Bacillus, Staphylococcus), cyanobacterial (Nostoc, Synechococcus), actinobacterial (*M. tuberculosis*), and deep-branching (Aquifex) lineages — each against *P. putida* Q88NB8. Only **9 positions are strictly invariant** across this broad phylogenetic sampling (P. putida numbering): **M1, G34, R37, G42, H81, G84, K117, P121, W123** — just 6% of the 148 residues.

Crucially, these invariant residues cluster in the two motifs that the crystallographic work implicated in catalysis: **H81/G84 lie in the "HRIG" loop**, and **K117/P121/W123 lie in the strictly conserved C-terminal "IMDYLKTRAPFW" segment** (residues 112–123). The near-absolute conservation of exactly these positions across billions of years of bacterial evolution is a strong independent, purely bioinformatic argument that they form the functional active site — the same interface at which precursor Z binds and the MoaD C-terminus inserts.

### Finding 9 — AlphaFold confirms a high-confidence MoaE fold with a well-defined active site

The AlphaFold DB model **AF-Q88NB8-F1** (v6, 148 residues) is **high confidence overall**: mean pLDDT 92.9, median 95.9, with **79.1% of residues at very-high confidence (pLDDT ≥ 90)**, 97.3% ≥ 70, and 0% below 50. The structured core (residues 6–143) averages pLDDT 93.0. Importantly, the strictly conserved active-site residues identified in Finding 8 are all modeled with very high confidence: H81 = 98.1, G84 = 96.6 (HRIG loop); K117 = 93.7, P121 = 93.6, W123 = 94.6 (C-terminal segment); G34 = 97.0; R37 = 87.9. Only the flexible N-terminal Met (M1 = 59.3) is low, as expected for a disordered terminus. The convergence of high structural confidence with the evolutionary conservation signal at the same residues provides a coherent structural picture of a fully folded MoaE with an intact catalytic pocket.

---

## Mechanistic Model / Interpretation

The findings assemble into a single coherent mechanistic narrative. MoaE is the catalytic hub of the two-subunit MPT synthase, working in a sulfur-transfer cycle that is chemically analogous to eukaryotic ubiquitin activation.

```
   MOLYBDENUM COFACTOR (Moco) BIOSYNTHESIS — the MoaE step in context
   ====================================================================

   GTP ──moaA──▶ cPMP (precursor Z) ──moaC (PP_1292)──▶ [cyclic pyranopterin monophosphate]
                                                                 │
                                                                 ▼  STEP 2  (EC 2.8.1.12)
                 ┌───────────────────────────────────────────────────────────┐
                 │            MPT SYNTHASE  (heterotetramer)                    │
                 │                                                             │
                 │      MoaD ── [ MoaE ── MoaE ] ── MoaD                        │
                 │    (PP_1293)   central dimer   (PP_1293)                     │
                 │       │        (PP_1294)          │                         │
                 │  C-term thiocarboxylate inserted into MoaE active site       │
                 │       │                           │                         │
                 │       ▼                           ▼                         │
                 │  transfers S → C2' , then C1' of precursor Z                │
                 └───────────────────────────────────────────────────────────┘
                                           │
                                           ▼
                               MOLYBDOPTERIN (MPT)  ← cis-dithiolene formed
                                           │
        MoaD (spent) ◀── recharge ──▶ moeB (PP_0735)   │  moeA (PP_2123) + Mo
        ATP → MoaD-adenylate → thiocarboxylate         ▼
                                     Mo INSERTED → Moco → +GMP (mobA) → bis-MGD
                                                                 │
                                                                 ▼
      Downstream molybdoenzymes: xanthine DH, nicotinate DH, aldehyde oxidase,
      isoquinoline oxidoreductase, formate DH, nitrate reductase, MsrP (periplasm)
```

**The core reaction.** MoaE receives precursor Z (cPMP) from the MoaC step. Precursor Z has the pterin ring but lacks the sulfur-bearing dithiolene needed to chelate molybdenum. Two MoaE monomers dimerize to create the substrate pocket at their shared interface (Finding 3). A sulfur-charged MoaD docks onto each MoaE, inserting its thiocarboxylated C-terminal Gly into the pocket (Finding 2). MoaE then catalyzes transfer of the first sulfur to C-2′ and the second to C-1′ of precursor Z, forming the cis-dithiolene and thereby converting precursor Z to molybdopterin (Finding 3). Because each turnover requires two sulfurs and each MoaD carries only one, the tetramer's two MoaD subunits jointly furnish the two sulfurs of a single dithiolene.

**The sulfur-supply cycle.** Spent (desulfured) MoaD dissociates from MoaE and binds MoeB instead. MoeB, an E1-ubiquitin-activating-enzyme homolog, adenylates the MoaD C-terminus (ATP-dependent), and a sulfurtransferase then converts the acyl-adenylate to a thiocarboxylate (Finding 4). Recharged MoaD returns to MoaE. Thus MoaD shuttles between MoaE (catalysis) and MoeB (recharging), and MoaE's throughput is coupled to this cycle.

**Localization.** Every step described here occurs in the **cytoplasm**; the whole Moco pathway is soluble and cytosolic (Finding 5). This is where MoaE carries out its function. The distinction with the periplasm is only relevant downstream: some Moco-client enzymes (notably MsrP, PP_4676) function in the periplasm, but they receive a *pre-assembled* bis-MGD cofactor whose molybdopterin backbone was built by MoaE in the cytoplasm.

**Structural/evolutionary corroboration.** The invariant residues H81, G84 (HRIG loop) and K117, P121, W123 (C-terminal IMDYLKTRAPFW segment) map onto exactly the crystallographically defined catalytic interface, and AlphaFold models them all at very high confidence in a well-folded core (Findings 8–9). Sequence, structure, and evolution all point to the same active site.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [12571227](https://pubmed.ncbi.nlm.nih.gov/12571227/) | *Structural studies of molybdopterin synthase* | Defines MoaE as the large subunit forming the heterotetramer's active site; MoaD C-terminus inserts into MoaE |
| [18092812](https://pubmed.ncbi.nlm.nih.gov/18092812/) | *Crystal structure of a MPT synthase–precursor Z complex* | Establishes 2×MoaE+2×MoaD architecture; substrate = precursor Z; sulfur to C1′/C2′; active site at MoaE dimer interface; first S at C2′ |
| [11459846](https://pubmed.ncbi.nlm.nih.gov/11459846/) | *Thiocarboxylation of molybdopterin synthase* | Shows only the thiocarboxylated complex converts precursor Z to MPT — the MoaD thiocarboxylate is the obligatory sulfur donor |
| [17223713](https://pubmed.ncbi.nlm.nih.gov/17223713/) | *C-terminal Gly-Gly motif of E. coli MoaD* | MoaD cycles between MoaE and MoeB; ubiquitin fold; terminal Gly essential for adenylate formation and sulfur transfer |
| [11713534](https://pubmed.ncbi.nlm.nih.gov/11713534/) | *Structure of a bacterial MoeB-MoaD complex* | Mechanism of MoaD recharging: MoeB adenylates MoaD C-terminus; sulfurtransferase generates the thiocarboxylate |
| [11463785](https://pubmed.ncbi.nlm.nih.gov/11463785/) | *Characterization of E. coli MoeB* | Demonstrates ATP-dependent MoeB–MoaD-adenylate complex; parallels ubiquitin activation |
| [24980677](https://pubmed.ncbi.nlm.nih.gov/24980677/) | *The biosynthesis of the molybdenum cofactors* | Places MPT formation as step 2 of the cytoplasmic pathway; >50 molybdoenzymes use the MPT dithiolene to coordinate Mo |

**Consistency of the evidence.** All seven papers are mutually reinforcing; none challenges the annotation. The structural studies (12571227, 18092812) and the biochemical study (11459846) directly define the reaction, substrate, and active-site location. The MoaD/MoeB studies (17223713, 11713534, 11463785) define the sulfur-supply cycle that MoaE depends on. The review (24980677) situates the step in the full pathway and quantifies its downstream importance. Because MoaE is highly conserved (66.9% identity to *E. coli*), these mechanistic conclusions transfer with high confidence to the *P. putida* protein — a transfer independently validated by the conservation and structural analyses (Findings 8–9).

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* protein.** All mechanistic and structural data come from orthologs (chiefly *E. coli*) and from bioinformatic/structural inference on Q88NB8 itself. There is no published enzyme assay, crystal structure, or knockout phenotype specifically for PP_1294. The functional assignment, while very strong, rests on homology transfer plus in-silico corroboration.

2. **Operon structure inferred, not experimentally mapped.** The *moaD–moaE* adjacency and the broader gene set were established from UniProt/genomic annotation. Transcript boundaries, promoter architecture, and co-transcription of PP_1293/PP_1294 in KT2440 have not been experimentally confirmed here.

3. **Downstream client list is annotation-based.** The molybdoenzyme complement (Finding 7) derives from UniProt annotations, which the task instructions correctly flag as potentially outdated. Which of these enzymes are actually expressed and Moco-dependent under given growth conditions in KT2440 was not tested.

4. **Kinetics and substrate specificity not quantified for this ortholog.** Km, kcat, and any species-specific substrate features for *P. putida* MoaE are unknown; specificity is assumed identical to characterized orthologs.

5. **AlphaFold caveats.** The model is monomeric and high-confidence, but it does not itself demonstrate the dimer interface or the MoaE–MoaD complex; the active-site interpretation relies on mapping conserved residues onto the model by analogy with the *E. coli* co-crystal structures.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant reconstitution and activity assay.** Co-express *P. putida* MoaE (PP_1294) and MoaD (PP_1293), thiocarboxylate MoaD via MoeB (PP_0735), and assay conversion of precursor Z to molybdopterin in vitro (e.g., HPLC detection of Form A / dephospho-MPT). This would provide the missing direct biochemical confirmation and Km/kcat values.

2. **Genetic complementation / knockout.** Delete PP_1294 in KT2440 and test for loss of molybdoenzyme activities (e.g., nitrate reductase or xanthine dehydrogenase); complement with wild-type and with active-site point mutants (H81A, K117A, W123A) to validate the conserved residues identified in Finding 8.

3. **Operon mapping.** Use RT-PCR / RNA-seq to confirm co-transcription of PP_1293–PP_1294 and define the promoter, establishing the operon experimentally.

4. **Structural validation of the complex.** Solve or predict (AlphaFold-Multimer) the MoaE₂MoaD₂ heterotetramer for the *P. putida* proteins to confirm the dimer interface and MoaD C-terminal insertion, and compare with the *E. coli* co-crystal templates.

5. **Cofactor-flux phenotyping.** Under molybdate-limited and molybdate-replete conditions, measure which downstream molybdoenzymes (Finding 7) are active, to define the physiological demand that MoaE serves in KT2440.

---

## Conclusion

*moaE* (Q88NB8, PP_1294) in *Pseudomonas putida* KT2440 encodes the **catalytic large subunit of molybdopterin synthase** (EC 2.8.1.12). It catalyzes the second, sulfur-incorporating step of molybdenum cofactor biosynthesis in the cytoplasm — converting precursor Z into molybdopterin by installing the two sulfur atoms of the cis-dithiolene at C1′/C2′, using sulfur donated by the thiocarboxylated C-terminus of its partner subunit MoaD (which is recharged by the E1-like enzyme MoeB). The molybdopterin it produces is the obligate precursor of Moco, required to activate the strain's molybdoenzymes. This conclusion is supported by four converging evidence lines: ortholog biochemistry/crystallography, 66.9% identity to *E. coli* MoaE, strict active-site conservation across 33 bacterial orthologs, and a high-confidence AlphaFold model (mean pLDDT 92.9).


## Artifacts

- [OpenScientist final report](moaE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](moaE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12571227
2. PMID:18092812
3. PMID:11459846
4. PMID:17223713
5. PMID:11713534
6. PMID:11463785
7. PMID:24980677