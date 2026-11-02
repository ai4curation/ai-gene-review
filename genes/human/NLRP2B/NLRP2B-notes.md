# NLRP2B (P0DMW2, POP4) review notes

## 2026-10-08 - MICROPROTEINS Tier 2 review (claude-code)

**Identity.** 45-aa pyrin-domain fragment (first two PYD helices) encoded by a processed
retrocopy of an NLRP2/NLRP7-like gene on Xp11.21. HGNC: `gene with protein product`
(prev. symbol NLRP2P; aliases NOD24, NALP2P, CLRX.1, POP4). UniProt PE2 (transcript level),
MANE Select ENST00000434992.1. HPA: protein not detected. PAN-GO: 0 IBA annotations.
Not an alt-ORF of another gene, so the standard folder convention applies.

**Literature.** PubMed search (NLRP2B OR NLRP2P OR "pyrin-only protein 4") returns only
PMID:24871464 and a 2013 review predating it (PMID:24062743, not cited). One-paper gene.

Key findings from PMID:24871464 (full text, PMC4311403):
- Locus is processed-pseudogene-like but keeps an ORF under purifying selection
  [PMID:24871464 "The entire NLRP2P coding region appears to be under purifying selection regardless of which two species were compared (Fig. 2A–C)."]
- Structure: only helices 1-2 of a PYD [PMID:24871464 "Since POP4 (45 a.a.) is shorter than POP2 (97 a.a.) and other Pyrin domains, POP4 likely forms only the first two α-helices."]
- mRNA induced by LPS in THP-1; absent from HeLa and A293T
  [PMID:24871464 "Despite detection in all tissue types tested, NLRP2P was not detectable in epithelial (HeLa) or fibroblast-like (A293T) cells"]
- Protein itself was never seen by western blot; only intracellular FLAG staining
  [PMID:24871464 "Although the predicted molecular mass of POP4, approximately 5 kDa, likely accounts for our lack of detection by western blot, intracellular POP4 was detectable (Fig. 3B, right panel)."]
- NF-kB: reduces TNF-induced reporter, acts at/downstream of RelA, reduces S536 phosphorylation
  [PMID:24871464 "Together these results strongly suggest that POP4 limits NF-κB phosphorylation of S536 in these cells, thereby reducing transactivation by the p65 TAD1."]
- TLR cytokines: overexpression lowers, siRNA knockdown in THP-1 raises TNF/IL-6
  [PMID:24871464 "In cells with reduced POP4 expression (250 ng siRNA), there was a statistically significant increase in IL-6 and TNFα cytokine release as compared to control cells (Fig. 7E)."]
- No inflammasome inhibition (contrast with POP2)
  [PMID:24871464 "Therefore, POP4 appears not to be an inhibitor of the NLRP3 inflammasome and is unlikely to inhibit other ASC-dependent inflammasomes"]
- Cell cycle / apoptosis: HeLa overexpression, only under CHX (+TNF)
  [PMID:24871464 "Further, apoptosis (as indicated by hypodiploid nuclei) was significantly increased by POP4, but only in the presence of both CHX and TNFα (Fig. 6D)."]

**Decisions.** 11 rows: 9 ACCEPT (4 location, TNF and TLR signalling, S536 phosphorylation,
two NOT rows), 2 KEEP_AS_NON_CORE (apoptosis, cell cycle). No REMOVE: every row is
experimental from a full-text paper and the claims match the data. Caveats recorded:
evidence is mostly overexpression labelled IMP; localisation is of a tagged protein in a
non-expressing line; endogenous protein never detected. No MF assigned (mechanism unknown).
No NEW: the TNF and TLR terms already cover the NF-kB effect; a general NF-kB term
(GO:0043124) raised as a question instead. Comparator: paralog PYDC2/POP2 (Q56P42) carries
the positive versions of both NOT rows (GO:0032691, GO:1900226), so the NOT rows are informative.
