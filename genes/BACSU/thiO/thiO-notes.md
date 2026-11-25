# thiO (O31616) notes, Bacillus subtilis 168

Deep research providers were not available in this session, so no `-deep-research-<provider>.md`
file was generated. Sources: UniProt O31616, cached abstracts PMID:9827558, PMID:11744710,
PMID:12627963, PMID:19864430 (all abstract-only), PTHR13847 PAINT/family review, and the
comparator reviews genes/PSEPK/thiO and genes/ECOLI/thiH. PMID:15105420 (cited by UniProt for the
structure) is not cached.

## Identity
- Glycine oxidase, EC 1.4.3.19; synonyms goxB, yjbR; BSU11670. DAO family, ThiO subfamily
  (IPR012727); PANTHER PTHR13847:SF289 (GLYCINE OXIDASE).

## Function
- Oxidative deamination [PMID:11744710 "it has been clearly shown that GO catalyzes the oxidative deamination of primary and secondary amines"].
- Substrates [PMID:9827558 "This protein effectively catalyzed the oxidation of sarcosine (N-methylglycine), N-ethylglycine and glycine."]; Km 46-81 mM for D-proline/D-alanine (UniProt kinetics).
- Thiamine role [PMID:12627963 "we demonstrate that ThiO is required for the biosynthesis of the thiazole moiety of thiamin pyrophosphate"]; disruption -> thiazole auxotrophy (UniProt DISRUPTION PHENOTYPE).
- Physiological substrate glycine [PMID:19864430 "more active on glyphosate than on the physiological substrate glycine"].
- Note conflict: PMID:26875494 (P. putida paper) states B. subtilis ThiO prefers D-proline; the B. subtilis
  kinetics (Km 46 mM D-proline vs ~1 mM glycine) do not support that as a physiological preference.

## Decisions
- GO:0043799 rows ACCEPT (core). GO:0016491 MODIFY -> GO:0043799. GO:0050660 MODIFY -> GO:0071949;
  GO:0071949 KEEP_AS_NON_CORE.
- GO:0006520 amino acid metabolic process MARK_AS_OVER_ANNOTATED (in vitro substrate range, no
  in vivo amino-acid metabolic role).
- GO:0009228 and GO:0009229 both ACCEPT (siblings in GO, not parent/child), as for ECOLI thiH.
- NEW GO:0052837 thiazole biosynthetic process (IMP, PMID:12627963): ThiO catalyses the glycine
  imine step; comparators ECOLI thiF (IMP) and BACSU thiI (IBA) carry the term.
- Cytoplasm (IBA root node PTN000354057; IEA SubCell) ACCEPT.
