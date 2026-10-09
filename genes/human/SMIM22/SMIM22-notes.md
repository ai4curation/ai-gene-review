# SMIM22 (CASIMO1) review notes

## 2026-10-03 — initial review (claude-code, MICROPROTEINS Tier 2)

### Identity
- UniProt K7EJ46, 83 aa (isoform 3, displayed); isoform 2 (VSP_060203) inserts 5 residues
  after R69 (R -> RKVSPW). PE1. One predicted helical TM segment (residues 32-52,
  ECO:0000255); C-terminal disordered, basic/acidic region 60-83. Cys-rich juxtamembrane
  stretch (VAHCCCCSS) just after the TM helix.
- Canonical gene symbol SMIM22 (HGNC:48329), not an alternative ORF of another protein-coding
  host, so the standard `genes/human/SMIM22/` folder is correct.
- Alias CASIMO1, "Cancer-Associated Small Integral Membrane Open reading frame 1"
  [PMID:29765154 "which we named Cancer-Associated Small Integral Membrane Open reading frame 1 (CASIMO1)"].

### Literature
PubMed search "CASIMO1 OR SMIM22" (2026-10-03) returns 7 records. Only two study the protein:

1. PMID:29765154 (Polycarpou-Schwarz et al., Oncogene 2018) — discovery and sole source of all
   GOA experimental rows. **Abstract only** in cache; not OA (Unpaywall/EuropePMC: no free copy).
   - Overexpressed in hormone-receptor-positive breast tumours [PMID:29765154 "CASIMO1 RNA is overexpressed predominantly in hormone receptor-positive breast tumors"].
   - Knockdown reduces proliferation [PMID:29765154 "Its knockdown leads to decreased proliferation in multiple breast cancer cell lines"].
   - Loss disturbs actin, motility, causes G0/G1 arrest [PMID:29765154 "Its loss disturbs the organization of the actin cytoskeleton, leads to inhibition of cell motility, and causes a G0/G1 cell cycle arrest"].
   - Protein (not RNA) responsible [PMID:29765154 "The proliferation phenotype upon overexpression is observed only with CASIMO1 protein expression, but not with a non-translatable mutant"].
   - Interacts with SQLE [PMID:29765154 "CASIMO1 microprotein interacts with squalene epoxidase (SQLE)"].
   - Raises SQLE protein, not mRNA; LD clustering; knockdown lowers SQLE and pERK [PMID:29765154 "Overexpression of CASIMO1 leads to SQLE protein accumulation without affecting its RNA levels and increased lipid droplet clustering"].
   - SQLE epistasis [PMID:29765154 "SQLE knockdown mimicked the CASIMO1 knockdown phenotype and in turn SQLE overexpression fully rescued the effect of CASIMO1 knockdown"].
   - UniProt (from full text, which I cannot see): interacts with CANX and DDOST; partially
     co-localises with LAMP1 in late endosome. The IPI row lists CANX (P27824), DDOST (P39656)
     and SQLE (Q14534). CANX and DDOST are abundant ER-membrane proteins (calnexin, OST
     subunit) — common co-purifying partners of any ER-inserted TM protein.
2. PMID:39215037 (Zhao et al., NPJ Precis Oncol 2024) — NSCLC, NORAD/miR-520g-3p/SMIM22/GALE
   axis. Full text. Claims SMIM22 overexpression raises glycolysis and proliferation, co-IP with
   GALE, and nuclear co-localisation [PMID:39215037 "immunofluorescence demonstrated the co-localization of SMIM22 with GALE within the nucleus of NSCLC samples"].
   The nuclear localisation of a single-pass TM protein is implausible and not explained;
   the paper never tests the protein vs RNA distinction. Treated as LOW_QUALITY, used only as
   corroboration of a proliferation phenotype.

Other hits (ALDH7A1 methylation, Li-7 HCC gene set, TiO2 lncRNA profile, prostate cancer
recurrence gene set, a 2026 microprotein review) are expression-list mentions only; not cached.

### Assessment
- Mechanistic picture is thin: one study, one interaction (SQLE) with epistasis, protein-level
  effect on SQLE (stabilisation vs translation not distinguished in abstract).
- All BP rows are cancer-cell-line knockdown phenotypes; plausibly downstream of SQLE /
  cholesterol synthesis / ERK signalling. Keep as non-core.
- No GO "regulation of lipid droplet formation" term exists (QuickGO search 2026-10-03), so the
  lipid droplet formation row cannot be refined to a regulation term; keep as non-core.
- protein binding IPI: modify to enzyme binding (GO:0019899) on the strength of SQLE, which is
  the functionally validated partner (epistasis). CANX/DDOST hits are not informative.
- No NEW annotation: protein stabilisation (GO:0050821) toward SQLE is tempting but the
  abstract does not show a half-life experiment; left as a question.
- Subcellular localisation: UniProt says late endosome (partial LAMP1 overlap); ER is
  predicted by CANX/DDOST association and by SQLE partner (SQLE is ER-resident), but no
  ER location row exists and I cannot verify from the abstract — not added.
