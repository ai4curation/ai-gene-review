# CG6836 (Q9VVV2) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q9VVV2 is the canonical Swiss-Prot product of CG6836 (FBgn0036834). It is 328 aa, from the
single annotated transcript CG6836-RA. It is not a fragment, isoform or alternative gene model. Its
length matches vertebrate OST-alpha (326-340 aa), and it has seven predicted TM helices and four
predicted N-glycosylation sites at the N-terminus (positions 2, 15, 25, 42), all in the predicted
extracellular N-terminal domain 1-44.

Literature: there are no experimental papers on CG6836. The falcon deep research correctly flags that
dOSCP1 (CG13178) is a different protein. The only paper that names FBgn0036834 is Dawson et al. 2010
[PMID:20538072 "It is important to note that the list of putative OSTα orthologues includes genes from
invertebrates such as the sea squirt (Ciona intestinalis; ENSCING00000009741), fruit fly (Drosophila
melanogaster; FBgn0036834), and roundworm (Caenorhabditis elegans; C18A3.4)."]. It also proposes that
the ancestral substrates were not bile acids [PMID:20538072 "Since bile acids (salts) have not been
detected in invertebrate animals [34], these results suggest that the original function of OSTα was to
transport non-bile acid (salt) substrates such as steroid hormones or eicosanoids."]. Vertebrate
OST-alpha needs OST-beta for plasma-membrane delivery [PMID:23506901 "is required for delivery of the
functional transporter complex"].

Evolutionary placement: PTHR23423 is heterogeneous (OST-alpha, TMEM184, Hfl1, LAZ1). UniProt gives
only the family. The PANTHER 19.0 fruit-fly classification file has no row for Q9VVV2/FBgn0036834, and
the PANTHER geneinfo API returns no family for it. So CG6836 has no PANTHER subfamily and no PAINT
node, and there are no IBA rows. I built an MAFFT + NJ tree of 15 PTHR23423 members
(CG6836-bioinformatics/RESULTS.md). CG6836 is sister to vertebrate SLC51A (SF11/SF80) inside an
OST-alpha-like clade with worm osta-1/2/3. The fly paralogs Tmep (SF17) and CG5850 (SF10, the TMEM184C
group) fall outside that clade. Identity is low (15-21%) and the tree has no bootstrap, so the placement
is moderate. This is consistent with the Ensembl Compara ortholog call.

Family review interpro/panther/PTHR23423/PTHR23423-review.yaml: it uses CG6836 as the reference
protein and gives a single catch-all "subfamily" (OST-alpha/TMEM184/Hfl1). It does not disagree with
this placement. It simply makes no subfamily-level assignment, and its caution against transferring
bile-acid transport is the same as mine.

Annotation decisions (3 rows):
- plasma membrane (IEA, SubCell): ACCEPT. Ortholog inference, with the OST-beta caveat noted.
- membrane (IEA, ARBA): ACCEPT. Directly supported by the TM helices. The ARBA rule itself is not
  used as evidence.
- membrane (ISS from mouse Slc51a Q8R000): ACCEPT. The donor is in the right lineage. The curators
  transferred only the location, not bile-acid transport. That is treated as deliberate, so no MF or
  BP is added.
No NEW annotations. Transporter MF and bile-acid/steroid transport BP are not asserted, because the
substrate and partner are unknown and the vertebrate activity requires OST-beta.

Relative for next review: human SLC51A (Q86UW1), the experimentally characterized OST-alpha. It is
an ortholog-lineage relative by tree and Ensembl Compara, not by a shared PANTHER subfamily, because
CG6836 has no subfamily assigned. There is no review in the repo. The module
modules/enterohepatic_bile_salt_cycling.yaml covers SLC51A in vertebrates. CG6836 is not a member of
that module.

## Follow-up on description sources (2026-11-01)

- The Alliance automated text says CG6836 is "Used to study chromosome 3q29 microdeletion syndrome". This disease-model statement most likely comes from the Drosophila 3q29 screen [PMID:32053595 "We systematically characterized developmental, cellular, and nervous system phenotypes for 14 conserved homologs of human 3q29 genes and 314 pairwise interactions using Drosophila"]; SLC51A (OSTalpha), the human ortholog of CG6836, lies in the 3q29 region. The cached main text does not name CG6836, so inclusion could not be verified. It is an RNAi disease model, not evidence of molecular function; no annotation change.
