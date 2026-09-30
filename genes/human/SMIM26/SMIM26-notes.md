# SMIM26 review notes

## Identity and why this gene is interesting

SMIM26 (HGNC:43430, UniProt A0A096LP01) is a 95-amino-acid microprotein. Its locus was
originally annotated as the long non-coding RNA **LINC00493** (still the HGNC *previous*
symbol), so this is a reannotated lncRNA that turned out to encode a protein. UniProt
records a single predicted transmembrane helix (residues 13-35) and calls it a
single-pass mitochondrial outer membrane protein. Two isoforms are recorded
(A0A096LP01-1 and -2); isoform 2 simply lacks residue 40 (VSP_062288) and no
isoform-specific function has been reported, so none of the annotations below are
isoform-scoped.

Translation of the LINC00493 ORF and mitochondrial localisation of its product were
established first: [PMID:33386847 "While proteomic analysis revealed that the LINC00493
peptide interacts with many mitochondrial proteins, immunofluorescence assays showed that
its peptide is mitochondrially localized."]

## Three papers, three interactomes

**2023, EMBO Rep (ccRCC).** SMIM26 binds AGK and SLC25A11:
[PMID:37009826 "SMIM26, but not LINC00493, suppresses ccRCC growth and metastatic lung
colonization by interacting with acylglycerol kinase (AGK) and glutathione transport
regulator SLC25A11 via its N-terminus."] and
[PMID:37009826 "Moreover, the formation of the SMIM26-AGK-SCL25A11 complex maintains
mitochondrial glutathione import and respiratory efficiency, which is abrogated by AGK
overexpression or SLC25A11 knockdown."]
Both partners are inner-membrane-associated: SLC25A11 is the mitochondrial
2-oxoglutarate/malate carrier of the inner membrane, and AGK (UniProt Q53H12) is a
**lipid** kinase (EC 2.7.1.94/2.7.1.107) that is also a subunit of the TIM22 inner-membrane
translocase. This matters for GOA: SMIM26 carries `GO:0019901 protein kinase binding` with
AGK as the WITH/FROM partner, but AGK is not a protein kinase.

**2025, Mol Cell (one-carbon metabolism).** A different interactome — sideroflexins and
the mitoribosome:
[PMID:40578345 "SMIM26 interacts with mitochondrial serine transporters SFXN1/2 and the
mitoribosome, forming a functional triad that facilitates translation of the complex I
subunit mt-ND5."] with the loss-of-function phenotype
[PMID:40578345 "SMIM26 deletion is embryonic lethal in mice and impedes tumor growth in a
xenograft model of folate-dependent acute myeloid leukemia."]
This is the paper behind GOA's `GO:0005743 mitochondrial inner membrane` (IDA) and
`GO:0140978 mitochondrial large ribosomal subunit binding` (IDA).

**2026, Genes Dev (respiratory chain).** A third interactome, and an explicit topology:
[PMID:41991342 "In biochemical and single-molecule tracking studies, we found that SMIM26
interacts with VDAC1/2 in the outer mitochondrial membrane and with SLC25A6 in the inner
mitochondrial membrane."], [PMID:41991342 "It spans the intermembrane space and is
phosphorylated at distinct residues."],
[PMID:41991342 "Knockout cells are viable, but respiratory chain activity is strongly
reduced."], [PMID:41991342 "Interestingly, knockout mice are not viable and die at early
developmental stages."], and the summary claim
[PMID:41991342 "Our work suggests that SMIM26 coordinates metabolite transport through the
inner and outer mitochondrial membranes and is essential for respiratory chain function in
vivo."]

SLC25A6 is ADP/ATP translocase 3 (ANT3), the inner-membrane adenine nucleotide carrier —
see this repository's `genes/human/SLC25A6` review, which describes it as an
alternating-access ADP/ATP antiporter of the inner membrane. An OMM-anchored protein
reaching SLC25A6 must do so from the intermembrane-space face, which is exactly what the
Genes Dev topology asserts.

## The tension GOA now carries

GOA holds, all as IDA/IPI on the same 95-residue protein:

- `GO:0005741` mitochondrial **outer** membrane (three independent papers)
- `GO:0005743` mitochondrial **inner** membrane (one paper)
- `GO:0030674` protein-macromolecule adaptor activity (two papers)
- `GO:0044325` transmembrane transporter binding (three papers, four different partners:
  SLC25A11, SFXN1, SLC25A6, VDAC1)
- `GO:0140978` mitochondrial **large ribosomal subunit** binding (one paper)

The adaptor and transporter-binding calls are mutually reinforcing: every paper finds
SMIM26 bridging metabolite carriers, and the partner set differs between papers rather than
contradicting between them. A microprotein with one TM helix and ~60 residues of soluble
sequence is a plausible tether for several carriers, and different cell backgrounds and
baits will pull out different ones.

**The mitoribosome claim is the one that does not sit comfortably.** The mitochondrial large
ribosomal subunit is on the **matrix** face of the inner membrane. A single-pass protein
anchored in the outer membrane and spanning the intermembrane space cannot reach it. Either

1. there is a second, inner-membrane-integral pool of SMIM26 whose soluble portion faces the
   matrix (which would also explain the `GO:0005743` IDA), or
2. the mitoribosome association is indirect — captured through SFXN1/2 or through the
   co-translational insertion machinery — and the direct-binding reading of `GO:0140978` is
   too strong.

I cannot distinguish these from the abstracts available (both PMID:40578345 and
PMID:41991342 are abstract-only in this repository's cache). Per project rules an IDA is not
overruled from an abstract, so `GO:0005743` and `GO:0140978` are marked **UNDECIDED** rather
than removed or demoted, with the topological objection recorded. These two annotations
stand or fall together; they are the two claims of the inner-membrane/mitoribosome model.

## Curation position taken

- `GO:0030674` protein-macromolecule adaptor activity → **core**. Two independent IDA
  papers, and it is the one molecular description all three papers agree on.
- `GO:0044325` transmembrane transporter binding → **ACCEPT**, core-adjacent. It is an
  informative binding term (unlike bare protein binding) and names the actual mechanism.
- `GO:0005741` mitochondrial outer membrane → **ACCEPT** (core location, three papers).
- `GO:0005739` mitochondrion → **ACCEPT** but less informative than the membrane terms.
- `GO:0005743` mitochondrial inner membrane and `GO:0140978` mitochondrial large ribosomal
  subunit binding → **UNDECIDED** (see above).
- `GO:0019901` protein kinase binding → **MODIFY** to `GO:0019900` kinase binding. The
  interaction with AGK is real, but AGK is a lipid kinase, not a protein kinase.
- `GO:0005515` protein binding → **MARK_AS_OVER_ANNOTATED** per project guidance.

## Proposed additions (reviewer proposals, single-source)

- `GO:0005758` mitochondrial intermembrane space as a location, from the explicit
  IMS-spanning topology in PMID:41991342.
- No molecular function is proposed beyond the adaptor term. SMIM26 has no catalytic or
  transport activity of its own; what it does is hold carriers together.

## Open questions

- Is there an inner-membrane pool of SMIM26, and if so what is its topology? This is the
  single question that would reconcile the two 2025/2026 models.
- Are the reported partner sets (AGK/SLC25A11; SFXN1/2 + mitoribosome; VDAC1/2 + SLC25A6)
  alternative states of one bridging complex, or cell-type-specific interactomes?
- What do the reported phosphorylation sites do? PMID:41991342 reports phosphorylation at
  distinct residues but the abstract does not assign a function to them.
