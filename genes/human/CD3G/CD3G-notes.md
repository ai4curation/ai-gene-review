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


## Whole reassessment — 2026-10-05

This reassessment preserves all 111 distinct archived GOA assertions, their qualifiers and WITH/FROM entities, all 91 prior reference identities and the original journal above. The imported historical review had no alternative-products slot and no authored NEW annotation. The archived UniProt record identifies human CD3G/P09693 as a 182-residue precursor, with a 22-residue signal peptide, extracellular immunoglobulin-like domain, transmembrane segment and one cytoplasmic ITAM. The seven UniProt-only supplemental citations absent from both local and inspected main caches remain unclosed; they were not silently fetched or treated as formal reviewed references.

All 111 prior decisions, all 23 formal publication headers/available complete abstracts, all 62 Reactome event summaries, five source-method records and the authentic archived Falcon report were assessed. Falcon is secondary orientation, not a substitute for primary evidence. Selected original Methods/Results/captions were additionally inspected for the human extracellular CD3 gamma-epsilon structure, TRIM-associated surface labeling, human gamma-delta receptor structures, regulatory-T-cell assays and human trafficking. The access ledger records which bodies were available versus actually read. No coordinate reanalysis, figure-pixel inspection, supplementary-target-table inspection or complete-paper reading is inferred from a full-text flag.

### Receptor assembly and signaling

CD3 gamma provides physical extracellular/transmembrane contacts and a phosphorylatable ITAM. The [human assembly study](https://pubmed.ncbi.nlm.nih.gov/8636209/), [extracellular gamma-epsilon structure](https://pubmed.ncbi.nlm.nih.gov/15136729/) and [whole human receptor structure](https://pubmed.ncbi.nlm.nih.gov/31461748/) support this own contribution. The 2004 construct used an engineered peptide linker; it does not imply that native gamma and epsilon form an interchain disulfide. The older double-TCR model in PMID:9485181 is not used as present stoichiometry. [Phosphorylated ITAM binding](https://pubmed.ncbi.nlm.nih.gov/8647168/) supports effector recruitment without making CD3G a kinase. Broad receptor activity is retained with its original source qualifier, while the core explicitly describes the complex contribution rather than CD3G antigen recognition.

The prior objection to contributes_to MHC-II receptor activity did not account for the qualified complex role. Eleven inspected production human GO-CAM activities include P09693 in an alpha-beta receptor complex enabling that activity. They reuse PMID:1323144 for activity and PMID:31461748 for composition and are not eleven independent experiments. The canonical PMID:1323144 abstract names zeta/delta ubiquitination and does not expose the original gamma or clone-specific assay; that original citation remains UNVERIFIED at that level. The positive curated model plus separate human composition evidence supports the qualified assertion. The core uses broader transmembrane signaling receptor activity, without claiming all TCRs are MHC-II restricted. Model example: [685de18700003492](https://noctua.geneontology.org/editor/graph/gomodel:685de18700003492); local cached activity and all eleven exact model pins are recorded in the independent consultation.

Mouse gamma-delta stoichiometry from PMID:16418397 is not generalized to humans. Selected original Methods/Results in [PMID:38657677](https://pmc.ncbi.nlm.nih.gov/articles/PMC11153141/) use reconstituted human Vgamma9Vdelta2 and Vgamma5Vdelta1 TCR complexes, ExpiHEK293F expression and Jurkat76 functional assays. Both include gamma-epsilon; a dimeric whole Vgamma5 receptor is not a native CD3G homodimer. The isolated-tail self-association in PMID:14967045 remains a non-core in-vitro observation.

### Binding and compartment evidence

The nine HuRI interaction assertions remain qualified non-core binding under the explicit project instruction. Each exact partner is preserved and is also positively recorded in reviewed UniProt; this corroborates curated identity without establishing an independent experiment. No screen supplementary target construct/table was newly inspected. Neither genericity nor a membrane-protein partner warrants declaring an edge false. Finer interface or adaptor functions are not inferred merely from partner names. The original PMID:11186279 letter cache lacks a scientific abstract; the same TCR-association claim is supported separately by human assembly/structure, rather than pretending the letter assay was recovered.

Selected original [PMID:11390434](https://pmc.ncbi.nlm.nih.gov/articles/PMC2193385/) Methods/Results directly include surface-biotinylated Jurkat CD3 gamma reprecipitation. Thus its TRIM/zeta title does not invalidate CD3G localization, and TRIM-driven signaling effects are not reassigned to CD3G. Plasma-membrane receptor location is central; broad membrane and transient coated-vesicle locations remain non-core.

A separate official-source check found a concrete Reactome identity problem: [R-HSA-2029455](https://reactome.org/content/detail/R-HSA-2029455) calls the Fc receptor gamma chain CD3G, and the input chain through R-HSA-2029093 and R-HSA-1861690 reaches [R-HSA-197917/P09693](https://reactome.org/content/detail/R-HSA-197917). Official human [FCER1G](https://www.ncbi.nlm.nih.gov/gene/2207/) instead maps to P30273/NCBI2207/HGNC3611. The event is marked MISCITED specifically for attributing this molecular context to CD3G; the immutable source record remains intact. Related Fc-receptor/Leishmania contexts retain unverified target attribution, rather than claiming every underlying physical-entity chain was audited. Their GOA assertions here are plasma-membrane location, which independent human TCR evidence supports. No new Fc receptor, phagocytosis or catalytic CD3G function is asserted. The source-mapping correction belongs with Reactome curation; no cache is edited.

### Sorting-tail role

The second core is an AP-2-binding sorting signal, grounded in actual target motif experiments, rather than a process inferred only from necessity. The [official AP-2 complex-binding definition](https://amigo.geneontology.org/amigo/term/GO:0035612) concerns the clathrin adaptor complex, not the AP-2 transcription factor. Selected original [PMID:9230070 Methods/Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC2138198/) show immobilized CD3 gamma peptides binding adaptins from human Jurkat cytosol, with LLAA and spacing controls. Mouse CD4/human CD3 gamma-tail chimeras and human JGN intact-receptor experiments are separate systems. These assays are not a pure two-component reconstitution. The authenticated normal PMID:9230070 cache contains full XML text. Its complete header/abstract and selected original Methods/Results were inspected; the normal cache preserves duplicated extraction passages exactly.

The existing protein-transport assertion remains a MODIFY to receptor internalization. Human [PMID:12794121](https://pubmed.ncbi.nlm.nih.gov/12794121/) is abstract-only in the normal cache; selected author-uploaded original Methods/Results/captions were read [externally](https://www.researchgate.net/publication/10719297_TCR_dynamics_in_human_mature_T_lymphocytes_lacking_CD3g). The work uses two patient-derived systems, retroviral restoration and acid-stripping to distinguish internalized from surface-bound antibody. Early stimulated uptake is delayed and recycling is impaired, while constitutive internalization/degradation persist. Therefore the sorting-tail role is not an absolute requirement for all uptake. Mature-chain S126/L131/L132/K128 numbering in older studies must not be confused with precursor numbering. No NEW biological-process row is proposed and no current cross-species comparator absence is claimed. Whether the binding MF needs a separate annotation remains an explicit question.

### Clinical scope and review outcome

Human CD3G deficiency is compatible with residual surface TCR. Polarization and activation-induced death effects in PMID:12407027 are retained outside the molecular core. The regulatory-T-cell cohort PMID:29653965 and CVID-like case PMID:31921117 have different measured phenotypes; autoimmunity and defective suppression are not universal claims. Actual PAINT IBD placements remain uninspected; short donor lists or the target in WITH/FROM are not negative evidence.

Review actions are 88 ACCEPT, 22 KEEP_AS_NON_CORE and one MODIFY, with no REMOVE, OVER, UNDECIDED or NEW. A lack of UNDECIDED rows does not mean every original assay was recovered: remaining original-assay limits are stated individually and independently supported annotations are retained. All previous notes remain as a historical prefix; this entry supersedes prior blanket binding removals, unverified PAINT-node narration and the no-own-MHC-contact objection. Current supporting quotations are finite cache-verbatim substrings; historical quotations in the immutable notes prefix are not new quotations.

Independent consultations covered identity/source projection, the qualified receptor/GO-CAM roles, and the Fc receptor identity issue; they did not author annotation actions. The source-specific decisions retain their stated access limits; the authenticated normal reference is integrated into this review.


### Receptor qualifier and complex scope clarification

The four source assertions of transmembrane signaling receptor activity retain their original enables qualifiers. An explicit question distinguishes that machine provenance from CD3 gamma's biological contribution to the assembled receptor; the core continues to describe its own assembly and signaling-adaptor role and its contribution to receptor activity. The first core uses GO:0042101 T cell receptor complex, whose official alpha-beta and gamma-delta children cover the separately inspected human structures, including PMID:38657677. This corrects the former alpha-beta-only complex scope without adding a redundant core or changing any annotation decision. The second, trafficking core retains the alpha-beta complex context actually tested in its cited experiments. A short cached structural anchor is added for PMID:38657677. A short literal normal-cache anchor for PMID:9230070 now supports the AP-2 core after verified source import.


### Authenticated sorting-motif source integration

The normal PMID:9230070 record confirms DOI10.1083/jcb.138.2.271 and PMCIDPMC2138198, with full XML availability. The imported text preserves the separation between human Jurkat/JGN assays and mouse CD4 extracellular/transmembrane domains joined to the human CD3 gamma tail. Immobilized peptides bind adaptins from cell cytosol, with dileucine and spacing controls; this does not establish a purified binary interaction. The existing AP-2 core receives one exact short supporting clause. All 111 machine assertions and manual decisions, 92 reference identities, both core activities, and the explicit receptor-qualifier question remain otherwise unchanged. No new annotation is introduced.


## 2026-10-09 — AP-2 annotation follow-up

The AP-2-binding molecular function already described in the core now has its own
GO:0035612 annotation with action NEW, qualifier enables and IPI evidence from
[PMID:9230070](https://pmc.ncbi.nlm.nih.gov/articles/PMC2138198/). The
[GO definition](https://www.ebi.ac.uk/QuickGO/term/GO:0035612) concerns the clathrin
adaptor complex. The new assertion describes CD3 gamma's own motif-dependent
association with that complex. It is supported by adaptin capture from human
Jurkat cytosol with immobilized human CD3 gamma-tail peptides and by dileucine,
D127 and spacing controls. The authors explicitly could not exclude another
molecule mediating the association, so no purified binary contact or specific
contacting AP-2 subunit is asserted.

[PMID:8187769](https://pubmed.ncbi.nlm.nih.gov/8187769/) supplies intact-receptor
context through motif mutations in human JGN transfectants; it is not described
as a second AP-2-binding assay. AP-1 was also recovered in the peptide experiments.
AP-2 is the selected core interaction because the accompanying biological role
is surface TCR internalization. AP-1 motif recognition is acknowledged without
adding an inferred TGN-trafficking process.

The nine existing generic-binding assertions concern different HuRI partners,
so none is repurposed as AP-2 evidence. All 111 source assertions and their
decisions remain intact. The review now contains 112 entries: 88 ACCEPT,
22 KEEP_AS_NON_CORE, one MODIFY and one NEW. The existing short PMID:9230070
quote is moved from the core to the new annotation; the core retains its source
citation. The answered question deferring the binding annotation is removed.
The other questions, both core activities and all reference records are
unchanged. No new biological-process assertion is proposed. This follow-up
supersedes the earlier decision to defer the AP-2 annotation.
