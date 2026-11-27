# Tap42 (Drosophila melanogaster, Q9VJZ5, FBgn0051852, CG31852) - manual literature research

No deep-research API was available; this summary was assembled by hand from cached
publications (publications/PMID_*.md) and a PubMed search ("Tap42 AND Drosophila", 9 hits,
of which 4 concern the fly gene: PMID:15802506, PMID:22701670, PMID:17570358, and the
interactome screens PMID:37061542 / PMID:38944040 that appear only through GOA).

## Identity and family

- Tap42 (CG31852) is the single Drosophila member of the IGBP1/TAP42 (alpha4) family
  (Pfam PF04177 TAP42; InterPro IPR007304 TAP46-like; PANTHER PTHR10933:SF9).
  [PMID:15802506 "BLAST searches of the Drosophila genome revealed a single gene CG31852 with significant identity to Tap42/α4"]
- 29% identity to human alpha4 (IGBP1) and 24% to yeast Tap42; the central PP2Ac-binding
  region is the best conserved part. [PMID:15802506 "The central region of α4 shown to mediate interactions with PP2A ( L iu et al. 2001 ; T rockenbacher et al. 2001 ) is particularly well conserved (35% identity)."]

## Binding to PP2A-family catalytic subunits

- Endogenous Tap42 co-immunoprecipitates PP2Ac from larval extracts.
  [PMID:15802506 "antibodies raised against a CG31852-GST fusion recognized a protein of ∼42 kDa and were able to co-immunoprecipitate the PP2A catalytic subunit (PP2Ac) from larval extracts"]
- In S2 cells FLAG-Tap42 pulls down Mts (PP2Ac), PP4 and PPV (PP6c); the R152E/K155D
  (Tap42ED) mutant fails to bind any of them.
  [PMID:22701670 "Western analysis of the immune complexes revealed that Tap42 interacts with all three Drosophila phosphatase catalytic subunits (Fig. 6-A)."]
  [PMID:22701670 "In contrast to wild type Tap42 (Tap42WT), Tap42ED failed to interact with the Drosophila phosphatases (Fig. 6-A)."]
- High-throughput binary interactome screens also record Tap42-Mts binding (GOA IPI rows,
  PMID:37061542, PMID:38944040; UniProt CC INTERACTION Q9VJZ5-P23696 NbExp=5).

## Regulation of PP2A level/localization

- Loss of Tap42 increases PP2Ac levels and drives PP2Ac into the nucleus; Tap42 keeps PP2Ac
  cytoplasmic. [PMID:15802506 "Thus, Tap42 acts independently of TOR to limit PP2Ac expression levels and to restrict its localization to the cytoplasm."]
- Genetic interaction: a heterozygous hypomorphic mts allele (mtsXE2258) suppresses Tap42 RNAi
  phenotypes and lethality, consistent with excess Mts activity in Tap42-depleted tissue.
  [PMID:22701670 "These findings demonstrate that Tap42's modulation of Mts plays an active role in Drosophila tissue development and viability."]
- Rescue requires phosphatase binding: Tap42WT but not Tap42ED rescues RNAi phenotypes.
  [PMID:22701670 "These findings indicate that the Tap42RNAi-induced phenotypes are entirely due to the impaired interactions between Tap42 and PP2A family members"]

## No role in TOR signaling in Drosophila

- [PMID:15802506 "Here we show that Tap42 does not contribute significantly to TOR signaling in Drosophila, as disruption of the Tap42 gene does not cause defects in cell growth, metabolism, or S6-kinase activity characteristic of TOR inactivation."]
- Independent S2-cell RNAi: [PMID:17570358 "Knockdown of the Drosophila homolog of the PP2A/PP4/PP6 interaction protein alpha4/Tap42 did not affect S6K phosphorylation, but did induce apoptosis."]

## Cellular and organismal phenotypes

- Null mutants die as early third-instar larvae; neuroblasts arrest before anaphase with
  disorganized spindles. [PMID:15802506 "In summary, mutations in Tap42 disrupt spindle morphology and arrest mitosis prior to anaphase entry, phenotypes similar to those caused by mutations in PP2A catalytic and regulatory subunits."]
  The authors note the phenotype might reflect a checkpoint rather than a direct role.
  [PMID:15802506 "it may also reflect engagement of a common mitotic checkpoint despite distinct or even opposing primary defects."]
- Tap42-null clones activate JNK signaling and caspases and die cell-autonomously
  [PMID:15802506 "Loss of Tap42 ultimately results in increased JNK signaling, caspase activation, and cell death."]
- Wing-disc RNAi (pnr-/ap-Gal4) gives thorax cleft, shriveled wings, altered HH/JNK/DPP signaling
  and apoptosis [PMID:22701670 "These findings suggest that Tap42 is involved in wing imaginal disc morphogenesis and plays a crucial role in the patterning and differentiation of wing discs."]
- Expression: enriched in disc stalk and peripodial epithelium; also brain, neurons and gut.
  [PMID:22701670 "Tap42 is highly expressed in the wing disc stalk and squamous peripodial epithelium (PE) cells but weakly expressed in the columnar disc proper (DP) cells"]

## Gaps

- No in vitro phosphatase assay with Drosophila Tap42 has been published; whether it inhibits,
  stabilizes, or retargets Mts/PP4/PPV catalytic activity is inferred genetically.
- Whether Tap42 participates in MID1-like ubiquitin-mediated PP2Ac turnover in flies is unknown
  (no clear MID1 ortholog; [PMID:15802506 "none is an obvious MID1 homolog"]).
