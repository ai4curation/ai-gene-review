# CDC27 (APC3 / ANAPC3, UniProt P30260) — curation notes

Working journal for the GO annotation review of human CDC27. Citations are given inline as
[PMID:NNN "verbatim text"] and refer to the cached `publications/PMID_NNN.md` files. Many cached
entries are abstract-only (PMID:7736578, 16364912, 18485873, 29033132, 15678131, 18445686 and most
of the protein-binding sources); full text is cached for PMID:26083744, 27120157, 21926987,
21241890, 18662541, 21186364, 24781523, 25383541, 20439707, 20802534 and the interactome papers.

## 1. What CDC27 is

- Human homolog of budding-yeast CDC27, first cloned by Tugendreich et al. and Chen et al. (UniProt
  RN[1], RN[2]); 824 aa, ~92 kDa, roughly 14 TPR motifs; belongs to the APC3/CDC27 family
  (`CDC27-uniprot.txt`, Pfam PF12895 ANAPC3, IPR011990/IPR019734 TPR).
- Homodimeric TPR subunit of the anaphase-promoting complex/cyclosome. UniProt: "Homodimer
  (PubMed:27120157, PubMed:27509861). Component of the anaphase promoting complex/cyclosome (APC/C),
  composed of ANAPC1, ANAPC2, CDC27/ANAPC3, ANAPC4, ANAPC5, CDC16/ANAPC6, ANAPC7, CDC23/ANAPC8,
  ANAPC10, ANAPC11, CDC26/ANAPC12, ANAPC13, ANAPC15 and ANAPC16".
- The APC/C is a RING E3: [PMID:26083744 "The anaphase-promoting complex (APC/C) is a multimeric RING
  E3 ubiquitin ligase that controls chromosome segregation and mitotic exit."]. Catalysis is performed
  by the ANAPC2-ANAPC11 module: [PMID:16364912 "bound substrates are ubiquitinated by E2 enzymes that
  interact with a hetero-dimer of the RING subunit Apc11 and the cullin Apc2"]. CDC27 is not catalytic
  (deep research: "CDC27 should not be annotated as the APC/C catalytic center").

## 2. Molecular function: coactivator/APC10 IR-tail receptor = ligase scaffold

- The coactivator IR tail binds the APC3 TPR superhelix: [PMID:26083744 "The adjacent Ile of the IR
  tail packs into a hydrophobic pocket on Apc3."]; [PMID:26083744 "Disruption of Apc3 residues Asn575
  and Leu606 impaired coactivator binding"]. The same is true of CDC20: [PMID:27120157 "Nonetheless,
  the crucial Ile-Arg interaction of Cdc20IR with the TPR superhelix of Apc3A is conserved between the
  two coactivators"].
- The second protomer of the APC3 homodimer binds the IR tail of APC10/DOC1, the other half of the
  bipartite substrate receptor: [PMID:26083744 "Through its C-terminal IR residues, Apc10 interacts
  with a similar conformation to the symmetry-related IR tail-binding site on the Apc3 homo-dimer
  (Apc3B)"]; [PMID:21186364 "In crosslinking experiments we identified Cdc27, Cdc16 and Apc1 as binding
  partners of Doc1."]; [PMID:21186364 "Our results suggest that substrates are recruited to the APC/C
  by binding to a bipartite substrate receptor composed of a coactivator protein and Doc1."].
- The APC/C inhibitor TAME works by occupying this pocket: [PMID:26083744 "Its proposed mechanism is
  to inhibit coactivator association by competing for the IR tail-binding site on Apc3."]; the TAME
  paper itself is the source of two GOA protein-binding rows [PMID:20951947 "tosyl-L-arginine methyl
  ester (TAME), which binds to the APC and prevents its activation by Cdc20 and Cdh1"].
- Conclusion: the informative MF is GO:0160072 ubiquitin ligase complex scaffold activity ("brings
  together an ubiquitin ligase and an ubiquitin ligase-substrate adaptor"); the coactivators are the
  adaptors (GO:1990756) and ANAPC2/ANAPC11 the ligase. This mirrors the ANAPC2 review, which uses
  GO:0160072 for the cullin scaffold, and the CDC20/FZR1 reviews, which resolve the reciprocal rows to
  GO:0010997 anaphase-promoting complex binding.

## 3. Phospho-regulation: the APC3 loop as the mitotic-kinase docking hub

- [PMID:27120157 "Hyperphosphorylation of APC/C subunits, notably Apc1 and Apc3, is required for Cdc20
  to activate the APC/C"]; [PMID:27120157 "In Apc3 about 50 phospho-sites are clustered in a large
  disordered loop comprising residues 180-450"]; [PMID:27120157 "Kinase treatment resulted in a complete
  upshift of the Apc3 subunit as visualized on SDS-PAGE, indicative of stoichiometric phosphorylation"].
- Mechanism: [PMID:27120157 "Efficient phosphorylation of the auto-inhibitory segment, and thus relief
  of auto-inhibition, requires the recruitment of Cdk-cyclin in complex with a Cdk regulatory subunit
  (Cks) to a hyperphosphorylated loop of Apc3."]; [PMID:27120157 "deletion of the Apc3 loop
  (APC/CΔApc3-loop) reduced the phosphorylation-mediated activation of APC/C"].
- UniProt PTM line: "Phosphorylation on Ser-426 and Thr-446 occurs specifically during mitosis"
  (Kraft et al. 2003, PMID:14657031, not cached).
- No GO MF term captures "phospho-dependent kinase-docking loop"; recorded as a core function that
  contributes to ligase activation, with a suggested question rather than a NEW annotation.

## 4. Processes

- Loss of function: [PMID:7736578 "Injection of affinity-purified anti-CDC27Hs antibodies into
  logarithmically growing HeLa cells causes a highly reproducible cell cycle arrest in metaphase with
  apparently normal spindle structure."]; [PMID:21926987 "inactivating the APC/C by depleting APC3
  stabilised Cyclin B1 and severely delayed mitosis"].
- Chain types built by the APC/C: [PMID:18485873 "We find that the APC/C triggers substrate degradation
  by assembling K11-linked ubiquitin chains"]; [PMID:29033132 "engineered a bispecific antibody to detect
  K11/K48-linked chains and identified mitotic regulators, misfolded nascent polypeptides, and
  pathological Huntingtin variants as their endogenous substrates."].
- Meiosis: APC/C has essential meiotic functions [PMID:16364912 "The anaphase-promoting complex/cyclosome
  (APC/C) is a ubiquitin ligase with essential functions in mitosis, meiosis, and G1 phase of the cell
  cycle."]; deep research reports Drosophila cdc27 knockout reducing oocyte maturation and a CDC27 variant
  burden in human ovarian failure (candidate association). Kept as non-core for the human somatic review.

## 5. Localisation

- [PMID:7736578 "We find that the CDC27Hs and CDC16Hs proteins colocalize to the centrosome at all stages
  of the mammalian cell cycle, and to the mitotic spindle."] -> centrosome, mitotic spindle (IDA).
- UniProt: "SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:18445686}. Cytoplasm, cytoskeleton,
  spindle". PMID:18445686 is the EML3 proteomic screen of nuclear microtubule-binding proteins
  (abstract-only; CDC27 not named in the abstract) - accepted, deferring to the curator/UniProt.
- Nuclear interphase APC/C-CDH1: [PMID:21241890 "nuclear PTEN interacts with APC/C, promotes APC/C
  association with CDH1, and thereby enhances the tumor-suppressive activity of the APC-CDH1 complex"].
- Reactome nucleoplasm rows = APC/C-CDH1 G1 reactions; cytosol rows = mitotic APC/C-CDC20/MCC reactions.
  Both accepted as genuine compartments of the scaffold function.

## 6. Decisions on the 46 GO:0005515 protein-binding IPI rows

Policy (CLAUDE.md / annotation-reviewer skill): resolve bare protein binding to an informative MF or
complex membership where the evidence supports it; otherwise REMOVE as uninformative without asserting
the interaction is false.

| Partner | Rows | Action | Rationale |
|---|---|---|---|
| FZR1/CDH1 (Q9UM11) | 10548110, 18662541, 21186364, 21241890, 22014574 | MODIFY -> GO:0160072 | coactivator IR-tail docking on APC3 [PMID:18662541 "We confirmed that Cdh1 re-associates with Cdc27 (an APC/C core subunit) in human G2 cells subjected to genotoxic stresses, and this APC/CCdh1 is active"] |
| FZR1 (screens) | 33961781, 40205054 | REMOVE | proteome-scale co-purification |
| CDC20 (Q12834) | 17443180, 17443186, 20212161, 20951947, 21300909, 22014574, 24781523 | MODIFY -> GO:0160072 | as above; CDC27 is the APC/C IP handle in these MCC/USP44/p31comet/PP2A papers |
| CDC20 (screens) | 20360068, 35271311, 40205054 | REMOVE | MitoCheck/OpenCell/cell-map screens |
| ANAPC4 (Q9UJX5) | 21241890, 25383541, 26083744 | MODIFY -> GO:0005680 | co-subunits of the same complex |
| ANAPC4 (screens) | 20360068, 26496610, 35271311 | REMOVE | screens |
| MAD2L1 (Q13257) | 17443180, 17443186, 20212161, 20951947, 21300909, 21772247 (+ screens 26496610, 33961781, 40205054) | REMOVE | MCC bound to APC/C-CDC20; not a CDC27 function: [PMID:21926987 "Depleting APC3 had no effect, whereas depleting APC6 and APC8 strongly reduced MCC binding to the APC/C"] |
| FBXO5/EMI1 (Q9UKT4) | 17719540, 18662541, 23708001 (+33961781) | REMOVE | inhibitor's function; [PMID:23708001 "the carboxy-terminal tail of Emi1 antagonizes chain elongation by Ube2S, by competitively preventing its binding to the APC cullin subunit"] |
| MAD2L2 (Q9UI95) | 17719540 | REMOVE | APC inhibitor targeted by Shigella IpaB |
| NEK2 (P51955) | 16648845 (+35271311) | REMOVE | substrate MR-tail docking on core APC/C [PMID:16648845 "Most importantly, we show that Nek2A binds directly to the APC/C, also in an MR-dependent manner, even in the absence of the adaptor protein Cdc20."]; receptor subunit not identified in the cached abstract |
| NCK1 (P16333) | 17474147 | REMOVE | SH3 peptide-array hit |
| CCND1 (P24385) | 20439707 | REMOVE | [PMID:20439707 "we detected association of endogenous cyclin D1 and Cdc27 by coimmunoprecipitation from MCF-10A cells, which was increased by proteasome inhibition with MG132"]; CDC27-dependence of cyclin D1 turnover is necessity evidence for the APC/C, the degron receptor is CDH1+APC10 |
| PTEN (P60484) | 21241890 | REMOVE (duplicate of GO:0019903 row) | phosphatase-independent regulatory input [PMID:21241890 "in mitotic cells we did not observe dephosphorylation of APC3 by PTEN neither in vivo nor in vitro"] |
| "CDH1" = P12830 cadherin-1 | 20802534, 20951947 | MODIFY -> GO:0160072, WITH mis-ID flagged | symbol collision: the papers' Cdh1 is the APC/C coactivator FZR1 [PMID:20802534 "pVHL associates with Cdh1, an activator of the anaphase-promoting complex/cyclosome (APC/C) E3 ubiquitin ligase."] |
| COMT-2, FOXO3 | 25416956, 25609649 | REMOVE | HuRI Y2H / TF TAP-MS screens |

## 7. IBA rows

- PTN000285286 (PTHR12558 APC3 clade): GO:0005680, GO:0005737, GO:0007091, GO:0016567, GO:0031145 -
  all ACCEPT; human CDC27 in its own WITH/FROM is the expected marker of experimental grounding.
- PTN001757014 (deeper node, worm seeds): GO:0051301 cell division - ACCEPT as coarse but correct.
- PTN002649387 (seed ANAPC7 only): GO:0140767 enzyme-substrate adaptor activity - MODIFY -> GO:0160072.
  APC3 binds the adaptors (coactivator, APC10 IR tails), not substrate degrons; raised as a question
  about the node placement rather than removed.

## 8. Open items

- WITH-entity error (P12830 vs Q9UM11) on two rows should be fixed upstream.
- Whether GO needs an MF for the phospho-loop/Cks docking role.
- Hemifacial-microsomia de novo variants (Song et al. 2024, deep research) and SF3B1-mutant mis-splicing
  are candidate disease links, not annotation-grade evidence.
