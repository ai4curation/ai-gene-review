# KRTAP17-1 notes

## Session 2026-10-24 (family-batched KRTAP review)

- No OpenScientist or other deep-research report exists for this gene; deep research was not run (per batch instructions). Literature found by PubMed search and cached with `just fetch-pmid`.

- Family context: KAPs are hair-fibre matrix proteins cross-linked to hair keratin IFs [PMID:18721477 "are essential for the formation of rigid and resistant hair shafts through their extensive disulfide bond cross-linking with the abundant cysteine residues of hair keratins or hydrophobic interactions with keratins"]; [PMID:16382671 "play crucial roles in forming a strong hair shaft through a cross-linked network with keratin intermediate filaments (KIF)"].

- Description used: KRTAP17-1 (keratin-associated protein 17-1, KAP17.1) is a small (105 aa) cysteine- and glycine-rich hair keratin-associated protein, cloned from human scalp and encoded in the chromosome 17q12-21 high/ultrahigh sulfur KAP gene cluster that lies within the type I keratin gene domain. Like other KAPs it is a component of the interfilamentous matrix of the hair fibre, in which hair keratin intermediate filaments are embedded and extensively disulfide cross-linked. IgG autoreactivity against KRTAP17-1 has been reported in a subset of atopic dermatitis patients, a finding not linked to its normal structural role.

- Decisions (family-consistent): bare GO:0005515 rows REMOVE (HuRI/Y2H promiscuous preys); cytosol (ARBA IEA, Reactome TAS) KEEP_AS_NON_CORE; keratin filament ACCEPT or NEW; structural molecule activity MODIFY (or NEW) to GO:0030281 structural constituent of cutaneous appendage (verified in OLS; is_a GO:0005198; definition covers hairs). Hair keratins are conventionally IBA-annotated to GO:0030280 skin epidermis instead; flagged as a consistency question.

- NEW BP GO:0031424 keratinization (participation as structural/scaffold constituent of the cornified hair shaft [Reactome:R-HSA-6809663 "involved in the formation of cornified, resilient hair shafts"]; comparator check: KRT81/KRT85/KRT86 carry it by IBA (QuickGO), KRTAP6-3 and sheep KRTAP6-1 by IEA). Hair cycle / hair follicle development deliberately not used. Kept consistent with the sibling KRTAP batches.

- Gene-specific sources: PMID:18721477, PMID:16382671, PMID:16939781, PMID:11279113

- Human association (not normal function): IgG autoreactivity to KRTAP17-1 in a subset of atopic dermatitis patients [PMID:30728947 "Forty-nine percent of the AD patients showed increased IgG-reactivity to any of the four antigens representing keratin associated protein 17-1 (KRTAP17-1)"].
- Composition (simple residue count of the UniProt sequence): ~36% Cys, ~30% Gly, i.e. an ultrahigh-cysteine KAP.
