# NCU04937 (Q7S3T0) homology re-check, 2026-10-21

Script: `homology_rereview.py` (run with `uv run --script homology_rereview.py`);
raw output in `results-rereview.json`.

## Sequence

Q7S3T0 is 114 aa (sequence version 3). A single uninterrupted polyglutamine run of 50 residues starts at position 55. The non-repetitive parts are an N-terminal 54-residue segment and a 10-residue C-terminal tail (LVSNTLECLV). UniParc UPI00015C37E0 is an earlier 124-aa model of the same locus (inactive versions of Q7S3T0, XP_959385 and EAA30149). It shares residues 1-104 and then has a different C-terminal tail (LHVVLDLAVSIVPWHACRHT), so the 3' end of the gene model has been revised.

## Family signatures

InterPro has a single match. It is PANTHER PTHR13270 (official name "PROTEIN C20ORF116-RELATED"; InterPro display name "Host Cell Invasion-Related"), subfamily PTHR13270:SF14 "SEX DETERMINATION AND DOSAGE COMPENSATION PROTEIN SDC-2", over residues 38-104, with score 3.7e-05. That region is almost entirely the polyglutamine run. The protein has no Pfam, SMART, PROSITE, CDD or other domain match. The weak PANTHER score and the composition of the matched region show that the assignment comes from low-complexity sequence and not from a shared conserved domain. No function can be transferred from this family placement, and in particular nothing from C. elegans SDC-2, a nematode-specific dosage-compensation protein.

## BLASTP (poly-Q collapsed to 10 Q, no low-complexity filter, UniProtKB)

The only significant hit is Q7S3T0 itself (8e-40). The next hits are scattered Drosophila CUB-domain proteins, a Rho-GAP protein, insect proteins and others. All have E >= 0.009 (bits <= 43), and the alignments fall on Q-rich stretches. No hit came from another Neurospora species or from any other Sordariomycete, even though N. tetrasperma and N. discreta proteomes are in UniProtKB.

## Conclusion

Within the limits of these searches, NCU04937 is an orphan open reading frame. It has no detectable ortholog, no conserved domain, and a gene model that has changed at its 3' end. No characterised relative can be identified on phylogenetic grounds. These results support no function or location for the protein. It is also possible that this locus is not a conserved protein-coding gene, but these searches cannot decide that.
