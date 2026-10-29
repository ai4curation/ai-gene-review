# casC (Cas7 / Cse4), *Escherichia coli* K-12 — UniProt Q46899

Curation journal. All assertions carry inline provenance as
`[PMID:xxxxxxx "verbatim supporting text"]`, copied verbatim from the cached records in
`publications/`.

## Session 1 (2026-10-01): initial full review

Reviewed together with casA, casB, casD and casE as one complex.

### What CasC is

CasC is the Cas7 backbone subunit and the only one present in six copies
[PMID:25103409 "The backbone of Cascade is composed of six Cas7 proteins that oligomerize along the crRNA forming an interwoven architecture that presents the crRNA-guide sequence in six discrete segments"].
UniProt Q46899 SUBUNIT: "The 6 CasC subunits make a helical stack forming a groove in
which the crRNA lies. Interacts directly with all of the Cas subunits."

Its fold is a modified RRM "palm" with a "fingers" domain and a 30-residue "thumb"
loop, and the oligomer is built thumb-into-palm
[PMID:25103409 "The thumb of each Cas7 protein folds over the top of the crRNA and fits into a positively charged crease on the palm of the adjacent Cas7 protein"].
Critically for how this subunit should be annotated, the crRNA contacts are *not*
sequence specific
[PMID:25103409 "Unlike Cas6e and Cas5e, which make sequence-specific interactions with portions of the CRISPR repeat sequence, the Cas7 proteins polymerize along the crRNA via non-sequence specific interactions"],
and the resulting architecture has two jobs at once
[PMID:25103409 "This assembly creates an interwoven architecture that simultaneously protects the crRNA from degradation by cellular nucleases, while presenting a series of 5-nts segments for complementary base pairing to a target."].

### The structural-subunit problem

CasC is the clearest case in the complex where the only GOA molecular-function rows are
`RNA binding` and `protein binding`, and where neither captures what the protein does.
My reading is that CasC has three separable, honestly assertable activities:

1. **structural constituent of the complex** (GO:0005198 structural molecule activity) —
   it *is* the backbone; it polymerises, kinks the guide at a fixed 6-nt periodicity, and
   shields it from cellular nucleases. The quotes above support this directly, and the
   same sentence confirms it is the oligomerisation that creates the architecture. GO has
   no child of GO:0005198 for a non-ribosomal ribonucleoprotein (the children are
   ribosome, proteasome, virion, chromatin, nuclear pore and so on), so the parent is the
   correct level. I use the same term for the equivalent intra-complex `protein binding`
   rows on casA, casB, casD and casE.
2. **non-sequence-specific crRNA binding** (GO:0003723 RNA binding) — already in GOA, and
   correct at the parent level precisely because it is non-specific.
3. **DNA/RNA hybrid binding** (GO:0071667) — already in GOA, and well supported
   [PMID:25123481 "fingers from the adjacent Cas7 subunit (residues 109-111 and 163-169) contact both strands of the hybrid across the minor groove"],
   with the hybrid being stabilised by exactly this network
   [PMID:25123481 "A highly interdigitated network of protein-nucleic acid interactions stabilizes the ribbon conformation of the guide-target hybrid"].

I did not invent a term for crRNA-guided target recognition; that gap is recorded in
`modules/crispr_cas_adaptive_immunity.yaml` and raised in `suggested_questions`.

### The Cas1 (YgbT) interaction — kept, but marked non-core

GOA holds a `GO:0005515` IPI row for CasC with UniProtKB:Q46896 (Cas1/YgbT), plus a
`part_of GO:0032991` IDA row, both from the Babu dual-function paper. The interaction is
real and was validated in both directions
[PMID:21219465 "we reproducibly detected two subunits of the CRISPR-associated Cascade complex, YgcJ (CasC) and YgcH (CasE)"],
[PMID:21219465 "In each case, mass spectrometry analyses of the affinity-purified protein confirmed its association with YgbT"],
and the authors themselves frame its significance as speculative
[PMID:21219465 "The physical interaction between YgbT and two components of the Cascade complex (Cse4/CasC and Cse3/CasE) reported in this work also suggests that Cascade might contribute to the integration of new spacers in E. coli."].

How the two rows are handled:

- the `protein binding` row gets `REMOVE`. My first pass used `KEEP_AS_NON_CORE`, but
  validation flagged it: keeping a bare protein-binding row preserves an annotation with
  no functional content, and the repo convention for GO:0005515 rows with no
  evidence-backed replacement is REMOVE. Unlike CasC's intra-Cascade contacts, this
  association is not a structural contribution to any defined complex, so GO:0005198
  would be wrong, and no functional consequence has been demonstrated for CasC (the
  inhibition assay in that paper used CasE, not CasC), so there is no replacement term
  to propose. The removal is about the term's emptiness, not about doubting the
  observation, and the reason field says so explicitly. The interaction belongs in
  IntAct/ComplexPortal.
- the `part_of GO:0032991` row gets `MODIFY` to GO:1990904, the same as the
  structure-derived row. I first split these two rows (ACCEPT here, MODIFY there) on the
  grounds that the Babu assembly is an ill-defined Cas1-CasC/CasE association rather than
  Cascade, but validation flagged the inconsistency and re-reading the sentence settled
  it the other way: the paper itself identifies CasC as a subunit *of Cascade*
  ("two subunits of the CRISPR-associated Cascade complex"), so both rows are about the
  same, RNA-containing complex and should be treated identically.

### Requirement for immunity, and non-requirement for processing

CasC is required for phage resistance
[PMID:18703739 "The phage resistance phenotype was lost when Cascade was omitted"],
but like CasA and CasB it is not required for crRNA maturation — crRNA over-accumulates
in its absence
[PMID:18703739 "The same product was present in much higher amounts in the casA, casB, and casC knockout strains but absent from strains lacking the overlapping genes casD and casE"].
Accordingly CasC gets no crRNA-biogenesis process term.

### Complex term

Same decision as the other subunits for the Cascade-derived row: Cascade is demonstrably
a ribonucleoprotein
[PMID:25103409 "both assemblies consist of 11 protein subunits and a single 61-nt crRNA that traverses the length of the complex"],
[PMID:23079036 "The E. coli Cascade complex is a 405 KDa ribonucleoprotein complex assembled from crRNA and five functionally essential Cse proteins"],
so GO:0032991 is MODIFYed to GO:1990904 ribonucleoprotein complex, and the absent
CRISPR-specific CC term is proposed. ComplexPortal does model the complex (CPX-1005,
cross-referenced from Q46899); GO does not.
