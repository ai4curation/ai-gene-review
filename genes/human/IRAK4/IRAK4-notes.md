# IRAK4 (human, Q9NWZ3) review notes

## Sources used

- UniProt Q9NWZ3 (`IRAK4-uniprot.txt`): 460 aa; N-terminal death domain (20-104), C-terminal
  protein kinase domain (186-454), active-site proton acceptor D311; Pelle subfamily of the TKL
  Ser/Thr kinases; EC 2.7.11.1; Mg2+ cofactor. Loss-of-function causes IMD67 (IRAK-4 deficiency).
- Cached GOA publications (all 26 GOA PMIDs present in `publications/`), and cached Reactome
  entries under `reactome/`.
- Deep research: `IRAK4-deep-research-falcon.md` (Falcon) arrived after the review was written;
  see the cross-check section below.

## Deep-research cross-check (2026-09-30)

Compared the Falcon report against every annotation decision, the description and both core
functions.
- **Agreement:** active Ser/Thr kinase of the Myddosome; DD-mediated MyD88 recruitment then
  IRAK1/IRAK2 recruitment; separable kinase and scaffold roles; scaffold integrates MYD88 and TRIF
  at TRAF6 in TLR4 signalling (PMID:35977521, already cited); TLR3 is IRAK4-independent; IRAK4 is
  cytosolic/receptor-proximal and "not a transmembrane, extracellular, or constitutively nuclear
  protein" - consistent with REMOVE (extracellular region) and MARK_AS_OVER_ANNOTATED (nucleus).
  The falcon file is now cited as context on those two rows. No annotation action changed.
- **Additions (not verified in a cached primary paper, so no annotation change):**
  trans-autophosphorylation at T345/S346 as a Myddosome-maturation switch (Srikanth et al. 2024,
  bioRxiv preprint); IRAK1 T209 as the initiating IRAK4 site, with T387 possibly IRAK1
  autophosphorylation (secondary review); a MyD88-independent IRAK4-IRAK1 pathway after DNA
  double-strand breaks (Li et al. 2023, not fetched). Raised as a suggested question.
- **Nuance:** the report states kinase activity is essential for MyD88 signalling largely from
  mouse Irak4 kinase-dead data; the review already records that human macrophages/fibroblasts
  are partly kinase-independent [PMID:36865541]. No conflict requiring change.
- Changes: falcon file added to references and cited on GO:0005576 and GO:0005634 rows; one new
  suggested question.

## Core biology (with provenance)

- Discovery and kinase activity: IRAK4 is the closest human homolog of Drosophila Pelle
  [PMID:11960013 "IRAK-4 is the closest human homolog to Pelle."]. It phosphorylates IRAK1 in vitro
  [PMID:11960013 "Here we show that recombinant IRAK-1 is a substrate for IRAK-4, whereas IRAK-1 is
  not able to phosphorylate IRAK-4 in vitro"], on activation-loop sites
  [PMID:11960013 "T387 and S376 are the main sites of phosphorylation by both IRAK-1 and IRAK-4"].
  Unlike other IRAKs it needs its kinase activity to activate NF-kB in overexpression
  [PMID:11960013 "IRAK-4 depends on its kinase activity to activate NF-κB"].
- Additional substrates: Pellino E3 ligases [PMID:12860405 "Pellino2 is one of the first substrates
  identified for IRAK1 and IRAK4."; PMID:19264966 "The E3 ubiquitin ligase Pellino can be activated by
  phosphorylation in vitro, catalyzed by IL-1 receptor-associated kinase 1 (IRAK1) or IRAK4."];
  IRAK2 [PMID:36865541 "Following activation by IRAK4, IRAK2 is autophosphorylated on residues S136
  and T140"].
- Myddosome: IRAK4 death domain binds MyD88 death domains and in turn recruits IRAK2/IRAK1
  [PMID:20485341 "Assembly of this helical signalling tower is hierarchical, in which MyD88 recruits
  IRAK4 and the MyD88-IRAK4 complex recruits the IRAK4 substrates IRAK2 or the related IRAK1."].
  Disease/SNP variants in the IRAK4 DD abolish MyD88 binding [PMID:24316379]. Endogenous
  myddosomes in macrophages have IRAK4 and IRAK2 as core kinases [PMID:38961291 "The proteins in the
  myddosome core were the kinases IRAK2 and IRAK4"].
- Kinase vs scaffold: In mouse, kinase activity required for MyD88 signalling; the scaffold (not the
  kinase) is also required for TRAF6 activation downstream of both MYD88 and TRIF in TLR4 signalling
  [PMID:35977521]. In human cells the kinase is partly dispensable for cytokine output
  [PMID:36865541 "Interestingly, inhibition of IRAK4 kinase activity in human macrophages or
  fibroblasts does not impact cytokine production"]. Both roles are part of the core function.
- Human genetics: IRAK4-deficient cells fail to respond to TLR7/8/9 (IFN induction)
  [PMID:16286015 "The TLR-7-, TLR-8-, and TLR-9-dependent induction of IFN-alpha/beta and -lambda is
  strictly IRAK-4 dependent"], but respond to TLR3 (TRIF-only) agonists.
- Other: IRAK4 also mediates the MyD88-independent Unc5CL pathway [PMID:22158417]; contributes to
  non-transcriptional NLRP3 priming [PMID:36865541 "study of non-transcriptional priming of the NLRP3
  inflammasome revealed an additional role for IRAK4 and IRAK1"].

## Curation decisions and rationale

- Kinase MF: accept GO:0004674 (EXP, TAS, IEA); generic `protein kinase activity` and `kinase
  activity` MODIFY to GO:0004674 (the IDA paper shows Ser/Thr phosphorylation of IRAK1 peptides).
- Scaffold: IPI protein-binding rows with MyD88 and IRAK2 from the structural/biophysical papers
  (PMID:20485341, PMID:24316379) are MODIFIED to GO:0070513 death domain binding (DD-DD
  interactions are what those papers measure). High-throughput Y2H/variant screens and the
  Pellino/IRAK3/VSIG8/TRIM7/ZNF597/IL36RN rows are REMOVED as uninformative `protein binding`
  (the substrate relationship to Pellino is already captured by the kinase MF).
- Project question (Toll vs TLR): the IBA to GO:0008063 Toll signaling pathway (node
  PTN000701353, donors FlyBase tub FBgn0003882 and pll FBgn0010441) transfers a term defined by
  the Drosophila Toll receptor/Spaetzle to a vertebrate protein. GO:0008063 is not an ancestor of
  GO:0002224 (its parent is cell surface receptor signaling pathway; GO:0002224 sits under pattern
  recognition receptor signaling). MODIFY to GO:0002755 MyD88-dependent TLR signaling pathway,
  which is the vertebrate equivalent. The IBA to `plasma membrane` from the same node is kept as
  non-core (IRAK4 is peripheral, recruited to activated receptor complexes).
- GO:0038172 IL-33 signalling (IDA, PMID:11960013): the full text studies IL-1 in 293RI cells
  and never mentions IL-33/ST2 (IL-33 was described after 2002). MODIFY to GO:0070498 IL-1
  mediated signaling; IL-33 signalling through IRAK4 is biologically plausible but is not what
  this paper shows.
- `cell surface` (IDA, PMID:22851693): IRAK4 is a cytosolic protein recruited to the cytoplasmic
  face of the IL-1R complex; the paper describes membrane-associated complex I. Results section not
  in cache. MODIFY to GO:0031234 extrinsic component of cytoplasmic side of plasma membrane.
- NLRP3 inflammasome complex assembly (NAS): IRAK4 acts in priming, it does not assemble the
  inflammasome; MODIFY to GO:1900227 positive regulation of NLRP3 inflammasome complex assembly.
- Ensembl Compara IEA from rat (extracellular region, positive regulation of smooth muscle cell
  proliferation): REMOVE. IRAK4 has no signal peptide and is intracellular; the SMC-proliferation
  claim is an indirect downstream phenotype.
- IL-1 receptor binding (IEA from mouse Irak4): IRAK4 is recruited through MyD88, not by direct
  receptor binding; MARK_AS_OVER_ANNOTATED.
- Nucleus IBA (PTN000784925; donors IRAK1, IRAK3, Pelle relatives, plant kinases): no IRAK4-specific
  nuclear evidence; UniProt says cytoplasm. MARK_AS_OVER_ANNOTATED.
- Neutrophil migration / neutrophil mediated immunity (IMP, PMID:19663824, abstract not available):
  kept as non-core; phenotype of patient cells downstream of TLR/IL-1R signalling.

## Paralog consistency (IRAK3)

IRAK3 (genes/human/IRAK3) is a pseudokinase; its kinase annotations are an IRAK-family
propagation issue. IRAK4 is the catalytically active apical kinase (canonical catalytic motifs
conserved in IRAK1 and IRAK4 but not IRAK2/IRAK3 [PMID:33238146 "the canonical kinase active site
motifs are conserved in the catalytically active family members, IRAK1 and IRAK4, but not in the
pseudokinases IRAK2 and IRAK3"]), so kinase terms are accepted here. Note for IRAK3's review
(not edited): the IRAK3 review keeps several UNDECIDED rows on magnesium ion binding etc.; not
changed here.
