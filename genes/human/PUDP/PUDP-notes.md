# PUDP (HDHD1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: PUDP is the closest experimentally characterised relative of fly CG5565
(Q9VQ04). This review assesses human PUDP on its own evidence. ProtNLM2 output was
not opened or used.

### Deep research

`just deep-research-falcon human PUDP --fallback perplexity-lite` failed on
2026-10-21: the Edison (falcon) API returned `403 Forbidden` at login, and the
perplexity-lite fallback returned `401 insufficient_quota`. No deep-research file
exists. The review relies on the UniProt record, the cached publications below, the
Reactome reaction, and the PANTHER/PAINT data in the repository.

Literature found with a PubMed search (`(PUDP[tiab] OR HDHD1[tiab]) AND
(pseudouridine OR phosphatase OR structure)`, six hits) and cached:

- PMID:20722631 (Preumont et al. 2010, Biochem J). The founding biochemical paper,
  abstract only in the cache.
  - Human erythrocytes contain a Mg2+-dependent pseudouridine-5'-phosphatase,
    inhibited by Ca2+ and vanadate, with a Km of 1 uM or less [PMID:20722631 "We show that human erythrocytes contain a pseudouridine-5'-phosphatase displaying a Km ≤ 1 μM for its substrate."].
  - Recombinant HDHD1 has kcat 1.6 s-1, Km 0.3 uM, and catalytic efficiency on
    psi-UMP at least 1000-fold higher than on other phosphate esters, including
    5'-UMP [PMID:20722631 "a catalytic efficiency at least 1000-fold higher than"].
  - Genetic confirmation: activity falls below 10% of controls in extracts of
    lymphoblasts and erythrocytes from X-linked ichthyosis patients whose deletion
    removes both STS and HDHD1 [PMID:20722631 "its activity was negligible (<10% of controls) in extracts of B-cell"].
  - Activity in women's erythrocytes is 1.5-fold higher than in men's, consistent
    with partial escape from X inactivation [PMID:20722631 "erythrocytes from women compared with men, in agreement with the HDHD1 gene"].
- PMID:31481524 (Defenouillere et al. 2019, Sci Signal), abstract only. Yeast Dog1
  and Dog2 dephosphorylate 2-deoxyglucose-6-phosphate. The human Dog2 homolog HDHD1
  dephosphorylates 2DG-6-P in vitro, and overexpressing it makes HeLa cells
  resistant to 2DG [PMID:31481524 "homolog HDHD1 displayed phosphatase activity toward 2DG-6-phosphate in vitro"].
  This is promiscuous activity toward a xenobiotic sugar phosphate. Overexpression
  shows what the enzyme can do, not what it does at endogenous levels, and no
  kinetic constants are given in the abstract. It is not added as a GO MF. PAINT
  curators did not place 2DG-6-P phosphatase activity on the PUDP node either.
- PMID:41053063 (Yu et al. 2025, Nat Commun). A biotechnology paper that uses HDHD1
  as the psi-MP-specific phosphatase in an engineered E. coli pseudouridine
  production pathway. It is independent applied confirmation of substrate
  selectivity, with LOW relevance to physiology.
- PMID:37895274 (Park et al. 2023, Genes Basel). A clinical XLI case with an Xp22.31
  deletion covering STS and PUDP. PUDP is a bystander here and not causal for the
  ichthyosis. LOW relevance.
- PMID:32296183 (HuRI). Yeast two-hybrid hits with AIRIM, GLYCTK and MAGEA4.
  Function is unknown, and the hits do not inform the enzyme activity.

### UniProt (Q08623, reviewed)

- Function, catalytic activity (RHEA:10944, EC 3.1.3.96), Mg2+ cofactor and
  kinetics all carry ECO:0000269 from PubMed:20722631. Km values: 0.38 uM for
  5'-PsiMP, 1.5 mM for 3'-AMP, 5.9 mM for fructose-6-P and 9.4 mM for 5'-UMP.
- The active-site nucleophile Asp14 and proton donor Asp16 are ECO:0000250 (by
  similarity), not tested by mutagenesis in human. Crystal structures exist: 3L5K
  (SGC, 2.0 A) and 9M7L/9M7M (1.3 A; no publication is cited in the entry).
- Classification: HAD-like hydrolase superfamily, CbbY/CbbZ/Gph/YieH family;
  InterPro IPR045228 Gpp1/Gpp2-like and IPR006439 HAD-IA; PANTHER PTHR18901:SF43.
- Four isoforms; only isoform 1 (the MANE transcript) has been assayed.

### Evolutionary grounding (PANTHER / PAINT)

From `interpro/panther/PTHR18901/PTHR18901-paint.tsv`:

- PTN000431251 (Eukaryota): GO:0016791 phosphatase activity IBD, seeded by
  Arabidopsis GPP1/GPP2 (AT4G25840, AT5G57440), yeast YKL033W-A and human PUDP.
- PTN000431252 (Unikonts): GO:1990738 pseudouridine 5'-phosphatase activity IBD,
  seeded by yeast YKL033W-A and human PUDP. It is dated 20260729 and is not yet in
  the GOA snapshot, which is why human PUDP has only the broad IBA.
- PTN008360158 (plant lineage): glycerol-3-phosphatase, mitochondrion and glycerol
  biosynthesis IBDs. These do not reach PUDP. PAINT curators deliberately kept
  glycerol-3-phosphatase off the unikont/PUDP node.

The CG5565 re-review tree walk
(`genes/DROME/CG5565/CG5565-bioinformatics/RESULTS-rereview.md`) places human
PUDP below PTN000431252. Its SF43 subfamily label comes from a Catarrhini
duplication (PTN004500568); mouse Pudp is SF38. This is a recent primate split,
not a deep functional divergence.

The function is therefore experimentally established in human (IDA, kinetics,
patient deficiency). Within the unikont clade it is inferred by PAINT, with yeast
YKL033W-A as the second experimental seed.

### Annotation decisions

- GO:1990738 (IDA and IEA from EC/RHEA): ACCEPT. This is the core function.
- GO:0016791 phosphatase activity (IBA, IEA): MODIFY to GO:1990738. It is correct but
  general, and the gene carries the specific child term.
- GO:0005829 cytosol (TAS, Reactome): ACCEPT. A soluble enzyme recovered from
  erythrocyte extracts with no targeting signals. There is no direct imaging.
- GO:0005515 protein binding (HuRI, three rows): REMOVE under the protein-binding
  policy. The interactions are not disputed.
- NEW GO:0009222 pyrimidine ribonucleotide catabolic process. PUDP itself catalyses
  the step, dephosphorylating psi-UMP to the nucleoside that is excreted. Comparator
  check: NT5C3A, a cytosolic pyrimidine 5'-nucleotidase in the same catalyst role,
  carries UMP/CMP/dUMP catabolic process terms from its biochemistry paper
  (PMID:11795870). No more specific "pseudouridine 5'-phosphate catabolic process"
  term exists in GO.

### Open questions

- Is the 2DG-6-P activity physiologically relevant to 2DG therapy at endogenous
  expression levels?
- What is the source of free psi-UMP in vivo: nuclear/cytosolic RNA turnover,
  UMP-pathway salvage errors, or both?
- Does the Catarrhini paralog produced by the PTN004500568 duplication keep the
  activity?
