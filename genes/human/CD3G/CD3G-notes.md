# CD3G (human, P09693) review notes

Context: ADAPTIVE_IMMUNITY project, T cell receptor trunk.

## Biology summary (with provenance)

- Invariant subunit of the TCR-CD3 complex; forms CD3 gamma-epsilon heterodimer.
  [PMID:9485181 "The TCR/CD3 complex is assembled after a series of pairwise interactions involving the formation of dimers of CD3 epsilon with either CD3 gamma or CD3 delta."]
  [PMID:31461748 "The octameric TCR-CD3 complex is assembled with 1:1:1:1 stoichiometry of TCRαβ:CD3γε:CD3δε:CD3ζζ."]
- EC Ig domain sites bind CD3E; TM acidic residue binds TCR beta.
  [PMID:8636209 "Site-directed mutagenesis of the acidic amino acid in the TM domain of CD3 gamma demonstrated that this residue is involved in TCR assembly probably by binding to Ti beta."]
- ITAM tyrosine-phosphorylated by LCK.
  [PMID:2470098 "members of the CD3 complex, including the gamma, delta, and epsilon chains, as well as a putative zeta subunit, can be phosphorylated at tyrosine residues by the CD4/CD8.p56lck complex."]
- PKC-phosphorylated S126 + di-leucine L131/L132 mediate clathrin-dependent TCR down-regulation.
  [PMID:8187769 "a membrane-proximal di-leucine motif (L131 and L132) in the cytoplasmic tail of CD3 gamma was required for PKC-mediated TCR down-regulation in addition to phosphorylation at S126."]
  [PMID:1535555 "A di-leucine- and a tyrosine-based motif are individually sufficient to induce both endocytosis and delivery to lysosomes of Tac."]
- Human CD3G-deficient T cells: reduced surface TCR, impaired ligand-induced endocytosis, no PMA-induced down-modulation.
  [PMID:12794121 "Kinetic confocal analysis indicated that early ligand-induced endocytosis was impaired."]
- gamma-delta TCRs contain CD3 gamma-epsilon but mostly lack CD3 delta.
  [PMID:30976362 "In fact, the CD3δ subunit is not even incorporated into the γδTCR complex and is not required for γδT cell development"]
- IMD17: CD3G deficiency milder than CD3D/CD3E deficiency.
  [PMID:17277165 "We propose a CD3delta >> CD3gamma hierarchy for the relative impact of their absence on the signaling for T cell production in humans."]

## Curation decisions

- 9 HuRI `protein binding` IPI rows: REMOVE (uninformative Y2H, mostly membrane-protein background partners).
- `protein transport` IMP (PMID:12794121): MODIFY -> GO:0031623 receptor internalization. CD3G supplies
  the sorting motif (structural participation), not merely cargo.
- Comparator check for internalization terms: CD3D (P04234), CD3E (P07766), CD79A (P11912), CD79B
  (P40259) carry none of GO:0031623 / GO:0036300 / GO:0006897 / GO:0038009 (QuickGO, 2026-09-30).
  So no NEW row was added; raised as a suggested question instead. The MODIFY refines an existing
  curated IMP assertion rather than manufacturing a new one.
- Knockout/deficiency phenotype process rows (cell polarity, regulation of lymphocyte apoptosis,
  positive thymic selection IBA): KEEP_AS_NON_CORE (necessity evidence, downstream of TCR signalling).
- `MHC class II receptor activity` contributes_to IDA (PMID:1323144, abstract-only): MARK_AS_OVER_ANNOTATED,
  consistent with CD247 review; class II specificity is a property of the clonotypic TCR.
- `identical protein binding` IDA (PMID:14967045): KEEP_AS_NON_CORE (in vitro oligomerization of disordered
  cytoplasmic fragment).
- `T cell receptor binding` NAS (PMID:11186279, case-report letter, no abstract): KEEP_AS_NON_CORE.
- Core MF: GO:0030159 signaling receptor complex adaptor activity, contributes_to GO:0004888.

## Deep research

Falcon deep research (`just deep-research-falcon human CD3G --fallback perplexity-lite`) was launched in
parallel with the review; see status below.

Status (2026-09-30): deep research FAILED (first attempt; superseded, see below). Falcon timed out/failed (600 s timeout). The
perplexity-lite fallback then failed with "Provider 'perplexity' not available. Available: falcon,
asta, openscientist", ending in "All providers failed". The review was written without a deep research
file, using the UniProt record, the cached GOA-cited publications, and five UniProt-cited papers
fetched with `just fetch-pmid` (PMID:2470098, 8187769, 1535555, 15136729, 17277165).

Update (2026-10-01): a falcon re-run succeeded and produced `CD3G-deep-research-falcon.md`; it was
integrated into the review afterwards (next section).

## Deep research integration (falcon)

Report: `CD3G-deep-research-falcon.md` (Edison/falcon, 2026-10-01). Short, cautious report; every DOI
resolved to the stated paper. Primary papers fetched for checking: PMID:15778375 (Szymczak & Vignali 2005,
abstract only), PMID:8647168 (Osman 1996, abstract only), PMID:29653965 (Rowe 2018, full text),
PMID:31921117 (Lee 2019, full text); PMID:38657677 (Xin 2024) and PMID:31461748 (Dong 2019) were already cached.

Claim classification (~18 substantive claims): confirms review 10, adds something new 5, conflicts 1
(by omission), not relevant/unsupported 2.

Confirms: CD3 gamma is a non-catalytic invariant TCR-CD3 subunit distinct from TCR gamma; CD3 gamma-epsilon
heterodimer; 1:1:1:1 octamer at 3.7 A (PMID:31461748); single ITAM, LCK phosphorylation and ZAP-70 recruitment;
di-leucine/AP-2 internalization (already core function 2); reduced surface TCR in CD3G deficiency; plasma
membrane single-pass topology; antigen recognition by clonotypic chains (supports MHC class II receptor
activity MARK_AS_OVER_ANNOTATED and contributes_to GO:0004888); not an enzyme/transporter; CD3G deficiency
milder than CD3D/CD3E.

Adopted (new):
- CD3G K128 required for AP-2 internalization [PMID:15778375 "an absolute requirement for the position of this
  signal in the context of the TCR complex and for a highly conserved lysine residue, K128, which is not
  present in CD3delta"] -> description, core function 2 description + supported_by.
- Phospho-CD3 gamma ITAM binds ZAP-70 (and Shc/Grb2/p85 in vitro) [PMID:8647168 "The data show that the
  doubly phosphorylated ITAM all bind the PTK ZAP-70"] -> description, core function 1 supported_by.
  Shc/Grb2/p85 binding not used for annotations (peptide pull-down only).
- Treg repertoire/suppression defect in CD3G patients [PMID:29653965 "Treg cells of patients with CD3G
  defects had reduced diversity, increased clonality, and reduced suppressive function."] -> description
  and a suggested question. No NEW process term (e.g. regulatory T cell differentiation/tolerance): this is
  necessity evidence downstream of reduced TCR signalling, CD3G performs no step of Treg selection itself.
- Phenotypic variability (CVID-like, preserved Treg function) [PMID:31921117] -> description ("CVID-like"),
  suggested question.
- Human gamma-delta TCR-CD3 contains CD3 epsilon-gamma [PMID:38657677 "In humans, the TCRγ and TCRδ chains
  associate with three CD3 dimeric subunits—CD3εγ, CD3εδ and CD3ζζ—forming an octameric γδ TCR–CD3 complex"]
  -> added as human structural support to the GO:0042106 part_of row (still ACCEPT).

Conflict (by omission) raised as a question: the review previously stated that in gamma-delta T cells CD3
gamma-epsilon is usually the only CD3 gamma/delta-family dimer (murine data, PMID:16418397, PMID:30976362).
The report says the 2024 human structures "identified a CD3εγ module" but does not mention that the same
structures also contain CD3 epsilon-delta. Primary evidence (PMID:38657677) shows both dimers in reconstituted
human complexes, so the description and the GO:0042106 summary were softened to state the mouse/human
difference; a suggested question about endogenous human gamma-delta CD3 composition was added. This is
consistent with the CD3D question about adding GO:0042106 to CD3D; CD3G's own GO:0042106 is unaffected.

Not acted on:
- Szymczak 2005 residue-level numbers (D127 or K128 mutation abolishes internalization; L131/L132 ~60%
  reduction): only K128 is in the abstract; full text not cached. Not used.
- Li 2024 sepsis biomarker (doi:10.3390/ijms25020749) and Menon 2024 CD3 aptamers
  (doi:10.1016/j.omtn.2024.102198): expression-correlation / translational, not gene function. Not fetched.
- Shah 2021 / Xu 2020 reviews: general TCR pathway, already covered.

Report errors: none detected (no wrong DOIs, no fabricated numbers among those checked: Treg ~log10 read
reduction, autoimmunity in all six Rowe patients, one-log lower CD3 in Lee 2019 all match full text). Only
issue is the gamma-delta omission above.

Consistency with CD3D/CD3E: first core MF kept as GO:0030159 contributing to GO:0004888; MHC class II receptor
activity row kept MARK_AS_OVER_ANNOTATED; receptor internalization core function kept CD3G-only. Nothing in the
primary evidence argues otherwise (PMID:15778375 shows the (D/E)xxxLL signal is CD3G-specific; CD3D
contributes YxxL motifs).
