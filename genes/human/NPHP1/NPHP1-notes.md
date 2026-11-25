# NPHP1 notes

Deep research: skipped. Falcon times out after 600 s in this environment and perplexity-lite is not installed. The review is based on cached publications, UniProt O15259 and PubMed searches. No deep-research file was generated.

## Key findings
- NPHP1 localizes to the transition zone of renal, respiratory and photoreceptor connecting cilia [PMID:16885411 "nephrocystin specifically localizes at the ciliary base to the transition zone of renal and respiratory cilia and to photoreceptor connecting cilia"].
- NPHP1 is not required for ciliogenesis on its own [PMID:16885411 "Cilia formation is not altered in primary nephrocystin-deficient respiratory cells"].
- With NPHP4 and RPGRIP1L it forms the NPHP1-4-8 module, found at cell-cell contacts and at the transition zone [PMID:21565611 "these NPHP proteins accumulate to cell-cell contacts, mostly basolateral of tight junctions"].
- It acts redundantly with the MKS module [PMID:28401750 "combining the disruption of a MKS complex component with the disruption of NPHP1 or NPHP4 severely disrupted ciliogenesis, and ciliary functions"]. The worm modules are described in [PMID:21422230].
- It is needed for timely tight-junction formation [PMID:19755384 "nephrocystins-1 and -4 are required for the proper timing of tight junctional establishment"].
- Its SH3 domain binds proline-rich motifs: in polycystin-1 [PMID:20856870] and in ADAM12/15/19 [PMID:25825872]. Generic protein-binding rows from these papers were changed to GO:0070064 proline-rich region binding. Other protein-binding rows were removed as uninformative.

## Decisions
- The structural molecule activity (NAS) row was removed as a placeholder.
- No specific molecular function is assigned to the transition-zone core function; molecular_function is left unset.
- Visual behavior (NAS) was removed because it is a disease phenotype, not a process NPHP1 carries out.
