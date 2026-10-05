---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T04:15:03.683554'
end_time: '2026-08-11T04:40:24.673045'
duration_seconds: 1520.99
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: Q88IS1
  gene_symbol: PP_2928
  uniprot_accession: Q88IS1
  protein_description: 'SubName: Full=Saccharopine dehydrogenase {ECO:0000313|EMBL:AAN68536.1};'
  gene_info: OrderedLocusNames=PP_2928 {ECO:0000313|EMBL:AAN68536.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: NAD(P)-bd_dom_sf. (IPR036291); Sacchrp_dh-like_C. (IPR032095);
    Sacchrp_dh_NADP-bd. (IPR005097); Sacchrp_dh_C (PF16653); Sacchrp_dh_NADP (PF03435)
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
citation_count: 4
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_2928-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_2928-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88IS1
- **Protein Description:** SubName: Full=Saccharopine dehydrogenase {ECO:0000313|EMBL:AAN68536.1};
- **Gene Information:** OrderedLocusNames=PP_2928 {ECO:0000313|EMBL:AAN68536.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** NAD(P)-bd_dom_sf. (IPR036291); Sacchrp_dh-like_C. (IPR032095); Sacchrp_dh_NADP-bd. (IPR005097); Sacchrp_dh_C (PF16653); Sacchrp_dh_NADP (PF03435)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2928" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2928' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2928** (gene ID: Q88IS1, UniProt: Q88IS1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_2928 (Q88IS1) in *Pseudomonas putida* KT2440

## 1. Summary (Answer to the Research Question)

The protein encoded by **PP_2928** (UniProt **Q88IS1**), generically annotated in databases as a
"saccharopine dehydrogenase," is more precisely a **carboxyspermidine dehydrogenase
(equivalently carboxynorspermidine dehydrogenase/synthase; CASDH/CANSDH), EC 1.5.1.43**. It is a
soluble, **cytoplasmic, NADPH‑dependent oxidoreductase** that catalyzes the reductive condensation
of **L‑aspartate‑4‑semialdehyde** with a diamine (**putrescine → carboxyspermidine**, or
**1,3‑diaminopropane → carboxynorspermidine**). This is the **penultimate step of the alternative
("carboxyspermidine") biosynthetic pathway for the polyamine spermidine (and sym‑norspermidine)**.
Its product is decarboxylated by the immediately adjacent enzyme **PP_2929** (carboxyspermidine/
carboxynorspermidine decarboxylase, CASDC, EC 4.1.1.96) to yield spermidine (or norspermidine).
Because *P. putida* KT2440 **lacks the canonical spermidine synthase (SpeE) and S‑adenosylmethionine
decarboxylase (SpeD)**, PP_2928 is expected to be the organism's principal route to spermidine.

## 2. Target Identity Verification

| Attribute | Value |
|---|---|
| UniProt | Q88IS1 (Q88IS1_PSEPK), 414 aa, 45.4 kDa, evidence level 4 (Predicted) |
| Locus | PP_2928 (OrderedLocusName); RefSeq WP_003248123.1; GenBank AAN68536 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125), TaxID 160488 |
| Domains | PF03435 Sacchrp_dh_NADP (res 5–146); PF16653 Sacchrp_dh_C (res 150–396) |
| Superfamily | Gene3D 3.40.50.720 NAD(P)-binding Rossmann fold; eggNOG **COG1748** (saccharopine dehydrogenase & related) |
| PANTHER | **PTHR43796:SF2 "Carboxynorspermidine synthase"** |
| KEGG | ppu:PP_2928 — name "Saccharopine dehydrogenase", **no KO, no pathway assigned** |

The gene symbol and organism match the UniProt record. The database label "saccharopine dehydrogenase"
is a **family‑level automatic annotation**, not an experimentally determined activity; this report
resolves the specific function using domain architecture, orthology, genomic context, and pathway logic.

## 3. Key Findings and Evidence

### 3.1 Enzymatic function: carboxyspermidine dehydrogenase (EC 1.5.1.43)

Four independent lines of evidence converge:

1. **Fold/family.** PP_2928 has the two‑domain saccharopine‑dehydrogenase architecture
   (PF03435 + PF16653) on a Rossmann NAD(P)‑binding fold, with an N‑terminal dinucleotide‑binding
   fingerprint `IIGAGGVAK` (residues 7–14). CASDH is a member of this saccharopine‑dehydrogenase
   structural superfamily (COG1748).
2. **Orthology.** UniProt's PANTHER classification assigns Q88IS1 to **PTHR43796:SF2,
   "Carboxynorspermidine synthase"** — i.e., CASDH.
3. **Genomic context (operon logic).** PP_2928 (complement 3,329,627–3,330,871) lies immediately
   adjacent to, and co‑oriented with, **PP_2929 = carboxynorspermidine/carboxyspermidine
   decarboxylase (CASDC; KEGG K13747; EC 4.1.1.96)**. CASDH and CASDC are the diagnostic,
   frequently‑clustered enzyme pair of the alternative polyamine pathway [Hanfrey 2011].
4. **Pathway‑gap logic.** KEGG assigns the decarboxylase KO (K13747) to PP_2929 but leaves the
   partner dehydrogenase KO (**K13746, CASDH, EC 1.5.1.43**) unassigned in *P. putida*. PP_2928 —
   an unassigned, CASDH‑fold protein sitting next to CASDC — is the "missing" dehydrogenase.

**Quantitative orthology (added Iteration 2).** By global (Needleman–Wunsch) alignment, PP_2928
(414 aa) is **45.2% identical over its full length to the reviewed, experimentally characterized
carboxynorspermidine synthase/dehydrogenase of *Vibrio cholerae* (UniProt Q9KRL3, VC_1624, 414 aa;
Lee et al. 2009)**, 46.2% to *V. alginolyticus* CANSDH (P0DPE4, 414 aa), 44.5% to *Idiomarina
loihiensis* (Q5QY81) and 42.3% to *Geobacter sulfurreducens* (Q74A52) — all annotated CANSDH/CASDH
(EC 1.5.1.43). By contrast PP_2928 is only **21.1%** identical to its own operon partner CASDC
(PP_2929), confirming they are distinct enzymes of the same pathway. ~45% identity over the entire
length, to a *reviewed, biochemically validated* enzyme, is well above the threshold for confident
functional transfer and moves the assignment beyond family-level inference.

**Reactions catalyzed** (from the 45%-identical reviewed ortholog Q9KRL3; the enzyme is dual-substrate):
> (i) L‑aspartate‑4‑semialdehyde + **1,3‑diaminopropane** + NADPH → **carboxynorspermidine** + NADP⁺ + H₂O (Rhea 34115)
> (ii) L‑aspartate‑4‑semialdehyde + **putrescine** + NADPH → **carboxyspermidine** + NADP⁺ + H₂O (Rhea 34111)

Aspartate‑β‑semialdehyde is the aminopropyl donor, replacing decarboxylated S‑adenosylmethionine used
by the canonical pathway. The *V. cholerae* ortholog is classified in UniProt as "saccharopine
dehydrogenase family, **Carboxynorspermidine synthase subfamily**" — the exact subfamily to which
PP_2928's domain architecture belongs. Deletion of this enzyme in *V. cholerae* abolishes **both**
norspermidine and spermidine and causes accumulation of 1,3‑diaminopropane (Lee et al. 2009),
demonstrating the dual‑substrate physiology.

**Cofactor/active-site conservation (Iteration 3).** The PP_2928 ↔ *V. cholerae* CANSDH alignment is
colinear over 417 columns with only 6 gaps (no large insertions/deletions), indicating identical
two-domain 3D architecture. The N‑terminal NAD(P)H‑binding Rossmann fingerprint is conserved
(PP_2928 `…IIGAGGVAK…IAIASRNISKC…` vs CANSDH `…LQIGAGGVGW…ITIASRSIAKC…`; the βαβ glycine‑rich
`GAGGV` motif and the downstream `IASR` dinucleotide‑binding motif are retained), confirming that
PP_2928 binds an NADP(H) cofactor exactly as the characterized enzyme does.

### 3.2 Pathway placement and the reason P. putida needs this enzyme

*P. putida* KT2440 **lacks** the canonical spermidine‑biosynthesis genes — spermidine synthase
*speE* (K00797) and SAM decarboxylase *speD* (K01611) are absent from the genome (KEGG). It **does**
encode the alternative‑pathway decarboxylase CASDC (PP_2929). Therefore the two‑step
**CASDH (PP_2928) → CASDC (PP_2929)** route is the only genomically encoded path to spermidine.
This mirrors the situation described by Hanfrey et al. (2011): species that make spermidine but lack
SpeD/SpeE instead carry carboxynorspermidine dehydrogenase and decarboxylase orthologues. The reaction
maps to KEGG **map00330 (Arginine and proline metabolism)**.

**Complete pathway reconstruction from primary metabolites (Iteration 3).** *P. putida* KT2440 encodes
every step needed to feed PP_2928 and to finish the pathway:

| Step | Enzyme | Locus (KEGG KO) |
|---|---|---|
| L‑aspartate → L‑aspartate‑4‑semialdehyde | aspartate‑semialdehyde dehydrogenase *asd* | PP_1989 (K00133) |
| L‑arginine → agmatine | arginine decarboxylase *speA* | PP_0567 (K01585) |
| agmatine → putrescine | agmatinase *speB* | PP_2196 (K01480) |
| L‑ornithine → putrescine | ornithine decarboxylase *speC* | PP_0864 (K01581) |
| **ASA + putrescine + NADPH → carboxyspermidine** | **CASDH** | **PP_2928 (this study; K13746 unassigned in KEGG)** |
| carboxyspermidine → **spermidine** | CASDC | PP_2929 (K13747) |

Both PP_2928 substrates are therefore demonstrably produced by the cell. The 1,3‑diaminopropane branch
is incomplete (DABA decarboxylase *ddc*/K13745 is **absent** in the KEGG annotation, although DABA
aminotransferase *dat* is present at PP_2800/PP_4223), so **putrescine is the more likely in vivo amine
substrate and spermidine the more likely product**, even though the enzyme is intrinsically
dual‑specificity. The canonical genes *speD* (K01611) and *speE* (K00797) are absent from KEGG, so this route is
the sole genomically encoded path to spermidine.

**Ruling out a canonical bypass (Iteration 4).** *P. putida* does encode one aminopropyltransferase‑
domain protein, PP_1867 (Q88LR2; Pfam PF01564 *Spermine_synth*; PANTHER PTHR43317 thermospermine
synthase). However, (i) its "spermidine synthase" name derives **only** from automated ProtNLM
text‑mining (ECO:0008006), and KEGG lists it as a "conserved protein of unknown function" with no KO;
and (ii) more decisively, canonical spermidine/spermine synthases require **decarboxylated
S‑adenosylmethionine (dcSAM)** as the aminopropyl donor, produced by **SAM decarboxylase (SpeD)** —
which *P. putida* **does not encode** (no KEGG K01611; zero hits in a UniProt proteome search for
adenosylmethionine decarboxylase). Without dcSAM, no aminopropyltransferase can synthesize spermidine.
The CASDH→CASDC route instead uses **L‑aspartate‑4‑semialdehyde** as the aminopropyl donor and is fully
encoded, so **PP_2928/PP_2929 constitute the only complete de novo route to spermidine in *P. putida*.**
(By contrast, *P. aeruginosa* makes norspermidine through a genuinely SAM‑dependent aminopropyltransferase
system, *speD2/speE2* = PA4773–PA4775 (Bolard et al. 2019) — a route absent from *P. putida*, underscoring
that the two pseudomonads use different chemistries.)

### 3.3 Subcellular localization

PP_2928 is a **cytoplasmic** enzyme: 414 aa, soluble, with **no predicted signal peptide or
transmembrane segment** (the N‑terminus is a Rossmann dinucleotide‑binding start, `MKKNVLIIGAGGVAK`).
NADPH‑dependent polyamine‑biosynthetic reactions occur in the cytosol.

### 3.4 Structural model confidence

The AlphaFold model of Q88IS1 (AF‑Q88IS1‑F1, v6) is **very high confidence**: mean pLDDT = 95.9, with
92% of residues ≥90 and none <50. The model is well‑ordered across both the N‑terminal Rossmann
NAD(P)‑binding domain and the C‑terminal substrate‑binding domain, consistent with the two‑domain
carboxynorspermidine‑synthase/saccharopine‑dehydrogenase fold and with the colinear (gap‑poor)
alignment to the characterized *V. cholerae* CANSDH.

### 3.5 Physiological importance

Polyamines (spermidine/norspermidine) are essential polycations supporting translation, growth, and
biofilm formation. In *Vibrio cholerae*, deletion of CANSDH or CANSDC abolishes spermidine/norspermidine,
reduces planktonic growth by 50–60%, and severely impairs biofilm formation (Lee et al. 2009). By
analogy — and given the absence of a bypass route — PP_2928 is expected to be important for optimal
growth and biofilm physiology in *P. putida* (a specific *P. putida* knockout has not, to my knowledge,
been reported).

## 4. Hypotheses: Supported and Refuted

- **Supported:** PP_2928 = carboxyspermidine/carboxynorspermidine dehydrogenase (EC 1.5.1.43),
  operating with adjacent CASDC (PP_2929) in de novo spermidine biosynthesis (cytoplasmic;
  KEGG arginine/proline metabolism). Strong convergent bioinformatic evidence.
- **Refuted / rejected:** PP_2928 is NOT involved in the well‑studied *P. putida* L‑/D‑lysine
  catabolic pathways. The definitive RB‑TnSeq study of *P. putida* lysine metabolism
  (Thompson et al. 2019, mBio) does **not** implicate PP_2928; its characterized enzymes are elsewhere
  in the genome (e.g., PP_5260, PP_5257/8, PP_2909/10, PP_3592/3). The literal "saccharopine
  dehydrogenase" (lysine biosynthesis/degradation via saccharopine) function is not supported by
  genomic context and is superseded by the carboxyspermidine assignment.

## 5. Limitations and Future Directions

- The assignment rests on **comparative/structural inference** (45% identity to an experimentally
  characterized enzyme, conserved NADP(H)‑binding fingerprint, very‑high‑confidence AlphaFold model,
  operon synteny, complete pathway reconstruction, and pathway‑gap logic) rather than on a direct
  enzymatic assay of the *P. putida* protein itself; UniProt's evidence level remains "Predicted."
  This is homology at a level (~45%, full‑length, to a *reviewed* enzyme) that is generally considered
  reliable for transferring enzymatic function, but a direct assay would formally close the gap.
- Genome‑wide RB‑TnSeq fitness data for *P. putida* KT2440 exist (Deutschbauer lab Fitness Browser) and
  would provide organism‑specific phenotypic evidence, but the resource was not machine‑accessible during
  this study (blocked by an anti‑bot gateway).
- **Substrate ambiguity:** whether the physiological product is spermidine (from putrescine) or
  sym‑norspermidine (from 1,3‑diaminopropane) depends on the available diamine pool; many bacteria with
  this pathway make predominantly spermidine (Hanfrey 2011), but this should be measured in *P. putida*.
- **Recommended experiments:** (i) heterologous expression and in vitro assay with L‑aspartate‑
  β‑semialdehyde + putrescine/1,3‑diaminopropane + NADPH, monitoring carboxyspermidine/carboxynorspermidine
  formation; (ii) a ΔPP_2928 mutant with polyamine profiling (expected loss of spermidine) and growth/
  biofilm phenotyping; (iii) an AlphaFold model + docking to confirm the Rossmann NADP site and the
  substrate channel; (iv) genetic complementation of a *V. cholerae* or *E. coli* CANSDH deletant.

## 6. References

1. Lee J, Sperandio V, Frantz DE, Longgood J, Camilli A, Phillips MA, Michael AJ. *An alternative
   polyamine biosynthetic pathway is widespread in bacteria and essential for biofilm formation in
   Vibrio cholerae.* J Biol Chem. 2009;284(15):9899–9907. PMID: 19196710.
2. Hanfrey CC, Pearson BM, Hazeldine S, Lee J, Gaskin DJ, Woster PM, Phillips MA, Michael AJ.
   *Alternative spermidine biosynthetic route is critical for growth of Campylobacter jejuni and is the
   dominant polyamine pathway in human gut microbiota.* J Biol Chem. 2011;286(50):43301–43312.
   PMID: 22025614.
3. Thompson MG, Blake‑Hedges JM, Cruz‑Morales P, et al. *Massively Parallel Fitness Profiling Reveals
   Multiple Novel Enzymes in Pseudomonas putida Lysine Metabolism.* mBio. 2019;10(3):e02577‑18.
   PMID: 31064836. (Used to exclude a lysine‑catabolic role for PP_2928.)
4. Bolard A, Schniederjans M, Häussler S, et al. *Production of Norspermidine Contributes to
   Aminoglycoside Resistance in pmrAB Mutants of Pseudomonas aeruginosa.* Antimicrob Agents Chemother.
   2019;63(10):e01044‑19. PMID: 31383668. (Cited as a *contrast*: P. aeruginosa uses a SAM‑dependent
   aminopropyltransferase route, not the CANSDH route.)
5. UniProt Q88IS1, Q9KRL3, P0DPE4, Q88LR2; KEGG ppu:PP_2928/PP_2929/PP_1867/PP_1989/PP_0567/PP_2196/
   PP_0864, KOs K13746/K13747/K00797/K01611/K01585/K01480/K01581/K00133 (accessed 2026‑08‑11).


## Artifacts

- [OpenScientist final report](PP_2928-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_2928-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19196710
2. PMID:22025614
3. PMID:31064836
4. PMID:31383668