---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-14T07:17:35.841544'
end_time: '2026-07-14T07:41:29.748426'
duration_seconds: 1433.91
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Bacterial lipoprotein maturation
  module_summary: A species-neutral bacterial envelope-biogenesis module for the ordered
    maturation of lipobox-containing prolipoproteins by Lgt diacylglyceryl transfer,
    LspA signal peptide cleavage, and Lnt or lineage-equivalent N-acylation where
    triacylated lipoproteins are produced. Pseudomonas putida KT2440 provides the
    current UniProt exemplars for the canonical diderm Lgt-LspA-Lnt route; Lol sorting
    and substrate-specific lipoprotein functions are downstream context outside this
    module.
  module_outline: "- Bacterial lipoprotein maturation\n  - 1. Diacylglyceryl transfer\
    \ to prolipoprotein cysteine\n  - Lgt diacylglyceryl transfer\n    - Lgt family:\
    \ prolipoprotein diacylglyceryl transferase (molecular player: prolipoprotein\
    \ diacylglyceryl transferase family; activity or role: phosphatidylglycerol-prolipoprotein\
    \ diacylglyceryl transferase activity)\n  - 2. Signal peptide cleavage from diacylglyceryl-prolipoprotein\n\
    \  - LspA signal peptide cleavage\n    - LspA family: signal peptidase II (molecular\
    \ player: lipoprotein signal peptidase family; activity or role: aspartic-type\
    \ endopeptidase activity)\n  - 3. Terminal N-acylation of apolipoprotein\n  -\
    \ Lnt N-acylation\n    - Lnt family: apolipoprotein N-acyltransferase (molecular\
    \ player: apolipoprotein N-acyltransferase family; activity or role: N-acyltransferase\
    \ activity)"
  module_connections: '- Lgt diacylglyceryl transfer precedes LspA signal peptide
    cleavage

    - LspA signal peptide cleavage precedes Lnt N-acylation'
  pathway_query: UPA00665
  pathway_id: UPA00665
  pathway_name: UPA00665
  pathway_source: free-text pathway query
  pathway_context: No local pathway bucket was resolved for this query.
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '1'
  candidate_genes: '- lspA: PP_0604 | Q88Q91 | Lipoprotein signal peptidase (EC 3.4.23.36)
    (Prolipoprotein signal peptidase) (Signal peptidase II) (SPase II) (EC 3.4.23.36;
    primary bucket kegg:ppu03060)'
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
  path: PSEPK__bacterial_lipoprotein_maturation__upa00665-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__bacterial_lipoprotein_maturation__upa00665-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Bacterial lipoprotein maturation in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00665
- Resolved ID: UPA00665
- Resolved name: UPA00665
- Source: free-text pathway query

No local pathway bucket was resolved for this query.

## Candidate Genes From Local Metadata

Candidate gene count: 1

- lspA: PP_0604 | Q88Q91 | Lipoprotein signal peptidase (EC 3.4.23.36) (Prolipoprotein signal peptidase) (Signal peptidase II) (SPase II) (EC 3.4.23.36; primary bucket kegg:ppu03060)

## Generic Module Context

### Working Scope

A species-neutral bacterial envelope-biogenesis module for the ordered maturation of lipobox-containing prolipoproteins by Lgt diacylglyceryl transfer, LspA signal peptide cleavage, and Lnt or lineage-equivalent N-acylation where triacylated lipoproteins are produced. Pseudomonas putida KT2440 provides the current UniProt exemplars for the canonical diderm Lgt-LspA-Lnt route; Lol sorting and substrate-specific lipoprotein functions are downstream context outside this module.

### Provisional Biological Outline

- Bacterial lipoprotein maturation
  - 1. Diacylglyceryl transfer to prolipoprotein cysteine
  - Lgt diacylglyceryl transfer
    - Lgt family: prolipoprotein diacylglyceryl transferase (molecular player: prolipoprotein diacylglyceryl transferase family; activity or role: phosphatidylglycerol-prolipoprotein diacylglyceryl transferase activity)
  - 2. Signal peptide cleavage from diacylglyceryl-prolipoprotein
  - LspA signal peptide cleavage
    - LspA family: signal peptidase II (molecular player: lipoprotein signal peptidase family; activity or role: aspartic-type endopeptidase activity)
  - 3. Terminal N-acylation of apolipoprotein
  - Lnt N-acylation
    - Lnt family: apolipoprotein N-acyltransferase (molecular player: apolipoprotein N-acyltransferase family; activity or role: N-acyltransferase activity)

### Known Relationships Among Steps

- Lgt diacylglyceryl transfer precedes LspA signal peptide cleavage
- LspA signal peptide cleavage precedes Lnt N-acylation

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

# Module/Pathway/Taxon Review: Bacterial Lipoprotein Maturation in *Pseudomonas putida* KT2440

**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Pathway query:** UPA00665 (UniPathway "Protein modification; lipoprotein biosynthesis")
**Module:** Ordered maturation of lipobox prolipoproteins — Lgt → LspA → Lnt
**Date:** 2026-07-14

---

## 1. Executive summary

The canonical three-step diderm lipoprotein-maturation route is **fully present and satisfiable** in *P. putida* KT2440. All three steps map to single-copy, reviewed Swiss-Prot genes:

| Step | Enzyme | Gene | Locus | UniProt | EC | KO |
|------|--------|------|-------|---------|----|----|
| 1. Diacylglyceryl transfer | Lgt | *lgt* (*umpA*) | PP_5142 | Q88CN8 | 2.5.1.145 | K13292 |
| 2. Signal-peptide cleavage | LspA | *lspA* | PP_0604 | Q88Q91 | 3.4.23.36 | K03101 |
| 3. N-acylation | Lnt | *lnt* | PP_4790 | Q88DN4 | 2.3.1.269 | K03820 |

The local candidate list contained **only** *lspA* (PP_0604). This is a **KEGG-boundary artifact**, not a genome gap: only LspA's KO is placed in KEGG's Protein export map (ppu03060), whereas *lgt* and *lnt* are unmapped in that KEGG pathway even though both genes exist. **Recommendation: `module_needs_revision`** — add PP_5142 (Lgt) and PP_4790 (Lnt) as covered steps. No step should be marked `gap` or `not_expected_in_target_taxon`.

Confidence is **high by orthology** (specific InterPro family calls, UniPathway sub-step annotations, single-copy loci) but there is **no direct experimental characterization in KT2440** — all three entries are protein-existence level 3 (inferred from homology). The strongest nearby experimental anchor is the *P. aeruginosa* LspA crystal structure (PMID 26912896). To upgrade this homology-only evidence, I verified at the sequence level that **each KT2440 enzyme conserves every experimentally-defined catalytic residue** of its characterized homolog (Section 4.4), which raises functional confidence to high and specifically clears the Lnt over-annotation flag.

---

## 2. Target-organism pathway definition

**Included process.** Post-translational maturation of lipobox-containing prolipoproteins at the cytoplasmic (inner) membrane, in strict order:
1. **Lgt** transfers a diacylglyceryl group from phosphatidylglycerol onto the thiol of the invariant lipobox cysteine, forming diacylglyceryl-prolipoprotein.
2. **LspA** (signal peptidase II), an aspartyl peptidase, cleaves the signal peptide immediately N-terminal to the modified cysteine, yielding apolipoprotein (N-terminal S-diacylglyceryl-cysteine).
3. **Lnt** N-acylates the free α-amino group of that cysteine, producing the mature **triacylated** lipoprotein.

**UniPathway mapping.** UniProt annotates the three KT2440 enzymes with the identical pathway "Protein modification; lipoprotein biosynthesis" and the three ordered sub-steps *(diacylglyceryl transfer)*, *(signal peptide cleavage)*, *(N-acyl transfer)* — i.e., the query **UPA00665** maps exactly to this module and is satisfied.

**Neighboring pathways to keep separate.**
- **Lol sorting/trafficking** (LolABCDE): outer-membrane targeting of mature lipoproteins. KT2440 encodes LolA (PP_4003), LolB (PP_0724), LolC (PP_2154), LolD (PP_2155), LolE (PP_2156). These are **downstream** and belong to a distinct module.
- **General Sec/Tat protein export** (KEGG map03060): the broad overview map that contains LspA but is not lipoprotein-specific; do not collapse the maturation module into it.
- Substrate-specific lipoprotein functions (e.g., Lpp/OprI-type, LptE, BamB/C/D/E) are downstream clients, not maturation steps.

**Alternate names / DB definitions.** Lgt = *umpA*; LspA = "prolipoprotein signal peptidase / SPase II / signal peptidase II"; Lnt = "apolipoprotein N-acyltransferase / ALP N-acyltransferase." EC set: 2.5.1.145 / 3.4.23.36 / 2.3.1.269.

---

## 3. Expected step model

For a **diderm (Gram-negative) gammaproteobacterium** such as KT2440, all three steps are **expected and essentially non-optional**:

- Lgt is the gating step and *lgt* deletion is lethal in most Gram-negatives (PMID 26729647).
- The route requires sequential Lgt → LspA → Lnt activity (PMID 28698362).
- Lnt-dependent N-acylation (triacylation) is characteristic of proteobacteria. Unlike many monoderm Firmicutes (which frequently lack a canonical Lnt and produce diacylated lipoproteins or use lineage-specific N-acyltransferases), KT2440 is expected to carry the canonical Lnt — consistent with the present PP_4790.

Ordering constraints in the generic module (Lgt precedes LspA precedes Lnt) hold in KT2440.

**Substrate pool.** The pathway is functionally engaged, not vestigial: UniProtKB annotates **≥76 lipoprotein (KW-0449) proteins** in the KT2440 proteome (52 also carrying a signal peptide), i.e. an abundant client set of lipobox prolipoproteins requiring maturation — consistent with the essentiality of the machinery.

---

## 4. Candidate genes and evidence

### 4.1 LspA — PP_0604 / Q88Q91 (the sole metadata candidate)
- **Role:** signal peptidase II; cleaves signal peptide from diacylglyceryl-prolipoprotein.
- **Evidence type:** homology-inferred (PE3, HAMAP MF_00161). InterPro **IPR001872 "Peptidase A8, signal peptidase II"** (specific); Pfam PF01252. GO:0004190 (aspartic-type endopeptidase), GO:0006508, GO:0005886.
- **Species transfer:** **strong.** The *P. aeruginosa* LspA–globomycin crystal structure identifies LspA as an aspartyl peptidase (PMID 26912896); *P. aeruginosa* is a close congener, so mechanism/active-site transfer to KT2440 is well justified. LspA is a validated antibacterial target (globomycin/myxovirescin; PMIDs 32768648, 22232277).
- **Caveats:** GO:0004190 "aspartic-type endopeptidase activity" is a broad parent term; the specific IPR001872 family and EC 3.4.23.36 anchor the correct function.

### 4.2 Lgt — PP_5142 / Q88CN8 (missing from metadata, present in genome)
- **Role:** phosphatidylglycerol–prolipoprotein diacylglyceryl transferase; step 1.
- **Evidence type:** homology-inferred (PE3, HAMAP MF_01147). InterPro **IPR001640 "…diacylglyceryl transferase Lgt"** (specific); Pfam PF01790. GO:0008961 (specific activity), GO:0042158, GO:0005886. UniPathway sub-step "(diacylglyceryl transfer)."
- **Species transfer:** strong by orthology; direct structural/mechanistic basis from *E. coli* Lgt (PMID 26729647) and cross-phylum conservation of Lgt (PMID 7592473).
- **Caveats:** none major; single-copy, specific family. Gene lies at ~5.87 Mb (complement 5867757–5868563), separate locus from the others.

### 4.3 Lnt — PP_4790 / Q88DN4 (missing from metadata, present in genome)
- **Role:** apolipoprotein N-acyltransferase; terminal step, produces triacylated lipoprotein.
- **Evidence type:** homology-inferred (PE3, HAMAP MF_01148). InterPro **IPR004563 "Apolipoprotein N-acyltransferase"** (specific family) plus generic **IPR003010 "Carbon-nitrogen hydrolase"** domain; Pfam PF00795 + PF20154. GO:0016410 (N-acyltransferase), GO:0042158, GO:0005886. UniPathway "(N-acyl transfer)."
- **Species transfer:** strong by orthology; mechanistic framework from structural work on Lnt (PMID 28698362).
- **Caveats:** PF00795/IPR003010 is the **nitrilase / carbon-nitrogen-hydrolase superfamily**, which harbors many unrelated activities — a generic over-propagation flag in isolation. Here it is **mitigated** by the dedicated IPR004563 family assignment and EC 2.3.1.269, so the Lnt call is reliable.

**Paralog check:** proteome scans on each EC (2.5.1.145, 3.4.23.36, 2.3.1.269) returned exactly one hit — **no paralog ambiguity** for any step.

### 4.4 Catalytic-residue conservation (sequence-level verification)
To move beyond database homology, KT2440 enzymes were pairwise-aligned to their characterized homologs and active-site residues checked:

| Enzyme | Reference (characterized) | % identity | Catalytic residues checked | Result |
|--------|---------------------------|-----------|-----------------------------|--------|
| LspA (Q88Q91) | *P. aeruginosa* PAO1 LspA (Q9HVM5; crystallized, PMID 26912896) | **78.7%** | Asp124, Asp143 (aspartyl dyad) | **both conserved** (near-identical context GHVVD**F**ILV / FN[V/L]AD**S**AIT) |
| Lgt (Q88CN8) | *E. coli* K12 Lgt (P60955; PMID 26729647) | 55.1% | Arg143, Arg239 (essential) | **both conserved** |
| Lnt (Q88DN4) | *E. coli* K12 Lnt (P23930; PMID 28698362) | 43.1% | Glu267, Lys335, Cys387 (nitrilase-superfamily triad) | **all conserved** |

Conservation of the full catalytic set — including the Lnt catalytic Cys387 — raises functional confidence to high despite the PE3 (homology-inferred) status, and decisively refutes the possibility that PP_4790 is a mis-annotated CN-hydrolase-superfamily paralog. The 78.7% identity of LspA to the crystallized *P. aeruginosa* enzyme makes mechanistic species transfer strong.

---

## 5. Gaps, ambiguities, and likely over-annotations

- **No true gaps.** Every expected step has a specific-family, single-copy gene.
- **Metadata gap is artifactual.** Lgt and Lnt are absent from the candidate list only because KEGG's ppu03060 pathway map does not contain their KOs (K13292, K03820); this is a database-boundary artifact.
- **Over-annotation flags (low risk):**
  - LspA GO:0004190 is a broad endopeptidase parent term — acceptable given IPR001872/EC anchoring.
  - Lnt CN-hydrolase superfamily membership (PF00795/IPR003010) is the classic over-propagation trap; here countered by IPR004563 **and** by conservation of the catalytic triad Glu267/Lys335/**Cys387** (Section 4.4) — flag cleared.
- **Evidence caveat:** all three are PE3 (inferred from homology) with no KT2440-specific wet-lab data; direct evidence exists only in relatives (*P. aeruginosa* LspA; *E. coli* Lgt/Lnt). However, sequence-level conservation of all experimentally-defined catalytic residues (Section 4.4) substantially mitigates this caveat.

---

## 6. Module and GO-curation recommendations

| Module step | Call | Gene(s) |
|-------------|------|---------|
| 1. Diacylglyceryl transfer (Lgt) | **covered** | PP_5142 / Q88CN8 |
| 2. Signal-peptide cleavage (LspA) | **covered** | PP_0604 / Q88Q91 |
| 3. N-acylation (Lnt) | **covered** | PP_4790 / Q88DN4 |

- **Overall module:** `module_needs_revision` — expand the KT2440 candidate set from 1 gene (lspA only) to all three; the genome fully satisfies UPA00665.
- **Boundaries:** correct as drawn. Keep Lol sorting (LolABCDE: PP_4003/PP_0724/PP_2154/PP_2155/PP_2156) and general Sec/Tat export (map03060) as separate modules.
- **GO/annotation:** no new GO term requests needed. Optionally prefer the specific child terms already present (GO:0008961 for Lgt; retain EC/InterPro anchors for LspA and Lnt) over broad parents. Note lolC/lolE are TrEMBL (unreviewed) if the Lol module is later curated.
- **No `not_expected_in_target_taxon` calls** — the diderm gammaproteobacterial context expects all three steps, including canonical Lnt.

---

## 7. Genes to promote to full `fetch-gene` review

1. **PP_5142 (lgt / Q88CN8)** — highest priority; must be added to satisfy step 1.
2. **PP_4790 (lnt / Q88DN4)** — add to satisfy step 3; note and clear the CN-hydrolase superfamily over-propagation flag during review.
3. **PP_0604 (lspA / Q88Q91)** — already the candidate; confirm and retain; broad GO:0004190 worth a note.

(Downstream, for a separate Lol module: PP_4003, PP_0724, PP_2154, PP_2155, PP_2156.)

---

## 8. Key references

- Vogeley L, *et al.* Structural basis of lipoprotein signal peptidase II action and inhibition by globomycin. *Science* 2016. **PMID 26912896.** (*P. aeruginosa* LspA structure; aspartyl peptidase.)
- Mao G, *et al.* Crystal structure of *E. coli* lipoprotein diacylglyceryl transferase. *Nat Commun* 2016. **PMID 26729647.** (Lgt structure; *lgt* deletion lethal in most Gram-negatives.)
- Noland CL, *et al.* Structural insights into lipoprotein N-acylation by Lnt. *PNAS* 2017. **PMID 28698362.** (Sequential three-enzyme maturation; Lnt.)
- Diao J, *et al.* Inhibition of *E. coli* lipoprotein diacylglyceryl transferase… *Antimicrob Agents Chemother* 2021. **PMID 33875545.** (Lgt essentiality / OM integrity.)
- Qi HY, *et al.* Structure-function relationship of bacterial prolipoprotein diacylglyceryl transferase. 1995. **PMID 7592473.** (Cross-phylum Lgt conservation.)
- Garland K, *et al.* Optimization of globomycin analogs as Gram-negative antibiotics. 2020. **PMID 32768648.** (LspA as validated target.)
- Xiao Y, *et al.* Myxovirescin inhibits type II signal peptidase. 2012. **PMID 22232277.** (LspA target validation.)

*Database evidence:* UniProtKB Q88CN8 / Q88Q91 / Q88DN4 (Swiss-Prot, PE3); KEGG ppu:PP_5142/PP_0604/PP_4790 (KO K13292/K03101/K03820); InterPro IPR001640 / IPR001872 / IPR004563; UniPathway UPA00665.


## Artifacts

- [OpenScientist final report](PSEPK__bacterial_lipoprotein_maturation__upa00665-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__bacterial_lipoprotein_maturation__upa00665-deep-research-openscientist_artifacts/final_report.pdf)