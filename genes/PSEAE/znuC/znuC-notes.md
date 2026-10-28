# znuC (PA5500, Q9HT73) notes

## 2026-10-28 review (PseudoCAP IBA-seed worklist, rank 92)

No deep-research provider keys were available; literature gathered by PubMed
search and from the cached publications.

### Identity

- UniProt Q9HT73 (Swiss-Prot, PE 3 "Inferred from homology"), 269 aa,
  "Zinc import ATP-binding protein ZnuC", EC 7.2.2.20, annotated by HAMAP rule
  MF_01725 [file:PSEAE/znuC/znuC-uniprot.txt].
- ABC transporter superfamily, zinc importer family (TC 3.A.1.15.5); Pfam
  PF00005 ABC_tran, PROSITE PS51298 ZNUC, NCBIfam NF007090, CDD
  cd03235 ABC_Metallic_Cations, PANTHER PTHR42734:SF9. A Walker A ATP-binding
  site is curated at residues 38-45 [file:PSEAE/znuC/znuC-uniprot.txt].
- The complex is "composed of two ATP-binding proteins (ZnuC), two transmembrane
  proteins (ZnuB) and a solute-binding protein (ZnuA)", located at the cell
  inner membrane as a peripheral membrane protein
  [file:PSEAE/znuC/znuC-uniprot.txt]. So ZnuC is the energy-coupling subunit,
  not the permease, and the transport activity is a property of the complex.
- Note a locus-tag discrepancy that does not affect this review: the Swiss-Prot
  entry gives PA5500 for znuC, while Ellison et al. describe in-frame deletions
  of "40 to 223 (80%) of znuB (PA5500), and 38 to 226 (70%) of znuC (PA5501)"
  [PMID:24086521]. GOA/PseudoCAP annotate Q9HT73 (znuC) and Q9HT72 (znuB) with
  the same term from this paper, so both subunits carry the annotation either
  way.

### What PMID:24086521 (the seed reference) shows

- The paper's subject is the regulator: Np20/PA5499 is the *P. aeruginosa* Zur
  [PMID:24086521 "ZurPA is zinc responsive and represses transcription of both
  znuA and the zur-znuC-znuB operon in a zinc dependent manner"], shown by
  promoter fusions, real-time RT-PCR and EMSA with the zinc chelator TPEN.
- znuC is in that operon [PMID:24086521 "Using reverse transcription-PCR, we
  found that primers designed to span the intergenic regions between zur and the
  znuC homolog, as well as znuC and znuB homolog each generated a PCR product"].
- The evidence that touches znuC itself is a growth phenotype
  [PMID:24086521 "Putative znuA, znuB, and znuC genes are required for wild-type
  level growth in low zinc conditions"], obtained in chelated medium
  [PMID:24086521 "the inability to express the putative znuA, znuB, or znuC
  genes resulted in decreased growth at 18 hours as compared wild-type strain
  PAO1 when the strains were grown in LB media supplemented with 0.5 mM EDTA"],
  with the deletions not causing a general growth defect in plain LB.
- The identification rests on sequence identity with the characterized E. coli
  system [PMID:24086521 "coli znuC (61% identity) and znuB (60% identity)"] and
  on the known architecture [PMID:24086521 "First identified in Escherichia
  coli, this ABC-type transport system is comprised of a zinc-binding
  periplasmic protein (ZnuA), an inner membrane permease (ZnuB), and an ATPase
  (ZnuC)"].
- So the paper supports znuC being required for growth under metal limitation,
  i.e. for zinc import. It does not show that ZnuC *responds* to zinc: the
  zinc-sensing step in this very paper is Zur's, and ZnuC is the thing Zur
  regulates.

### Related work

- D'Orazio et al. made a znuA mutant in PA14 and found that
  "this mutant strain displays a limited growth defect in zinc depleted media"
  and that "intracellular zinc content is not evidently affected by inactivation
  of the ZnuABC transporter", concluding that
  "P. aeruginosa is equipped with redundant mechanisms for the acquisition of
  zinc" while ZnuABC still matters for zinc-dependent virulence factors
  [PMID:25751674]. This is consistent with ZnuABC being a high-affinity zinc
  importer whose loss is partially buffered, and it is a reason to keep the
  annotation at the level of zinc import rather than of organism-level zinc
  homeostasis phenotypes.

### PAINT node (znuC-bioinformatics/RESULTS.md)

PTN001952271 is a Gammaproteobacteria speciation node of PTHR42734
(PTHR42734:SF9), 7 leaves in 7 organisms: znuC of *Haemophilus influenzae*,
*Vibrio cholerae*, *Salmonella* Typhimurium, *Yersinia pestis*, *E. coli* and
*P. aeruginosa*, plus one *Nematostella* ABC-domain fragment. The clade is
tight: all the bacterial leaves are named ZnuC. The node's GO:0010043 IBD is
sole-seeded by this gene's PseudoCAP IMP row, and GOA holds 1455 rows with this
node in with/from (7 GO_Central reference leaves and 1448 TreeGrafter), so the
term is propagated very widely.

### Annotation decisions

- GO:0010043 response to zinc ion (IBA, IMP): MODIFY to GO:0071578 zinc ion
  import across plasma membrane. The phenotype is a zinc-limitation growth
  defect of an importer subunit; the sensing/response in this system is Zur's
  job. Defects filed to PSEUDOCAP (the seed row) and GO_CENTRAL (the node).
- GO:0015633 ABC-type zinc transporter activity (IEA from EC): ACCEPT as the
  core activity, with a note that the activity is the complex's, so the
  qualifier should be contributes_to.
- GO:0043190 ABC transporter complex: ACCEPT. GO:0005886 plasma membrane:
  ACCEPT. GO:0005524 ATP binding and GO:0016887 ATP hydrolysis activity:
  ACCEPT (the subunit's own, curated Walker A site).
- GO:0042626 ATPase-coupled transmembrane transporter activity (IBA from the
  family root, donor BtuD) and GO:0055085 transmembrane transport and
  GO:0071577 zinc ion transmembrane transport: MODIFY to the specific supported
  terms (GO:0015633 and GO:0071578).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001952271 | GO:0010043 response to zinc ion | 1 (sole) | 7 GO_Central (1455 GOA rows incl. TreeGrafter) | GO:0010043, IMP, PMID:24086521 | INDIRECT-PHENOTYPE | The seed is the reduced growth of a znuC deletion in LB + 0.5 mM EDTA. That is sound evidence that ZnuC is required for zinc acquisition, but "response to zinc ion" describes a stimulus-response, and in this very paper the zinc-sensing component is Zur (Np20), which represses the zur-znuC-znuB operon; ZnuC is its target and the energy-coupling ATPase of the importer. The supported process term is zinc import across the plasma membrane (GO:0071578, under GO:0071577, already on the gene by IEA). The clade is right - all six bacterial leaves are ZnuC - so the node should carry the import term rather than the response term; it currently propagates to 1455 GOA rows. |
