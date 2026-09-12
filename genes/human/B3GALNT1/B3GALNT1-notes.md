# B3GALNT1 (O75752) review notes

## Identity and core function

B3GALNT1 (UDP-GalNAc:beta-1,3-N-acetylgalactosaminyltransferase 1; also known as
beta-1,3-galactosyltransferase 3 / beta3Gal-T3 / B3GALT3; globoside synthase; Gb4
synthase). Human gene on chromosome 3, HGNC:918, UniProt O75752, 331 aa, single-pass
type II Golgi membrane protein.

- UniProt RecName: "UDP-GalNAc:beta-1,3-N-acetylgalactosaminyltransferase 1"; EC 2.4.1.79
  attributed to PubMed:10993897 [file:human/B3GALNT1/B3GALNT1-uniprot.txt "EC=2.4.1.79 {ECO:0000269|PubMed:10993897}"].
- AltNames include "Globoside synthase" and
  "UDP-N-acetylgalactosamine:globotriaosylceramide beta-1,3-N-acetylgalactosaminyltransferase"
  [file:human/B3GALNT1/B3GALNT1-uniprot.txt "AltName: Full=Globoside synthase"].

### Catalytic activity (authoritative, UniProt)

Reaction: a globoside Gb3Cer (d18:1(4E)) + UDP-N-acetyl-alpha-D-galactosamine =
a globoside Gb4Cer (d18:1(4E)) + UDP + H(+); EC 2.4.1.79; RHEA:22252
[file:human/B3GALNT1/B3GALNT1-uniprot.txt "Reaction=a globoside Gb3Cer (d18:1(4E)) + UDP-N-acetyl-alpha-D-"].
So B3GALNT1 transfers GalNAc in beta-1,3 linkage from UDP-GalNAc onto
globotriaosylceramide (Gb3 / CD77 / Pk antigen), producing globoside (Gb4 /
globotetraosylceramide), which is the P blood-group antigen.

Cofactor: Mg(2+) [file:human/B3GALNT1/B3GALNT1-uniprot.txt "Name=Mg(2+); Xref=ChEBI:CHEBI:18420"].

### Primary experimental evidence

PMID:10993897 (Okajima et al. 2000, J Biol Chem; abstract-only in cache,
full_text_available: false) — expression cloning of human globoside synthase;
identified beta3Gal-T3 as the globoside synthase. Substrate-specificity analysis of
extracts from cDNA-transfected L cells confirmed the product transfers GalNAc onto
Gb3: [PMID:10993897 "the gene product was actually beta1, 3-N-acetylgalactosaminyltransferase that specifically catalyzes the transfer of N-acetylgalactosamine onto globotriaosylceramide"].
TLC immunostaining confirmed the new component as globoside
[PMID:10993897 "supported the identity of the newly synthesized component as globoside"].
Notably the abstract stresses that members of one glycosyltransferase family need not
use the same acceptor/donor
[PMID:10993897 "do not necessarily catalyze reactions utilizing the same acceptor or even the same sugar donor"] —
directly relevant to the family-level GO:0008499 (GlcNAc beta-3-galactosyltransferase)
IBA annotation being a poor fit for this GalNAc-transferring member.

Tissue expression: expressed in many tissues including heart, brain, testis
[PMID:10993897 "The globoside synthase gene was expressed in many tissues, such as heart, brain, testis, etc."].
UniProt: higher expression in heart and brain
[file:human/B3GALNT1/B3GALNT1-uniprot.txt "Higher expression in heart and brain, and to a"].

### Localization

Golgi apparatus membrane; single-pass type II membrane protein
[file:human/B3GALNT1/B3GALNT1-uniprot.txt "SUBCELLULAR LOCATION: Golgi apparatus membrane; Single-pass type II"].
Feature table: TOPO_DOM 1-20 Cytoplasmic; TRANSMEM 21-43 signal-anchor for type II
membrane protein; TOPO_DOM 44-331 Lumenal — consistent with a Golgi glycosyltransferase.

### Family / fold

Belongs to glycosyltransferase 31 family (CAZy GT31); InterPro IPR002659
(Glyco_trans_31); PANTHER PTHR11214:SF153 "UDP-GALNAC:BETA-1,3-N-
ACETYLGALACTOSAMINYLTRANSFERASE 1"
[file:human/B3GALNT1/B3GALNT1-uniprot.txt "Belongs to the glycosyltransferase 31 family."].

## Disease / blood group (context, not GO-annotated here)

Genetic variation in B3GALNT1 underlies the blood group P1PK system (MIM:111400) and
the globoside (GLOB) blood group system defined by the P antigen (MIM:615021)
[file:human/B3GALNT1/B3GALNT1-uniprot.txt "B3GALNT1 activity is responsible for the globoside blood"].
Loss-of-function variants (e.g. E266A in P2(k), G271R in P1(k)) cause the rare
P(k) / globoside-deficient (P-null-like) phenotypes with lack of the P antigen
[file:human/B3GALNT1/B3GALNT1-uniprot.txt "P1(k) and P2(k) phenotypes are rare and characterized"].

## Reactome

- R-HSA-8878914 "B3GALNT1 transfers GalNAc to Gb3Cer to form Gb4Cer" — the reaction, a
  Golgi membrane-associated protein adding GalNAc to Gb3Cer to form Gb4Cer (Okajima 2000,
  Amado 1998). Supports GO:0047273 (MF) and GO:0000139 (Golgi membrane).
- R-HSA-9840309 "Glycosphingolipid biosynthesis" — parent pathway; supports GO:0006688.

## Annotation review reasoning summary

Core function is unambiguous and well supported: Gb4 (globoside) synthase, a Golgi
glycosphingolipid-branch enzyme.

- GO:0047273 (Gb4 synthase MF): ACCEPT — exact reaction (Gb3 + UDP-GalNAc -> Gb4);
  supported by EXP PMID:10993897, Reactome TAS, and IEA(EC/RHEA). This is the core MF.
- GO:0000139 (Golgi membrane): ACCEPT (IBA/IEA/TAS all agree; matches UniProt).
- GO:0006688 (glycosphingolipid biosynthetic process, TAS Reactome): ACCEPT as the BP
  aspect; the more precise child GO:0001576 (globoside biosynthetic process) is used in
  core_functions as the directly-supported process term.
- GO:0008499 (GlcNAc beta-3-galactosyltransferase activity, IBA): MODIFY -> GO:0047273.
  This family-level activity describes the Gal-onto-GlcNAc reaction of paralogous GT31
  members (B3GALT1/2/4/5); B3GALNT1 instead transfers GalNAc onto a Gal acceptor (Gb3).
  The IBA propagated the ancestral family activity, but the specific member catalyzes a
  different reaction (explicitly flagged by PMID:10993897).
- GO:0009312 (oligosaccharide biosynthetic process, IBA): MODIFY -> GO:0001576. The
  product is a membrane glycosphingolipid, not a free oligosaccharide; globoside
  biosynthetic process is the correct, specific process.
- GO:0009101 (glycoprotein biosynthetic process, IEA InterPro): MARK_AS_OVER_ANNOTATED.
  B3GALNT1 glycosylates a lipid (ceramide-based Gb3), not a protein; InterPro2GO applied
  a generic GT31 mapping. Not removed (IEA is not clearly contradicted at the family
  level, but wrong for this member's demonstrated biology).
- GO:0016020 (membrane, IEA InterPro): MODIFY -> GO:0000139 (Golgi membrane) — too
  general; specific Golgi localization is known.
- GO:0016758 (hexosyltransferase activity, IEA): KEEP_AS_NON_CORE — correct but a broad
  parent of the specific MF.
- GO:1901135 (carbohydrate derivative metabolic process, IEA ARBA): KEEP_AS_NON_CORE —
  correct but very general.
