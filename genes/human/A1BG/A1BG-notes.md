# A1BG (alpha-1B-glycoprotein) — review notes

Reviewed as part of the PAINT human no-IBA project, using the `affinage` deep-research
provider (`A1BG-deep-research-affinage.md`) plus UniProt P04217, the GOA TSV, and the
primary literature.

## What the protein is

A1BG is an abundant **secreted plasma glycoprotein** of unknown catalytic function. The
mature chain (residues 22–495) follows a cleaved signal peptide and is built from **five
tandem immunoglobulin-like domains**; there is **no transmembrane segment** anywhere in the
protein and UniProt lists `SUBCELLULAR LOCATION: Secreted` with keyword `Secreted`
[file:human/A1BG/A1BG-uniprot.txt, "SUBCELLULAR LOCATION: Secreted."].

The complete protein sequence was determined directly from *plasma*-purified protein
[PMID:3458201, "The complete amino acid sequence has been determined for alpha
1B-glycoprotein"], which also established the five-domain internal duplication and the
immunoglobulin-superfamily relationship [PMID:3458201, "consists of five repeating
structural domains, each containing about 95 amino acids and one disulfide bond"].

## Why the IBA annotations are wrong for this gene

This is the central curation finding for A1BG.

PANTHER places A1BG in **PTHR11738 ("MHC class I NK cell receptor")**, the LILR/KIR
leukocyte-receptor family (subfamily `PTHR11738:SF184`), and InterPro assigns
`IPR016332 A1B_glyco/leuk_Ig-like_rcpt` and `IPR050412 Ig-like_Receptors_ImmuneReg`
[file:human/A1BG/A1BG-uniprot.txt, "PANTHER; PTHR11738; MHC CLASS I NK CELL RECEPTOR; 1."].
The other members of that family are **type-I transmembrane immune receptors**. A1BG is the
divergent, **soluble, secreted** member — it kept the Ig ectodomain repeats but has no
transmembrane anchor and no cytoplasmic signalling tail.

The three GO_Central IBA annotations therefore propagate receptor biology that A1BG
physically cannot perform:

| IBA term | Problem |
|---|---|
| `GO:0005886` plasma membrane (`is_active_in`) | A1BG is secreted; no TM domain (UniProt FT lists SIGNAL 1..21, CHAIN 22..495, five DOMAINs, **no TRANSMEM**) |
| `GO:0004888` transmembrane signaling receptor activity | requires a transmembrane protein; A1BG has none |
| `GO:0060396` growth hormone receptor signaling pathway | different root cause — see below |

The first two are straightforward **PROPAGATION_BAD**: the source annotations are correct
for the transmembrane receptors they came from, but the term must not transfer to the
secreted member.

### The growth-hormone IBA is a *source* problem, not a transfer problem

I initially assumed `GO:0060396` was another family over-propagation, but tracing the
WITH/FROM field disproves that. It cites `PANTHER:PTN000200788` and `MGI:MGI:2152878` —
and MGI:2152878 is **mouse *A1bg* itself**, i.e. the true ortholog, which carries an MGI
**IMP** to the same term. So the transfer is mechanically legitimate; the defect is in the
source annotation.

The mouse IMP rests on PMID:16723264, which isolated *A1bg* ("cDNA #5") in a subtractive
screen for transcripts induced in the liver of GH-transgenic mice, and found it absent from
GH-deficient dwarf mice, GH-antagonist mice, and GH-receptor knockouts
[PMID:16723264, "These findings suggest that induction of mRNA #5 in the liver requires a
continuous pattern of GH secretion and an intact GH-GH receptor-signaling complex."].

That demonstrates A1bg is a **transcriptional target downstream of** the GH axis. GO:0060396
is defined as the molecular signals generated as a consequence of the GH receptor binding
growth hormone — a GH-inducible secreted liver product is not part of that cascade. This is
a `ROLE_CONFLATION` at the source (response-to-X read as participates-in-X-pathway). The
defensible term for the mouse data would be a response term such as `GO:0060416 response to
growth hormone`; there is no human evidence for even that, so the human IBA is removed
rather than modified. Flagged as a `suggested_question` so the mouse source annotation can
be re-curated upstream.

All three IBAs are therefore recommended for `REMOVE`, each with a `propagation_review`
recording the root cause. None of these is second-guessing a human experimental curator.

## What A1BG actually does

A1BG works through its Ig-like domains as a **plasma binding/sequestering partner for
CAP-superfamily (CRISP) proteins**.

- **CRISP3.** CRISP3 circulates in plasma bound to A1BG; the complex is 1:1, noncovalent,
  electrostatically held, with a nanomolar dissociation constant
  [PMID:15461460, "We demonstrate that CRISP-3 is a specific and high-affinity ligand of A1BG
  with a dissociation constant in the nanomolar range as evidenced by surface plasmon
  resonance."]. UniProt records this as the sole curated `SUBUNIT` interaction
  [file:human/A1BG/A1BG-uniprot.txt, "Interacts with CRISP3."]. The same paper notes that the
  analogous complexes between snake-venom toxins and A1BG-like opossum plasma proteins
  neutralise toxin activity — i.e. this protein family is a plasma sequestering/neutralising
  system.
- **CRISP2 / CAP proteins.** Co-expression of A1BG with CAP proteins **abolished their sterol
  export function** and A1BG **inhibits their sterol binding in vitro**
  [PMID:39433128, "Coexpression of A1BG with CAP proteins abolished their sterol export
  function in yeast and their interaction inhibits sterol-binding in vitro."]. The contact is
  mapped to **the third of the five Ig-like domains** and requires Mg²⁺
  [PMID:39433128, "We map the interaction between A1BG and CRISP2 to the third of five
  repeated immunoglobulin-like domains within A1BG."].

This is a coherent molecular function — binding a partner protein so as to block that
partner's own ligand-binding/export activity — and maps onto `GO:0140311 protein sequestering
activity` ("Binding to a protein to prevent it from interacting with other partners or to
inhibit its localization to the area of the cell or complex where it is active"). It is
proposed as a `NEW` annotation because GOA currently gives A1BG **no** molecular function at
all other than the incorrect receptor IBA.

## Other reported activities (recorded, not annotated as core)

- **NAMPT stabilisation / chemoresistance.** Adipocyte-secreted A1BG binds NAMPT and stabilises
  it, raising NAD⁺ and boosting PARP1-dependent DNA repair, driving cisplatin resistance in
  osteosarcoma [PMID:40560034, "Further investigation revealed a direct interaction between
  A1BG and NAMPT, leading to the stabilization of NAMPT and an increased NAD+ production."].
  Single-paper, cancer-context; noted in `suggested_questions` rather than annotated.
- **Female-specific cardiac role.** Cardiomyocyte-restricted *A1bg* knockout gives dilated
  cardiomyopathy in female but not male mice [PMID:40270023, "The glycoprotein A1BG has emerged
  as a female-specific regulator of cardiac structure and integrity"]. Mouse phenotype; not
  used for a human GO process annotation here.

## Localisation calls

`GO:0005576 extracellular region` is the core location and is supported by direct isolation
from plasma (IDA), by UniProt SubCell, and by several independent proteomics datasets. The
granule-lumen terms (`GO:0034774`, `GO:1904813`, `GO:0031093`) come from Reactome
degranulation reactions and the exosome/blood-microparticle terms from HDA proteomics; all are
consistent with an abundant secreted plasma protein but are peripheral, so they are kept as
non-core.

## Affinage assessment

The affinage report passed its trust gates at fetch time (accession P04217 matching the local
UniProt record, no non-human organism token; it carries no `self_evaluation_pairwise` score) and its narrative — secreted Ig-domain plasma protein acting through
protein–protein interactions with CRISP2 and NAMPT — agrees with the primary literature. Its
own `mechanism_profile` grounding (`GO:0098772 molecular function regulator activity`,
`GO:0005576 extracellular region`) is correct but coarse; `GO:0140311` was chosen instead as
the specific descendant supported by the CRISP2/CRISP3 experiments. Notably the affinage
narrative independently contains **nothing** about membrane receptors or growth-hormone
signalling, corroborating the IBA removals.

Limitation worth recording: affinage gave no signal *at all* about the incorrect IBAs — it
simply does not mention them. The IBA root-cause analysis above required going outside the
deep-research report, to the GOA WITH/FROM field, the mouse ortholog's own GO record, and
the source paper. Affinage is useful for establishing what a gene *does*; it does not audit
what GO already says.
