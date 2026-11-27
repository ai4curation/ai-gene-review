# femA (PA1910, Q9I2J4) — review notes

Tier-3 PseudoCAP review. `femA` is the last unreviewed member of the `GO:0016987` /
PMID:18086184 shared claim — and it turns out not to belong to that claim at all.

## The finding: two experimental rows are swapped between femA and femI

PMID:18086184 (Llamas *et al.* 2008) characterises five cell-surface signalling systems.
Each such system has three parts:

`[PMID:18086184 "an outer membrane-localized TonB-dependent receptor (TonB-dependent transducer), a cytoplasmic membrane-localized antisigma factor and an extracytoplasmic function (ECF) sigma factor"]`

The abstract names the sigma factors and, separately, names this system's three genes:

- `[PMID:18086184 "the ECF sigmas PA0149, PA1912, PA2050, PA2093 and PA4896 have been overexpressed"]`
- `[PMID:18086184 "the PA1912-PA1911-PA1910 (designated FemI-FemR-FemA in this work) signalling system"]`

So in this paper's own nomenclature **PA1912 = FemI = the ECF sigma factor** and
**PA1910 = FemA = the TonB-dependent transducer**. Our `femA` is Q9I2J4 = PA1910, the
transducer. UniProt agrees: `Ferric-mycobactin receptor, FemA` for PA1910 and
`ECF sigma factor, FemI` for PA1912.

The GOA rows derived from this paper are exchanged between the two genes. QuickGO,
queried directly for femI (Q9I2J2) rather than taken from the worklist:

| row from PMID:18086184 | femA (PA1910, transducer) | femI (PA1912, sigma) |
|---|---|---|
| `GO:0016987` sigma factor activity | **IMP** | IEA, IBA only |
| `GO:0015344` siderophore uptake transmembrane transporter activity | IBA only | **IMP** |
| `GO:0005829` cytosol | **NAS** | — |
| `GO:0015891` siderophore transport | IMP | IMP |

The two molecular-function rows have changed places, and the cytosol statement went with
the sigma factor's function. In both genes the protein's *own* correct activity is left with
only electronic support — femA's transporter activity is IBA, femI's sigma activity is IEA
and IBA — while the experimental row each gene received describes the other one. That
pattern is the signature of a pair of rows entered against swapped accessions. The
`GO:0015891` process row, by contrast, is on both genes and is defensible on both, so the
exchange is confined to the MF rows and the NAS.

This is recorded at `confidence: CONFIRMED`. The project rule allows that where an abstract
defines the entity as another protein, and here the abstract assigns the loci explicitly;
the reciprocal row on the other gene is also one of the rule's listed confident cases. It
does not depend on reading the full text, and it does not depend on the PMID-proximity-style
reasoning used for the sox genes. Two independent checks agree: the paper's own locus
assignment, and femA's record.

## The record alone rules out sigma factor activity

femA is 804 residues and its record is unambiguous:

- `[file:PSEAE/femA/femA-uniprot.txt "Belongs to the TonB-dependent receptor family."]`
  — from PROSITE-ProRule `PRU01360` and `RuleBase:RU003357`, both curated UniRule systems.
- `[file:PSEAE/femA/femA-uniprot.txt "Cell outer membrane"]`,
  `[file:PSEAE/femA/femA-uniprot.txt "Multi-pass membrane protein"]`
- `[file:PSEAE/femA/femA-uniprot.txt "DR   Pfam; PF07715; Plug; 1."]` — the plug domain that
  occludes the β-barrel until a ligand is bound.
- `[file:PSEAE/femA/femA-uniprot.txt "DR   Pfam; PF07660; STN; 1."]` and
  `[file:PSEAE/femA/femA-uniprot.txt "DR   InterPro; IPR011662; Secretin/TonB_short_N."]` —
  the signalling domain that distinguishes a TonB-dependent **transducer** from a plain
  receptor. This is the domain that makes FemA the sensing component of the Fem system, and
  it is why the signalling-receptor and iron-regulation rows below are kept.
- `PE   1: Evidence at protein level`, with PDB structures `8S34` and `9EX3`.

An outer-membrane β-barrel with a plug and a periplasmic signalling domain is not a sigma
factor. ECF sigma factors are small cytoplasmic DNA-binding proteins, which is why femI
carries DNA binding and transcription-factor rows and femA carries none.

## Rows removed, and one row removed as a consequence

- `GO:0016987 sigma factor activity` (IMP) — removed; `WRONG_GENE_PRODUCT`, `REPOINT` to
  Q9I2J2.
- `GO:0005829 cytosol` (NAS) — removed, same defect. A multi-pass outer-membrane protein is
  not cytosolic; the compartment belongs to the sigma factor.
- `GO:2000142 regulation of DNA-templated transcription initiation` (IEA,
  `GO_REF:0000108`) — removed. Its `supporting_entities` is `GO:0016987` itself: it is
  computed from the sigma-factor row, so it falls with it. Recorded as an
  `OVER_PROPAGATION` consequence against GOA rather than as a second wrong-gene claim,
  because the pipeline did its job correctly on a wrong input.

## What is kept, and why the siderophore rows are not touched

The receptor identity is independently well supported and the IBA node is sound. Donors for
`PTN000793005` were resolved against the UniProt API rather than read from accessions, and
every one is an experimentally characterised TonB-dependent siderophore receptor: FhuA
(P06971) and FhuE (P16869) and Fiu (P75780) of *E. coli*, and FptA (P42512), FpvA (P48632),
foxA (Q9I116) and fiuA (Q9I648) of this organism. Two donors from the same species make this
a particularly well-grounded node.

`GO:0034756 regulation of iron ion transport` (IMP) is **kept**. It is tempting to read it as
part of the swap, since regulation sounds like the sigma factor's job, but the transducer
does part of that work: it binds the siderophore and transmits the signal inward, which is
what initiates the regulatory cascade. The paper's result for this system is about exactly
that — `[PMID:18086184 "is involved in the utilization of these heterologous siderophores"]` —
and the STN domain is the structural basis for it. This is why femA gets a second core
function for signalling rather than only the transport one.

`GO:0015343` is kept rather than marked too general. `GO:0015344`, accepted here, is its
child and adds the direction of transport, but `GO:0015343 siderophore-iron transmembrane
transporter activity` already names substrate and mechanism and is respectably specific on
its own, which the 2026-11-14 ruling says to keep. `GO:0019867 outer membrane` is a different
case and is marked `TOO_GENERAL`: it does not say *which* outer membrane, and `GO:0009279 cell
outer membrane` is its child (verified in OLS).

`GO:0015891 siderophore transport` and `GO:0033214 siderophore-iron import into cell` are
both kept. Checked in OLS: neither is an ancestor of the other, so they are not redundant.

## Consequence for the shared claim

The `GO:0016987` / PMID:18086184 group should have five members: PA0149, PA1912, PA2050,
PA2093 and PA4896 — the five ECF sigmas the abstract names. It currently reads PA0149,
PA2050, PA2093, PA4896 and **femA**, with PA1912 absent. Once the row is repointed the group
becomes the five sigmas the paper describes, and femA leaves it.

The four merged members all ACCEPT the term with the reason that "the ECF sigma domain
architecture is complete". femA fails precisely that test, which is a useful check on this
finding: the group's own stated criterion excludes the fifth member.
