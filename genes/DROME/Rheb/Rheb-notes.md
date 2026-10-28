# Rheb (DROME, Q9VND8) review notes

## Session 1 (2026-10-28)

- `just fetch-gene DROME Rheb` resolved Q9VND8 (RHEB_DROME); 60 GOA rows. First attempt timed
  out on UniProt; the retry succeeded. Reactome R-DME-165131 failed to cache during fetch
  (timeout); its title ("GEF dissociates from DRheb-GTP") was confirmed via a separate fetch
  and entered by hand, the cache file was not kept (out of scope directory for this session).
- No deep research provider available; literature summary in `Rheb-deep-research-manual.md`.
- PMID:23028662 (Brown et al. 2012, mushroom body overexpression) read in full: overexpression
  phenotypes only (Kenyon cell enlargement, 3 h memory deficit) [PMID:23028662 "Rheb
  overexpression in the mushroom bodies causes a memory deficiency"]. Not used for NEW terms
  per the strict NEW bar (gain-of-function phenotype, not participation).

### Key decisions

- Core MF: GTP-dependent activator of TORC1 kinase (GO:0043539 protein serine/threonine kinase
  activator activity, IBA) plus GTPase activity / GTP binding as the switch.
- Core BP: positive regulation of TORC1 signaling (multiple IMP/IDA rows) [PMID:12766776
  "Rheb functions in the insulin signalling pathway downstream of Tsc1-Tsc2 and upstream of
  TOR"].
- `positive regulation of macroautophagy` (PMID:22952930) appears to be a sign error: the
  paper reports Rheb overexpression increases (non-significantly) p62 dots, which indicates
  inhibition [PMID:22952930 "Enhancing TOR signaling by overexpression of its activator Rheb
  or knockdown of the Rheb inhibitor Tsc2 also increased p62 dot number"]. MODIFY to negative
  regulation of macroautophagy and recorded as a source defect (PROBABLE).
- `positive regulation of axon guidance` (PMID:22319582): the only data are overexpression-
  induced misrouting; the direction does not follow. MARK_AS_OVER_ANNOTATED.
- `negative regulation of TORC2 signaling`: S2-cell evidence suggests indirect feedback via
  S6K [PMID:16627617]. UniProt's FUNCTION text for PMID:22493059 instead says "May also have a
  role in activating TORC2 signaling", which conflicts with the IDA row from the same paper
  (abstract-only, cannot verify). Kept as non-core; flagged.
- PMID:11782951 (Kozma & Thomas 2002, Bioessays review on PI3K/PKB/S6K) is cited as IMP for
  insulin receptor signaling. A review is an odd source for IMP, and the abstract does not
  mention Rheb; cannot verify without full text. Kept the claim (supported by PMID:12766776),
  flagged the reference.
- Plasma membrane (IBA + Reactome TAS): no Drosophila evidence; Rheb is an endomembrane
  (Golgi/ER, lysosome in mammals) GTPase. MARK_AS_OVER_ANNOTATED.
- Golgi membrane now has direct Drosophila support [PMID:36435842].
- Protein binding rows: REMOVE per protein-binding policy (interactions with Tctp, Cln7, sau are
  real but uninformative as GO:0005515).

## 2026-10-28 PR review fix: GO:0016239 row

- The GO:0016239 positive regulation of macroautophagy IMP row (PMID:22952930) is still MODIFY to GO:0016242. Its only support was the non-significant p62 result, so it now also cites the PMID:18474623 (GFP-2xFYVE punctae) and PMID:24265594 (GFP-Atg8 in muscle) quotes, which show that Rheb negatively regulates macroautophagy.
- Its FlyBase source defect now asks for DELETE_ROW instead of REPOINT, and corrected_value/corrected_label were dropped. GO:0016242 is already annotated independently from PMID:18474623, and a non-significant result cannot support either sign. The explanation now says this.
