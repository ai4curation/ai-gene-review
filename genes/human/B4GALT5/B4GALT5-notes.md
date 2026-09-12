# B4GALT5 (human) — gene review notes

UniProt: O43286 (B4GT5_HUMAN). HGNC:928. Gene on chromosome 20.
Beta-1,4-galactosyltransferase 5 / lactosylceramide (LacCer) synthase. 388 aa,
single-pass type II Golgi membrane protein. Glycosyltransferase family 7 (GT7, CAZy).

## Identity and enzymatic function

B4GALT5 is one of seven human beta-1,4-galactosyltransferases (B4GALT1–7). Its
principal, physiologically dominant activity is as **lactosylceramide synthase**:
it transfers galactose from UDP-galactose to glucosylceramide (GlcCer) on the
lumenal face of the Golgi, producing lactosylceramide (LacCer, Galβ1-4Glc-ceramide)
+ UDP.

- UniProt recommended/alt names encode this directly:
  `[file:human/B4GALT5/B4GALT5-uniprot.txt "AltName: Full=Glucosylceramide beta-1,4-galactosyltransferase"]`
  and `[file:human/B4GALT5/B4GALT5-uniprot.txt "AltName: Full=Lactosylceramide synthase"]`,
  EC=2.4.1.274.
- UniProt FUNCTION: `[file:human/B4GALT5/B4GALT5-uniprot.txt "Catalyzes the synthesis of lactosylceramide (LacCer) via the"]`
  ... "transfer of galactose from UDP-galactose to glucosylceramide (GlcCer)".
- Catalytic activity (Rhea RHEA:31495, EC 2.4.1.274): beta-D-glucosyl-(1<->1')-N-acylsphing-4-enine
  + UDP-alpha-D-galactose = beta-D-Gal-(1->4)-beta-D-Glc-(1<->1)-Cer + UDP + H(+).
  Evidence ECO:0000269|PubMed:24498430 (experimental).
- Cofactor: Mn(2+) (`[file:human/B4GALT5/B4GALT5-uniprot.txt "Name=Mn(2+)"]`), typical of GT7 galactosyltransferases.

The corresponding GO molecular-function term is **GO:0008489
UDP-galactose:glucosylceramide beta-1,4-galactosyltransferase activity**, whose GO
definition and Rhea xref match the UniProt reaction exactly (verified via OLS).

## Key experimental evidence (LacCer synthase, IMP)

Yamaji & Hanada 2014 (PMID:24498430, full text cached) generated B4GalT5-deficient
HeLa clones by TALEN and showed:
- `[PMID:24498430 "B4GalT5 is the major LacCer synthase"]` (abstract and Discussion).
- `[PMID:24498430 "The present study also demonstrated that B4GalT5 is the major LacCer synthase in HeLa cells because the Stx-binding negative population appeared in the transfection of a pair of TALEN-B4GalT5 plasmids, and TAL-G5#2 clone showed considerable reduction in Gb3 and GM3, both downstream metabolites of LacCer."]`
- Consistent with B4GalT5-knockout mice; the paralog B4GalT6 has minor/redundant
  LacCer synthase activity (`[PMID:24498430 "we confirmed that B4GalT6 also exhibits discernible activity of LacCer synthase in cells"]`).
This directly supports the IMP annotation to GO:0008489 (PMID:24498430).

LacCer is the common branch-point precursor for ganglio-, globo-, (iso)globo- and
(neo)lacto-series glycosphingolipids: `[PMID:24498430 "GlcCer is converted to lactosylceramide (LacCer) on the lumen side of the Golgi apparatus"]`;
LacCer is "the starting point in the biosynthesis of all gangliosides"
(`[file:human/B4GALT5/B4GALT5-uniprot.txt "LacCer is the starting point in the biosynthesis"]`).

## Broader galactosyltransferase activity (glycoproteins)

Like other B4GALTs, B4GALT5 can also transfer Gal to terminal GlcNAc on
glycoprotein N-glycans (beta-N-acetylglucosaminylglycopeptide beta-1,4-galactosyltransferase,
GO:0003831; forms N-acetyllactosamine). This underlies the Reactome N-glycan/keratan
annotations and the IBA/ISS "glycoprotein biosynthetic process" (GO:0009101)
annotations. The active-site GlcNAc-binding residues are annotated in UniProt
(BINDING 298..301, 340 to N-acetyl-D-glucosamine). This is a secondary/broader
activity relative to the dominant LacCer-synthase role.

## Localization

Golgi apparatus, Golgi stack (trans cisternae) membrane; single-pass type II
membrane protein: `[file:human/B4GALT5/B4GALT5-uniprot.txt "Golgi apparatus, Golgi stack membrane"]`,
`[file:human/B4GALT5/B4GALT5-uniprot.txt "Single-pass type II membrane protein"]`,
Note=`[file:human/B4GALT5/B4GALT5-uniprot.txt "Trans"]` cisternae of Golgi stack.
IDA to trans-Golgi network (GO:0005802) from PMID:23913272 (D'Angelo et al 2013),
a study of intra-Golgi GlcCer transport and glycosphingolipid glycosylation tracks
(abstract-only in cache; experimental annotation deferred to curator).

## Physiological roles (from mouse ortholog Q9JMK0, ISS/IEA)

Mouse B4galt5 knockout is embryonic lethal; the gene is essential for
extraembryonic development. UniProt (by similarity to mouse Q9JMK0) attributes:
role in glycosylation/stability of BMPR1A; ganglioside biosynthesis; CNS neuronal
maturation, axonogenesis, myelination. These human annotations are ISS/IEA
transferred from mouse and are plausible but not directly demonstrated in human;
kept as non-core (developmental/tissue-level roles downstream of the core enzymatic
function). `[file:human/B4GALT5/B4GALT5-uniprot.txt "Plays a role in the glycosylation of BMPR1A"]`,
`[file:human/B4GALT5/B4GALT5-uniprot.txt "Essential for"]` extraembryonic development.

## Induction / disease context

Up-regulated in subcutaneous adipose tissue in obesity/diabetes; knockdown
improves insulin resistance (PMID:29415997, INDUCTION). Not in GOA annotations;
contextual only.

## Protein interactions

GOA has two IPI "protein binding" (GO:0005515) annotations, both to HSPA13
(UniProt P48723), from high-throughput AP-MS interactome screens
(PMID:28514442 BioPlex/Nature 2017; PMID:33961781 BioPlex Cell 2021). UniProt
INTERACTION line records O43286–P48723 (HSPA13), NbExp=2. These are
uninformative bare "protein binding" from proteome-scale screens; marked as
over-annotated (not removed, per policy for IPI).

## Curation summary

- Core MF: **GO:0008489** UDP-galactose:glucosylceramide beta-1,4-galactosyltransferase
  activity (LacCer synthase) — experimentally supported (IMP, PMID:24498430).
- Core BP: **GO:0001572** lactosylceramide biosynthetic process; broader
  **GO:0006688** glycosphingolipid biosynthetic process.
- Secondary MF: **GO:0003831** beta-1,4-galactosyltransferase activity on
  glycoprotein N-glycans (GlcNAc -> LacNAc).
- Location: **GO:0000139** Golgi membrane (trans-Golgi).
- Developmental/neural ISS annotations from mouse ortholog: KEEP_AS_NON_CORE.
- Bare "protein binding" IPI: MARK_AS_OVER_ANNOTATED.
- Redundant Reactome "Golgi membrane" TAS annotations: ACCEPT (one), others
  duplicate the same location.
</content>
</invoke>
