# DCV1 (YFR012W) — Curation notes

UniProt: P43595 · SGD: S000001908 · systematic name YFR012W · 202 aa · organism *Saccharomyces cerevisiae* S288C (NCBITaxon:559292)

This is an **understudied ("dark") gene**. The primary deliverable is an honest
`knowledge_gaps` section plus carefully-reasoned `description`/`core_functions`
grounded in domain/orthology/literature — never invented function.

## 1. Identity and naming

- Standard name **DCV1** = "**D**emands **C**dc28 kinase activity for **V**iability protein **1**".
  [UniProt P43595 record: `AltName: Full=Demands CDC28 kinase activity for viability protein 1`]
- SGD gene description: "predicted integral membrane protein whose biological role is unknown"; name reflects a genetic interaction with the *cdc28-as1* (analog-sensitive) allele. [SGD locus page S000001908, fetched 2026-07-05]

## 2. What is KNOWN (with provenance)

### Protein architecture (from the UniProt record, verifiable)
- 202 aa precursor with an N-terminal **signal peptide (1–18)** (ECO:0000255) and a mature chain 19–202.
- **Three predicted transmembrane helices** (91–107, 137–155, 168–189) → **multi-pass (polytopic) integral membrane protein** [UniProt FT lines; `SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}`].
- Domain assignments: **Pfam PF06687 (SUR7)**; **InterPro IPR009571 (SUR7/Rim9-like_fungi)** and **IPR051380 (pH-response_reg palI/RIM9)**; **PANTHER PTHR28013** ("Fungal pH-response regulator palI/RIM9"), subfamily **PTHR28013:SF3 "PROTEIN DCV1-RELATED"**.
- UniProt evidence level **PE=3 (Inferred from homology)** — i.e., no direct protein-level experimental characterization of function.

### Family / orthology (from PANTHER PTHR28013 member list, `interpro/panther/PTHR28013/PTHR28013-entries.csv`)
- DCV1 sits in the **Sur7/PalI/Rim9 family** of fungal tetraspan plasma-membrane proteins.
- Its **PANTHER SF3 subfamily** groups it with the canonical **pH-response regulator PalI/Rim9** orthologs across fungi: *A. nidulans* palI (O93956), *S. cerevisiae* **RIM9 (Q04734)**, *C. albicans* RIM9, *N. crassa* prr-5, *S. pombe* mac1 (Q10268), etc. So **DCV1 is a S. cerevisiae paralog of RIM9** within the same subfamily.
- PANTHER family description (LLM-generated, EBI): the palI/RIM9 family is "involved in the regulation of pH response in various fungi … essential for the proteolytic cleavage of transcription factors, such as RIM101 … Some members may also function as pH sensors." **NOTE: this is an LLM family blurb, `is_reviewed_llm: false` — treat as a hypothesis, not established fact for DCV1.**
- Paralog by whole-genome duplication (WGD): **TOS7 / YOL019W** (Q08157; PANTHER SF8). [SGD: "DCV1 has a paralog, TOS7, that arose from the whole genome duplication"]

### Cellular localization
- **Nuclear envelope (GO:0005635)** — **IDA**, assigned by SGD from **PMID:33002606** (date 20201016). [`DCV1-goa.tsv` row]
  - CAVEAT: The cached PMID:33002606 record is **abstract-only** (`full_text_available: false`) and its title/abstract concern the **paralog Tos7 (Yol019w)** localizing to plasma-membrane MCC/eisosome microdomains, not DCV1. I could **not** access the full text (ScienceDirect 403; PubMed MCP OAuth unavailable) to confirm that DCV1/YFR012W was assayed for nuclear-envelope localization. Per curation policy I do **not** REMOVE an experimental (IDA) annotation on paralog grounds — the curator read the full text I cannot see. I ACCEPT it as a localization but flag the verification gap. SGD's own gene summary independently states DCV1 is "specifically localized to the nuclear envelope."
- **IBA (GO_Central) localizations** propagated within PTHR28013:
  - plasma membrane (GO:0005886), cell division site (GO:0032153), growing cell tip (GO:0035838). WITH/FROM includes S. pombe members (PomBase:SPAC13G7.04c, PomBase:SPCC1739.10) and A. nidulans palI (UniProtKB:O93956).
  - **"growing cell tip" (GO:0035838)** = polarized-growth region at the ends of elongated/cylindrical cells (OLS def). This is a **fission-yeast** concept; *S. cerevisiae* is a budding yeast and does not grow by tip extension. This IBA is a **fission-yeast-specific localization over-propagated to budding yeast** and is not appropriate for DCV1.
  - **"cell division site" (GO:0032153)** likewise reflects the S. pombe septation/tip pattern; questionable for budding-yeast DCV1 with no direct evidence.
  - **plasma membrane (GO:0005886)** is family-consistent (Sur7/PalI proteins are PM eisosome/MCC components) and is a defensible IBA localization for a tetraspan PM-family protein, even if DCV1's own IDA points to the nuclear envelope.
- IEA: plasma membrane (InterPro IPR009571 → GO:0005886, GO_REF:0000002) and membrane (UniProt SubCell SL-0162 → GO:0016020, GO_REF:0000044). The generic "membrane" (GO:0016020) is uninformative given 3 TM helices are known; plasma-membrane IEA duplicates the IBA.

### Genetics / phenotype
- **Disruption/deletion phenotype (UniProt DISRUPTION PHENOTYPE, ECO:0000269|PMID:22042866): "Leads to lethality in absence of CDC28."** i.e. *dcv1Δ* is synthetically lethal / sick with loss of Cdc28 (CDK1) activity — the source of the gene name. PMID:22042866 (Zimmermann et al. 2011 PNAS) is a genome-wide chemical-genetic array screen mapping the *CDC28* genetic network (107 strong interactors); DCV1/YFR012W was one of the hits. Cached record is abstract-only and the abstract does not name DCV1, but UniProt curators cite it specifically for this phenotype.
- *dcv1Δ* is **non-essential** in S288C. Reported deletion phenotypes are pleiotropic and subtle (per SGD high-throughput phenotype data): altered metal-ion accumulation (Na+, Cd, Ni resistance), MMS sensitivity, decreased chronological lifespan/competitive fitness, reduced peroxisomal transport. These are dispersed HTP screen readouts, not a coherent molecular function.

## 3. What is NOT known (knowledge gaps)

- **Molecular function: unknown.** No enzymatic activity; no direct binding partner established for DCV1 itself. The Sur7/PalI family has **no catalytic activity** — members are scaffolding/sensor tetraspan membrane proteins. GOA carries only the root MF (GO:0003674) with ND.
- **Biological process: unknown.** GOA carries only the root BP (GO:0008150) with ND. Whether DCV1 participates in the **Rim101 (PalI/Rim9) alkaline-pH response** — the process characterised for its RIM9 paralog — is **untested for DCV1**; the subfamily assignment is suggestive but not evidence. The *cdc28*-dependence phenotype is a genetic interaction, not a defined pathway role.
- **Localization** is only partly resolved: an SGD IDA says nuclear envelope, while family/IBA evidence points to plasma membrane/eisosome. These are not obviously reconcilable and the primary IDA source could not be verified here.
- **Redundancy with paralog TOS7** is untested (no reported *dcv1Δ tos7Δ* double-mutant phenotype).

## 4. Reasoning for annotation actions

- MF root (GO:0003674) ND, BP root (GO:0008150) ND → **ACCEPT** (correctly reflect "function unknown"; these are the honest state of knowledge).
- GO:0005635 nuclear envelope IDA (PMID:33002606) → **KEEP_AS_NON_CORE** (experimental, SGD-curated; keep, defer to curator, note verification gap; it is a localization, not a core function).
- GO:0005886 plasma membrane IBA and duplicate IEA (GO_REF:0000002) → both **MARK_AS_OVER_ANNOTATED** (family-consistent PM localization but no DCV1-specific evidence; DCV1's own IDA is nuclear envelope; kept consistent across evidence types for the same term).
- GO:0032153 cell division site IBA → **REMOVE**. NB (per PR review): GO:0032153 is NOT lineage-specific — the S. cerevisiae bud neck is a bona fide cell division site — so the justification is weak single-source phylogenetic propagation (one S. pombe donor, PomBase:SPCC1739.10) with no DCV1-specific division-site evidence, NOT a taxon mismatch. Failure mode set to SOURCE_EVIDENCE_WEAK + COMPARTMENT_OR_COMPLEX_MISMATCH (LINEAGE_OR_TAXON_MISMATCH reserved for GO:0035838 growing cell tip, which genuinely is a tip-growth concept absent in budding yeast).
- GO:0035838 growing cell tip IBA → **REMOVE** (fission-yeast polarized-tip-growth concept; not applicable to budding yeast S. cerevisiae).
- GO:0016020 membrane IEA (SubCell) → **MARK_AS_OVER_ANNOTATED** (uninformative generic parent; the protein's PM/multi-pass membrane status is already captured more specifically).

No `protein binding` annotations present (good).

## 5. Sources consulted
- UniProt P43595 (`DCV1-uniprot.txt`) — architecture, family, disruption phenotype.
- GOA (`DCV1-goa.tsv`) — 8 annotations.
- PANTHER PTHR28013 member CSV + metadata (`interpro/panther/PTHR28013/`).
- SGD locus page S000001908 (WebFetch 2026-07-05) — description, paralog, phenotypes.
- PMID:33002606 (Tos7 paper, abstract-only cache) — paralog localization.
- PMID:22042866 (Zimmermann 2011 PNAS, abstract-only cache) — CDC28 genetic-network screen (source of DCV1 name/phenotype).
- OLS (GO term defs for GO:0035838, GO:0032153, GO:0005635).
- Falcon deep research: completed (`DCV1-deep-research-falcon.md`, ~29 min, 16 refs). **Concordant** with this review: it finds no DCV1-specific experimental characterization; all function is family-level inference (Sur7/PalI/Rim9 tetraspanner, plasma-membrane/MCC-eisosome, Rim101 pH-response by analogy to RIM9's auxiliary role in the Rim21–Dfg16–Rim9 sensor complex). Its citations are reviews / other-gene primary papers (Athanasopoulos 2019 FEMS Microbiol Rev; Obara 2012 JBC on Rim21; Douglas 2012 mBio on Sur7) — none are DCV1-specific, so they are used as background only and not added as `supporting_text` (falcon file: quote-tokens are not validator-verified per project guidance).
</content>
</invoke>
