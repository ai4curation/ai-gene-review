---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T05:00:52.457688'
end_time: '2026-08-31T05:38:33.024506'
duration_seconds: 2260.57
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: bacterial choline O-sulfate uptake and desulfation
  module_summary: No module YAML was resolved; use the pathway and taxon context.
  module_outline: No module YAML outline available.
  module_connections: No module YAML connections available.
  pathway_query: choline-o-sulfate-utilization
  pathway_id: choline-o-sulfate-utilization
  pathway_name: choline-o-sulfate-utilization
  pathway_source: free-text pathway query
  pathway_context: No local pathway bucket was resolved for this query.
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '0'
  candidate_genes: No local candidate gene table was available or no genes matched
    this pathway/bucket.
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
  path: PSEPK__bacterial-choline-o-sulfate-uptake-and-desulfation__choline-o-sulfate-utilization-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial-choline-o-sulfate-uptake-and-desulfation__choline-o-sulfate-utilization-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

bacterial choline O-sulfate uptake and desulfation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: choline-o-sulfate-utilization
- Resolved ID: choline-o-sulfate-utilization
- Resolved name: choline-o-sulfate-utilization
- Source: free-text pathway query

No local pathway bucket was resolved for this query.

## Candidate Genes From Local Metadata

Candidate gene count: 0

No local candidate gene table was available or no genes matched this pathway/bucket.

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

# Module/Pathway Review: Choline-O-sulfate uptake and desulfation in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Pathway/module:** choline-O-sulfate-utilization (free-text; no local module YAML or candidate gene table supplied)
**Curation intent:** module satisfiability + gene-annotation review
**Evidence date:** 2026-08-31

---

## 1. Executive summary

*P. putida* KT2440 **is genomically equipped to import and desulfate choline-O-sulfate (COS)**, and the module should be marked **satisfiable (largely covered)**. The pathway core is a discrete, isolated three-gene cassette on the chromosome:

- **PP_0077 = *betC*, choline-sulfatase (EC 3.1.6.6)** — the desulfation step (COS → choline + inorganic sulfate). **COVERED** (high-confidence homology + catalytic-motif evidence).
- **PP_0076** — OpuAC/ProX-family periplasmic **choline/COS-binding protein** (uptake). **COVERED, but transporter architecture is ambiguous.**
- **PP_0075** — annotated "choline sulfate transporter" but is actually a **SulP/SLC26 anion (sulfate) permease**; the specific "choline sulfate" label is a **likely over-annotation**. Uptake mechanism = **candidate_uncertain**.

A candidate pathway-specific regulator (**PP_0079**) sits immediately downstream. BetC is a **formylglycine-dependent type-I sulfatase** (canonical C-x-P-x-R motif), so it depends on the maturation enzyme **PP_3353 (formylglycine-generating enzyme, FGE)** — an obligatory accessory step. The liberated **choline** feeds the well-annotated betaine pathway (*betA/betB*), and the liberated **sulfate** enters standard cysteine/sulfur assimilation.

**Important caveat:** essentially all target-taxon evidence is **computational/homology-based**. There is, to our knowledge, **no direct experimental characterization of COS utilization in KT2440**. Functional transfer comes from *Sinorhizobium meliloti* (BetC; strong, same enzyme family) and *Bacillus subtilis* (OpuC-mediated COS uptake; mechanistically informative but transporter-family-divergent).

---

## 2. Target-organism pathway definition

**Included process (pathway boundary):** the *uptake of the plant/fungal-derived osmolyte choline-O-sulfate from the periplasm/environment, followed by intracellular hydrolysis of its sulfate-ester bond to yield free choline + inorganic sulfate.* The module's two committed steps are (i) **COS import** and (ii) **COS desulfation (BetC)**. Sulfate then serves as a **sulfur source**; choline is a **carbon/nitrogen source and osmoprotectant precursor**.

**Neighboring pathways to keep separate (do NOT merge into this module):**
- **Choline → glycine betaine oxidation** (*betA* PP_5064, *betA-I* PP_0056 choline dehydrogenase EC 1.1.99.1; *betB* PP_5063 betaine aldehyde dehydrogenase EC 1.2.1.8) — a *downstream* module that consumes the choline product; it is separately annotated and much better supported.
- **Glycine-betaine catabolism** (*gbcAB* PP_0315/PP_0316 dioxygenase → dimethylglycine …) — further downstream C/N mobilization.
- **Osmoprotectant/quaternary-amine transport** (BCCT carriers *betT-I/II/III* PP_5061/PP_0229/PP_3957; ABC systems *cbcVWX* PP_0294–0296, *opuA* PP_2774, *yehWXYZ* PP_0868–0871) — broad choline/betaine/carnitine transport overview; overlaps but is not COS-specific.
- **Assimilatory sulfate reduction / sulfonate & sulfate-ester scavenging** (Cys pathway; *atsA* PP_3352 arylsulfatase; alkylsulfatase PP_2045) — receives the sulfate product but is a different pathway. Keep the general "sulfur-limitation ester scavenging" map separate from the choline-specific COS module.

**Alternate names / database definitions:** choline-O-sulphate; choline sulfate; EC 3.1.6.6 = *choline-sulfatase*; MetaCyc/BioCyc frames COS desulfation within "choline degradation"/"glycine betaine biosynthesis" supersets; KEGG lists *ppu:PP_0077* with the K-ortholog for choline-sulfatase. InterPro family **IPR017785 (Choline-sulfatase)** is the tightest definition and cleanly distinguishes BetC from generic arylsulfatases.

---

## 3. Expected step model

| Step | Expected function | Best KT2440 candidate | Call |
|------|-------------------|-----------------------|------|
| S1 | COS import across inner membrane | PP_0075 (SulP permease) and/or PP_0076 (ABC SBP) + a QA-ABC permease/ATPase | **candidate_uncertain** |
| S2 | COS desulfation → choline + sulfate | **PP_0077 (betC, EC 3.1.6.6)** | **covered** |
| S2a | Sulfatase maturation (Cys→formylglycine) | **PP_3353 (FGE)** | **covered (accessory, obligatory)** |
| S3 | Fate of choline (oxidation to betaine) | *betA* PP_5064 / PP_0056; *betB* PP_5063 | covered (separate module) |
| S4 | Fate of sulfate (assimilation) | Cys/sulfate-assimilation genes | covered (separate module) |
| R | Pathway-specific transcriptional regulation | PP_0079 (adjacent regulator) | candidate |

---

## 4. Candidate genes and evidence

**PP_0077 — *betC*, Choline-sulfatase (Q88RQ2; EC 3.1.6.6; 505 aa).** *High confidence.*
- Evidence: InterPro **IPR017785 (dedicated Choline-sulfatase family)** + IPR000917 Sulfatase_N + IPR025863 (choline-sulfatase C-domain), Pfam PF00884 + PF12411; GO:0047753 choline-sulfatase activity. UniProt proteinExistence = "3: Inferred from homology."
- Sequence-level confirmation: canonical **type-I sulfatase catalytic motif C51-A-P-S-R55** (…AY**CAPSR**FTL…), the Cys that is oxidized to Cα-formylglycine.
- Curation caveat: no direct KT2440 assay; functional transfer from *S. meliloti* BetC (PMID 9736747) is **strong** (same InterPro family, same motif, syntenic role). **Promote to full `fetch-gene` review.**

**PP_0076 — Choline/betaine-binding protein (Q88RQ3; 307 aa).** *Medium confidence for uptake, low for COS specificity.*
- Evidence: Pfam **PF04069 OpuAC**, InterPro IPR017783 (ABC choline substrate-binding) / IPR007210 (ABC glycine-betaine SBP); GO:0033265 choline binding, GO:0015871 choline transport; signal peptide; proteinExistence "4: Predicted."
- Caveat: it is the **periplasmic SBP of an ABC importer, but the cognate permease/ATPase are not in the immediate cluster** (orphan SBP). It may pair with a shared QA-ABC permease/ATPase (e.g., *yehWXYZ* PP_0868–0871 or *cbcVW* PP_0294–0295). Whether it binds COS specifically vs. choline is unproven. Paralog ambiguity with *cbcX* PP_0296, *betX* PP_1741, PP_0870.

**PP_0075 — "Choline sulfate transporter" (Q88RQ4; 521 aa).** *Likely mis-specific annotation.*
- Evidence: InterPro **IPR001902/IPR011547 (SLC26A/SulP family)** + STAS domain (PF01740) + PF00916 Sulfate_transp; GO:0055085 transmembrane transport; proteinExistence "4: Predicted." This is a **SulP/SLC26 anion (typically inorganic sulfate) permease**, not a BCCT/QA carrier.
- Interpretation: the specific "choline sulfate" substrate name is **probable over-annotation derived from gene neighborhood** (it abuts *betC*). Plausible real roles: import of the anionic COS ester, or import/recycling of the inorganic **sulfate product**. **Substrate = uncertain; promote to full review and correct the substrate-specific label.**

**PP_0079 — Transcriptional regulator (Q88RQ0; 299 aa).** Adjacent to the cassette; candidate local regulator (analogous to BetI in the *S. meliloti bet* operon). Not yet assigned a family here — worth a `fetch-gene` review.

**PP_3353 — Sulfatase-modifying factor / FGE (Q88HK3; 341 aa).** Obligatory maturation enzyme for BetC (and for *atsA* PP_3352, alkylsulfatase PP_2045). Should be recorded as an **accessory module dependency**, not a per-organism gap.

**Downstream (context, separate modules):** *betA* PP_5064 & *betA-I* PP_0056 (choline dehydrogenase), *betB* PP_5063 (betaine aldehyde dehydrogenase) — high-confidence, HAMAP-ruled; consume the choline product.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **Likely over-annotation (flag):** PP_0075 "choline sulfate transporter" — family is SulP/SLC26; substrate specificity for choline-O-sulfate is unsupported. Recommend relabeling to "SulP-family sulfate/anion permease (putative COS/sulfate transporter)."
- **Ambiguity — which transporter actually imports COS:** three non-exclusive possibilities: (a) PP_0075 SulP permease imports the COS anion; (b) PP_0076 ABC-SBP (with a shared QA-ABC permease/ATPase) imports COS as a choline ester; (c) broad BCCT/OpuC-like systems co-import COS (as in *B. subtilis*, where OpuC handles COS; PMID 9925583). **Step S1 = candidate_uncertain.**
- **PP_0075 is probably not redundant inorganic-sulfate transport:** KT2440 already encodes a dedicated assimilatory sulfate ABC importer (*cysA* PP_5168 [EC 7.3.2.3], *cysW* PP_5169, sulfate-binding *sbp-I* PP_4305 / *sbp-II* PP_5171). Because inorganic-sulfate uptake is already covered by that system, the SulP permease PP_0075 embedded in the COS cassette is more plausibly dedicated to importing the anionic **COS ester** (or recycling the liberated sulfate) — modestly raising confidence that PP_0075 belongs to the uptake step, though its substrate remains experimentally unproven.
- **PP_0078** has no distinct UniProt entry (small/hypothetical ORF); the cassette effectively reads PP_0075–PP_0076–PP_0077 followed by regulator PP_0079.
- **Orphan SBP:** PP_0076 lacks an adjacent permease/ATPase — a genuine module-structure question.
- **No direct KT2440 phenotype:** growth on COS as sole S (or C/N) source, and *betC*/PP_0075/PP_0076 mutant phenotypes, have not been reported for KT2440. All calls are homology/motif-based.
- **Not a gap:** the desulfation step itself is well covered; do **not** mark the module as a gap.

---

## 6. Module and GO-curation recommendations

- **S2 desulfation → COVERED** by PP_0077 (*betC*, EC 3.1.6.6). GO:0047753 (choline-sulfatase activity) is appropriate and well-supported.
- **S2a maturation → COVERED (accessory)**: add PP_3353 (FGE) as an obligatory dependency of any BetC-containing module.
- **S1 uptake → CANDIDATE_UNCERTAIN**: retain PP_0075 and PP_0076 as candidates but flag substrate uncertainty; do not assert a specific COS transporter.
- **Regulation**: add PP_0079 as candidate regulator (module_needs_revision if a regulatory step is expected but absent from the generic module).
- **Module boundary**: keep COS-utilization (import + desulfation) **distinct** from the downstream choline→betaine oxidation module and from general sulfur-ester scavenging; the generic module should **not** absorb *betA/betB* or the Cys pathway.
- **GO requests**: existing GO terms (GO:0047753 choline-sulfatase; GO:0015871 choline transport) suffice; a dedicated "choline-O-sulfate transmembrane transporter activity" child term would help disambiguate PP_0075/PP_0076 if such a term is lacking.

---

## 7. Genes to promote to full review

1. **PP_0077 (*betC*)** — anchor desulfation gene; verify motif, FGE dependency, and *S. meliloti* orthology. *(highest priority)*
2. **PP_0075** — correct/qualify the "choline sulfate transporter" annotation; determine SulP substrate.
3. **PP_0076** — confirm as COS/choline SBP and identify its cognate ABC permease/ATPase.
4. **PP_0079** — assess as pathway-specific transcriptional regulator.
5. **PP_3353 (FGE)** — record as shared maturation dependency.

---

## 8. Key references

- Osterås M, Boncompagni E, Vincent N, Poggi M-C, Le Rudulier D. *Presence of a gene encoding choline sulfatase in Sinorhizobium meliloti bet operon: choline-O-sulfate is metabolized into glycine betaine.* PNAS 1998. **PMID 9736747.** — Defines BetC/choline-sulfatase (EC 3.1.6.6); COS used as sole C/N/S source via a functional *bet* locus. (*Strong transfer to KT2440: same enzyme family/motif.*)
- Nau-Wagner G, Boch J, Le Good JA, Bremer E. *High-affinity transport of choline-O-sulfate and its use as a compatible solute in Bacillus subtilis.* Appl Environ Microbiol 1999. **PMID 9925583.** — COS acquired via the OpuC ABC transporter; informs the uptake-mechanism question. (*Mechanistic, transporter-family divergent from PP_0075.*)
- Holt S, Kankipati H, De Graeve S, et al. *Major sulfonate transporter Soa1 in Saccharomyces cerevisiae and considerable substrate diversity in its fungal family.* 2017. **PMID 28165463.** — Establishes COS/sulfonates as prominent environmental sulfur sources (ecological rationale).
- UniProt/InterPro/KEGG (taxon 160488): Q88RQ2 (PP_0077 betC), Q88RQ3 (PP_0076), Q88RQ4 (PP_0075), Q88HK3 (PP_3353 FGE); InterPro IPR017785 (Choline-sulfatase), IPR001902 (SLC26A/SulP). Accessed 2026-08-31. (*Computational evidence.*)

**Uncertainty statement:** desulfation (BetC) assignment is **high-confidence homology + sequence motif**; uptake assignments are **low-to-medium confidence, computational only**; no direct KT2440 experimental data exist. Resolving experiments: growth of KT2440 and Δ*betC*/ΔPP_0075/ΔPP_0076 mutants on COS as sole sulfur (and C/N) source; ¹⁴C-COS transport assays; and induction/RNA-seq of PP_0075–0079 under sulfate limitation or COS exposure.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial-choline-o-sulfate-uptake-and-desulfation__choline-o-sulfate-utilization-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial-choline-o-sulfate-uptake-and-desulfation__choline-o-sulfate-utilization-deep-research-openscientist_artifacts/final_report.pdf)