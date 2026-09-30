# tlr21 (zebrafish, UniProt F1QMN8) — curation notes

No `tlr21-deep-research-*.md` file was produced by the batch harness before this
review was written; these notes rest on the UniProt record, the GOA rows and the
cached publications.

## Entry identity (TrEMBL, unreviewed)

`F1QMN8_DANRE`, 989 aa, submitter name "Toll-like receptor 21 precursor", gene name
tlr21 (synonym TLR21.1), cross-referenced to RefSeq NP_001186264, GeneID 402884 and
ZFIN ZDB-GENE-040220-4. NCBI gene 402884 is "tlr21 toll-like receptor 21" on
chromosome 16, so this is the right gene, and the length matches the
receptor characterised in the literature
[PMID:24282308 "zebTLR21 contains 989 amino acid residues"]. PANTHER subfamily PTHR24365:SF545, shared with chicken TLR21.

The entry's DE line carries `EC=3.2.2.6`, inherited from the RefSeq record; this is
the source of a spurious enzymatic GO annotation, discussed below.

## Established biology

- Zebrafish TLR21 is a CpG-DNA receptor with its own sequence preference, distinct
  from that of zebrafish TLR9:
  [PMID:24282308 "zebTLR21 responded preferentially to CpG-ODN with GTCGTT motifs"],
  whereas zebTLR9 has a broader profile. Specificity is a property of the ectodomain:
  [PMID:24282308 "the ectodomains of these two TLRs determine their ligand recognition"].
- It does not respond to the ligands of other TLRs — poly(I:C), flagellin,
  Pam3CSK4, lipopolysaccharide and the TLR7/8 agonists were all tested and did not
  activate cells expressing it.
- It is an intracellular receptor:
  [PMID:24282308 "The majority of that zebTLR9 and zebTLR21 was localized in the endoplasmic reticulum"],
  its activation is blocked by chloroquine, and it binds and is regulated by
  UNC93B1, with acidic residues in its juxtamembrane region required for that
  interaction.
- Functionally the two receptors cooperate in vivo:
  [PMID:24282308 "These results suggest that zebTLR9 and zebTLR21 cooperatively mediate the antimicrobial"]
  [PMID:24282308 "activities of CpG-ODN"], with CpG oligodeoxynucleotides that
  activate both inducing more cytokine production and giving better protection
  against *Edwardsiella tarda* than those that activate TLR9 alone.
- Expression is highest in immune organs and is induced by immunostimulants:
  [PMID:22729906 "Up to a 3-fold increase in tlr21 and tlr22"]
  [PMID:22729906 "expression was detected in larvae exposed to immunostimulants such as"]
  lipopolysaccharide, peptidoglycan or poly I:C. That is transcript-level evidence
  only.

## The EC:3.2.2.6 annotation

GOA carries GO:0061809 "NAD+ nucleosidase activity, cyclic ADP-ribose generating"
(IEA from EC:3.2.2.6) on this entry, because the TrEMBL DE line inherited that EC
number from RefSeq. This is removed. The claim presumably originates in the NADase
activity of some TIR domains (plant TIR proteins and human SARM1), and UniProt
states the general case explicitly for Toll-like receptors: "In some plant proteins
and in human SARM1, the TIR domain has NAD(+) hydrolase (NADase) activity (By
similarity). However, despite the presence of the catalytic Asp residue, the
isolated TIR domain of human TLR4 lacks NADase activity (By similarity). Based on
this, it is unlikely that Toll-like receptors have NADase activity"
(the same caution appears on every reviewed mouse entry of this family, e.g.
`file:mouse/Tlr13/Tlr13-uniprot.txt` lines 141-147). No NADase activity has been reported for any TLR21,
and the functional literature on this receptor concerns CpG-DNA sensing.

## Annotation decisions (summary)

- Both GO:0002224 rows (IDA, PMID:24282308; IBA) modified to GO:0035682 toll-like
  receptor 21 signaling pathway: the receptor-specific term exists, and the cited
  paper demonstrated ligand-induced signalling through this receptor, with the
  specificity residing in its own ectodomain and the output depending on its own TIR
  residues.
- GO:0002221 pattern recognition receptor signaling pathway (IDA, PMID:22729906) kept
  as non-core: it is the generic parent of the terms above, and its cited evidence is
  expression modulation rather than signalling.
- GO:0038023 (IBA) modified to GO:0038187 pattern recognition receptor activity —
  CpG DNA is a pattern, the receptor's ectodomain determines which CpG motifs are
  recognised, and it does not respond to other TLR ligands.
- GO:0005783 endoplasmic reticulum (IDA) accepted; GO:0005886 plasma membrane (IBA)
  marked as over-annotated, since the receptor is intracellular and
  chloroquine-sensitive.
- GO:0019731 antibacterial humoral response (IDA) kept as non-core: the receptor
  mediates a CpG-driven protective response against a bacterial pathogen, but it is
  the sensor upstream of the humoral effectors rather than an effector itself.
- GO:0061809 removed (see above); GO:0007165 and GO:0016020 kept as non-core.
