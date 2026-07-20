# ITIH1 review notes

## Review scope and provenance

- Target: human **ITIH1**, UniProtKB **P19827** (inter-alpha-trypsin inhibitor heavy chain H1).
- Review date: 2026-07-18.
- The GOA stub contained 14 grouped annotations derived from 15 source rows; every group was reviewed manually.
- `just deep-research-falcon human ITIH1 --fallback perplexity-lite` was attempted. Falcon/Edison returned HTTP 402 and Perplexity-lite returned HTTP 401, so no provider-named deep-research file was created. The synthesis below instead uses the reviewed UniProt record and cached primary literature.

## Protein identity and architecture

ITIH1 is a liver-enriched secreted precursor. UniProt assigns a signal peptide (residues 1-27), a propeptide (28-34), the mature heavy chain (35-672), and a C-terminal propeptide (673-911). The mature chain contains VIT and VWFA domains. Its C-terminal Asp672 is ester-linked to the chondroitin-4-sulfate chain of bikunin after processing [UniProtKB:P19827, `CC   -!- PTM: Heavy chains are linked to bikunin via chondroitin 4-sulfate`].

The plasma inter-alpha-inhibitor complex contains ITIH1/HC1, ITIH2/HC2, and bikunin. The component-level distinction is decisive: the heavy chains are noninhibitory, while the 30-kDa bikunin chain supplies trypsin-inhibitor activity [PMID:2476436, "Inter-alpha-trypsin inhibitor contains noninhibitory heavy chains of 65,000 and 70,000 Da"]. Therefore ITIH1 must not inherit the serine-protease inhibitor activity of the assembled complex.

## Direct functional evidence

- Serum-derived hyaluronan-associated proteins were identified as HC2 and HC1. Mapping of resistant fragments implicated the C-terminal half of inter-alpha-inhibitor heavy chains in HA association [PMID:7504674, "participation of the COOH-terminal half of ITI with an amphipathic alpha helix structure in the HA binding"].
- HC1 and other bikunin-complex heavy chains can be transferred covalently from bikunin chondroitin sulfate to hyaluronan through TSG-6/HC2-mediated transesterification [PMID:20463016, "can be transferred to different hyaluronan (HA) molecules by TSG-6/HC2"]. This establishes a direct role in hyaluronan metabolism and the HA-rich extracellular matrix.
- Recombinant human HC1 binds the TSG-6 CUB domain. The HC1 VWFA domain contains a magnesium-bearing MIDAS motif, and D298A abolishes metal binding and the CUB-domain interaction [PMID:26468290, "its von Willebrand factor A domain contains a Mg2+-containing MIDAS motif"].
- The 1987 cDNA paper stated only that HC1 contained *potential* calcium-binding sites [PMID:2446322, "The H chain contains potential calcium-binding sites"]. It did not demonstrate calcium binding. Modern direct evidence instead supports magnesium ion binding, so the calcium term is modified rather than retained.
- Chondroitin sulfate covalently cross-links bikunin, HC1, and HC2 [PMID:7513643, "the different peptide chains constituting ITI are associated by the new cross-link described as the protein-glycosaminoglycan-protein cross-link"]. This is covalent assembly, not evidence for a broad intrinsic carbohydrate-binding activity. Independent HC1/HA work supports the more specific hyaluronic acid binding term.
- TSG-6-driven release of free bikunin increases antiprotease activity, and free bikunin rather than HC-associated bikunin accounts for the inhibition [PMID:16873769, "bikunin in its free state, but not when associated with HCs, is a relevant protease inhibitor"].

## Annotation decisions

| Source term | Decision | Rationale |
|---|---|---|
| serine-type endopeptidase inhibitor activity | REMOVE | Complex-to-component conflation; HC1 is explicitly noninhibitory. |
| extracellular region (IEA and NAS) | MODIFY to extracellular space | Correct but unnecessarily broad for a soluble secreted plasma protein. The two duplicate terms receive the same action. |
| hyaluronan metabolic process | ACCEPT | HC1 is transferred onto HA and participates in the dynamic HC-HA system. |
| carbohydrate binding | MODIFY to hyaluronic acid binding | The source establishes covalent glycosaminoglycan assembly; independent direct studies identify the biologically specific HA interaction. |
| protein binding (three IPI records) | MARK_AS_OVER_ANNOTATED | TNFAIP6/bikunin interactions are real, but generic protein binding is uninformative and no partner-specific GO MF exists. |
| hyaluronic acid binding | ACCEPT | Direct HC/HA evidence and mapped HA-associated region. |
| extracellular matrix (two HDA records) | ACCEPT | Proteomic detection agrees with the established covalent HC1-HA matrix pool. |
| extracellular exosome | KEEP_AS_NON_CORE | Retain the HDA observation; an abundant soluble plasma protein may co-purify, so it is not a defining location. |
| blood microparticle | KEEP_AS_NON_CORE | Retain the HDA observation without making microparticle association a core location. |
| calcium ion binding | MODIFY to magnesium ion binding | Old sequence prediction did not establish calcium binding; recombinant human HC1 directly contains a Mg2+-bearing MIDAS motif. |

## Curation boundaries

- ITIH1 is a substrate/structural heavy chain in the TSG-6 reaction, not the HC transferase; catalytic transferase activity belongs to TSG-6.
- Covalent attachment of HC1 to HA should not be described as HA biosynthesis or degradation. The broad existing hyaluronan metabolic process term is retained.
- Mouse cumulus-oocyte phenotypes demonstrate the biological importance of the IalphaI/TSG-6/HA system, but they do not by themselves establish an ITIH1-specific human reproductive-process annotation because IalphaI contains both HC1 and HC2.
- Exosome, microparticle, and tumor-ECM proteomics support occurrence in sampled fractions but do not define a distinct vesicle function.

## Open questions

- Does HC1 have noncovalent HA affinity before or after transfer, or does the current GO binding annotation primarily reflect covalent HC-HA attachment?
- Which human tissues preferentially use HC1 versus HC2 in HC-HA matrices, and do the two heavy chains impart different mechanics or receptor interactions?
- Do the three annotated ITIH1 isoforms differ in secretion, propeptide processing, bikunin loading, or TSG-6-mediated transfer?
