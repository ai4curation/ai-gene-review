---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T19:18:06.318812'
end_time: '2026-07-11T19:35:21.045834'
duration_seconds: 1034.73
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lpd
  gene_symbol: lpd
  uniprot_accession: Q88C17
  protein_description: 'RecName: Full=Dihydrolipoyl dehydrogenase {ECO:0000256|ARBA:ARBA00012608,
    ECO:0000256|RuleBase:RU003692}; EC=1.8.1.4 {ECO:0000256|ARBA:ARBA00012608, ECO:0000256|RuleBase:RU003692};'
  gene_info: Name=lpd {ECO:0000313|EMBL:AAN70931.1}; OrderedLocusNames=PP_5366 {ECO:0000313|EMBL:AAN70931.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-I pyridine nucleotide-disulfide
  protein_domains: Class-I_Pyr_Nuc-Dis_Oxidored. (IPR050151); FAD/NAD-bd_sf. (IPR036188);
    FAD/NAD-binding_dom. (IPR023753); FAD/NAD-linked_Rdtase_dimer_sf. (IPR016156);
    Lipoamide_DH. (IPR006258)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lpd-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lpd-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88C17
- **Protein Description:** RecName: Full=Dihydrolipoyl dehydrogenase {ECO:0000256|ARBA:ARBA00012608, ECO:0000256|RuleBase:RU003692}; EC=1.8.1.4 {ECO:0000256|ARBA:ARBA00012608, ECO:0000256|RuleBase:RU003692};
- **Gene Information:** Name=lpd {ECO:0000313|EMBL:AAN70931.1}; OrderedLocusNames=PP_5366 {ECO:0000313|EMBL:AAN70931.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-I pyridine nucleotide-disulfide
- **Key Domains:** Class-I_Pyr_Nuc-Dis_Oxidored. (IPR050151); FAD/NAD-bd_sf. (IPR036188); FAD/NAD-binding_dom. (IPR023753); FAD/NAD-linked_Rdtase_dimer_sf. (IPR016156); Lipoamide_DH. (IPR006258)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lpd" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lpd' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lpd** (gene ID: lpd, UniProt: Q88C17) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *lpd* (PP_5366, UniProt Q88C17) in *Pseudomonas putida* KT2440

**Target:** Dihydrolipoyl dehydrogenase (dihydrolipoamide dehydrogenase, E3), EC 1.8.1.4
**Gene:** *lpd* / OrderedLocusName **PP_5366** (GenBank AAN70931.1; RefSeq WP_010955849.1)
**Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950)
**Length:** 466 aa, ~49.4 kDa; genome position 6,115,792–6,117,192

---

## 1. Summary (Answer to the Research Question)

The product of **PP_5366 (*lpd*, Q88C17)** is a **dihydrolipoyl dehydrogenase (dihydrolipoamide dehydrogenase, "E3", EC 1.8.1.4)** — an FAD-dependent, homodimeric flavoenzyme of the class-I pyridine-nucleotide–disulfide oxidoreductase family. Its primary catalytic function is to **reoxidize the reduced (dihydro)lipoyl group carried on the lysine of a partner E2/H-protein and transfer the electrons, via a redox-active active-site disulfide and the FAD, to NAD⁺, producing NADH** (N⁶-[(R)-dihydrolipoyl]-L-lysyl-[protein] + NAD⁺ → N⁶-[(R)-lipoyl]-L-lysyl-[protein] + NADH + H⁺). It operates in the **cytoplasm** as a soluble homodimer.

A key identification result: although the KT2440 genome labels PP_5366 generically as "*lpd*", **sequence and genomic-context analysis show it is specifically the ortholog of the historically described "third lipoamide dehydrogenase," LPD-3 (gene *lpd3*)** — 97.0% identical to *P. putida* LPD-3, but only ~51% identical to the operon-encoded E3 of the pyruvate/2-oxoglutarate dehydrogenases (LpdG) and ~45% to that of the branched-chain keto-acid dehydrogenase (LpdV). Those two complex-dedicated E3s are separate genes in KT2440 (**PP_4187 lpdG** and **PP_4404 lpdV**). PP_5366/LPD-3 is a standalone, eukaryote-like isozyme that is catalytically competent (it can fully substitute for the housekeeping E3 in pyruvate dehydrogenase and ~60% in 2-oxoglutarate dehydrogenase) but whose dedicated in-vivo physiological niche remains uncharacterized.

---

## 2. Gene/Protein Identity Verification (Mandatory)

- **Gene symbol match:** ✔ "lpd" is the accepted symbol for lipoamide/dihydrolipoyl dehydrogenase; the protein description (Dihydrolipoyl dehydrogenase, EC 1.8.1.4) is consistent.
- **Organism match:** ✔ *P. putida* KT2440 (NCBI taxid 160488).
- **Family/domain match:** ✔ Class-I pyridine nucleotide–disulfide oxidoreductase; FAD/NAD-binding + dimerization domains; lipoamide-DH signature (InterPro IPR006258, IPR050151, IPR036188, IPR023753, IPR016156; NCBIfam TIGR01350 lipoamide_DH; PROSITE PS00076).
- **Paralog disambiguation (critical):** ✔ Resolved. KT2440 encodes **three** EC 1.8.1.4 paralogs (KEGG KO K00382): PP_4187 (*lpdG*), PP_4404 (*lpdV*), and PP_5366 (*lpd* = *lpd3* ortholog). Pairwise identity of PP_5366: **97.0%** to LPD-3 (P31046), 51.1% to LpdG (P31052), 45.2% to LpdV (P09063). PP_5366's 1401-bp/466-aa coding region exactly matches the reported *lpd3* [PMID 1722146].

---

## 3. Molecular Function — What Reaction Is Catalyzed and Substrate Specificity

**Reaction (UniProt/Rhea:15045, EC 1.8.1.4):**
N⁶-[(R)-dihydrolipoyl]-L-lysyl-[protein] + NAD⁺ ⇌ N⁶-[(R)-lipoyl]-L-lysyl-[protein] + NADH + H⁺

- **Substrate specificity:** the physiological substrate is the **protein-bound dihydrolipoyl group** (the lipoyl-lysine "swinging arm" of an E2 dihydrolipoyl acyltransferase or of the glycine-cleavage H-protein), with **NAD⁺ as the electron acceptor**. The isolated LPD-3 protein was shown biochemically to be "clearly a lipoamide dehydrogenase as opposed to a mercuric reductase or glutathione reductase" [PMID 2914869], confirming the specificity within this mechanistically related flavoprotein family.
- **Cofactor:** one non-covalently bound **FAD per subunit** (UniProt; ChEBI:57692).
- **Active site / mechanism:** a **redox-active disulfide (Cys42–Cys47)** accepts electrons from dihydrolipoamide and passes them to FAD, which then reduces NAD⁺. Structural studies of the conserved family show the mechanism "uses two molecules: non-covalently bound FAD and a transiently bound substrate, NAD⁺," and that in the reductive half-reaction "the nicotinamide base stacks directly on the isoalloxazine ring system of the FAD" for hydride transfer [PMID 15946682]. A conserved **His (His445 here) proton acceptor**, working with a neighboring Glu, deprotonates the dithiol during catalysis. Sequence features in Q88C17 confirm this architecture: FAD-binding residues (51, 115, 144–146, 313, 319–322), NAD⁺-binding residues (181–188, 204, 273), catalytic His445, and the redox-active Cys42/Cys47 disulfide.
- **Regulation:** family E3s are subject to product inhibition by NADH (over-reduction of FAD); assembly with the E2 core relieves this by lowering flavin redox potential — "subunit interaction plays an important role in the protection of the enzyme against over-reduction" and interaction with E2p/E2o "relieves the inhibition to a large extent" [PMID 8575446].

**Functional competence of LPD-3:** in a *lpdG* mutant, LPD-3 "completely restored pyruvate dehydrogenase activity" and was "about 60% as effective as LPD-Glc in restoring 2-ketoglutarate dehydrogenase activity" [PMID 2914869], demonstrating it is a fully active E3.

---

### 3a. Structure-Based Inference (AlphaFold)

No experimental structure exists for this specific protein, but the AlphaFold model **AF-Q88C17-F1 (v6)** is of exceptional confidence (**global mean pLDDT = 97.4**; 98% of residues pLDDT ≥ 90; 0% below 50), and every functionally assigned residue is modeled at very high confidence (Cys42 = 98.0, Cys47 = 97.4, FAD-binding Ser51/His115/313 ≈ 98–99, NAD-binding 181/204/273 ≈ 96–98, catalytic His445 = 96.9). Sequence/structure analysis confirms the diagnostic features of the glutathione-reductase-like class-I pyridine-nucleotide–disulfide oxidoreductase fold:
- **FAD Rossmann fingerprint** G9-G10-G11-P-G13-G14 (GxGxxG);
- **NAD⁺ Rossmann fingerprint** G181-A-G183-V-I-G186 (GxGxxG);
- **Redox-active disulfide Cys42/Cys47** within the lipoamide-DH signature (…GGT**C**LNVG**C**MPSK…);
- **Catalytic His445–Glu450 dyad** (…TC**H**PHPT**RSE**…), the general base of the E3 mechanism;
- **Two-domain topology** (N-terminal FAD/NAD(P)-binding Rossmann fold + C-terminal dimerization domain; Pfam PF07992/PF02852).

This independent structural evidence corroborates the enzymatic annotation and places the redox-active dithiol at the *re*-face of the flavin, adjacent to the transient NAD(H) site — the geometry required for the FAD-mediated electron relay [PMID 15946682].

## 4. Quaternary Structure and Subcellular Localization

- **Quaternary structure:** **homodimer**; each of the two active sites is built at the dimer interface, and the redox-active disulfide of one subunit is juxtaposed with the FAD (UniProt SUBUNIT; consistent with all characterized E3 crystal structures, e.g., human E3 [PMID 15946682]).
- **Localization:** **cytoplasm** (UniProt SUBCELLULAR LOCATION; GO:0005737). As a bacterial soluble enzyme it performs its reaction in the cytosol, physically/dynamically associated with the peripheral E2 cores of the 2-oxo-acid dehydrogenase complexes (a "transferase complex", GO:1990234) or with the glycine-cleavage machinery.

---

## 5. Pathway Context and Biological Process

Dihydrolipoyl dehydrogenase is the shared terminal component of the **lipoyl-dependent oxidative decarboxylation systems**: "LADH is the common E3 subunit of the alpha-ketoglutarate (KGDHc), pyruvate (PDHc), and branched-chain α-keto acid dehydrogenase complexes and is also part of the glycine cleavage system" [PMID 28579060]. By reoxidizing the E2/H-protein lipoyl arm and generating NADH, the enzyme:

- Couples **pyruvate → acetyl-CoA** (PDH; KEGG M00307) and the **2-oxoglutarate → succinyl-CoA** step of the TCA cycle (KGDH; M00009/M00011) to the NAD⁺/NADH pool and hence to respiration (GO:0045333 cellular respiration).
- Supports **branched-chain amino-acid catabolism** (BCKAD; leucine degradation M00036) and the **glycine cleavage system** (M00621; one-carbon/folate metabolism).

**Division of labor in *P. putida* (important distinction):** these physiological roles are carried out by the **operon-encoded, complex-dedicated E3s**, not primarily by PP_5366:
- **LpdG (PP_4187)** — encoded within the *sucABCD* operon (neighbors *sucB*/E2o, *sucA*/E1o); it is "the E3 component of the pyruvate and 2-ketoglutarate dehydrogenase complexes and the L-factor for the glycine oxidation system" [PMID 1902462].
- **LpdV (PP_4404)** — encoded within the *bkdAA–bkdAB–bkdB* branched-chain keto-acid dehydrogenase operon; it is "the specific E3 component of the branched-chain keto acid dehydrogenase complex... induced by growth on leucine, isoleucine, or valine" [PMID 1902462], under BkdR/L-branched-chain-amino-acid control [PMID 10217783].
- **PDH (aceEF)** — the pyruvate dehydrogenase E1/E2 genes are located separately at PP_0339 (*aceE*/E1p) and PP_0338 (*aceF*/E2p), far from all three E3 loci; the PDH complex therefore has **no dedicated co-operonic E3** and recruits a shared E3 (LpdG), exactly as the biochemistry indicates. (KEGG lists only three K00382 E3 paralogs genome-wide — PP_4187, PP_4404, PP_5366 — so no fourth, PDH-specific E3 exists.)
- **PP_5366 / LPD-3 (this gene)** — the "third lipoamide dehydrogenase... whose role is unknown" [PMID 1902462]; *lpd3* "is not part of an operon, which is unique for a prokaryotic lipoamide dehydrogenase" [PMID 1722146], and the protein "was not produced in wild-type *P. putida*... under a variety of growth conditions" [PMID 1722146]. It is the most eukaryote-like of the three (~54% identity to pig/human mitochondrial E3) [PMID 1722146].

**Evolutionary placement (this work):** a cross-species pairwise-identity comparison shows PP_5366/LPD-3 is atypically eukaryote-like: 50.9% identical to human E3 (P09622) and 50.7% to yeast E3 (P09624) — as close as to its own bacterial paralog LpdG (51.1%) — whereas the canonical *E. coli* housekeeping Lpd (P0A9P0) is only 43.9% identical to human E3 and 42.9% to LPD-3. This indicates LPD-3 is an evolutionarily distinct isozyme (ancient duplication or horizontal acquisition), consistent with its standalone genomic location, rather than a recent duplicate of LpdG/LpdV.

**Interpretation of PP_5366's specific role:** its molecular function is unambiguous (an authentic, catalytically competent dihydrolipoamide:NAD⁺ oxidoreductase). However, its dedicated physiological niche/regulon is not established. The evidence (latent expression in the wild type, standalone locus, ability to substitute for LpdG) is most consistent with a **backup/redundant isozyme** that can supply E3 activity to the 2-oxo-acid dehydrogenase complexes under conditions where the primary E3 is absent or limiting. The KEGG assignment of PP_5366 to all E3-dependent pathways reflects its enzymatic capability (K00382) rather than a demonstrated dedicated in-vivo assignment.

---

## 6. Supported and Refuted Hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| PP_5366 encodes a dihydrolipoyl dehydrogenase (EC 1.8.1.4), FAD homodimer, cytoplasmic | **Supported** | UniProt Q88C17; family/domain signatures; biochemistry of LPD-3 [PMID 2914869] |
| PP_5366 is the operon-embedded, complex-dedicated housekeeping E3 (LpdG) | **Refuted** | Only 51% identity to LpdG; the dedicated E3s are separate genes PP_4187/PP_4404; PP_5366 is standalone |
| PP_5366 is the branched-chain (LpdV) E3 | **Refuted** | Only 45% identity to LpdV; LpdV = PP_4404 in the *bkd* operon |
| PP_5366 is the ortholog of the "third" lipoamide dehydrogenase, LPD-3/*lpd3* | **Supported** | 97.0% identity to LPD-3; exact 466-aa/1401-bp match; standalone locus [PMID 1722146] |
| PP_5366/LPD-3 is catalytically able to serve 2-oxo-acid dehydrogenase complexes | **Supported** | Complements *lpdG* mutant: full PDH, ~60% OGDH restoration [PMID 2914869] |
| PP_5366/LPD-3 has a defined, dedicated physiological role | **Not established** | Latent in wild type; role historically "unknown" [PMID 1902462; PMID 1722146] |

---

## 7. Evidence Types

- **Experimental (primary):** enzymatic characterization and mutant complementation of LPD-3 [PMID 2914869]; gene cloning/sequence and operon analysis of *lpd3*, *lpdG*, *lpdV* [PMID 1722146, 1902462, 2917566, 6185468]; family catalytic-mechanism crystallography [PMID 15946682]; E3–E2 interaction/inhibition [PMID 8575446]; *bkd* regulation [PMID 10217783].
- **Bioinformatic/sequence (this work):** Needleman–Wunsch pairwise identity assigning PP_5366 to LPD-3 (97.0%); KEGG K00382 paralog enumeration (PP_4187/4404/5366); genomic-context (operon) analysis placing LpdG in *sucABCD* and LpdV in *bkd*, PP_5366 standalone; UniProt/InterPro domain and active-site residue mapping; Rossmann fingerprint and His445–Glu450 dyad identification.
- **Structural inference (this work):** AlphaFold AF-Q88C17-F1 v6, mean pLDDT 97.4, all catalytic/cofactor residues pLDDT 96–99, confirming the canonical E3 fold and active-site architecture.
- **Database annotation:** UniProt Q88C17, KEGG ppu:PP_5366, InterPro, Rhea.

---

## 8. Limitations and Future Directions

- The precise physiological role and expression conditions of the LPD-3 isozyme (PP_5366) remain undetermined; classic work was performed in strain PpG2, not KT2440. Targeted transcriptomics/proteomics and a clean ∆PP_5366 (alone and combined with ∆*lpdG*/∆*lpdV*) knockout in KT2440 would test whether it provides conditional backup E3 activity, stress-specific function, or a distinct partner.
- No experimental 3D structure of PP_5366 exists; the mechanism/active-site description is inferred from the highly conserved E3 family plus a very-high-confidence AlphaFold model (mean pLDDT 97.4). Because E3 function in KT2440 is distributed across three paralogs (PP_4187/PP_4404/PP_5366), a single-gene knockout is not expected to be phenotypically essential on rich or minimal medium (cf. the genome-wide conditional-essentiality screen of KT2440 [PMID 20158506]); dedicated multi-knockout studies would be needed to expose the specific contribution of PP_5366.
- The eukaryote-like character of LPD-3 raises (untested) questions about horizontal acquisition or a specialized redox/moonlighting function; this was not resolved here.

---

## References (PMID)
1722146 · 1902462 · 2914869 · 2917566 · 6185468 · 15946682 · 17960497 · 8575446 · 28579060 · 10217783 · 20158506


## Artifacts

- [OpenScientist final report](lpd-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lpd-deep-research-openscientist_artifacts/final_report.pdf)