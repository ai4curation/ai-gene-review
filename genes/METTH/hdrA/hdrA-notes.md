# hdrA (MTH_1381, O27434) - Methanothermobacter thermautotrophicus Delta H - review notes

## Literature search (2026-11-07)

Deep-research providers were unavailable; no `-deep-research-*.md` file exists.
Searches (WebSearch): "Setzke Hedderich Thauer 1994 H2:heterodisulfide oxidoreductase
complex", "Stojanowic 2003 Mvh physiological role", "Hamann 2007 CCG domain HdrB",
"Kaster 2011 electron bifurcation MvhADG/HdrABC". No paper characterises the Delta H
HdrA protein itself; strain Delta H appears only in genome/sequence papers
(PMID:9371463). All biochemistry is on the Marburg strain, now Methanothermobacter
marburgensis.

Cached and read: PMID:21262829 (full text), PMID:8119281 (abstract), PMID:12856108
(abstract), PMID:28818947 (abstract), PMID:17929940 (full text), PMID:2654933 (abstract).

## Record facts (UniProt O27434, PE 3)

- 659 aa. FAD-binding region 159..182 (ECO:0000255); four 4Fe-4S ferredoxin-type
  domains (PROSITE PRU00711), "Binds 4 [4Fe-4S] clusters per subunit".
- Name, EC 1.8.98.5 and FUNCTION by similarity to Q50756 (M. marburgensis HdrA).
- PANTHER PTHR43498:SF1 (family PTHR43498, "FERREDOXIN:COB-COM HETERODISULFIDE
  REDUCTASE SUBUNIT A").
- Rhea for EC 1.8.98.5: RHEA:55748 (Rhea REST query ec:1.8.98.5, 2026-11-07), equation
  "coenzyme B + coenzyme M + 2 reduced [2Fe-2S]-[ferredoxin] + 2 H(+) = coenzyme
  M-coenzyme B heterodisulfide + 2 H2 + 2 oxidized [2Fe-2S]-[ferredoxin]". The
  methanophenazine reaction of GO:0051912 is RHEA:18085 (EC 1.8.98.1).

## Ortholog identity (file:METTH/hdrA/hdrA-bioinformatics/RESULTS.md)

O27434 is 97.1% identical to Q50756 over 658 aligned columns. Delta H HdrB and MvhA
are 94.7% and 97.5% identical to their Marburg orthologs.

## Biology

- In strain Marburg, H2 reduction of the heterodisulfide is catalysed by a stable complex
  of F420-non-reducing hydrogenase and heterodisulfide reductase [PMID:8119281 "this
  reaction is catalyzed by a stable H2-heterodisulfide oxidoreductase complex of
  F420-non-reducing hydrogenase and heterodisulfide reductase"]. The 80-kDa subunit
  (HdrA) is in the subcomplex with FAD and heterodisulfide reductase activity
  [PMID:8119281 "The other subcomplex was composed of the 80-, 36- and 21-kDa subunits;
  1 mol trimer contained 0.8 mol FAD"].
- The purified MvhADG/HdrABC complex reduces ferredoxin with H2 only with
  CoM-S-S-CoB present, 1 Fd per heterodisulfide [PMID:21262829 "Per mole CoM-S-S-CoB
  added, 1 mol of ferredoxin (Fd) was reduced, indicating an electron bifurcation
  coupling mechanism"]. FAD is essential [PMID:21262829 "Purification was performed in
  the presence of FAD, which was essential for activity recovery."]. HdrA is the
  proposed bifurcation site [PMID:21262829 "the FAD harboring subunit HdrA is the site
  of electron bifurcation in the MvhADG/HdrABC complex"].
- The heterodisulfide is cleaved at HdrB, not HdrA [PMID:28818947 "the heterodisulfide
  is clamped between the two noncubane [4Fe-4S] clusters and homolytically cleaved"].

## Decisions

- GO:0016491 (ARBA IEA): MODIFY to the proposed term "H2:CoB-CoM
  heterodisulfide,ferredoxin reductase activity" (same proposed_name as METJA/hdrA), to be
  read as contributes_to.
- NEW: electron transfer activity (own role; no bifurcation term in GO), FAD binding,
  4Fe-4S cluster binding, GO:0044678 complex, GO:0019386 methanogenesis from CO2.
- No GO:0051912 row on this gene, so pattern 20 does not apply here directly; it does
  on METTH/hdrB.
