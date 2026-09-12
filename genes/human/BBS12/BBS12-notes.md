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
