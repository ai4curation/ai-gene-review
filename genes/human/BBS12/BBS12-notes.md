# BBS12 (Q6ZW61) review notes

## Gene identity
- Human BBS12, gene C4orf24, HGNC:26648, chromosome 4. 710 aa.
- UniProt RecName: "Chaperonin-containing T-complex member BBS12". SIMILARITY: belongs to the TCP-1 chaperonin family, BBS12 subfamily.
- Vertebrate-specific branch of chaperonin-related proteins [PMID:17160889 "highlights the major role of a vertebrate-specific branch of chaperonin-related proteins in Bardet-Biedl syndrome"].
- InterPro domains: Cpn60/GroEL/TCP-1 (IPR002423), GroEL-like apical/equatorial/intermediate folds; PANTHER PTHR46883 "Bardet-Biedl syndrome 12 protein".

## Core function: BBSome assembly chaperone (not a structural BBSome subunit)
- BBS6 (MKKS), BBS10, BBS12 are three chaperonin-LIKE BBS proteins that, with CCT/TRiC chaperonins, form the "BBS-chaperonin complex" that mediates BBSome assembly [PMID:20080638 "a novel complex composed of three chaperonin-like BBS proteins (BBS6, BBS10, and BBS12) and CCT/TRiC family chaperonins mediates BBSome assembly"].
- "Chaperonin-like BBS proteins interact with a subset of BBSome subunits and promote their association with CCT chaperonins. CCT activity is essential for BBSome assembly" [PMID:20080638].
- "BBS6, BBS10, and BBS12 are necessary for BBSome assembly, and ... impaired BBSome assembly contributes to the etiology of BBS phenotypes" [PMID:20080638].
- The mature BBSome (GO:0034464) consists of BBS1,2,4,5,7,8,9; BBS12 is NOT one of these structural subunits [PMID:22500027 "Seven of the BBS proteins (BBS1, 2, 4, 5, 7, 8, and 9) have been shown to form a complex known as the BBSome"].
- The BBS-chaperonin complex (incl. BBS12) plays a role in BBS7 stability and seeds the BBS7-BBS2-BBS9 "BBSome core" assembly intermediate [PMID:22500027 "the BBS-chaperonin complex plays a role in BBS7 stability. BBS7 interacts with BBS2 and becomes part of a BBS7-BBS2-BBS9 assembly intermediate referred to as the BBSome core complex"].
- => BP: chaperone-mediated protein complex assembly (GO:0051131) is well supported (IMP MGI from PMID:20080638; also IBA/IEA). This is the CORE function.

## Interactions (basis of IPI "protein binding" annotations)
- UniProt SUBUNIT/INTERACTION: BBS10 (Q8TAM1), BBS2 (Q9BXC9), BBS7 (Q8IWZ6), BBS9 (Q3SYG4), MKKS/BBS6 (Q9NPJ1).
- IntAct IPI annotations from PMID:20080638 cite WITH = Q3SYG4(BBS9), Q8IWZ6(BBS7), Q8TAM1(BBS10), Q9BXC9(BBS2), Q9NPJ1(MKKS) — all the bona fide BBS partners.
- PMID:22500027 IPI WITH = BBS7 (Q8IWZ6), MKKS (Q9NPJ1).
- PMID:26900326 IPI WITH = MKKS (Q9NPJ1): "Interacts with MKKS" [UniProt SUBUNIT, ECO:0000269|PubMed:26900326]. This paper is primarily an MKKS/BBS6 H395R case report, but characterizes MKKS-BBS12 interaction.
- PMID:28514442 and PMID:33961781 = Bioplex high-throughput AP-MS interactome studies (Huttlin et al.); IPI WITH = BBS7 (Q8IWZ6), MKKS (Q9NPJ1). High-throughput but corroborate the curated interactions.
- The IPI partners all point to the assembly-chaperone interaction network; the underlying MF is adapter/unfolded-protein-binding within BBS-chaperonin complex, not generic "protein binding".

## Subcellular location
- UniProt: Cell projection, cilium; localized to the basal body of the primary cilium of differentiating preadipocytes [PMID:19190184 (Marion 2009) FUNCTION + SUBCELLULAR LOCATION]. (PMID:19190184 not in cache; UniProt curated.)
- GO:0005929 cilium is IEA from UniProtKB-SubCell SL-0066. Reasonable but indirect; the curated location is more specifically basal body. Chaperone assembly factors act in cytoplasm; ciliary/basal-body localization is consistent with role in transient ciliogenesis during adipogenesis.

## Adipogenesis / fat cell differentiation
- BBS12 inactivation in human MSCs facilitates adipogenesis, increases insulin sensitivity and glucose utilization; Bbs12-/- mouse: increased obesity [PMID:22958920 "BBS12 inactivation facilitated adipogenesis, increased insulin sensitivity, and glucose utilization"].
- GO:0045599 negative regulation of fat cell differentiation, IMP from PMID:22958920, acts_upstream_of_or_within. Loss of BBS12 -> enhanced adipogenesis means BBS12 normally restrains/negatively regulates fat cell differentiation. Direction is consistent. This is downstream/pleiotropic (via ciliary dysfunction), not the molecular core function => KEEP_AS_NON_CORE.

## Photoreceptor cell maintenance
- GO:0045494 IBA from GO_Central (PANTHER PTN002478298). Retinal degeneration / pigmentary retinopathy is a cardinal BBS feature; BBS12 loss causes BBSome assembly failure -> ciliary trafficking defects in photoreceptors. Plausible phylogenetic inference but downstream/pleiotropic, not the molecular core. KEEP_AS_NON_CORE.

## ATP binding
- GO:0005524 ATP binding, IEA ECO:0000256 from InterPro IPR002423 (Cpn60/GroEL/TCP-1). Group II chaperonins are ATP-dependent. However BBS6/10/12 are divergent chaperonin-LIKE proteins; their ATP-binding/hydrolysis competence is not experimentally established for BBS12. No experimental ATPase data. The InterPro family-level mapping is plausible but unverified for this divergent subfamily. Flag as MARK_AS_OVER_ANNOTATED / cautious — keep but note lack of direct evidence (cannot REMOVE an IEA without positive contradiction; degenerate, so flag).

## Summary of actions
- GO:0045494 photoreceptor cell maintenance (IBA) -> KEEP_AS_NON_CORE (pleiotropic ciliopathy phenotype, downstream).
- GO:0051131 chaperone-mediated protein complex assembly (IBA) -> ACCEPT (core).
- GO:0005524 ATP binding (IEA InterPro) -> MARK_AS_OVER_ANNOTATED (family inference, no direct evidence in divergent subfamily).
- GO:0005929 cilium (IEA SubCell) -> KEEP_AS_NON_CORE / ACCEPT (curated location basal body; keep).
- GO:0051131 chaperone-mediated protein complex assembly (IEA InterPro) -> ACCEPT (redundant with IBA/IMP, core).
- GO:0005515 protein binding x5 (IPI) -> all MARK_AS_OVER_ANNOTATED (uninformative "protein binding"; suggest more specific MF). Partners are real BBS assembly partners.
- GO:0045599 negative regulation of fat cell differentiation (IMP) -> KEEP_AS_NON_CORE.
- GO:0051131 chaperone-mediated protein complex assembly (IMP PMID:20080638) -> ACCEPT (core, best-evidenced).
</content>


## 2026-09-30: primary-source reassessment

This entry supersedes the earlier molecular-function and evolutionary conclusions while preserving the journal above. BBS12 participates in BBSome assembly, but the reviewed experiments do not establish that BBS12 itself folds a bound protein. The separate authored GO:0044183 proposal and the five inherited generic-interaction replacements are withdrawn. The twelve inherited source assertions are retained, with ten missing supporting-entity lists restored by the normal local seeder. Seven previously collapsed partner-specific sources are recovered from the unchanged GOA file. The nineteen distinct source tuples represent twenty raw records: the duplicate PMID:26900326 MKKS interaction is represented once. All twelve resulting generic interactions remain KEEP_AS_NON_CORE under the supplied ActionEnum. The decisions are three ACCEPT, fourteen KEEP_AS_NON_CORE, one MODIFY and one UNDECIDED, with no NEW annotation.

The normal source projection was confined to a temporary file with title fetching disabled. The seven recovered sources explicitly identify BBS7, BBS10, BBS2 or MKKS/BBS6; source identifiers are independently corroborated by the UniProt interaction list. Each received a supplemental annotation consultation. BBS12's association with those partners is distinguished from direct protein-folding activity, purified binary affinity and the exact supplementary BioPlex experiments that were not independently inspected. The earlier annotation count reflected the inherited collapsed representation and did not establish complete partner-specific source coverage.

The assembly evidence combines BBS12-containing complexes and depletion effects (PMID:20080638, PMID:22500027). Selected complete assembly/stability Results and Discussion passages from the cached second paper describe loss of BBS2 after BBS12 depletion and release of BBS12 as assembly proceeds. The protease-sensitivity experiments in Bbs6/Bbs7 contexts are not a direct BBS12 folding assay. BBS10-specific regulation experiments are not relabeled as BBS12 experiments. The core therefore records chaperone-mediated complex assembly without inventing a molecular function; the physical assembly step and nucleotide dependence remain open questions.

PMID:26900326 was checked beyond its MKKS-focused title. Complete cached construct-generation and cell-culture Methods and the relevant Results and Figure 4 caption explicitly include Myc-tagged wild-type BBS12 with FLAG-tagged wild-type or mutant MKKS in human HEK293T and ARPE-19 cells. The MKKS H395R variant affects co-immunoprecipitation differently in the two cell lines. These are association experiments, not a purified direct-affinity or BBS12 folding assay. No blot-image reanalysis is claimed.

The ATP-binding IEA is UNDECIDED. ATP binding and ATP hydrolysis are different claims. PMID:24010126 reports motif divergence in a comparative non-vertebrate chaperonin-like BBS collection and discusses earlier vertebrate work. Those sequence observations neither measure human BBS12 nucleotide binding nor prove its absence. This study also supersedes the earlier blanket vertebrate-specific wording. No new phylogeny or alignment reconstruction was performed.

The electronic cilium localization is refined to ciliary basal body, supported by the curated UniProt source note and the primary PMID:19190184 abstract concerning differentiating preadipocytes. This is not an assertion of exclusive basal-body localization or absence from the axoneme. The complete official abstract of PMID:40914337 describes primary-cilium localization, variant-dependent instability, altered partner interactions and changed ciliary length in human HEK293T and hTERT-RPE1 models; it does not resolve basal body versus shaft or establish an autonomous ATPase/folding activity. Its publisher full-text request returned 403; no full Methods, Results, images or construct-level controls were inspected. BBS12 being degraded does not establish participation in protein degradation, and no such process is proposed.

The complete PMID:22958920 abstract explicitly reports increased adipogenesis after BBS12 inactivation in human primary mesenchymal stem cells. That supports retaining negative regulation of fat-cell differentiation as a contextual, non-core outcome. Separate mouse knockout metabolic results are not substituted for the human-cell evidence. Its full Methods and Results were not inspected.

All six original cached abstracts were reviewed during annotation consultation. The exact BioPlex supplementary bait/prey records and the PAINT ancestral node/alignment were not independently reconstructed; curated interactions and phylogenetic assertions are retained without claiming these audits. PMID:20080638 remains an abstract-only canonical cache, supplemented by separately inspected official indexed Results and textual captions. Other full-text flags do not imply that every paragraph, figure or supplement was read. The original Falcon report and its artifact are preserved as leads; their absolute axoneme and nucleotide claims are not adopted. HGNC:26648, NCBI Gene 166379 and UniProt Q6ZW61 identify the same human BBS12 target. Two RefSeq transcripts encode the same protein; no alternative product is invented. No matching cached GO-CAM was found.

Independent annotation consultation and root synthesis agree on the assembly-only core. The normal Source86 cache import supplies PMID:19190184, PMID:24010126 and PMID:40914337; new reference titles are taken from those machine-generated records. No provider report, GOA file, UniProt cache or existing publication is rewritten. The only new quoted excerpt is an 11-word anchor from PMID:22500027. Validation and rendering results follow separately after application.

### Validation of this revision

Focused schema, term, reference and best-practice validation passed on 2026-09-30. The 13 advisories comprise 12 supported generic-binding rows retained as non-core under the supplied ActionEnum and one unused-provider-evidence advisory. The unchanged provider report is a lead map; primary publications support the annotation decisions. Rendering passed. No repository-wide validation pass is claimed.


## 2026-09-30 — source and citation follow-up

The ATP-binding rationale now explicitly includes the published comparison with vertebrate orthologs and has a short verbatim primary-source anchor (PMID:24010126). Motif divergence weakens the electronic transfer; it does not measure human BBS12 nucleotide binding. The decision remains UNDECIDED, with binding distinguished from hydrolysis. This supersedes any reading of the earlier rationale as restricting the divergence to non-vertebrates.

The description now names BBS10 among the associated assembly proteins, restores the mature BBSome composition and cytoplasmic context, and keeps evidential judgments in the review and knowledge gap. The PMID:33961781 full-text-unavailable flag was incorrect and is removed; its uninspected supplementary pair records remain a separate reading limit. The PMID:20080638 notes now identify the selected PMC text as external consultation, separate from the abstract-only normal cache. Its unrelated additional citation on photoreceptor maintenance is removed. The Falcon assessment again distinguishes independently supported assembly/localization claims from unverified motif, localization-exclusion, signaling and quantitative claims.

The twelve generic interaction rows remain KEEP_AS_NON_CORE because their named associations are supported while an informative molecular activity is unresolved. REMOVE and UNDECIDED are available actions; neither is selected merely to satisfy the generic-binding advisory. This is an explicit biological judgment under the supplied ActionEnum, despite the narrower action preference in the repository's protein-binding policy. It does not claim that the enum permits only KEEP_AS_NON_CORE. No source tuple or annotation action changes in this follow-up.
