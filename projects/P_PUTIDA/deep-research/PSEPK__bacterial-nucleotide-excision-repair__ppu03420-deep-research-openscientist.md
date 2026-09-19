---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T13:50:27.631506'
end_time: '2026-08-08T14:12:49.233761'
duration_seconds: 1341.6
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: bacterial_nucleotide_excision_repair
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu03420
  pathway_id: ppu03420
  pathway_name: Nucleotide excision repair
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03420 with 10 primary genes; module
    area: nucleotide_metabolism.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '10'
  candidate_genes: '- polA: PP_0123 | Q88RK6 | DNA polymerase I (EC 2.7.7.7) (EC 2.7.7.7;
    primary bucket kegg:ppu03420)

    - uvrA: PP_0483 | Q88QK7 | UvrABC system protein A (UvrA protein) (Excinuclease
    ABC subunit A) (primary bucket kegg:ppu03420)

    - uvrB: PP_1974 | Q88LF9 | UvrABC system protein B (Protein UvrB) (Excinuclease
    ABC subunit B) (primary bucket kegg:ppu03420)

    - mfd: PP_2148 | Q88KZ1 | Transcription-repair-coupling factor (TRCF) (EC 3.6.4.-)
    (EC 3.6.4.-; primary bucket kegg:ppu03420)

    - PP_2839: PP_2839 | Q88J10 | Helicase ATP-binding domain-containing protein (primary
    bucket kegg:ppu03420)

    - PP_3087: PP_3087 | Q88IB2 | UvrABC system protein A (Excinuclease ABC subunit
    A) (primary bucket kegg:ppu03420)

    - uvrC: PP_4098 | Q88FJ7 | UvrABC system protein C (Protein UvrC) (Excinuclease
    ABC subunit C) (primary bucket kegg:ppu03420)

    - ligA: PP_4274 | Q88F25 | DNA ligase (EC 6.5.1.2) (Polydeoxyribonucleotide synthase
    [NAD(+)]) (EC 6.5.1.2; primary bucket kegg:ppu03420)

    - ligB: PP_4968 | Q88D59 | DNA ligase B (EC 6.5.1.2) (Polydeoxyribonucleotide
    synthase [NAD(+)] B) (EC 6.5.1.2; primary bucket kegg:ppu03420)

    - uvrD: PP_5352 | Q88C31 | DNA helicase II (EC 5.6.2.4) (DNA 3''-5'' helicase
    II) (EC 5.6.2.4; primary bucket kegg:ppu03420)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__bacterial-nucleotide-excision-repair__ppu03420-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial-nucleotide-excision-repair__ppu03420-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

bacterial_nucleotide_excision_repair in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03420
- Resolved ID: ppu03420
- Resolved name: Nucleotide excision repair
- Source: KEGG

Resolved local bucket kegg:ppu03420 with 10 primary genes; module area: nucleotide_metabolism.

## Candidate Genes From Local Metadata

Candidate gene count: 10

- polA: PP_0123 | Q88RK6 | DNA polymerase I (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03420)
- uvrA: PP_0483 | Q88QK7 | UvrABC system protein A (UvrA protein) (Excinuclease ABC subunit A) (primary bucket kegg:ppu03420)
- uvrB: PP_1974 | Q88LF9 | UvrABC system protein B (Protein UvrB) (Excinuclease ABC subunit B) (primary bucket kegg:ppu03420)
- mfd: PP_2148 | Q88KZ1 | Transcription-repair-coupling factor (TRCF) (EC 3.6.4.-) (EC 3.6.4.-; primary bucket kegg:ppu03420)
- PP_2839: PP_2839 | Q88J10 | Helicase ATP-binding domain-containing protein (primary bucket kegg:ppu03420)
- PP_3087: PP_3087 | Q88IB2 | UvrABC system protein A (Excinuclease ABC subunit A) (primary bucket kegg:ppu03420)
- uvrC: PP_4098 | Q88FJ7 | UvrABC system protein C (Protein UvrC) (Excinuclease ABC subunit C) (primary bucket kegg:ppu03420)
- ligA: PP_4274 | Q88F25 | DNA ligase (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)]) (EC 6.5.1.2; primary bucket kegg:ppu03420)
- ligB: PP_4968 | Q88D59 | DNA ligase B (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)] B) (EC 6.5.1.2; primary bucket kegg:ppu03420)
- uvrD: PP_5352 | Q88C31 | DNA helicase II (EC 5.6.2.4) (DNA 3'-5' helicase II) (EC 5.6.2.4; primary bucket kegg:ppu03420)

## Generic Module Context

### Working Scope

No module YAML was resolved; use the pathway and taxon context.

### Provisional Biological Outline

No module YAML outline available.

### Known Relationships Among Steps

No module YAML connections available.

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

# Species-Aware Review: Bacterial Nucleotide Excision Repair (NER) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Target bucket:** KEGG `ppu03420` — Nucleotide excision repair (module area: nucleotide_metabolism)
**Scope of evidence:** UniProtKB (Swiss-Prot + TrEMBL), KEGG orthology/genome context, and primary literature. All KT2440 protein annotations are homology-inferred (UniProt protein-existence level "Inferred from homology"); no direct KT2440 protein-level enzymatic assays exist in UniProt. Regulatory evidence is direct for KT2440 (PMID 17933893).

---

## 1. Executive summary

The **canonical bacterial NER pathway is complete and satisfiable** in *P. putida* KT2440. Every required step of the global-genome (GG-NER) and transcription-coupled (TC-NER) sub-pathways is encoded by a high-confidence gene: damage recognition (**UvrA** PP_0483, **UvrB** PP_1974), dual incision (**UvrC** PP_4098), damaged-oligonucleotide/UvrB turnover (**UvrD** PP_5352), repair-synthesis gap filling (**DNA Pol I** PP_0123), nick sealing (**LigA** PP_4274), and transcription–repair coupling (**Mfd** PP_2148).

Of the 10 genes in the KEGG bucket, **7 are core NER** and **3 are accessory or over-propagated** and should not be counted toward step satisfiability:
- **PP_2839** is a **DinG-family Fe–S helicase** placed in `ppu03420` only because KEGG maps it to the *eukaryotic* ERCC2/XPD node (KO K10844). Bacteria have no XPD/TFIIH NER step → **over-propagation / not_expected_in_target_taxon**.
- **PP_3087** is a **UvrA2 paralog** (shares KO K03701 with true UvrA but lacks NER/SOS GO terms; standalone locus) → **candidate_uncertain / accessory**.
- **ligB (PP_4968)** is a **LigB-subfamily** secondary NAD⁺-ligase (KEGG primary pathway = DNA replication) → **candidate_uncertain**; LigA is the functional NER ligase.

No **Cho** alternative 3′-endonuclease is present (single UvrC). The module boundary should exclude the LexA2-controlled **imuABC/dnaE2** translesion-mutagenesis branch, which is a distinct pathway in KT2440.

**Overall module verdict: COVERED** (all core steps satisfied), with three flagged annotations for cleanup.

---

## 2. Target-organism pathway definition

**Process included.** Bacterial NER is the UvrABC excinuclease system that recognizes and removes **helix-distorting, bulky DNA lesions** (UV cyclobutane pyrimidine dimers and (6–4) photoproducts, intrastrand crosslinks, bulky chemical adducts) by excising a **short 12–13 nt damage-containing oligonucleotide**, followed by repair synthesis and ligation (PMID 35149830). Two entry modes converge on the same UvrBC incision machinery:
- **Global-genome NER (GG-NER):** UvrA₂B₂ scans duplex DNA for distortions.
- **Transcription-coupled NER (TC-NER):** **Mfd** recognizes RNA-polymerase stalled at a template-strand lesion, dislodges it, and recruits Uvr(A)BC (PMID 33480355).

**Neighboring pathways to keep separate (do not merge into this bucket):**
- **Base excision repair (BER)** — glycosylase/AP-endonuclease-initiated removal of small/non-bulky base damage (KEGG ppu03410). Shares no core enzymes with NER.
- **Mismatch repair (MMR)** — MutS/MutL/UvrD (ppu03430). Note **UvrD/PcrA (PP_5352) is shared** between NER, MMR, and replication; it is not NER-exclusive.
- **DNA replication (ppu03030)** — the primary KEGG pathway for PolA (PP_0123), LigA (PP_4274), and LigB (PP_4968); these are shared enzymes.
- **SOS translesion mutagenesis** — LexA2-regulated **imuA–imuB–dnaE2** cassette and TLS polymerases; error-prone lesion *tolerance*, not excision. Must be excluded (PMID 17933893).
- **Global "DNA repair" overview maps** should not be conflated with the specific UvrABC excinuclease bucket.

**Alternate names / database definitions.** UvrABC endonuclease / excinuclease ABC / "excision nuclease" system; KEGG map 03420 is a **combined eukaryote+prokaryote map**, which is the direct cause of the ERCC2/XPD over-mapping (Section 5). GO anchor for the core process: **GO:0006289 nucleotide-excision repair**; TC-NER damage recognition: **GO:0000716**.

---

## 3. Expected step model (canonical bacterial NER)

| # | Step | Function | Expected enzyme/KO | Present in KT2440? |
|---|------|----------|--------------------|--------------------|
| 1 | Damage recognition (GG) | UvrA₂B₂ scans DNA; UvrA is ATPase/sensor | UvrA (K03701) | ✅ PP_0483 |
| 2 | Lesion verification / preincision | UvrB melts/probes strand, forms preincision complex | UvrB (K03702) | ✅ PP_1974 |
| 3 | Dual incision | UvrC cuts 3′ and 5′ of lesion | UvrC (K03703) | ✅ PP_4098 |
| 4 | Oligo + UvrB release | Helicase II unwinds the 12–13 nt fragment | UvrD (K03657) | ✅ PP_5352 |
| 5 | Repair synthesis | Gap filling | DNA Pol I (K02335) | ✅ PP_0123 |
| 6 | Nick sealing | NAD⁺-dependent ligation | LigA (K01972) | ✅ PP_4274 |
| 7 | Transcription coupling (TC) | Remove stalled RNAP, recruit UvrAB | Mfd/TRCF (K03723) | ✅ PP_2148 |
| — | *Alt. 3′ incision* | Cho endonuclease (some bacteria) | Cho (K19226) | ❌ absent (not required) |
| — | *XPD/ERCC2 helicase* | eukaryotic TFIIH only | K10844 | ❌ not applicable to bacteria |

All seven core steps are covered. Steps 5 and 6 are enzymatically shared with replication but are the accepted NER repair-synthesis/ligation activities.

---

## 4. Candidate genes and evidence

**High-confidence core NER genes (Swiss-Prot, HAMAP-ruled unless noted):**

- **uvrA — PP_0483 / Q88QK7** (944 aa; K03701). UvrABC subunit A, ATPase/DNA-binding damage sensor. Keywords include *SOS response*, *Zinc-finger*; GO:0006289 + GO:0009432. **Role: primary GG-NER damage recognition. Caveat: none — unambiguous. Evidence: homology (strong family assignment).**
- **uvrB — PP_1974 / Q88LF9** (671 aa). UvrB family; forms preincision complex; GO:0006289. **Role: lesion verification. Caveat: none.**
- **uvrC — PP_4098 / Q88FJ7** (607 aa). UvrC family; N-terminal 3′ incision, C-terminal 5′ incision; GO:0006289. **Role: dual incision. Caveat: single copy — no Cho backup.** *(Note: neighboring PP_4099 "uvrY" is actually GacA response regulator — a gene-name artifact, NOT NER.)*
- **mfd — PP_2148 / Q88KZ1** (1149 aa; K03723; EC 5.6.2.4). TRCF; N-terminal UvrB-homology module + C-terminal RecG-like helicase; GO:0000716. **Role: transcription-coupled NER. Caveat: none; well-conserved.**
- **uvrD — PP_5352 / Q88C31** (728 aa; K03657; EC 5.6.2.4). UvrD/helicase II subfamily (TrEMBL). **Role: unwinds excised oligo + displaces UvrB. Caveat: pleiotropic — also functions in MMR and replication; not NER-exclusive.**
- **polA — PP_0123 / Q88RK6** (915 aa; K02335; EC 2.7.7.7; TrEMBL). Pol I with 5′→3′ and 3′→5′ exonuclease. **Role: NER repair synthesis. Caveat: primary role/KEGG pathway is replication; shared enzyme.**
- **ligA — PP_4274 / Q88F25** (776 aa; K01972; EC 6.5.1.2; LigA subfamily). NAD⁺-dependent ligase, "essential for DNA replication and repair." **Role: NER nick sealing. Caveat: essential, shared with replication; this is the functional NER ligase.**

**Accessory / flagged genes:**

- **PP_2839 / Q88J10** (762 aa). KEGG KO **K10844 (ERCC2/XPD, EC 5.6.2.3)**; UniProt = **helicase, DinG subfamily**, 4Fe–4S cluster; GO only 0006281 (generic DNA repair). Standalone locus. **Assessment: DinG R-loop helicase (PMID 24738733); over-propagated to NER via the eukaryotic XPD node.**
- **PP_3087 / Q88IB2** (838 aa). KO K03701 (same as UvrA) but **UvrA2 paralog**: TrEMBL, no SOS keyword, no GO:0006289 (only 0006281). Standalone, adjacent to ECF sigma-70 factor PP_3086 (not a uvrA2B2 operon). **Assessment: accessory/stress-associated UvrA paralog; not the primary sensor.**
- **ligB — PP_4968 / Q88D59** (566 aa; K01972; LigB subfamily MF_01587). KEGG primary pathway = DNA replication (ppu03030). **Assessment: secondary ligase of uncertain function; LigA is the NER ligase.**

**Evidence type across all genes:** homology-based (UniProt "Inferred from homology"); family/KO assignments are unambiguous for the 7 core genes. Regulatory embedding (SOS/LexA1) is directly demonstrated in KT2440 (PMID 17933893).

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Over-propagation #1 (structural artifact of KEGG's combined map): PP_2839 → ERCC2/XPD.** KEGG map 03420 contains eukaryotic TFIIH nodes; the bacterial DinG helicase (KO K10844) is auto-slotted there. Bacterial UvrABC NER has **no XPD/ERCC2/TFIIH step**. DinG's real characterized function is **R-loop resolution and Fe–S redox coordination with BER** (PMID 24738733). → Mark the XPD/ERCC2 step **not_expected_in_target_taxon**; PP_2839 is **not** an NER step.
- **Paralog over-count #2: PP_3087 (UvrA2).** Sharing KO K03701 inflates the UvrA step to two genes. Only PP_0483 carries the NER/SOS annotation signature; PP_3087 lacks it and sits in a non-operonic, sigma-factor-adjacent context. → Keep **one** covered UvrA (PP_0483); PP_3087 = **candidate_uncertain**.
- **Enzyme-family over-count #3: ligB (PP_4968).** Two LigA/LigB genes share KO K01972. LigA (essential) is the NER ligase; LigB is a secondary ligase whose KEGG primary bucket is replication. → Keep **one** covered ligase (LigA); ligB = **candidate_uncertain**.
- **Shared-enzyme caveats:** UvrD, PolA, and LigA are pleiotropic (MMR/replication). They legitimately serve NER but should be cross-annotated, not treated as NER-exclusive markers.
- **True gap check — none critical.** Cho (alternative 3′ endonuclease) is **absent**, but Cho is dispensable where UvrC is intact, so this is **not a gap**. No core step is missing.
- **Boundary error to avoid:** do not absorb the LexA2 **imuA–imuB–dnaE2** SOS-mutagenesis cassette or TLS polymerases into this bucket — that is a separate lesion-tolerance pathway in KT2440 (PMID 17933893).

---

## 6. Module and GO-curation recommendations

**Per-step module status:**

| Module step | Gene | Status |
|-------------|------|--------|
| UvrA damage recognition | PP_0483 | **covered** |
| UvrB verification | PP_1974 | **covered** |
| UvrC dual incision | PP_4098 | **covered** |
| UvrD oligo release | PP_5352 | **covered** (shared enzyme) |
| Pol I repair synthesis | PP_0123 | **covered** (shared enzyme) |
| LigA nick sealing | PP_4274 | **covered** (shared enzyme) |
| Mfd TC-NER coupling | PP_2148 | **covered** |
| UvrA2 paralog | PP_3087 | **candidate_uncertain** (accessory) |
| Secondary ligase | PP_4968 (ligB) | **candidate_uncertain** |
| ERCC2/XPD (DinG) | PP_2839 | **not_expected_in_target_taxon** (over-propagated) |

**Module verdict:** **COVERED** — the module is satisfiable without any of the three flagged genes.

**Module boundary / revision:** The generic KEGG bucket is broadly correct but imports a **eukaryote-only step (XPD/ERCC2)** that is meaningless for bacteria — **module_needs_revision** to (a) drop the ERCC2/XPD node for prokaryotic taxa, and (b) demote PP_3087/ligB from primary NER membership.

**GO-curation actions:**
- **Remove/avoid GO:0006289** propagation to **PP_2839** (DinG); prefer R-loop/helicase terms (e.g., GO:0004386 helicase activity, GO:0051880/GO:0000737-type processes as appropriate) — flag for manual review.
- **PP_3087:** retain generic GO:0006281 unless experimental UvrA2 evidence appears; do not assign GO:0006289 by paralogy alone.
- **PP_4968 (ligB):** keep GO:0006281/0006260; do not assert NER-specific GO without evidence.
- Core seven genes: GO:0006289 (and GO:0000716 for Mfd) assignments are appropriate.
- No new module document is required, but a **prokaryote-specific NER module** (UvrABCD + PolA + LigA + Mfd, excluding XPD/ERCC2) would prevent recurrent over-propagation across Gram-negative genomes.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_2839 (DinG helicase)** — **highest priority.** Resolve the ERCC2/XPD mis-mapping; confirm DinG identity and reassign out of NER. Directly affects module boundary correctness.
2. **PP_3087 (UvrA2)** — verify paralog status, operon context, and any stress/resistance phenotype; decide accessory vs. redundant.
3. **PP_4968 (ligB)** — confirm LigB-subfamily assignment and non-NER primary role; keep as secondary ligase.
4. *(Optional)* **PP_5352 (uvrD)** — TrEMBL entry shared across NER/MMR; a review would document multi-pathway membership cleanly.

---

## 8. Key references

- **PMID 35149830** — Seck et al. (2022), *Nucleic Acids Res.*-adjacent. In vitro reconstitution of *Deinococcus radiodurans* UvrABC NER; defines the sequential UvrA/B/C action releasing a 12–13 nt fragment. *(Related-organism mechanism; strong transfer to KT2440 for core steps.)*
- **PMID 33480355** — Kang et al. (2021). Cryo-EM of Mfd disrupting stalled transcription complexes; Mfd removes stalled RNAP and recruits Uvr(A)BC. *(Mechanistic; strong transfer.)*
- **PMID 38513450** — Kaja et al. (2024). Single-molecule test of Mfd- vs UvrD-dependent TC-NER models in *E. coli*. *(Mechanistic context for coupling factors.)*
- **PMID 24738733** — Grodick et al. (2014), *Cell*. DinG is an ATP-dependent, 4Fe–4S R-loop-repair helicase coordinating with EndoIII via DNA charge transport. *(Basis for excluding PP_2839 from NER.)*
- **PMID 17933893** — Abella et al. (2007), *J. Bacteriol.* **Direct KT2440 evidence:** dual LexA regulons; LexA1 = conventional SOS response, LexA2 = imuA/imuB/dnaE2 mutagenesis cassette. *(Defines module boundary and regulatory context.)*
- **Databases:** UniProtKB entries Q88QK7, Q88LF9, Q88FJ7, Q88KZ1, Q88C31, Q88RK6, Q88F25 (core); Q88J10, Q88IB2, Q88D59 (flagged). KEGG `ppu03420` and KO assignments K03701/K03702/K03703/K03657/K02335/K01972/K03723/K10844.

---

### Limitations
- All KT2440 protein annotations are homology-inferred; no strain-specific enzymatic or knockout data for NER components were located in this review (the strongest KT2440-direct evidence is regulatory, PMID 17933893).
- UvrB/UvrC KO numbers (K03702/K03703) are stated from canonical NER conventions; the KEGG bucket was verified for all 10 candidates but per-gene KO for uvrB/uvrC was not separately re-queried.
- UvrA2 (PP_3087) function is inferred from the general bacterial UvrA2 pattern and local genomic context, not from KT2440 experiments.

### Future experiments / expert questions
- KT2440 knockout/UV-survival phenotyping of *uvrA (PP_0483)* vs *uvrA2 (PP_3087)*, and of *ligA* vs *ligB*, to resolve functional redundancy.
- ChIP/transcriptomics to confirm LexA1-dependent SOS induction of *uvrA/uvrB/uvrD* in KT2440.
- Biochemical confirmation that PP_2839 is a DinG R-loop helicase (Fe–S, 5′→3′) and lacks UvrABC-associated activity.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial-nucleotide-excision-repair__ppu03420-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial-nucleotide-excision-repair__ppu03420-deep-research-openscientist_artifacts/final_report.pdf)