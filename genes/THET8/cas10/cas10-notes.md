# Thermus thermophilus HB8 Cas10/Csm1 (Q53W19) — curation notes

## Identity and context

- UniProt Q53W19, reviewed (Swiss-Prot), 805 aa, locus TTHB147, encoded on plasmid
  pTT27. RecName: "CRISPR system single-strand-specific deoxyribonuclease Cas10/Csm1
  (subtype III-A)"; AltName "Cyclic oligoadenylate synthase".
- **No GOA annotations exist at all** (the `cas10-goa.tsv` file has a header and no
  rows). The entry is nonetheless a reviewed Swiss-Prot record with explicit FUNCTION,
  CATALYTIC ACTIVITY, DOMAIN and SUBUNIT blocks, so the absence of GO rows reflects an
  uncurated entry rather than unknown function.
- Domain architecture from UniProt FT lines: `REGION 1..99 HD domain` (ECO:0000305) and
  `DOMAIN 542..702 GGDEF` (PROSITE-ProRule:PRU00095). The GGDEF assignment is the
  InterPro/PROSITE read-out of the Palm/cyclase fold; it is *not* a diguanylate cyclase.

## The two separable activities of Cas10

Type III effectors are licensed by target RNA, not by target DNA, and target-RNA binding
switches on two chemically unrelated activities that sit in different domains of the same
protein:

[PMID:28663439 "The Cas10 subunit of the complex contains an HD nuclease domain that is
responsible for DNA degradation and two Palm domains with elusive functions."]

[PMID:31942067 "cOA activates defence enzymes with a CARF (CRISPR Associated Rossmann
Fold) domain"]

### (a) HD-domain single-strand-specific DNase

UniProt assigns this to Q53W19 by similarity to UniProtKB:B6YWB8, and the activating
logic by similarity to the S. thermophilus orthologue UniProtKB:A0A0A7HFE1:

> FUNCTION: This subunit is a single-strand-specific deoxyribonuclease (ssDNase) which
> digests both linear and circular ssDNA; it has both exo- and endonuclease activity.
> {ECO:0000250|UniProtKB:B6YWB8}

> FUNCTION: ssDNase activity is stimulated in the ternary Csm effector complex; binding
> of cognate target RNA activates the ssDNase, as the target RNA is degraded ssDNA
> activity decreases. {ECO:0000250|UniProtKB:A0A0A7HFE1}

The experimental grounding for that behaviour is in the *S. thermophilus* system, not in
Thermus — see `genes/STRTR/cas10/cas10-notes.md`:

[PMID:27105119 "ssDNase activity is confined to the HD-domain of Cas10"]

Because the protein has both endo- and exonuclease activity on single-stranded DNA, two
MF terms apply rather than one: GO:0000014 (single-stranded DNA endonuclease activity)
and GO:0008297 (single-stranded DNA exodeoxyribonuclease activity).

### (b) Palm/GGDEF-domain cyclic oligoadenylate synthase

[PMID:28663439 "target RNA binding by the Csm effector complex of Streptococcus
thermophilus triggers Cas10 to synthesize cyclic oligoadenylates"]

[PMID:28722012 "Upon target RNA binding by the interference complex, its Cas10 subunit
converts ATP into a cyclic oligoadenylate product, which allosterically activates Csm6
by binding to its CRISPR-associated Rossmann fold (CARF) domain."]

UniProt records the reaction for *this* entry with a Rhea cross-reference but an
inferential evidence code (ECO:0000305, i.e. curator inference from the two 2017 papers,
not a measurement on TtCas10):

> CATALYTIC ACTIVITY: Reaction=4 ATP = cyclic tetraadenylate + 4 diphosphate;
> Xref=Rhea:RHEA:58280 ... Evidence={ECO:0000305|PubMed:28663439,
> ECO:0000305|PubMed:28722012}

> FUNCTION: ... The active cOA in this bacteria is cyclic tetraadenylate (cA4),
> presumably made by this enzyme. {ECO:0000305|PubMed:28663439,
> ECO:0000305|PubMed:28722012}

**Organism discipline.** The cOA-synthesis assay in PMID:28663439 was done on the
*Streptococcus thermophilus* Csm complex, and the Thermus contribution of that paper is
the demonstration that cA4 activates *T. thermophilus* Csm6 (TtCsm6, Q53W17). What is
established in Thermus is therefore that cA4 is the active signal *received* by TtCsm6;
that TtCas10 is the enzyme that *makes* it is UniProt's inference (ECO:0000305), and the
annotations below are coded ISS accordingly. The demonstrated-synthesis exemplar is
A0A0A7HFE1 (STRTR), reviewed separately.

## Ontology gap: no GO term for cyclic oligoadenylate synthase activity

This is the substantive curation problem for this gene.

- `GO:0001730` 2'-5'-oligoadenylate synthetase activity is **not** reusable. Its
  definition is "Catalysis of the reaction: ATP = pppA(2'p5'A)n oligomers. This reaction
  requires the binding of double-stranded RNA." That is the metazoan interferon-induced
  OAS enzyme: the product is a *linear* 2'-5'-linked oligomer retaining a 5'-triphosphate,
  and the trigger is dsRNA. Cas10 makes a *cyclic* ring of 3'-5'-linked AMP units and is
  triggered by crRNA-guided target-RNA binding inside a ribonucleoprotein complex. The
  parentage differs too: GO:0001730 sits under GO:0070566 adenylyltransferase activity.
- GO *does* have sibling terms for the analogous bacterial cyclic-dinucleotide synthases,
  and both are direct children of GO:0016779 nucleotidyltransferase activity:
  `GO:0106408` diadenylate cyclase activity ("Catalysis of the reaction: 2 ATP =
  3',3'-c-di-AMP + 2 diphosphate") and `GO:0052621` diguanylate cyclase activity. A
  cyclic *oligo*adenylate synthase term is the missing member of that series, not a
  variant of the OAS term.
- `modules/crispr_cas_adaptive_immunity.yaml` (annoton `cas10_coa_synthesis`) deliberately
  carries no GO id for this function and records the gap under `knowledge_gaps`; a module
  cannot itself propose a term, so the proposal is made here.

Handled per CLAUDE.md "When a core activity has no GO term yet": a top-level
`proposed_new_terms` entry plus `proposed_molecular_function` on the core function, with
`molecular_function` left unset.

## Comparator check for the process terms

GO:0099048 CRISPR-cas system is the established process term for Cas proteins that do
part of the work of the three CRISPR stages; its definition names "acquisition of foreign
DNA by integration into CRISPR loci in the host chromosome, CRISPR RNA (crRNA)
biogenesis, and target interference". Cas10 performs target interference, so it is a
participant, not merely a requirement. The comparator check confirms the convention:
every curated *E. coli* K-12 Cascade subunit and adaptation protein in this repository
carries GO:0099048 (`genes/ECOLI/casA`, `casB`, `casC`, `casD`, `casE`, `ygbT`/cas1,
`ygbF`/cas2 — IDA, PMID:18703739), and casA/casE additionally carry GO:0051607 defense
response to virus (IMP, same paper) and GO:0032991 protein-containing complex (IDA,
PMID:25103409). Cas10 is annotated on the same pattern here.

No GO cellular-component term exists for the Csm/Cmr effector complex, so complex
membership is recorded at GO:0032991, which is exactly what the Cascade subunits carry.

## Decisions

- No existing annotations to adjudicate (GOA empty); all rows are `NEW`, coded ISS with
  the orthologue carried in `supporting_entities`, matching UniProt's own ECO:0000250/0305
  evidence for this entry.
- Two core functions: the HD ssDNase and the Palm cOA synthase, the latter via
  `proposed_molecular_function`.
- Biotechnology applications of type III systems are deliberately absent; they are not
  functions of the gene in its native host.
