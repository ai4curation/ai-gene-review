# mvhA (MTH_1134, Q50783) - Methanothermobacter thermautotrophicus Delta H - review notes

## Literature search (2026-11-07)

Deep-research providers were unavailable; no `-deep-research-*.md` file exists.
WebSearch: "Stojanowic Mander Duin Hedderich 2003 Mvh physiological role", "Setzke 1994
H2:heterodisulfide oxidoreductase complex", "Reeve 1989 polyferredoxin mvhDGAB".
Cached and read: PMID:2654933 (abstract; Delta H mvh operon), PMID:12856108 (abstract),
PMID:8119281 (abstract), PMID:21262829 (full text), PMID:28818947 (abstract).

## Record facts (UniProt Q50783, PE 3)

- 472 aa, [NiFe]/[NiFeSe] hydrogenase large subunit family; Ni(2+) binding Cys61, Cys64,
  Cys442, Cys445 (ECO:0000255); PROSITE NI_HGENASE_L_1/L_2.
- EC 1.12.99.- (acceptor not specified). FUNCTION "Part of a complex that provides reducing
  equivalents for heterodisulfide reductase."
- PANTHER PTHR43600:SF2 (family PTHR43600, "COENZYME F420 HYDROGENASE, SUBUNIT ALPHA";
  subfamily "F420-NON-REDUCING HYDROGENASE VHU SUBUNIT A"). The family name is dominated by
  FrhA, which is why an F420 family name sits on an F420-non-reducing enzyme.
- 97.5% identical to M. marburgensis MvhA P60227 (file:METTH/hdrA/hdrA-bioinformatics/RESULTS.md).

## Biology

- The Delta H mvhDGAB genes form an operon [PMID:2654933 "These genes, together with a
  fourth open reading frame designated mvhB, are tightly linked and appear to form an operon
  that is transcribed starting 42 base pairs upstream of mvhD."].
- Mvh (MvhA, MvhG, MvhD) is the hydrogenase that feeds Hdr; its only known role is to supply
  Hdr with electrons [PMID:12856108 "the only function of Mvh is to provide reducing
  equivalents for heterodisulfide reductase and that the MvhD subunit is an electron transfer
  protein that forms the contact site to heterodisulfide reductase"]. The 51/41/17-kDa
  subcomplex holds the nickel and has F420-non-reducing (viologen-reducing) hydrogenase
  activity [PMID:8119281].
- Ferredoxin is reduced by the complex only when the heterodisulfide is reduced at the same
  time [PMID:21262829 "Cell extracts of M. marburgensis catalyzed the reduction of Fd from C.
  pasteurianum with H 2 at significant rates only in the presence of CoM-S-S-CoB"].

## Decision on GO:0008901 ferredoxin hydrogenase activity (IEA, IPR018194)

Pattern 19 again (IPR018194, the acceptor-neutral Ni motif, mapped to an acceptor-specific
activity). Unlike Frh, ferredoxin is one of the two acceptors that Mvh electrons reach,
but only through HdrA bifurcation coupled to heterodisulfide reduction. GO:0008901 is the
uncoupled H2/ferredoxin reaction, which Mvh/Hdr does not catalyse at significant rates. MvhA's
electrons go to MvhG -> MvhD -> HdrA. Action: MODIFY to the proposed complex term (contributes_to),
which contains ferredoxin as acceptor, plus a source defect against the IPR018194 mapping.
Own subunit activity: contributes_to GO:0033748 hydrogenase (acceptor) activity (the
Mvh-module activity with viologens) — NEW.

## Decision on GO:0016151 nickel cation binding

ACCEPT, as for FrhA: the Ni of the [NiFe] site is on MvhA (four conserved Cys), and GO has no
[NiFe]-cofactor binding term.
