# MVP (Q14764) review notes

## Deep research

`just deep-research-falcon human MVP --fallback perplexity-lite` failed in this
environment: neither the falcon nor the perplexity provider was available (no API
keys; only `openscientist` and `claude_code` were listed). No `-deep-research-*.md`
file was generated. The literature search below was done by hand through PubMed
E-utilities, and the hits were cached with `ai-gene-review fetch-pmid`.

Queries (PubMed, title fields unless stated): "major vault protein knockout mice",
"vault structure 3.5 Angstrom", "major vault protein interferon", "major vault protein
Pseudomonas", "major vault protein NF-kappaB", "major vault protein apoptosis",
"vault particle cryo-EM", "vault Dictyostelium", "vault evolution distribution
phylogenetic", author searches for Mossink, Stephen AG and Kickhoefer.

## What MVP is

- The structural shell of the vault. Two half-vaults, each made of 39 identical MVP
  chains [PMID:19150846 "the cage structure consists of a dimer of half-vaults, with each
  half-vault comprising 39 identical major vault protein (MVP) chains"]. MVP alone forms
  vault-like particles [PMID:11349122 "the expression of the rat MVP alone can direct the
  formation of particles that have biochemical characteristics similar to endogenous rat
  vaults"].
- Minor components: PARP4, TEP1 and vault RNAs [PMID:10551828; PMID:38612882]. PARP4 binds
  MVP repeats 3-4, and the human cage has interior NAD+/ADP sites [PMID:40691181
  "unexpected binding sites for NAD+ and related nucleotides within the interior of the
  vault cage"].
- Ancestral in eukaryotes, lost in fungi, insects and probably plants [PMID:23887922].
- LRP, the "lung resistance-related protein", is MVP [PMID:7585126].

## Function: still unknown

- MVP-/- mice are viable and healthy, and are not sensitised to cytostatics
  [PMID:12499273 "The MVP(-/-) mice are viable, healthy, and show no obvious
  abnormalities"].
- Nucleocytoplasmic transport is normal in MVP-/- MEFs [PMID:16310186 "indicated no
  differences in nuclear import/export kinetics, suggesting no role for vaults in these
  processes"].
- Signalling modulation: SHP-2 substrate and scaffold in EGF signalling [PMID:15133037];
  binds the SRC SH2 domain and inhibits SRC [PMID:16441665]; IFN-gamma inducible and
  dampens STAT1 [PMID:16418217]; restrains TRAF6/NF-kappaB in macrophages (mouse KO)
  [PMID:30996248]; induced by viruses and promotes type I IFN [PMID:22318991].
- Recruited to lipid rafts and needed for clearance of P. aeruginosa by lung epithelial
  cells [PMID:17615361].
- In situ cryo-ET (Dictyostelium): some vaults sit on ER and nuclear-envelope membranes,
  and some enclose ribosomes [PMID:42014721].
- Anthropic research post (Nov 2026, "Investigating vault particles with Claude"):
  MVP-like proteins occur in some bacteria and phages, and several form vault-like
  particles in E. coli. A coenzyme A-like ligand was seen in one phage vault (L05). This
  is not yet peer reviewed and is not cited in the review.

## Curation decisions

- Generic protein binding rows (10): REMOVE under the protein-binding policy. The SHP-2
  and SRC interactions stay in the review through the protein phosphatase binding and
  protein kinase binding rows.
- Identical protein binding (4 rows, interactome screens): ACCEPT. Self-assembly is the
  defining property of MVP.
- NEW GO:0005198 structural molecule activity (IDA, PMID:40691181) as the core MF;
  proposed new CC term "vault complex" under GO:1990904.
- GO:0072376 protein activation cascade (IEA from the mouse IMP, PMID:15133037): REMOVE,
  and a source defect was recorded. It is a zymogen-cascade term used for a Ras/ERK effect.
- GO:0008283 cell population proliferation (IEA from the same mouse IMP): over-annotated.
- Reactome neutrophil degranulation rows (extracellular region, secretory granule lumen,
  ficolin-1-rich granule lumen): over-annotated. These are cargo lists drawn from
  proteomics, and MVP has no signal peptide.
- Protein transport (NAS): over-annotated; this is a hypothesis, not a demonstrated
  function.
- Signalling, nucleus, nuclear pore, perinuclear, cytoskeleton, membrane and exosome
  rows: KEEP_AS_NON_CORE.
