# tgpA (PA2873, Q9HZX3) — curation notes

## Gene identity

UniProt Q9HZX3, `TGPA_PSEAE`, 668 aa, reviewed; PseudoCAP PA2873; matches the
worklist accession. EC 2.3.2.13; PANTHER PTHR42736:SF1; Pfam PF11992 (TgpA_N /
DUF3488-type N-terminal region), PF01841 (Transglut_core), PF13559; SMART
TGc; SUPFAM "Cysteine proteinases". PDB 6G49 and 6G4H cover residues 180-499.
UniProt topology: six TM helices in the first 180 residues, a large
periplasmic domain 180-548, one more TM helix 549-569, cytoplasmic C-terminus.
Catalytic triad Cys404 (nucleophile), His448, Asp464 — all `ECO:0000250`
(inferred by similarity), not mutated experimentally.

## What was actually assayed

This matters for the seed, so it is worth stating precisely. The only
experimental paper is PMID:23209712.

- The protein assayed was not full-length TgpA but the His10-tagged
  periplasmic domain expressed in *E. coli*: "the N-(His)10-tagged periplasmic
  domain (aa 180–544) of PA2873 protein (TG180–544) was expressed in E. coli
  and subjected to affinity purification."
- The assay was a kit: "Transglutaminase activity (TGase; EC 2.3.2.13) was
  assayed by a Transglutaminase Colorimetric Microassay Kit (Covalab) which
  uses immobilized N-carbobenzoxy(CBZ)-Gln-Gly as amine acceptor and
  biotin-conjugated cadaverine as amine donor." So the acyl donor is a blocked
  dipeptide and the amine donor is a diamine, not a protein lysine.
- Result: "TG180–544 was positive to the TGase test." and "2.5 µg of
  TG180–544, equal to reference gpTGase, showed TGase activity that differed
  significantly from the negative control and was about 45% of gpTGase activity
  in the absence of EDTA."; "Unlike gpTGase, EDTA addition did not affect
  TG180–544 activity", hence Ca2+-independent (UniProt MISCELLANEOUS).
- Localisation: five tryptic peptides of the periplasmic domain were recovered
  from washed PAO1 membrane fractions by MudPIT, and "Since all five PA2873
  peptides 'shaved' by trypsin belonged to the predicted outside membrane
  domain, this strongly supports the notion that it actually emerges from
  membrane itself."
- Essentiality: antisense expression of a 350-nt fragment impairs PAO1 growth,
  only in the antisense orientation and from two different vectors, and a
  PrhaB::tgpA conditional strain shows only residual growth under repression.
  The authors conclude "we suggest that TgpA takes part in an essential
  function linked to the cell wall." and list four possible envelope roles
  (peptidoglycan assembly, maturation/secretion of periplasmic proteins,
  surface polypeptide assembly, LPS biogenesis).
- Relatives with known activity: Methanothermobacter prophage PeiW/PeiP are
  pseudomurein endoisopeptidases, and "In the periplasm of B. bronchiseptica,
  WbmE protein catalyzes the deamidation of uronamide-rich O chains of
  lipopolysaccharide (LPS)". Neither is a protein cross-linker.

So the demonstrated chemistry is gamma-glutamyl transfer to a primary amine —
the EC 2.3.2.13 reaction as EC writes it — while the GO definition of
GO:0003810 is the protein-to-protein isopeptide cross-link. No TgpA substrate
is known, and the catalytic triad has never been mutated.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002126683 | GO:0003810 protein-glutamine gamma-glutamyltransferase activity | 1 (sole seed; the same experiment is annotated twice, by PseudoCAP and by UniProt) | 17 (15 taxa, PAINT leaf GAF) | GO:0003810, IDA, PMID:23209712 (PseudoCAP, and identically UniProt) | OVER-SPECIFIC | The seed is an activity assay on purified protein, not a mutant phenotype, so it is not the usual phenotype-as-function failure, and for TgpA itself the row stands. But what was assayed is amine incorporation by an isolated domain with surrogate substrates; GO:0003810 asserts protein-protein cross-linking, which was not shown, and no physiological substrate is known. The 17 leaves (Chloroflexi, Aquificae, Thermodesulfovibrio, Dictyoglomus, Synechocystis, Deinococcus, three Rhodopirellula paralogues, B. subtilis YebA, B. cereus, Listeria, Streptomyces, Shewanella, Geobacter, Xanthomonas) are named only by domain content, PF01841 is a papain-like fold used for proteolysis and deamidation as well as transamidation, and the nearest characterised relative, Bordetella WbmE, is a deamidase. A GO_CENTRAL `WRONG_TERM`/CHECK defect asks for a more general node term (e.g. GO:0016755 aminoacyltransferase activity) or restriction of the IBD to Pseudomonas TgpA orthologues. No PseudoCAP defect: the row is a reasonable reading of the paper and matches UniProt's own call. |

PseudoCAP has no other annotation for PA2873 (the plasma membrane IDA is
UniProt's), so no further seed needs assessment.

## Decisions summary

- ACCEPT (6, all rows): GO:0003810 (IBA, two IDA rows, IEA from EC/Rhea);
  GO:0005886 plasma membrane (IDA, IEA).
- No MODIFY, no REMOVE, no NEW. The essentiality result is a strong phenotype
  but names no process TgpA performs, so it is described in `description` and
  in the knowledge gap rather than annotated (the Unknown-substrate problem is
  exactly a BIOLOGY gap: a wet-lab experiment would close it).
- One GO_CENTRAL source defect at PTN002126683 (term too specific for the
  clade); no PseudoCAP defect.
