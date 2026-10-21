# WDPCP: paired human–horse review notes

## Biological evidence

WDPCP is a CPLANE ciliary scaffold with an independent actin/septin/polarity role. Mouse microscopy and perturbation establish ciliary-base, cytoplasmic actin and focal-adhesion pools. Recombinant structural work demonstrates individual WDPCP phosphoinositide binding in its C-terminal tail. The full2016paper explicitly reports human WDPCP variants and relevant digit/tongue/palate phenotypes.

- [PMID:24302887: Wdpcp, a PCP protein required for ciliogenesis, regulates directional cell migration and cell polarity by direct modulation of the actin cytoskeleton.](https://pubmed.ncbi.nlm.nih.gov/24302887/) — full text cached.
- [PMID:27158779: The ciliopathy-associated CPLANE proteins direct basal body recruitment of intraflagellar transport machinery.](https://pubmed.ncbi.nlm.nih.gov/27158779/) — full text cached.
- [PMID:35427153: Structure of the ciliogenesis-associated CPLANE complex.](https://pubmed.ncbi.nlm.nih.gov/35427153/) — full text cached.

## Exact horse model

The horse N-terminal difference resembles the approximately35-residue human extension relative to mouse reported in the structure. The conserved scaffold supports broad ciliary/cytoskeletal predictions. A separate nine-residue deletion affects the lipid-binding tail; disorder does not imply that deletion is functionally irrelevant, and exact lipid affinity remains unresolved.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/WDPCP/WDPCP-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

Distinguish transition-zone/base localization from the axonemal shaft. Test the tail deletion before transferring quantitative phosphoinositide affinity.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used. Deep research: `just deep-research-falcon HORSE WDPCP --fallback perplexity-lite`
failed (Edison API "Failed to authenticate", 403; the perplexity-lite fallback also failed), so this
re-review uses the cached primary literature directly.

### Identity of the benchmark accession

- A0A3Q2KRK8 (705 aa) is the product of Ensembl transcript ENSECAT00000034053, one of eight protein-coding
  transcripts of horse gene ENSECAG00000019956. Ensembl marks ENSECAT00000134648 (UniProt A0A9L0T876,
  756 aa) as canonical, and GOA propagates the PTHR13667 IBA set (cilium organization, axonemal basal
  plate, establishment of protein localization, nervous system development) only to A0A9L0T876; this
  accession receives only the two ARBA/SubCell IEA rows. No horse WDPCP entry is Swiss-Prot reviewed.
- Re-review alignment (`WDPCP-bioinformatics/rereview/RESULTS-rereview.md`): A0A3Q2KRK8 is colinear with
  human O95876 from human residue 34 to 722 (89.3% identity), i.e. WD40 propeller and alpha-solenoid intact.
  The missing human 1-33 is the human-specific N-terminal extension, also absent from mouse Q8C456
  [PMID:35427153 "Compared to mouse, the human Wdpcp has an N-terminal extension of ~35 residues"].
- Its C-terminus is an alternative final exon: horse 694-705 (ASYWKHQQWTMYA region) aligns to neither
  human nor mouse, and the conserved terminal motif (GSLxMxHFxLV) of human, mouse and horse A0A9L0R7M2 is
  missing. That motif lies in the C-terminal ~60 residues that carry mouse Wdpcp PIP binding
  [PMID:35427153 "MmWdpcp PIP binding is mediated by the C-terminal ~60 amino acids"]. The earlier note
  describing this as a short "721-729 deletion" is superseded.
- The horse model colinear with human/mouse at both ends is A0A9L0R7M2 (713 aa). The Ensembl canonical
  A0A9L0T876 itself diverges after residue 668.

### Evolutionary grounding

All horse models, human, mouse, rat and Xenopus WDPCP are in PTHR13667:SF5. The PAINT node PTN001007408
(Eumetazoa) carries IBD for GO:0097541, GO:0044782, GO:0045184 and GO:0007399, but not plasma membrane,
axoneme, phosphatidylinositol binding or septin cytoskeleton organization (taken as deliberate).

### Annotation decisions

- GO:0005886 plasma membrane (IEA, ARBA SubCell): MODIFY to GO:0005938 cell cortex. Xenopus Fritz-GFP is
  "concentrated at the cell cortex" [PMID:20671153]; mouse Wdpcp is on actin and focal adhesions
  [PMID:24302887]; no TM segment; PI(3)P preference is not a plasma-membrane signature.
- GO:0005930 axoneme (IEA): changed UNDECIDED -> ACCEPT. Mouse IMCD3 antibody staining [PMID:24302887
  "Wdpcp is localized to the ciliary axoneme and in a ring-like structure at the base of the cilia"] and
  Xenopus [PMID:20671153 "sept7 and Fritz were localized along ciliary axonemes"].
- NEW GO:0097541 axonemal basal plate and GO:0044782 cilium organization, both from the PAINT node; the
  omission is a GOA propagation artefact for a non-canonical product. CPLANE participation: WDPCP is a
  structural subunit of the complex that recruits peripheral IFT-A to basal bodies [PMID:27158779].
- Not added: phosphatidylinositol binding (not on the PAINT node, and this isoform lacks the conserved
  tail end), septin cytoskeleton organization (not on node), nervous system development, and mouse
  digit/palate/cochlear phenotypes (organismal outcomes).

### Relative / family / modules

- Relative: same-gene canonical product A0A9L0T876 (Ensembl canonical; no review in repo; folder would be
  `genes/HORSE/WDPCP__A0A9L0T876`). A0A9L0R7M2 is the more human-like full-length model and could be the
  better representative. The closest characterized ortholog is human O95876 (`genes/human/WDPCP/`, all rows
  reviewed though status IN_PROGRESS; its axoneme rows are still UNDECIDED, which this review's evidence
  would resolve).
- `interpro/panther/PTHR13667/PTHR13667-review.yaml` places horse A0A3Q2KRK8 and human O95876 in SF5; no
  disagreement. The family review does not record the PAINT node or the isoform issue.
- Modules: `modules/bbsome.yaml` mentions WDPCP/BBS15 only as out of scope; no CPLANE module exists.
