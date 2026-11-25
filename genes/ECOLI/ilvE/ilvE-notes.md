# ilvE (P0AB80) — Escherichia coli K-12 — curation notes

Provider deep research was not run for this gene. These notes are drawn from the
cached publications in `publications/` and the UniProt record
(`ilvE-uniprot.txt`). Several key papers are abstract-only in the cache and
Europe PMC returned no full text for PMC216874 or PMC235221 (scanned 1970s
J Bacteriol articles), so the reasoning below rests on abstracts plus the
curated UniProt record.

## Identity and activity

- IlvE is transaminase B, the branched-chain amino acid aminotransferase
  (EC 2.6.1.42) [PMID:378964 "Transaminase B (branched-chain amino acid
  aminotransferase, EC 2.6.1.42), the ilvE gene product, was purified to
  apparent homogeneity"].
- Purified enzyme transaminates all three branched-chain amino acids with
  2-oxoglutarate, and aromatic amino acids only weakly [PMID:378964 "Purified
  transaminase B catalyzed transamination between alpha-ketoglutarate and
  l-isoleucine, l-leucine, l-valine, and, to a lesser extent, l-phenylalanine
  and l-tyrosine, the latter reacting very sluggishly."]. This directly
  supports the substrate-specific children GO:0052654 (Leu), GO:0052655 (Val)
  and GO:0052656 (Ile) as well as the parent GO:0004084; all three Rhea
  reactions are on the UniProt record.
- There is no separate valine transaminase in E. coli: valine and isoleucine
  activities co-purify and are both removed by anti-IlvE antibody
  [PMID:378964 "These observations argue against the existence of a separate
  valine-alpha-ketoglutarate transaminase."].
- The purified enzyme lacks aspartate transaminase activity [PMID:378964 "The
  enzyme was free of aspartate transaminase and of transaminase C."].
- Quaternary structure: hexamer of identical subunits, double-trimer
  arrangement [PMID:378964 "was confirmed to be that of a hexamer with a
  molecular weight of about 182,000 and apparently identical subunits"].
  UniProt: "SUBUNIT: Homohexamer."
- Cofactor: PLP, Lys160 Schiff base (UniProt COFACTOR and MOD_RES
  N6-(pyridoxal phosphate)lysine; class-IV PLP aminotransferase family,
  Pfam PF01063, PROSITE PS00770). Several crystal structures exist (1IYE etc.).

## Pathway role

- UniProt places IlvE at the final step (4/4) of L-isoleucine, L-leucine and
  L-valine biosynthesis. GOA has leucine and valine biosynthesis rows but no
  L-isoleucine biosynthetic process row; added as NEW.
- The tyrosine-repressible aromatic aminotransferase TyrB also contributes to
  leucine biosynthesis, and IlvE alone can satisfy a phenylalanine requirement
  [PMID:15983 "the tyrosine-repressible enzyme is also active in leucine
  biosynthesis. The ilvE gene product alone can reverse a phenylalanine
  requirement."].

## L-aspartate biosynthesis rows

- The IGI row (PMID:15983, with aspC and tyrB) is a genetic-interaction
  annotation from an aminotransferase triple-mutant study. The abstract shows
  that in ilvE- strains either AspC or TyrB suffices for aspartate, and that
  no aminotransferase activity for the alpha-keto acids of Tyr, Phe or Asp
  was detected in the triple mutant. The full text is not available, so the
  exact basis for the IlvE-aspartate link is not visible; the curator's
  acts_upstream_of_or_within row is not removed, but it is marked as
  over-annotated, matching the IBA row (AspC and TyrB carry aspartate
  transamination).
- The IBA row propagates involved_in L-aspartate biosynthesis from this single
  IGI seed (PTN000214714) to gammaproteobacterial IlvE. Given that purified
  IlvE has no aspartate transaminase activity (PMID:378964), the involved_in
  claim is treated as over-annotated. The PTHR42743 family review also flags
  this node assertion as UNRESOLVED.

## Comparators

- P. putida ilvE (PSEPK), yeast BAT1/BAT2 and S. pombe eca39 all accept
  GO:0004084; the fungal reviews accept the three substrate-specific
  children, and the yeast/pombe reviews MODIFY GO:0003824 to GO:0004084 and
  GO:0009081 to the biosynthetic term. The same treatment is used here.

## Localization

- Cytosol: identified in the E. coli cytosolic lysate proteome
  (PMID:18304323, IDA row) and IBA. Soluble enzyme, no signal peptide or TM.
