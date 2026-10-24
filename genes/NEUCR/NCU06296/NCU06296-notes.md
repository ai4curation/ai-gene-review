# NCU06296: biological evidence

NCU06296 is a predicted flavin-containing monooxygenase with an FMO-like dinucleotide-binding architecture. Family evidence supports FAD-dependent oxygenation using a reduced nicotinamide cofactor, commonly NADPH. Its physiological substrate, reaction specificity, pathway, and cellular compartment in Neurospora crassa remain unknown.

- monooxygenase activity: The FMO-like catalytic architecture and conserved monooxygenase IBA support broad flavin-dependent oxygenation. Experimentally characterized fungal FMO establishes NADPH/O2-dependent oxidation, while the substrate remains unresolved for this target.
- N,N-dimethylaniline monooxygenase activity: IPR020946 identifies a flavin-monooxygenase-like family with diverse substrates; it does not uniquely identify N,N-dimethylaniline as the acceptor. The target lacks retrieved substrate assays or a resolved characterized substrate-specific subfamily, so this exact reaction cannot be confirmed or refuted.
- flavin adenine dinucleotide binding: FAD is the prosthetic flavin used by the supported FMO catalytic architecture. Family placement supports this cofactor-binding annotation without resolving the oxidized substrate.
- NADP binding: The FMO dinucleotide-binding architecture and experimentally characterized NADPH-dependent fungal FMO chemistry support conserved NADP(H) cofactor binding.

Primary evidence excerpts

- [file:NEUCR/NCU06296/NCU06296-uniprot.txt] “DR   InterPro; IPR020946; Flavin_mOase-like.”
- [PMID:10077572] “The flavin-containing monooxygenase from yeast (yFMO) catalyzes the O2- and NADPH-dependent oxidations of biological thiols, including oxidation of glutathione to glutathione disulfide (GSSG).”

Provenance: live API snapshot 2026-09-09T03:00:51.831347+00:00. Complete API prediction JSON and all emitted claim IDs, text, and original evidence are preserved in the source and provenance JSON files. Current sequence/annotation data are separate comparison snapshots. Annotation overlap records known biology, not demonstrated training membership. All seven gene-focused Falcon jobs completed; the provider reports were inspected and useful primary leads checked. Publication retrieval used Europe PMC metadata/XML when the canonical PubMed fetch returned HTTP 429.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q7SAD4 is the only UniProt entry for NCU06296 (616 aa, sequence version 3, TrEMBL,
PE 3). It is the full-length gene model in the OR74A reference proteome, not an isoform or
fragment: the FMO-like Pfam domain (PF00743) and the PANTHER match span the protein
(PANTHER match 7-598) and the N-terminal FAD motif starts at residue 10. No other UniProt
accession for this gene exists, so there is no separate canonical product to review.

Literature: the falcon deep-research report found no gene-specific publication (no
biochemistry, phenotype, localization or pathway study for NCU06296/Q7SAD4). No new PMIDs.

Phylogenetic placement (see NCU06296-bioinformatics/RESULTS.md, panther_placement.py):
- PANTHER 19 subfamily PTHR23023:SF292 (FLAVIN-BINDING MONOOXYGENASE-LIKE PROTEIN
  (AFU_ORTHOLOGUE AFUA_6G01900)), a Pezizomycotina clade; NCU08749 (Q7SCE6) is a Neurospora
  in-paralog from a recent duplication (PTN000545913).
- The Fungi node (PTN007724818, 16 leaves, all uncharacterised) is joined to the animal FMO
  clade by the Opisthokonts speciation node PTN000545687, so human FMO1-5 are equally distant
  co-orthologs. None is in SF292.
- The IBA monooxygenase activity comes from the family root PTN009058586. PANTHER GO-slim MF on
  all ancestral nodes is generic (oxidoreductase / monooxygenase / GO:0016709); no substrate-
  specific activity was propagated.
- Yeast FMO1 (P38866; PMID:10077572) is in a different PANTHER family (PTHR43539:SF78), so the
  previous review's use of yFMO thiol oxidation as support was a cross-family transfer. It is
  removed as support (reference kept, flagged LOW relevance).

Sequence: FAD GxGxxG conserved (10-15 GSGLFG); FMO motif core retained with an insertion
(FKGQ...FHSK); second NADPH GxGxxG and FATGY motifs diverged; no hydrophobic C-terminal anchor
(unlike mammalian FMOs), so ER-membrane localization is not transferable. 29% identity to
human FMO3 over the global alignment.

Changes to actions:
- GO:0004497 monooxygenase activity (IBA): ACCEPT (unchanged), now supported by node placement
  and motif analysis instead of the out-of-family yeast paper.
- GO:0004499 N,N-dimethylaniline monooxygenase activity (IEA InterPro2GO): UNDECIDED ->
  MARK_AS_OVER_ANNOTATED. Substrate-specific reaction of mammalian xenobiotic FMOs; PAINT
  deliberately did not propagate any substrate-specific activity to ancestors of this clade.
- GO:0050660 FAD binding: ACCEPT (unchanged).
- GO:0050661 NADP binding: ACCEPT -> KEEP_AS_NON_CORE, because the NADPH dinucleotide motif is
  diverged and cofactor preference is unverified.

Relative to review next: human FMO3 (P31513), chosen as the best-characterised member of the
animal FMO clade, which is co-orthologous (Opisthokonts speciation node) to the fungal clade
containing NCU06296; FMO1/2/4/5 are equally close phylogenetically. No genes/human/FMO* review
exists in the repo.

Family review interpro/panther/PTHR23023/PTHR23023-review.yaml lists NCU06296 under a single
family-wide subfamily label and cites yeast yFMO as fungal experimental context; it does not
record SF292, and PANTHER 19 places yeast FMO1 outside PTHR23023. Not edited (outside this
gene folder); reported to the orchestrator.

No modules contain this gene (only modules/aliphatic_glucosinolate_myrosinase_defense.yaml
mentions plant FMOs).
