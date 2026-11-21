# MAVS (Q7Z434) — curation notes

Human mitochondrial antiviral-signaling protein. Review created 2026-10-28 in response to the
`litscan:module-member` handoff ai4curation/ai-gene-review#3923, which asked whether the newly
reported MAVS role in maintaining mitochondrial import competence belongs in
`modules/rig_i_signaling.yaml`. The determination for the module is at the end of these notes; the
bulk of the work was the gene review itself, which did not exist (PR #5620 names
`genes/human/MAVS/` as a missing prerequisite for any MAVS-regulation arm of that module).

## Deep research

`just deep-research human MAVS --provider perplexity` failed in this environment:

```
ERROR - No research providers available. Please set API keys:
```

No `MAVS-deep-research-*.md` was written, and none was fabricated. These notes stand in for it and
cite only the cached `publications/PMID_*.md` records, the UniProt flat file, `gocams/index.tsv` and
the GOA table. 81 of 81 GOA-cited PMIDs were already cached (47 with full text); `PMID:42808786`
was fetched for this review and is abstract-only (no PMC record yet).

## What MAVS is

A tail-anchored outer-membrane protein with an N-terminal CARD, a proline-rich region, TRAF-interaction
motifs and a single C-terminal transmembrane segment. Both ends of the architecture were functionally
assigned in the discovery paper: *"MAVS contains an N-terminal CARD-like domain and a C-terminal
transmembrane domain, both of which are essential for MAVS signaling"* and *"The transmembrane domain
targets MAVS to the mitochondria, implicating a new role of mitochondria in innate immunity"*
[PMID:16125763]. It was reported independently in 2005 under three names that are all in this gene's
reference list — MAVS [PMID:16125763], IPS-1 [PMID:16127453], Cardif [PMID:16177806] — and under a
fourth, VISA, in a paper UniProt cites (PubMed:16153868) that is not among the GOA references and so
is not cached here. UniProt also keeps `031N` from a 2003 genome-scale NF-kappaB-activator screen
[PMID:12761501], which is the origin of the HMP row on `GO:0043123`.

## Mechanism, in the order the pathway runs

1. **Sensor engagement.** *"IPS-1 contained an N-terminal CARD-like structure that mediated
   interaction with the CARD of RIG-I and Mda5"* [PMID:16127453]. This is the informative content of
   the nineteen bare protein-binding rows whose partner is RIG-I (O95786) or MDA5 (Q9BYX4).
2. **Polymerisation.** *"Mitochondrial antiviral signaling (MAVS) protein forms prion-like aggregates
   mediated by the N-terminal caspase activation and recruitment domain (CARD)"*; the eLife correction
   reports *"a 4.2 Å resolution reconstruction of MAVS CARD filaments purified from mammalian cells
   under native conditions"* with C1 helical symmetry, superseding the earlier C3 model
   [PMID:26314863]. GOA cites the correction rather than the 2014 original, which is the right choice
   and is recorded as such in `reference_review`. The transition is reconstitutable in vitro
   [PMID:26803627].
3. **Kinase and E3 recruitment.** Cardif *"recruits IKKalpha, IKKbeta and IKKvarepsilon kinases by
   means of its C-terminal region"* [PMID:16177806]; *"TBK1 and IKKi protein kinases were required for
   the IPS-1-mediated interferon induction"* [PMID:16127453]. TRAF3 binds a TRAF-interaction motif:
   *"a novel TRAF3-binding site in the aa450-468 region of MAVS"*, with the consensus TIM
   455-PEENEY-460 [PMID:21200404], and *"Cardif-mediated IFNalpha induction occurs through a direct
   interaction between the TRAF domain of TRAF3 and a TRAF-interaction motif (TIM) within Cardif"*
   [PMID:16858409]. TOMM70 contributes an Hsp90-dependent arm: *"the clamp domain (R192) of Tom70
   interacts with the C-terminal motif (EEVD) of Hsp90, thus recruiting TBK1/IRF3 to mitochondria"*
   [PMID:20628368].
4. **IRF3 hand-off.** *"MAVS and STING harbor two conserved serine and threonine clusters that are
   phosphorylated by the kinases IKK and/or TBK1"*, and *"Phosphorylated MAVS and STING then bind to a
   positively charged surface of interferon regulatory factor 3 (IRF3) and thereby recruit IRF3 for
   its phosphorylation and activation by TBK1"* [PMID:25636800], through *"a conserved pLxIS motif"*
   shared with STING1 and TRIF [PMID:27302953]. This is why `GO:0140297 DNA-binding transcription
   factor binding` is informative here rather than incidental.
5. **Outputs.** *"Silencing of MAVS expression through RNA interference abolishes the activation of
   NF-kappaB and IRF 3 by viruses, thereby permitting viral replication"* [PMID:16125763]; *"Epistasis
   experiments show that MAVS is required for the phosphorylation of IRF 3 and IkappaB and functions
   downstream of RIG-I"* [PMID:16125763].

## Two organellar pools, not one

*"the RIG-I-like receptor (RLR) adaptor protein MAVS is located on peroxisomes and mitochondria"* and
*"peroxisomal and mitochondrial MAVS act sequentially to create an antiviral cellular state"*; the
division of labour is explicit — *"peroxisomal MAVS induces the rapid interferon-independent
expression of defense factors that provide short-term protection, whereas mitochondrial MAVS activates
an interferon-dependent signaling pathway with delayed kinetics, which amplifies and stabilizes the
antiviral response"* [PMID:20451243]. The same paper is the sole basis for the
`GO:1900063 regulation of peroxisome organization` row, and it does support it: *"reovirus infection
induced peroxisomal aggregation and the formation of peroxisomal tubules"*, and *"The tubes formed
ranged from approximately 2 microns in length to over 5 microns, and depended on MAVS localization to
peroxisomes"* — exaggerated in MAVS-Pex cells and absent in MAVS-Mito and MAVS-Cyto cells. That is a
signalling-dependent morphological readout rather than a biogenesis function, hence
`KEEP_AS_NON_CORE` rather than `REMOVE`.

## Second adaptor role: NLRP3

*"the mitochondria-associated adaptor molecule, MAVS, is required for optimal NLRP3 inflammasome
activity"* and *"MAVS mediates recruitment of NLRP3 to mitochondria, promoting production of IL-1β and
the pathophysiologic activity of the NLRP3 inflammasome in vivo"* [PMID:23582325]. A second study
places MAVS upstream of TRAF3-dependent ASC ubiquitination: *"Deficiency in MAVS or TNFR-associated
factor 3 impaired ASC ubiquitination and cytosolic aggregates formation, resulting in reduced
inflammasome response upon RNA virus infection"* [PMID:25847972]. This is kept as a third core
function: it is the same molecular activity (signalling adaptor) in a different process, with its own
in vivo phenotype.

## Decisions taken across the 230 GOA rows

The row count is dominated by repetition: 94 bare `GO:0005515`, 40 `GO:0005741` (35 of them Reactome
TAS), 16 `GO:0005739`. About 48 distinct terms.

- **Bare protein binding (94 rows).** Policy actions only (`src/ai_gene_review/validation/protein_binding_policy.py`).
  `MODIFY` where the row's partner is a pathway component for which the gene already carries a
  specific term: RIG-I/MDA5 → `GO:0050700` (19 rows), TBK1/IKKepsilon → `GO:0120283` (10), IRF3 →
  `GO:0140297` (1).
  `REMOVE` (64 rows) otherwise, with the standard caveat that removal does not mean the interaction is
  false. MAVS is a genuine hub — UniProt lists interactions with regulators, E3 ligases, DUBs and a
  dozen viral antagonists — and those relationships belong in GO-CAM models or the partners' own
  reviews.
- **Root organelle terms.** `GO:0005739` and `GO:0005777` are kept as informative in their own right
  per `projects/ORGANELLES.md`, never `TOO_GENERAL` and never modified down. Both sub-compartments are
  already annotated (`GO:0005741`, `GO:0005778`), so nothing needed adding. The HTP proteomics row
  [PMID:34800366] and the automated-imaging IDA row are exactly the assays that cannot resolve a
  sub-compartment, so they correctly stop at the organelle. `GO:0031966 mitochondrial membrane` is
  **not** a root organelle term, so the ordinary refinement rule applies and it is `MODIFY` →
  `GO:0005741`.
- **Interferon direction errors (3 rows).** `GO:0060337` and `GO:0060340` are about the pathway
  *initiated by* type I interferon binding IFNAR; MAVS acts upstream of interferon synthesis and has
  never been placed in the JAK-STAT cascade. `GO:0035458 cellular response to interferon-beta` from
  [PMID:31390091] is the same error: that paper's assays measure IFN-beta promoter and ISRE output
  downstream of MAVS. All three are `MODIFY` (lateral correction) to the interferon-production terms
  the gene already carries. Whether this is a systematic habit across RLR genes is raised in
  `suggested_questions`.
- **`GO:0051262 protein tetramerization`** → `MODIFY` to `GO:0051258 protein polymerization`. The word
  *tetramer* appears **nowhere** in the full text of [PMID:31390091]; what the authors did was
  *"enforced the multimerization of MAVS‐Region III by artificially tagging it with GCN4‐derived
  peptides"*. The term reflects the engineering device, not MAVS.
- **`GO:0045944` and `GO:0042307`** → `MARK_AS_OVER_ANNOTATED`. MAVS activates IRF3 and NF-kappaB; the
  transcription and the nuclear import are done by those factors and the import machinery. Reasoning
  is on biological grounds only — [PMID:18818105] is a MITA/STING paper whose full text I have not
  read, so no mis-attribution is alleged.
- **`GO:0000151 ubiquitin ligase complex`** → `MARK_AS_OVER_ANNOTATED`. NAS, and what the cited paper
  shows is that MAVS *recruits* and is *modified by* E3 ligases, which is adaptor behaviour.
- **`GO:0140693 molecular condensate scaffold activity`** → **`ACCEPT`**, deliberately, against my
  first instinct. A cryo-EM-resolved helical filament is not obviously a phase-separated condensate,
  and the term's synonyms are *"phase separation nucleation activity"*. But `gocams/index.tsv` shows GO
  curators chose this term for MAVS in two models (`635b1e3e00002360`, `648d0dc100001547`) and for
  NLRP3 beside it, so the condensate framing of prion-like signalling assemblies is a decision to argue
  with explicitly, not a stray IDA. Logged as a terminology question for the ontology editors and as a
  `BIOLOGY`+`ONTOLOGY` knowledge gap instead of downgrading the row.
- **Cytokine output terms** (IL-6, IL-8, TNF, CCL5, CXCL10, myeloid-DC cytokine production) →
  `KEEP_AS_NON_CORE`: real, measured, but transcriptional outputs of the signalosome.
  `GO:0060760 positive regulation of response to cytokine stimulus` is `MODIFY`, since
  [PMID:21957149] measures cytokine *production*, not responsiveness.
- **Broad-but-correct immune terms** (`GO:0045087`, `GO:0051607`) → `ACCEPT`, following the STING1
  precedent: each row's own evidence does not select a narrower branch, and the specific terms the
  gene carries supply the detail. Near-root generic terms whose refinement *is* supported by the row's
  own reference (`GO:0007165`, `GO:0035556`, `GO:0060090`, `GO:0030674`, `GO:0019901`) are `MODIFY`.
- **Electronic rows.** 10 `GO_REF:0000117` ARBA rows and the `GO_REF:0000044`/`GO_REF:0000120`
  UniProt-keyword rows are kept consistent with the experimental rows that share their term, with a
  reason recording that they are rule-based predictions rather than independent support. `REMOVE` on
  any of them would assert the claim is doubtful, which it is not.

Final tally: 109 `ACCEPT`, 64 `REMOVE` (all bare protein binding), 42 `MODIFY`, 11
`KEEP_AS_NON_CORE`, 4 `MARK_AS_OVER_ANNOTATED`.

## GO-CAM cross-check

18 activities for Q7Z434 in `gocams/index.tsv`, across 17 models. The dominant typing, on thirteen of them, is
`GO:0035591 signaling adaptor activity` in `GO:0002753` at `GO:0005741`/`GO:0031966` — the same shape
as core function 1 here, which is good corroboration. Two models use `GO:0140693` (above); two use
`GO:0060090`/`GO:0030674`, which this review proposes refining to `GO:0035591`; several use
`GO:0031966` where `GO:0005741` is supported. Models for viral antagonism (SARS-CoV-2 ORF9b and M,
HHV1 US3 and UL37, HMPV M2-2, EBV BILF1) all place MAVS correctly as the target.

## No new annotations proposed

`NEW` was not used. The one candidate was the 2026 mitochondrial-import result (below) and it does not
meet the bar: a single paper, abstract-only in the cache, and the question of **which entity performs
the step** is exactly what cannot be settled from the abstract. Maintaining the expression and assembly
of another complex is at best a regulatory relationship, and the observed import defect may be
downstream of the fragmentation and mitophagy reported in the same sentence. Recorded as a knowledge
gap with a matched `suggested_experiments` entry instead.

## Determination for issue #3923 (RIG-I signaling module)

**No — the MAVS mitochondrial-import result is not added to `modules/rig_i_signaling.yaml`, and the
module file is not touched by this change.** Three reasons:

1. **Outside the module boundary.** That module is a compact three-step backbone (viral RNA sensing →
   MAVS signalosome assembly → TBK1-IRF activation) describing signal transduction to type I
   interferon. The 2026 finding is explicitly *not* that: *"we demonstrate that MAVS can restrict viral
   replication entirely independently of traditional interferon signaling"* [PMID:42808786]. A
   mitochondrial-maintenance function running parallel to the cascade is a different mechanism, and
   modules model mechanisms.
2. **No new part to add.** MAVS is already the module's `mavs_signalosome_assembly` annoton. The
   candidate names no new participant; the TOM subunits it implicates are not RLR signalling
   components. Adding a TOM-maintenance step would mean a second, unrelated mechanism inside one
   module.
3. **Determinacy.** Single paper, online ahead of print, abstract-only in the cache, and the causal
   order between loss of TOM assembly and the fragmentation/depolarisation/mitophagy phenotype is not
   established from the abstract. That is a knowledge gap, which is where it has been recorded.

Note for whoever picks up #3922/PR #5620: that PR edits `module.notes` of the same module file. This
change deliberately avoids `modules/rig_i_signaling.yaml` so the two do not conflict. If a
module-level note for #3923 is wanted, it should be added after #5620 merges, alongside the
assessed-but-unmodelled paragraph already drafted there.
