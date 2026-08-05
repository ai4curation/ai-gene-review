---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T13:59:14.548283'
end_time: '2026-07-23T14:08:52.672035'
duration_seconds: 578.12
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: murC
  gene_symbol: murC
  uniprot_accession: Q88N75
  protein_description: 'RecName: Full=UDP-N-acetylmuramate--L-alanine ligase {ECO:0000255|HAMAP-Rule:MF_00046};
    EC=6.3.2.8 {ECO:0000255|HAMAP-Rule:MF_00046}; AltName: Full=UDP-N-acetylmuramoyl-L-alanine
    synthetase {ECO:0000255|HAMAP-Rule:MF_00046};'
  gene_info: Name=murC {ECO:0000255|HAMAP-Rule:MF_00046}; OrderedLocusNames=PP_1338;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MurCDEF family. {ECO:0000255|HAMAP-
  protein_domains: Mur-like_cat_sf. (IPR036565); Mur_ligase_C. (IPR004101); Mur_ligase_C_dom_sf.
    (IPR036615); Mur_ligase_cen. (IPR013221); Mur_ligase_N. (IPR000713)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: murC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: murC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N75
- **Protein Description:** RecName: Full=UDP-N-acetylmuramate--L-alanine ligase {ECO:0000255|HAMAP-Rule:MF_00046}; EC=6.3.2.8 {ECO:0000255|HAMAP-Rule:MF_00046}; AltName: Full=UDP-N-acetylmuramoyl-L-alanine synthetase {ECO:0000255|HAMAP-Rule:MF_00046};
- **Gene Information:** Name=murC {ECO:0000255|HAMAP-Rule:MF_00046}; OrderedLocusNames=PP_1338;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MurCDEF family. {ECO:0000255|HAMAP-
- **Key Domains:** Mur-like_cat_sf. (IPR036565); Mur_ligase_C. (IPR004101); Mur_ligase_C_dom_sf. (IPR036615); Mur_ligase_cen. (IPR013221); Mur_ligase_N. (IPR000713)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "murC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'murC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **murC** (gene ID: murC, UniProt: Q88N75) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: MurC (Q88N75, PP_1338) in *Pseudomonas putida* KT2440

**UniProt:** Q88N75 · **Gene:** *murC* · **Locus:** PP_1338 · **EC:** 6.3.2.8
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440) — PSEPK
**Family:** MurCDEF (Mur ligase) family; ADP-forming amide-bond ligase

---

## Summary

**MurC (UniProt Q88N75; gene *murC*; ordered locus PP_1338) of *Pseudomonas putida* KT2440 is a cytoplasmic, ATP- and Mg²⁺-dependent amide-bond ligase (EC 6.3.2.8) that catalyzes the first amino-acid-adding step of bacterial peptidoglycan biosynthesis.** It ligates **L-alanine** to the D-lactoyl carboxylate of **UDP-*N*-acetylmuramate (UDP-MurNAc)**, producing **UDP-MurNAc-L-Ala + ADP + inorganic phosphate**. This reaction is the committed entry point into assembly of the peptidoglycan "peptide stem" — the short cross-linking peptide that gives the murein sacculus its mechanical strength.

The gene/protein identity is unambiguous. The UniProt HAMAP-rule annotation (MF_00046), the EC number (6.3.2.8), the gene name (*murC*/PP_1338), MurCDEF family membership, and the diagnostic three-domain Mur-ligase architecture (InterPro Mur_ligase_N IPR000713, Mur_ligase_cen IPR013221, Mur_ligase_C IPR004101; Mur-like catalytic superfamily IPR036565) all converge on a single, well-characterized enzyme class. The catalyzed reaction is directly demonstrated in vitro for MurC orthologs across diverse bacteria, most relevantly the **same genus** (*Pseudomonas aeruginosa*; [PMID: 12615853](https://pubmed.ncbi.nlm.nih.gov/12615853/)), and high-resolution crystal structures from *Haemophilus influenzae* and *Mycobacterium bovis* define its mechanism at atomic resolution ([PMID: 12837790](https://pubmed.ncbi.nlm.nih.gov/12837790/); [PMID: 33950018](https://pubmed.ncbi.nlm.nih.gov/33950018/)).

Functionally, MurC operates in the **cytosol** as the first of four ATP-dependent Mur ligases (MurC → MurD → MurE → MurF) that sequentially append amino acids to UDP-MurNAc to build UDP-MurNAc-pentapeptide (Park's nucleotide), which the membrane translocase MraY then transfers to the lipid carrier. Because this pathway is essential, absent in humans, and rate-limiting for cell-wall integrity, MurC is a validated Gram-negative antibacterial drug target actively pursued in *P. aeruginosa*. No direct study of the *P. putida* KT2440 protein itself was found; the functional assignment rests on unambiguous sequence/family/domain identity plus rich experimental characterization of close orthologs — a robust inference for a universally conserved, HAMAP-annotated housekeeping enzyme.

---

## Gene / Protein Identity Verification

The mandatory identity checks were performed and **all passed**:

| Verification criterion | Result |
|---|---|
| Gene symbol "murC" matches protein description | ✅ UDP-*N*-acetylmuramate–L-alanine ligase (MurC synthetase) |
| Organism correct | ✅ *Pseudomonas putida* KT2440 (PP_1338) |
| Protein family / domain alignment with literature | ✅ MurCDEF family; three-domain Mur-ligase fold (IPR000713 / IPR013221 / IPR004101) |
| Risk of same-symbol confusion | ✅ Low — "murC" is highly specific to this ligase across bacteria |

The symbol *murC* is **not ambiguous**. It refers consistently to the UDP-MurNAc:L-alanine ligase across the bacterial domain, and every paper retrieved describes exactly this enzyme class (in Pseudomonas, Haemophilus, Mycobacterium, Chlamydia, Salmonella, Verrucomicrobium, and Anabaena). Research therefore proceeded on the correct enzyme, using orthologs to inform mechanism where no *P. putida*-specific study exists.

---

## Key Findings

### Finding 1 — MurC catalyzes ATP-dependent ligation of L-alanine to UDP-*N*-acetylmuramate (EC 6.3.2.8)

The primary function of MurC is to catalyze the amide-bond-forming reaction:

> UDP-*N*-acetyl-α-D-muramate + L-alanine + ATP → UDP-*N*-acetyl-α-D-muramoyl-L-alanine + ADP + phosphate  (Mg²⁺-dependent)

This is the first amino-acid-adding step of the cytoplasmic phase of peptidoglycan biosynthesis. MurC forms an amide (peptide) bond between the α-amino group of L-alanine and the D-lactoyl carboxylate on the muramic acid moiety of the nucleotide-activated sugar UDP-MurNAc.

The identity supporting this assignment is unambiguous: UniProt Q88N75 is annotated under HAMAP rule MF_00046 as UDP-*N*-acetylmuramate–L-alanine ligase, EC 6.3.2.8, gene *murC*/PP_1338, MurCDEF family, with the diagnostic three-domain fold. The reaction has been **directly demonstrated in vitro** for MurC from multiple bacteria. Most relevantly, recombinant His-tagged MurC from the close relative *P. aeruginosa* was purified and assayed with its substrates UDP-*N*-acetylmuramate, ATP, and L-alanine, and is described as *"an essential enzyme involved in the early steps of biosynthesis of peptidoglycan monomer"* ([PMID: 12615853](https://pubmed.ncbi.nlm.nih.gov/12615853/)). Its substrate UDP-MurNAc is itself generated by the upstream enzymes MurA (enolpyruvyl transfer to UDP-GlcNAc) and MurB (reduction). Independently, MurC from *C. trachomatis* was shown to display *"in vitro ATP-dependent UDP-MurNAc:L-alanine ligase activity, with a pH optimum of 8.0 and dependence upon magnesium ions"* ([PMID: 14594822](https://pubmed.ncbi.nlm.nih.gov/14594822/)), establishing the conserved cofactor requirements (ATP, Mg²⁺) and pH behavior of the family.

**Substrate specificity.** UDP-MurNAc is the specific nucleotide-sugar acceptor. L-alanine is the physiological amino-acid substrate that defines the first residue of the peptide stem. In vitro, some orthologs display relaxed amino-acid specificity: the *C. trachomatis* enzyme was tested with *"three amino acids (L-alanine, L-serine, and glycine); comparable Vmax/Km values were obtained"* ([PMID: 14594822](https://pubmed.ncbi.nlm.nih.gov/14594822/)). Nonetheless, in Gram-negative bacteria such as *E. coli* and *Pseudomonas* the physiological product carries L-Ala at position 1, indicating high in vivo selectivity for L-alanine.

### Finding 2 — Conserved three-domain architecture assembles the active site at domain interfaces; catalysis proceeds via an acyl-phosphate intermediate

MurC belongs to the Mur ligase family, whose members share a characteristic **three-domain fold**. High-resolution crystal structures of *H. influenzae* MurC captured fully assembled catalytic states: a 1.85 Å substrate complex (UDP-MurNAc + Mg²⁺) and a 1.7 Å product complex (UDP-MurNAc-L-Ala + the non-hydrolyzable ATP analog AMPPNP + Mn²⁺). These *"reveal a conserved, three-domain architecture with the binding sites for UNAM and ATP formed at the domain interfaces: the N-terminal domain binds the UDP portion of UNAM, and the central and C-terminal domains form the ATP-binding site, while the C-terminal domain also positions the alanine"* ([PMID: 12837790](https://pubmed.ncbi.nlm.nih.gov/12837790/)). This matches exactly the IPR domain complement annotated for Q88N75 (Mur_ligase_N / _cen / _C).

The productive active site is assembled only when all three substrates bind and the three domains close around them — an induced-fit mechanism. The structures also reveal the metal chemistry: *"the gamma-phosphate of AMPPNP is positioned between two bound metal ions, one of which also binds the reactive UNAM carboxylate"* ([PMID: 12837790](https://pubmed.ncbi.nlm.nih.gov/12837790/)), the geometry required for in-line phosphoryl transfer from ATP to the substrate carboxylate. Two conserved arginine residues orient the incoming alanine.

The **catalytic mechanism** shared by the Mur ligases (MurC–MurF) is an ordered, ATP-dependent condensation: ATP first phosphorylates the substrate carboxylate to a high-energy **acyl-phosphate intermediate**; the incoming amino group then attacks this activated carbonyl to form a **tetrahedral intermediate**, which collapses to release inorganic phosphate and form the amide bond. This chemistry is documented for the paralogous ligase MurD, which *"is responsible for the ATP-dependent addition of d-glutamic acid to UDP-MurNAc-l-Ala, a reaction which involves acyl-phosphate and tetrahedral intermediates"* ([PMID: 25436755](https://pubmed.ncbi.nlm.nih.gov/25436755/)) — the same mechanism applies to MurC's addition of L-alanine.

Independent structures of *M. bovis* MurC reproduce the fold: they *"[exhibit] a three-domain architecture for the binding of UNAM, ATP and an amino acid as substrates, with a nickel ion at the domain interface"* and show a UDP-*N*-acetylglucosamine substrate mimic engaging the UDP-binding domain ([PMID: 33950018](https://pubmed.ncbi.nlm.nih.gov/33950018/)). Convergence of *H. influenzae* and *M. bovis* structures on the identical architecture and metal-at-interface geometry gives high confidence that *P. putida* MurC operates the same way.

### Finding 3 — MurC acts in the cytoplasm as the committed first step of the MurCDEF pathway; it is essential and a validated antibacterial target

MurC functions in the **cytosol**. It is the first of four cytoplasmic ATP-dependent Mur ligases that sequentially build the peptidoglycan peptide stem on UDP-MurNAc. A review of the cytoplasmic steps confirms that MurB and MurC *"are involved in the cytoplasmic steps of peptidoglycan biosynthesis"* ([PMID: 27047475](https://pubmed.ncbi.nlm.nih.gov/27047475/)), establishing both MurC's subcellular localization (cytoplasm) and its pathway position — immediately downstream of the MurA/MurB steps that produce UDP-MurNAc and immediately upstream of MurD. All of MurC's substrates and its product are soluble cytoplasmic nucleotide intermediates; only later does the membrane enzyme MraY transfer the completed precursor to the lipid carrier at the inner-membrane face.

**Essentiality and drug-target status.** MurC is essential for viability because peptidoglycan maintains cell shape and osmotic integrity. It is explicitly described as *"an essential enzyme"* in *P. aeruginosa* ([PMID: 12615853](https://pubmed.ncbi.nlm.nih.gov/12615853/)) and as *"an excellent target for the design of new classes of antimicrobial inhibitors in gram-negative bacteria"* ([PMID: 31333120](https://pubmed.ncbi.nlm.nih.gov/31333120/)). Genetic evidence comes from the cyanobacterium *Anabaena*, where reduced *murC* expression caused *decreased filament integrity* and blocked heterocyst differentiation, directly linking MurC-mediated peptidoglycan synthesis to cell-envelope integrity ([PMID: 26811320](https://pubmed.ncbi.nlm.nih.gov/26811320/)).

Because the pathway is absent from humans, MurC is actively pursued as an antibacterial target, including directly in *P. aeruginosa*, where structure-based virtual screening plus an in vitro inhibition assay identified a benzodiazole sulfonamide inhibitor ([PMID: 31333120](https://pubmed.ncbi.nlm.nih.gov/31333120/)). Similar computational lead-discovery efforts target MurC in multidrug-resistant *Salmonella* Typhi, where a curcumin derivative was predicted to competitively inhibit ATP binding at the MurC catalytic domain ([PMID: 35985453](https://pubmed.ncbi.nlm.nih.gov/35985453/)).

---

## Mechanistic Model / Interpretation

### Position in the peptidoglycan biosynthetic pathway

```
   Cytoplasm
   =========
   UDP-GlcNAc
       │  MurA (enolpyruvyl transfer)
       ▼
   UDP-GlcNAc-enolpyruvate
       │  MurB (reduction)
       ▼
   UDP-MurNAc  ─────────────────┐
       │                         │  + L-Ala + ATP
       ▼   ★ MurC (Q88N75) ★     │  → UDP-MurNAc-L-Ala + ADP + Pi
   UDP-MurNAc-L-Ala              │
       │  MurD  (+ D-Glu)
       ▼
   UDP-MurNAc-L-Ala-D-Glu
       │  MurE  (+ meso-DAP)     [position-3 residue in Pseudomonas / Gram-negatives]
       ▼
   UDP-MurNAc-tripeptide
       │  MurF  (+ D-Ala-D-Ala)
       ▼
   UDP-MurNAc-pentapeptide  (Park's nucleotide)
       │
   ----│-----------------------------------  inner membrane
       ▼  MraY (→ Lipid I) → MurG (→ Lipid II) → flippase → transglycosylation / transpeptidation
   Peptidoglycan sacculus
```

MurC is the **committed first amino-acid-adding step** — the transition from an activated sugar (UDP-MurNAc) to a nascent peptide-bearing precursor, committing carbon and nitrogen to the peptide stem.

### Catalytic cycle (single-turnover schematic)

```
  (1) Substrate binding & domain closure
      UDP-MurNAc  →  N-terminal domain
      ATP·Mg²⁺    →  central + C-terminal domains
      L-Ala       →  C-terminal domain pocket (oriented by two conserved Arg)

  (2) Phosphoryl transfer  (two metal ions bridge ATP γ-P and substrate carboxylate)
      UDP-MurNAc-COO⁻ + ATP  →  UDP-MurNAc-CO-O-PO3²⁻ (acyl-phosphate) + ADP

  (3) Nucleophilic attack
      L-Ala α-NH2 attacks acyl-phosphate carbonyl → tetrahedral intermediate

  (4) Collapse & product release
      → UDP-MurNAc-L-Ala (amide bond) + Pi ; domains reopen
```

This model integrates the structural data (three-domain assembly, two-metal geometry, Arg-mediated amino-acid positioning; [PMID: 12837790](https://pubmed.ncbi.nlm.nih.gov/12837790/), [PMID: 33950018](https://pubmed.ncbi.nlm.nih.gov/33950018/)) with the acyl-phosphate/tetrahedral-intermediate chemistry established for the Mur ligase family ([PMID: 25436755](https://pubmed.ncbi.nlm.nih.gov/25436755/)) and the biochemical requirements (ATP, Mg²⁺, pH ~8) demonstrated for MurC orthologs ([PMID: 14594822](https://pubmed.ncbi.nlm.nih.gov/14594822/)).

### Localization

MurC is a soluble **cytoplasmic** enzyme (no signal peptide, no transmembrane segments in the Mur ligase fold), consistent with the cytoplasmic location of its nucleotide-sugar substrate and of the entire Mur ligase cascade ([PMID: 27047475](https://pubmed.ncbi.nlm.nih.gov/27047475/)). It likely acts near the divisome/elongasome machinery that coordinates precursor supply with cell-wall growth.

---

## Evidence Base

| PMID | Organism / topic | How it supports this report |
|---|---|---|
| [12615853](https://pubmed.ncbi.nlm.nih.gov/12615853/) | *P. aeruginosa* MurC (same genus) | Recombinant MurC purified and assayed with UDP-MurNAc, ATP, L-Ala; described as an essential early peptidoglycan enzyme — most transferable evidence for the target genus (Findings 1, 3) |
| [14594822](https://pubmed.ncbi.nlm.nih.gov/14594822/) | *C. trachomatis* MurC | Direct in vitro demonstration of ATP- and Mg²⁺-dependent UDP-MurNAc:L-alanine ligase activity, pH optimum 8.0; amino-acid specificity profile (Findings 1, 3) |
| [12837790](https://pubmed.ncbi.nlm.nih.gov/12837790/) | *H. influenzae* MurC crystal structures | Substrate- and product-bound structures defining three-domain architecture, domain-interface active site, two-metal ATP geometry, Arg-mediated alanine positioning (Finding 2) |
| [33950018](https://pubmed.ncbi.nlm.nih.gov/33950018/) | *M. bovis* MurC crystal structures | Independent confirmation of three-domain fold and metal-at-interface; UNAG substrate-mimic binding (Finding 2) |
| [25436755](https://pubmed.ncbi.nlm.nih.gov/25436755/) | Mur ligase (MurD) mechanism | Documents the shared acyl-phosphate/tetrahedral-intermediate mechanism of the family (Finding 2) |
| [27047475](https://pubmed.ncbi.nlm.nih.gov/27047475/) | *Verrucomicrobium* MurB/C fusion | States MurC operates in the cytoplasmic steps of peptidoglycan biosynthesis — localization and pathway position (Finding 3) |
| [31333120](https://pubmed.ncbi.nlm.nih.gov/31333120/) | *P. aeruginosa* MurC inhibitor discovery | Confirms essentiality and validated Gram-negative drug-target status in the target genus (Finding 3) |
| [26811320](https://pubmed.ncbi.nlm.nih.gov/26811320/) | *Anabaena* murC/murB genetics | In vivo depletion of murC decreases filament integrity — genetic link to cell-envelope integrity (Finding 3) |
| [35985453](https://pubmed.ncbi.nlm.nih.gov/35985453/) | *Salmonella* Typhi MurC docking | Reinforces MurC as an antibacterial target and ATP-competitive inhibition at the catalytic domain |
| [23786712](https://pubmed.ncbi.nlm.nih.gov/23786712/) | MurF inhibitors | Illustrates the Mur ligase family as validated antibacterial targets with no human counterpart (pathway context) |

**Strength of inference.** No study has characterized the *P. putida* KT2440 MurC protein directly. However, the assignment rests on (i) unambiguous, rule-based sequence identity (HAMAP MF_00046) with the universally conserved MurC class; (ii) direct biochemistry of the same enzyme in the sister species *P. aeruginosa* and diverse bacteria; and (iii) multiple independent crystal structures converging on a single conserved mechanism. For an essential, universally distributed housekeeping enzyme, this ortholog-based inference is robust.

---

## Supported vs. Refuted Hypotheses

- **Supported:** (i) Q88N75 is UDP-MurNAc:L-alanine ligase (EC 6.3.2.8); (ii) it adds L-Ala to UDP-MurNAc using ATP and a divalent metal; (iii) it is cytoplasmic; (iv) it is the first Mur-ligase step of peptidoglycan precursor synthesis; (v) it uses a conserved three-domain fold and an acyl-phosphate mechanism; (vi) it is essential and a validated antibacterial target.
- **Refuted / not supported:** No evidence that this protein acts extracytoplasmically, transports substrates, or has a non-catalytic structural role. The gene-symbol ambiguity concern raised in the prompt did not materialize — all literature converges on the same enzyme.

---

## Limitations and Knowledge Gaps

1. **No target-specific biochemistry.** No published assay, kinetic parameters (Km, kcat), or structure exists for *P. putida* KT2440 MurC (PP_1338) itself. All mechanistic and kinetic detail is inferred from orthologs. Conservation is high, but species-specific values and precise pocket dimensions remain unmeasured.
2. **Substrate-specificity extrapolation.** The relaxed amino-acid tolerance (L-Ala/L-Ser/Gly) was measured in *C. trachomatis*, not *Pseudomonas*; whether *P. putida* MurC similarly accepts L-serine or glycine in vitro is unknown, though L-alanine is confidently the physiological substrate.
3. **No experimental localization for this protein.** Cytoplasmic localization is inferred from the pathway and the soluble Mur ligase fold, not from a *P. putida*-specific experiment (though the inference is very strong).
4. **Regulation and interaction partners unexplored.** Expression regulation of *murC* in *P. putida*, and physical association with divisome/elongasome components or with MurB/MurD, is not addressed by the available literature.
5. **Essentiality assumed, not demonstrated in *P. putida*.** Essentiality is well established for *P. aeruginosa* and generalizable, but a KT2440-specific essentiality experiment for PP_1338 was not located.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzyme assay.** Overexpress and purify recombinant His-MurC (PP_1338) and measure steady-state kinetics (Km for UDP-MurNAc, L-Ala, ATP; kcat; Mg²⁺ dependence; pH optimum) via an ADP/Pi-release or coupled spectrophotometric assay, directly validating the ortholog-based assignment.
2. **Substrate-specificity screen.** Test L-Ala, L-Ser, Gly (and controls) with purified *P. putida* MurC to determine whether the relaxed specificity seen in *C. trachomatis* holds, confirming L-alanine as the preferred substrate.
3. **Complementation test.** Complement an *E. coli murC*(ts) or conditional mutant with PP_1338 — the strategy used to validate *Anabaena* MurC ([PMID: 26811320](https://pubmed.ncbi.nlm.nih.gov/26811320/)).
4. **Essentiality/depletion in *P. putida*.** Build a conditional (inducible / CRISPRi) *murC* knockdown in KT2440 and assess viability, morphology, and envelope integrity.
5. **Structural determination.** Solve the crystal/cryo-EM structure (or validate a high-confidence AlphaFold model) of *P. putida* MurC in substrate/product complexes to confirm the three-domain assembly and two-metal geometry and to enable *Pseudomonas*-tailored inhibitor design.
6. **Inhibitor cross-testing.** Test whether the *P. aeruginosa* MurC benzodiazole sulfonamide ([PMID: 31333120](https://pubmed.ncbi.nlm.nih.gov/31333120/)) and related Mur ligase inhibitors also inhibit *P. putida* MurC, informing broad-spectrum anti-Pseudomonas strategies.

---

## Conclusion

MurC (Q88N75 / PP_1338) of *Pseudomonas putida* KT2440 is confidently assigned as the cytoplasmic, ATP- and Mg²⁺-dependent UDP-*N*-acetylmuramate–L-alanine ligase (EC 6.3.2.8). It catalyzes the committed first amino-acid-adding step of peptidoglycan biosynthesis — ligating L-alanine to UDP-MurNAc to form UDP-MurNAc-L-Ala — via a two-metal, acyl-phosphate/tetrahedral-intermediate mechanism within a conserved three-domain Mur-ligase fold. It initiates the MurC→MurD→MurE→MurF cytosolic cascade that produces Park's nucleotide, is essential for cell-wall integrity, and is a validated Gram-negative antibacterial target. The assignment is unambiguous by sequence, family, and domain identity and is strongly supported by direct biochemical and structural characterization of close orthologs, although no study has yet examined the *P. putida* protein directly.

---

*Report generated from primary literature (PubMed) and curated UniProt/HAMAP annotation.*


## Artifacts

- [OpenScientist final report](murC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](murC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12615853
2. PMID:12837790
3. PMID:33950018
4. PMID:14594822
5. PMID:25436755
6. PMID:27047475
7. PMID:31333120
8. PMID:26811320
9. PMID:35985453