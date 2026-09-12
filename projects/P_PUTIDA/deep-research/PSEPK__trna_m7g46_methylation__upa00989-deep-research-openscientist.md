---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T13:05:39.834713'
end_time: '2026-07-11T13:17:23.466959'
duration_seconds: 703.63
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: tRNA m7G46 methylation
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00989 module for SAM-dependent
    formation of N7-methylguanosine at position 46 of tRNA. The module is centered
    on TrmB, the tRNA (guanine(46)-N7)-methyltransferase encoded by PP_5103. Broader
    RNA methylation and methyltransferase-complex annotations are retained only as
    context unless supported by more specific evidence.
  module_outline: "- tRNA m7G46 methylation\n  - 1. Formation of m7G46 in tRNA\n \
    \ - TrmB tRNA guanine-46 N7 methylation\n    - trmB: tRNA m7G46 methyltransferase\
    \ (molecular player: PSEPK trmB; activity or role: tRNA (guanine(46)-N7)-methyltransferase\
    \ activity)"
  module_connections: No explicit connections.
  pathway_query: UPA00989
  pathway_id: UPA00989
  pathway_name: UniPathway UPA00989
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00989 with 1 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '1'
  candidate_genes: '- trmB: PP_5103 | Q88CS7 | tRNA (guanine-N(7)-)-methyltransferase
    (EC 2.1.1.33) (tRNA (guanine(46)-N(7))-methyltransferase) (tRNA(m7G46)-methyltransferase)
    (EC 2.1.1.33; primary bucket unipathway:UPA00989)'
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
citation_count: 5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__trna_m7g46_methylation__upa00989-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__trna_m7g46_methylation__upa00989-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

tRNA m7G46 methylation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00989
- Resolved ID: UPA00989
- Resolved name: UniPathway UPA00989
- Source: UniPathway

Resolved local bucket unipathway:UPA00989 with 1 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 1

- trmB: PP_5103 | Q88CS7 | tRNA (guanine-N(7)-)-methyltransferase (EC 2.1.1.33) (tRNA (guanine(46)-N(7))-methyltransferase) (tRNA(m7G46)-methyltransferase) (EC 2.1.1.33; primary bucket unipathway:UPA00989)

## Generic Module Context

### Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00989 module for SAM-dependent formation of N7-methylguanosine at position 46 of tRNA. The module is centered on TrmB, the tRNA (guanine(46)-N7)-methyltransferase encoded by PP_5103. Broader RNA methylation and methyltransferase-complex annotations are retained only as context unless supported by more specific evidence.

### Provisional Biological Outline

- tRNA m7G46 methylation
  - 1. Formation of m7G46 in tRNA
  - TrmB tRNA guanine-46 N7 methylation
    - trmB: tRNA m7G46 methyltransferase (molecular player: PSEPK trmB; activity or role: tRNA (guanine(46)-N7)-methyltransferase activity)

### Known Relationships Among Steps

No explicit connections.

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

# Species-aware Module Review: tRNA m7G46 Methylation (UniPathway UPA00989) in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Module / bucket:** unipathway:UPA00989 — "tRNA modification; N(7)-methylguanine-tRNA biosynthesis"
**Candidate gene:** trmB (PP_5103 | UniProt Q88CS7)

---

## Summary

The UniPathway **UPA00989** module — SAM-dependent formation of **N7-methylguanosine at position 46 (m7G46)** in the tRNA variable loop (EC 2.1.1.33) — is a **single biochemical step catalyzed by a single enzyme**. In *Pseudomonas putida* KT2440 this module is **fully satisfied ("covered")** by one gene, **trmB / PP_5103** (UniProt **Q88CS7**, TRMB_PSEPK, a reviewed Swiss-Prot entry). The gene maps cleanly to the TrmB family (HAMAP MF_01057, TIGR00091, Pfam PF02390, InterPro IPR003358, PROSITE PS51625), and a proteome-wide search of UP000000556 confirms it is the **unique** EC 2.1.1.33 / PF02390 protein in KT2440. There is no paralog ambiguity, and no second subunit or accessory step is expected.

The target-strain annotation itself rests on **rule-based homology evidence** (UniRule/HAMAP MF_01057; protein existence "inferred from homology"; ECO:0000255) rather than a direct *P. putida* KT2440 experiment. However, **functional transfer is very strong**: KT2440 TrmB is **80.2% identical** across its full length to the experimentally validated *P. aeruginosa* PAO1 TrmB, which was directly shown to form m7G46 on 23 tRNA substrates and to modulate translation of Phe/Asp-rich mRNAs and H2O2 resistance ([PMID: 31428787](https://pubmed.ncbi.nlm.nih.gov/31428787/)). Because both organisms are in the same genus and share the identical single-domain, single-subunit TrmB architecture, transfer of function to KT2440 is robust.

The single most important **curation action** is to flag the Cellular Component term **GO:0043527 "tRNA methyltransferase complex"** on Q88CS7 as a **likely over-propagated annotation**. That complex term derives from the eukaryotic m7G46 enzyme, an obligate **Trm8–Trm82 (METTL1–WDR4) heterodimer**, whereas bacterial TrmB is a **monomeric, stand-alone** class I SAM-methyltransferase. The GO:0043527 annotation on Q88CS7 carries only phylogenetically propagated (IEA:TreeGrafter) evidence and should be removed or down-weighted for the bacterial ortholog. With that caveat, the module is clean: one step, one enzyme, high-confidence covered.

---

## Target-organism pathway definition

**Process included (and only this):** UPA00989 covers the transfer of a methyl group from S-adenosyl-L-methionine (SAM) to the **N7 atom of guanine 46** in the variable/tertiary core of cytoplasmic tRNAs, producing **m7G46 + S-adenosyl-L-homocysteine (SAH)**. m7G46 stabilizes tRNA tertiary structure and, in bacteria, feeds a "modification network" that promotes other modifications and tRNA stability ([PMID: 19934251](https://pubmed.ncbi.nlm.nih.gov/19934251/)).

**Reaction (UniProt catalytic activity):**

```
guanosine(46) in tRNA  +  SAM   --TrmB-->   N7-methylguanosine(46) in tRNA  +  SAH   (EC 2.1.1.33)
```

**Enzyme:** TrmB (PP_5103, Q88CS7), a 240-aa class I (Rossmann-fold) SAM-dependent methyltransferase.

**Alternate names / database-specific definitions:**
- **UniPathway:** UPA00989 — "tRNA modification; N(7)-methylguanine-tRNA biosynthesis."
- **Enzyme:** EC **2.1.1.33**; names "tRNA (guanine-N(7)-)-methyltransferase," "tRNA (guanine(46)-N(7))-methyltransferase," "tRNA(m7G46)-methyltransferase."
- **Gene name:** *trmB* (bacterial; = *yggH* in *E. coli*). Eukaryotic orthologs are **Trm8/Trm82** (yeast) and **METTL1/WDR4** (human) — the same chemistry, but a *different family boundary and quaternary structure* that must **not** be merged into the bacterial module.
- **Family identifiers:** HAMAP **MF_01057**; TIGRFAM **TIGR00091**; InterPro **IPR003358**; Pfam **PF02390** (Methyltransf_4); PROSITE **PS51625**; SUPFAM SSF53335.

**Boundaries — what to keep separate:**
- This is **not** a general "RNA methylation" or "methyltransferase complex" bucket.
- Other tRNA methyltransferases (TrmA/m5U54, TrmD/m1G37, TrmH/Gm18, TrmFO, m5C, etc.) are **distinct modules** that share only the class I SAM-MTase fold; do not collapse them into UPA00989.
- Overview/superpathway "tRNA modification" maps should be kept separate from this single-step module.

---

## Expected step model

UPA00989 is a **one-step module**:

| Step | Reaction | Expected enzyme | KT2440 gene | Status |
|------|----------|-----------------|-------------|--------|
| 1 (only step) | tRNA-G46 + SAM → tRNA-m7G46 + SAH | tRNA (guanine46-N7)-methyltransferase (EC 2.1.1.33) | trmB / PP_5103 (Q88CS7) | **Covered** |

There are no upstream/downstream enzymatic steps within this UniPathway. **No accessory/second subunit is expected** — the eukaryotic Trm82/WDR4 partner has no bacterial counterpart, so a "missing second subunit" is `not_expected_in_target_taxon`, not a gap. SAM supply and tRNA substrate provision are shared cellular resources, not module steps.

---

## Key Findings

### Finding 1 — The module is satisfied by a single gene, trmB/PP_5103 (Q88CS7)

The UPA00989 module is fully satisfied in *P. putida* KT2440 by a single gene. UniProt **Q88CS7** (TRMB_PSEPK, reviewed Swiss-Prot) is annotated with gene *trmB*, ordered locus **PP_5103**, EC 2.1.1.33, recommended name "tRNA (guanine-N(7)-)-methyltransferase," and a PATHWAY annotation of "tRNA modification; N(7)-methylguanine-tRNA biosynthesis" — exactly UPA00989. The catalytic activity is defined as guanosine(46) in tRNA + SAM → m7G46 in tRNA + SAH. The protein is 240 aa with a class I SAM-MTase fold, and carries a consistent stack of family assignments (HAMAP MF_01057, TIGR00091, InterPro IPR003358, Pfam PF02390, PROSITE PS51625). This is an unambiguous, reviewed, single-step-to-single-gene mapping.

### Finding 2 — TrmB function is experimentally validated in the same genus

The functional assignment is anchored by direct experiments in related bacteria. In *P. aeruginosa*, *trmB* was shown to encode a tRNA guanine(46)-N7-methyltransferase that forms m7G46 in the tRNA variable loop, acting on 23 identified tRNA substrates; loss of *trmB* reduced translation of Phe/Asp-enriched mRNAs (*katA*, *katB*) and caused H2O2 sensitivity ([PMID: 31428787](https://pubmed.ncbi.nlm.nih.gov/31428787/)). In *Thermus thermophilus*, TrmB/m7G46 is required for viability at high temperature via a tRNA modification network ([PMID: 19934251](https://pubmed.ncbi.nlm.nih.gov/19934251/)). For KT2440 itself, the UniProt evidence is rule-based (ECO:0000255; UniRule MF_01057; protein existence "inferred from homology"), so there is no direct *P. putida* experiment — but the same-genus *Pseudomonas* validation makes transfer strong.

> [PMID: 31428787]: "the P. aeruginosa trmB gene encodes a tRNA guanine (46)-N7-methyltransferase that catalyzes the formation of m7G46 in the tRNA variable loop"
>
> [PMID: 19934251]: "N(7)-methylguanine at position 46 (m(7)G46) in tRNA is produced by tRNA (m(7)G46) methyltransferase (TrmB)"

### Finding 3 — GO:0043527 "tRNA methyltransferase complex" is a likely over-propagation

Q88CS7 carries **GO:0043527** (C: tRNA methyltransferase complex) with evidence code **IEA:TreeGrafter** — purely phylogenetic propagation, not experimental — alongside the appropriate GO:0008176 (F: tRNA guanine46-N7-methyltransferase activity, IEA:UniProtKB-UniRule). The complex term is a **eukaryotic feature**: the yeast m7G46 enzyme is an obligate **Trm8–Trm82 heterodimer** ([PMID: 18029735](https://pubmed.ncbi.nlm.nih.gov/18029735/)), and the human ortholog is the METTL1–WDR4 heterodimer ([PMID: 36599982](https://pubmed.ncbi.nlm.nih.gov/36599982/)). By contrast, bacterial TrmB acts as a **single subunit** with less strict tRNA recognition, and a structural model describes it as a stand-alone class I SAM-MTase bound to tRNA ([PMID: 34006170](https://pubmed.ncbi.nlm.nih.gov/34006170/)). The heterogeneous PANTHER family PTHR23417 to which this entry maps ("KDO transferase / tRNA guanine-N7-methyltransferase," garbled subfamily label) is the likely source of the noisy complex term.

> [PMID: 18029735]: "Yeast tRNA (m(7)G46) methyltransferase contains two protein subunits (Trm8 and Trm82)"

### Finding 4 — PP_5103 is the unique TrmB/EC 2.1.1.33 protein in KT2440 (no paralog, no missing subunit)

A UniProtKB proteome search of UP000000556 returns **exactly one** EC 2.1.1.33 hit (Q88CS7/PP_5103), **exactly one** Pfam PF02390 (Methyltransf_4/TrmB) hit (Q88CS7), and the gene name *trmB* returns only Q88CS7. There is no second TrmB-family paralog and no annotated Trm82/WDR4-like accessory-subunit gene. This confirms a clean one-step-to-one-gene mapping with no paralog ambiguity and no genuine subunit gap.

### Finding 5 — 80% identity to the validated *P. aeruginosa* TrmB makes transfer very strong

Global (Needleman–Wunsch) pairwise alignment gives: Q88CS7 (KT2440, 240 aa) vs Q9I6B3 (TRMB_PSEAE, *P. aeruginosa* PAO1, 244 aa — the enzyme characterized in PMID 31428787) = **80.2% identity** over 237 aligned residues; vs P0A8I5 (TRMB_ECOLI, 239 aa) = 59.4%. All three are full-length single-domain TrmB orthologs. Such high full-length identity to a directly assayed same-genus ortholog upgrades confidence in the "covered" call well beyond generic UniRule homology.

| Comparison | Identity | Aligned residues | Basis |
|------------|----------|------------------|-------|
| KT2440 Q88CS7 vs *P. aeruginosa* Q9I6B3 | **80.2%** | 237 | Same-genus, experimentally validated ortholog |
| KT2440 Q88CS7 vs *E. coli* P0A8I5 | 59.4% | full-length | Distant bacterial ortholog |

---

## Mechanistic Model / Interpretation

The module is best understood as a **single node** with well-defined inputs/outputs and an experimentally anchored genus-level ortholog:

```
   SAM                          SAH
    |                            ^
    v                            |
[ tRNA-G46 ] --- TrmB (PP_5103, Q88CS7, MONOMER) ---> [ tRNA-m7G46 ]
                        |
             80.2% identity to P. aeruginosa TrmB
             (Q9I6B3, experimentally validated, PMID 31428787)
                        |
             59.4% identity to E. coli TrmB (P0A8I5)

  Eukaryotic contrast:  Trm8–Trm82 (yeast) / METTL1–WDR4 (human) = obligate HETERODIMER
  Bacterial reality:    TrmB = single-subunit enzyme  =>  GO:0043527 (complex) is OVER-PROPAGATED
```

The curation narrative is simple and confident: (1) the module is one step; (2) KT2440 encodes exactly one enzyme for it; (3) that enzyme is nearly identical to a directly validated *Pseudomonas* ortholog; (4) the only quaternary-structure annotation in the record (a complex CC term) is a eukaryote-derived artifact and should be flagged. Downstream biology — the tRNA-modification network, rapid tRNA decay, and translational/oxidative-stress phenotypes — is a *consequence* of the modification, not an additional catalytic step, and must not expand the module boundary.

---

## Candidate gene assessment (curation detail)

**trmB — PP_5103 — Q88CS7 (TRMB_PSEPK)**

| Attribute | Value |
|-----------|-------|
| Role | tRNA (guanine46-N7)-methyltransferase; forms m7G46 (GO:0008176) |
| Target-strain evidence | Rule-based homology (ECO:0000255; HAMAP MF_01057; protein existence "inferred from homology"); reviewed Swiss-Prot |
| Family support | HAMAP MF_01057; TIGR00091; Pfam PF02390; InterPro IPR003358; PROSITE PS51625; SUPFAM SSF53335 |
| Length | 240 aa (consistent with monomeric bacterial TrmB) |
| Cross-species support | *P. aeruginosa* (PMID 31428787), *T. thermophilus* (PMID 19934251) |
| Sequence transfer | 80.2% identical to validated *P. aeruginosa* Q9I6B3; 59.4% to *E. coli* P0A8I5 |
| Paralog ambiguity | None — sole EC 2.1.1.33/PF02390/*trmB* protein in UP000000556 |

**Curation caveats:**
- **GO:0043527** "tRNA methyltransferase complex" (IEA:TreeGrafter) is over-propagated from the eukaryotic heterodimer; flag/remove for the monomeric bacterial entry.
- **PANTHER PTHR23417** is heterogeneous (mixes KDO transferase / tRNA-guanine-N7-MTase); do not use PANTHER subfamily text as the authoritative name — HAMAP/TIGRFAM are the reliable anchors.
- Broad fold-level EC/GO terms (class I SAM-MTase) are shared with unrelated MTases, but the specific TrmB signatures resolve identity cleanly.

---

## Gaps, ambiguities, and likely over-annotations

- **No missing steps.** The pathway has one reaction and it is encoded.
- **Proteome-wide uniqueness (verified):** exactly one EC 2.1.1.33, one PF02390, and one *trmB* in UP000000556 — no second paralog, no annotated Trm82/WDR4-like subunit.
- **Not expected in this organism:** a Trm82/WDR4-like accessory subunit (contrast the yeast obligate heterodimer, [PMID: 18029735](https://pubmed.ncbi.nlm.nih.gov/18029735/)). Do **not** open a gap for a missing second subunit.
- **Likely over-annotation:** GO:0043527 "tRNA methyltransferase complex" (CC) — over-propagated; the MF term GO:0008176 is correct.
- **Direct target-strain data gap:** no published *P. putida* KT2440 biochemical/knockout study of *trmB*; the annotation rests on UniRule homology plus strong genus-level experiments.

---

## Module and GO-curation recommendations

| Module element | Recommended status | Rationale |
|----------------|--------------------|-----------|
| Step 1: m7G46 formation (trmB/PP_5103) | **covered** (high confidence) | Sole EC 2.1.1.33/PF02390 protein; 80% identical to validated *P. aeruginosa* TrmB |
| Second subunit / accessory step | **not_expected_in_target_taxon** | Bacterial TrmB is monomeric; no Trm82/WDR4 counterpart |
| Overall module UPA00989 | **satisfied / covered** | Single-step, single-enzyme; no residual gaps |
| Generic module boundaries | **correct for this organism** | One-step scope matches bacterial biology; no revision needed |

**GO-curation actions:**
1. **Flag/remove GO:0043527** (tRNA methyltransferase complex) on Q88CS7 as over-propagated for the monomeric bacterial enzyme (evidence IEA:TreeGrafter only).
2. **Retain** GO:0008176 (tRNA guanine46-N7-methyltransferase activity) and a tRNA-methylation BP term (e.g., GO:0106004 / GO:0030488).
3. **No new module document or GO term is needed** — existing terms cover the biology; the only action is trimming the complex CC term.

---

## Genes to promote to full review

- **trmB (PP_5103 / Q88CS7):** promote to full `fetch-gene` review **only to record the GO complex-term correction** and to upgrade the evidence note (cite same-genus experimental validation, PMID 31428787; record 80% identity to Q9I6B3). The gene identity is unambiguous and does not require reassignment. Priority: **low-to-moderate** (annotation cleanup, not identity resolution). No other genes warrant promotion, as the proteome contains no paralog or candidate alternative.

---

## Evidence Base

| PMID | Paper (abbrev.) | Role in this review |
|------|-----------------|---------------------|
| [31428787](https://pubmed.ncbi.nlm.nih.gov/31428787/) | *TrmB, a tRNA m7G46 methyltransferase … in Pseudomonas aeruginosa* (2019) | **Same-genus experimental anchor.** Direct demonstration that *Pseudomonas* TrmB forms m7G46 (23 substrates) and affects katA/katB translation and H2O2 resistance — the strongest transfer basis for KT2440. |
| [19934251](https://pubmed.ncbi.nlm.nih.gov/19934251/) | *m7G46 in tRNA from Thermus thermophilus required for viability at high temperature* (2010) | Confirms TrmB catalyzes the defining UPA00989 reaction and places m7G46 in a tRNA modification network. |
| [18029735](https://pubmed.ncbi.nlm.nih.gov/18029735/) | *Hetero subunit interaction … of yeast tRNA (m7G46) methyltransferase* (2007) | Establishes the complex/heterodimer as a **eukaryotic feature** (Trm8+Trm82) — the basis for flagging GO:0043527 in the bacterial entry. |
| [34006170](https://pubmed.ncbi.nlm.nih.gov/34006170/) | *Structural model of the M7G46 methyltransferase TrmB in complex with tRNA* (2021) | Describes bacterial TrmB as a monomeric, stand-alone class I SAM-MTase. |
| [36599982](https://pubmed.ncbi.nlm.nih.gov/36599982/) | *Structures and mechanisms of tRNA methylation by METTL1-WDR4* (2023) | Human ortholog is a heterodimer — parallels the yeast case, contrasts with bacteria. |
| [16387656](https://pubmed.ncbi.nlm.nih.gov/16387656/) | *Rapid tRNA decay from lack of nonessential modifications* (2006) | Places m7G46 (Trm8/Trm82) in the RTD network — downstream biology, out of module scope. |
| [22895820](https://pubmed.ncbi.nlm.nih.gov/22895820/) | *Yeast RTD pathway competes with EF-1A for hypomodified tRNAs* (2012) | Further RTD/network context; not part of the catalytic module. |
| [38977661](https://pubmed.ncbi.nlm.nih.gov/38977661/) | *Perturbation of METTL1-mediated tRNA m7G …* (2024) | Eukaryotic functional consequences of m7G46 loss; context only. |

Additional anchors: UniProt **Q88CS7** (TRMB_PSEPK); HAMAP **MF_01057**; UniPathway **UPA00989**.

---

## Limitations and Knowledge Gaps

- **No direct KT2440 experiment.** All target-strain evidence is homology/UniRule (ECO:0000255). The functional call depends on transfer from *P. aeruginosa*; while 80% single-domain identity makes this strong, it is not a KT2440-specific demonstration of m7G46 formation.
- **Substrate scope inferred.** The 23-tRNA substrate set was mapped in *P. aeruginosa*; the exact set of KT2440 tRNAs bearing m7G46 is not experimentally defined.
- **Phenotype unverified in KT2440.** The H2O2-resistance / catalase-translation role is a *P. aeruginosa* finding; whether *trmB* loss produces the same oxidative-stress phenotype in KT2440 is untested.
- **PANTHER family noise.** The heterogeneous PTHR23417 assignment is the probable origin of the over-propagated complex term; other spuriously propagated terms should be checked during full review.

---

## Proposed Follow-up Experiments / Actions

1. **Curation (immediate):** Flag/remove **GO:0043527** on Q88CS7; retain GO:0008176 and a tRNA-methylation BP term. Record the *P. aeruginosa* 80%-identity ortholog and PMID 31428787 as the transfer basis in the gene note.
2. **Mark module UPA00989 as covered** for KT2440 with a single-step model; record "second subunit" as `not_expected_in_target_taxon`.
3. **Optional experimental confirmation (low priority):** LC-MS/MS or primer-extension analysis of bulk KT2440 tRNA ± Δ*trmB* (PP_5103) to directly confirm m7G46 in the target strain and enumerate KT2440 substrates.
4. **Optional phenotype test:** Assess H2O2 sensitivity of a KT2440 Δ*trmB* mutant to test whether the *P. aeruginosa* oxidative-stress role transfers, given KT2440's own catalase repertoire.
5. **No new module document or GO term request is needed.**

---

### Uncertainty statement

The only *direct* target-strain evidence is homology-based (UniProt ECO:0000255, UniRule). All functional claims are inferred from (a) unambiguous TrmB family signatures, (b) 80.2% full-length identity to the experimentally validated *P. aeruginosa* PAO1 TrmB (Q9I6B3), and (c) experimental data in related bacteria (*P. aeruginosa*, *T. thermophilus*). Transfer of function to *P. putida* KT2440 is judged **strong**; the complex-term over-annotation judgment is **high confidence**, based on the well-established monomeric nature of bacterial TrmB and the proteome-wide absence of any second subunit.


## Artifacts

- [OpenScientist final report](PSEPK__trna_m7g46_methylation__upa00989-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__trna_m7g46_methylation__upa00989-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:31428787
2. PMID:19934251
3. PMID:18029735
4. PMID:36599982
5. PMID:34006170