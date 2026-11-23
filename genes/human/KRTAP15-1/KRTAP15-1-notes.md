# KRTAP15-1 notes

## Session 2026-10-24 (family-batched KRTAP review)

- No OpenScientist or other deep-research report exists for this gene; deep research was not run (per batch instructions). Literature found by PubMed search and cached with `just fetch-pmid`.

- Family context: KAPs are hair-fibre matrix proteins cross-linked to hair keratin IFs [PMID:18721477 "are essential for the formation of rigid and resistant hair shafts through their extensive disulfide bond cross-linking with the abundant cysteine residues of hair keratins or hydrophobic interactions with keratins"]; [PMID:16382671 "play crucial roles in forming a strong hair shaft through a cross-linked network with keratin intermediate filaments (KIF)"].

- Description used: KRTAP15-1 (keratin-associated protein 15-1, KAP15.1) is a small (137 aa) high-sulfur hair keratin-associated protein of the KAP15 family (PMG/KRTAP_PMG family), encoded in the chromosome 21q22.1 KAP gene domain. KAPs form the interfilamentous matrix of the hair fibre, in which hair keratin intermediate filaments are embedded and cross-linked by disulfide bonds to give a rigid, resistant hair shaft. In goats the orthologous KRTAP15-1 is expressed in secondary (cashmere) hair follicles but not in internal organs, and its sequence variants are associated with cashmere mean fibre diameter.

- Decisions (family-consistent): bare GO:0005515 rows REMOVE (HuRI/Y2H promiscuous preys); cytosol (ARBA IEA, Reactome TAS) KEEP_AS_NON_CORE; keratin filament ACCEPT or NEW; structural molecule activity MODIFY (or NEW) to GO:0030281 structural constituent of cutaneous appendage (verified in OLS; is_a GO:0005198; definition covers hairs). Hair keratins are conventionally IBA-annotated to GO:0030280 skin epidermis instead; flagged as a consistency question.

- NEW BP GO:0031424 keratinization (participation as structural/scaffold constituent of the cornified hair shaft [Reactome:R-HSA-6809663 "involved in the formation of cornified, resilient hair shafts"]; comparator check: KRT81/KRT85/KRT86 carry it by IBA (QuickGO), KRTAP6-3 and sheep KRTAP6-1 by IEA). Hair cycle / hair follicle development deliberately not used. Kept consistent with the sibling KRTAP batches.

- Gene-specific sources: PMID:18721477, PMID:16382671, PMID:16939781, PMID:12359730, PMID:31807622
