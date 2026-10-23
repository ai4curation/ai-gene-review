# MYMX (myomixer / Minion / myomerger) review notes

UniProt A0A1B0GTQ4 (MYMX_HUMAN), 84 aa, HGNC:52391, chr6. Previously annotated as a lncRNA
(LOC101929726 / RP1-302G2.5). Member of the MICROPROTEINS project.

## 2026-09-30 session (claude-code)

### Identity and discovery
- Three simultaneous 2017 discoveries of the same mouse gene (Gm7325):
  - Bi et al. Science 2017 [PMID:28386024 "we discovered an 84-amino acid muscle-specific peptide that we call Myomixer"] (CRISPR screen in C2C12).
  - Quinn et al. Nat Commun 2017 [PMID:28569755 "Here we show that Gm7325, which we name myomerger, induces the fusion of myomaker-expressing fibroblasts."]
  - Zhang et al. Nat Commun 2017 (Minion) [PMID:28569745]. Note: the task brief said "Zhang et al. 2017 Genes Dev"; PubMed shows the Minion paper is in Nat Commun (PMID:28569745), not Genes Dev.
- Human ORF first identified by Zhang et al. [PMID:28569745 "TBLASTN search revealed a putative human MINION homologue (hMINION) with an intact ORF of 84 codons (GenBank accession number KY857877)"], and shown to be protein-coding and functional [PMID:28569745 "both untagged and C-terminally epitope-tagged human MINION ORFs strongly reconstituted cell fusion in MinionKD cells"]; frameshifts abolish rescue, so the activity is from the protein, not the RNA.

### Topology / location
- Single-pass membrane protein; N-terminal hydrophobic helix anchors in plasma membrane, C-terminal region extracellular (ectodomain) [PMID:30197239 "Immunoblotting of the isolated proteins with Myomerger antibodies showed that Myomerger is normally expressed on the cell surface and suggested that the non-transmembrane region of Myomerger is extracellular"].
- Bi 2017: [PMID:28386024 "Myomixer localizes to the plasma membrane, where it promotes myoblast fusion and associates with Myomaker"].
- ER/Golgi: the only primary evidence is a crude fractionation [PMID:28569745 "Subcellular fractionation did however confirm significant enrichment within the membrane-associated fraction containing plasma membrane, ER and Golgi"] — this fraction does not discriminate among the three compartments. It is the likely source of the mouse ER/Golgi IDA that seeds the IBA and Ensembl-Compara IEA. ER/Golgi presence would be biosynthetic transit at most; the functional site is the cell surface. -> over-annotation.

### Mechanism (the MF question)
- Myomaker (MYMK, 7-TM) drives hemifusion; MYMX drives pore formation [PMID:30197239 "Myomaker is involved in membrane hemifusion and Myomerger is necessary for fusion pore formation"].
- MYMX works independently of MYMK in a heterologous HA-driven hemifusion system [PMID:30197239 "This finding demonstrates that Myomerger drives fusion pore formation and fusion completion in a Myomaker-independent manner."].
- Recombinant ectodomain (aa 26-84) rescues fusion of Mymx-null myoblasts in trans [PMID:30197239 "myoblast fusion depends on the interactions between the ectodomain of Myomerger and the plasma membrane of the myoblasts"].
- Biophysics: ectodomain induces positive spontaneous curvature in the outer leaflet [PMID:33479215 "We showed that Myomerger ectodomain indeed generates positive spontaneous curvature of lipid monolayers."]; two ectodomain helices regulated by externalized PS [PMID:36095199].
- Required on only one of the two fusing cells [PMID:35642635 "MYMX is a single-pass transmembrane micropeptide that is required on only 1 of 2 fusing cells"].
- Co-IP with Myomaker [PMID:28386024] but interaction not required for function [PMID:30197239 "a Myomaker-Myomerger physical interaction is not required for function"]. So "protein binding"/MYMK binding is not the core MF.
- MF term: GO:0140522 fusogenic activity ("The activity of joining two lipid bilayers to form a single membrane.") is the closest existing term. None of its children fit (GTPase-dependent, refolding-mediated, helical-bundle zippering). GO:0140912 membrane destabilizing activity is defined around permeabilisation/lysis — not a good fit.
  - Participation test: MYMX itself does the work of the pore-opening step (its ectodomain stresses the outer leaflet); it is not a substrate. Passes.
  - Comparator check (QuickGO 2026-09-30): GO:0140522 has very few experimental annotations (e.g. Chlamydomonas HAP2 IDA). Mouse Mymx (Q2Q5T5) and Mymk carry no MF other than protein binding (IPI) — i.e. no MF at all has been assigned; the absence reflects the recency of the fusogen MF branch rather than a deliberate convention excluding MYMX. Proposed as NEW with caution; flagged as a question for experts whether a partial (pore-completing) fusogen should carry the parent term.

### Processes
- Mouse KO: no multinucleated myofibers, perinatal lethality [PMID:28386024 "Histological sections through limb, body wall, and diaphragm musculature revealed an absence of multinucleated myofibers in Myomixer KO embryos"].
- Zebrafish KO abolishes fusion [PMID:29078404 "genetic deletion of myomixer using CRISPR/Cas9 mutagenesis abolishes myoblast fusion in vivo"].
- Satellite cell cKO abolishes regeneration [PMID:29581287 "abolishes satellite cell fusion and prevents muscle regeneration"] — this is the mouse IMP source for GO:0014905/GO:0043403 propagated to human.
- Human disease: CFZS2 (MIM:619941), R46* truncation removes ectodomain incl. AxLyCxL motif [PMID:35642635 "We describe a human pedigree harboring a recessive truncating variant of the MYMX gene that eliminates an evolutionarily conserved extracellular hydrophobic domain of MYMX, thereby impairing fusogenic activity."]. Patient iPSC myoblasts fail to fuse; knock-in mice die perinatally.
- PMID:35642635 IMP was annotated to GO:0014905 (myoblast fusion involved in skeletal muscle regeneration). Full text checked: no injury/regeneration experiments; "regenerat" appears only in introduction citing earlier work. Experiments are iPSC-derived myoblast fusion, developmental muscle phenotype of knock-in mice, and heterologous fusion. -> MODIFY to GO:0007520.
- Evolution: de novo vertebrate gene [PMID:36054355 "Myomixer appears to have evolved de novo in early vertebrates"]; poorly conserved sequence, fish orthologs ~62-75 aa but functional.

### Microprotein-project observations
- Classic smORF misannotated as lncRNA; rescue with frameshift controls is the gold standard coding proof.
- A microprotein can be a bona fide MF-bearing effector (membrane-remodelling ectodomain), not only a regulator of a larger partner — contrasts with SERCA-regulating micropeptides (SLN, PLN, MRLN, DWORF).
- GO currently gives MYMX no MF; fusogenic activity is the gap.

### Action summary
- PM (IBA, IEA, ISS): ACCEPT
- Golgi/ER membrane (IBA x2, IEA x2): MARK_AS_OVER_ANNOTATED
- myoblast fusion (IBA, IEA, IGI, ISS): ACCEPT
- GO:0014905 IEA, ISS: ACCEPT; IMP PMID:35642635: MODIFY -> GO:0007520
- GO:0043403, GO:0060538 (all): KEEP_AS_NON_CORE
- NEW: GO:0140522 fusogenic activity
