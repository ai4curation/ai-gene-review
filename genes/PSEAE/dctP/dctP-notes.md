# dctP (PA5167, Q9HU18) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE dctP`. Accession Q9HU18 matches the worklist
(rank 88). Swiss-Prot reviewed entry DCTP_PSEAE (PE 1). No deep-research
provider was used. Reviewed for consistency with genes/PSEAE/dctQ (same
operon, same paper).

### Identity and literature

- DctP is the periplasmic binding protein of the DctPQM TRAP transporter;
  InterPro IPR004682 TRAP_DctP, NCBIfam TIGR00787 dctP, Pfam PF03480, PANTHER
  PTHR33376:SF7. Signal peptide 1-23 (predicted). A 1.30 A crystal structure of
  the mature protein is deposited (PDB 9DY3); I found no associated paper in
  PubMed.
- Valentini et al. 2011 (PMID:21725012; abstract only in the cache; full text
  not retrievable):
  - [PMID:21725012 "Tn5 insertion mutagenesis of the ΔdctA mutant led to the
    identification of a second Dct system, i.e., the DctPQM transporter belonging
    to the tripartite ATP-independent periplasmic (TRAP) family of carriers."]
  - [PMID:21725012 "The ΔdctA ΔdctPQM double mutant showed no growth on malate and
    fumarate and residual growth on succinate, suggesting that DctA and DctPQM are
    the only malate and fumarate transporters, whereas additional transporters for
    succinate are present."]
  - [PMID:21725012 "Competition experiments demonstrated that the DctPQM carrier
    was more efficient than the DctA carrier for the utilization of succinate at
    micromolar concentrations, whereas DctA was the major transporter at
    millimolar concentrations."]
- UniProt curated function [file:PSEAE/dctP/dctP-uniprot.txt "FUNCTION: Part of
  the tripartite ATP-independent periplasmic (TRAP) transport system DctPQM
  involved in C4-dicarboxylates uptake."]

Evidence: operon deletion in a dctA background plus competition experiments.
The readout is growth, but the perturbation removes only transporters, and the
substrates are specific. DctP as the TRAP binding protein does part of the
transport work. A dctP-only mutant is not mentioned in the abstract.

### Clade check for PTN002121312 (cached PAINT leaf GAF; QuickGO 2026-10-28)

9 leaves in 5 taxa: P. aeruginosa DctP (Q9HU18), PA0884 and PA4616;
Bradyrhizobium bll4430, bll6434, blr2749; Shewanella oneidensis DctP (Q8ECK4);
Vibrio cholerae DctP (Q9KQR9); Nematostella vectensis A7T6W2 ("response
regulatory domain-containing protein", probably a bacterial contaminant). No
leaf except DctP has experimental annotations in QuickGO. The classical
R. capsulatus DctP (P37735) is not among the leaves. Because the binding protein
determines TRAP substrate specificity, a C4-dicarboxylate term on a
binding-protein clade is better founded than on the permease clade of DctQ
(PTN002169725, YiaM-type). The caveat is within-genome paralogs (three in PAO1,
three in B. japonicum) whose substrates are unknown.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002121312 | GO:0015740 C4-dicarboxylate transport | 1 (sole) | 9 (5 taxa) | GO:0015740, IMP, PMID:21725012 (PseudoCAP) | SOUND | Seed is sound for DctP (dctA dctPQM double mutant cannot grow on malate or fumarate; DctPQM is the high-affinity succinate carrier). The node is a DctP-family binding-protein clade, the subunit that sets TRAP substrate specificity, and no leaf is characterised with a different substrate. Caveat: paralogs PA0884/PA4616 and three Bradyrhizobium paralogs are uncharacterised; one leaf is a probable contaminant in a cnidarian genome. |

Defects filed: none. The PseudoCAP IMP is correct, only refined to the
specific import terms.

## Decisions summary

- ACCEPT: outer membrane-bounded periplasmic space (IEA).
- MODIFY: C4-dicarboxylate transport (IBA, IMP) and transmembrane transport
  (IEA) -> malate import across plasma membrane, succinate import across plasma
  membrane, fumarate transport; periplasmic space (IEA, ISS) -> outer
  membrane-bounded periplasmic space.
- NEW: part_of tripartite ATP-independent periplasmic transporter complex (IC).
