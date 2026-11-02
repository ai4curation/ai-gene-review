# Horse WDPCP Ensembl canonical product A0A9L0T876: gene-model analysis

Reproduce: `uv run analyze_canonical_model.py` in this folder (2026-10-20). The script downloads the sequences from UniProt REST (saved to `sequences.fasta`) and the exon structures from Ensembl REST; its raw output is in `output.txt`. No number below is entered by hand.

## Sequence comparison

- A0A9L0T876 (756 aa, transcript ENSECAT00000134648, Ensembl canonical) and A0A9L0R7M2 (713 aa, ENSECAT00000123939) are identical over residues 1-660.
- After residue 660, A0A9L0T876 has 96 novel residues (661-756) and lacks the 53 C-terminal residues of A0A9L0R7M2 (661-713), which end in the conserved GSLxMxHFxLV motif shared with human and mouse.
- Against human O95876 (746 aa), the longest aligned block ends at A0A9L0T876 659 = O95876 692, leaving 54 human residues with no counterpart.
- Mouse Wdpcp binds phosphoinositides through its last 60 C-terminal residues (PMID:35427153). The equivalent human window is O95876 687-746. Only 6 of those 60 residues (687-692) lie inside the colinear block of A0A9L0T876, and the ciliopathy residue S708, which sits in the PIP-binding tail, has no counterpart.
- The cryo-EM maps of PMID:35427153 do not resolve the C-terminal ~100 residues of human or mouse Wdpcp, which are predicted to be disordered. The divergence of A0A9L0T876 therefore falls entirely within the unresolved tail: the seven-bladed WD40 beta-propeller and the alpha-solenoid that form the Inturned/Fuzzy interfaces are retained intact.

## Exon structure

- ENSECAT00000134648 has 16 exons and ENSECAT00000123939 has 18. Fourteen exons have identical coordinates. The first exons overlap and differ only at their 5' end.
- The last exon of ENSECAT00000134648 (chr15:39280402-39281267) lies inside the ENSECAT00000123939 intron between the exon ending at 39278914 and the exon starting at 39304548. Three ENSECAT00000123939 exons lie downstream of it.
- The novel 96-residue tail of A0A9L0T876 is thus encoded by an alternative terminal exon placed within an intron of the full-length model. Neither UniProt nor Ensembl provides protein-level evidence that this product is made.

## Family and PAINT context

- UniProt places A0A9L0T876 in PANTHER PTHR13667:SF5, the subfamily that contains human O95876, mouse Q8C456 and Xenopus Q32NR9 (all with experimental data).
- A0A9L0T876 receives the four IBA annotations of PAINT node PTN001007408 (taxon 6072, Eumetazoa; interpro/panther/PTHR13667/PTHR13667-paint.tsv): axonemal basal plate (GO:0097541), cilium organization (GO:0044782), nervous system development (GO:0007399) and establishment of protein localization (GO:0045184). The node carries no plasma membrane, axoneme, cell cortex or phosphatidylinositol binding assertion.

## Interpretation

The core CPLANE-forming scaffold (propeller plus solenoid) is fully present, so the ciliary-base functions placed at PTN001007408 can be inherited by this product on phylogenetic grounds. The phosphoinositide-binding module mapped in mouse is absent and is replaced by an unrelated sequence, so lipid binding cannot be transferred to A0A9L0T876. Whether the novel tail has any property of its own is unknown.
