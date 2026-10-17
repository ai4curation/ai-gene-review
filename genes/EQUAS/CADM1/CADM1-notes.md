# CADM1 (donkey, Equus asinus; UniProt A0A9L0IX39) - review notes

## Sources used

- Donkey UniProt record (unreviewed, Ensembl ENSEASP00005045449.1): `CADM1-uniprot.txt`, 390 aa; signal peptide, three Ig-like domains, one transmembrane helix.
- Donkey GOA: 8 IEA rows (6 TreeGrafter GO_REF:0000118 from PANTHER:PTN000589348; plasma membrane and synapse via GO_REF:0000120).
- Human CADM1 (Q9BY67) UniProt record fetched 2026-10-14: `CADM1-bioinformatics/human-CADM1-Q9BY67-uniprot.txt`.
- Alignment: `CADM1-bioinformatics/RESULTS.md`.
- Human QuickGO annotations (2026-10-14) as comparator: IDA (PMID:15811952) for signaling receptor binding (IPI), cell recognition, susceptibility to NK cell mediated cytotoxicity, detection of stimulus; IBA for homophilic cell-cell adhesion, neuron projection, synapse. PMID:15811952 is not cached, so it is not quoted.

## Sequence

- [RESULTS.md "The donkey CADM1 protein matches human CADM1 at 96.38% identity over 387 paired residues."]
- Stalk lacks the segment absent from human isoform 5 (human 333..360).
- Cytoplasmic tail is divergent: [RESULTS.md "The donkey entry therefore lacks the human C-terminal region that binds protein 4.1 (EPB41L3) and PDZ proteins (MPP2, MPP3, PALS2)"]. Note that the donkey record's ARBA SUBUNIT text lists these C-terminal interactions; that text is an automatic transfer and does not take the divergent donkey tail into account.

## Function (human ortholog)

- [human UniProt "Mediates homophilic cell-cell adhesion in a Ca(2+)-independent manner"]
- [human UniProt "Interaction with CRTAM promotes natural killer (NK) cell cytotoxicity"]
- [human UniProt "Acts as a synaptic cell adhesion molecule and plays a role in the formation of dendritic spines and in synapse assembly (By similarity)."]
- [human UniProt "Cell membrane {ECO:0000269|PubMed:11279526"]

## Review decisions (summary)

- signaling receptor binding (CRTAM ligand): ACCEPT. plasma membrane: ACCEPT. homophilic cell-cell adhesion: ACCEPT (core). susceptibility to NK cell mediated cytotoxicity: ACCEPT.
- cell recognition: KEEP_AS_NON_CORE. neuron projection, synapse: KEEP_AS_NON_CORE (the donkey tail lacks the C-terminal 4.1/PDZ-binding region used by the synaptic scaffolding interactions of human/mouse CADM1).
- detection of stimulus: MARK_AS_OVER_ANNOTATED (CADM1 is the ligand recognized by CRTAM on NK/T cells; the detecting cell is the NK cell).
