# hes6 (Q6P0J1): evidence and exact-input prediction review

The three emitted GO predictions are biologically supported but broad. Direct zebrafish biochemistry establishes DNA binding by the Her7:Hes6 heterodimer, so a blanket claim that Hes6 cannot contribute to DNA binding would be wrong.

## Input identity and functional boundary

Q6P0J1 is zebrafish hes6/her13.2, a 226-residue product with bHLH and Orange domains. It is not her6 or her8a. The 2012 paper directly studies Hes6 alongside Her1 and Her7. The three generic protein-binding GOA rows have donors Her1/Q90463, Myod1/Q90477 and Her7/Q9I9K1 respectively; the separate identical-protein-binding row records Hes6 self-association. The primary paper includes MyoD as a promiscuous bHLH interaction comparison.

## Biological evidence

- [PMID:15905406 — Zebrafish hairy/enhancer of split protein links FGF signaling to cyclic gene expression in the periodic segmentation of somites.](https://pubmed.ncbi.nlm.nih.gov/15905406/): The primary reporter and interaction experiments establish transcriptional repression and Her1 association for Her13.2/Hes6.

> Her13.2 augments autorepression of her1 in association with Her1 protein.


> her13.2 is required for periodic repression of the
> Notch-regulated genes her1 and her7, and for proper somite segmentation.

- [PMID:16545363 — her1 and her13.2 are jointly required for somitic border specification along the entire axis of the fish embryo.](https://pubmed.ncbi.nlm.nih.gov/16545363/): The primary abstract explicitly reports combined Her1/Her13.2 loss-of-function effects on somitic borders.

> joint inactivation of her1 and her13.2 leads to a complete loss of all somitic
> borders

- [PMID:20637625 — Segment number and axial identity in a segmentation clock period mutant.](https://pubmed.ncbi.nlm.nih.gov/20637625/): The period-mutant study supports clock-dependent segment number; target identity is independently corroborated by the full 2018 report.

> precise control of segmentation
> clock period in relation to axial growth ensures a species-specific segment
> number


> arguing
> against an instructive role of the segmentation clock in determining axial
> identities.

- [PMID:22911291 — Topology and dynamics of the zebrafish segmentation clock core circuit.](https://pubmed.ncbi.nlm.nih.gov/22911291/): Direct zebrafish biochemistry establishes partner-dependent DNA binding by Hes6 in the Her7:Hes6 heterodimer.

> only Her1 homodimers and Her7:Hes6 heterodimers have strong DNA binding activity and target similar DNA sites.


> all of the possible dimers between Her1, Her7 and Hes6 form


> even the bHLH containing factor MyoD, but not the negative control non-bHLH protein PPARγ, was co-purified by Her1, Her7, and Hes6 to a similar extent

- [PMID:29624170 — Segmentation of the zebrafish axial skeleton relies on notochord sheath cells and not on the segmentation clock.](https://pubmed.ncbi.nlm.nih.gov/29624170/): The full primary report directly generates and analyzes a hes6 mutant; its focus on notochord-derived centra does not make the Hes6 annotation a wrong-gene citation.

> The novel hes6 mutation was created by injection of a TALEN targeted against hes6 in wild type.


> her1;hes6 mutants (n=15)

## Exact non-GO claims

The complete emitted record is preserved in [hes6-protnlm-source.json](hes6-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Uncharacterized protein

UNSCORED: “Uncharacterized protein” has no ProtNLM evidence tag in the returned name field. It is an API default rather than a scored biological hypothesis.

## Emitted GO claims

All 3 emitted GO claims are individually assessed in [hes6-protnlm-predictions-review.yaml](hes6-protnlm-predictions-review.yaml).

## Family integration

Hairy/HES-family domains support dimer formation, but individual homo- and heterodimers differ strongly in DNA binding and regulatory effect. In zebrafish, Her7:Hes6 is directly DNA-binding while Hes6 homodimers are not in the tested assays. Neither a universal DNA-binding grant to every dimer nor a blanket non-DNA-binding label for Hes6 is appropriate. Somitogenesis and neurogenesis also require lineage- and tissue-specific evidence.

## Evidence limits

Full text was read for the 2005, 2012 and 2018 target studies, including the interaction controls and hes6-mutant figure captions. The 2006 and 2010 cache entries are abstract-only, with target relevance corroborated by the full later reports. The genuine Falcon research synthesis identifies useful clock studies; the conclusions here are anchored to the experiments themselves. Neural function remains unresolved rather than rejected because mesoderm is the best-studied context.

## Re-review 2026-09-29
- Audit of the earlier careful review: actions on the segmentation-clock rows stand. Filled the empty `reason` field on all 26 rows with row-specific arguments (the summaries already carried the evidence).
- Protein-binding policy applied to the three GO:0005515 IPI rows from [PMID:22911291 "all of the possible dimers between Her1, Her7 and Hes6 form"]: the Her1 (Q90463) and Her7 (Q9I9K1) rows remain MODIFY -> GO:0046982 protein heterodimerization activity; the Myod1 (Q90477) row changed KEEP_AS_NON_CORE -> REMOVE, because the paper uses MyoD only as a demonstration of promiscuous bHLH association [PMID:22911291 "even the bHLH containing factor MyoD, but not the negative control non-bHLH protein PPARγ, was co-purified by Her1, Her7, and Hes6 to a similar extent"] and no informative MF is supported for that pair; removal does not deny the observed interaction.
- Added the missing propagation_review to the UNDECIDED IBA GO:0050767 regulation of neurogenesis (node PTN000105428; fly and mouse donors support the source but zebrafish hes6 is studied only in the presomitic mesoderm [PMID:15905406 "her13.2 is required for periodic repression of the Notch-regulated genes her1 and her7, and for proper somite segmentation."]).
- Added reference_review for the two local support files and the deep-research file (one corroborating quote, "Hes6 alone showed no detectable binding to the tested E-box probes.", on the DNA binding IEA row), plus one suggested experiment on a possible neural role. Validation: 0 errors, 0 warnings.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This entry was written during a re-review that deliberately ignored the ProtNLM2 predictions; the earlier sections above, including the ProtNLM2 claim assessments, are retained unchanged.

Direct zebrafish biochemistry establishes DNA binding by the Her7:Hes6 heterodimer, so a blanket claim that Hes6 cannot contribute to DNA binding would be wrong.

### Input identity and functional boundary

Q6P0J1 is zebrafish hes6/her13.2, a 226-residue product with bHLH and Orange domains. It is not her6 or her8a. The 2012 paper directly studies Hes6 alongside Her1 and Her7. The three generic protein-binding GOA rows have donors Her1/Q90463, Myod1/Q90477 and Her7/Q9I9K1 respectively; the separate identical-protein-binding row records Hes6 self-association. The primary paper includes MyoD as a promiscuous bHLH interaction comparison.

### Biological evidence

- [PMID:15905406 — Zebrafish hairy/enhancer of split protein links FGF signaling to cyclic gene expression in the periodic segmentation of somites.](https://pubmed.ncbi.nlm.nih.gov/15905406/): The primary reporter and interaction experiments establish transcriptional repression and Her1 association for Her13.2/Hes6.

> Her13.2 augments autorepression of her1 in association with Her1 protein.


> her13.2 is required for periodic repression of the
> Notch-regulated genes her1 and her7, and for proper somite segmentation.

- [PMID:16545363 — her1 and her13.2 are jointly required for somitic border specification along the entire axis of the fish embryo.](https://pubmed.ncbi.nlm.nih.gov/16545363/): The primary abstract explicitly reports combined Her1/Her13.2 loss-of-function effects on somitic borders.

> joint inactivation of her1 and her13.2 leads to a complete loss of all somitic
> borders

- [PMID:20637625 — Segment number and axial identity in a segmentation clock period mutant.](https://pubmed.ncbi.nlm.nih.gov/20637625/): The period-mutant study supports clock-dependent segment number; target identity is independently corroborated by the full 2018 report.

> precise control of segmentation
> clock period in relation to axial growth ensures a species-specific segment
> number


> arguing
> against an instructive role of the segmentation clock in determining axial
> identities.

- [PMID:22911291 — Topology and dynamics of the zebrafish segmentation clock core circuit.](https://pubmed.ncbi.nlm.nih.gov/22911291/): Direct zebrafish biochemistry establishes partner-dependent DNA binding by Hes6 in the Her7:Hes6 heterodimer.

> only Her1 homodimers and Her7:Hes6 heterodimers have strong DNA binding activity and target similar DNA sites.


> all of the possible dimers between Her1, Her7 and Hes6 form


> even the bHLH containing factor MyoD, but not the negative control non-bHLH protein PPARγ, was co-purified by Her1, Her7, and Hes6 to a similar extent

- [PMID:29624170 — Segmentation of the zebrafish axial skeleton relies on notochord sheath cells and not on the segmentation clock.](https://pubmed.ncbi.nlm.nih.gov/29624170/): The full primary report directly generates and analyzes a hes6 mutant; its focus on notochord-derived centra does not make the Hes6 annotation a wrong-gene citation.

> The novel hes6 mutation was created by injection of a TALEN targeted against hes6 in wild type.


> her1;hes6 mutants (n=15)

### Family integration

Hairy/HES-family domains support dimer formation, but individual homo- and heterodimers differ strongly in DNA binding and regulatory effect. In zebrafish, Her7:Hes6 is directly DNA-binding while Hes6 homodimers are not in the tested assays. Neither a universal DNA-binding grant to every dimer nor a blanket non-DNA-binding label for Hes6 is appropriate. Somitogenesis and neurogenesis also require lineage- and tissue-specific evidence.

### Evidence limits

Full text was read for the 2005, 2012 and 2018 target studies, including the interaction controls and hes6-mutant figure captions. The 2006 and 2010 cache entries are abstract-only, with target relevance corroborated by the full later reports. The genuine Falcon research synthesis identifies useful clock studies; the conclusions here are anchored to the experiments themselves. Neural function remains unresolved rather than rejected because mesoderm is the best-studied context.

### Re-review 2026-09-29
- Audit of the earlier careful review: actions on the segmentation-clock rows stand. Filled the empty `reason` field on all 26 rows with row-specific arguments (the summaries already carried the evidence).
- Protein-binding policy applied to the three GO:0005515 IPI rows from [PMID:22911291 "all of the possible dimers between Her1, Her7 and Hes6 form"]: the Her1 (Q90463) and Her7 (Q9I9K1) rows remain MODIFY -> GO:0046982 protein heterodimerization activity; the Myod1 (Q90477) row changed KEEP_AS_NON_CORE -> REMOVE, because the paper uses MyoD only as a demonstration of promiscuous bHLH association [PMID:22911291 "even the bHLH containing factor MyoD, but not the negative control non-bHLH protein PPARγ, was co-purified by Her1, Her7, and Hes6 to a similar extent"] and no informative MF is supported for that pair; removal does not deny the observed interaction.
- Added the missing propagation_review to the UNDECIDED IBA GO:0050767 regulation of neurogenesis (node PTN000105428; fly and mouse donors support the source but zebrafish hes6 is studied only in the presomitic mesoderm [PMID:15905406 "her13.2 is required for periodic repression of the Notch-regulated genes her1 and her7, and for proper somite segmentation."]).
- Added reference_review for the two local support files and the deep-research file (one corroborating quote, "Hes6 alone showed no detectable binding to the tested E-box probes.", on the DNA binding IEA row), plus one suggested experiment on a possible neural role. Validation: 0 errors, 0 warnings.

### Full re-review 2026-10-20 (ProtNLM2 benchmark cohort MOD_EVOLUTION20)

This re-review was done independently of any ProtNLM output; prediction files were not consulted, and the ProtNLM-related sections and the `hes6-protnlm-source.json` reference were removed from the review and these notes.

#### Identity
- Q6P0J1 (TrEMBL, 226 aa) is the full-length canonical hes6/her13.2 product: bHLH domain 19-71, Orange domain 90-123, and the C-terminal WRPW Groucho/TLE-recruitment tetrapeptide (sequence ends ...KSIWRPW), as in mouse Hes6 (Q9JHE6, 224 aa, also ending WRPW). It is not an isoform, fragment or alternative gene model.
- UniProt also holds A0A8N7UZW5 (226 aa, gene hes6), whose sequence is identical to Q6P0J1 (a redundant TrEMBL entry from a different genome assembly, not a distinct product).

#### Evolutionary placement
- PANTHER geneinfo (v19): Q6P0J1 -> PTHR10985:SF11 "TRANSCRIPTION COFACTOR HES-6"; human HES6 (Q96HZ4) and mouse Hes6 (Q9JHE6, MGI:1859852) are both in PTHR10985:SF11. So zebrafish hes6 is the 1:1 HES6 ortholog by subfamily membership, not just by name.
- The IBA rows derive from deep PAINT nodes (PTN004213585, PTN000105428) spanning the whole Hairy/E(spl) family; the HES6 subfamily itself is not a seed of the GO:0050767 regulation of neurogenesis node.
- Closest experimentally characterised relative: mouse Hes6. [PMID:10851137 "Hes6 alone does not bind to the DNA but suppresses Hes1 from repressing transcription."] and [PMID:10851137 "misexpression of Hes6 with retrovirus in the developing retina promotes rod photoreceptor differentiation"]. A later study reports ESE-box binding and repression by mouse Hes6 [PMID:11959828 "Hes6 binds DNA containing the Enhancer of Split E box (ESE) motif"]. Partner-dependent, weak autonomous DNA binding thus appears conserved across the HES6 subfamily, consistent with zebrafish data. Mammalian neural/myogenic roles were not transferred: they come from overexpression assays and the zebrafish protein has not been tested in neural tissue.
- No review of mouse Hes6 or human HES6 exists in the repo.
- Family review interpro/panther/PTHR10985/PTHR10985-review.yaml lists hes6 as representative of an unlabelled "Zebrafish Hes6/Her13.2" subfamily with no PANTHER subfamily id. This is not a conflict, but the subfamily could be grounded as PANTHER:PTHR10985:SF11 (TRANSCRIPTION COFACTOR HES-6) with human/mouse HES6 as co-members; left for the family curator.

#### Changes in this re-review
- GO:0045892 (IDA and IGI, PMID:15905406): ACCEPT -> MODIFY to GO:0000122 negative regulation of transcription by RNA polymerase II (correct but general; consistent with the IEA transcription rows already modified to GO:0000122).
- GO:0046983 protein dimerization activity (IEA): ACCEPT -> MODIFY to GO:0046982 and GO:0042803 (refinement rule; both children experimentally supported).
- GO:0050767 regulation of neurogenesis (IBA): still UNDECIDED; reason updated with the SF11 ortholog context.
- Description: added the HES6 orthology statement.
- All other actions re-checked and retained (somitogenesis rows: Hes6 is a clock repressor subunit, and the somite phenotype is supported by a TALEN mutant and a period mutant, not morpholinos alone).

#### Modules
- modules/notch_signaling.yaml models HES/E(spl) repressors (PTHR10985) as Notch target outputs at family level; zebrafish hes6 expression is FGF- rather than Notch-driven [PMID:15905406], so it fits that module only at family level. No segmentation-clock module exists.
