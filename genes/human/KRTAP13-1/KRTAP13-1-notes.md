# KRTAP13-1 notes

## Session 2026-10-24 (family-batched KRTAP review)

- No OpenScientist or other deep-research report exists for this gene; deep research was not run (per batch instructions). Literature found by PubMed search and cached with `just fetch-pmid`.

- Family context: KAPs are hair-fibre matrix proteins cross-linked to hair keratin IFs [PMID:18721477 "are essential for the formation of rigid and resistant hair shafts through their extensive disulfide bond cross-linking with the abundant cysteine residues of hair keratins or hydrophobic interactions with keratins"]; [PMID:16382671 "play crucial roles in forming a strong hair shaft through a cross-linked network with keratin intermediate filaments (KIF)"].

- Description used: KRTAP13-1 (keratin-associated protein 13-1, KAP13.1) is a small (172 aa) high-sulfur hair keratin-associated protein of the KAP13 family (PMG/KRTAP_PMG family), encoded in the chromosome 21q22.1 KAP gene domain. Like other KAPs it is a hair-specific matrix protein: in the hair cortex the hair keratin intermediate filaments are embedded in an interfilamentous matrix of KAPs that become extensively disulfide cross-linked to the cysteine-rich hair keratins, giving the hair shaft its rigidity and resistance. KRTAP13-1 transcripts are weakly expressed in the late matrix and throughout the cortex of the anagen hair follicle. An orthologous KRTAP13-1 gene is present in sheep within a conserved chromosome 1 KAP cluster.

- Decisions (family-consistent): bare GO:0005515 rows REMOVE (HuRI/Y2H promiscuous preys); cytosol (ARBA IEA, Reactome TAS) KEEP_AS_NON_CORE; keratin filament ACCEPT or NEW; structural molecule activity MODIFY (or NEW) to GO:0030281 structural constituent of cutaneous appendage (verified in OLS; is_a GO:0005198; definition covers hairs). Hair keratins are conventionally IBA-annotated to GO:0030280 skin epidermis instead; flagged as a consistency question.

- NEW BP GO:0031424 keratinization (participation as structural/scaffold constituent of the cornified hair shaft [Reactome:R-HSA-6809663 "involved in the formation of cornified, resilient hair shafts"]; comparator check: KRT81/KRT85/KRT86 carry it by IBA (QuickGO), KRTAP6-3 and sheep KRTAP6-1 by IEA). Hair cycle / hair follicle development deliberately not used. Kept consistent with the sibling KRTAP batches.

- Gene-specific sources: PMID:18721477, PMID:16382671, PMID:16939781, PMID:12359730, PMID:39409811

- KRTAP13-1 was listed as a PPI "hub" gene in a Graves disease methylation study (PMID:33617351, not cached/cited); network-derived, not a verified association.
