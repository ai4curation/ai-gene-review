# slc7a10b notes

## Setup and provenance

- Fetched with `just fetch-gene` on E7FE11 (TrEMBL, 517 aa); 11 GOA rows (5 IBA, 5 IEA, 1 IMP from PMID:33408126).
  ZFIN ZDB-GENE-121105-2, Ensembl ENSDARG00000051730, chromosome 25.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is invalid. Literature
  searched by hand via Europe PMC (see `../slc7a10a/slc7a10a-notes.md` for queries).
- DANRE_DUPLICATION batch 4, random draw 18 (seed 20260928); paralog slc7a10a. Pair analysis in
  `../slc7a10a/slc7a10a-bioinformatics/`.

## Zebrafish literature

- Obesity model: slc7a10b loss of function accelerates diet-induced weight gain
  [PMID:33408126 "Concordantly, loss of Slc7a10 function in zebrafish in vivo accelerates diet-induced body weight gain and adipocyte enlargement."].
  The primary paper is cached as abstract only. The same group's review gives details:
  [PMID:36172277 "To evaluate a possible causal role of altered SLC7A10 expression in obesity, an Slc7a10b Zebrafish loss-of-function model was subjected to overfeeding for 2 months (Jersin et al., 2021)."];
  [PMID:36172277 "Compared to wildtypes, the fish with impaired Slc7a10b function gained 38% more body weight and had on average 49% larger visceral adipocytes"];
  [PMID:36172277 "Because two isoforms of Slc7a10 exist in zebrafish (Slc7a10a as well as Slc7a10b), this model should be considered a partial global knockout of Slc7a10."].
  The copy was chosen for sequence identity, not expression; slc7a10a was not studied and paralog compensation was
  not measured.
- Meninges scRNA-seq: SLC7A10B among transporters enriched in arachnoid cells
  [PMID:35805100 "solute transporter Slc6a13 (GABA transporter), and many other SLC transporters (SLC1A2B, SLC1A3B, SLC3A2A SLC4A4, SLC6A1B, SLC6A9, SLC6A10, SLC7A10B, SLC27A1B) (Figure 6)."].
- No ZFIN curated expression and no EST profile [PMID:34338990 "slc7a10a (Chr 7)Developmental stage|adultAdult|heart > kidney > brain > eye---slc7a10b (Chr 25)----"].

## Mammalian background

See `../slc7a10a/slc7a10a-notes.md`.

## My analysis

See `../slc7a10a/slc7a10a-bioinformatics/RESULTS.md`: protein conserved at all tested Asc-1 residues; slc7a10b is
the slower-evolving copy; expression low and narrow (brain, eye, bone, testis, early embryo), closer to the gar
pattern than slc7a10a.

## GOA review decisions

- The 10 IBA/IEA rows accepted, as for slc7a10a.
- Energy homeostasis (IMP, acts upstream of or within) kept as non-core: real, copy-specific phenotype, but an
  organism-level consequence of adipocyte amino acid transport.
