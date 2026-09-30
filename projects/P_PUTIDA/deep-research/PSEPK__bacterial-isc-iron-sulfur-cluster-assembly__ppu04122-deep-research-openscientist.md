---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-12T22:54:50.393183'
end_time: '2026-08-12T23:04:59.418237'
duration_seconds: 609.03
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: bacterial_isc_iron_sulfur_cluster_assembly
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu04122
  pathway_id: ppu04122
  pathway_name: Sulfur relay system
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu04122 with 19 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '22'
  candidate_genes: '- moeB: PP_0735 | Q88PW3 | Molybdopterin-synthase adenylyltransferase
    (EC 2.7.7.80) (MoaD protein adenylase) (Molybdopterin-converting factor subunit
    1 adenylase) (Sulfur carrier protein MoaD adenylyltransferase) (EC 2.7.7.80; primary
    bucket kegg:ppu04122)

    - iscS: PP_0842 | Q88PK8 | Cysteine desulfurase IscS (EC 2.8.1.7) (EC 2.8.1.7;
    primary bucket kegg:ppu00730)

    - tusA-I: PP_1233 | Q88NH6 | Sulfurtransferase (EC 2.8.1.-) (EC 2.8.1.-; primary
    bucket kegg:ppu04122)

    - moaC: PP_1292 | Q88NC0 | Cyclic pyranopterin monophosphate synthase (EC 4.6.1.17)
    (Molybdenum cofactor biosynthesis protein C) (EC 4.6.1.17; primary bucket kegg:ppu04122)

    - moaD: PP_1293 | Q88NB9 | Molybdopterin synthase sulfur carrier subunit (primary
    bucket kegg:ppu04122)

    - moaE: PP_1294 | Q88NB8 | Molybdopterin synthase catalytic subunit (EC 2.8.1.12)
    (MPT synthase subunit 2) (Molybdenum cofactor biosynthesis protein E) (Molybdopterin-converting
    factor large subunit) (Molybdopterin-converting factor subunit 2) (EC 2.8.1.12;
    primary bucket kegg:ppu04122)

    - PP_1969: PP_1969 | Q88LG4 | Molybdenum cofactor biosynthesis protein A (primary
    bucket kegg:ppu04122)

    - tusA: PP_2116 | Q88L21 | Sulfur carrier protein TusA (primary bucket kegg:ppu04122)

    - moaB-I: PP_2122 | Q88L15 | Molybdenum cofactor biosynthesis protein B (primary
    bucket kegg:ppu04122)

    - iscS-II: PP_2435 | Q88K56 | cysteine desulfurase (EC 2.8.1.7) (EC 2.8.1.7; primary
    bucket kegg:ppu00730)

    - PP_2482: PP_2482 | Q88K11 | Molybdenum cofactor biosynthesis protein A (primary
    bucket kegg:ppu04122)

    - tusD: PP_3993 | Q88FT9 | Sulfur transfer protein complex, TusD subunit (primary
    bucket kegg:ppu04122)

    - PP_3994: PP_3994 | Q88FT8 | tRNA 5-methylaminomethyl-2-thiouridine synthase
    (TusC-like) (primary bucket kegg:ppu04122)

    - PP_3995: PP_3995 | Q88FT7 | Sulfurtransferase complex subunit TusB (primary
    bucket kegg:ppu04122)

    - tusE: PP_3996 | Q88FT6 | Sulfurtransferase (EC 2.8.1.-) (EC 2.8.1.-; primary
    bucket kegg:ppu04122)

    - mnmA: PP_4014 | Q88FR9 | tRNA-specific 2-thiouridylase MnmA (EC 2.8.1.13) (EC
    2.8.1.13; primary bucket kegg:ppu04122)

    - moaA: PP_4597 | Q88E69 | GTP 3'',8-cyclase (EC 4.1.99.22) (Molybdenum cofactor
    biosynthesis protein A) (EC 4.1.99.22; primary bucket kegg:ppu04122)

    - moaB-II: PP_4600 | Q88E67 | Molybdenum cofactor biosynthesis protein B (primary
    bucket kegg:ppu04122)

    - rhdA: PP_4907 | Q88DC0 | Sulfurtransferase (primary bucket kegg:ppu04122)

    - thiI: PP_5045 | Q88CY4 | tRNA sulfurtransferase (EC 2.8.1.4) (Sulfur carrier
    protein ThiS sulfurtransferase) (Thiamine biosynthesis protein ThiI) (tRNA 4-thiouridine
    synthase) (EC 2.8.1.4; primary bucket kegg:ppu00730)

    - PP_5105: PP_5105 | Q88CS5 | Sulfur carrier protein ThiS (primary bucket kegg:ppu04122)

    - sseA: PP_5118 | Q88CR2 | 3-mercaptopyruvate sulfurtransferase (EC 2.8.1.2) (EC
    2.8.1.2; primary bucket kegg:ppu04122)'
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
  path: PSEPK__bacterial-isc-iron-sulfur-cluster-assembly__ppu04122-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial-isc-iron-sulfur-cluster-assembly__ppu04122-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

bacterial_isc_iron_sulfur_cluster_assembly in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu04122
- Resolved ID: ppu04122
- Resolved name: Sulfur relay system
- Source: KEGG

Resolved local bucket kegg:ppu04122 with 19 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 22

- moeB: PP_0735 | Q88PW3 | Molybdopterin-synthase adenylyltransferase (EC 2.7.7.80) (MoaD protein adenylase) (Molybdopterin-converting factor subunit 1 adenylase) (Sulfur carrier protein MoaD adenylyltransferase) (EC 2.7.7.80; primary bucket kegg:ppu04122)
- iscS: PP_0842 | Q88PK8 | Cysteine desulfurase IscS (EC 2.8.1.7) (EC 2.8.1.7; primary bucket kegg:ppu00730)
- tusA-I: PP_1233 | Q88NH6 | Sulfurtransferase (EC 2.8.1.-) (EC 2.8.1.-; primary bucket kegg:ppu04122)
- moaC: PP_1292 | Q88NC0 | Cyclic pyranopterin monophosphate synthase (EC 4.6.1.17) (Molybdenum cofactor biosynthesis protein C) (EC 4.6.1.17; primary bucket kegg:ppu04122)
- moaD: PP_1293 | Q88NB9 | Molybdopterin synthase sulfur carrier subunit (primary bucket kegg:ppu04122)
- moaE: PP_1294 | Q88NB8 | Molybdopterin synthase catalytic subunit (EC 2.8.1.12) (MPT synthase subunit 2) (Molybdenum cofactor biosynthesis protein E) (Molybdopterin-converting factor large subunit) (Molybdopterin-converting factor subunit 2) (EC 2.8.1.12; primary bucket kegg:ppu04122)
- PP_1969: PP_1969 | Q88LG4 | Molybdenum cofactor biosynthesis protein A (primary bucket kegg:ppu04122)
- tusA: PP_2116 | Q88L21 | Sulfur carrier protein TusA (primary bucket kegg:ppu04122)
- moaB-I: PP_2122 | Q88L15 | Molybdenum cofactor biosynthesis protein B (primary bucket kegg:ppu04122)
- iscS-II: PP_2435 | Q88K56 | cysteine desulfurase (EC 2.8.1.7) (EC 2.8.1.7; primary bucket kegg:ppu00730)
- PP_2482: PP_2482 | Q88K11 | Molybdenum cofactor biosynthesis protein A (primary bucket kegg:ppu04122)
- tusD: PP_3993 | Q88FT9 | Sulfur transfer protein complex, TusD subunit (primary bucket kegg:ppu04122)
- PP_3994: PP_3994 | Q88FT8 | tRNA 5-methylaminomethyl-2-thiouridine synthase (TusC-like) (primary bucket kegg:ppu04122)
- PP_3995: PP_3995 | Q88FT7 | Sulfurtransferase complex subunit TusB (primary bucket kegg:ppu04122)
- tusE: PP_3996 | Q88FT6 | Sulfurtransferase (EC 2.8.1.-) (EC 2.8.1.-; primary bucket kegg:ppu04122)
- mnmA: PP_4014 | Q88FR9 | tRNA-specific 2-thiouridylase MnmA (EC 2.8.1.13) (EC 2.8.1.13; primary bucket kegg:ppu04122)
- moaA: PP_4597 | Q88E69 | GTP 3',8-cyclase (EC 4.1.99.22) (Molybdenum cofactor biosynthesis protein A) (EC 4.1.99.22; primary bucket kegg:ppu04122)
- moaB-II: PP_4600 | Q88E67 | Molybdenum cofactor biosynthesis protein B (primary bucket kegg:ppu04122)
- rhdA: PP_4907 | Q88DC0 | Sulfurtransferase (primary bucket kegg:ppu04122)
- thiI: PP_5045 | Q88CY4 | tRNA sulfurtransferase (EC 2.8.1.4) (Sulfur carrier protein ThiS sulfurtransferase) (Thiamine biosynthesis protein ThiI) (tRNA 4-thiouridine synthase) (EC 2.8.1.4; primary bucket kegg:ppu00730)
- PP_5105: PP_5105 | Q88CS5 | Sulfur carrier protein ThiS (primary bucket kegg:ppu04122)
- sseA: PP_5118 | Q88CR2 | 3-mercaptopyruvate sulfurtransferase (EC 2.8.1.2) (EC 2.8.1.2; primary bucket kegg:ppu04122)

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

# Species-Aware Review: Bacterial ISC Iron–Sulfur Cluster Assembly in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Commissioned topic:** `bacterial_isc_iron_sulfur_cluster_assembly`
**Resolved bucket:** KEGG `ppu04122` "Sulfur relay system" (22 candidate genes)
**Prepared:** Iteration 3 of a 3-iteration autonomous review

---

## 1. Executive summary

**The review topic and the resolved gene bucket describe two different modules.** The commissioned
topic is *ISC iron–sulfur cluster assembly* (the `iscRSUA–hscBA–fdx` machinery that builds [2Fe-2S]/[4Fe-4S]
cofactors), but the resolved KEGG bucket `ppu04122` is the **"Sulfur relay system"** — a distinct KEGG map
covering **tRNA thiolation** (2-thiouridine, 4-thiouridine) and **molybdenum-cofactor (Moco)/thiamine sulfur
transfer**. The only node shared by both is the cysteine desulfurase **IscS (PP_0842)**, which is the sulfur-mobilizing
hub feeding both processes. This is the single most important curation conclusion: **the bucket is the wrong gene
source for an ISC review** and needs to be split.

Key results (all from UniProt proteome UP000000556 + InterPro/Pfam signatures, corroborated by literature):

1. **The ISC module IS satisfiable in PSEPK.** A complete, contiguous canonical operon exists at
   **PP_0841–PP_0847** = `iscR–iscS–iscU–iscA–hscB–hscA–fdx`. Six of these seven genes are **absent from the
   candidate list** (only `iscS` PP_0842 is included).
2. **No SUF system.** `sufABCDSE` is absent; ISC is the **sole** Fe–S biogenesis machinery in PSEPK (contrast
   with *E. coli*, which has both ISC and stress-inducible SUF). A SUF module step should be marked
   `not_expected_in_target_taxon`.
3. **The `ppu04122` bucket itself is largely well-populated** for the sulfur-relay/Moco processes it actually
   represents (tRNA 2-thiouridine relay complete; Moco and thiamine sulfur carriers present), **but contains
   over-propagated MoaA annotations** (PP_1969, PP_2482) and desulfurase/TusA paralog ambiguity.

**Bottom line for curators:** mark ISC as `covered` using PP_0841–PP_0847 (add the 6 missing genes), mark SUF
`not_expected_in_target_taxon`, and flag `ppu04122` as `module_needs_revision` (split ISC vs. sulfur-relay vs. Moco).

---

## 2. Target-organism pathway definition

**ISC iron–sulfur cluster assembly (the commissioned topic).** The housekeeping bacterial pathway that assembles
nascent [2Fe-2S]/[4Fe-4S] clusters and delivers them to apoproteins. Mechanistically: iron binds the scaffold
**IscU**; the cysteine desulfurase **IscS** inserts persulfide sulfur; the ferredoxin **Fdx** reduces persulfide to
sulfide, producing a [1Fe-1S] precursor; two precursors fuse on an IscU dimer to a bridging [2Fe-2S] cluster; the
**HscA/HscB** chaperone/co-chaperone pair drives ATP-dependent cluster transfer; **IscA** acts as an A-type
carrier/alternate scaffold; **IscR** (Rrf2-family, [2Fe-2S]-sensing) transcriptionally regulates the operon
(PMID 39870763; PMID 39632806).

**What to keep separate (neighbouring maps / broad overviews):**
- **KEGG `ppu04122` "Sulfur relay system"** — tRNA thiolation + Moco/thiamine sulfur transfer. *This is the resolved
  bucket, and it is NOT the ISC pathway.* Keep separate.
- **KEGG `ppu00730` "Thiamine metabolism"** and Moco biosynthesis (KEGG module M00880) — downstream sulfur users.
- **SUF system** (`sufABCDSE`) — the alternative Fe–S assembly pathway; **absent** in PSEPK.
- **CIA / NIF systems** — eukaryotic cytosolic and nitrogen-fixation-specific Fe–S systems; not applicable.

**Alternate names / DB definitions:** ISC = "iron–sulfur cluster" system; operon genes also appear as
`isc`/`nifU`-like (IscU carries the NifU_N domain) and `hsc` (Hsp70-class chaperones). KEGG places `iscS` under
sulfur/relay metabolism, which is why it — and not the rest of the operon — leaked into the `ppu04122` bucket.

---

## 3. Expected step model (ISC) and status in PSEPK

| ISC step | Expected gene | PSEPK locus | UniProt | Evidence (domain signature) | Status |
|---|---|---|---|---|---|
| Cysteine desulfurase (S donor) | iscS | **PP_0842** | Q88PK8 | Aminotran_5; Cys desulfurase; EC 2.8.1.7 | `covered` (in bucket) |
| Scaffold | iscU | **PP_0843** | Q88PK7 | NifU_N; IPR011339 ISCU | `covered` (missing from bucket) |
| A-type carrier | iscA | **PP_0844** | Q88PK6 | Fe-S_biosyn; IPR011302 IscA_proteobact | `covered` (missing) |
| Co-chaperone (J-protein) | hscB | **PP_0845** | Q88PK5 | DnaJ + HSCB_C; IPR004640 HscB | `covered` (missing) |
| Chaperone (Hsp70) | hscA | **PP_0846** | Q88PK4 | HSP70; IPR042039 HscA_NBD | `covered` (missing) |
| Ferredoxin (e⁻ donor) | fdx | **PP_0847** | Q88PK3 | Fer2; IPR011536 **Fdx_isc** | `covered` (missing) |
| Regulator ([2Fe-2S] sensor) | iscR | **PP_0841** | Q88PK9 | Rrf2; IPR010242 **TF_HTH_IscR** | `covered` (missing) |
| Alternative assembly system | suf operon | — | — | 0 hits for sufABCDSE | `not_expected_in_target_taxon` |

Gene order PP_0841→PP_0847 reproduces the textbook `iscR-iscS-iscU-iscA-hscB-hscA-fdx` operon, giving strong
**direct genomic (species-specific)** support that the ISC module is complete and satisfiable.

---

## 4. Candidate genes and evidence (the `ppu04122` bucket, 22 genes)

Evidence type is **homology/domain-signature** unless noted; all loci are direct PSEPK sequences from proteome
UP000000556. None of the candidate genes below are ISC-assembly genes except `iscS`.

**A. Sulfur donor / hub**
- **iscS PP_0842 (Q88PK8)** — Cysteine desulfurase, EC 2.8.1.7. The shared hub for ISC assembly, tRNA thiolation,
  and Moco/thiamine. High confidence. *Only bucket gene that is also an ISC gene.*

**B. tRNA 2-thiouridine (mnm⁵s²U34) relay — complete**
- **tusA PP_2116 (Q88L21)** — TusA sulfur carrier (IPR022931, specific). High confidence.
- **tusB PP_3995 / tusC PP_3994 / tusD PP_3993 (Q88FT7/FT8/FT9)** — TusBCD (DsrEFH-like: DsrH/DsrF/DsrE). Clustered
  PP_3993–3996 → strong operon support. Note the DsrEFH family also functions in sulfur oxidation in other taxa, but
  in this non-sulfur-oxidizer the genomic context supports the TusBCD (tRNA) assignment.
- **tusE PP_3996 (Q88FT6)** — DsrC/TusE (IPR007453). High confidence.
- **mnmA PP_4014 (Q88FR9)** — tRNA 2-thiouridylase, EC 2.8.1.13. Terminal transferase. High confidence.
  Relay architecture (IscS→TusA→TusBCD→TusE→MnmA) is directly supported by *E. coli* biochemistry (PMID 16387657).

**C. 4-thiouridine / thiamine sulfur transfer**
- **thiI PP_5045 (Q88CY4)** — tRNA sulfurtransferase / 4-thiouridine synthase, EC 2.8.1.4. High confidence.
- **thiS PP_5105 (Q88CS5)** — ThiS sulfur carrier (ThiS/MoaD-like, β-grasp). High confidence for thiamine branch.

**D. Molybdenum-cofactor (Moco) sulfur transfer & synthesis**
- **moeB PP_0735 (Q88PW3)** — MoaD adenylyltransferase, EC 2.7.7.80. High confidence.
- **moaC PP_1292 (Q88NC0)** — cyclic pyranopterin monophosphate synthase, EC 4.6.1.17. High confidence.
- **moaD PP_1293 (Q88NB9) / moaE PP_1294 (Q88NB8)** — molybdopterin synthase (sulfur carrier + catalytic, EC 2.8.1.12).
  High confidence; MoaD is a β-grasp sulfur carrier analogous to ThiS.
- **moaA PP_4597 (Q88E69)** — GTP 3',8-cyclase, EC 4.1.99.22; carries the **MoaA-specific** IPR013483 + IPR000385.
  High confidence — the bona fide MoaA.
- **moaB PP_2122 (Q88L15) & PP_4600 (Q88E67)** — two MoaB paralogs (IPR013484 MoaB_proteobac). Genuine paralogy.

**E. Over-propagated / ambiguous within the bucket**
- **PP_1969 (Q88LG4) & PP_2482 (Q88K11)** — annotated "Molybdenum cofactor biosynthesis protein A" but carry only
  generic **MoaA-like** radical-SAM signatures (IPR040064, IPR010505), **no EC**, and **not** the MoaA-specific
  IPR013483 held by PP_4597. **Likely over-propagated** → `candidate_uncertain`.
- **tusA-I PP_1233 (Q88NH6)** — only generic TusA-like (IPR001455), not the specific TusA IPR022931 of PP_2116.
  Possible non-relay TusA/YeeD-like paralog → `candidate_uncertain`.
- **iscS-II PP_2435 (Q88K56)** — a second generic cysteine desulfurase (IPR016454). Role unassigned.
- **rhdA PP_4907 (Q88DC0)** — single-domain rhodanese (thiosulfate sulfurtransferase), broad EC 2.8.1.-. Generic.
- **sseA PP_5118 (Q88CR2)** — 3-mercaptopyruvate sulfurtransferase (TST/MPST-like), EC 2.8.1.2. Generic.

**Not in the bucket but present in the genome (SufS-clade):**
- **CsdA (Q9Z408)** — "Probable cysteine desulfurase," SufS/CsdA clade (**IPR010970 Cys_dSase_SufS**), present
  **despite absence of a SUF scaffold**; likely a Moco/tRNA CsdA-type desulfurase. Needs role assignment.

---

## 5. Gaps, ambiguities, and likely over-annotations

1. **ISC genes missing from the bucket (biggest gap).** iscR/iscU/iscA/hscB/hscA/fdx (PP_0841, PP_0843–PP_0847)
   are all present in PSEPK but absent from `ppu04122`. The topic-vs-bucket mismatch, not a biological gap, is the cause.
2. **MoaA over-propagation.** PP_1969, PP_2482 lack MoaA-specific signatures/EC — probably not GTP 3',8-cyclases.
3. **Desulfurase paralogy (3 enzymes).** IscS (PP_0842), PP_2435, and SufS-clade CsdA (Q9Z408). Broad EC 2.8.1.7
   invites over-propagation; specific roles (ISC vs. relay vs. Moco/CsdA) are not resolvable from annotation alone.
4. **TusA paralogy.** PP_2116 (bona fide) vs. PP_1233 (generic TusA-like).
5. **DsrEFH ambiguity.** TusBCD (PP_3993–3995) belong to the DsrEFH superfamily used for sulfur oxidation in other
   lineages; assignment as tRNA-thiolation TusBCD rests on genomic clustering and homology, not direct PSEPK assay.
6. **No SUF backup.** Fe–S biogenesis depends solely on ISC — a genuine lineage feature, not a metadata gap.

---

## 6. Module and GO-curation recommendations

- **ISC Fe–S assembly module:** mark **`covered`**. Add/assert PP_0841 (iscR), PP_0843 (iscU), PP_0844 (iscA),
  PP_0845 (hscB), PP_0846 (hscA), PP_0847 (fdx); iscS = PP_0842. Consider creating a dedicated **ISC module document**
  (`iscRSUA-hscBA-fdx`) rather than relying on the KEGG sulfur-relay bucket.
- **SUF assembly step:** mark **`not_expected_in_target_taxon`** (no sufABCDSE).
- **`ppu04122` bucket:** mark **`module_needs_revision`** — it conflates three biologically distinct modules
  (ISC assembly; tRNA thiolation relay; Moco/thiamine sulfur transfer). Recommend splitting into separate module docs.
- **tRNA 2-thiouridine relay** (if curated as its own module): **`covered`** (IscS-TusA-TusBCD-TusE-MnmA).
- **Moco sulfur-transfer/synthesis** (if curated): core steps **`covered`** (moeB, moaC, moaD/E, moaA PP_4597, moaB).
- **`candidate_uncertain`:** PP_1969, PP_2482 (MoaA-like), PP_1233 (TusA-like), PP_2435 (desulfurase), CsdA Q9Z408.
- **GO requests:** likely none new for ISC (well-covered by GO:0016226 iron–sulfur cluster assembly and gene-specific
  terms). Focus curation effort on disambiguating the three desulfurases and the MoaA-like radical-SAM paralogs.

---

## 7. Genes to promote to full `fetch-gene` review

**High priority (add to ISC module; currently missing):**
1. PP_0841 iscR (Q88PK9) — regulator
2. PP_0843 iscU (Q88PK7) — scaffold
3. PP_0844 iscA (Q88PK6) — A-type carrier
4. PP_0845 hscB (Q88PK5) — co-chaperone
5. PP_0846 hscA (Q88PK4) — chaperone
6. PP_0847 fdx (Q88PK3) — ferredoxin

**Medium priority (resolve ambiguity/over-annotation):**
7. PP_1969 (Q88LG4) & PP_2482 (Q88K11) — confirm/deny MoaA function
8. PP_2435 iscS-II (Q88K56) & CsdA (Q9Z408) — assign specific desulfurase roles
9. PP_1233 tusA-I (Q88NH6) — confirm whether relay TusA or paralog

---

## 8. Evidence base and open questions

**Direct (species-specific) evidence:** All locus/domain assignments are from PSEPK sequences (proteome UP000000556)
+ InterPro/Pfam. The contiguous PP_0841–PP_0847 operon structure is direct genomic evidence for ISC completeness, and
the absence of `sufABCDSE` is a direct negative genomic result. A published PSEPK study confirms a TudS-type [4Fe-4S]
desulfidase recycling 4-thiouridine monophosphate in KT2440 (PMID 37891428), corroborating active tRNA-sulfur metabolism.

**Transferred (homology / related-organism) evidence:** The mechanistic ISC assembly model and the TusA→TusBCD→TusE→MnmA
relay architecture derive from *E. coli* biochemistry (PMID 39870763; PMID 16387657). Transfer to PSEPK is **strong**
because the domain compositions and operon structures are conserved, but the specific in-vivo roles of the paralogous
desulfurases (PP_2435, CsdA) and MoaA-like proteins (PP_1969, PP_2482) are **uncertain** in PSEPK.

**Open questions / experiments to resolve gaps:**
- Which desulfurase (IscS vs. PP_2435 vs. CsdA) donates sulfur to ISC vs. Moco vs. the tRNA relay in PSEPK?
  (targeted knockouts + Fe–S/thiolation phenotyping)
- Are PP_1969/PP_2482 true Moco enzymes or other radical-SAM enzymes? (complementation of a *moaA* mutant)
- Is ISC essential/inducible under oxidative stress given the SUF absence? (conditional depletion; IscR regulon mapping)

## Key references
- PMID **39870763** — Gervason et al. 2025. Step-by-step [2Fe-2S] assembly by the *E. coli* ISC machinery (IscU/IscS/Fdx). Defines ISC core.
- PMID **39632806** — Steinhilper et al. 2024. Ferredoxin binding to the core ISC complex (electron donor role of Fdx).
- PMID **16387657** — Ikeuchi et al. 2006. Sulfur-relay for 2-thiouridine: IscS→TusA→TusBCD→TusE→MnmA reconstitution.
- PMID **37891428** — Fuchs et al. 2023. A KT2440 gene product acts as a TudS [4Fe-4S] desulfidase in vivo (direct PSEPK evidence).
- UniProt proteome **UP000000556** (PSEPK); InterPro/Pfam domain signatures (queried Iterations 1–2).

---
*Uncertainty statement:* Conclusions about operon completeness and SUF absence are high-confidence (direct genomic).
Specific in-vivo roles of paralogous desulfurases, MoaA-like radical-SAM proteins, and DsrEFH/TusBCD are homology-based
inferences requiring experimental confirmation in *P. putida* KT2440.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial-isc-iron-sulfur-cluster-assembly__ppu04122-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial-isc-iron-sulfur-cluster-assembly__ppu04122-deep-research-openscientist_artifacts/final_report.pdf)