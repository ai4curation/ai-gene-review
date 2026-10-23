# PLGG1 (AtLrgB; At1g32080; UniProtKB:Q9FVQ4) curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes
are a manual literature summary built only from cached publications in `publications/`
and the UniProt record (`PLGG1-uniprot.txt`). No `-deep-research-*.md` file exists for
this gene.

## Identity

- UniProt Q9FVQ4, "Plastidal glycolate/glycerate translocator 1, chloroplastic"
  (AltName AtLrgB); 512 aa precursor; transit peptide 1-76 (N-terminus of the mature
  protein, Ala-77, N-acetylated; mapped by envelope proteomics, PMID:12766230); twelve
  predicted transmembrane helices; CidB/LrgB family (Pfam PF04172, InterPro IPR007300;
  TCDB 2.A.122.2.1).
- Earlier name AtLrgB, from homology to the bacterial LrgA/LrgB holin-like proteins
  [PMID:21916894 "The protein, designated AtLrgB, may have evolved from a gene fusion of
  lrgA and lrgB."].

## Molecular function: glycolate/glycerate transmembrane transport

- Identified by coexpression with photorespiratory genes and reverse genetics
  [PMID:23382251 "Using transcript coexpression analyses, we identified Plastidal glycolate
  glycerate translocator 1 (PLGG1) as a candidate core photorespiratory transporter."].
- Transport evidence (Pick et al. 2013):
  - liposome uptake of 14C-glycerate with saturation kinetics, though with high background
    [PMID:23382251 "A Michaelis–Menten-type saturation kinetics of glycerate uptake was
    observed when liposomes were preloaded with glycerate or glycolate."];
  - isolated plgg1-1 chloroplasts cannot drive glycerate-dependent O2 evolution
    [PMID:23382251 "Hence, chloroplasts of the plgg1-1 mutant do not display
    glycerate-dependent oxygen evolution, which supports PLGG1’s function as a glycerate
    transporter."];
  - 18O2 flux shows glycolate trapped in the chloroplast [PMID:23382251 "Thus, plgg1-1 is
    impaired in the transport of both glycolate and glycerate."].
  - Conclusion [PMID:23382251 "Our results indicate that PLGG1 is the chloroplastidic
    glycolate/glycerate transporter, which is required for the function of the
    photorespiratory cycle."].
- Independent heterologous evidence: PLGG1 rescues a yeast glycolate-uptake mutant
  [PMID:28351992 "Our data indicate that both BASS6 and PLGG1 expressed in yeast facilitate
  transmembrane glycolate transport leading to rescue of the growth in glycolate uptake
  defective ady2Δ mutant ( Figure 8B )."]. BASS6 shares glycolate export, PLGG1 alone
  imports glycerate [PMID:28351992 "Our data indicate that BASS6 and PLGG1 partner in
  glycolate export from the chloroplast, whereas PLGG1 alone accounts for the import of
  glycerate."]; PLGG1 is described as an antiporter [PMID:28351992 "BASS6 is a member of the
  family of sodium-dependent symporters, which are unidirectional in transport, whereas
  PLGG1 is a glycolate/glycerate antiporter."]. GO has no glycolate:glycerate antiporter
  term (OLS search, this review); the two substrate-specific transporter activity terms are
  used.
- Older biochemistry in pea/spinach had already shown a single envelope carrier for both
  substrates [PMID:22303256 "The transporter exchanged glycolate for glycerate ( Howitz and
  McCarty, 1991 )."].
- Plasticity: plgg1-1 is not limiting under low light, implying alternative routes
  [PMID:27251551 "These results suggest that glycolate/glycerate transport during
  photorespiration can proceed in moderate rates through an alternative transport process
  with wild-type efficiencies."].

## Biological process: photorespiration

- [PMID:23382251 "A mutant deficient in PLGG1 shows WT-like growth only in an elevated
  carbon dioxide atmosphere."] and glycolate/glycerate accumulate [PMID:23382251 "The
  mutant accumulates glycolate and glycerate, leading to the hypothesis that PLGG1 is a
  glycolate/glycerate transporter."]; complementation restores the phenotype
  [PMID:23382251 "The phenotype was complemented when PLGG1 was expressed under its own
  promoter in plgg1-1 plants ( Fig. 1C )."].
- Orthologs in rice (OsPLGG1a/b; PMID:33483723, PMID:32038690, not cached) and moss
  (PpLrgB1; PMID:25793376, not cached) were reported with similar photorespiratory
  phenotypes; I only have PubMed abstracts for these and did not cite them in the review.

## Location: chloroplast envelope (inner membrane)

- Envelope proteomics (PMID:12766230, PMID:12938931, PMID:20061580) and PLGG1-GFP in
  N. benthamiana protoplasts [PMID:23382251 "The localization of PLGG1 in the chloroplast
  envelope ( Fig. S3 ), together with the metabolite accumulation patterns ( Figs. 2 and 3 ),
  identify PLGG1 as the chloroplastidic glycolate/glycerate transporter"].
- Inner-membrane assignment comes from TAIR IDA (PMID:21916894, abstract-only in cache)
  and HDA (PMID:12766230, abstract-only). The abstract of PMID:21916894 only says
  "chloroplast envelope membrane protein". I defer to the curators who read the full text.

## Earlier interpretations: chloroplast development / cell death

- The atlrgB mutants show interveinal chlorosis and premature necrosis [PMID:21916894
  "T-DNA insertion mutation of AtLrgB produced plants with interveinal chlorotic and
  premature necrotic leaves."] and lesion-mimic-like cell death [PMID:22180599 "The
  phenotypes of atlrgB resembled those in lesion mimic mutants, suggesting that AtLrgB
  functions against cell death, similar to the bacterial Lrg system."]; chlorosis was
  suppressed in continuous light [PMID:22180599 "When the atlrgB mutant was grown under
  continuous light, its chlorotic phenotype was suppressed."].
- Pick et al. reinterpret these as secondary consequences of photorespiratory metabolite
  toxicity [PMID:23382251 "Because the phenotype can be suppressed with high CO 2 ( Fig. 1 )
  and biochemically active chloroplasts can be isolated from plgg1-1 mutant plants grown in
  high CO 2 ( Table 2 ), we posit that the visible symptoms are due to the accumulation of
  toxic concentrations of glycolate and glycerate."]. UniProt records the same as a CAUTION.
  The GO "chloroplast organization" IMP is therefore treated as an over-annotation of an
  indirect effect.

## ABA, stomata, drought, lateral roots (PMID:29097201, abstract only)

- [PMID:29097201 "The length and number of LRs at the root-hypocotyl junction of plgg1-1
  and plgg1-2 were significantly impaired under exogenous ABA treatment"] and
  [PMID:29097201 "we found that PLGG1 is involved in other major ABA responses, including
  ABA-inhibited seed germination, ABA-mediated stomatal movement, and drought tolerance."]
- PLGG1 is not expressed in roots (PMID:22180599, PMID:21916894), so the root phenotype is
  presumably systemic. No mechanism linking a plastid glycolate/glycerate transporter to
  ABA signalling is given in the abstract. Kept as non-core acts_upstream_of_or_within
  phenotypes; full text not available to me.

## Immunity (not reviewed)

- PMID:42222920 (2026, Plant Cell Environ) links plgg1 and hpr1 to bacterial susceptibility,
  largely rescued by elevated CO2. Not cached and not used.
