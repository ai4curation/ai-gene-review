# ybbM curation notes

- Source: KBase gene-annotate dashboard protein NZ_CP016699.1_28 (*Lactococcus lactis*),
  https://gene-annotate-dashboard.kbase.us/review/NZ_CP016699.1_28 (hackathon review). The page and
  call were captured from the dashboard's Dash callback into `ybbM-dashboard-prediction-evidence/`.
- The exact sequence is UniParc UPI0009C0EEE3 (RefSeq WP_081144392). Its UniProtKB entry A0A1V0NBR7
  (LL275_pA030) was deleted as "Not part of a reference proteome". NZ_CP016699.1 is plasmid p275A of
  L. lactis subsp. lactis strain 275, which carries two identical copies (LL275_pA030, LL275_pA069).
- No reference proteome of L. lactis has a UPF0014 protein. Two active UniProtKB entries are 98.8%
  identical (248/251): G1FE25 (PVF_pVF18p21, plasmid pVF18, subsp. lactis bv. diacetylactis) and
  A4VC75 (plasmid pGdh442). The review is filed on G1FE25 because its subspecies matches strain 275.
  The folder uses the dashboard/eggNOG name ybbM; UniProt gives no gene name.
- GOA for G1FE25 has two IEA rows: GO:0005886 plasma membrane (TreeGrafter) and GO:0016020
  membrane (UniProt subcellular location).
- Dashboard call: "Putative iron-export ABC transporter permease FetB (UPF0014 family), associated
  with nickel tolerance." (tier A), with GO:0140359, GO:0006826 and GO:1990532.
- Bioinformatics (`ybbM-bioinformatics/RESULTS.md`): the query is full-length UPF0014 but scores
  359.9 bits against the NCBIfam FetB equivalog TIGR00245, below its 410-bit trusted cutoff
  (E. coli FetB: 476.8). The query is in a two-gene permease/ATPase cassette; the ATPase is 47.4%
  identical to E. coli FetA. Both cassettes on p275A sit among IS-element transposases.
- Experimental evidence for the family:
  - E. coli FetAB (59% identical): deletion of fetA or fetB increases H2O2 sensitivity;
    overexpression lowers intracellular iron by 37% in a Δfur strain [PMID:24038693, "intracellular
    iron levels in the Δfur strain are decreased by 37% by fetA and fetB overexpression"]. Nickel
    was among the metals tested, and iron was identified as the likely substrate. No direct
    transport assay was done.
  - Rice STAR2 (34% identical) with STAR1 is a UDP-glucose efflux transporter needed for aluminium
    tolerance [PMID:19244140, "STAR1/2 shows efflux transport activity specific for UDP-glucose"].
    The family therefore does not have one substrate.
  - Streptococcal homologs: expression changes only (S. agalactiae fetB down 16-fold after NO
    exposure, PMID:36297171; S. thermophilus stu1665 down at 50 °C, cited by the dashboard as
    PMID:22022447, but the locus is not named in the cached text, so it is not cited here).
- The nickel claim rests on one Fitness Browser phenotype of the Klebsiella michiganensis M5al
  homolog (58.1% identical; fitness -3.08, t -7.40 in 1.5 mM NiCl2). That homolog is in the
  proteobacterial FetB group, which the query is outside. There is no cofitness support.
- No deep-research report was generated for this gene; the review relies on the dashboard evidence,
  the bioinformatics above and the cached primary papers.
