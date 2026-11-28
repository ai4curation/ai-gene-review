# ICY1 (Q04329) Foldseek fold assignment: hypothesis report

Hypothesis slug: `kgap-icy1-foldseek-fold-assignment`
Gene: *Saccharomyces cerevisiae* ICY1 / YMR195W, UniProt Q04329, 127 aa
Source: `genes/yeast/ICY1/ICY1-ai-review.yaml`, free-text focus

## Executive judgment

**Refuted.** The analysis the hypothesis asked for was run and it returns the opposite of the hypothesis: ICY1 has no confident structural homolog in PDB, CATH or the AlphaFold database, and no fold can be assigned. The strongest structural match anywhere is TM = 0.454 to an uncharacterized *Brugia pahangi* protein at 4.9% sequence identity; the best experimental-structure match is TM = 0.419 over 45% of the query. All fall below the TM = 0.5 same-fold threshold (PMID 20164152).

The mechanistic reason matters more than the hit list. The AlphaFold model of ICY1 has **zero** long-range CA-CA contacts (|i-j| >= 12, < 8 A). It is a single helix (residues 77-126) hanging off a 76-residue disordered N-terminus, with mean pLDDT 56.7 and mean predicted aligned error 27.7 A for long-range pairs against a 31 A ceiling. There is no tertiary structure to search with. A control search using only the ordered helix (77-127) returns **0 hits** in PDB100, CATH50 and AFDB/Swiss-Prot, which confirms the null is a property of the query and not of database coverage. InterPro returns 204 No Content for Q04329: no Pfam, SUPFAM, Gene3D, CDD or PANTHER signature.

Caveats. (1) AlphaFold models disordered regions poorly by construction, so the model's extended geometry is a disorder prediction, not an observed conformation; ICY1 could fold on binding a partner or a membrane. (2) Foldseek on a low-pLDDT monomer is near its sensitivity floor, so this is "no evidence of a fold", not "proof of no fold". (3) The search is monomeric; a coiled coil formed in a complex would not be recovered. None of these caveats rescue the hypothesis as written, because the hypothesis required a confidently assigned fold.

## Evidence matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| This work (Foldseek web server, run 2026-11-23; tickets `IwWdmVvNh2P-...`, `io6ItC9XriUNVYVDeDHYFPqLf5jeCoDlRXx_zw`) | Computational, structural | **Refutes** | ICY1 adopts a known fold | 3Di+AA mode: only hit with E < 1 is the self-hit (E = 2.0e-19); all others E = 4.9-9.5, prob 0.05-0.35. TM-align mode: PDB100 best TM 0.419 (8iyj doublet microtubule, 61 aln res, 45% coverage, 8.1% id); CATH50 best 0.399; AFDB/Swiss-Prot best non-self 0.418 (human TRAK2, 0.5% id); AFDB50 best non-self 0.454 | AF-Q04329-F1-model_v6 vs PDB100 20240101, CATH50 4.3.0, AFDB v6 | High for the null. Monomeric search only; low-pLDDT query limits sensitivity |
| This work (geometry from AF model + PAE v6) | Computational, structural | **Explains the null** | The model has a fold to search | 0 long-range contacts; Rg 33.4 A vs 13.9 A expected (ratio 2.41); one helix 77-126; mean pLDDT 56.7, 49.6% of residues < 50; mean PAE 24.5 A | AlphaFold DB v6 | High. Benchmarked against FKBP1A (2.09 LR contacts/res), lysozyme (1.19), collagen (0.41), tau (0.03), alpha-synuclein (0.00) |
| This work (control search) | Computational | **Refutes** | A fold is hidden by flanking disorder | Helix 77-127 alone: 0 hits in PDB100, CATH50, AFDB/Swiss-Prot | Same server | High. An isolated helix is not a fold |
| InterPro API (204 No Content for Q04329) | Database | **Qualifies** | Sequence-level domain assignment exists | No member-database signature matches ICY1 | InterPro, accessed 2026-11-23 | High. Database-level evidence, consistent with the structural null |
| PMID 20164152 (Xu & Zhang 2010) | Computational / methodological | **Qualifies** | TM = 0.5 as fold criterion | "protein pairs with a TM-score >0.5 are mostly in the same fold"; P = 5.5e-7 at TM 0.5 | 6684 non-homologous PDB domains | High. Threshold derived for single-domain globular proteins |
| PMID 37156916 (van Kempen et al. 2023) | Computational / methodological | Orientation | Method used | Foldseek sensitivity is 86-133% of Dali/TM-align/CE | Method paper | High |
| PMID 38124369 (Versini et al. 2024) | Review | **Qualifies** | pLDDT reads out disorder | "AF2's confidence score (pLDDT) serves as a competitive disorder predictor" | Review of AF2/RF applications | Review-level; widely replicated |
| PMID 26565778 (Yao et al. 2015) | Mutant phenotype + interaction | **Competing** | Function requires a fold | The ICY1 paralog Icy2 is Atg41: interacts with Atg9, required for autophagosome formation, Gcn4-induced. AF-Q12048 has the same disordered signature as ICY1 (0 long-range contacts, Rg ratio 2.39) | *S. cerevisiae*, autophagy assays | High for Atg41. Paralog, not ICY1 itself |
| PMID 14504216 (Dunn & Jensen 2003) | Mutant phenotype | **Qualifies** | ICY1 has a molecular function | ICY1 overexpression rescues mtDNA dependence of *tim18Δ*; *icy1Δ* cells cannot grow without mtDNA | *S. cerevisiae*, high-copy suppressor screen | Genetic, indirect. Does not specify a molecular activity |
| PMID 19001347 (Wiederhold et al. 2009) | Localization (proteomics) | Orientation | ICY1 is a vacuolar membrane protein | 148 proteins significantly enriched in pure vacuolar membrane preparations; source of the HDA-supported GO:0000329 annotation | Purified *S. cerevisiae* vacuoles | Medium. Subtractive proteomics; the paper itself notes non-vacuolar proteins co-enrich |
| PMID 14562106 (Ghaemmaghami et al. 2003) | Direct measurement | Orientation | Expression level | 4050 molecules/cell in log-phase SD; ICY1 is expressed, not a dubious ORF | *S. cerevisiae*, TAP-tag census | High for abundance only |

## GO curation implications

All items below are **leads requiring curator verification**.

| Decision point | Lead | Rationale |
|---|---|---|
| New MF term from structure | **Do not add any.** | No fold reaches TM 0.5; no InterPro signature; no conserved catalytic or binding residues can be nominated. The hypothesis supplies no basis for an MF assertion |
| Existing "molecular function unknown" status | **Retain.** The correct representation is GO:0003674 with a `ND` style no-data stance, or no MF annotation at all | The structural search is a documented negative, which strengthens rather than weakens leaving MF empty |
| `protein binding` (GO:0005515) as a fallback | **Avoid as a final recommendation.** Only 2 IntAct and 59 BioGRID entries exist, none with an identified direct biochemical partner for ICY1 | Per curation guidance, uninformative; the Atg9-style interaction route (see below) would be the informative replacement if demonstrated |
| CC GO:0000329 fungal-type vacuole membrane (HDA, SGD) | **Retain as non-core, with the existing HDA evidence code.** Do not upgrade to a direct-binding or integral-membrane claim | Supported only by subtractive vacuolar proteomics (PMID 19001347); UniProt topology is "peripheral membrane protein". The amphipathic helix found here (muH 0.481 at residues 106-123) is a candidate mechanism but is itself computational |
| BP terms derived from *icy1Δ* phenotypes (invasive growth, petite-negativity) | **Treat as downstream phenotype, non-core**, unless a curator finds direct pathway evidence | Both come from genetic screens (PMID 14504216 and the invasive-growth screen cited in UniProt); high-copy suppression is a classic source of indirect BP over-annotation |
| Any IEA/ISS transfer from the top Foldseek hits | **Block.** The top matches (TRAK2, BBP1, Jun, collagen, clathrin light chain, Src substrate p85) are coiled-coil promiscuity artifacts at 0.5-8% identity | These would be textbook structural-noise over-annotation |

## Mechanistic scope

The immediate question is whether ICY1's polypeptide itself carries a catalytic or binding activity readable from its 3D shape. The answer from this analysis is no: the chain has no packed core, so there is no active-site geometry, no ligand pocket and no interface to annotate.

Separate from that, three downstream observations exist in the literature and must not be converted into molecular function. (1) *icy1Δ* cells cannot grow without mtDNA and ICY1 overexpression suppresses *tim18Δ* petite-negativity: a genetic interaction at the level of mitochondrial inner-membrane potential, several steps removed from ICY1's own activity. (2) *icy1Δ* shows an invasive-growth defect with elongated morphology: a developmental/colony-level phenotype. (3) ICY1 co-purifies with vacuolar membranes and is induced by amino-acid starvation: a localization and a regulatory observation. The one biochemical lead the structure does supply is the C-terminal amphipathic helix (residues 106-123, DKLTDLYANAAQQNYRLW, hydrophobic moment 0.481 at mean hydrophobicity -0.15), which could mediate peripheral membrane binding directly. That remains a prediction.

## Conflicts and alternatives

The paralog is the main alternative framing. ICY2 / YPL250C (UniProt Q12048) was renamed **ATG41** after it was shown to interact with Atg9 and to be required for autophagosome formation (PMID 26565778). Its AlphaFold model has the identical signature to ICY1: 136 aa, mean pLDDT 60.0, zero long-range contacts, Rg ratio 2.39. A protein in this family therefore acquired a defined cellular role through genetics and interaction work with no fold assignment at all. Absence of a structural homolog is not evidence against function for ICY1.

Secondary conflicts. The protein name "Interacting with cytoskeleton protein 1" is a database carry-over from a large-scale screen and is not supported by any primary cytoskeletal assay found here; a curator should not read a cytoskeletal function into the symbol. The Foldseek matches to spindle pole component BBP1 and to a doublet-microtubule MIP superficially look cytoskeletal and could reinforce that carry-over, but they are coiled-coil noise at 1.6% and 8.1% sequence identity and must not be used that way. The vacuolar localization rests on subtractive proteomics, a method whose own authors note that proteins from other compartments co-enrich.

## Knowledge gaps

1. **Does ICY1 fold on binding?** Checked: monomeric AlphaFold model and monomeric Foldseek only. Matters because a conditionally folded helix in a complex would give a real interface to annotate. Resolved by AlphaFold-Multimer or Boltz predictions of ICY1 with candidate partners (Atg9, vacuolar membrane proteins, its BioGRID hits), or by circular dichroism of recombinant ICY1 with and without liposomes.
2. **Is the C-terminal helix a membrane-binding amphipathic helix?** Checked: hydrophobic-moment scan only (muH 0.481, at the low end of the 0.45-0.50 band for lipid-binding helices). Matters because it would convert the CC annotation from co-purification to mechanism. Resolved by liposome flotation of ICY1 106-127 peptide and by testing an L112D/L123D-style hydrophobic-face mutant for loss of vacuolar localization.
3. **How deep is the ICY1 family?** Checked: OrthoDB group 4033322at2759 and HOGENOM CLU_149528_0_0_1 are listed in the UniProt record, but orthology breadth was not retrieved programmatically in this run. Matters because a fungal-restricted, fast-evolving disordered protein changes the prior on finding any distant homolog. Resolved by an explicit HMMER/jackhmmer profile search and an OrthoDB species-coverage query.
4. **Does ICY1 have an autophagy phenotype like Atg41?** Checked: literature search only; no primary paper assays *icy1Δ* for autophagy. Matters directly for whether a BP term is addable. Resolved by Pho8Δ60 and GFP-Atg8 processing assays in *icy1Δ*, *atg41Δ* and the double mutant.
5. **Is there a direct ICY1 binding partner?** Checked: UniProt cross-references only (IntAct 2, BioGRID 59). Matters because it is the only realistic route to a non-"protein binding" MF term. Resolved by affinity purification of tagged Icy1 under amino-acid starvation followed by mass spectrometry.

## Discriminating tests

Ranked by how much they would change the curation.

1. AlphaFold-Multimer / Boltz co-folding of ICY1 with Atg9, with Atg41, and with its top BioGRID partners. Reading out ipTM and interface PAE distinguishes "disordered and inert" from "conditionally folded binding element". Cheap, and it is the direct successor to the monomeric search that failed.
2. Autophagy flux assays (Pho8Δ60, GFP-Atg8 processing) in *icy1Δ* versus *atg41Δ* versus the double mutant under nitrogen starvation. Tests whether ICY1 shares the paralog's pathway and would supply a defensible BP term.
3. Liposome flotation with purified Icy1 and with the 106-127 peptide, plus a hydrophobic-face mutant, scored by vacuolar membrane localization in vivo. Converts GO:0000329 from co-purification to a mechanistically supported CC annotation.
4. jackhmmer profile search of ICY1 across fungi and beyond, followed by Foldseek on the most divergent ortholog models. If the family is fungal-only and uniformly disordered, close the fold question; if a distant ordered ortholog exists, re-run the search on it.
5. Limited proteolysis or NMR of recombinant Icy1 to test the disorder prediction experimentally. Lowest curation yield but it settles the premise directly.

## Curation leads

Candidate references to verify, with exact snippets:

- PMID **26565778**: "Here, we identified the yeast protein Icy2, which we now name Atg41, as playing a role in autophagosome formation. Atg41 interacts with the transmembrane protein Atg9, a key component involved in autophagosome biogenesis, and both proteins display a similar localization profile." Use as paralog context; **do not** transfer to ICY1.
- PMID **14504216**: "We identified several genes encoding cytosolic proteins, including CCT6, SSB1, ICY1, TIP41, and PBP1, which, when overproduced, rescue the mtDNA dependence of tim18Delta cells." Supports a genetic phenotype only. Note the tension with the vacuolar membrane annotation: this paper calls ICY1 cytosolic.
- PMID **19001347**: "A robust statistical analysis combining enrichment ranking with the double boundary iterative group analysis revealed that 148 proteins were significantly enriched in the pure vacuolar preparations." Source of GO:0000329 HDA.
- PMID **20164152**: "protein pairs with a TM-score >0.5 are mostly in the same fold" (abstract truncated in the retrieved record at "...are mostly in t"; verify the full sentence against the published abstract before quoting). Threshold justification.

Suggested action changes:

- Add a free-text note to the ICY1 review recording the negative structural search with its parameters and date, so a future reviewer does not repeat it.
- Flag the recommended name "Interacting with cytoskeleton protein 1" as unsupported by primary assay, and flag the Foldseek coiled-coil hits as non-transferable.
- Keep MF unannotated. Keep CC GO:0000329 with HDA, marked non-core. Do not add BP terms from suppressor genetics.

Suggested questions for the curator:

- Does the repository's existing ICY1 bioinformatics analysis (withheld from this run) reach the same null, and with which database versions?
- Is there an internal policy for recording a documented negative fold search as curation evidence? It is more useful here than any positive term.
- Should ICY1 and ICY2/ATG41 be reviewed as a pair given the shared disorder signature and shared Gcn4 induction?

## Provenance artifacts

Written to `provenance/`:

- `ICY1_foldseek_summary.csv`: every reported number in one table.
- `ICY1_foldseek_tmalign_all_hits.csv`: all 704 TM-align hits across PDB100, CATH50, AFDB/Swiss-Prot and AFDB50, with TM-score, probability, sequence identity, alignment length, target length and query coverage.
- `ICY1_foldseek_3diaa_hits.csv`: all 3Di+AA mode hits with E-values.
- `ICY1_globularity_benchmark.csv`: pLDDT, Rg, Rg ratio and long-range contact counts for ICY1, ICY2/ATG41, FKBP1A, lysozyme C, tau, alpha-synuclein and collagen alpha-1(I).
- `plot_1.png`: pLDDT profile, PAE matrix, CA-CA contact map, and the tertiary-packing benchmark.
- `plot_2.png`: TM-score distribution per database against the 0.5 threshold, and the top 10 hits with coverage.
- `out/`: raw Foldseek JSON responses, the AlphaFold PDB, the trimmed helix control model, and the PAE matrix.

All structural results come from the public Foldseek web server (https://search.foldseek.com) and AlphaFold DB v6, queried on 2026-11-23. Nothing in this report is a simulated or hand-drawn result.
