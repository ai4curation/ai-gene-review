# traD (F plasmid, *Escherichia coli* K-12) — curation notes

UniProt: P09130 (TRAD1_ECOLI), 717 aa, encoded on plasmid F and on plasmid
p1658/97. Inner membrane, with the location experimentally supported
(ECO:0000269|PubMed:9324263). UniProt states the role directly: "Couples the
transferosome to a type IV secretion system (T4SS). Probably forms a pore
through which single-stranded plasmid DNA is transferred to the secretion
system."

## Coupling protein: the role is well defined and the family is well named

TraD is the F plasmid's type IV coupling protein. The function is defined by
what the protein connects rather than by a reaction it catalyses: the
relaxosome, which processes the DNA at *oriT*, and the membrane-spanning
apparatus that translocates it. The naming and the family membership are set
out explicitly, with the counterparts in other systems named alongside
[PMID:9811665 "Proteins encoded by these genes, which are termed the TraG protein family, show significant similarities among their amino acid sequences and share transmembrane domains and sequence signatures for nucleoside triphosphate binding"].
That family contains TraG of RP4, TrwB of R388, TraD of F, and VirD4 of the
*Agrobacterium* T-DNA system, which is the correspondence
`modules/bacterial_type_iv_secretion_apparatus.yaml` uses when it grounds the
coupling-protein annoton on TraD and VirD4 together.

The C-terminal tail is the specificity determinant. Truncating it broadens the
range of relaxosomes TraD will serve while reducing transfer of F itself
[PMID:9811665 "The change in specificity was due to a loss of some amino acids in the carboxyl terminus of TraD that resulted in a broadening of the range of mobilizable relaxosomes at the expense of a decrease in the efficiency of F-plasmid transfer."].

## The relaxosome contact is structurally resolved

TraD binds the relaxosome component TraM. This was first shown in vitro
[PMID:9324263 "the affinity of TraM to TraD was studied in vitro by an overlay assay and by affinity chromatography."]
and later resolved crystallographically, with the TraD C-terminal peptide bound
in four symmetry-related grooves on a TraM tetramer
[PMID:18717787 "The structure reveals the TraD C-terminal peptide bound to each of four symmetry-related grooves on the surface of the TraM tetramer."].
The interaction is required in vivo, which is the evidence behind the existing
GOA conjugation annotation
[PMID:18717787 "Mutational analysis indicates that these interactions are specific and required for efficient F conjugation in vivo."].

The same paper describes TraD as "a hexameric ring ATPase that forms the
cytoplasmic face of the conjugative pore", and UniProt records that it "May
form a hexamer".

## ATP hydrolysis: grounded on the family, not on an F assay

No assay of ATP binding or hydrolysis by F TraD itself turned up. The activity
is nonetheless well established for the family through TrwB, the R388 coupling
protein (UniProt Q04230), which is the biochemically characterised member:

- Its structure is a hexamer with a central channel resembling ring helicases
  and F1-ATPase [PMID:11214325].
- It is a DNA-dependent ATPase
  [PMID:15919815 "In this work, we characterize a DNA-dependent ATPase activity for TrwBDeltaN70."],
  with the hexameric architecture established crystallographically
  [PMID:15919815 "TrwBDeltaN70 crystallographic structure revealed a hexamer with six equivalent subunits and a central channel."].
- TrwB is itself described as recruiting the relaxosome
  [PMID:11214325 "This large multimeric protein is responsible for recruiting the relaxosome DNA-protein complex"],
  the same role TraD plays for F, so the functional correspondence is not merely
  one of sequence.

So ATP hydrolysis is proposed here as ISS from Q04230 rather than as a
traceable author statement, which keeps the evidential basis explicit: the
activity belongs to a characterised family member, and TraD is inferred to share
it. This contrasts with F TraC in the same transfer region, where the
family-based ATPase inference is weaker and no molecular function is asserted at
all (see `genes/ECOLI/traC/traC-notes.md`).

## Note on the F system's internal nomenclature

Within the F transfer region, TraD is the VirD4 counterpart and TraC is the
VirB4 counterpart. On pKM101 the symbol TraB names the VirB4 counterpart. The
symbols are not portable between plasmids, and one GOA row has already been
attributed across that boundary (see `genes/ECOLI/traB/traB-notes.md`).

---

## Hierarchy check: GO:0044097 and GO:0009291 are not in the same subtree

Raised in PR review, since CLAUDE.md rejects a proposed term that is an ancestor
or descendant of one the gene already carries. Checked both directions against
the live ontology's ancestor closure over `is_a` and `part_of`:

- ancestors of `GO:0044097` (secretion by the type IV secretion system) do **not**
  contain `GO:0009291` (unidirectional conjugation);
- ancestors of `GO:0009291` do **not** contain `GO:0044097`.

So proposing the secretion term alongside the existing conjugation term adds
coverage rather than redundancy, and the mirror-image choice in
`genes/ECOLI/traB` of using `GO:0044097` in preference to `GO:0009291` is
likewise not a parent/child substitution. Both stand as written.
