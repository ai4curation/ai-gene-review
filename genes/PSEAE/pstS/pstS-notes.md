# pstS (PA5369, G3XDA8) review notes

## Two locations, two functions, and they are genuinely separable

PstS looks at first like a gene with contradictory location annotations — `GO:0042597` periplasmic
space by IDA and `GO:0005576` extracellular region by EXP. It is not a contradiction. The protein
is in both places, by two routes, doing two things, and the literature separates them cleanly.

**Periplasmic, as the binding component of the Pst phosphate importer.** The 1984 characterisation
purified it from osmotic-shock fluid, which is the periplasmic fraction:
[PMID:6436026 "A binding protein for inorganic phosphate was purified to apparent homogeneity from
the shock fluids of phosphate-limited Pseudomonas aeruginosa."] It binds one phosphate with
sub-micromolar affinity [PMID:6436026 "The purified protein bound one molecule of phosphate per
molecule of binding protein with an average Kd of 0.34 microM."], is specific for inorganic over
organic phosphates, and its loss removes the high-affinity uptake system
[PMID:6436026 "Mutants lacking the phosphate-binding protein were isolated and shown to be
deficient in phosphate transport compared with wild-type cells."].

**Surface-exposed, exported by a second secretion system.** A later study found PstS on the outside
of the cell, in appendages, under the same phosphate limitation that induces the transporter, and
identified the export route:
[PMID:18282104 "Formation of the PstS rich appendages was induced during phosphate limitation and
completely suppressed in phosphate-rich media."] and
[PMID:18282104 "significantly less outer surface PstS was observed in the MPAO1 mutant DeltaHxcR
thus establishing a role for the alternative type II secretion system Hxc in outer surface PstS
expression"].

## The surface location is annotated to the wrong term

GO's own term comments decide this, and they are unusually explicit:

- `GO:0009986` cell surface — "intended to annotate gene products that are **attached** (integrated
  or loosely bound) to the plasma membrane or cell wall."
- `GO:0005576` extracellular region — "intended to annotate gene products that are **not attached**
  to the cell surface. For gene products at the cell surface, consider a[nother term]."

And the two are not parent and child: OLS confirms `GO:0005576` is not among `GO:0009986`'s
ancestors. They are alternatives, distinguished precisely by attachment.

What the paper reports is attached protein — "outer surface PstS", forming "appendages", reduced in
a secretion mutant. That is `GO:0009986`, not `GO:0005576`. So both extracellular rows are
`MODIFY`, which is a lateral correction rather than a refinement.

## The biofilm row is the opposite case from pslB

Batch 6 marked `GO:0044010` single-species biofilm formation over-annotated on `pslB`, because the
paper behind it reported that the single mutant had **no** attachment defect. The same term on
`pstS` is among the best-supported rows in either batch, and the difference is worth stating
because the term and the evidence code are identical:

[PMID:25223609 "Structure-based experiments showed that PstS-mediated phosphate uptake and biofilm
formation are in fact two distinct functions. Specifically, a point mutation that abrogated
phosphate binding did not eliminate biofilm formation; conversely, truncation of the N' loop
diminished the ability of PA to form biofilms but had no effect on phosphate binding and uptake."]

That is a separation-of-function pair: one mutation kills binding and spares biofilm, the other
kills biofilm and spares binding. It does not merely show that the gene is needed for biofilm; it
shows the biofilm role is a property of a particular structural element — an unusual 15-residue
N-terminal loop extension identified crystallographically — and not a downstream consequence of
phosphate starvation. The project's own caution about biofilm phenotypes is about inferring
participation from a growth or attachment defect; this evidence is of a different kind.

## What is not claimed

The virulence findings in PMID:18282104 — adhesion to and barrier disruption of intestinal
epithelium, mortality in a surgical mouse model reversed by phosphate repletion — are not
annotated. They are host-interaction outcomes of a surface protein, several steps from anything
PstS does molecularly, and the project's rule on indirect and pleiotropic effects applies. Recorded
as a question instead.
