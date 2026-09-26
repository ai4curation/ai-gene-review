# fogD (A0A017SE81) -- Research Notes

## Gene Identity

- **Gene symbol**: fogD
- **UniProt ID**: A0A017SE81 (FOGD_ASPRC)
- **Organism**: *Aspergillus ruber* (strain CBS 135680), formerly *Eurotium rubrum*
- **Protein**: Short-chain dehydrogenase fogD, 286 aa, 31.8 kDa
- **EC**: 1.1.1.- (oxidoreductase acting on CH-OH donors, NAD(P) as acceptor)
- **Family**: Short-chain dehydrogenases/reductases (SDR), Pfam PF00106 (adh_short)

## The fog Biosynthetic Gene Cluster

The fog (flavoglaucin) gene cluster contains 9 genes (fogA-fogI) and was characterized by Nies et al. (2020) [PMID:32134669, DOI:10.1021/acs.orglett.0c00440, "The biosynthetic pathway of the prenylated salicylaldehyde flavoglaucin and congeners in *Aspergillus ruber* was elucidated by genome mining, heterologous expression, precursor feeding, and biochemical characterization"]. The cluster produces prenylated salicylaldehyde derivatives: flavoglaucin, dihydroauroglaucin, auroglaucin, and aspergin.

The genome of *A. ruber* CBS 135680 was sequenced by Kis-Papo et al. (2014) [PMID:24811710, DOI:10.1038/ncomms4745, "Genomic adaptations of the halophilic Dead Sea filamentous fungus Eurotium rubrum"].

## fogD's Role in Biosynthesis

According to the UniProt entry and PMID:32134669:

1. The PKS fogA assembles the polyketide chain and releases carboxylic acid products.
2. fogB, fogC, and fogD modify the nascent polyketide while it is still bound to fogA.
3. Together, fogA+fogB+fogC+fogD are necessary and sufficient for formation of the aromatic core; the cyclized PKS products are released as salicyl alcohols.
4. fogD is "probably involved in the reductive release of the modified PKS products" [PMID:32134669].
5. fogB is responsible for "oxidation of a hydroxyl group or reduction of remaining double bond(s) at the C-7 residue" [PMID:32134669].

Key insight from Nies et al.: "The polyketide skeleton was released as alkylated salicyl alcohols, which is a prerequisite for consecutive hydroxylation and prenylation, before reoxidation to the final aldehyde products" [PMID:32134669].

### Disruption phenotype

"Impairs the production of flavoglaucin and congeners, and leads to very low accumulation of the carboxylic acid (8E,10E,12E)-3,5,7-trihydroxytetradeca-8,10,12-trienoic acid" [PMID:32134669, via UniProt annotation].

### Important caveats

- No in vitro biochemical assay of purified fogD has been published.
- Protein existence level: 3 (inferred from homology) -- the protein has not been directly detected.
- The assignment as "reductive release enzyme" is based on (1) requirement in the minimal gene set, (2) SDR family membership, and (3) logical deduction given fogB's separate assignment.
- fogD acts as a **trans-acting** SDR rather than a cis-encoded domain within the PKS itself.

## PANTHER Family and TreeGrafter Mis-annotation

fogD is assigned to PANTHER family **PTHR44169** (NADPH-dependent 1-acyldihydroxyacetone phosphate reductase), subfamily **PTHR44169:SF3** (short-chain dehydrogenase SrdE). TreeGrafter propagates GO annotations from well-characterized members of this family, which are lipid metabolism enzymes (Ayr1p-like DHAP reductases in yeast).

This is a clear case of **incorrect annotation transfer across a functionally diverse enzyme superfamily**. The SDR superfamily is enormous and catalyzes many unrelated reactions. fogD's actual function is in secondary metabolite (polyketide) biosynthesis, not lipid metabolism.

### Assessment of Each TreeGrafter Annotation

All six TreeGrafter annotations derive from PANTHER:PTN001211783 via GO_REF:0000118:

1. **GO:0000140 (acylglycerone-phosphate reductase (NADP+) activity)** -- WRONG. This is the activity of Ayr1p, a lipid biosynthesis enzyme. fogD has no demonstrated or predicted DHAP reductase activity.

2. **GO:0004806 (triacylglycerol lipase activity)** -- WRONG. This is a hydrolase activity; fogD is an oxidoreductase. Completely wrong reaction type.

3. **GO:0005783 (endoplasmic reticulum)** -- WRONG. No evidence for ER localization. Secondary metabolite cluster enzymes in fungi typically function in the cytoplasm.

4. **GO:0005811 (lipid droplet)** -- WRONG. No evidence for lipid droplet localization. Propagated from lipid metabolism family members.

5. **GO:0006654 (phosphatidic acid biosynthetic process)** -- WRONG. fogD has no role in phospholipid biosynthesis.

6. **GO:0019433 (triglyceride catabolic process)** -- WRONG. fogD has no role in triglyceride catabolism.

### The Correct Annotation

- **GO:0044550 (secondary metabolite biosynthetic process)** from ARBA (GO_REF:0000117) is CORRECT.

## Correct GO Annotations for fogD

### Molecular Function
- **GO:0016616** (oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor) -- supported by SDR family membership and NADP binding sites
- The more specific reaction (reductive release from PKS) has no dedicated GO term

### Biological Process
- **GO:0044550** (secondary metabolite biosynthetic process) -- correct, already annotated
- **GO:0030639** (polyketide biosynthetic process) -- appropriate, as the fog cluster produces polyketide-derived metabolites

### Cellular Component
- No CC annotation is supported by current evidence. Cytoplasm (GO:0005737) would be a conservative inference for a soluble enzyme lacking signal peptide or TM domains.

## Comparison with Other fog Cluster SDRs

- **fogB** (P9WES5): Annotated with GO:0016491 and GO:0044550 only -- accurate and conservative.
- **fogG** (A0A017SEY2): Annotated with GO:0016491 only -- minimal and correct.
- **fogD** (A0A017SE81): Carries 6 incorrect TreeGrafter annotations + 1 correct ARBA annotation. The discrepancy with fogB is notable.

## ChEBI References

- Flavoglaucin: CHEBI:68188
- Salicylaldehyde: CHEBI:16008
- NADP(+): CHEBI:58349

## Open Questions

1. What is the exact catalytic mechanism of fogD? The reductive release hypothesis lacks in vitro confirmation.
2. Does fogD interact directly with the fogA PKS? Protein-protein interaction not demonstrated.
3. Why are three SDR enzymes in the cluster when fogG appears dispensable?


## 2026-09-20 re-review: corrections to the original categorical assessment

The six TreeGrafter rejections above are superseded by UNDECIDED pending a focused OpenScientist investigation. Secondary-metabolite participation does not prove exclusive function. Ayr1 is a direct counterexample to the original claim that no SDR can be a triglyceride lipase ([PMID:24187129](https://pubmed.ncbi.nlm.nih.gov/24187129/)); its primary study establishes source activity, not FogD activity. Lack of transmembrane or secretion features cannot exclude peripheral ER or lipid-droplet association.

The current PAINT slice records experimentally grounded Ayr1-seeded IBDs, but does not contain historical node PTN001211783. The ER assertion is at PTN001213826; the other five claims are at PTN001963740, each seeded by SGD:S000001386. Historical graft reconstruction is unresolved. A single well-characterized source is valid ancestral evidence, not intrinsically weak support.

The main PMID:32134669 cache is abstract-only and the publisher main article returned 403. Its open supplement was independently downloaded from the ACS Figshare API (article 11944365, file 21927279; DOI:10.1021/acs.orglett.0c00440.s001; MD5 a4e37dcbc2f110a230a24b385e1cfba6). Methods S5-S6 identify A. ruber QEN-0407-G2 as the DNA/RNA source and CBS135680 as the reference genome. Table S1 maps FogD to EYE95338/EURHEDRAFT_455854. The supplement identifies JN009 as the fogD deletion strain in the reconstructed A. nidulans JN004 cluster background. Table S2 and Figure S8 (S18/S30) were visually inspected: the latter contains a small 2d peak in the deletion strain. This corrects any implication of a native CBS135680 deletion or purified FogD catalytic assay.

Retain broad secondary-metabolite participation and a conservative SDR-derived oxidoreductase proposal. Withdraw the specific CH-OH/NAD(P) reaction assignment pending direct reaction/cofactor evidence; a reductive thioester-release proposal does not establish that reaction class by itself. Remove the redundant NEW polyketide-process row because it descends from the existing secondary-metabolite process; keep the specific pathway in the core summary. The former flavoglaucin-term proposal is moved to an ontology question. Unverified supporting_text_fulltext paraphrases are removed, and UniProt-derived statements are explicitly attributed to UniProt rather than invented primary quotations.
