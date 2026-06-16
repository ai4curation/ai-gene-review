---
title: "Structure papers for the prioritized candidates"
---
# Structure papers for the prioritized candidates

For the top functional-insight candidates, the bound ligand/cofactor is only the *clue*;
the **primary structure paper** is where the functional interpretation lives. This brief
records, for a balanced eukaryotic + prokaryotic shortlist, what the structure papers
actually establish and the GO-annotation implication.

> Source attribution: article metadata below was retrieved from **PubMed**. DOIs are linked
> per reference.

## Important caveat: auto-assigned citations need verifying

`pdb_gene_enriched.tsv:structure_papers` lists the RCSB **per-entry primary citation** for
the ligand/cofactor-bearing structures. That is the paper that *deposited that entry* — which
is frequently a downstream ligand/inhibitor or methods study, **not** the definitive
structure-determination or functional paper. Verified examples of this drift:

- **SPR** → `PMID:31740247`, `PMID:31244106` are *inhibitor-discovery* papers (virtual /
  fragment screening), not the original SPR structure paper. They still confirm the enzyme
  (NADP-dependent sepiapterin reductase, an analgesic drug target) but should not be cited as
  "the structure of SPR."
- **cbh1 (HYPJE Cel7A)** → `PMID:37666405`, `PMID:30255965` are glycosylation / propranolol-
  binding NMR studies, not the cellobiohydrolase function paper.
- **merA (PSEAI)** → `PMID:20828160` is an NMR study of the **N-terminal NmerA HMA domain**
  (metal-binding Cys pKa), not the FAD/NADP catalytic-core structure that carries the cofactor.

By contrast, several auto-citations *are* the definitive paper (XYL1, psaC, IDH3, ATAD1, pcaF,
COX6B1, CFAP61). **Verify each PMID against the gene before citing it in a review** — this is
the "verify, don't trust" rule from CLAUDE.md, and the data above makes the failure mode
concrete.

## Eukaryotic shortlist (verified)

### human IDH3B (O43837) — β subunit of NAD-dependent isocitrate dehydrogenase
Currently IEA-only MF in our cache. Crystal structures of the human IDH3 (αβαγ) heterooctamer
and αβ/αγ heterodimers, captured with **NAD, NADH, ADP, Ca²⁺ and a pseudo-Michaelis complex**,
establish IDH3B as the **structural/regulatory β subunit** that builds the catalytic interface
and the (pseudo-)allosteric sites of the TCA-cycle enzyme; the holoenzyme is allosterically
activated by citrate/ADP and inhibited by NADH/ATP (PubMed: Chen et al. 2022, J Biol Chem,
[DOI](https://doi.org/10.1016/j.jbc.2022.102695); Sun et al. 2019, J Biol Chem,
[DOI](https://doi.org/10.1074/jbc.RA119.010099)).
*GO implication*: supports `isocitrate dehydrogenase (NAD+) activity` / NAD binding **at the
complex level** and **protein-complex membership** (IDH3 octamer); useful for distinguishing
the catalytic vs regulatory contribution of the β subunit.

### human ATAD1 (Q8NBU5) — mitochondrial AAA+ membrane-protein extractase
IEA-leaning MF. Near-atomic cryo-EM of human ATAD1 (Msp1 ortholog) **bound to a peptide
substrate, with ATP/ADP**, shows a hexameric AAA+ unfoldase that grips substrate in its
central pore via conserved aromatic pore-loop residues and **extracts mislocalized
tail-anchored membrane proteins from the mitochondrial outer membrane** (PubMed: Wang et al.
2022, eLife, [DOI](https://doi.org/10.7554/eLife.73941)).
*GO implication*: grounds `ATPase activity` + `protein unfolding`/membrane-protein extraction
and mitochondrial protein-quality-control BP — beyond a generic "ATP binding" IEA.

### PICST XYL1 (P31867) — NADPH-dependent D-xylose reductase
No experimental GO in cache. 1.95 Å structure, including the **NADPH-bound** closed state,
defines an aldo-keto-reductase that reduces D-xylose; the paper also shows phylogenetically
that bacterial/archaeal "XR" annotations likely lack true XR activity, while the yeast/fungal
clade (incl. SsXR) are bona fide xylose reductases (PubMed: Son et al. 2018, Sci Rep,
[DOI](https://doi.org/10.1038/s41598-018-35703-x)).
*GO implication*: supports `D-xylose reductase (NADPH) activity` and xylose catabolism;
the phylogenetic point is directly relevant to over-propagated XR annotations elsewhere.

### CHLRE psaC (Q00914) — Photosystem I [4Fe-4S] electron-acceptor subunit
No experimental GO in cache. Cryo-EM of the *Chlamydomonas* Photosystem I supercomplex resolves
psaC carrying the terminal **[4Fe-4S] clusters (F_A/F_B)** that pass electrons to ferredoxin
(PubMed: Schwartz et al. 2023, Biomolecules,
[DOI](https://doi.org/10.3390/biom13030537)).
*GO implication*: supports `4 iron, 4 sulfur cluster binding`, `electron transfer activity`,
and `photosystem I` complex membership.

### human COX6B1 (P14854) — cytochrome c oxidase (complex IV) subunit
3.3 Å cryo-EM of the intact 14-subunit human complex IV places COX6B1 in the assembled enzyme
(PubMed: Zong et al. 2018, Cell Res,
[DOI](https://doi.org/10.1038/s41422-018-0071-1)).
*GO implication*: supports `respiratory chain complex IV` membership and its role in oxidative
phosphorylation.

### human SPR (P35270) — sepiapterin reductase (NADPH; BH4 biosynthesis)
IEA-leaning MF. Multiple ligand-bound crystal structures (NADP + sepiapterin pocket inhibitors)
confirm an **NADPH-dependent sepiapterin reductase**, the terminal enzyme of tetrahydrobiopterin
(BH4) biosynthesis and an analgesic drug target (PubMed: Alen et al. 2019, J Med Chem,
[DOI](https://doi.org/10.1021/acs.jmedchem.9b00218)). *Note: cited entries are inhibitor papers,
not the original apo structure.*
*GO implication*: supports `sepiapterin reductase activity` and BH4 biosynthesis.

### ARATH COI1 (O04197) — jasmonate co-receptor F-box protein
Structure of the COI1–JAZ co-receptor with **jasmonoyl-isoleucine / inositol pentakisphosphate**
defines COI1 as the F-box receptor whose ligand-binding completes the jasmonate hormone sensor
(PubMed: Sheard et al. 2010, Nature, [DOI](https://doi.org/10.1038/nature09430); RCSB lists
`PMID:20927106`).
*GO implication*: supports `jasmonic acid receptor activity` / hormone perception and SCF^COI1
complex membership.

## Prokaryotic / other shortlist (verified)

### PSEPK pcaF (Q88N39) — degradative β-ketoadipyl-CoA thiolase
No experimental GO in cache. CoA- and acyl-CoA–bound structures (incl. a trapped covalent
intermediate) distinguish **degradative β-ketoadipyl-CoA thiolase** from biosynthetic
acetoacetyl-CoA thiolase by active-site architecture and a long substrate tunnel + "covering
loop" unique to the degradative class (PubMed: Bhaskar et al. 2020, J Struct Biol X,
[DOI](https://doi.org/10.1016/j.yjsbx.2019.100018)).
*GO implication*: supports the **degradative** thiolase MF (β-ketoadipyl-CoA thiolase) in the
β-ketoadipate / protocatechuate degradation pathway — a precise call the structure enables.

### METAC mcrA (Q8THH1) — methyl-coenzyme M reductase α subunit
IEA-only MF. Structure of the Gln-methylated MCR captured with the **heterodisulfide reaction
product** (and the F430 nickel hydrocorrinoid cofactor) supports MCR as the terminal
methanogenesis catalyst (PubMed: Rodriguez Carrero et al. 2025, mBio,
[DOI](https://doi.org/10.1128/mbio.03546-24)). *Note: this paper centers on the MgmA modifying
enzyme; the canonical MCR catalytic structure is Ermler et al. 1997 — cite that for the core
function.*
*GO implication*: supports `coenzyme-B sulfoethylthiotransferase` (MCR) activity, F430 binding,
and methanogenesis.

### PSEAI merA (P00392) — mercuric reductase
IEA-only MF. FAD/NADP-bound catalytic-core entries support a **mercuric(II) reductase**
(pyridine-nucleotide-disulfide oxidoreductase) reducing Hg²⁺ to Hg⁰; the NmerA N-terminal
HMA domain (the deposited NMR entry) handles Hg²⁺ delivery to the core (PubMed: Ledwidge et al.
2010, Biochemistry, [DOI](https://doi.org/10.1021/bi100537f)).
*GO implication*: supports `mercury(II) reductase activity`, FAD/NADP binding, and mercury
detoxification — but cite the catalytic-core structure, not only the NmerA-domain paper.

## How structure papers feed the review

For any gene taken to full review, the workflow is: (1) read the verified structure paper(s)
for the **bound ligand → mechanism** statement; (2) cite the paper + PDB id as evidence in the
relevant `existing_annotations[].review.reason`; (3) record the reference (with
`reference_review.correctness`) in the top-level `references:` list; (4) where the auto-assigned
PMID is peripheral, substitute the definitive paper and note the discrepancy.
