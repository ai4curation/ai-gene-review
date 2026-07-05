# mks-2 (C. elegans) research notes

UniProt: C8JQP7 (C8JQP7_CAEEL) · WormBase: WBGene00194710 / C30B5.9 · Human ortholog: **TMEM216 (MKS2)**
Taxon: NCBITaxon:6239 (Caenorhabditis elegans)

## Summary of gene product

- Small (142 aa) integral membrane protein of the ciliary **transition zone (TZ)**.
  UniProt/Phobius predicts 4 transmembrane helices (12–35, 47–65, 77–99, 111–133);
  the mammalian TMEM216 literature usually describes 3–4 TM segments. Pfam
  `PF09799` (Transmemb_17); InterPro `IPR019184` (Uncharacterised_TM-17);
  PANTHER `PTHR13531`. No catalytic domain; "Predicted" evidence level (PE 4).
- Ortholog of human **TMEM216/MKS2**, a Meckel-Gruber syndrome / Joubert syndrome
  (JBTS2) gene. In *C. elegans* it is a **core component of the MKS module** of the
  ciliary transition zone, which acts with the NPHP module to build the ciliary
  gate (membrane diffusion barrier) and the Y-link connectors between the axoneme
  doublet microtubules and the ciliary membrane.

## KNOWN (well supported)

### Localization: ciliary transition zone
- MKS-2::GFP is concentrated at the TZ of amphid (head) and phasmid (tail) sensory
  cilia, immediately distal to the basal body/transition fibres, marked relative to
  XBX-1::tdTomato. [PMID:26982032 Fig 2/3/4 text: MKS-2::GFP is used as a TZ
  comarker throughout Li et al 2016]
  - [PMID:26982032 "MKSR-1::tdTomato and MKS-2::GFP are TZ protein comarkers (in wild-type) that mislocalise in the cep-290 mutant"]
- Lambacher et al 2016 (TMEM107 paper, abstract-only in cache): the MKS module
  membrane proteins (which include MKS-2/TMEM216) are immobile and show periodic
  localization within the TZ; TMEM-107 organizes recruitment of MKS-1, TMEM-231,
  JBTS-14. [PMID:26595381 "MKS module membrane proteins are immobile and super-resolution microscopy in worms and mammalian cells reveals periodic localizations within the TZ"]
- IDA annotation GO:0035869 (ciliary transition zone) is WormBase-assigned from
  PMID:26595381 (curator read full text; abstract-only in our cache).

### Core MKS-module identity and gate function
- MKS-2 is explicitly one of the **"core" MKS module proteins** (with MKSR-1, MKSR-2,
  TMEM-231) that are all required for TZ **gate function** — restricting the
  inappropriate entry of the membrane-associated protein TRAM-1a into cilia.
  [PMID:26982032 "these“core” TZ proteins are all necessary for TZ gate function—namely, restricting the inappropriate entry of membrane-associated TRAM-1a into cilia"]
- In the *cep-290* mutant, MKS-2 mislocalizes / "leaks" into the axoneme, i.e. its
  correct TZ confinement depends on the upstream assembly factors MKS-5 (RPGRIP1L)
  and CEP-290. [PMID:26982032 "MKS-2 “leaks'”into the axoneme"]

### Role in recruiting/assembling other TZ proteins (protein localization to TZ)
- MKS-2 is required for TZ localization of the peripheral MKS-module protein
  TMEM-218: in the *mks-2* mutant TMEM-218 is absent from the TZ.
  [PMID:26982032 "TMEM-218 is no longer present at the TZ in the mks-2 MKS module mutant"]
  - Reciprocally, MKS-2 does NOT require TMEM-218 for its own localization:
    [PMID:26982032 "TMEM-218 is not required for the localisation of MKS-5, MKS-2 (“core” MKS module protein), or NPHP-4"]
  - Supports GO:1904491 (protein localization to ciliary transition zone), IMP.

### Genetic redundancy / cilium assembly (module logic)
- Single *mks-2* null mutants have **no overt dye-filling (Dyf) defect** — cilia
  still assemble. The MKS module is highly redundant.
  [PMID:26863025 "Similar to mks-1(tm2705) and mks-2(nx111) single mutants, there was no overt defect in dye uptake"]
- A novel EMS allele *mks-2(yhw128)* (start-codon G→A) was recovered as an
  enhancer of *nphp-4(tm925)*: *nphp-4;mks-2* double mutants are strongly Dyf and
  mislocalize MKS-3::GFP; non-complementation with *mks-2(mx1198)/(nx111)* confirms
  identity. [PMID:26863025 "failed to complement the Dyf phenotypes of nphp-4(tm925);mks-1(tm2705), nphp-4;mks-2(mx1198), and nphp-4;mks-5(tm3100)"]
  - Supports GO:1905515 (non-motile cilium assembly) by IMP (mks-2 allele) and by
    IGI (genetic interaction with nphp-4 = UniProtKB:G5ECP0).
  - Confirmed G5ECP0 = nphp-4 (genes/worm/nphp-4/nphp-4-ai-review.yaml `id: G5ECP0`).
- The redundancy logic is canonical: MKS-module single mutants are subtle; MKS+NPHP
  double mutants disrupt the barrier / Y-links. mks-2 behaves as an MKS-module gene
  (no synthetic Dyf with other MKS-module mutants such as tmem-218/mks-3;
  synthetic Dyf with NPHP-module nphp-4).
  [PMID:26982032 "combining the tmem-218 mutation with another MKS module mutant, mks-2 [28], does not cause a dye-filling phenotype"]

### Assembly hierarchy (upstream factors)
- MKS-5 (RPGRIP1L) is the master TZ assembly factor and CEP-290 acts between MKS-5
  and MKS-module proteins; both are required to localize MKS-2 to the TZ.
  [PMID:26982032 "MKS-5 as a critical assembly factor for all known MKS module proteins tested thus far"]

## NOT known / knowledge gaps

- **No precise molecular-function term / no assigned MF.** GOA carries only CC and
  BP terms for mks-2; there is no GO molecular-function term for a "structural
  constituent / diffusion-barrier scaffold subunit of the ciliary transition zone."
  The gene reads as MF-dark despite a well-understood CC/BP role. (Analogous to the
  DYF-2 "structural constituent of IFT particle" ontology gap.) → ONTOLOGY gap.
- **The specific molecular contribution of MKS-2/TMEM216 within the MKS module is
  undetermined.** Its direct binding partners in the worm TZ, and whether it
  contributes a discrete, non-redundant biochemical/structural sub-function (vs.
  being fully redundant with other core MKS proteins) are not resolved. Li et al
  note that *how* different core proteins mislocalize differs (MKS-2 "leaks" into
  the axoneme whereas TMEM-17 stays in the dendrite) but "the reason for this is
  unclear." [PMID:26982032 "the reason for this is unclear"] → BIOLOGY / RESIDUAL_SUBGAP.
- No worm phenotype uniquely attributable to *mks-2* beyond the shared MKS-module
  redundancy; a non-redundant role, if any, is unknown.

## Existing GOA annotations (7) — review plan

| # | Term | Evidence | Ref | Plan |
|---|------|----------|-----|------|
| 1 | GO:0035869 ciliary transition zone (is_active_in) | IBA | GO_REF:0000033 | ACCEPT (core CC) |
| 2 | GO:1905515 non-motile cilium assembly (involved_in) | IBA | GO_REF:0000033 | ACCEPT (module-level BP) |
| 3 | GO:0016020 membrane (located_in) | IEA | GO_REF:0000044 | KEEP_AS_NON_CORE (generic; subsumed by TZ membrane) |
| 4 | GO:1905515 non-motile cilium assembly (involved_in) | IMP | PMID:26863025 | ACCEPT (mks-2 allele; redundant single-mutant) |
| 5 | GO:1905515 non-motile cilium assembly (involved_in) | IGI | PMID:26863025 (with nphp-4) | ACCEPT (synthetic Dyf) |
| 6 | GO:1904491 protein localization to ciliary transition zone (involved_in) | IMP | PMID:26982032 | ACCEPT (recruits TMEM-218) |
| 7 | GO:0035869 ciliary transition zone (located_in) | IDA | PMID:26595381 | ACCEPT (direct localization) |

Plus one NEW: GO:1903565 negative regulation of protein localization to cilium
(gate function; restricting TRAM-1a entry), IMP, PMID:26982032.

## Deep-research provenance note

Falcon (Edison) deep research was launched (`just deep-research-falcon worm mks-2
--fallback perplexity-lite`) but did not return a file within ~24 min — the Edison
API was saturated by many concurrent gene jobs from parallel agents (429-class
slowdown; cf. falcon concurrency limits). No `*-deep-research-*.md` was produced.
Per project guidance, this review therefore rests on primary literature: the two
full-text papers PMID:26982032 (Li et al) and PMID:26863025 (Masyukova et al),
which both extensively assay mks-2, plus the abstract-only PMID:26595381
(Lambacher et al) whose WormBase IDA is deferred to the curator. Every
`supporting_text` is a verbatim substring of a cached publication; nothing was
fabricated. No annotation required UNDECIDED because all seven GOA annotations are
verifiable from the cached full-text papers.

## References used
- PMID:26982032 — Li et al 2016, PLoS Biol. MKS5/CEP290-dependent assembly of the
  TZ; full text cached; mks-2 heavily featured (core MKS module, gate, recruits
  TMEM-218). HIGH relevance, VERIFIED.
- PMID:26863025 — Masyukova et al 2016, PLoS Genet. Screen for nphp-4 modifiers;
  novel mks-2(yhw128) allele, synthetic Dyf with nphp-4. Full text cached. HIGH,
  VERIFIED. Source of the IMP + IGI cilium-assembly annotations.
- PMID:26595381 — Lambacher et al 2016, Nat Cell Biol. TMEM107 recruits ciliopathy
  proteins; MKS module membrane proteins immobile/periodic in TZ. Abstract-only in
  cache; WormBase IDA for mks-2 TZ localization drawn from full text. HIGH, VERIFIED
  (defer to curator for the IDA full-text evidence).
