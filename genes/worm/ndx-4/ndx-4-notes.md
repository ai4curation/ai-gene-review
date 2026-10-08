# ndx-4 (Y37H9A.6, Q9U2M7) review notes

## Summary of evidence

- Asymmetrical Ap4A hydrolase (Nudix family), the worm counterpart of human NUDT2.
  [PMID:11738085 "It hydrolyses Ap4A with a K(m) of 7 microM and k(cat) of 27 s(-1) producing AMP and ATP as products."]
- Activity also present in adult worm extracts.
  [PMID:11738085 "Asymmetrically cleaving diadenosine 5',5\"'-P(1),P(4)-tetraphosphate (Ap4A) hydrolase activity has been detected in extracts of adult Caenorhabditis elegans"]
- Broad (di)adenosine polyphosphate substrate range (>=4 phosphates), not Ap3A; ATP is always a product.
  [PMID:11738085 "always generating ATP as one of the products"]
- Crystal structures (free, 2.0 A; binary complex, 1.8 A); monomer with Nudix fold.
  [PMID:11937063 "The structures reveal that the enzyme has the mixed alpha/beta fold of the Nudix family"]
- Mutagenesis: Glu56, Glu52, Glu103 catalytic; P1/P4 phosphate contacts sufficient for binding.
  [PMID:12475970 "interactions with the P(1)- and P(4)-phosphates are minimum and sufficient requirements for substrate binding"]
- Secondary in vitro PRPP pyrophosphatase activity using the same active site.
  [PMID:12370170 "Active site mutants of the Caenorhabditis elegans diadenosine tetraphosphate hydrolase had no activity, confirming that the same active site is responsible for nucleotide and PRPP hydrolysis."]

## Curation decisions

- AMP/ADP/ATP biosynthetic process: products of a catabolic reaction; marked over-annotated
  in favour of GO:0015967 diadenosine tetraphosphate catabolic process.
- Apoptotic process (TAS, PMID:11937063): the sentence is speculative ("potentially") background
  in a structure paper; removed.
- Ribose phosphate metabolic process: in vitro family screen only; authors did not consider
  PRPP significant for Ap4A hydrolases; over-annotated. PRPP pyrophosphatase MF kept as non-core.
- No cellular component annotations exist and no localization data were found; none proposed.

## Caveats

All four cached publications are abstract-only (`full_text_available: false`).
