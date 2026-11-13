# mraY (Escherichia coli K-12, P0A6W3) — curation notes

Reviewed as the lipid I synthesis exemplar of
`modules/peptidoglycan_precursor_biosynthesis.yaml`. No provider deep-research
file was generated for this gene (the deep-research providers were not available
in this session); these are the curator's own notes, and every claim below is
traceable to the cached UniProt record or a cached publication.

## What the protein does

MraY transfers phospho-MurNAc-pentapeptide from UDP-MurNAc-pentapeptide onto
undecaprenyl phosphate, releasing UMP and forming lipid I — the first
membrane-bound step of peptidoglycan synthesis
[file:ECOLI/mraY/mraY-uniprot.txt "Catalyzes the initial step of the lipid cycle reactions in"].
UniProt curates the reaction with the meso-diaminopimelate-containing
pentapeptide (Rhea:RHEA:28386), with evidence from PMID:1846850 and PMID:215212
[file:ECOLI/mraY/mraY-uniprot.txt "Xref=Rhea:RHEA:28386, ChEBI:CHEBI:57865,"].
Mg2+ is required; Mn2+ restores only 10% of activity
[file:ECOLI/mraY/mraY-uniprot.txt "Replacement of Mg(2+) by Mn(2+) restores only 10% of the activity."].

Gene identification rests on amplification of the then-unnamed ORF-Y raising the
measured transferase activity
[PMID:1846850 "Very probably mraY is the structural gene for the"], with the
amplified activity tunicamycin-sensitive
[PMID:1846850 "The enhanced enzyme activity was sensitive to tunicamycin, and the amino"].
Geis and Plapp solubilized the enzyme from K12 envelopes
[PMID:215212 "was solubilized by repeated freezing and thawing of crude envelopes"]
and showed that transfer activity depends on phospholipid
[PMID:215212 "addition of an aqueous lipid dispersion."].

Location: UniProt records the inner membrane and multi-pass topology from the
global inner-membrane topology study (PMID:15919996)
[file:ECOLI/mraY/mraY-uniprot.txt "SUBCELLULAR LOCATION: Cell inner membrane"],
and the cryo-EM structure of the YES complex shows a membrane-embedded MraY dimer
[PMID:37440661 "densities for 22 TMDs are clear, 20 of which are accounted for by the EcMraY dimer"].
Phage phiX174 protein E inhibits MraY by occupying the active-site pocket; that is
host-pathogen context, not an MraY function, so it is not annotated here.

## The stem-peptide term problem

`GO:0008963` has a stem-generic name (EC 2.7.8.13) but an L-lysine-specific
definition (RHEA:21920). Its meso-diaminopimelate counterpart `GO:0051992`
(RHEA:28386) is a **sibling** under `GO:0016780`, not a descendant. E. coli makes
the DAP pentapeptide, so the four `GO:0008963` rows are corrected laterally to
`GO:0051992` (MODIFY with a non-descendant replacement, the long-standing use for
lateral/substrate corrections) rather than removed: the enzyme itself does not
select the third stem residue, MurE does.

The same pair-of-siblings problem affects MurF (`GO:0047480` vs `GO:0008766`) and
MurG (`GO:0050511` vs `GO:0051991`). For MurF there is direct evidence that the
enzyme accepts both tripeptide forms in both E. coli and S. aureus
[PMID:20659527 "S. aureus MurF appeared less specific and accepted both forms"],
so the other-stem row is retained as non-core there; for MraY and MurG no such
evidence exists for the organism in question, so those rows are corrected. That
distinction is the standard applied across the module's genes. A
stem-peptide-agnostic parent for all three activities is raised as a
`suggested_questions` entry.
