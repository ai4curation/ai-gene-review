# PFK2 notes (P16862, YMR205C) — PFK beta subunit

- alpha4beta4 PFK, EC 2.7.1.11 [UniProt:P16862 "SUBUNIT: Heterooctamer of 4 alpha and 4 beta chains."]; [PMID:3007939 "Subcloning of both genes in one multicopy vector (YEp13) and reintroduction into the yeast cell resulted in a 3.5-fold higher specific activity"].
- pfk2 has the stronger glycolytic defect [PMID:27226568 "exhibits reduced downstream glycolytic intermediates, glucose consumption, and ethanol production"].
- V-ATPase: [PMID:24860096 "In vitro ATP hydrolysis and proton transport were reduced by 35% in pfk2Δ membrane fractions"]; [PMID:24860096 "Glucose-dependent reassembly was 50% reduced in pfk2Δ"].
- RNA functions: [PMID:41816908 "Strikingly, Pfk2p displays directional 5'-3' double-stranded RNA unwinding activity not seen with Pfk1p."]; [PMID:41816908 "Pfk2p dynamically associates with ribosomes and promotes translation of cell cycle genes."]; own-mRNA binding [PMID:21124907 "Four of the 13 proteins (30%) were associated with their own mRNA (Pfk2, Pre2, Map1, Meu1)."].

Decisions: RNA helicase/ribosome/translation/mRNA-binding rows KEEP_AS_NON_CORE (single recent study); response to glucose MARK_AS_OVER_ANNOTATED; V-ATPase pump-activity/proton-transport rows MARK_AS_OVER_ANNOTATED; vacuolar acidification, pH, V-ATPase assembly KEEP_AS_NON_CORE; protein binding x7 REMOVE.

## QA pass 2026-11-19
- 5'-3' RNA helicase activity (IDA PMID:41816908) KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED: GO:0032574 is defined as unwinding driven by ATP hydrolysis, but the paper reports [PMID:41816908 "These findings suggest that ATP hydrolysis is not strictly required for Pfk2p’s unwinding activity."]. No GO term exists for ATP-independent RNA duplex unwinding.
- mitochondrial outer membrane (IEA SubCell) KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED (same organelle-policy reasoning as PFK1).
- obsolete canonical glycolysis IBA: added propagation_review.
- mRNA binding IDA (PMID:21124907): reason corrected (it previously cited the Albihlal 2026 paper by copy-paste).
- GO:0046961 IGI (PMID:18632794, UniProt): With/From is PFK2 itself; recorded a WRONG_WITH_FROM source defect (should be PFK1, P16861).
- Added the SGD description file as a reference with reference_review (VERIFIED).
