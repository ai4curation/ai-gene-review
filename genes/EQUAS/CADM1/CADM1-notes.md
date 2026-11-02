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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

- Deep research: `just deep-research-falcon EQUAS CADM1 --fallback perplexity-lite` failed (Edison API 403 "Failed to authenticate"; the perplexity-lite fallback also failed). No deep-research file was written; the review uses cached literature and sequence analysis.
- Literature cached this session (abstract-only): PMID:15811952 (Boles 2005, Necl-2 is the CRTAM ligand) [PMID:15811952 "CRTAM-Necl-2 interactions promote cytotoxicity of NK cells"]; PMID:15781451 (Galibert 2005) [PMID:15781451 "We further show that Necl2 binds Class-I-restricted T-cell-associated molecule (CRTAM)"]; PMID:12202822 (Biederer 2002, SynCAM) [PMID:12202822 "functions as a homophilic cell adhesion molecule at the synapse"; "Expression of the isolated cytoplasmic tail of SynCAM in neurons inhibited synapse assembly."]; PMID:11279526 (Kuramochi 2001, TSLC1).
- Identity: A0A9L0IX39 is one of eight UniProt/Ensembl products of the single donkey CADM1 gene. The UniProt gene-centric canonical product is A0A9L0IJE9 (473 aa, ends EYFI). The benchmark (390 aa) is identical to the short-stalk product A0A9L0IKY6 for 379 residues and then ends in an 11-residue alternative tail LFSLTSSPRIK in place of the 38-residue 4.1/PDZ-binding tail [RESULTS-rereview.md "It then ends in an 11-residue alternative tail (LFSLTSSPRIK) in place of the 38-residue cytoplasmic tail that carries the protein 4.1-binding region and the C-terminal EYFI PDZ-binding motif."]. The earlier open question of whether donkey has an EYFI-tail CADM1 is answered: it does (A0A9L0IJE9, A0A9L0IKY6, A0A8C4LBJ1, A0A9L0JLU5, A0A9L0JM59). Analysis: `CADM1-bioinformatics/compare_isoforms_rereview.py`, `RESULTS-rereview.md`.
- Evolutionary grounding: donkey UniProt places the protein in PANTHER PTHR45889:SF2 (CELL ADHESION MOLECULE 1), the same subfamily as human Q9BY67 and mouse Q8R5M8. Donkey GOA rows are TreeGrafter transfers from PTN000589348. In human, PAINT node PTN002913382 carries signaling receptor binding, cell recognition, susceptibility to NK cytotoxicity, detection of stimulus, plasma membrane, neuron projection and synapse; homophilic cell-cell adhesion sits on deeper node PTN001910345 (with CADM3). PAINT did not propagate the mouse ISS-based protein homodimerization or cytoskeletal-binding terms; I did not add them.
- Decisions unchanged in substance: ACCEPT signaling receptor binding, plasma membrane, homophilic cell-cell adhesion, susceptibility to NK cell mediated cytotoxicity; KEEP_AS_NON_CORE cell recognition, neuron projection, synapse (tail-dependent synaptic roles uncertain for this short-tail product); MARK_AS_OVER_ANNOTATED detection of stimulus (CADM1 is the detected ligand; not removed because human has IDA + IBA). NEW cell-cell adhesion mediator activity retained, now supported by PMID:12202822. Supporting text moved from UniProt-only to primary-literature quotes where available.
- PANTHER family folder interpro/panther/PTHR45889 has only the InterPro metadata/entries (no family review); no subfamily placement disagreement. No module in modules/ mentions CADM1.
- Relative: canonical product of the same gene, A0A9L0IJE9 (no review in repo; would go in genes/EQUAS/CADM1__A0A9L0IJE9). The best characterised ortholog (human CADM1 Q9BY67, same PANTHER subfamily) also has no review in the repo.
