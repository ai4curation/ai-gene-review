---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T13:37:52.310310'
end_time: '2026-08-08T14:02:49.943720'
duration_seconds: 1497.63
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: base_excision_repair
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: ppu03410
  pathway_id: ppu03410
  pathway_name: Base excision repair
  pathway_source: KEGG
  pathway_context: 'Resolved local bucket kegg:ppu03410 with 11 primary genes; module
    area: other_kegg_pathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '14'
  candidate_genes: '- tag: PP_0062 | Q88RR7 | DNA-3-methyladenine glycosylase I (EC
    3.2.2.20) (EC 3.2.2.20; primary bucket kegg:ppu03410)

    - polA: PP_0123 | Q88RK6 | DNA polymerase I (EC 2.7.7.7) (EC 2.7.7.7; primary
    bucket kegg:ppu03420)

    - mutY: PP_0286 | Q88R48 | Adenine DNA glycosylase (EC 3.2.2.31) (EC 3.2.2.31;
    primary bucket kegg:ppu03410)

    - PP_0705: PP_0705 | Q88PZ3 | DNA-3-methyladenine glycosylase II (EC 3.2.2.21)
    (EC 3.2.2.21; primary bucket kegg:ppu03410)

    - nth: PP_1092 | Q88NW2 | Endonuclease III (EC 4.2.99.18) (DNA-(apurinic or apyrimidinic
    site) lyase) (EC 4.2.99.18; primary bucket kegg:ppu03410)

    - ung: PP_1413 | Q88N05 | Uracil-DNA glycosylase (UDG) (EC 3.2.2.27) (EC 3.2.2.27;
    primary bucket kegg:ppu03410)

    - recJ: PP_1477 | Q88MU1 | Single-stranded-DNA-specific exonuclease RecJ (primary
    bucket kegg:ppu03410)

    - PP_2707: PP_2707 | Q88JE2 | Exodeoxyribonuclease III (primary bucket kegg:ppu03410)

    - xthA: PP_2890 | Q88IV9 | Exodeoxyribonuclease III / apurinic/apyrimidinic endodeoxyribonuclease
    VI (EC 3.1.11.2) (EC 3.1.11.2; primary bucket kegg:ppu03410)

    - ligA: PP_4274 | Q88F25 | DNA ligase (EC 6.5.1.2) (Polydeoxyribonucleotide synthase
    [NAD(+)]) (EC 6.5.1.2; primary bucket kegg:ppu03420)

    - PP_4812: PP_4812 | Q88DL3 | Putative 3-methyladenine DNA glycosylase (EC 3.2.2.-)
    (EC 3.2.2.-; primary bucket kegg:ppu03410)

    - ligB: PP_4968 | Q88D59 | DNA ligase B (EC 6.5.1.2) (Polydeoxyribonucleotide
    synthase [NAD(+)] B) (EC 6.5.1.2; primary bucket kegg:ppu03420)

    - mutM: PP_5125 | Q88CQ5 | Formamidopyrimidine-DNA glycosylase (Fapy-DNA glycosylase)
    (EC 3.2.2.23) (DNA-(apurinic or apyrimidinic site) lyase MutM) (AP lyase MutM)
    (EC 4.2.99.18) (EC 3.2.2.23; 4.2.99.18; primary bucket kegg:ppu03410)

    - PP_5292: PP_5292 | Q88C91 | Catabolite repression control protein (primary bucket
    kegg:ppu03410)'
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__base-excision-repair__ppu03410-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__base-excision-repair__ppu03410-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

base_excision_repair in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: ppu03410
- Resolved ID: ppu03410
- Resolved name: Base excision repair
- Source: KEGG

Resolved local bucket kegg:ppu03410 with 11 primary genes; module area: other_kegg_pathway.

## Candidate Genes From Local Metadata

Candidate gene count: 14

- tag: PP_0062 | Q88RR7 | DNA-3-methyladenine glycosylase I (EC 3.2.2.20) (EC 3.2.2.20; primary bucket kegg:ppu03410)
- polA: PP_0123 | Q88RK6 | DNA polymerase I (EC 2.7.7.7) (EC 2.7.7.7; primary bucket kegg:ppu03420)
- mutY: PP_0286 | Q88R48 | Adenine DNA glycosylase (EC 3.2.2.31) (EC 3.2.2.31; primary bucket kegg:ppu03410)
- PP_0705: PP_0705 | Q88PZ3 | DNA-3-methyladenine glycosylase II (EC 3.2.2.21) (EC 3.2.2.21; primary bucket kegg:ppu03410)
- nth: PP_1092 | Q88NW2 | Endonuclease III (EC 4.2.99.18) (DNA-(apurinic or apyrimidinic site) lyase) (EC 4.2.99.18; primary bucket kegg:ppu03410)
- ung: PP_1413 | Q88N05 | Uracil-DNA glycosylase (UDG) (EC 3.2.2.27) (EC 3.2.2.27; primary bucket kegg:ppu03410)
- recJ: PP_1477 | Q88MU1 | Single-stranded-DNA-specific exonuclease RecJ (primary bucket kegg:ppu03410)
- PP_2707: PP_2707 | Q88JE2 | Exodeoxyribonuclease III (primary bucket kegg:ppu03410)
- xthA: PP_2890 | Q88IV9 | Exodeoxyribonuclease III / apurinic/apyrimidinic endodeoxyribonuclease VI (EC 3.1.11.2) (EC 3.1.11.2; primary bucket kegg:ppu03410)
- ligA: PP_4274 | Q88F25 | DNA ligase (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)]) (EC 6.5.1.2; primary bucket kegg:ppu03420)
- PP_4812: PP_4812 | Q88DL3 | Putative 3-methyladenine DNA glycosylase (EC 3.2.2.-) (EC 3.2.2.-; primary bucket kegg:ppu03410)
- ligB: PP_4968 | Q88D59 | DNA ligase B (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)] B) (EC 6.5.1.2; primary bucket kegg:ppu03420)
- mutM: PP_5125 | Q88CQ5 | Formamidopyrimidine-DNA glycosylase (Fapy-DNA glycosylase) (EC 3.2.2.23) (DNA-(apurinic or apyrimidinic site) lyase MutM) (AP lyase MutM) (EC 4.2.99.18) (EC 3.2.2.23; 4.2.99.18; primary bucket kegg:ppu03410)
- PP_5292: PP_5292 | Q88C91 | Catabolite repression control protein (primary bucket kegg:ppu03410)

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

# Base Excision Repair (KEGG ppu03410) in *Pseudomonas putida* KT2440 — Curation Review

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Pathway:** Base excision repair — KEGG map ppu03410
**Purpose:** Species-aware module satisfiability and gene-annotation curation review

---

## 1. Executive Summary

Base excision repair (BER) is **complete and satisfiable** in *Pseudomonas putida* KT2440. Every core enzymatic step of the canonical bacterial short-patch BER pathway is encoded in the genome: damage-specific DNA glycosylases (uracil-DNA glycosylase Ung, formamidopyrimidine glycosylase MutM/Fpg, adenine glycosylase MutY, endonuclease III Nth), a redundant set of 3-methyladenine glycosylases (Tag, AlkA, and an Mpg/AAG-type enzyme), a class-II apurinic/apyrimidinic (AP) endonuclease activity supplied by exonuclease III–family enzymes, gap-filling by DNA polymerase I (PolA), and nick sealing by the NAD⁺-dependent DNA ligase LigA. On satisfiability grounds, the module can be marked **covered**.

The candidate gene list supplied with this brief is, however, **not** a clean representation of the pathway and requires two corrective edits. First, **PP_5292 ("Crc") is an over-propagated annotation** and should be removed from the BER bucket: it is a catalytically inactive member of the exonuclease-III/DNase-I-like superfamily that functions in *P. putida* as an RNA-binding translational repressor in carbon-catabolite repression (the Crc–Hfq complex), not as a DNA-repair nuclease. Second, **MutT (PP_1348, 8-oxo-dGTP diphosphatase, EC 3.6.1.55) is present in the genome but missing from the candidate list**; adding it completes the three-component "GO" (8-oxoguanine) anti-mutator system (MutT + MutY + MutM) that KEGG groups alongside BER.

A notable **lineage-specific architectural feature** is that KT2440 **lacks Endonuclease IV (Nfo)**, as well as Endonuclease VIII (Nei) and Endonuclease V (Nfi). AP-site incision therefore rests entirely on the two exonuclease-III (Xth-family) paralogs, PP_2890 (xthA) and PP_2707. This "Xth-only" AP-endonuclease configuration should be recorded explicitly in the module because it differs from organisms such as *Mycobacterium tuberculosis* and *Escherichia coli*, where Nfo/EndoIV contributes substantially. Additional curation-relevant observations include a paralogous Tag-family glycosylase (PP_1642) that is likewise absent from the candidate list, and the fact that most step assignments rest on homology/pathway-database inference rather than direct KT2440 biochemistry.

---

## 2. Target-Organism Pathway Definition

**Process included.** Base excision repair is the pathway that removes small, non-helix-distorting base lesions — deaminated bases (e.g., uracil from cytosine deamination), oxidized bases (e.g., 8-oxoguanine, thymine glycol, formamidopyrimidines), and alkylated bases (e.g., 3-methyladenine) — through a defined enzymatic relay:

1. A **damage-specific DNA glycosylase** recognizes and excises the aberrant base, leaving an abasic (AP) site. Bifunctional glycosylases additionally nick the backbone via an associated AP-lyase activity.
2. A **class-II AP endonuclease** cleaves the phosphodiester backbone 5′ to the AP site, generating a 3′-OH and 5′-deoxyribose-phosphate.
3. **DNA polymerase I** removes the 5′-dRP/short flap and fills the single-nucleotide (or short-patch) gap.
4. A **DNA ligase** (NAD⁺-dependent LigA in bacteria) seals the remaining nick.

**Boundaries to keep separate.** For curation, KEGG ppu03410 (BER) must be distinguished from neighboring repair maps: **nucleotide excision repair** (ppu03420, which contains *polA* and *ligA* as shared downstream enzymes — note that these two candidate genes are bucketed under 03420, not 03410), **mismatch repair** (ppu03430), and **homologous recombination** (ppu03440). Nucleotide-pool sanitization enzymes (MutT/Nudix hydrolases) are functionally part of the "GO system" and are frequently co-mapped with BER even though they act on the dNTP pool rather than on duplex DNA. Broad overview maps (e.g., metabolic overview map01100) should not be used to define membership.

**Alternate names / database definitions.** The pathway is universally called "base excision repair" (BER). Individual steps carry family-specific names: exonuclease III = XthA = "class-II AP-endonuclease/3′-5′ exonuclease"; MutM = Fpg = "formamidopyrimidine-DNA glycosylase"; Nth = "endonuclease III"; the 8-oxo-dGTPase is MutT (a Nudix hydrolase). The "GO system" (for 8-oxo-**G**uanine) is the standard umbrella term for the MutT/MutY/MutM triad.

---

## 3. Expected Step Model

The table below lists the canonical BER steps expected in a Gram-negative bacterium and the KT2440 status determined in this review.

| Step | Function (EC) | Expected gene(s) | KT2440 status | Locus/UniProt |
|------|---------------|------------------|---------------|---------------|
| Uracil excision | Uracil-DNA glycosylase (3.2.2.27) | *ung* | **Covered** | PP_1413 / Q88N05 |
| 8-oxoG excision (from 8-oxoG:C) | Fapy/8-oxoG glycosylase + AP lyase (3.2.2.23; 4.2.99.18) | *mutM/fpg* | **Covered** | PP_5125 / Q88CQ5 |
| Adenine excision (from 8-oxoG:A) | Adenine DNA glycosylase (3.2.2.31) | *mutY* | **Covered** | PP_0286 / Q88R48 |
| Oxidized pyrimidine excision | Endonuclease III + AP lyase (4.2.99.18) | *nth* | **Covered** | PP_1092 / Q88NW2 |
| 3-methyladenine excision | 3-mA glycosylase I / II / Mpg (3.2.2.20/21/-) | *tag*, *alkA*, *mpg* | **Covered (redundant)** | PP_0062, PP_0705, PP_4812 (+PP_1642) |
| AP-site incision | Class-II AP endonuclease (3.1.11.2) | *xthA* / *nfo* | **Covered by Xth only; Nfo absent** | PP_2890, PP_2707 |
| Nucleotide-pool sanitization | 8-oxo-dGTP diphosphatase (3.6.1.55) | *mutT* | **Present but missing from candidate list** | PP_1348 / Q88N67 |
| Gap filling | DNA polymerase I (2.7.7.7) | *polA* | **Covered** (bucket 03420) | PP_0123 / Q88RK6 |
| Nick sealing | NAD⁺-dependent DNA ligase (6.5.1.2) | *ligA* | **Covered** (bucket 03420) | PP_4274 / Q88F25 |
| ssDNA exonuclease (long-patch/end resection) | RecJ | *recJ* | **Covered (ancillary)** | PP_1477 / Q88MU1 |

**Steps probably not expected / absent in this organism:** Endonuclease IV (*nfo*), Endonuclease VIII (*nei*), and Endonuclease V (*nfi*) are absent from the proteome. Their absence is not a satisfiability gap because the Xth-family paralogs supply AP-endonuclease activity, but it should be recorded as a lineage-specific feature (`not_expected_in_target_taxon` for *nfo/nei/nfi*).

---

## 4. Candidate Genes and Evidence

### High-confidence, correctly bucketed genes

**Ung — PP_1413 / Q88N05 (uracil-DNA glycosylase, EC 3.2.2.27).** Family-diagnostic UDG annotation; the single-family monofunctional uracil glycosylase expected in essentially all bacteria. Role and evidence type: homology-based, high confidence. No curation caveat.

**MutM/Fpg — PP_5125 / Q88CQ5 (EC 3.2.2.23 / 4.2.99.18).** Bifunctional formamidopyrimidine-DNA glycosylase with associated AP-lyase. Core of the GO anti-mutator system; excises 8-oxoG opposite C and Fapy lesions. Homology-based, high confidence.

**MutY — PP_0286 / Q88R48 (adenine DNA glycosylase, EC 3.2.2.31).** Removes adenine misincorporated opposite 8-oxoG; second component of the GO system. Contains the HhH-GPD glycosylase fold (Pfam PF00730), confirmed by positive-control domain scan. High confidence.

**Nth — PP_1092 / Q88NW2 (endonuclease III, EC 4.2.99.18).** Bifunctional glycosylase/AP-lyase acting on oxidized pyrimidines; HhH-GPD fold. High confidence.

**Tag / AlkA / Mpg alkylation glycosylases.** KT2440 encodes **three distinct 3-methyladenine glycosylase families**: PP_0062 (*tag*, 3-mA glycosylase I, EC 3.2.2.20) and the un-listed paralog **PP_1642** (also Tag-family); PP_0705 (*alkA*-type, 3-mA glycosylase II, EC 3.2.2.21), whose gene is adjacent to *ada* (PP_0706), consistent with an Ada adaptive-response operon; and **PP_4812 / Q88DL3**, which carries Pfam PF02245 + InterPro IPR003180 (methylpurine/AAG glycosylase superfamily, SSF50486) — an Mpg/AAG family distinct from both Tag and AlkA. The alkylation-repair step is therefore covered redundantly. Caveat: PP_4812 carries only the generic EC 3.2.2.- and BER keywords (DNA damage, DNA repair, Glycosidase); its precise substrate profile is inferred, not measured.

**xthA / PP_2707 — the AP-endonuclease step.** PP_2890 (*xthA*, Q88IV9, EC 3.1.11.2) and PP_2707 (Q88JE2) are both ~270-aa exonuclease-III proteins with the Mg²⁺/Mn²⁺ ExoIII hydrolase signature. Together they supply the class-II AP-endonuclease activity that incises the backbone at abasic sites. Evidence is homology-based for KT2440 but strongly supported by mechanism in related bacteria (see §7). Caveat: which paralog is dominant in vivo is unknown; both should be treated as AP-endonuclease candidates.

**RecJ — PP_1477 / Q88MU1 (ssDNA-specific exonuclease).** Ancillary nuclease that contributes to end resection / long-patch processing. Correctly associated but peripheral to the core short-patch relay.

### Genes bucketed under NER (ppu03420) but required for BER completion

**PolA — PP_0123 / Q88RK6 (DNA polymerase I, EC 2.7.7.7)** and **LigA — PP_4274 / Q88F25 (NAD⁺-dependent DNA ligase, EC 6.5.1.2)** are shared downstream enzymes. Their primary bucket is ppu03420, but they are indispensable for BER gap-filling and sealing, respectively. For module satisfiability they must be counted as **covered**. LigB (PP_4968 / Q88D59) is a second, ancillary NAD⁺-ligase of uncertain physiological role and should not be relied on for the core step.

### Over-propagated annotation (remove)

**PP_5292 / Q88C91 ("Crc").** See Finding F001 in §5 — this gene is not a BER enzyme and should be dropped from the bucket.

---

## 5. Key Findings

### F001 — PP_5292 ("Crc") is an over-propagated BER annotation

PP_5292 (UniProt Q88C91) is bucketed in kegg:ppu03410 solely on the basis of fold homology to the exonuclease-III / DNase-I-like (exonuclease-endonuclease-phosphatase) superfamily. Its UniProt entry carries only generic superfamily keywords (Hydrolase, Magnesium, Manganese, Metal-binding) — the same keywords shared by the two genuine ExoIII proteins Q88IV9/PP_2890 (xthA) and Q88JE2/PP_2707 — but **no curated FUNCTION statement and no BER-specific EC number.** Crc is a catalytically inactive member of this superfamily. In *P. putida* KT2440, Crc is an RNA-binding translational repressor that assembles with Hfq into the Crc–Hfq complex to effect carbon-catabolite repression, binding the 5′ region of target mRNAs to inhibit their translation. This is a direct, experimentally established function in the target strain. **Curation action: remove PP_5292 from the BER bucket** (mark as over-annotation).

> Supporting citation — [PMID: 37348756](https://pubmed.ncbi.nlm.nih.gov/37348756/): *"In Pseudomonas spp., it is mainly mediated by the Crc-Hfq complex which binds to the 5' region of the target mRNAs, thereby inhibiting their translation."* This directly identifies KT2440 Crc as a translational regulator, not a DNA-repair nuclease.

### F002 — MutT (PP_1348) is present but missing from the candidate list

A UniProt proteome search of UP000000556 returns Q88N67 / PP_1348, annotated **"8-oxo-dGTP diphosphatase" (EC 3.6.1.55)** — the MutT/Nudix enzyme of the GO anti-mutator system, which hydrolyzes 8-oxo-dGTP in the nucleotide pool to prevent its misincorporation into DNA. It was absent from the 14-gene candidate metadata. Together with *mutY* (PP_0286) and *mutM/fpg* (PP_5125), MutT completes the three-component 8-oxoguanine defense system. KEGG groups nucleotide-pool sanitization (*mutT*) alongside the BER glycosylases. **Curation action: add PP_1348 to the module** to close the GO-system coverage gap.

### F003 — AP-endonuclease step is served by two Xth paralogs; Nfo absent

Name/gene searches of the proteome for "endonuclease IV"/*nfo*, "endonuclease VIII"/*nei*, and "endonuclease V"/*nfi* all returned **zero hits**. The AP-endonuclease incision step is represented instead by Q88IV9/PP_2890 (*xthA*, EC 3.1.11.2) and a second ExoIII paralog Q88JE2/PP_2707 (both ~270 aa, ExoIII/Mg-Mn hydrolase signature). In *E. coli* and *M. tuberculosis*, XthA (ExoIII) provides principal AP-endonuclease activity in BER and its loss causes hypersensitivity to oxidative/alkylating agents. This establishes an **Xth-only AP-incision architecture** for KT2440.

> Supporting citation — [PMID: 16524897](https://pubmed.ncbi.nlm.nih.gov/16524897/): *"Both are endowed with AP endonucleolytic activity, cleaving the 5' phosphodiester bond adjacent to spontaneous or induced abasic sites in DNA."* This establishes ExoIII (xthA) as a bona fide AP-endonuclease in bacterial BER, supporting that Xth-family paralogs cover the incision step even without Nfo.

### F004 — Three distinct alkylation-glycosylase families; a second Tag paralog (PP_1642) is un-listed

InterPro/Pfam analysis of UP000000556 shows PP_0062 (*tag*) and **PP_1642** both annotated "DNA-3-methyladenine glycosylase I" (Tag family); PP_0705 is AlkA-type "3-methyladenine glycosylase II"; and PP_4812 (Q88DL3) carries Pfam PF02245 + InterPro IPR003180 (methylpurine/AAG superfamily, SSF50486), a family distinct from both Tag and AlkA. PP_4812 has BER keywords but only generic EC 3.2.2.-. PP_1642 was not in the candidate list. The AlkA gene PP_0705 is adjacent to *ada* (PP_0706), consistent with an Ada adaptive-response operon. The alkylation-repair step is thus **redundantly covered**, and the candidate list under-represents the true glycosylase complement.

### F005 — Domain-level scan confirms genuine absence of Endonuclease IV (Nfo)

A proteome scan for xref:pfam-PF01261 (AP_endonuc_2 / EndoIV TIM-barrel clan) returned only three metabolic TIM-barrel proteins — PP_2554 (3-dehydroshikimate dehydratase), PP_2603 (xylose isomerase-like), and PP_4298 — **none** annotated as an AP endonuclease or DNA-repair enzyme. Combined with zero hits for *nfo* / "endonuclease IV" by name, this confirms there is no functional Nfo. Positive controls behaved correctly: PF00730 (HhH-GPD) returned exactly the expected AlkA (PP_0705), MutY (PP_0286), and Nth (PP_1092); PF01035 returned the Ada/Ogt direct-reversal methyltransferases (PP_3017, PP_0706, PP_1356). This rules out a domain-search false negative and confirms the Xth-only architecture is real. **Curation action: mark *nfo* as `not_expected_in_target_taxon`.**

---

## 6. Mechanistic Model / Interpretation

The KT2440 BER pathway can be drawn as a complete short-patch relay in which every canonical station is occupied, with the AP-endonuclease station uniquely reliant on exonuclease III:

```
   Damaged base
   ┌───────────────────────────────────────────────────────────┐
   │  GLYCOSYLASES (base recognition & excision → AP site)       │
   │  • Ung (PP_1413)      uracil                                │
   │  • MutM/Fpg (PP_5125) 8-oxoG:C, Fapy   [+AP lyase]          │
   │  • MutY (PP_0286)     A:8-oxoG                              │
   │  • Nth (PP_1092)      ox. pyrimidines  [+AP lyase]          │
   │  • Tag (PP_0062, PP_1642) / AlkA (PP_0705) / Mpg (PP_4812)  │
   │    → 3-methyladenine (redundant)                           │
   └───────────────────────────────┬───────────────────────────┘
                                    ▼  AP site
   ┌───────────────────────────────────────────────────────────┐
   │  AP-ENDONUCLEASE  — XTH-ONLY (no Nfo/EndoIV)                │
   │  • XthA (PP_2890)    ExoIII, EC 3.1.11.2                    │
   │  • PP_2707           ExoIII paralog                         │
   └───────────────────────────────┬───────────────────────────┘
                                    ▼  nick, 3'-OH / 5'-dRP
   ┌───────────────────────────────────────────────────────────┐
   │  GAP FILLING   • PolA (PP_0123, DNA Pol I)   [bucket 03420] │
   │  NICK SEALING  • LigA (PP_4274, NAD+ ligase) [bucket 03420] │
   │  (ancillary: RecJ PP_1477 resection; LigB PP_4968)         │
   └───────────────────────────────────────────────────────────┘

   PARALLEL "GO SYSTEM" (nucleotide-pool sanitization):
     MutT (PP_1348, 8-oxo-dGTPase) + MutY (PP_0286) + MutM (PP_5125)
     → prevents 8-oxoG-driven G:C→T:A transversions

   NOT A BER ENZYME (remove): Crc (PP_5292) — Crc–Hfq translational repressor
```

Two interpretive points follow. First, the **redundancy in glycosylases** (three alkylation families; bifunctional MutM and Nth carrying their own AP-lyase activity) means the pathway is robust to loss of any single glycosylase, and the true bottleneck for satisfiability is the AP-endonuclease/downstream relay. Second, because AP incision depends on the Xth paralogs alone, KT2440's oxidative-stress resistance profile is predicted to hinge on ExoIII rather than on the EndoIV that dominates in *M. tuberculosis*. This is a testable, curation-relevant prediction and marks a genuine lineage difference rather than a metadata artifact.

The GO system operates as a parallel, three-layered defense against 8-oxoguanine: MutT sanitizes the dNTP pool, MutM removes 8-oxoG from 8-oxoG:C pairs, and MutY removes the mis-inserted adenine from 8-oxoG:A pairs before it is fixed as a transversion. Because MutT was missing from the candidate list, the module as delivered would have under-represented this system by one-third.

---

## 7. Evidence Base

| PMID | Relevance | How it supports/challenges the review |
|------|-----------|----------------------------------------|
| [37348756](https://pubmed.ncbi.nlm.nih.gov/37348756/) | **Direct, KT2440** | Establishes Crc (PP_5292) as a Crc–Hfq translational repressor in *P. putida* KT2440 → confirms BER bucketing of PP_5292 is spurious (F001). |
| [16524897](https://pubmed.ncbi.nlm.nih.gov/16524897/) | Mechanism, *E. coli* | Shows EndoIV and ExoIII both incise AP sites; supports that Xth-family enzymes cover the AP-incision step in KT2440 (F003). |
| [40887175](https://pubmed.ncbi.nlm.nih.gov/40887175/) | Mechanism, *E. coli* | *xthA* deletion alters SOS induction/survival across genotoxins; ExoIII is a key AP-endonuclease in BER — supports Xth centrality (F003). |
| [23936515](https://pubmed.ncbi.nlm.nih.gov/23936515/) | Comparative, *M. tuberculosis* | EndoIV is the *major* AP-endonuclease in *M. tuberculosis*, XthA predominantly a 3′→5′ exonuclease — highlights that KT2440's Nfo absence is a real lineage difference, not universal (F003/F005). |
| [25748880](https://pubmed.ncbi.nlm.nih.gov/25748880/) | Mechanism, *M. tuberculosis* | Characterizes class-II AP-endonuclease/3′-5′ exonuclease XthA catalysis; supports ExoIII as a bona fide BER AP-endonuclease. |
| [26103519](https://pubmed.ncbi.nlm.nih.gov/26103519/) | Mechanism, *M. tuberculosis* | XthA interacts with the β-clamp during BER; reinforces ExoIII's in vivo BER role. |
| [30429516](https://pubmed.ncbi.nlm.nih.gov/30429516/) | *P. aeruginosa* | Maps the Crc post-transcriptional regulon — corroborates Crc's regulatory (non-repair) function across *Pseudomonas*. |
| [33857481](https://pubmed.ncbi.nlm.nih.gov/33857481/) | *Pseudomonas* | Structural dynamics of the Hfq–RNA–Crc translation-repression complex — further confirms Crc's true molecular role. |
| [37823038](https://pubmed.ncbi.nlm.nih.gov/37823038/) | *Pseudomonas* | CbrAB–CrcZ–Hfq/Crc pathway in biocontrol *Pseudomonas* — Crc as a catabolite-repression regulator. |
| [37847735](https://pubmed.ncbi.nlm.nih.gov/37847735/) | Biofilm | Peripheral; biofilm metabolic heterogeneity context. |

**Evidence-strength summary.** Only F001 rests on *direct experimental evidence in the target strain* (KT2440 Crc function). F002, F004, and F005 are established by **direct proteome/domain database inspection** of UP000000556 (strong for presence/absence calls, but the enzymatic activities of the individual proteins are inferred). F003 combines direct proteome absence calls with **mechanistic transfer from *E. coli* and *M. tuberculosis***; transfer of the "ExoIII performs AP incision" principle to KT2440 is strong (conserved enzyme family), but the relative in-vivo contribution of PP_2890 vs PP_2707 is untested.

---

## 8. Limitations and Knowledge Gaps

- **No direct KT2440 biochemistry for the repair enzymes.** With the exception of Crc, none of the KT2440 BER proteins has been characterized biochemically or genetically in this strain. Step assignments are homology- and domain-based. This is adequate for satisfiability curation but not for firm functional claims.
- **Paralog dominance unknown.** For both the AP-endonuclease step (PP_2890 vs PP_2707) and the alkylation-glycosylase step (Tag PP_0062 vs PP_1642 vs AlkA PP_0705 vs Mpg PP_4812), the physiologically dominant enzyme is unknown. Curation should treat these as redundant candidates rather than assigning a single "the" gene.
- **Broad/generic EC and GO mappings.** PP_4812 carries only EC 3.2.2.- and generic BER keywords; its exact substrate specificity is unverified. LigB (PP_4968) has an uncertain physiological role.
- **Nfo absence is a presence/absence inference.** F005 is robust (name search + PF01261 domain scan + positive controls), but functional AP-endonuclease redundancy from an unrecognized fold cannot be formally excluded without an activity assay.
- **Species transfer for the AP-incision model.** The mechanistic weight for "Xth covers AP incision" comes from *E. coli* and *M. tuberculosis*. The *M. tuberculosis* data specifically show EndoIV, not XthA, as the major AP-endonuclease there — a caution that AP-endonuclease dominance is organism-dependent and should not be over-generalized to KT2440.

---

## 9. Module and GO-Curation Recommendations

**Module step calls:**

| Step | Recommended status |
|------|--------------------|
| Uracil glycosylase (Ung, PP_1413) | **covered** |
| 8-oxoG glycosylase (MutM, PP_5125) | **covered** |
| Adenine glycosylase (MutY, PP_0286) | **covered** |
| EndoIII (Nth, PP_1092) | **covered** |
| 3-mA glycosylases (PP_0062/PP_1642/PP_0705/PP_4812) | **covered (redundant)** |
| AP endonuclease (XthA PP_2890, PP_2707) | **covered** (Xth-only) |
| 8-oxo-dGTPase (MutT, PP_1348) | **covered — ADD to module** (currently a gap in metadata) |
| DNA Pol I (PolA, PP_0123) | **covered** (cross-bucket from 03420) |
| DNA ligase (LigA, PP_4274) | **covered** (cross-bucket from 03420) |
| Endonuclease IV (Nfo) | **not_expected_in_target_taxon** |
| Endonuclease VIII (Nei) / Endonuclease V (Nfi) | **not_expected_in_target_taxon** |
| Crc (PP_5292) | **remove — over-annotation** |

**Specific curation edits:**
1. **Remove PP_5292 ("Crc")** from kegg:ppu03410 (over-propagated ExoIII-fold homology; true function is Crc–Hfq translational repression).
2. **Add PP_1348 (MutT)** to the module to complete the MutT+MutY+MutM GO system.
3. **Add PP_1642** (second Tag-family 3-mA glycosylase) to the alkylation-glycosylase step.
4. **Record the Xth-only AP-endonuclease architecture** as a lineage-specific feature and flag *nfo/nei/nfi* absence as `not_expected_in_target_taxon`.
5. **Retain PolA and LigA** as covered downstream steps despite their 03420 primary bucket; note the cross-pathway sharing so the module is not falsely scored as incomplete.

**GO / module-document requests:** No new GO term is required. Consider a module note documenting the "GO system" grouping (MutT/MutY/MutM) so nucleotide-pool sanitization is not lost when it is split across map00230/03410.

---

## 10. Genes to Promote to Full `fetch-gene` Review

Priority order for full gene-level review:

1. **PP_2890 (xthA) and PP_2707** — highest priority. These carry the entire AP-endonuclease step; resolving their individual activities and dominance is central to module confidence given the Nfo absence.
2. **PP_1348 (MutT)** — to formally add and validate the missing GO-system component.
3. **PP_4812 (Mpg/AAG glycosylase)** — generic EC 3.2.2.-; substrate specificity needs verification.
4. **PP_1642 (Tag paralog)** — to confirm it is a functional 3-mA glycosylase and add to the module.
5. **PP_5292 (Crc)** — brief review to formally document and execute its removal from the BER bucket.

---

## 11. Proposed Follow-up Experiments / Actions

- **AP-endonuclease genetics in KT2440.** Construct single (Δ*PP_2890*, Δ*PP_2707*) and double mutants; assay sensitivity to H₂O₂, MMS, and alkylating agents to determine which Xth paralog dominates AP incision and to confirm no cryptic EndoIV-like backup.
- **In vitro AP-incision assay** on purified PP_2890 and PP_2707 to confirm class-II AP-endonuclease activity directly in the target strain.
- **MutT complementation/mutator assay.** Test whether Δ*PP_1348* elevates G:C→T:A transversion rates (rifampicin-resistance mutation spectrum) to confirm its GO-system role in KT2440.
- **Alkylation-glycosylase substrate profiling** for PP_4812 and PP_1642 (MMS survival, in vitro 3-mA excision) to firm up the redundant alkylation step.
- **Database curation execution:** apply the five edits in §9 to the module metadata and re-score satisfiability.

---

## 12. Key References

1. [PMID: 37348756](https://pubmed.ncbi.nlm.nih.gov/37348756/) — Crossing bacterial boundaries: the carbon catabolite repression system Crc-Hfq of *Pseudomonas putida* KT2440 as a tool to control translation in *E. coli*. **(Direct KT2440 evidence for F001.)**
2. [PMID: 16524897](https://pubmed.ncbi.nlm.nih.gov/16524897/) — Endonuclease IV and exonuclease III in the repair/mutagenesis of UVB-induced lesions in *E. coli*. **(Supports F003.)**
3. [PMID: 40887175](https://pubmed.ncbi.nlm.nih.gov/40887175/) — Effect of *xthA* deletion on SOS activation by genotoxic agents in *E. coli*. **(Supports F003.)**
4. [PMID: 23936515](https://pubmed.ncbi.nlm.nih.gov/23936515/) — Endonuclease IV is the major AP endonuclease in *M. tuberculosis*. **(Comparative context for F003/F005.)**
5. [PMID: 25748880](https://pubmed.ncbi.nlm.nih.gov/25748880/) — Substrate recognition and catalysis in the *M. tuberculosis* class-II AP-endonuclease/ExoIII.
6. [PMID: 26103519](https://pubmed.ncbi.nlm.nih.gov/26103519/) — *M. tuberculosis* XthA interactions with the sliding β-clamp.
7. [PMID: 30429516](https://pubmed.ncbi.nlm.nih.gov/30429516/) — Map of the *P. aeruginosa* Crc regulon (post-transcriptional regulation).
8. [PMID: 33857481](https://pubmed.ncbi.nlm.nih.gov/33857481/) — MD simulations of Hfq–RNA–Crc complex assembly in *Pseudomonas*.
9. [PMID: 37823038](https://pubmed.ncbi.nlm.nih.gov/37823038/) — CbrAB–CrcZ–Hfq/Crc pathway in biocontrol *Pseudomonas*.
10. [PMID: 37847735](https://pubmed.ncbi.nlm.nih.gov/37847735/) — Spatial heterogeneity in biofilm metabolism (peripheral context).

---

## Conclusion

Base excision repair is **complete and satisfiable** in *Pseudomonas putida* KT2440. The pathway is covered end-to-end, with notable glycosylase redundancy, an NAD⁺-dependent LigA sealing step, and a distinctive **Xth-only AP-endonuclease architecture** (Endonuclease IV, VIII, and V are absent). Two metadata corrections are required: **remove PP_5292 ("Crc"), an over-propagated ExoIII-fold annotation that is actually a Crc–Hfq translational regulator, and add MutT (PP_1348)**, the 8-oxo-dGTPase that completes the MutT/MutY/MutM GO anti-mutator system.


## Artifacts

- [OpenScientist final report](PSEPK__base-excision-repair__ppu03410-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__base-excision-repair__ppu03410-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:37348756
2. PMID:16524897
3. PMID:40887175
4. PMID:23936515
5. PMID:25748880
6. PMID:26103519
7. PMID:30429516
8. PMID:33857481
9. PMID:37823038
10. PMID:37847735