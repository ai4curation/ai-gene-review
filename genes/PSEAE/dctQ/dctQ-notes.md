# dctQ (PA5168, Q9HU17) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE dctQ` (UniProt read timeouts on early
attempts; a re-run completed). Accession Q9HU17 matches the worklist (rank 49).
Swiss-Prot reviewed entry (DCTQ_PSEAE, PE 1). No deep-research provider was
used.

### Identity and literature

- DctQ is the small (4-TM) permease of the DctPQM TRAP transporter; Pfam PF04290
  DctQ; PANTHER PTHR35011 (official name "2,3-DIKETO-L-GULONATE TRAP TRANSPORTER
  SMALL PERMEASE PROTEIN YIAM"), subfamily SF2.
- The only primary paper is Valentini et al. 2011 (PMID:21725012), abstract only
  in the cache; PMC (PMC3165536) and Europe PMC returned no full text.
  - A Tn5 screen of a dctA mutant found the TRAP system [PMID:21725012 "Tn5
    insertion mutagenesis of the ΔdctA mutant led to the identification of a
    second Dct system, i.e., the DctPQM transporter belonging to the tripartite
    ATP-independent periplasmic (TRAP) family of carriers"].
  - [PMID:21725012 "The ΔdctA ΔdctPQM double mutant showed no growth on malate and
    fumarate and residual growth on succinate, suggesting that DctA and DctPQM are
    the only malate and fumarate transporters, whereas additional transporters for
    succinate are present."]
  - [PMID:21725012 "Competition experiments demonstrated that the DctPQM carrier
    was more efficient than the DctA carrier for the utilization of succinate at
    micromolar concentrations, whereas DctA was the major transporter at
    millimolar concentrations."]
- UniProt curated function, linked to the paper [file:PSEAE/dctQ/dctQ-uniprot.txt
  "FUNCTION: Part of the tripartite ATP-independent periplasmic (TRAP) transport
  system DctPQM involved in C4-dicarboxylates uptake."]

Evidence type: growth phenotypes of an operon deletion (in a dctA background) and
competition experiments. The readout is indirect (growth), but the perturbation
removes only transporters, and the substrates are specific. DctQ is part of the
TRAP translocator, so it does some of the transport work; the claim holds for
DctQ. The abstract does not say whether a dctQ-only mutant was tested.

### Clade check for PTN002169725 (cached PAINT leaf GAF; QuickGO 2026-10-28)

24 leaves in 11 taxa: E. coli YiaM (P37674) and Salmonella YiaM; Haemophilus
HI_0051 and HI_1030; nine or more Bradyrhizobium japonicum paralogs; Geobacter
GSU2056; Dictyoglomus Dtur_1773; Yersinia YPO1578; P. aeruginosa DctQ. The node
also carries a YiaM-seeded GO:0022857 IBD. E. coli YiaM has experimental
annotations for carbohydrate transmembrane transporter activity and
2,3-diketo-L-gulonate transport (EcoCyc IDA, PMID:16385129), not a
C4-dicarboxylate. TRAP substrate specificity is set by the DctP-type binding
protein. So the C4-dicarboxylate IBD, seeded only by DctQ, is over-specific for
this clade and wrongly propagated to YiaM and to the many uncharacterised
paralogs.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002169725 | GO:0015740 C4-dicarboxylate transport | 1 (sole) | 24 (11 taxa) | GO:0015740, IMP, PMID:21725012 (PseudoCAP) | OVER-SPECIFIC | The seed is sound for DctQ (dctA dctPQM double mutant cannot grow on malate or fumarate; DctPQM is the high-affinity succinate carrier). But the node is a YiaM-type TRAP small-permease clade (PANTHER named for YiaM) containing E. coli YiaM, whose characterised substrate is 2,3-diketo-L-gulonate, plus many paralogs of unknown substrate; in TRAP systems the binding protein sets the substrate. |

Defects filed: GO_CENTRAL WRONG_TERM (CHECK) for the PTN002169725 IBD on the IBA
row. No PSEUDOCAP defect; the IMP row is correct, only refined to the specific
import terms.

## Decisions summary

- ACCEPT: plasma membrane (IBA, IEA, ISS).
- MODIFY: C4-dicarboxylate transport (IBA, IMP) and transmembrane transport
  (IEA) -> malate import across plasma membrane, succinate import across plasma
  membrane, fumarate transport (no fumarate import term exists);
  transmembrane transporter activity (IBA) -> C4-dicarboxylate transmembrane
  transporter activity.
- NEW: part_of tripartite ATP-independent periplasmic transporter complex (IC).
