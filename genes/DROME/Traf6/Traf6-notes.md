# Traf6 (TNF-receptor-associated factor 6) notes

Gene: Traf6, FBgn0265464, CG10961. Formerly DTRAF2/dTRAF2 (and "Traf2" in several papers);
the other fly TRAFs are Traf4 (formerly DTRAF1, FBgn0026319, Q9XYR0) and Traf-like
(formerly dTRAF3, FBgn0030748, Q8IR14). Papers before about 2013 call this gene DTRAF2/dTRAF2 or
Traf2; "DTRAF1"/"dTRAF1" in those papers is today's Traf4, not this gene.

UniProt Q9W3I9 (unreviewed TrEMBL, 475 aa; RING 104-143, coiled coil 293-320, MATH 329-472). Two
other unreviewed entries exist for the gene: Q9XYQ9 ("TNF-receptor-associated factor 2", 463 aa,
from Liu et al. 1999) and Q9UAC4 ("TRAF6", 475 aa, direct submission). On 2026-11-17 QuickGO lists
only IEA rows on them (Q9XYQ9: GO:0004842, GO:0005164, GO:0016567, GO:0043122, GO:0005737; Q9UAC4: the
same plus GO:0046872 and GO:0005634). This review covers only Q9W3I9, the entry that carries the
FlyBase and PAINT rows (49 rows).

## Sources and searches (2026-11-17)

- Cached GOA references: 14 PMIDs. Full text available for PMID:11447260, PMID:14585960,
  PMID:16894030, PMID:21912646, PMID:24374193; the others are abstract-only.
- FlyBase hand-written description (`Traf6-deep-research-flybase.md`), fetched 2026-11-17. No
  Falcon/Perplexity deep research was run.
- PubMed queries run (E-utilities, 2026-11-17):
  - `Drosophila AND (Traf6 OR dTraf6 OR dTRAF2 OR Traf2[tiab]) AND (synapse OR neuromuscular OR NMJ OR
    neuron)` (5 hits; none reports Traf6 at a fly synapse or in synaptic function).
  - `Drosophila AND (Traf6 OR dTraf6 OR dTRAF2) AND (Toll OR Imd OR immune)` (30 hits, mostly
    mammalian or other invertebrates).
  - `Drosophila AND (Traf6 OR dTRAF6 OR dTRAF2) AND (lipopolysaccharide OR LPS)` (12 hits; none is a fly
    study of Traf6 or of LPS signalling).
  - `Kaneko T[au] AND Drosophila AND peptidoglycan AND LPS AND 2004` and
    `Leulier F[au] AND peptidoglycan recognition AND 2003` (found PMID:15142531 and PMID:12692550).
- QuickGO by reference PMID:10449347 (2026-11-17): FlyBase made 16 TAS rows from this review on
  2006-08-03, including GO:0007391 dorsal closure on both Traf4 and Traf6.
- Newly cached and quoted: PMID:15142531, PMID:12692550 (abstracts), PMID:10021364 (abstract).
- PANTHER tree (PANTHER 19 treeinfo for PTHR10131, scratch only) and PAINT rows from
  `interpro/panther/PTHR10131/PTHR10131-paint.tsv` in the coordinator checkout.

## Biochemistry and partners

- Domain architecture like mammalian TRAF6: N-terminal RING, zinc fingers, coiled coil, C-terminal
  MATH/TRAF domain [PMID:11447260 "Drosophila tumor necrosis factor receptor-associated factor 2
  (dTRAF2), a homologue of human TRAF6, physically and functionally interacts with Pelle, and is
  phosphorylated by Pelle in vitro."]. Liu et al. found the Msn kinase binds DTRAF1, not this protein
  [PMID:10021364 "Msn specifically binds the TRAF domain of DTRAF1 but not that of DTRAF2."].
- Receptor binding: Wengen [PMID:12894227 "Wengen, which is a type I membrane protein that can
  physically interact with the recently described TRAF2 homolog dTRAF2"]; Grindelwald (IntAct IPI,
  PMID:25874673) [PMID:33824334 "We recently identified a second Drosophila TNFR, Grnd, which interacts
  with both Egr and Traf2 and mediate Egr pro-apoptotic functions"]. Notch intracellular domain
  (PMID:25280943).
- Ubiquitination: the E2 Bendless (Ubc13) binds and regulates Egr-induced polyubiquitination of the
  protein [PMID:24162658 "Ben physically interacts with dTRAF2 and regulates Egr-induced dTRAF2
  polyubiquitination."]; dUev1a cooperates with Bendless through it (PMID:23726905); CYLD
  deubiquitinates and stabilises it (PMID:17765686). Ji et al. 2019 report K63-linked ubiquitination and
  E3 activity in a feedback loop with the Otu/Bam deubiquitinase (PMID:30879902, abstract-only here).

## Signalling roles

- Eiger-JNK: [PMID:17765686 "dCYLD regulates TNF-induced JNK activation and cell death through dTRAF2,
  which acts downstream of the TNF receptor Wengen and upstream of the JNKK kinase dTAK1."]; Bendless
  and dUev1a (PMID:24162658, PMID:23726905); Grnd (PMID:25874673).
- Toll/NF-kB: Shen et al. 2001 (Pelle binding; Dorsal activation in S2 cells). Cha et al. 2003: gain
  of function induces Dif and Relish nuclear translocation, and the null impairs antimicrobial gene
  induction [PMID:14585960 "DTRAF2 is required for NF-κB signaling and activation of the antimicrobial
  immune system."]; the null is viable [PMID:14585960 "Intriguingly, the mutant flies managed to develop
  into adult and showed no morphological defects."].
- Imd: Leulier et al. 2006 found the null fully resistant to Gram-negative infection [PMID:16894030
  "Hence, Traf2 appears not to be essential for an effective Imd-mediated immune response."]. So the
  Imd role is unresolved; the Toll and Eiger-JNK roles are better supported.
- Antiviral autophagy against RVFV, a response the same study shows is triggered by Toll-7 [PMID:24374193 "Traf6 mutants showed impaired autophagy
  activation during RVFV infection as assessed by Atg8 immunoblot"].
- Notch: negative regulator with Deltex/Kurtz (PMID:25280943, abstract-only).

## LPS sensing does not exist in the fly pathways

- Imd responds to DAP-type peptidoglycan, not LPS [PMID:15142531 "We found that highly purified LPS
  did not stimulate the IMD pathway."]; [PMID:12692550 "Gram-negative diaminopimelic acid-type
  peptidoglycan is the most potent inducer of the Imd pathway and that the Toll pathway is
  predominantly activated by Gram-positive lysine-type peptidoglycan."]. The fly genome has no
  TLR4/MD-2/CD14 LPS receptor system.

## PAINT nodes (PTHR10131, PANTHER 19 tree)

Path: PTN008938480 (root) > PTN000014919 (Eukaryota, SF94) > PTN000014921 (Unikonts) > PTN000014922
(Opisthokonts) > PTN000805648 (Metazoa-Choanoflagellida) > PTN008301857 (Eumetazoa DUPLICATION:
TRAF3/5, TRAF4, TRAF6, TRAF1/2 and other clades) > PTN008494376 (Eumetazoa TRAF6 orthologs, SF152) >
PTN008494377 (Bilateria) > PTN008494381 (Arthropoda) > PTN002562182 (Endopterygota) > PTN000015136
(Diptera) > fly leaf. Fly Traf4 sits in the TRAF4 clade and Traf-like in the TRAF1/2 ("RE66324P",
SF138) clade.

- PTN008494376 (TRAF6 clade): cytoplasmic side of plasma membrane (seed mouse Traf6 only; BHF-UCL IDA
  PMID:20614026, HOIP in the CD40 signalling complex), glutamatergic synapse (mouse and rat Traf6; SynGO
  IDA/IMP PMID:28973854, TRAF6 K63-ubiquitination of the postsynaptic scaffold in hippocampal neurons),
  LPS-mediated signaling pathway (mouse Traf6 only; MGI IGI/IMP PMID:26458771, Tifab and TLR-TRAF6 in
  haematopoiesis), ubiquitin protein ligase activity and innate immune response (both seeded with fly
  Traf6). The only LPS loss (IRD) is on the tick leaf PTN000805675; none on insects.
- PTN008301857 (duplication node): signaling adaptor activity, seeded only by mouse Traf2 (MGI IDA
  PMID:8710854, I-TRAF). PAINT added losses on the fly Traf-like/insect TRAF1/2 clade (PTN007421972,
  Endopterygota), an ecdysozoan "putative" clade (PTN008494389) and two vertebrate nodes, but not on the
  TRAF6 clade, so Traf6 keeps the inheritance.
- PTN000805648: regulation of canonical NF-kappaB signal transduction (seeded with fly Traf6).
- PTN008938480 (root): cytoplasm.

## FlyBase description check

"TNF-receptor-associated factor 6 (Traf6) encodes a protein that belongs to a family of adaptor
proteins involved in transducing downstream signaling by interacting with cell surface receptors. It
mediates the pro-inflammatory effects of Toll and related receptor signaling, and the cell death induced
by JNK activation via the product of egr."

- Adaptor binding cell-surface receptors: Wengen and Grnd binding (PMID:12894227, PMID:25874673).
- Toll signalling: PMID:11447260, PMID:14585960; antiviral autophagy, a Toll-7-triggered response (PMID:24374193).
  "Pro-inflammatory" is mammalian wording; in the fly the outputs are antimicrobial peptide induction
  and antiviral autophagy.
- Egr-induced JNK-dependent cell death: PMID:17765686, PMID:24162658, PMID:25874673.
- Nothing wrong. Missing: E3 ligase/K63 ubiquitination with Bendless and dUev1a, Notch regulation, the
  disputed Imd role.

## UniProt

Q9W3I9 is an unreviewed entry with no FUNCTION comment (expected for TrEMBL); its cytoplasm location
and keywords come from ARBA.
