# fliD (PA1094, Q9K3C5) — curation notes

## Gene identity

UniProt Q9K3C5 (secondary P72153), `FLID2_PSEAE`, 474 aa, reviewed; PseudoCAP
PA1094; matches the worklist accession. RecName "B-type flagellar
hook-associated protein 2 (HAP2)", because PAO1 carries the B type of the two
divergent P. aeruginosa fliD types [PMID:10678962]. PANTHER PTHR30288:SF0;
Pfam PF02465 (FliD_N), PF07195 (FliD_C), PF07196 (Flagellin_IN); InterPro
IPR040026 (FliD), IPR003481 (FliD_N), IPR010809 (FliD_C). PDB 5FHY covers
residues 78-405. UniProt COILED 408-454; SUBUNIT "Homopentamer {ECO:0000250}"
— superseded, see below.

## What is established

- The cap at the filament tip. "A FliD (also called HAP2) oligomer forms the cap
  protein complex that is located at the tip of the flagellar filament (Yonekura
  et al." [PMID:27664419]. For PAO1 specifically: "In the crystal, FliD78–405
  monomer subunits are arranged in hexamers, resulting in a shape akin to a
  six-pointed star when viewed from the top of the FliD oligomer (Figure 2a),
  which corresponds to the distal end of the growing flagellum."
- Oligomeric state is a hexamer, not a pentamer. "Thus, we confirmed that the
  hexameric assembly of FliD78–405 occurs not only in the crystalline
  environment but also in solution using negative stain EM class averaging (Tang
  et al." and "Full-length FliD1–474, by contrast, forms up to hexamers in
  solution (Figure 3e,f), which are likely to represent the physiologically
  relevant oligomerization state of this protein on the tip of the flagellum."
  [PMID:27664419]. UniProt still records a homopentamer by similarity; recorded
  as a CONFIRMED UNIPROT source defect (SUBUNIT).
- Motility requires it. "We found that swimming motility that was lost in the
  ΔfliD strain was restored in both ΔfliD/fliD1–474 and
  ΔfliD/fliD1–474(I167C/D253C) complementation strains" and Salmonella fliD does
  not complement PAO1 [PMID:27664419].
- FliD is itself a mucin adhesin. "A polar chromosomal insertional mutation in
  the P. aeruginosa fliD gene made this organism nonadhesive to mucin in an in
  vitro mucin adhesion assay." plus a competition experiment: "purified FliD
  protein inhibited the mucin adhesion of nonpiliated P. aeruginosa PAK-NP,
  while the same concentrations of PilA and FlaG proteins of P. aeruginosa were
  ineffective in this function." [PMID:9488388]. The purified-protein
  competition is what makes this more than a flagellum-loss phenotype.
- Regulation: fliD is sigma-28-independent and depends on FleQ and RpoN
  [PMID:9488388].
- A caveat on the hook: "Notably, in mutants of Salmonella that lack filaments,
  FlgK (HAP1), FliD (HAP2) and FlgL (HAP3) form a layered structure at the
  distal end of the hook-basal body (Homma and Iino, 1985)." [PMID:27664419] —
  a transient pre-filament placement, not hook membership.

## Comparator check before proposing anything new

FliD does part of the work of filament elongation, so GO:0044780 bacterial-type
flagellum assembly looked like a gap. QuickGO (2026-10-28) for Q9K3C5, P24216
(E. coli), P16328 (Salmonella) and P39738 (B. subtilis) returns only
GO:0009421, GO:0071973, GO:0009288, GO:0009424, GO:0005576, GO:0007155 and
GO:0005515 — no FliD orthologue carries any flagellum-assembly or -organization
term, and E. coli FliD's only experimental process annotation is GO:0071973
(IMP, PMID:25350000). A systematic absence across four species and several MODs
is a convention, not a twenty-year oversight: the cap's contribution is recorded
through the motility term plus the filament-cap component. No NEW row was added.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000767631 | GO:0009421 bacterial-type flagellum filament cap | 1 (sole seed) | 20 (19 taxa, PAINT leaf GAF) | GO:0009421, IDA, PMID:9488388 (PseudoCAP) | SOUND | The conclusion is right at every level. All 20 leaves are FliD orthologues, the cap is the defining structure of the family, and the PAINT curator has already placed NOT IBDs for this term and for GO:0071973 at two descendant nodes (PTN004740641, PTN004740642) covering flagellum-less lineages, which is the careful treatment. For PAO1 FliD itself the cap is established structurally (hexamer in crystal, solution and EM; PDB 5FHY) with a matching motility phenotype. The one weakness is the choice of reference: PMID:9488388 is the mucin-adhesion and fliD-regulation paper, and its abstract reports no cap-localisation experiment, treating the cap identity as background. The full text is not accessible (PMC returns no body), so per the rule on not overruling curators I did not downgrade the row or file a PseudoCAP defect; the better reference, PMID:27664419, is recorded in the review and is absent from GOA. |

The same node also carries a GO:0071973 IBD, but that one is seeded by E. coli
P24216 and B. subtilis P96786, not by PAO1 fliD, so it is outside this gene's
seeding scope; the IBA row on fliD was still reviewed and accepted.

PseudoCAP's other row for PA1094 is GO:0007155 cell adhesion (IDA, same paper),
which seeds no IBD; it is sound (purified-protein competition) but non-core.

## Decisions summary

- ACCEPT (4): GO:0009421 (IBA, IDA seed, IEA from IPR040026); GO:0071973
  motility (IBA).
- MODIFY (1): GO:0009288 bacterial-type flagellum (IEA) -> GO:0009421 filament
  cap (specific descendant already carried with structural evidence).
- MARK_AS_OVER_ANNOTATED (1): GO:0009424 bacterial-type flagellum hook (IEA from
  IPR003481), with an InterPro source defect (CHECK): FliD is the filament cap,
  not a hook component, and the row appears family-wide, so the InterPro2GO
  mapping is what should be fixed. Not REMOVE, because FliD has been observed at
  the distal end of the hook-basal body in filament-less Salmonella mutants.
- KEEP_AS_NON_CORE (3): GO:0005576 extracellular region (true, not refinable to
  the cap term by GO's relations); both GO:0007155 cell adhesion rows (real
  secondary host-interaction role).
- NEW: none (see the comparator check above).
- Source defects: UNIPROT SUBUNIT homopentamer -> homohexamer (CONFIRMED);
  InterPro IPR003481 -> GO:0009424 mapping (PROBABLE). No PseudoCAP defect.
