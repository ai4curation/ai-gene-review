# FbpA (Q50964), *Neisseria gonorrhoeae* — review notes

## Why this gene is in scope

Grounded from the CMMMech critical-minerals corpus: `data/records/hafnium.yaml`
lists `UniProtKB:Q50964` as a protein example for a hafnium record, because
purified *N. gonorrhoeae* ferric ion-binding protein (nFbp/FbpA) binds
multinuclear oxo-Hf(IV) clusters in its interdomain cleft
[PMID:12598891 "We show that the ferric ion-binding protein from Neisseria gonorrhoeae (nFbp) readily binds
clusters of Fe3+, Ti4+, Zr4+ or Hf4+ in solution."].

## Identity

- UniProtKB `Q50964` (TrEMBL, unreviewed), 331 aa precursor, `Q50964_NEIGO`,
  gene `fbpA`, strain F62 sequence `AAB63559.1`.
- Protein existence `PE 1: Evidence at protein level`; two PDB entries,
  `1D9Y` (2.20 Å, Fe(3+) complex) and `1O7T` (1.65 Å, the Hf-cluster structure).
- Despite PE 1 and an extensive primary literature the entry has **no curated
  `CC -!- FUNCTION`** and only two IEA GO rows. Its only `CC` line is an
  ARBA-only similarity statement, which the repo rules forbid citing as support.
  The protein names are all submitter-derived (`ECO:0000313|EMBL:...`), so they
  are labels, not evidence.
- Signal peptide 1–22 (SignalP), chain 23–331. **Numbering caution:** the
  literature numbers the mature protein, UniProt numbers the precursor. The
  iron ligands His9, Glu57, Tyr195, Tyr196 of the papers are
  His31, Glu79, Tyr217, Tyr218 in `fbpA-uniprot.txt` — the four `FT BINDING`
  residues with `ECO:0007829|PDB:1D9Y` evidence. Offset is exactly +22.

## Function

FbpA is the periplasmic solute-binding protein of the FbpABC ABC importer. In
the gonococcus, iron stripped from host transferrin/lactoferrin at the outer
membrane by TbpAB/LbpAB is handed to FbpA in the periplasm, which shuttles it
to the FbpB permease for FbpC-powered, ATP-dependent transport into the
cytosol.

- Periplasmic binding-protein role, pulse-chase:
  [PMID:7934822 "Predictive of a
periplasmic-binding protein, which functions in the high-affinity acquisition of
iron, is that Fbp is a transient participant in the process of iron acquisition
from human transferrin."]
- The operon and its architecture:
  [PMID:8606197 "The fpbABC operon composes an iron transport system
that is homologous to the sfu and hit operons previously reported for Serratia
marcescens and Haemophilus influenzae, respectively, and displays elements
characteristic of ATP binding cassette transporters."]
  (note the typo `fpbABC` in the source abstract — quoted verbatim).
- Periplasm-to-cytosol direction is in that paper's title
  [PMID:8606197 "The fbpABC locus of Neisseria gonorrhoeae functions in the periplasm-to-cytosol
transport of iron."]
- Conditional-expression mutants in strain FA19 show the operon is required for
  iron acquisition, here from catecholate xenosiderophores:
  [PMID:21041493 "We determined that expression of FbpABC was required for growth of
gonococcal strain FA19 in the presence of enterobactin and salmochelin."], and
  [PMID:21041493 "The fbpABC operon encodes a periplasmic-binding-protein-dependent ABC transport system that enables the gonococcus to transport iron into the cell subsequent to outer membrane translocation."]

## Iron binding and the synergistic anion

FbpA is a structural and functional analogue of a single transferrin lobe —
"bacterial transferrin":

- [PMID:7947682 "Fbp reversibly binds a single ferric ion per molecule of protein with
high affinity."]
- Ligand set and the synergistic anion requirement:
  [PMID:7947682 "Chemical modification of purified Fbp in the presence and
absence of iron using the Tyr-specific modifier tetranitromethane demonstrates
that between two and three Tyr residues are implicated in iron binding."] and
  [PMID:7947682 "In addition, like the transferrins, a bicarbonate anion is required for the
efficient coordination of iron by Fbp."]
- The physiological synergistic anion is phosphate, but FbpA is anion-promiscuous;
  the anion sets both affinity and redox potential, i.e. it gates release:
  [PMID:17630737 "The sequestration of iron by FbpA is facilitated by the presence of a
synergistic anion, such as phosphate or sulfate."],
  [PMID:17630737 "The iron affinity of the FeFbpA-SO4 protein assembly is 2 orders of magnitude lower than when bound with phosphate and is the lowest of any of the FeFbpA-X assemblies yet reported."]
- Release kinetics and the anion "gatekeeper":
  [PMID:16008346 "These results reaffirm the contribution of the
synergistic anion to the FbpA iron transport process as the anion, in addition
to playing a facilitative role in iron binding, appears to have a \"gatekeeper\"
role, thereby modulating the Fe(3+) release process."]
- Review framing: [PMID:21933698 "Here we establish that FbpA may be considered a bacterial
transferrin on structural and functional grounds."]

## Non-ferric metals (the CMMMech angle)

The di-tyrosyl motif at the bottom of the open cleft nucleates polynuclear
oxo-metal clusters of hard, highly charged cations:

- [PMID:12598891 "A di-tyrosyl cluster nucleation motif (Tyr195-Tyr196) is situated at the bottom of this cleft
and binds either a trinuclear oxo-Hf cluster, which is capped by phosphate, or a
pentanuclear cluster, which in turn can be capped with phosphate."]
- Cu(II) binds the same two tyrosines but as a dinuclear oxo-Cu2 centre:
  [PMID:23884152 "The crystal structure of recombinant Cu-NgFbpA at 2.1 Å
revealed that the oxo-Cu2 clusters (dinuclear centres) assembled in the iron
binding cleft and were bound to the two adjacent tyrosine residues (Y195 and
Y196) of the protein"]

**This is cell-free chemistry on purified protein.** No whole-cell Hf (or Zr,
Ti) uptake, no FbpABC-dependent transport of those metals, and no mutagenesis
of Tyr195/Tyr196 for the non-ferric metals has been reported. Nothing here
supports a GO annotation beyond iron: GO has no hafnium- or zirconium-binding
term, and the only non-redundant grouping term (`GO:0046914` transition metal
ion binding) is an ancestor of `GO:0008199` ferric iron binding, so proposing
it would add nothing. The cluster chemistry is therefore recorded here and in
`suggested_experiments`, not as an annotation.

## Notes on the CMMMech record (`data/records/hafnium.yaml`) — not edited

CMMMech is read-only for this work. Two things a future CMMMech curator may
want to check; neither is a GOA/UniProt/InterPro defect, so neither is recorded
as a `source_defect`:

1. **Resolution.** The record's protein-example evidence says "a 1.8-A crystal
   structure of an oxo-bridged multinuclear Hf cluster". The paper's abstract
   says 1.7 Å and both UniProt's `DR PDB` line and the PDB entry give **1.65 Å**
   for 1O7T. The 1.8 Å figure does not match any of the three.
2. **Residue numbering.** `Tyr195`/`Tyr196` is the mature-protein numbering used
   throughout the literature; readers going to UniProt Q50964 will find those
   residues at 217/218. Worth stating which sequence the numbers refer to.

The record's `functional_role` itself ("binds oxo-bridged polynuclear Hf(IV)
clusters (3-5 Hf atoms) within its interdomain metal-binding cleft **in vitro**")
is appropriately hedged and is supported by the cited structure; it does not
over-extrapolate to whole-cell hafnium handling, and the record's own evidence
notes say as much.

## Curation gaps (not knowledge gaps)

- Q50964 is a TrEMBL entry with no curated function, no curated subcellular
  location and no experimental GO annotation, although the protein has been
  characterised biochemically and structurally since 1990. The review adds
  `NEW` rows for ferric iron binding, iron import and ABC-importer complex
  membership rather than leaving them implicit.
- The *N. meningitidis* and *H. influenzae* (HitA) orthologues have their own
  literature that was not reviewed here.

## Review decisions

| Term | Evidence | Action | Why |
|---|---|---|---|
| GO:0030288 outer membrane-bounded periplasmic space | IEA (TreeGrafter, PTN002823921) | ACCEPT | Periplasmic location is the experimentally established one; the root-level phylogenetic row is right and is as precise as the compartment gets for a Gram-negative periplasmic protein. |
| GO:0055085 transmembrane transport | IEA (InterPro IPR006061) | MODIFY → GO:0034755 | True but uninformative: the substrate and direction are known. The replacement is an `is_a` descendant. |
| GO:0008199 ferric iron binding | NEW, IDA | — | 1D9Y Fe(3+) structure plus solution biochemistry. |
| GO:0033212 iron import into cell | NEW, IMP | — | Conditional *fbpABC* mutants; periplasm-to-cytosol transport. Not an ancestor or descendant of GO:0034755. |
| GO:0055052 ABC transporter complex, substrate-binding subunit-containing | NEW, IC | — | FbpA is the substrate-binding subunit of FbpABC; follows the `genes/ECOLI/pstS` precedent. |

Per the `genes/ECOLI/pstS` / `genes/ECOLI/pstC` precedent, the solute-binding
protein is not asserted to *enable* the primary active transporter activity:
`core_functions` carries `molecular_function: GO:0008199` for the binding
activity and `contributes_to_molecular_function: GO:0015091` for the
complex-level ferric iron transmembrane transporter activity.
