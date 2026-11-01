# Msed_0399 (A4YDS4) notes

Metallosphaera sedula DSM 5348, Msed_0399, UniProt A4YDS4 (TrEMBL, unreviewed;
"3-hydroxyacyl-CoA dehydrogenase, NAD-binding protein"), 651 aa.

Automated deep research was unavailable for this review. No
`-deep-research-*.md` file was generated. The literature below was read
directly from the cached full texts in `publications/` (all four primary papers
are cached in full text).

## Domain architecture

- UniProt features: 3-hydroxyacyl-CoA dehydrogenase NAD-binding domain (Pfam
  PF02737, residues 2-181), two 3HCDH C-terminal domains (PF00725, 183-277 and
  299-389), and an enoyl-CoA hydratase/isomerase domain (PF00378, 407-650). So the
  dehydrogenase is N-terminal and the crotonase is C-terminal.
- This matches Ramos-Vera et al. [PMID:21169482 "an apparent fusion protein (∼70
  kDa) of an enoyl-CoA hydratase (C-terminal domain, ∼20 kDa) and a dehydrogenase
  (N-terminal domain, ∼40 kDa)"].
- The UniProt SIMILARITY line from ARBA00008750 says the reverse ("In the
  N-terminal section; belongs to the enoyl-CoA hydratase/isomerase family"). This
  contradicts the entry's own Pfam domain coordinates. It is a text-level ARBA
  error that does not reach GO.
- PANTHER PTHR23309:SF49 ("peroxisomal bifunctional enzyme"), the same
  multifunctional-enzyme family as E. coli FadB and human EHHADH. The domain order is
  reversed relative to FadB [PMID:21169482 "in E. coli , the tetrafunctional FadB,
  which is involved in fatty acid degradation, contains these two domains in reverse
  order"].

## Biochemistry

- Identification: the enzyme was purified from autotrophically grown cells [PMID:21169482
  "Mass-spectrometric analysis identified the 70-kDa protein as Msed_0399."]. The
  recombinant enzyme catalysed both steps [PMID:21169482 "Substrates were indeed
  crotonyl-CoA ( K m 0.3 mM), ( S )-3-hydroxybutyryl-CoA ( K m 0.2 mM), and NAD + ( K m
  0.25 mM)."].
- Cofactor: NAD+, not NADP+ [PMID:21169482 "NADP + , acryloyl-CoA, 3-hydroxypropionyl-CoA,
  and the ( R ) stereoisomer of 3-hydroxybutyryl-CoA were not transformed."]. The protein
  also binds NAD+ in the purification [PMID:21169482 "The enzyme was eluted with 1 ml of
  0.25 mM NAD + in buffer A."].
  - So GO:0003857 (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity (EC 1.1.1.35)
    fits. GO:0008691 3-hydroxybutyryl-CoA dehydrogenase activity is defined with NADP+
    (EC 1.1.1.157) and does not fit, even though the paper and BRENDA use EC 1.1.1.157.
  - The NAD+ binding IEA (InterPro IPR006176) is therefore correct here. This contrasts
    with the default NAD binding error on the NADPH enzyme Msed_0709 (ARCHAEA pattern 6).
- Expression: [PMID:21169482 "The expected bifunctional hydratase/dehydrogenase activity
  was present in similar amounts in extracts of autotrophically and heterotrophically
  grown cells of M. sedula"]. The activity is not autotrophy-specific.
- In-vitro reconstitution: Msed_0406, Msed_1321, Msed_0399 and Msed_0656 [PMID:24532060
  "were produced recombinantly in Escherichia coli , combined in vitro , and shown to
  convert 4HB to acetyl-CoA."], with NAD+ in the assay.
- Substrate range [PMID:32218776 "In hydratase reaction, Msed_0399 was promiscuous and
  could hydrate not only crotonyl-CoA, but also (E)-2-octenoyl-CoA and acrylyl-CoA
  (Table 2)."; "Similarly, it acted as dehydrogenase with both C4 and C8
  (S)-3-hydroxyacyl-CoAs (Table 2)."; "Interestingly, the enzyme was most active with
  octenoyl-CoA, thus suggesting that Msed_0399 may participate in β-oxidation, in
  addition to autotrophic CO2 fixation."].
  - The hydratase therefore acts on (2E)-enoyl-CoAs from C3 to C8. GO:0018812
    3-hydroxyacyl-CoA dehydratase activity ((2E)-enoyl-CoA; no stereochemistry stated)
    is the right level. GO:0120092 (C4 only) is too narrow, and GO:0080023 is the
    (3R)-specific reaction, while this enzyme is (S)-specific.

## Physiological role: not the main cycle enzyme

- Dehydrogenase: [PMID:32218776 "show that Msed_1423 is the main
  (S)-3-hydroxybutyryl-CoA dehydrogenase in the HP/HB cycle in Sulfolobales."]. Msed_1423
  (UniProt A4YGM9) clusters with Msed_1424 and Msed_1426. Msed_1423 and Msed_0389 have
  kcat/Km values 3- and 20-fold higher than Msed_0399 for (S)-3-hydroxybutyryl-CoA.
- Conclusion of the same paper: [PMID:32218776 "our data show that the bifunctional
  crotonyl-CoA hydratase/(S)-3-hydroxybutyryl-CoA dehydrogenase is not the main enzyme
  that catalyzes these reactions in M. sedula. This is corroborated by the fact that its
  gene is absent in many other autotrophic Sulfolobales."].
- Distribution: [PMID:32218776 "Homolog(s) of bifunctional crotonyl-CoA
  hydratase/(S)-3-hydroxybutyryl-CoA dehydrogenase Msed_0399 genes were found in 75% of
  the genomes, whereas four autotrophic species (Acidianus ambivalens, Acidianus
  hospitalis, Acidianus sulfidivorans, and Stygiolobus azoricus) do not possess the
  corresponding gene (Table 5)."].
- Genomic context: [PMID:32218776 "In fact, msed_0399 is located in the cluster with the
  genes homologous to various β-oxidation genes (Figure 2A) and may thus be primarily
  involved in, e.g., fatty acid metabolism rather than CO2 fixation (Table 2)."]. Caveat:
  [PMID:32218776 "Although the growth of M. sedula on fatty acids has not been shown,
  some Sulfolobales are capable to use these compounds as a sole carbon source"].
- Hydratase: [PMID:33472982 "the latter probably with some contribution of Msed_0399
  (8.2%)"]; [PMID:33472982 "Msed_0399, which was previously thought to be responsible
  for crotonyl-CoA conversion into acetoacetyl-CoA, is responsible for a small flux in
  autotrophically grown M. sedula, at best."]. The protein is abundant in autotrophic
  cells (89% of the level of Msed_2001), so its low in-vivo share reflects low Vmax, not
  absence.
- In the dicarboxylate/4-hydroxybutyrate cycle of Ignicoccus and Pyrobaculum, the
  orthologous fusion protein is the only candidate and is thought to do both steps
  (PMID:21169482, PMID:32218776). Its secondary role in M. sedula is a Sulfolobales
  peculiarity.

## Curation conclusions

- Core MF: GO:0003857 (NAD+-specific, (S)-specific, C4 to C8 tested) and GO:0018812
  (C-terminal crotonase domain). Both are intrinsic activities of the protein. Neither
  is the main in-vivo catalyst of its 3HP/4HB cycle step.
- Process: no process term is well supported. Carbon fixation (GO:0015977) is not
  added as NEW because the authors who measured the fluxes conclude the enzyme carries
  "a small flux ..., at best", and the gene is missing from several autotrophic
  Sulfolobales. Fatty acid metabolism is a hypothesis from substrate range and gene
  context, with no in-vivo evidence. GO:0006631 is kept as non-core (broad, compatible
  with the C4 to C8 acyl-CoA chemistry). GO:0006635 is defined as complete oxidation of a
  long-chain fatty acid, which has never been tested, so it is UNDECIDED.
- Module impact: the module's step 6 ((S)-3-hydroxybutyryl-CoA oxidation) uses Msed_0399
  as the representative. PMID:32218776 shows that Msed_1423 (A4YGM9) is the main enzyme.
  The step should be re-grounded on Msed_1423, with Msed_0399 at most a minor
  contributor. GO:0003857 remains the right function term, because Msed_1423 is also
  NAD-dependent [PMID:32218776 "The purified recombinant Msed_0389 and Msed_1423
  catalyzed the NAD-dependent oxidation of (S)-3-hydroxybutyryl-CoA to acetoacetyl-CoA"].
  PMID:32218776 should be added to the module's evidence.
