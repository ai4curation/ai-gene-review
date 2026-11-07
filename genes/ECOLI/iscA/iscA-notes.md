# iscA (P0AAC8, E. coli K-12) notes

## Provenance of research

- Provider deep research could not run: `just deep-research-falcon` failed with an
  Edison API 403 authentication error in this container (2026-10-23). No
  `*-deep-research-*.md` file was created. Notes below are from the cached
  publications and the UniProt record.

## Function summary

- [2Fe-2S] cluster and transfer to ferredoxin [PMID:11319236 "It can assemble an
  air-sensitive [2Fe-2S] cluster as shown by UV-visible and resonance Raman
  spectroscopy."; "The metal form but not the apoform of IscA binds ferredoxin ...
  allowing transfer of iron and sulfide from IscA to ferredoxin"].
- Multiple-turnover cluster transfer [PMID:15964837 "Both IscU and IscA were found to
  be capable of multiple cycles of [2Fe2S] cluster formation and transfer"].
- Iron binding and donation to IscU [PMID:14720122 "IscA is an iron binding protein
  with an apparent iron association constant of 3.0x10(19) M(-1), and that
  iron-loaded IscA can provide iron for the assembly of transient iron-sulphur
  clusters in IscU"]; Cys99/Cys101 essential [PMID:15247288 "The IscA mutants that
  fail to bind iron are unable to mediate iron delivery"].
- In vivo iron loading, aerobic; bound iron oxidised to ferric [PMID:20942799 "oxygen
  in the medium promotes the iron binding in IscA by oxidizing ferrous iron to ferric
  iron in the iron binding site of IscA"]; iscA/sufA needed aerobically only.
- IscU is the preferred scaffold over IscA [PMID:16877383 "iron-sulfur clusters are
  assembled in IscU, but not in IscA, suggesting that IscU is a preferred
  iron-sulfur cluster assembly scaffold protein"].
- Genetics: required in reporter Fd coexpression system [PMID:10544286 "we show the
  iscS, iscA, hscA, and fdx genes to be required for the assembly of the Fe-S
  clusters"].
- Structure: homotetramer [PMID:15050828 "IscA exists as an (alpha1alpha2)2
  homotetramer"].
- Copper binds IscA anaerobically [PMID:28576762].

## Curation decisions (summary)

- Core MFs: GO:0140132 iron-sulfur cluster chaperone activity (agrees with the Isc
  module) and GO:0034986 iron chaperone activity (both experimentally supported; the
  relative in vivo importance of the two modes is unresolved). BP GO:0016226; CC
  cytosol.
- 3 GO:0005515 rows REMOVE (policy). cytoplasm IBA MODIFY to cytosol;
  Fe-S cluster binding IEA MODIFY to 2Fe-2S binding + cluster chaperone activity.
- ferrous iron binding, protein maturation, iron-sulfur cluster transfer complex:
  KEEP_AS_NON_CORE.
- Not reviewed here (not cached): ErpA/A-type carrier literature (Vinella 2009,
  Loiseau 2007) on IscA as a [4Fe-4S] carrier; worth adding on a future pass.
