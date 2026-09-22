---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T16:05:06.552282'
end_time: '2026-09-01T16:31:15.848841'
duration_seconds: 1569.3
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial non-homologous end joining
  module_summary: A reusable bacterial DNA double-strand-break repair module in which
    a Ku homodimer recognizes, protects, and aligns broken duplex ends, a LigD-family
    enzyme conditionally remodels non-ligatable termini through polymerase and 3-prime-phosphoesterase
    activities, and an ATP-dependent LigD ligase domain seals the DNA backbone. The
    module excludes homologous recombination, single-strand annealing, eukaryotic
    NHEJ factors, and accessory bacterial backup routes that do not require the Ku-LigD
    core.
  module_outline: "- Bacterial non-homologous end joining\n  - 1. DNA-end recognition,\
    \ protection, and synapsis\n  - Ku-dependent double-strand-break end recognition\n\
    \    - Prokaryotic Ku double-stranded-DNA-end binding (molecular player: prokaryotic\
    \ Ku family; activity or role: double-stranded DNA binding)\n  - 2. conditional\
    \ DNA-end remodeling\n  - LigD-dependent DNA-end remodeling\n    - LigD gap-filling\
    \ polymerase activity (molecular player: bacterial LigD family; activity or role:\
    \ DNA-directed DNA polymerase activity)\n    - LigD 3-prime-end healing activity\
    \ (molecular player: bacterial LigD family with a phosphoesterase domain; activity\
    \ or role: polynucleotide 3-prime-phosphatase activity)\n  - 3. ATP-dependent\
    \ phosphodiester sealing\n  - LigD-mediated DNA-end sealing\n    - LigD ATP-dependent\
    \ DNA ligase activity (molecular player: bacterial LigD family; activity or role:\
    \ DNA ligase (ATP) activity)"
  module_connections: '- Ku-dependent double-strand-break end recognition feeds into
    LigD-dependent DNA-end remodeling: Ku-bound incompatible or blocked ends are delivered
    to LigD for conditional remodeling.

    - Ku-dependent double-strand-break end recognition feeds into LigD-mediated DNA-end
    sealing: Ku-bound compatible ends can be sealed without an obligatory processing
    reaction.

    - LigD-dependent DNA-end remodeling precedes LigD-mediated DNA-end sealing: When
    remodeling is required, polymerase or phosphatase activity generates a ligatable
    substrate before sealing.'
  pathway_query: ppu03450
  pathway_id: ppu03450
  pathway_name: Non-homologous end-joining
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03450 with 2 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '2'
  candidate_genes: '- ku: PP_3255 | Q88HU8 | Non-homologous end joining protein Ku
    (primary bucket kegg:ppu03450)

    - ligD: PP_3260 | Q88HU3 | DNA ligase (ATP) (EC 6.5.1.1) (NHEJ DNA polymerase)
    (EC 6.5.1.1; primary bucket kegg:ppu03450)'
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
  path: PSEPK__bacterial_nonhomologous_end_joining__ppu03450-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_nonhomologous_end_joining__ppu03450-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial non-homologous end joining in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03450
- Resolved ID: ppu03450
- Resolved name: Non-homologous end-joining
- Source: KEGG

Resolved local bucket kegg:ppu03450 with 2 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 2

- ku: PP_3255 | Q88HU8 | Non-homologous end joining protein Ku (primary bucket kegg:ppu03450)
- ligD: PP_3260 | Q88HU3 | DNA ligase (ATP) (EC 6.5.1.1) (NHEJ DNA polymerase) (EC 6.5.1.1; primary bucket kegg:ppu03450)

## Generic Module Context

### Working Scope

A reusable bacterial DNA double-strand-break repair module in which a Ku homodimer recognizes, protects, and aligns broken duplex ends, a LigD-family enzyme conditionally remodels non-ligatable termini through polymerase and 3-prime-phosphoesterase activities, and an ATP-dependent LigD ligase domain seals the DNA backbone. The module excludes homologous recombination, single-strand annealing, eukaryotic NHEJ factors, and accessory bacterial backup routes that do not require the Ku-LigD core.

### Provisional Biological Outline

- Bacterial non-homologous end joining
  - 1. DNA-end recognition, protection, and synapsis
  - Ku-dependent double-strand-break end recognition
    - Prokaryotic Ku double-stranded-DNA-end binding (molecular player: prokaryotic Ku family; activity or role: double-stranded DNA binding)
  - 2. conditional DNA-end remodeling
  - LigD-dependent DNA-end remodeling
    - LigD gap-filling polymerase activity (molecular player: bacterial LigD family; activity or role: DNA-directed DNA polymerase activity)
    - LigD 3-prime-end healing activity (molecular player: bacterial LigD family with a phosphoesterase domain; activity or role: polynucleotide 3-prime-phosphatase activity)
  - 3. ATP-dependent phosphodiester sealing
  - LigD-mediated DNA-end sealing
    - LigD ATP-dependent DNA ligase activity (molecular player: bacterial LigD family; activity or role: DNA ligase (ATP) activity)

### Known Relationships Among Steps

- Ku-dependent double-strand-break end recognition feeds into LigD-dependent DNA-end remodeling: Ku-bound incompatible or blocked ends are delivered to LigD for conditional remodeling.
- Ku-dependent double-strand-break end recognition feeds into LigD-mediated DNA-end sealing: Ku-bound compatible ends can be sealed without an obligatory processing reaction.
- LigD-dependent DNA-end remodeling precedes LigD-mediated DNA-end sealing: When remodeling is required, polymerase or phosphatase activity generates a ligatable substrate before sealing.

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

# Species-Aware Review: Bacterial Non-Homologous End Joining (Ku–LigD) in *Pseudomonas putida* KT2440

**Module/bucket:** kegg:ppu03450 — Non-homologous end-joining
**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module area:** other_kegg_pathway | **Candidate genes:** `ku` (PP_3255 / Q88HU8), `ligD` (PP_3260 / Q88HU3)

---

## 1. Executive summary

The bacterial NHEJ module is **satisfied in *P. putida* KT2440 by exactly the two candidate genes**, Ku (PP_3255) and LigD (PP_3260), and this is supported by **direct experimental evidence in the target strain** — an unusually strong footing for a bacterial NHEJ call. Genetic ablation of either *ku* or *ligD* alters DSB-repair/mutagenesis phenotypes in KT2440 (Paris et al. 2015, PMID 25942369; Sharaev et al. 2022, PMID 36475478). All three mechanistic sub-steps of the module (Ku-dependent end recognition/synapsis; LigD polymerase gap-fill and 3′-phosphoesterase end-healing; LigD ATP-dependent sealing) map to just these two proteins, with LigD being a single multifunctional polypeptide (POL + PE + LIG).

Key curation cautions: (i) **EC 6.5.1.1 captures only the ligase activity of LigD** — its polymerase and phosphoesterase activities need separate GO terms and are not conveyed by the enzyme name/EC; (ii) the gene symbol **"ligC" in KT2440 (PP_2602) is a homonym false-friend** — it is 4-carboxy-2-hydroxymuconate-6-semialdehyde dehydrogenase (aromatic catabolism, EC 1.1.1.312), **not** a backup NHEJ ligase; (iii) the **mycobacterial-style LigC/PrimC backup NHEJ routes are absent** and should be marked not_expected_in_target_taxon. Both candidate genes merit promotion to full `fetch-gene` review, LigD especially because of its multi-activity/single-EC mismatch.

---

## 2. Target-organism pathway definition

**Included process.** The Ku–LigD "two-component" bacterial NHEJ pathway: template-independent repair of a chromosomal (or plasmid) DNA **double-strand break (DSB)** in which (1) a **Ku homodimer** binds, protects, and juxtaposes the two broken duplex ends and recruits LigD; (2) **LigD** conditionally remodels non-ligatable termini via a **polymerase (POL)** module (gap fill, with a marked preference for ribonucleotide addition) and a **3′-phosphoesterase (PE)** module (removes 3′-phosphate/3′-blocking groups to yield a ligatable 3′-OH); and (3) the **ATP-dependent ligase (LIG)** module seals the backbone. The pathway is characteristically **error-prone/mutagenic** and is most important in stationary phase / quiescent, non-replicating cells where a sister chromosome for homologous recombination (HR) is unavailable.

**Kept separate (neighboring processes / overview maps).**
- **Homologous recombination** (RecA/RecBCD/AddAB; KEGG "Homologous recombination" ppu03440) — the alternative DSB pathway that requires a template; explicitly excluded.
- **Base excision repair / mismatch repair / nucleotide excision repair** overview maps — even though Ku has a reported AP/5′-dRP-lyase moonlighting activity (PMID 25355514), BER proper is a separate module.
- **NAD⁺-dependent replicative/backup ligases** LigA (PP_4274, EC 6.5.1.2) and LigB (PP_4968, EC 6.5.1.2) — these seal nicks in replication/repair but are **not** the ATP-dependent NHEJ ligase and are not part of this module.
- **Eukaryotic NHEJ factors** (DNA-PKcs, XRCC4, LIG4, Artemis, etc.) — not present in bacteria; excluded.

**Alternate names / database definitions.** "Bacterial/prokaryotic NHEJ"; "Ku–LigD end-joining"; KEGG map03450 (organism-specific ppu03450). LigD is also called "DNA ligase D," "NHEJ DNA ligase/polymerase," "LigD (POL/PE/LIG)." Ku is "Non-homologous end joining protein Ku," "prokaryotic Ku," "bacterial Ku."

---

## 3. Expected step model (module satisfiability)

| Module step | Expected player | KT2440 gene (domain) | Status | Evidence strength |
|---|---|---|---|---|
| 1. DNA-end recognition, protection & synapsis | prokaryotic Ku (dsDNA-end binding) | **ku / PP_3255 (Q88HU8)** — Ku β-barrel ~11–194 | **covered** | Direct (target strain, genetics) + genus biochemistry + InterPro domain |
| 2a. Gap-filling polymerase | LigD POL (DNA/RNA polymerase) | **ligD / PP_3260 (Q88HU3)** — POL ~547–812 | **covered** | Direct (target strain: POL domain implicated) + genus structure + InterPro (PaeLigD-type) |
| 2b. 3′-end healing | LigD PE (3′-phosphoesterase) | **ligD / PP_3260** — PE ~5–160 | **covered** | Direct (target strain: PE domain implicated) + InterPro (TIGR02777) |
| 3. ATP-dependent sealing | LigD LIG (ATP ligase, EC 6.5.1.1) | **ligD / PP_3260** — LIG ~219–520 | **covered** | Direct (UniProt EC 6.5.1.1) + genus end-joining assays + InterPro (TIGR02779) |
| (Backup) LigD-independent ligase | mycobacterial LigC / PrimC | *none* (PP_2602 "ligC" is unrelated) | **not_expected_in_target_taxon** | Bioinformatic (proteome scan) + comparative |

**All four core steps are marked `covered`.** No core step is a gap. The only "missing" element relative to the fully generic bacterial-DSB picture is a dedicated backup ligase, which is a genuine biological absence in this lineage rather than an annotation gap.

---

## 4. Candidate genes and evidence

### 4.1 `ku` — PP_3255 / Q88HU8 (Non-homologous end joining protein Ku)
- **Role:** DNA-end-binding homodimer; recognizes and protects duplex DNA ends, promotes synapsis, and recruits/stimulates LigD.
- **Evidence type:** *Direct target-strain genetics* — Δ*ku* changes the stationary-phase mutation spectrum in carbon-starved KT2440 (PMID 25942369) and alters Cas9-DSB repair outcomes in KT2440 (PMID 36475478). *Genus biochemistry* — Pseudomonas Ku stimulates LigD POL activity and promotes full-length LigD end-joining (PMID 20018881). *Structural model* — cryo-EM of *M. tuberculosis* Ku shows homodimer→proteofilament on DNA and a C-terminus that regulates DNA loading and LigD recruitment (PMID 41298423; transfer to KT2440 is moderate — conserved fold, different species).
- **UniProt/InterPro features:** 273 aa; prokaryotic-type Ku domain (CDD cd00789 KU_like; Pfam PF02735 Ku70/Ku80 β-barrel ~11–194; IPR009187 prokaryotic Ku; HAMAP MF_01875), with a **C-terminal extension (~195–273)** beyond the core β-barrel that corresponds to the region implicated in DNA loading/LigD recruitment (cf. *P. aeruginosa* Ku C-terminal truncations mapping the functional core to Ku-(1–229), PMID 20018881; and the C-terminal regulatory role in *M. tuberculosis* Ku, PMID 41298423). Single-copy — **no Ku paralog** in the proteome scan.
- **Curation caveats:** GO "double-stranded DNA binding" and "DSB repair via NHEJ" are well supported. A reported AP/5′-dRP-lyase side activity of bacterial Ku (shown for *B. subtilis* and *P. aeruginosa* Ku, PMID 25355514) is a *moonlighting* function; do **not** promote it to a core NHEJ annotation for KT2440 without direct data.

### 4.2 `ligD` — PP_3260 / Q88HU3 (DNA ligase D; EC 6.5.1.1)
- **Role:** Multifunctional NHEJ end-processing/sealing enzyme carrying three autonomous modules — POL (gap fill, rNTP-preferring, Mn²⁺-dependent), PE (3′-phosphoesterase → 3′-OH), and LIG (ATP-dependent sealing).
- **Evidence type:** *Direct target-strain genetics* — Δ*ligD* alters the KT2440 stationary-phase mutation spectrum, and **both PE and POL domains are implicated** in the mutation phenotype (PMID 25942369); KT2440 Cas9-DSB repair depends on LigD (PMID 36475478). *Genus structure/biochemistry* — 1.5 Å crystal structure of the *Pseudomonas* LigD POL domain (primase-superfamily, two-metal, rNTP preference; PMID 16446439) and detailed gap-fill/Ku-stimulation biochemistry (PMID 20018881). *Domain framework* — LigD three-module review (PMID 34901162).
- **UniProt features:** 833 aa; annotated "ATP-dependent DNA ligase family profile" (307–399); keywords include **DNA-directed DNA polymerase, Exonuclease/Nuclease, Manganese, Nucleotidyltransferase, Multifunctional enzyme** — consistent with a full POL+PE+LIG LigD.
- **InterPro domain architecture (curation-ready boundaries; order N→C is PE–LIG–POL):**
  - **PE (3′-phosphoesterase)** ~residues **5–160** — TIGR02777 / IPR014144 "DNA ligase D, 3′-phosphoesterase domain"; Pfam PF13298 (38–143). → GO: polynucleotide 3′-phosphatase activity (GO:0046403).
  - **LIG (ATP-dependent ligase/adenylation)** ~residues **219–520** — TIGR02779 / IPR014146; Pfam PF01068 (adenylation, 219–399) + PF04679 (C-terminal, 418–514) + OB-fold (IPR012340, 401–522). → GO: DNA ligase (ATP) activity (GO:0003910); this is the sole activity covered by EC 6.5.1.1.
  - **POL (primase-superfamily polymerase)** ~residues **547–812** — TIGR02778 / IPR014145; Pfam PF21686; CDD cd04862 **"PaeLigD_Pol_like"**; IPR033651 **"LigD polymerase domain, PaeLigD-type"**. → GO: DNA-directed DNA polymerase activity (GO:0003887).
  - Overall: IPR014143 "DNA ligase D" (228–816); NCBIfam TIGR02776; PANTHER PTHR42705. The POL module being explicitly classified as **PaeLigD-type** ties KT2440 LigD directly to the *P. aeruginosa* LigD Pol structure (PMID 16446439), making genus→KT2440 mechanistic transfer **strong** at the fold level.
- **Curation caveats (important):**
  - **Single-EC / multi-activity mismatch:** the recommended EC (6.5.1.1) and the "DNA ligase (ATP)" name describe **only** the LIG module. The POL and PE activities are biologically essential module steps but are invisible to the EC/name. Ensure GO annotations include **DNA-directed DNA polymerase activity** (GO:0003887 / or DNA/RNA polymerase) and **polynucleotide 3′-phosphatase activity** (GO:0046403) in addition to **DNA ligase (ATP) activity** (GO:0003910).
  - **Over-propagation risk in reverse:** automated pipelines keyed only on "DNA ligase (ATP)" may under-annotate LigD (missing POL/PE). Conversely, generic "DNA ligase" text should not be conflated with the NAD⁺ ligases LigA/LigB.
  - No KT2440-specific crystal structure exists; atomic data are genus-level (mostly *P. aeruginosa*). Ortholog transfer is **strong** but should be flagged as inferred at the structural level.

### 4.3 Genomic context
`ku` (PP_3255) and `ligD` (PP_3260) sit in the same chromosomal region but are **not part of a shared operon**: the four intervening genes are functionally unrelated to DNA repair — PP_3256 (glycosyltransferase, group 2), PP_3257 (methyltransferase), PP_3258 (acetylglucosaminylphosphatidylinositol deacetylase), and PP_3259 (acyl-CoA dehydrogenase-related). Thus *ku* and *ligD* are **independently encoded and likely independently regulated**, consistent with the genetic observation that Ku and LigD can act in partly separate mutagenic sub-pathways in KT2440 (Paris et al. 2015, PMID 25942369). Unlike some bacteria where *ku* and *ligD* are adjacent/co-transcribed, this locus arrangement argues against inferring co-regulation, and any module reconstruction should treat the two as separate transcriptional units absent operon/transcriptomic data.

---

## 5. Gaps, ambiguities, and likely over-annotations

1. **"ligC" (PP_2602 / Q88JP7) is NOT an NHEJ ligase.** It is 4-carboxy-2-hydroxymuconate-6-semialdehyde dehydrogenase (EC 1.1.1.312), a protocatechuate/aromatic-degradation enzyme. This is a classic gene-symbol homonym; any mapping of KT2440 "ligC" to bacterial NHEJ backup would be an **over-annotation error**. Mark the LigC/PrimC backup steps `not_expected_in_target_taxon`.
2. **No dedicated backup NHEJ ligase.** Proteome scan shows LigD is the **sole ATP-dependent DNA ligase (EC 6.5.1.1)** in KT2440; LigA (PP_4274) and LigB (PP_4968) are NAD⁺-dependent (EC 6.5.1.2). Mycobacteria-style LigC/PrimC redundancy is a lineage-specific feature, not general.
3. **LigD-independent NHEJ caveat (uncertain).** A 2026 study reports that *P. aeruginosa* can perform **LigD-independent NHEJ** and microhomology-mediated repair, with Ku (but not LigD) conditionally essential in some contexts (PMID 42306942). The responsible ligase is not defined and this is a *related-species* result. It does **not** change the KT2440 module core, but flags that an as-yet-unidentified alternative sealing route may exist in pseudomonads — an open question, not a curatable gene.
4. **Ku moonlighting (AP-lyase).** Do not over-extend Ku's annotation to BER on the basis of the *B. subtilis*/*P. aeruginosa* lyase activity (PMID 25355514) without direct KT2440 evidence.
5. **Species transfer bookkeeping.** Distinguish: KT2440-direct (PMID 25942369, 36475478) > genus *Pseudomonas* biochemistry/structure (PMID 16446439, 20018881) > generic bacterial/mycobacterial mechanism (PMID 34901162, 15778718, 24957619, 41298423).

---

## 6. Module and GO-curation recommendations

- **Step calls:** end recognition/synapsis → **covered** (Ku); gap-fill polymerase → **covered** (LigD POL); 3′-end healing → **covered** (LigD PE); ATP-dependent sealing → **covered** (LigD LIG). Backup ligase → **not_expected_in_target_taxon**.
- **Module boundaries:** the generic module scope (Ku–LigD core, excluding HR/SSA/eukaryotic NHEJ/backup routes) is **correct for KT2440**. No `module_needs_revision` required; the "conditional" remodeling framing matches the observed data (Ku alone can present compatible ends for direct sealing; POL/PE act only when termini are non-ligatable).
- **GO term needs for LigD (Q88HU3):** ensure co-annotation of (a) DNA ligase (ATP) activity GO:0003910; (b) DNA-directed DNA polymerase / DNA polymerase activity (POL module); (c) polynucleotide 3′-phosphatase activity GO:0046403 (PE module); and process term DSB repair via NHEJ GO:0006303. Flag the EC-vs-activity mismatch so downstream EC→GO pipelines do not drop POL/PE.
- **GO for Ku (Q88HU8):** double-stranded DNA binding GO:0003690 (or dsDNA end binding), DSB repair via NHEJ GO:0006303.
- **No new module document** appears necessary; the existing generic bacterial-NHEJ module applies cleanly. A curator note recording the "ligC" homonym and the LigD single-EC/multi-activity issue is recommended.

---

## 7. Genes to promote to full `fetch-gene` review

1. **`ligD` / PP_3260 (Q88HU3)** — **High priority.** Multifunctional enzyme whose EC/name conveys only 1 of 3 activities; verify POL and PE module annotations and GO coverage; confirm domain boundaries against AlphaFold/InterPro.
2. **`ku` / PP_3255 (Q88HU8)** — **Medium priority.** Straightforward core call; confirm single-copy status and check whether to note (without promoting) the AP-lyase moonlighting literature.
3. **(Watchlist, not a candidate) `ligC` / PP_2602 (Q88JP7)** — flag explicitly as a **name collision** to prevent erroneous NHEJ mapping; no NHEJ review needed.

---

## 8. Key references

- Paris Q, et al. *NHEJ enzymes LigD and Ku participate in stationary-phase mutagenesis in Pseudomonas putida.* 2015. **PMID 25942369** — *direct KT2440/putida genetics; PE+POL domains implicated.*
- Sharaev N, et al. *Repair of Double-Stranded DNA Breaks Generated by CRISPR-Cas9 in Pseudomonas putida KT2440.* 2022. **PMID 36475478** — *direct KT2440 NHEJ manipulation.*
- Zhu H, et al. *Atomic structure and NHEJ function of the polymerase component of bacterial DNA ligase D.* 2006. **PMID 16446439** — *Pseudomonas LigD POL crystal structure.*
- Zhu H, Shuman S. *Gap filling activities of Pseudomonas LigD polymerase and functional interactions with Ku.* 2010. **PMID 20018881** — *Pseudomonas Ku–LigD biochemistry.*
- Amare B, et al. *LigD: A Structural Guide to the Multi-Tool of Bacterial NHEJ.* 2021. **PMID 34901162** — *POL/PE/LIG module review.*
- de Ory A, et al. *Efficient processing of abasic sites by bacterial NHEJ Ku proteins.* 2014. **PMID 25355514** — *Ku AP/5′-dRP-lyase moonlighting (Bsu, Pae).*
- Bhattarai H, et al. *DNA ligase C1 mediates LigD-independent NHEJ of M. smegmatis.* 2014. **PMID 24957619** — *LigC backup (mycobacteria; absent in Pseudomonas).*
- Gong C, et al. *Mechanism of NHEJ in mycobacteria: Ku, LigD and LigC.* 2005. **PMID 15778718** — *backup LigC concept.*
- Zahid S, et al. *Oligomerisation of Ku from M. tuberculosis promotes DNA synapsis.* 2025. **PMID 41298423** — *Ku structure/synapsis (cross-species).*
- Hare PJ, et al. *Non-canonical DSB repair in P. aeruginosa includes LigD-independent NHEJ.* 2026. **PMID 42306942** — *open question on alternative routes (related species).*

---

### Uncertainty ledger
- **Direct (KT2440):** functional requirement of Ku and LigD, and involvement of LigD POL+PE domains, in DSB repair/mutagenesis.
- **Strong inference (genus Pseudomonas):** LigD POL structure/mechanism, Ku–LigD stimulation, ribonucleotide-preferring gap fill.
- **Comparative/generic:** three-module LigD architecture, PE→3′-OH chemistry, Ku synapsis mechanics, absence of LigC/PrimC backup (bioinformatic for KT2440).
- **Open:** existence/identity of any LigD-independent sealing route in pseudomonads; in-vivo relevance of Ku AP-lyase in KT2440; operon structure of ku/ligD.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_nonhomologous_end_joining__ppu03450-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_nonhomologous_end_joining__ppu03450-deep-research-openscientist_artifacts/final_report.pdf)
