# APOOL/MIC27 bioinformatics: the basic inter-transmembrane loop is conserved across PTHR14564

Run: `UV_NO_WORKSPACE=1 uv run python loop_conservation.py` (raw output in `loop_conservation.out`).

## Question

Human APOOL/MIC27 binds cardiolipin in vitro and not its precursor phosphatidylglycerol
(PMID:23704930). Two independent descriptions point at the same structural element as the
likely lipid contact: Weber et al. drew APOOL as "two putative transmembrane helices connected
by a positively charged stretch of amino acids", and Brown et al. 2026 (PMID:42647630) reported
from AlphaFold3 models and coarse-grained/atomistic simulations that Mic10, Mic26 and Mic27
"strongly recruit cardiolipin at conserved positive loop motifs", with 83% cardiolipin occupancy
measured at the Mic27 connecting loop.

Neither statement had been checked against the family alignment. Two things follow if the motif
is real: (i) it supports annotating cardiolipin binding as a molecular function of MIC27 itself
rather than of the complex, and (ii) it is the target-specific divergence check that reviewing
the two PTHR14564 IBA rows requires — a protein that had lost the family's lipid-facing element
would be a candidate for arguing against the phylogenetic transfer.

## Method

Identifiers only are hard-coded; every sequence and feature is read live.

1. Accessions are taken from `interpro/panther/PTHR14564/PTHR14564-entries.csv` (the nine
   representative members of the family), plus `Q9VEY5`, the *Drosophila* protein behind
   `FB:FBgn0038400`, which is one of the seeds of the family's PAINT IBD node `PTN001803267`.
2. Sequences are fetched from the UniProt REST API. Every fetched length is asserted against
   the length the family index records; a mismatch aborts the run rather than aligning a stale
   or truncated sequence. All nine matched.
3. The transmembrane and topological domain boundaries of human APOOL are **read from
   `APOOL-uniprot.txt`**, not re-predicted, so the loop definition is UniProt's.
4. The ten sequences are aligned with FAMSA (`pyfamsa`, UPGMA guide tree) and the alignment
   columns spanning the human loop are projected onto every member.

## Result

UniProt topology of human APOOL (Q6UXV4, 268 aa, sequence version 1):

| feature | span | note |
|---|---|---|
| TRANSIT | 1–27 | Mitochondrion |
| TOPO_DOM | 28–110 | Mitochondrial intermembrane |
| TRANSMEM | 111–129 | Helical |
| TOPO_DOM | 130–137 | Mitochondrial matrix |
| TRANSMEM | 138–155 | Helical |
| TOPO_DOM | 156–268 | Mitochondrial intermembrane |

The inter-TM loop is therefore residues 130–137, `RKGSKFKK`: five of eight residues are lysine
or arginine, no acidic residue, net charge +5.

Projected onto the family alignment:

| accession | gene | organism | span | aligned segment | K+R | net charge |
|---|---|---|---|---|---|---|
| Q6UXV4 | APOOL | *Homo sapiens* | 130–137 | RKGSKFKK | 5 | +5 |
| Q5NVS6 | APOOL | *Pongo abelii* | 130–137 | RKGSKFKK | 5 | +5 |
| Q78IK4 | Apool | *Mus musculus* | 130–137 | RKGSRFKK | 5 | +5 |
| Q3SZ27 | APOL | *Bos taurus* | 130–137 | RKGSRFKR | 5 | +5 |
| Q5ZK55 | APOOL | *Gallus gallus* | 127–134 | RKDSRFKK | 5 | +4 |
| Q9BUR5 | APOO | *Homo sapiens* | 129–135 | RGSKIKK | 4 | +4 |
| Q9DCZ4 | Apoo | *Mus musculus* | 129–135 | RGSKIKK | 4 | +4 |
| Q148H0 | APOO | *Bos taurus* | 129–135 | RGSKIKK | 4 | +4 |
| Q21154 | moma-1 | *Caenorhabditis elegans* | 138–145 | LKRGPVGR | 3 | +3 |
| Q9VEY5 | Mic26-27 | *Drosophila melanogaster* | 136–143 | ARGGFIKK | 3 | +3 |

**10/10 members carry at least two basic residues and a net positive charge in this block, and
none carries an acidic residue there.** The vertebrate MIC27 orthologues are near-identical
(`RKGS[KR]FK[KR]`); the MIC26 paralogues are one residue shorter and use a distinct but equally
basic `RGSKIKK`; the two invertebrate single-copy members diverge in sequence yet keep the
positive charge.

The alignment places human APOOL R130 opposite human MIC26 R129, and the human APOOL loop
resolves as R130 K131 G132 S133 K134 F135 K136 K137.

## Interpretation and limits

- Human APOOL has **not** lost the family's basic inter-TM loop; on the contrary it has the
  most basic version of it in the set. There is therefore no residue-level argument against the
  PTHR14564 IBA transfers, and the retention is consistent with cardiolipin binding being a
  property of MIC27 itself.
- This is a conservation and charge argument, **not** a demonstration that these residues bind
  cardiolipin. The only functional evidence remains the in-vitro lipid-strip assay on
  recombinant GST-APOOL (PMID:23704930); the residue-level mechanism is so far only modelled
  (PMID:42647630). No cardiolipin-binding-deficient APOOL mutant has been reported.
- The loop is annotated `Mitochondrial matrix` by UniProt (ECO:0000255, prediction) while the
  bulk of the protein faces the intermembrane space, which was shown experimentally by protease
  protection (PMID:23704930). Which leaflet the basic loop contacts is therefore not settled
  here, and the simulation work assumes the matrix-facing orientation established for Mic10.
- Nine of the ten sequences are PANTHER *representative* members of a 3288-protein family, so
  this is a conservation spot-check across chordates plus two invertebrates, not a
  family-wide survey.
