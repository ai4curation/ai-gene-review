---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T13:26:42.768565'
end_time: '2026-09-01T13:41:20.421427'
duration_seconds: 877.65
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial DNA-directed RNA polymerase core enzyme
  module_summary: Species-neutral bacterial module for the DNA-directed RNA polymerase
    core enzyme that carries out DNA-templated RNA synthesis. The conserved bacterial
    core enzyme is built from an alpha dimer, beta and beta-prime catalytic cleft
    subunits, and the omega assembly/stability subunit. This module deliberately stops
    at the core enzyme and excludes sigma factors, transcription elongation factors,
    and promoter-specific regulatory proteins.
  module_outline: "- Bacterial DNA-directed RNA polymerase core enzyme\n  - 1. alpha\
    \ dimer assembly platform\n  - RpoA alpha dimer platform\n    - rpoA: RNA polymerase\
    \ alpha subunit (molecular player: bacterial DNA-directed RNA polymerase alpha\
    \ subunit family; activity or role: protein dimerization activity)\n  - 2. beta\
    \ and beta-prime catalytic cleft\n  - RpoB/RpoC catalytic cleft\n    - rpoB: RNA\
    \ polymerase beta subunit (molecular player: DNA-directed RNA polymerase beta\
    \ subunit family; activity or role: contributes to DNA-directed RNA polymerase\
    \ activity)\n    - rpoC: RNA polymerase beta-prime subunit (molecular player:\
    \ bacterial DNA-directed RNA polymerase beta-prime subunit family; activity or\
    \ role: contributes to DNA-directed RNA polymerase activity)\n  - 3. omega assembly\
    \ and stability subunit\n  - RpoZ omega assembly/stability subunit\n    - rpoZ:\
    \ RNA polymerase omega subunit (molecular player: DNA-directed RNA polymerase\
    \ omega subunit family; activity or role: contributes to DNA-directed RNA polymerase\
    \ activity)"
  module_connections: '- RpoA alpha dimer platform feeds into RpoB/RpoC catalytic
    cleft: The alpha dimer provides the assembly platform for recruitment of the beta
    and beta-prime subunits into the core enzyme.

    - RpoZ omega assembly/stability subunit promotes RpoB/RpoC catalytic cleft: The
    omega subunit supports proper assembly and stability of the beta/beta-prime-containing
    core enzyme.'
  pathway_query: ppu03020
  pathway_id: ppu03020
  pathway_name: RNA polymerase
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03020 with 4 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '4'
  candidate_genes: '- rpoB: PP_0447 | Q88QP2 | DNA-directed RNA polymerase subunit
    beta (RNAP subunit beta) (EC 2.7.7.6) (RNA polymerase subunit beta) (Transcriptase
    subunit beta) (EC 2.7.7.6; primary bucket kegg:ppu03020)

    - rpoC: PP_0448 | Q88QP1 | DNA-directed RNA polymerase subunit beta'' (RNAP subunit
    beta'') (EC 2.7.7.6) (RNA polymerase subunit beta'') (Transcriptase subunit beta'')
    (EC 2.7.7.6; primary bucket kegg:ppu03020)

    - rpoA: PP_0479 | Q88QL1 | DNA-directed RNA polymerase subunit alpha (RNAP subunit
    alpha) (EC 2.7.7.6) (RNA polymerase subunit alpha) (Transcriptase subunit alpha)
    (EC 2.7.7.6; primary bucket kegg:ppu03020)

    - rpoZ: PP_5301 | Q88C82 | DNA-directed RNA polymerase subunit omega (RNAP omega
    subunit) (EC 2.7.7.6) (RNA polymerase omega subunit) (Transcriptase subunit omega)
    (EC 2.7.7.6; primary bucket kegg:ppu03020)'
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial_rna_polymerase_core__ppu03020-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_rna_polymerase_core__ppu03020-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial DNA-directed RNA polymerase core enzyme in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03020
- Resolved ID: ppu03020
- Resolved name: RNA polymerase
- Source: KEGG

Resolved local bucket kegg:ppu03020 with 4 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 4

- rpoB: PP_0447 | Q88QP2 | DNA-directed RNA polymerase subunit beta (RNAP subunit beta) (EC 2.7.7.6) (RNA polymerase subunit beta) (Transcriptase subunit beta) (EC 2.7.7.6; primary bucket kegg:ppu03020)
- rpoC: PP_0448 | Q88QP1 | DNA-directed RNA polymerase subunit beta' (RNAP subunit beta') (EC 2.7.7.6) (RNA polymerase subunit beta') (Transcriptase subunit beta') (EC 2.7.7.6; primary bucket kegg:ppu03020)
- rpoA: PP_0479 | Q88QL1 | DNA-directed RNA polymerase subunit alpha (RNAP subunit alpha) (EC 2.7.7.6) (RNA polymerase subunit alpha) (Transcriptase subunit alpha) (EC 2.7.7.6; primary bucket kegg:ppu03020)
- rpoZ: PP_5301 | Q88C82 | DNA-directed RNA polymerase subunit omega (RNAP omega subunit) (EC 2.7.7.6) (RNA polymerase omega subunit) (Transcriptase subunit omega) (EC 2.7.7.6; primary bucket kegg:ppu03020)

## Generic Module Context

### Working Scope

Species-neutral bacterial module for the DNA-directed RNA polymerase core enzyme that carries out DNA-templated RNA synthesis. The conserved bacterial core enzyme is built from an alpha dimer, beta and beta-prime catalytic cleft subunits, and the omega assembly/stability subunit. This module deliberately stops at the core enzyme and excludes sigma factors, transcription elongation factors, and promoter-specific regulatory proteins.

### Provisional Biological Outline

- Bacterial DNA-directed RNA polymerase core enzyme
  - 1. alpha dimer assembly platform
  - RpoA alpha dimer platform
    - rpoA: RNA polymerase alpha subunit (molecular player: bacterial DNA-directed RNA polymerase alpha subunit family; activity or role: protein dimerization activity)
  - 2. beta and beta-prime catalytic cleft
  - RpoB/RpoC catalytic cleft
    - rpoB: RNA polymerase beta subunit (molecular player: DNA-directed RNA polymerase beta subunit family; activity or role: contributes to DNA-directed RNA polymerase activity)
    - rpoC: RNA polymerase beta-prime subunit (molecular player: bacterial DNA-directed RNA polymerase beta-prime subunit family; activity or role: contributes to DNA-directed RNA polymerase activity)
  - 3. omega assembly and stability subunit
  - RpoZ omega assembly/stability subunit
    - rpoZ: RNA polymerase omega subunit (molecular player: DNA-directed RNA polymerase omega subunit family; activity or role: contributes to DNA-directed RNA polymerase activity)

### Known Relationships Among Steps

- RpoA alpha dimer platform feeds into RpoB/RpoC catalytic cleft: The alpha dimer provides the assembly platform for recruitment of the beta and beta-prime subunits into the core enzyme.
- RpoZ omega assembly/stability subunit promotes RpoB/RpoC catalytic cleft: The omega subunit supports proper assembly and stability of the beta/beta-prime-containing core enzyme.

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

## Output

# Module Review: Bacterial DNA-directed RNA polymerase core enzyme in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Bucket:** kegg:ppu03020 "RNA polymerase" (module area: other_kegg_pathway)
**Module scope:** bacterial core enzyme α₂ββ'ω (excludes sigma factors, elongation factors, promoter-specific regulators)
**Overall verdict:** **Module fully COVERED — high confidence.** All four core subunits are present, single-copy, structurally intact, and syntenically corroborated.

---

## 1. Executive summary

The bacterial DNA-directed RNA polymerase (RNAP) core enzyme module is **completely satisfiable** in *P. putida* KT2440. All four expected steps map to unambiguous, high-confidence candidate genes:

| Module step | Gene | Locus | UniProt | KO | Length | Verdict |
|---|---|---|---|---|---|---|
| α-dimer assembly platform | rpoA | PP_0479 | Q88QL1 | K03040 | 333 aa | **covered** |
| β/β' catalytic cleft | rpoB | PP_0447 | Q88QP2 | K03043 | 1357 aa | **covered** |
| β/β' catalytic cleft | rpoC | PP_0448 | Q88QP1 | K03046 | 1399 aa | **covered** |
| ω assembly/stability | rpoZ | PP_5301 | Q88C82 | K03060 | 87 aa | **covered** |

Evidence is convergent across four independent lines: (i) canonical KEGG/UniProt orthology; (ii) complete, non-truncated Pfam/InterPro domain architectures including the intact catalytic **NADFDGD** Mg²⁺-triad in rpoC; (iii) strict single-copy status with no rpoC1/rpoC2 split; (iv) conserved operon synteny (β-operon, α-operon, rpoZ–spoT linkage). The only curation caveats are annotation-hygiene issues, not gaps: EC 2.7.7.6 / GO:0003899 is propagated as a complex-level attribute onto the non-catalytic subunits rpoA and rpoZ, and all four genes rest on homology-level evidence (protein-existence level 3) rather than direct KT2440 biochemistry. No module revision or new GO term is required.

---

## 2. Target-organism pathway definition

**Process included:** DNA-templated RNA synthesis by the bacterial RNAP **core enzyme** — the minimal catalytically competent assembly α₂ββ'ω that polymerizes ribonucleotides on a DNA template (EC 2.7.7.6). The α-dimer nucleates assembly; β and β' form the catalytic cleft housing the Mg²⁺ active center and the main/secondary channels; ω clamps β' and stabilizes the assembled enzyme.

**Boundaries — keep separate:**
- **Sigma factors** (promoter recognition; convert core → holoenzyme): rpoD/σ⁷⁰ (PP_0387, K03086), rpoN/σ⁵⁴ (PP_0952, K03092), rpoS/σ³⁸ (PP_1623, K03087), plus other ECF/alternative sigmas. These are *correctly excluded* from this bucket.
- **Elongation/anti-termination and cleavage factors** (GreA/B, NusA/G, Mfd, Rho) — separate.
- **Promoter-specific transcriptional regulators / stringent-response effectors** (DksA, RelA/SpoT) — separate, though rpoZ is genomically linked to spoT (see §5).
- **KEGG map03020** is a *pan-domain* reference map that also displays eukaryotic Pol I/II/III and archaeal RNAP subunits; only the four bacterial core KOs above are relevant to this organism. Do not import eukaryotic/archaeal subunit rows.

**Alternate names / database definitions:** "RNA polymerase" (KEGG ppu03020, DBLINK GO:0000428); GO:0000428 "DNA-directed RNA polymerase complex"; the core enzyme is EC 2.7.7.6 ("DNA-directed RNA polymerase"). Subunits are also referred to by their eukaryotic-homolog Pfam clans (Rpb1=β', Rpb2=β, Rpb3/Rpb11≈α, Rpb6=ω).

---

## 3. Expected step model

1. **RpoA α-dimer platform** — two α subunits dimerize via their N-terminal domains (αNTD) to form the assembly scaffold onto which β and β' are recruited; the α C-terminal domains (αCTD) are mobile and contact UP-element DNA and many activators.
2. **RpoB/RpoC catalytic cleft** — β (Rpb2 homolog) and β' (Rpb1 homolog) assemble on the α-dimer to build the crab-claw catalytic center; β' contributes the absolutely conserved NADFDGD aspartate triad that chelates the catalytic Mg²⁺, and an N-terminal Zn-binding domain.
3. **RpoZ ω assembly/stability subunit** — ω wraps around the β' C-terminus, chaperoning β' folding and stabilizing the assembled core.

All three steps are present and intact in KT2440 (§4).

---

## 4. Candidate genes and evidence

**rpoA — PP_0479 / Q88QL1 (K03040, 333 aa).** αNTD dimerization domain (PF01000) **and** αCTD (PF03118) both present → full-length, assembly-competent and regulation-competent. InterPro bacterial-α signatures (IPR011773). *Role:* assembly platform (GO:0046983 protein dimerization). *Evidence:* homology + domain architecture + α-operon synteny (rpsK–rpsD–**rpoA**–rplQ). *Caveat:* EC 2.7.7.6/GO:0003899 is a complex-level attribute, not individual catalysis. Single-copy. **Verdict: covered.**

**rpoB — PP_0447 / Q88QP2 (K03043, 1357 aa).** Complete Rpb2 domain set (PF04563/04561/04565/10385/00562/04560); length matches *E. coli* β (1342 aa). Harbors the rifampicin-binding pocket (clinically/experimentally validated target of rpoB mutations in *Pseudomonas*; PMID 35768665). *Role:* catalytic cleft. *Evidence:* homology + domain architecture + β-operon synteny (rplJ–rplL–**rpoB**–rpoC). Single-copy. **Verdict: covered.**

**rpoC — PP_0448 / Q88QP1 (K03046, 1399 aa).** Complete Rpb1 domain set (PF04997/00623/04983/05000/04998); bacterial-β' InterPro (IPR012754). **Intact catalytic NADFDGD Mg²⁺-triad at position 458** and N-terminal Zn-finger; UniProt records GO:0000287 (Mg²⁺) and GO:0008270 (Zn²⁺) binding. This is the strongest single indicator that the core is catalytically competent. *Evidence:* homology + motif + synteny. Single-copy; **no rpoC1/rpoC2 split.** **Verdict: covered.**

**rpoZ — PP_5301 / Q88C82 (K03060, 87 aa).** Clean Rpb6/omega domain (PF01192, IPR006110); length matches *E. coli* ω (91 aa). *Role:* assembly/stability chaperone of β'. *Evidence:* homology + domain + synteny (directly upstream of **spoT** PP_5302). Single-copy. *Caveat:* dual-function annotation — the assembly/stability role transfers strongly, but any ppGpp/stringent-response function is an **uncertain species transfer** (see §5). **Verdict: covered.**

**Evidence type for all four:** UniProt protein-existence level 3 ("Inferred from homology") — i.e., no published KT2440-specific protein-level biochemistry; annotations derive from HAMAP/UniRule orthology. This is expected and unproblematic for universal housekeeping genes, but it means direct target-organism experimental support is absent. **Organism-specific genetic support:** a genome-wide RB-TnSeq library in KT2440 disrupted "nearly all (4,778) non-essential genes" (PMID 33964456), operationally defining an essential-gene complement into which the obligatory RNAP core subunits fall — indirect but strain-specific evidence of indispensability that complements the homology annotations.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No true gaps.** Every module step is covered; no step is "missing but present under a different name." There is no lineage-specific replacement: Pseudomonas does not split rpoC (KEGG K13797/K13798 = 0 hits), unlike some cyanobacteria/*Helicobacter*.
- **Correctly absent (not_expected_in_target_taxon):** the Firmicutes/Gram-positive δ subunit (rpoE, K03048) has 0 hits in KT2440 — as expected for a Proteobacterium, whose core is α₂ββ'ω with no δ. Do not add a δ-subunit step for this organism.
- **Over-propagated catalytic annotation (benign):** EC 2.7.7.6 and molecular-function GO:0003899 ("DNA-directed RNA polymerase activity") are attached to **rpoA and rpoZ**, which have no independent nucleotidyl-transferase activity. This is a holoenzyme attribute mechanically inherited by every subunit. Prefer expressing it via complex membership (GO:0000428, `part_of`) or the `contributes_to` qualifier at the gene level.
- **Omega functional caveat (species transfer):** In *E. coli*, ω facilitates ppGpp binding and stringent-response control; but "key residues that facilitate ppGpp binding by ω are not conserved in *S. aureus*" and rpoZ deletion there caused "increased degradation and misfolding of the β' subunit … and a general dissociation of RNAP" (PMID 27799328). Thus the **assembly/stability** role is a strong transfer to KT2440; the **ppGpp-binding** role is uncertain and should not be asserted for PP_5301 without direct evidence. The genomic rpoZ–spoT adjacency is suggestive but not proof.
- **Homology-only evidence:** all four are protein-existence level 3; a skeptical reviewer would note there is no KT2440 knockout/biochemistry cited, only orthology + essentiality expectation.

---

## 6. Module and GO-curation recommendations

| Module step | Status | Rationale |
|---|---|---|
| RpoA α-dimer platform | **covered** | rpoA/PP_0479, αNTD+αCTD intact, single-copy |
| RpoB/RpoC catalytic cleft | **covered** | rpoB+rpoC, full domain sets, NADFDGD triad intact |
| RpoZ ω assembly/stability | **covered** | rpoZ/PP_5301, Rpb6 domain, single-copy |

- **Do not** mark any of the three module steps (α-platform, β/β' cleft, ω) as candidate_uncertain, gap, or not_expected_in_target_taxon — all three are covered. (Separately, the Firmicutes δ subunit is not a step in this Proteobacterial module and is correctly absent; see §5.)
- **Module boundaries are correct** for this organism — sigma factors, elongation factors, and stringent-response effectors are separate genes and rightly excluded. No `module_needs_revision`.
- **No new module document or GO-term request needed.** Existing GO terms suffice: GO:0000428 (complex), GO:0003899 (activity, complex-level), GO:0006351 (DNA-templated transcription), GO:0046983 (rpoA dimerization).
- **GO-hygiene recommendation:** for rpoA and rpoZ, annotate catalytic function with `contributes_to`/`part_of` rather than a direct GO:0003899 assertion, to avoid implying independent catalysis.

---

## 7. Genes to promote to full review

Priority is low — the module is unambiguous — but if a `fetch-gene` pass is run:

1. **rpoZ / PP_5301** *(highest value)* — smallest, most functionally variable subunit; resolve whether the *E. coli*-type ppGpp-binding residues are conserved and whether the rpoZ–spoT linkage implies a stringent-response role in KT2440. Recommended.
2. **rpoC / PP_0448** — confirm the NADFDGD active site and Zn-finger coordinates at residue level for the structural annotation record. Optional.
3. **rpoB / PP_0447** — document the rifampicin-resistance-determining region for antibiotic-resistance curation cross-links. Optional.
4. **rpoA / PP_0479** — lowest priority; annotation is unambiguous.

---

## 8. Key references

- Zhang G. *et al.* Crystal structure of *Thermus aquaticus* core RNA polymerase at 3.3 Å. **Cell** 98:811–824 (1999). PMID: 10499798. *(KEGG ppu03020 primary reference; core α₂ββ'ω architecture.)*
- Weiss A. *et al.* The ω subunit governs RNA polymerase stability and transcriptional specificity in *Staphylococcus aureus*. **J Bacteriol** (2017). PMID: 27799328. *(ω assembly/stability role; non-conservation of ppGpp-binding residues — species-transfer caveat.)*
- Khitiri *et al.* The ω subunit stabilizes transcribing RNA polymerase to balance processivity and collision resolution (2026). PMID: 42182183. *(Refined mechanistic role of ω.)*
- Alam K. *et al.* Rifampicin-resistant (rpoB) mutation in *Pseudomonas stutzeri* … (2022). PMID: 35768665. *(rpoB as validated rifampicin target in Pseudomonas.)*
- Cai *et al.* Novel antibiotic susceptibility of an RNA polymerase α-subunit mutant in *Pseudomonas aeruginosa* (2023). PMID: 37428003. *(rpoA αCTD functional relevance in Pseudomonas.)*
- Eng T. *et al.* Engineering *Pseudomonas putida* for efficient aromatic conversion … high-throughput screening in a bioreactor (2021). PMID: 33964456. *(Genome-wide RB-TnSeq library over ~4,778 non-essential genes → defines the essential complement containing RNAP core genes.)*
- UniProt: Q88QL1 (rpoA), Q88QP2 (rpoB), Q88QP1 (rpoC), Q88C82 (rpoZ). KEGG: ppu03020 and KOs K03040/K03043/K03046/K03060.

---

### Uncertainty statement
All four gene assignments rest on strong, convergent homology/orthology, domain-architecture, copy-number, and synteny evidence, but **no direct *P. putida* KT2440 protein-level experiment** was identified (protein-existence level 3). The core-enzyme catalytic competence is inferred from the intact NADFDGD/Zn-finger motifs. Species transfer is **strong** for all structural/assembly roles; it is **uncertain** only for the specific ppGpp-binding function of ω. Experiments that would close remaining gaps: a KT2440 rpoZ knockout (essentiality/stringent-response phenotype), and proteomic detection of all four subunits to raise evidence above homology level.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_rna_polymerase_core__ppu03020-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_rna_polymerase_core__ppu03020-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10499798
2. PMID:27799328
3. PMID:42182183
4. PMID:35768665
5. PMID:37428003
6. PMID:33964456