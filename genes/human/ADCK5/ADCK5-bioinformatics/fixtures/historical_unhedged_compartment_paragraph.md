<!-- REGRESSION FIXTURE - DO NOT EDIT.
     The paragraph exactly as it shipped in branch commit 419dc9e37 and was flagged in
     review of PR #2312: it asserts the withdrawn compartment conclusion with no hedge.
     Frozen here rather than referenced by SHA, because a branch-local commit does not
     survive squash-merge and the strongest test in the suite would break on landing. -->

Topology: NOTCH2NLA (Q7Z3S9, reviewed, 236 aa) is annotated `Secreted` and `Cytoplasm` and
is a human-specific regulator of neural progenitor proliferation. ADCK5 is a mitochondrial
protein — in eukaryotes "UbiB homologs are found exclusively in mitochondria" — and its only
large interaction dataset (PMID:27499296, the mitochondrial interactome) returns 25 partners
of which 17 are annotated to the mitochondrion. Y2H places both proteins in the yeast
nucleus and so removes exactly the targeting constraint that makes the pairing implausible
in vivo.
