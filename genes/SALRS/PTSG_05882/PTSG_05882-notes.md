# PTSG_05882 (Salpingoeca rosetta, F2UD23) - curation notes

**Automated deep research was unavailable** (no deep-research provider key in this
environment), so no `-deep-research-*.md` file exists. These notes were written on
2026-10-02 from the cached publications, the UniProt record and the shared analysis in
`genes/MONBE/MBCDH12/MBCDH12-bioinformatics/` (PANTHER tree API, InterPro and UniProt REST).
The four choanoflagellate cadherins PTSG_05882, PTSG_06458, PTSG_11235 and MONBE MBCDH12 were
reviewed together in one session for consistency.

## Identity and architecture

- F2UD23, TrEMBL, 1856 aa, ORF PTSG_05882, EMBL EGD74518.1. "Uncharacterized protein".
- Signal peptide 1-25. VWFD 149-356, EGF_Teneurin, 8 cadherin (PS50268) domains 703-1597,
  TM 1623-1645, cytoplasmic SH2 1692-1795 (UniProt features).
- The SH2 domain keeps the FLVR-motif arginine (FIIRDY)
  [file:MONBE/MBCDH12/MBCDH12-bioinformatics/RESULTS.md "Both SH2 domains keep the arginine of the FLVR"].
- The EC repeats have no DXNDN-type calcium motif and no PROSITE CADHERIN_1 match. UniProt
  carries a "lacks conserved residue(s)" caution, so the repeats are divergent.
- There is no Pfam PF01049 (Cadherin_C), the classical-cadherin beta-catenin-binding domain
  [file:MONBE/MBCDH12/MBCDH12-bioinformatics/RESULTS.md "None of the four has the classical-cadherin cytoplasmic domain through which classical"].
- The architecture (VWD, EGF, EC, TM, SH2) matches *M. brevicollis* MBCDH12 (A9V8Y4). This is a
  possible ortholog pair. PANTHER puts them in different subfamilies (SF422 and SF438).

## Literature

- There is no experimental literature on this protein. A search of the cached publications
  for PTSG_05882 and EGD74518 found no hits.
- Choanoflagellates have no classical cadherins
  [PMID:27189570 "Choanoflagellates, which are thought to be the closest extant eukaryotic relatives of metazoans, also lack classical cadherins"].
- S. rosetta colonies have no adherens junctions
  [PMID:22837400 "even in colony-forming S. rosetta , adjacent cells are linked by cytoplasmic bridges and lack structures that resemble the cadherin-based adherens junctions of metazoans"].
- Possible premetazoan cadherin roles have been proposed, but none tested
  [PMID:22837400 "cadherins in unicellular lineages could have adhesive functions other than the regulation of stable cell-cell adhesion, such as during bacterial prey capture, attachment to ECM, attachment to environmental substrates, or gamete recognition"].

## Track C: propagation

- All 10 TreeGrafter rows cite PANTHER:PTN000616280.
  - PAINT records this node at taxon:33213 (Bilateria). The PANTHER tree labels it
    "Bilateria", and all 524 of its leaves are bilaterian.
  - Six IBDs sit on the node itself (adherens junction, cell morphogenesis, cell-cell junction
    assembly, Ca-dependent cell-cell adhesion, AJ organization, cadherin-mediated adhesion).
  - Four come from the family root PTN008601603 "Metazoa-Choanoflagellida" (beta-catenin
    binding, catenin complex, cadherin binding, cell migration).
- *S. rosetta* is not a reference genome, so TreeGrafter grafts F2UD23 onto the Bilateria
  node, outside its own clade.
- Actions:
  - REMOVE: adherens junction, cell-cell junction assembly, beta-catenin binding, catenin
    complex, AJ organization. These need a Cadherin_C domain or an adherens junction, and
    both are absent.
  - MARK_AS_OVER_ANNOTATED: cell morphogenesis, cell migration, cadherin binding,
    Ca-dependent cell-cell adhesion and cadherin-mediated cell-cell adhesion. These are not
    impossible for a unicellular cadherin, but they are untested and rest on donor biology
    from animal tissues.
- InterPro2GO homophilic and cell-cell adhesion: MARK_AS_OVER_ANNOTATED (TERM_SCOPING).
- Calcium ion binding: UNDECIDED, because the calcium motifs are not canonical.
- No SH2-derived GO rows exist. Phosphotyrosine binding is a reasonable domain-level
  prediction, but it was not added as NEW, because there are no experiments and this review
  adds no NEW rows.
