# ASDURF (L0R819) review notes

## 2026-10-03 — initial review (MICROPROTEINS Tier 2)

**Identity.** ASDURF ("ASNSD1 upstream open reading frame protein", HGNC:53619) is a
96-aa peptide encoded by an upstream ORF in the 5' leader of the ASNSD1 mRNA. It is a
separate UniProt entry (L0R819) with its own HGNC symbol, so it has its own folder.
UniProt lists the host ASNSD1 protein (Q9NWL6) as the "external" alternative product.

**Literature found (PubMed E-utilities, 2026-10-03).** Query
`ASDURF OR "ASNSD1 uORF" OR (ASNSD1 AND (uORF OR upstream open reading frame))` returned 6
hits; the relevant ones are PMID:23160002, PMID:31738558, PMID:38176414 (+ bioRxiv
preprint PMID:37205492 of the same work) and the Mol Cell preview PMID:38242097. A
`PAQosome` query (18 hits) found no further ASDURF-specific primary work.

### Discovery / localization — PMID:23160002 (Slavoff et al. 2013, full text)
- Detected by peptidomics in K562 as "ASNSD1-SEP"; quantified by isotope dilution
  [PMID:23160002 "examined the cellular concentrations (K562 cells) of three selected SEPs (ASNSD1-SEP, PHF19-SEP and H2AFx-SEP)"].
- FLAG-tagged construct with native UTRs gives cytoplasmic signal in HEK293T
  [PMID:23160002 "all produced cytoplasmically localized polypeptides, as detected by anti-FLAG immunofluorescence in transfected HEK293T cells"].
  Overexpression with tag; fine for a broad CC term.

### PAQosome subunit — PMID:31738558 (Cloutier et al. 2020, J Proteome Res; abstract only)
- [PMID:31738558 "ASDURF, a recently discovered upstream open reading frame (uORF) in the 5' UTR of ASNSD1 mRNA, encodes the 12th subunit of the PAQosome"]
- [PMID:31738558 "assembles with the five known subunits of the prefoldin-like module of the PAQosome to form a heterohexameric prefoldin-like complex"]
- [PMID:31738558 "ASDURF displays significant structural homology to β-prefoldins"]
- Basis of ComplexPortal CPX-6145 (paqosome_human) annotations. Full text not cached;
  defer to ComplexPortal curators.

### Medulloblastoma dependency — PMID:38176414 (Hofman et al. 2024 Mol Cell, full text)
- CRISPR screens of non-canonical ORFs; ASNSD1-uORF KO reduces viability of MYC-driven
  medulloblastoma lines, rescued by WT but not start-site-mutant cDNA.
- Co-IP/MS with prefoldin subunits, endogenous co-IP with PFDN6, GST pulldown
  [PMID:38176414 "purified ASNSD1-uORF tagged with a Glutathione S Transferase (GST) tag showed direct interactions with the PFDL complex"].
- DepMap/PRISM co-dependency clusters it with PFDL not canonical PFD
  [PMID:38176414 "ASNSD1-uORF was strongly associated with the PFDL but not the PFD complex"].
- KO of ASNSD1-uORF or PFDN2 gives an overlapping post-transcriptional proteome change
  (cell-cycle proteins), with little RNA change. Actin/tubulin unaffected.
- Interpretation: independent confirmation of PFDL/PAQosome membership. Cancer cell
  survival is a context-specific dependency, not a GO BP to assert.

### Caller's context check
- Chen et al. 2020 Science (PMID:32139545, cached full text) does **not** mention ASNSD1 or
  ASDURF in its cached text; it did not report the PAQosome association. The PAQosome
  finding is Cloutier et al. 2020 (Coulombe lab), and the CRISPR-screen context is Hofman
  et al. 2024 (Prensner lab). Not cited in the review.

### GOA decisions
| term | ev | action |
|---|---|---|
| GO:0005737 cytoplasm | EXP PMID:23160002 | ACCEPT |
| GO:0005737 cytoplasm | IEA SubCell | ACCEPT |
| GO:0050821 protein stabilization | NAS ComplexPortal | KEEP_AS_NON_CORE (complex-level blanket annotation, given to all 12 subunits; same call as PFDN2 review) |
| GO:1990062 RPAP3/R2TP/prefoldin-like complex | IPI PMID:31738558 | ACCEPT (core) |

- No MF: chaperone activity of the prefoldin-like module has not been shown for ASDURF
  itself; GO:0051082 is obsolete. Bare protein binding not used.
- No NEW terms. Prefoldin complex GO:0016272 not proposed — Hofman's data argue PFDL, not PFD.
