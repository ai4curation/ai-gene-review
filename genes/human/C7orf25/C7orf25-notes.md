# C7orf25 / PANAD review notes

## Identity

C7orf25 (HGNC:21703, UniProt Q9BPX7) is a 421-amino-acid protein of the UPF0415 family. It
is a genuine dark-genome entry: the symbol is still an open-reading-frame placeholder,
UniProt's recommended name is "UPF0415 protein C7orf25", Pharos classes it Tdark, and until
2026 GOA held exactly one molecular function annotation for it - bare `GO:0005515 protein
binding` from three high-throughput binary interactome screens - plus a Human Protein Atlas
nucleoplasm localisation.

HGNC has since registered the alias **PANAD** ("proliferation-associated NXF1 adaptor"),
citing PMID:42449115. UniProt has not yet adopted it (entry version 152, 10-JUN-2026, still
`Name=C7orf25` with no function block). Two isoforms are recorded, differing only in an
N-terminal extension in isoform 2 (VSP_047243); the residue numbering used in the functional
paper (R122/E125/G133/D139) is that of isoform 1, so the work is on the canonical form.

## What the 2026 paper shows

[PMID:42449115 "In an effort to identify novel NXF1 adaptors involved in hepatocellular
carcinoma (HCC) development, we discovered that C7orf25, a previously uncharacterized
protein named proliferation-associated NXF1 adaptor (PANAD), interacts with NXF1 in the
nucleus."]

The mechanism is specific and is the reason bare protein binding is inadequate here. NXF1 is
autoinhibited: its arginine-rich RNA-binding domain (RBD) folds back onto its NTF2-like
domain, and an adaptor must break that contact before NXF1 can hold mRNA stably. PANAD does
exactly this, and the interface is mapped to single residues on both sides:
[PMID:42449115 "Specifically, the R122/E125/G133/D139 residues of PANAD bound to the
Q20/K22/K23 residues in the RBD of NXF1."] and
[PMID:42449115 "In vitro binding and BiFC assays confirmed that PANAD directly attenuated
intramolecular RBD-NTF2L interactions in a binding-dependent manner."]

It also binds cargo directly, which is what makes this an adaptor rather than merely an
activator: [PMID:42449115 "Notably, RNA pulldown assays demonstrated that PANAD directly
interacted with target mRNAs such as CDK6."] The binding was mapped with purified GST-PANAD
to a defined region of the CDK6 3' UTR, and the authors state the dual mechanism explicitly:
[PMID:42449115 "These findings suggest that PANAD employs a dual regulatory mechanism: it
disrupts the intramolecular interaction of NXF1 to shift it to an active conformation while
simultaneously binding directly to target mRNAs to promote their recruitment to NXF1."]

The export consequence is selective rather than global:
[PMID:42449115 "The mRNAs whose nuclear export was impaired upon PANAD knockdown were highly
enriched in cell proliferation pathways."] and
[PMID:42449115 "We confirmed that the nuclear export of these nine mRNAs encoding
proliferation stimulators was decreased upon PANAD knockdown"] Knockdown of NXF1 itself
phenocopied the effect on those mRNAs, and NXF1 depletion abolished the PANAD effect, which
is the epistasis needed to say PANAD acts through NXF1.

Downstream: [PMID:42449115 "The results revealed that the G1 population increased upon PANAD
knockdown"], with the corresponding decrease on overexpression, and effects on colony
formation and xenograft growth.

Summary as the authors put it:
[PMID:42449115 "Our findings demonstrate that PANAD functions by directly interacting with
NXF1, disrupting the intramolecular interaction of NXF1 and facilitating the nuclear export
of target mRNAs."]

## Why bare protein binding is not adequate, and what replaces it

The three existing `GO:0005515` rows come from proteome-scale binary interaction screens and
carry no functional content on their own. One of them is worth a second look, though: the
partner in PMID:37219487 is **RANBP2/Nup358** (UniProtKB:P49792), the cytoplasmic-filament
nucleoporin at which NXF1-bound mRNP is remodelled on arrival. That is not evidence of the
adaptor function by itself - it is a motif-based screen hit - but it is at least consistent
with a protein that works in the NXF1 export pathway, and it was sitting unexploited in GOA.

The claimed molecular function is "NXF1 adaptor conferring mRNA-export selectivity". The GO
term whose definition matches is `GO:0030674` protein-macromolecule adaptor activity: "An
adaptor activity that brings together two or more macromolecules in contact... The adaptor
can bring together two proteins, or a protein and another macromolecule such as a lipid or a
nucleic acid." PANAD brings together a protein (NXF1) and a nucleic acid (the cargo mRNA),
which is the nucleic-acid clause of that definition almost verbatim. `GO:0003729` mRNA
binding is independently supported by the GST-PANAD RNA pulldown. `GO:0006406` mRNA export
from nucleus is the process.

The **selectivity** claim - that PANAD biases export towards proliferation-stimulating
transcripts rather than acting globally - is the part GO cannot express in a single term.
`core_functions` can carry it in two ways used here: `substrates` records the cargo class
(CHEBI:33699 messenger RNA), and the free-text `description` states which transcripts are
affected. There is no "export-cargo-selectivity" molecular function term and I am not
proposing one: the selectivity is a property of which mRNAs PANAD binds, and the right way
to capture it in GO would be an annotation extension naming the cargo, not a new MF term.

## Curation position taken

- All three `GO:0005515` protein binding rows -> **MARK_AS_OVER_ANNOTATED**.
- `GO:0005654` nucleoplasm (HPA, IDA) -> **ACCEPT**. Independently corroborated by the
  BiFC signal inside the lamin B1 boundary in PMID:42449115.
- Proposed as reviewer additions, all from one paper and flagged as such: `GO:0030674`
  protein-macromolecule adaptor activity (core MF), `GO:0003729` mRNA binding,
  `GO:0006406` mRNA export from nucleus (core BP), and `GO:1902808` positive regulation of
  cell cycle G1/S phase transition (downstream, non-core).

## What is not established

- This is a single paper from a single laboratory, and the function has not been reproduced
  elsewhere. Nothing in the older literature on C7orf25 anticipates it.
- The structural basis is inferred from mutagenesis and FRET, not from a structure. The
  authors say so themselves.
- Whether PANAD has a role outside proliferating and tumour cells is untested; the entire
  study is in hepatocellular carcinoma models.
- The UPF0415 family is otherwise uncharacterised, so there is no orthology-based support
  for or against the adaptor assignment. No PAINT/IBA annotation exists for this gene.
