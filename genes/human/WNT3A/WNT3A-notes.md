# WNT3A evidence notes

Deep research note: `falcon` and the configured `perplexity-lite` fallback both
failed in this runtime because no corresponding provider was available. These
manual notes capture the curation synthesis for the WNT3A review.

WNT3A is a secreted, palmitoleated canonical Wnt ligand. Its UniProt record
summarizes the protein as a Frizzled-family ligand that activates the
TCF/LEF/beta-catenin pathway, and several direct human studies in GOA support
that core activity: recombinant or expressed WNT3A drives FZD/LRP-dependent
beta-catenin signaling, is carried in a soluble AFM complex, and requires
conserved disulfides for secretion and activity [PMID:20093360; PMID:26902720;
PMID:24841207].

WNT3A has a clean molecular/cellular core: extracellular Wnt ligand,
Frizzled/LRP receptor engagement, and activation of canonical Wnt signaling. The
many synapse, cardiac, mesoderm, neural and receptor-internalization rows in
GOA are context rows downstream of that ligand activity. They should be kept
only when WNT3A itself was supplied, depleted or bound in the cited experiment;
generic interactome protein-binding rows remain removable unless they establish
a WNT3A signaling function.

The PTHR12027 root PAINT rows support the generic Wnt-ligand features inherited
by WNT3A, and no PAINT IRD/IKR loss lies on the WNT3A lineage. Reactome ER,
Golgi, plasma-membrane and endocytic-vesicle rows describe the Wnt secretion
and receptor-trafficking itinerary; they are useful pathway context but should
not replace WNT3A's main extracellular/cell-surface ligand location.
