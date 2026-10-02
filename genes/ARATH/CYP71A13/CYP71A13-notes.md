# CYP71A13 (At2g30770, UniProt O49342) — curation notes

## Identity
- Cytochrome P450 71A13, Arabidopsis thaliana; N-terminal single-pass membrane anchor (UniProt FT TRANSMEM 2..20), heme-thiolate Cys (BINDING 439). PANTHER PTHR47955:SF15 (CYP71A2-like). Tandem paralog of CYP71A12 (At2g30750), ~90% identity [PMID:24151049 "The Arabidopsis P450 CYP71A12 shares 89.5% amino acid identity with CYP71A13"].

## Catalytic function
- Original characterization: recombinant CYP71A13 converts indole-3-acetaldoxime (IAOx) to indole-3-acetonitrile (IAN); cyp71A13 mutants make greatly reduced camalexin; IAN feeding rescues [PMID:17573535 "CYP71A13 expressed in Escherichia coli converted IAOx to indole-3-acetonitrile (IAN)"; "Exogenously supplied IAN restored camalexin production in cyp71A13 mutant plants"]. Basis of EC 4.8.1.3 / RHEA:23156 / GO:0047720.
- Klein et al. 2013 (yeast microsomes with ATR1): reaction is strictly NADPH-dependent and also oxidative; CYP71A13 produces, in the presence of Cys/GSH, Cys-IAN, via a proposed alpha-hydroxy-IAN (cyanohydrin) -> dehydro-IAN electrophile [PMID:24151049 "the formation of both IAN and IAL is strictly dependent on the presence of both CYP71A13 and the cofactor NADPH"; "These data establish that CYP71A13 catalyzes the conversion of IAOx to an electrophile capable of accepting the thiol group of L-cysteine or glutathione"]. Three P450s (CYP79B2, CYP71A13, CYP71B15) suffice to reconstitute camalexin in vitro. So CYP71A13 is a genuine heme monooxygenase, not only a dehydratase; the IAOx-dehydratase term captures the IAN-forming part of the reaction only.
- Mucha et al. 2019 (abstract): indole-3-cyanohydrin "is synthesized by CYP71A12 and especially CYP71A13" [PMID:31511315].
- Kinetics: catalytic efficiency on IAOx ~0.029 uM-1 s-1 for CYP71A13 vs ~0.066 for CYP71A12 [PMID:25953104].
- No GO MF term exists for the oxidative IAOx -> cyanohydrin/dehydro-IAN step (OLS search for "indoleacetaldoxime" returns only GO:0047720). Mechanism still partly proposed, so no new-term proposal made; raised as a question.

## Biological process
- Camalexin biosynthesis: cyp71a13 ~2.2% of WT camalexin after UV; cyp71a12 cyp71a13 double KO essentially camalexin-deficient [PMID:25953104 "In cyp71a12 cyp71a13 double mutants, only traces of camalexin are synthesized, showing that dehydration of IAOx by CYP71A12 and CYP71A13 is essential for IAN synthesis as a camalexin precursor."]. CYP71A13 is the dominant isoform for camalexin in leaves; CYP71A12 for ICOOH derivatives [PMID:31411742 "CYP71A12, but not CYP71A13, is the major enzyme responsible for the accumulation of ICA"].
- Defense: cyp71A13 susceptible to Alternaria brassicicola [PMID:17573535]; UV-C-induced resistance to Botrytis lost in cyp71A13 [PMID:19154205]; infection defects with P. cucumerina / C. tropicale [PMID:31411742]. All downstream of camalexin production — the enzyme acts upstream of defense by making the phytoalexin.
- Rhizobacterium (P. fluorescens SS101) induced resistance to Pst requires camalexin; cyp71A13 among tested mutants [PMID:23073694]. Root-specific camalexin also controls PGPR growth promotion (CYP71A27 paper, cyp71A12/A13 as comparators) [PMID:31311863].

## Complex / localization
- Camalexin metabolon: co-IP and FRET-FLIM show CYP71A13 associates with CYP79B2, CYP71B15 (PAD3), ATR1 and GSTU4; CYP71A13 allosterically increases CYP79B2 substrate affinity [PMID:31511315]. Supports ComplexPortal "catalytic complex" NAS; the three IPI "protein binding" rows (CYP71B15, GSTU4, 14-3-3 omega/GRF2 At1g78300 from TAP proteomics PMID:19452453) are uninformative and removed per policy.
- Localization: P450 N-terminal anchor; ER membrane expected (plant class II P450), cytosolic-facing catalytic domain. GOA has "ER lumen" IDA from PMID:33831160 (TAIR) — this PMID does not resolve in NCBI E-utilities ("cannot get document summary") or Europe PMC (0 hits); PubMed web page served a JS challenge so no redirection notice could be checked. No canonical replacement established; per docs/reference_curation.md not guessed. Same row exists for CYP71A12. Topologically, "lumen" is unexpected for a signal-anchored P450, but paper unreadable -> UNDECIDED.
- Mitochondrion ISM (AtSubP prediction) — contradicted by the ER-type N-terminal anchor; removed.

## Expression (project context, not annotation grounds)
- Tang et al. 2023 (Colletotrichum higginsianum single-cell atlas; full text user-supplied): "CYP71A12 was induced mainly in the epidermis, whereas CYP71A13 was almost exclusively induced in the vasculature cells" at infection sites. Expression only; no GO annotation follows. [PMID:37741284, cached abstract only]
- UniProt: induced by Pst DC3000, B. cinerea, flagellin, BTH, UV-C; repressed by WRKY18/WRKY40.

## PMID:33831160 investigation
- `just fetch-gene-pmids` failed; esummary returns error "cannot get document summary"; Europe PMC EXT_ID query hitCount 0; WebSearch no hits. Treated as unresolvable/likely deleted PMID; annotation set UNDECIDED; reference kept with original id for provenance, flagged in reference_review.
