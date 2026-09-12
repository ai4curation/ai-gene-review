# DNAJC5 (Q9H3Z4) research notes

## Identity
- DnaJ homolog subfamily C member 5; cysteine string protein alpha (CSPalpha/CSP); CLN4.
- 198 aa. J domain (aa 13-82) [file:human/DNAJC5/DNAJC5-uniprot.txt "DOMAIN 13..82 /note=\"J\""].
- Cysteine-string domain (aa ~113-136), heavily palmitoylated, mediates membrane attachment [uniprot PTM "Palmitoylated... Palmitoylation occurs probably in the cysteine-rich domain and regulates DNAJC5 membrane attachment"].

## Function (UniProt FUNCTION, By similarity)
- "Acts as a general chaperone in regulated exocytosis ... Acts as a co-chaperone for the SNARE protein SNAP-25 ... Involved in the calcium-mediated control of a late stage of exocytosis ... important role in presynaptic function ... calcium-dependent neurotransmitter release at nerve endings."
- Interacts with HSC70/HSPA8 and SGTA chaperone complex; with synaptotagmins SYT1/5/7/9 forming a complex with SNAP25; with ZDHHC13/ZDHHC17 (palmitoyltransferases).
- Core MF: J-domain co-chaperone (HSP70/HSC70 co-chaperone) — stimulates HSC70 ATPase, chaperones the SNARE assembly machinery (SNAP-25). This is the bona fide "ATPase activator / Hsp70 protein binding / chaperone" function. Distinct from generic protein folding (downstream).

## Localization
- Synaptic vesicle / secretory vesicle membrane, presynapse; plasma membrane; chromaffin granule membrane. Palmitoylation-dependent membrane anchor.
- IEA melanosome (PMID:17081065 mass spec) and HDA mitochondrion (PMID:20833797), lysosomal membrane (PMID:17897319) — large-scale proteomics; non-core/peripheral.
- Reactome neutrophil degranulation (azurophil/specific granule membrane) — peripheral, leukocyte context.

## Disease
- Autosomal-dominant adult-onset neuronal ceroid lipofuscinosis (CLN4B / ANCL / Kufs type) caused by Leu115Arg and Leu116del in the cysteine-string domain [PMID:21820099]. Mutants: near absence of palmitoylated monomeric forms; high MW aggregates [uniprot VARIANT].

## PTM / regulation
- Ser-10 phosphorylation (PKA) triggers order-to-disorder switch, reduces syntaxin/synaptotagmin binding without altering HSC70 interaction [PMID:27452402 from uniprot].

## Curation judgment
- Core MF: HSP70/HSC70 co-chaperone (ATPase activator / Hsp70 protein binding); the "ATP-dependent protein binding" (GO:0043008, IEA from rat ortholog) reflects this. protein folding KEEP_AS_NON_CORE (downstream). presynapse / synaptic vesicle membrane: core localizations -> ACCEPT. regulated exocytosis / synaptic vesicle cycle: genuine BP -> ACCEPT/KEEP_AS_NON_CORE.
- The two protein binding IPI are with ZDHHC17 (Q8IUH5) -> the informative MF is the ZDHHC17/palmitoyltransferase interaction; bare protein binding KEEP_AS_NON_CORE.
- Melanosome/mitochondrion/lysosomal membrane/granule membranes: KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED depending on strength; large-scale proteomics localizations not reflecting core synaptic role.
