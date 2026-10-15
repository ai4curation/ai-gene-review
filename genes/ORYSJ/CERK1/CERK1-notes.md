# OsCERK1 (ORYSJ CERK1, A0A0P0XII1) curation notes

## Identity
- Rice LysM receptor-like kinase OsLysM-RLK9 / OsCERK1, Os08g0538300; 624 aa, signal peptide,
  extracellular region with a single recognisable LysM, one TM helix, cytoplasmic Ser/Thr kinase
  (UniProt). Not to be conflated with Arabidopsis CERK1 (A8R7E6; genes/ARATH/CERK1), whose
  three-LysM ectodomain binds chitin directly.

## Chitin immunity (with OsCEBiP)
- Knockdown abolishes most chitin responses: [PMID:21070404 "Knockdown of OsCERK1 resulted in marked suppression
  of the defense responses induced by chitin oligosaccharides"].
- Chitin-induced receptor complex with CEBiP: [PMID:21070404 "suggested the ligand-induced formation of a receptor complex containing both CEBiP and OsCERK1"].
- Ligand binding is done by CEBiP, not OsCERK1: [PMID:21070404 "the observed binding of a biotinylated chitin oligosaccharide, GN8-Bio (Shinya et al., 2010), to the microsomal membrane was not affected by knockdown of OsCERK1"];
  [PMID:21070404 "it does appear that CEBiP plays a major role in chitin elicitor binding and that OsCERK1 functions as a signal transducer through its Ser/Thr kinase activity in rice"].
  Shinya et al. 2012 compared At/OsCERK1 ectodomains; only AtCERK1 is "sufficient for chitin perception by itself" [PMID:22891159]. Deep research: "in the tested colloidal-chitin assay, the rice OsCERK1 ectodomain did not bind" [file:ORYSJ/CERK1/CERK1-deep-research-falcon.md].
  => IEA (ARBA) and TAS chitin binding rows are transfers from AtCERK1 biology; REMOVE.
- Kinase substrates: OsRLCK185 [PMID:23498959 "OsRLCK185 associates with, and is directly phosphorylated by, OsCERK1 at the plasma membrane"];
  OsRacGEF1 S549 [PMID:23601108 "is activated when its C-terminal S549 is phosphorylated by the cytoplasmic domain of OsCERK1 in response to chitin"];
  OsCIE1 (E3 ligase brake) [PMID:38750355 "active OsCERK1 phosphorylates OsCIE1 and blocks its E3 ligase activity"].
- PGN signalling via LYP4/LYP6 [PMID:25335639 "OsCERK1 is essential for both PGN and chitin signaling initiated by OsLYP4 and OsLYP6"];
  knockout [PMID:24964058 "OsCERK1 is indispensable for chitin perception and participates in innate immunity in rice"].
- Plasma membrane: PMID:23498959 (abstract: "at the plasma membrane"), PMID:23601108, PMID:24964058 (GFP-OsCERK1 around infection hyphae).

## AM symbiosis (with OsMYR1/OsLYK2)
- KO impaired in AM symbiosis while Oscebip KO is not: [PMID:25231970 "OsCERK1 but not chitin-triggered immunity is required for AM symbiosis"].
- [PMID:25399831 "this gene is also necessary for the establishment of the mycorrhizal interaction as well as for resistance to the rice blast fungus"].
- Receptor heteromer: [PMID:31706032 "CO4 directly binds to OsMYR1, promoting the dimerization and phosphorylation of this receptor complex"]; kinase-dead T484A fails to rescue colonisation (deep research).
- Receptor competition between OsMYR1 and OsCEBiP for OsCERK1 [PMID:33853950 "OsMYR1 and OsCEBiP receptors compete for OsCERK1 to determine the outcome of symbiosis and immunity signals"].

## Curation decisions
- No existing annotation captures the symbiotic role; all BP rows are immune. Proposed NEW
  GO:0036377 arbuscular mycorrhizal association. Participation: OsCERK1 is the catalytically
  active kinase of the OsMYR1-OsCERK1 Myc-factor receptor heteromer (phosphorylates OsMYR1;
  kinase-dead does not rescue), so it does part of the work of symbiotic signalling.
  Comparator check (QuickGO, 2026-10-02): other symbiosis-signalling components carry
  GO:0036377 by IMP: rice D14L (Q10J20), rice CYCLOPS (A9XMT5), Medicago CNGC15a/b, CYCLOPS,
  and rice CCaMK has it in genes/ORYSJ/CCAMK. Passes.
- GO:0038187 pattern recognition receptor activity (EXP, PHI-base): OsCERK1 does not bind the
  PAMP itself in rice; MODIFY to transmembrane receptor protein kinase activity GO:0019199
  (co-receptor kinase).
- GO:0002768 -> MODIFY to the more specific GO:0002752 (is_a child, already IBA).
- Project question 4 (symbiosis vs defense): immunity terms remain on immune-specific rows;
  symbiosis captured separately by GO:0036377; the kinase MF is shared. No row conflates them.
- Project question 2 (LysM effector/receptor leakage): chitin binding on OsCERK1 is an
  ARBA/AtCERK1-derived leak; removed.
