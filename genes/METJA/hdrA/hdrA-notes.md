# hdrA (MJ1190, P60200) — Methanocaldococcus jannaschii — review notes

## Literature search (2026-11-07)

Deep-research providers were unavailable, so no `-deep-research-*.md` file exists.
Searches run: WebSearch for "Kaster 2011 PNAS electron bifurcation MvhADG/HdrABC",
"Wagner 2017 Science HdrABC-MvhAGD structure", "Methanocaldococcus jannaschii
heterodisulfide reductase HdrA MJ1190 selenocysteine purified". No paper on purified
or genetically characterized M. jannaschii HdrA was found. All functional knowledge of
this protein is by homology to HdrA of Methanothermobacter marburgensis,
Methanothermococcus thermolithotrophicus and Methanococcus maripaludis.

Cached and read: PMID:9102456 (abstract only), PMID:21262829 (full text),
PMID:20534465 (full text), PMID:28818947 (abstract only).

## Sequence/record facts (UniProt P60200, PE 3)

- 657 aa, FAD-binding Rossmann region (FT BINDING 149..172, ECO:0000255), four
  4Fe-4S ferredoxin-type domains (PROSITE PRU00711), "Binds 4 [4Fe-4S] clusters per subunit".
- Probable selenocysteine at position 196, from PMID:9102456.
- FUNCTION and SUBUNIT lines are by similarity to Q6LWL2 (ECO:0000250): "Part of a
  complex that catalyzes the reversible reduction of CoM-S-S-CoB"; "The ferredoxin:CoB-CoM
  heterodisulfide reductase is composed of three subunits; HdrA, HdrB and HdrC."
- PANTHER PTHR43498:SF1. The family (11,512 proteins, 8,076 taxa per local
  `interpro/panther/PTHR43498/PTHR43498-metadata.yaml`) is much wider than methanogens.

## Biology

- In hydrogenotrophic methanogens the cytoplasmic MvhADG/HdrABC complex couples the
  endergonic reduction of ferredoxin with H2 to the exergonic reduction of CoM-S-S-CoB
  [PMID:21262829 "the purified complex from Methanothermobacter marburgensis catalyzes the
  CoM-S-S-CoB-dependent reduction of ferredoxin with H 2"; "Per mole CoM-S-S-CoB added, 1 mol
  of ferredoxin (Fd) was reduced, indicating an electron bifurcation coupling mechanism"].
- FAD is required and HdrA is the proposed bifurcation site [PMID:21262829 "Purification was
  performed in the presence of FAD, which was essential for activity recovery."; "it is
  reasonable to assume that electron bifurcation is flavin based and that therefore the FAD
  harboring subunit HdrA is the site of electron bifurcation in the MvhADG/HdrABC complex"].
- The disulfide is cleaved at HdrB, not HdrA [PMID:28818947 "the heterodisulfide is clamped
  between the two noncubane [4Fe-4S] clusters and homolytically cleaved"; HdrB carries
  these clusters]. PMID:20534465: "The β subunits were used for purification as this subunit
  has been demonstrated to contain the active site for heterodisulfide reduction".
- Methanococcales: Hdr forms a supercomplex with Vhu hydrogenase, Fdh and Fwd
  [PMID:20534465 "We identify a protein complex from the hydrogenotrophic methanogen,
  Methanococcus maripaludis , that contains heterodisulfide reductase, formylmethanofuran
  dehydrogenase, F 420 -nonreducing hydrogenase, and formate dehydrogenase."]. Selenocysteine
  (HdrAu) and cysteine (HdrAc) forms of HdrA exist in M. maripaludis [PMID:20534465 "In the
  case of the F 420 -nonreducing hydrogenase and HdrA, the two forms of the enzyme contain
  selenocysteine (Vhu and HdrA u ) or cysteine (Vhc and HdrA c )."].
- Hydrogenotrophs lack methanophenazine [PMID:20534465 "all other methanogens (the
  hydrogenotrophic methanogens) lack methanophenazine and cytochromes, have a cytoplasmic Hdr"].

## GO term findings (OLS)

- GO:0051912 "CoB--CoM heterodisulfide reductase activity" is DEFINED with methanophenazine
  as acceptor (EC 1.8.98.1, the membrane HdrDE of Methanosarcinales). It is the wrong
  electron-acceptor variant for a cytoplasmic HdrABC, and the disulfide step is HdrB's.
- No GO term exists for EC 1.8.98.5 (H2:CoB-CoM heterodisulfide,ferredoxin reductase) or
  EC 1.8.7.3-like bifurcating Hdr. The old GO:0045331 (heterodisulfide hydrogenase) is
  obsolete ("represents two activities"). No GO term contains "bifurcation".
- GO:0044678 CoB-CoM heterodisulfide reductase complex exists (definition mentions the
  six-subunit Methanobacterium complex = MvhADG/HdrABC).
- GO:0009055 electron transfer activity; GO:0050660 FAD binding; GO:0051539 4Fe-4S binding;
  GO:0019386 methanogenesis, from carbon dioxide.

## Evidence for the GOA rows

- IDA (MENGO, PMID:9102456): the paper identifies M. jannaschii selenoproteins by 75Se
  labelling and size matching to UGA-containing ORFs. Nothing in the abstract suggests a
  heterodisulfide reductase assay. Full text not seen, so not removed; flagged as a
  suspected wrong reference.
- QuickGO (2026-11-07): GO:0051912 has 952 annotations. Only 5 IBA rows, all from
  PTN000078336 with with/from = P60200 only: P60200, M. acetivorans HdrA1/HdrA2 (Q8TLB0,
  Q8TM02), and two Korarchaeum cryptofilum proteins (B1L4Y3, B1L5Y2). So the IBD that seeds
  this PAINT node rests on the selenoprotein-labelling IDA. M. marburgensis HdrA Q50756 has
  its own IDA (PMID:2121478) but is not among the with/from. Korarchaeum is not a known
  methanogen (not verified here; needs a check of its genome paper).

## Decisions

- Both GO:0051912 rows: MODIFY to NTR "H2:CoB-CoM heterodisulfide,ferredoxin reductase
  activity", contributes_to (whole-complex activity on a subunit, pattern 16; plus wrong
  acceptor variant).
- GO:0016491 oxidoreductase activity (ARBA): MODIFY to the same NTR (descendant).
- NEW: GO:0009055 electron transfer activity (subunit-level role), GO:0050660 FAD binding,
  GO:0051539 4Fe-4S cluster binding, GO:0044678 complex, GO:0019386 methanogenesis from CO2.
