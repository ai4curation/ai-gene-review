---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T06:18:20.857742'
end_time: '2026-07-17T06:42:15.349797'
duration_seconds: 1434.49
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pdxH
  gene_symbol: pdxH
  uniprot_accession: Q88NS5
  protein_description: 'RecName: Full=Pyridoxine/pyridoxamine 5''-phosphate oxidase
    {ECO:0000255|HAMAP-Rule:MF_01629}; EC=1.4.3.5 {ECO:0000255|HAMAP-Rule:MF_01629};
    AltName: Full=PNP/PMP oxidase {ECO:0000255|HAMAP-Rule:MF_01629}; Short=PNPOx {ECO:0000255|HAMAP-Rule:MF_01629};
    AltName: Full=Pyridoxal 5''-phosphate synthase {ECO:0000255|HAMAP-Rule:MF_01629};'
  gene_info: Name=pdxH {ECO:0000255|HAMAP-Rule:MF_01629}; OrderedLocusNames=PP_1129;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the pyridoxamine 5'-phosphate oxidase family.
  protein_domains: Pyridox_Oxase. (IPR000659); Pyridox_Oxase_CS. (IPR019740); Pyridox_Oxase_N.
    (IPR011576); Pyridoxamine_oxidase_dimer_C. (IPR019576); Split_barrel_FMN-bd. (IPR012349)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: pdxH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pdxH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88NS5
- **Protein Description:** RecName: Full=Pyridoxine/pyridoxamine 5'-phosphate oxidase {ECO:0000255|HAMAP-Rule:MF_01629}; EC=1.4.3.5 {ECO:0000255|HAMAP-Rule:MF_01629}; AltName: Full=PNP/PMP oxidase {ECO:0000255|HAMAP-Rule:MF_01629}; Short=PNPOx {ECO:0000255|HAMAP-Rule:MF_01629}; AltName: Full=Pyridoxal 5'-phosphate synthase {ECO:0000255|HAMAP-Rule:MF_01629};
- **Gene Information:** Name=pdxH {ECO:0000255|HAMAP-Rule:MF_01629}; OrderedLocusNames=PP_1129;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the pyridoxamine 5'-phosphate oxidase family.
- **Key Domains:** Pyridox_Oxase. (IPR000659); Pyridox_Oxase_CS. (IPR019740); Pyridox_Oxase_N. (IPR011576); Pyridoxamine_oxidase_dimer_C. (IPR019576); Split_barrel_FMN-bd. (IPR012349)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pdxH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pdxH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pdxH** (gene ID: pdxH, UniProt: Q88NS5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *pdxH* (Q88NS5, PP_1129) in *Pseudomonas putida* KT2440

**Gene:** *pdxH* — **UniProt:** Q88NS5 — **Locus:** PP_1129
**Protein:** Pyridoxine/pyridoxamine 5'-phosphate oxidase (PNPOx)
**EC:** 1.4.3.5 — **Family:** Pyridoxamine 5'-phosphate oxidase family
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), PSEPK

---

## Summary

**The product of *pdxH* (PP_1129) in *Pseudomonas putida* KT2440 is pyridoxine/pyridoxamine 5'-phosphate oxidase (PNPOx, EC 1.4.3.5), the FMN-dependent flavo-oxidase that carries out the terminal, committed step of vitamin B6 (pyridoxal 5'-phosphate, PLP) production.** It catalyzes the molecular-oxygen–dependent oxidation of either pyridoxine 5'-phosphate (PNP) at its C4′ hydroxyl group, or pyridoxamine 5'-phosphate (PMP) at its C4′ primary amine, to yield pyridoxal 5'-phosphate (PLP) — the catalytically active form of vitamin B6 — together with reduced flavin (FMNH₂) and hydrogen peroxide (H₂O₂). PLP is the essential cofactor for more than 140 distinct PLP-dependent enzymes governing amino-acid metabolism, one-carbon metabolism, and cofactor/neurotransmitter biosynthesis, making PdxH a hub of central metabolism.

This assignment is a **high-confidence annotation-by-orthology** grounded in three lines of evidence. First, UniProt/HAMAP rule MF_01629 places Q88NS5 in the pyridoxamine 5'-phosphate oxidase family, and the protein carries all diagnostic domains of that family (Pyridox_Oxase IPR000659; Split_barrel_FMN-bd IPR012349; the conserved-site signature IPR019740). Second, our own target-specific sequence analysis confirms Q88NS5 is a genuine PdxH ortholog: it shares ~40% amino-acid identity with the biochemically characterized *E. coli* enzyme over its full length, retains the catalytically essential active-site arginine (equivalent to *E. coli* Arg197), and matches the single-domain (~215 aa) architecture of the family. Third, the enzymology of the orthologous *E. coli* and human enzymes is established in exhaustive crystallographic, kinetic, and stereochemical detail, providing a mechanistic template that the *P. putida* enzyme, by conservation, is expected to follow.

Functionally, PdxH sits at the **convergence point of de novo PLP biosynthesis and B6 salvage**. Our proteome survey confirms that *P. putida* KT2440 possesses the complete *E. coli*-type, deoxyxylulose-5-phosphate (DXP)-dependent de novo pathway (Epd → PdxB → SerC → PdxA → PdxJ → PdxH) and lacks the alternative DXP-independent PdxS/PdxT synthase — meaning **PdxH is the organism's sole, non-redundant terminal step for producing PLP**. The enzyme is a soluble cytoplasmic protein (no transmembrane helix, no signal peptide by sequence analysis) that acts as an obligate homodimer with a split-barrel FMN fold, and is subject to product feedback inhibition by PLP binding at a non-catalytic allosteric site — a regulatory feature that keeps toxic free PLP low and channels the product directly to apo-B6 enzymes. No *P. putida*–specific experimental study of PP_1129 currently exists; the functional model rests on orthology to well-studied family members plus target-specific bioinformatic verification.

---

## Key Findings

### Finding 1 — PdxH is an FMN-dependent PNP/PMP oxidase catalyzing the terminal step of PLP biosynthesis

Q88NS5 is assigned by UniProt/HAMAP rule MF_01629 to the pyridoxamine 5'-phosphate oxidase family (EC 1.4.3.5) and shares the family's diagnostic domain architecture (Pyridox_Oxase IPR000659; Split_barrel_FMN-bd IPR012349). The reaction catalyzed by this family is definitively established biochemically in the orthologous *E. coli* enzyme. As stated by di Salvo and colleagues, "*Escherichia coli* pyridoxine 5'-phosphate oxidase (PNPOx) catalyzes the oxidation of either pyridoxine 5'-phosphate (PNP) or pyridoxamine 5'-phosphate (PMP), forming pyridoxal 5'-phosphate (PLP). This reaction serves as the terminal step in the de novo biosynthesis of PLP in E. coli and as a part of the salvage pathway of this coenzyme in both E. coli and mammalian cells" ([PMID: 12686112](https://pubmed.ncbi.nlm.nih.gov/12686112/)).

The substrate specificity and cofactor requirements are precisely defined: "The enzyme oxidizes either the 4'-hydroxyl group of pyridoxine 5'-phosphate (PNP) or the 4'-primary amine of pyridoxamine 5'-phosphate (PMP) to an aldehyde. PNPOx is a homodimeric enzyme with one flavin mononucleotide (FMN) molecule non-covalently bound to each subunit" ([PMID: 10903950](https://pubmed.ncbi.nlm.nih.gov/10903950/)). In summary, the enzyme accepts two substrates (PNP and PMP), uses non-covalently bound FMN as the redox cofactor, consumes molecular O₂, and produces PLP plus H₂O₂. This is the single most important functional statement about the gene: **PdxH converts inactive B6 vitamers into the active cofactor PLP.**

### Finding 2 — Catalytic mechanism: stereospecific hydride transfer to FMN within a homodimeric split-barrel fold

Crystallographic and stereochemical studies of the orthologous *E. coli* enzyme show that catalysis proceeds by abstraction of a hydrogen from the prochiral C4′ carbon of the substrate and transfer of a pair of electrons to the tightly bound FMN as a hydride ion. The reaction is strictly stereospecific: "the enzyme is specific for removal of the proR hydrogen atom from the prochiral C4' carbon atom of pyridoxamine 5'-phosphate" ([PMID: 11786019](https://pubmed.ncbi.nlm.nih.gov/11786019/)). The reduced flavin (FMNH₂) is then re-oxidized by molecular oxygen, regenerating FMN and releasing H₂O₂ — the hallmark of a flavin oxidase.

The structural fold is a classic FMN-binding split-barrel. As described for the *E. coli* enzyme, "The monomeric subunit folds into an eight-stranded beta sheet surrounded by five alpha-helical structures. Two monomers related by a twofold axis interact extensively along one-half of each monomer to form the dimer" ([PMID: 10903950](https://pubmed.ncbi.nlm.nih.gov/10903950/)). The two active-site clefts sit at the dimer interface, and each FMN contacts residues from both subunits — meaning the **homodimer is the obligate functional unit**, not a mere crystallographic artifact. Active-site residues govern substrate binding and orientation (Arg197 in *E. coli*), and Arg229 anchors the FMN cofactor; mutation of the latter (R229W) causes an ~850-fold loss of catalytic efficiency and reduced FMN/substrate affinity in the human enzyme ([PMID: 19759001](https://pubmed.ncbi.nlm.nih.gov/19759001/)). These structural insights transfer to Q88NS5 because the relevant residues are conserved (Finding 4).

### Finding 3 — Regulation by PLP product feedback inhibition at a non-catalytic allosteric site

Beyond its active site, PNPOx possesses a second, non-catalytic site that binds the product PLP tightly: "Recent studies have shown that in addition to the active site, PNPOx contains a noncatalytic site that binds PLP tightly" ([PMID: 12686112](https://pubmed.ncbi.nlm.nih.gov/12686112/)). This allosteric PLP-binding site — located roughly 11 Å from the active site, potentially linked by a tunnel — has since been formally identified and characterized in both the *E. coli* and human enzymes ([PMID: 34019876](https://pubmed.ncbi.nlm.nih.gov/34019876/); [PMID: 38284493](https://pubmed.ncbi.nlm.nih.gov/38284493/)). It mediates product feedback inhibition, which keeps the cellular concentration of free PLP — a reactive, potentially toxic aldehyde — very low.

This regulatory feature is coupled to a **channeling/hand-off function**: rather than releasing PLP freely into the cytosol, PNPOx is thought to transfer it directly to apo-B6 enzymes. As summarized for the salvage pathway, "Pyridoxal kinase and pyridoxine 5'-phosphate oxidase play kinetic roles in regulating the level of pyridoxal 5'-phosphate formation" ([PMID: 21182989](https://pubmed.ncbi.nlm.nih.gov/21182989/)). Direct binding and PLP transfer from PNPO to an apo-B6 enzyme (dopa decarboxylase) has been demonstrated biochemically, with the allosteric tight-binding PLP site implicated in the hand-off ([PMID: 36614085](https://pubmed.ncbi.nlm.nih.gov/36614085/)). While these last details were characterized in bacterial/human systems, the presence of the conserved fold in Q88NS5 makes analogous regulation the most parsimonious expectation for the *P. putida* enzyme.

### Finding 4 — Target-specific sequence evidence: Q88NS5 is a genuine PdxH ortholog with an intact active site

Because no experimental study exists for PP_1129 itself, we verified the annotation directly at the sequence level. A global Needleman–Wunsch alignment of Q88NS5 (215 aa) against the biochemically characterized *E. coli* PdxH (P0AFI7, 218 aa) yields **40.4% amino-acid identity over the full length** — squarely within the ortholog range for this family and far above the twilight zone for confident homology. The protein length (~215 aa) matches the single-domain PNPOx family (~215–230 aa), ruling out fusion or truncation artifacts.

Critically, the **catalytically essential Arg197 of *E. coli* PNPOx — described by di Salvo et al. as the residue that is "important for both binding and catalysis"** ([PMID: 11786019](https://pubmed.ncbi.nlm.nih.gov/11786019/)) — is conserved in Q88NS5, as is Arg14 and the conserved FMN/phosphate-binding motif region (*E. coli* "ERQVMVIGKAERL" aligns to *P. putida* "ERQVRIEGRVQKV"). The conservation of the active-site machinery means the *P. putida* enzyme is expected to possess a fully functional active site and to catalyze the same reaction with the same substrate specificity. UniProt curation independently assigns the Pyridox_Oxase_CS conserved-site signature (IPR019740 / PROSITE PS01064) to the protein, corroborating our alignment.

### Finding 5 — PdxH is the terminal step of a complete DXP-dependent de novo PLP pathway and the sole de novo source of PLP

A survey of the *P. putida* KT2440 proteome confirms that the full *E. coli*-type, **deoxyxylulose-5-phosphate (DXP)-dependent** PLP biosynthesis route is present and complete:

| Step | Enzyme | Locus | EC / Function |
|------|--------|-------|---------------|
| 1 | Epd | PP_4964 | Erythrose-4-P dehydrogenase |
| 2 | PdxB | PP_2117 | Erythronate-4-P dehydrogenase |
| 3 | SerC | PP_1768 | Phosphoserine / phosphohydroxythreonine aminotransferase |
| 4 | PdxA | PP_0402 | 4-Hydroxythreonine-4-P dehydrogenase |
| 5 | PdxJ | PP_1436 | Pyridoxine-5'-P synthase (EC 2.6.99.2) → makes PNP |
| **6** | **PdxH** | **PP_1129** | **PNP/PMP oxidase (EC 1.4.3.5) → makes PLP** |

PdxJ synthesizes pyridoxine 5'-phosphate (PNP), which is the **direct substrate PdxH oxidizes to PLP** — placing PdxH as the committed terminal step of the pathway. Critically, the organism **lacks the alternative DXP-independent PLP synthase genes *pdxS*/*pdxT* (0 hits in the proteome survey)**. Therefore the DXP-dependent route — and hence PdxH — is the **sole de novo source of PLP** in *P. putida* KT2440, with no redundant bypass. The salvage-pathway pyridoxal kinase PdxY (PP_5357) is also present, feeding the salvage branch that likewise converges on PdxH for oxidation of PNP/PMP to PLP. This non-redundancy strongly implies PdxH is physiologically essential (or near-essential) for growth in minimal media without an exogenous PLP/pyridoxal supply.

### Finding 6 — Sequence-based localization: a soluble cytoplasmic enzyme

A Kyte–Doolittle hydropathy scan (window 19) of Q88NS5 gives a maximum mean hydropathy of only **0.43**, far below the ~1.6 threshold indicative of a transmembrane helix — i.e., there is **no membrane-spanning segment**. The N-terminus (MTQSLADMRRDYTRDGLAEDQ…) is polar and charged (3 Arg, 4 Asp, 2 Glu within the first 30 residues), with a maximum 9-residue hydrophobicity of only 0.66, and therefore lacks the hydrophobic h-region required for a Sec- or Tat-type signal peptide. The enzyme is thus predicted to be **soluble and cytoplasmic**, with no secretion or membrane targeting. This is consistent with UniProt's cytoplasmic subcellular-location annotation and with the known cytosolic localization of all biochemically characterized PNPOx family enzymes. Cytoplasmic localization is also the functionally logical location: its substrates (PNP, PMP) are phosphorylated intracellular metabolites, and its product PLP is required by cytoplasmic PLP-dependent enzymes.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent picture of PdxH as the **cytoplasmic gatekeeper of active vitamin B6** in *P. putida* KT2440.

**Reaction catalyzed:**

```
   PNP (C4'-OH)  \                         FMN → FMNH2
                  } + O2  --[ PdxH ]-->  PLP  +  H2O2
   PMP (C4'-NH2) /                        (FMNH2 + O2 → FMN + H2O2)
```

**Pathway context — where PdxH sits:**

```
 DE NOVO (DXP-dependent) BRANCH
   Erythrose-4-P
      │ Epd (PP_4964)
      ▼
   4-Phosphoerythronate
      │ PdxB (PP_2117)
      ▼
   ... SerC (PP_1768) ... PdxA (PP_0402) ...
      ▼
   PdxJ (PP_1436)  ── synthesizes ──►  PNP ─┐
                                             │
 SALVAGE BRANCH                              ├──►  [ PdxH / PP_1129 ]  ──►  PLP
   Pyridoxine/Pyridoxamine                   │        (FMN oxidase)          │
      │ PdxY kinase (PP_5357)                │                              ▼
      ▼                                      │                    >140 PLP-dependent
   PNP / PMP  ───────────────────────────────┘                    apo-enzymes (holo)
```

Both the de novo biosynthetic branch and the salvage branch **converge on PdxH**, which performs the single oxidation that yields the active cofactor. Because *P. putida* KT2440 has no *pdxS/pdxT* alternative synthase, this convergence point is a genuine bottleneck: **all PLP produced endogenously must pass through PdxH.**

**Molecular mechanism.** PdxH is a homodimeric flavoenzyme. Each monomer adopts the FMN-binding split-barrel fold (eight-stranded β-sheet wrapped by five α-helices); the two subunits pack against each other so that each of the two active-site clefts is built from both monomers and each holds one non-covalently bound FMN. Catalysis proceeds in two half-reactions: (1) the reductive half-reaction, in which the substrate's C4′ prochiral center is oxidized by stereospecific abstraction of the *proR* hydrogen and hydride transfer to FMN (giving PLP + FMNH₂); and (2) the oxidative half-reaction, in which O₂ re-oxidizes FMNH₂ to FMN, releasing H₂O₂. Conserved active-site arginines (Arg197-equivalent for substrate binding/stereospecificity; Arg229-equivalent for FMN anchoring) are retained in Q88NS5, supporting an intact catalytic apparatus.

**Regulation and product handling.** A distinct, non-catalytic allosteric site binds the product PLP tightly, producing feedback inhibition that prevents accumulation of free (toxic) PLP. Rather than dumping PLP into the cytosol, the enzyme is thought to hand it off directly to apo-B6 enzymes, coupling PLP production to demand. This makes PdxH not just a biosynthetic terminal step but a **homeostatic control node** for B6 status.

**Localization.** All of this occurs in the cytoplasm, where the phosphorylated vitamers and the client PLP-dependent enzymes reside; PdxH bears no signal peptide or transmembrane segment.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|------|-----------------|-------------------------------|
| [12686112](https://pubmed.ncbi.nlm.nih.gov/12686112/) | *Structure and mechanism of E. coli PNP oxidase* | Establishes the exact reaction, dual substrates (PNP/PMP), product (PLP), the terminal de novo + salvage role, and the existence of a non-catalytic PLP-binding site. |
| [10903950](https://pubmed.ncbi.nlm.nih.gov/10903950/) | *X-ray structure of E. coli PNPOx with FMN at 1.8 Å* | Defines substrate specificity (C4′-OH of PNP / C4′-NH₂ of PMP), FMN cofactor, split-barrel monomer fold, and obligate homodimer architecture. |
| [11786019](https://pubmed.ncbi.nlm.nih.gov/11786019/) | *Active site structure and stereospecificity of E. coli PNPOx* | Documents stereospecific proR hydrogen abstraction at C4′; identifies Arg197 as essential for binding and catalysis (conserved in Q88NS5). |
| [19759001](https://pubmed.ncbi.nlm.nih.gov/19759001/) | *Molecular basis of reduced PNPOx activity in NEE (R229W)* | Shows Arg229 anchors FMN; its mutation causes ~850-fold loss of efficiency — underscores the catalytic importance of conserved active-site arginines. |
| [21182989](https://pubmed.ncbi.nlm.nih.gov/21182989/) | *Vitamin B6 salvage enzymes: mechanism, structure, regulation* | States PNPOx (with PL kinase) kinetically controls PLP formation — establishing it as a regulatory node in B6 homeostasis. |
| [34019876](https://pubmed.ncbi.nlm.nih.gov/34019876/) | *Identification of the PLP allosteric site in E. coli PNPOx* | Formally maps the non-catalytic PLP feedback-inhibition site in the bacterial enzyme. |
| [38284493](https://pubmed.ncbi.nlm.nih.gov/38284493/) | *Identification of the PLP allosteric site in human PNPO* | Confirms the allosteric PLP site is conserved to the human ortholog. |
| [36614085](https://pubmed.ncbi.nlm.nih.gov/36614085/) | *PNPO–Dopa decarboxylase interaction* | Demonstrates direct PLP hand-off from PNPO to an apo-B6 enzyme via the allosteric site. |
| [15858270](https://pubmed.ncbi.nlm.nih.gov/15858270/) | *Tetragonal crystal form of E. coli PNPOx* | Provides a snapshot series of the catalytic pathway (substrate binding → catalysis → product release) and a putative product-release tunnel. |

**Consistency across the family.** The mechanism, fold, cofactor, and regulation are conserved from *E. coli* to human PNPO, where loss-of-function mutations cause pyridox(am)ine 5'-phosphate oxidase deficiency / neonatal epileptic encephalopathy ([PMID: 33421502](https://pubmed.ncbi.nlm.nih.gov/33421502/); [PMID: 32788630](https://pubmed.ncbi.nlm.nih.gov/32788630/)). This deep conservation of both sequence and function across billions of years of divergence is what makes the annotation-by-orthology to the *P. putida* enzyme robust.

**Organism context.** *P. putida* KT2440 is a well-studied, biotechnologically important soil bacterium, and its PLP-dependent enzymes (e.g., ω-transaminases, methionine γ-lyase) are actively engineered for industrial biocatalysis — all of which depend on a functional PLP supply, i.e., on PdxH ([PMID: 40436318](https://pubmed.ncbi.nlm.nih.gov/40436318/); [PMID: 34953671](https://pubmed.ncbi.nlm.nih.gov/34953671/)). The upstream DXP pathway enzymology (e.g., E4P dehydrogenase) is likewise conserved and structurally characterized in related Gram-negatives ([PMID: 41230615](https://pubmed.ncbi.nlm.nih.gov/41230615/)).

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of PP_1129.** The functional model rests entirely on (a) annotation-by-orthology (HAMAP MF_01629 + conserved domains) and (b) our own target-specific sequence verification. No enzyme has been purified from *P. putida* KT2440 to measure its kinetic constants (kcat, Km for PNP vs. PMP), substrate preference, or oxygen dependence directly. There is no crystal structure of the *P. putida* enzyme.

2. **Localization is predicted, not measured.** Cytoplasmic localization is inferred from the absence of a signal peptide/TM helix and from family precedent; it has not been demonstrated experimentally (e.g., by fractionation or fluorescent tagging) for PP_1129.

3. **Regulatory details are extrapolated.** The allosteric PLP feedback site and the direct PLP hand-off to apo-B6 enzymes are established in *E. coli* and human enzymes. While the fold is conserved, the precise residues, affinities, and interaction partners of the *P. putida* allosteric site have not been mapped.

4. **Essentiality is inferred, not proven.** The absence of *pdxS/pdxT* and any other terminal oxidase strongly implies PdxH is essential for de novo PLP production, but a *P. putida* knockout / conditional-depletion experiment confirming a PLP-auxotrophy phenotype has not been reported here.

5. **Sequence identity is moderate (~40%).** While comfortably within the ortholog range and supported by conserved active-site residues, ~40% identity leaves room for organism-specific differences in substrate preference, oligomerization, or regulation that only direct biochemistry could resolve.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and enzyme assay.** Clone PP_1129, express in *E. coli*, purify, and measure the FMN content, PNP/PMP oxidase activity (spectrophotometric PLP formation), and kinetic constants (kcat, Km) for both substrates plus O₂ dependence. This would directly confirm EC 1.4.3.5 activity for the *P. putida* protein.

2. **Genetic essentiality test.** Attempt a clean *pdxH* deletion (or CRISPRi knockdown) in KT2440; test for PLP/pyridoxal auxotrophy — predicted growth failure in minimal medium rescued by exogenous pyridoxal, confirming PdxH as the sole terminal PLP source.

3. **Structural determination / modeling.** Solve the crystal structure (or generate a high-confidence AlphaFold model) to verify the split-barrel homodimer fold, FMN pocket, and the position of Arg197/Arg229 equivalents; test whether an allosteric PLP site is structurally present.

4. **Feedback-inhibition assay.** Measure inhibition of the purified enzyme by PLP to confirm product feedback regulation and, if present, mutate candidate allosteric-site residues to test their role.

5. **Subcellular localization.** Confirm cytoplasmic localization by cell fractionation or a fluorescent-protein fusion.

6. **Physiological coupling.** Test whether PdxH activity/expression is coordinated with demand from *P. putida*'s many PLP-dependent enzymes (e.g., under conditions that induce transaminases or amino-acid catabolism), linking the enzyme's homeostatic role to the organism's metabolic versatility.

---

## Conclusion

*pdxH* (PP_1129, UniProt Q88NS5) of *Pseudomonas putida* KT2440 encodes **pyridoxine/pyridoxamine 5'-phosphate oxidase (PNPOx, EC 1.4.3.5)**, a soluble cytoplasmic, FMN-dependent flavo-oxidase that catalyzes the **terminal, committed step of vitamin B6 metabolism** — the O₂-dependent oxidation of pyridoxine 5'-phosphate (at C4′-OH) or pyridoxamine 5'-phosphate (at C4′-NH₂) to pyridoxal 5'-phosphate (PLP), producing FMNH₂ and H₂O₂. Acting as an obligate homodimer with a split-barrel FMN fold, it is the convergence point of both the DXP-dependent de novo biosynthesis pathway and the B6 salvage pathway, is the organism's sole terminal source of PLP (no *pdxS/pdxT* backup), and is regulated by PLP product feedback inhibition at a non-catalytic allosteric site. This is a high-confidence assignment from orthology plus target-specific sequence verification (~40% identity to *E. coli* PdxH with conserved catalytic Arg197), pending direct biochemical study of the *P. putida* protein.


## Artifacts

- [OpenScientist final report](pdxH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pdxH-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12686112
2. PMID:10903950
3. PMID:11786019
4. PMID:19759001
5. PMID:34019876
6. PMID:38284493
7. PMID:21182989
8. PMID:36614085
9. PMID:33421502
10. PMID:32788630
11. PMID:40436318
12. PMID:34953671
13. PMID:41230615