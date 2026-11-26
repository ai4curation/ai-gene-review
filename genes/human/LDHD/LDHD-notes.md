# LDHD (Q86WU2) review notes

Journal for the human LDHD review, written 2026-11-26. The second half of this file is the
evidence digest: every `QUOTE:` there is a verbatim substring of the cached
`publications/PMID_<id>.md` file (234 quotes machine-checked after whitespace normalisation).

## What was searched

- PubMed (MCP and E-utilities), 2026-11-26: `LDHD OR "D-lactate dehydrogenase deficiency" OR "D-lactic aciduria"` (57 hits); `(LDHD[tiab] OR "D-lactate dehydrogenase"[tiab]) AND (gout OR hyperuricemia OR mutation OR variant OR deficiency)` (120 hits); `D-lactate[Title] AND (mitochondria[Title] OR mitochondrial[Title])` (24 hits); further searches for an Ldhd knockout mouse, additional patient reports 2019-2026 and D-lactate/urate exchangers found nothing new.
- Deep research: Falcon and Perplexity providers are not available in this environment (`Provider 'falcon' not available. Available: asta, openscientist, claude_code`). Asta retrieval was generated (`LDHD-deep-research-asta.md`); an OpenScientist deep-research run and three OpenScientist hypothesis runs were launched (see the end of this file).
- GO-CAM: `gocams/index.tsv` has no activity for UniProtKB:Q86WU2 and none for the mouse, zebrafish or yeast DLD1 orthologs, so there is no GO-CAM to review for this gene. The Noctua MCP search could not be used (no Barista token).
- Reactome: LDHD is in the participant set of R-HSA-9837978 and R-HSA-9838004 (participants service, 2026-11-26), although neither event summary names it.

## Synthesis

1. **Activity.** LDHD is the mitochondrial FAD-dependent D-lactate dehydrogenase. On the human protein: strict D-stereospecificity and FAD [PMID:38373542 "hDLDH is strictly stereospecific"], direct reduction of cytochrome c [PMID:38413804 "we could confirm direct electron transfer from d-lactate to cytochrome c by monitoring its haem absorbance"], and in vivo clearance of D-lactate [PMID:30931947 "We therefore conclude that LDHD is essential for human D-lactate metabolism."]. The physiological acceptor is cytochrome c; the mouse structural paper used artificial dyes and left the acceptor open [PMID:37863926 "the primary oxidant under physiological conditions is unknown"].
2. **Substrate scope.** D-2-hydroxy acids with small hydrophobic side chains; branched-chain ones are better substrates of the mouse enzyme than D-lactate, and D-2-hydroxyglutarate is not a substrate [PMID:37863926 "mLDHD is an Mn2+-dependent general dehydrogenase for a broad range of D-2-hydroxyacids with small to moderate-size hydrophobic moieties at the C2 atom."]. Patients accumulate D-2-hydroxyisovalerate and D-2-hydroxyisocaproate [PMID:30931947 "Increased levels of D-2-hydroxyisovaleric acid and D-2-hydroxyisocaproic acid were observed in both of our patients."].
3. **Numbering.** Three systems are in use for the same residues: isoform 1 (UniProt displayed, NM_153486; all published missense variants), isoform 2 = MANE Select = mouse numbering (ClinVar, gnomAD, PDB 8JD*; 23 lower after residue 233), and a presequence-less numbering 51 lower than isoform 1 in PMID:38373542 (W323C, T412M). See `LDHD-bioinformatics/RESULTS.md`.
4. **Disease mechanism.** Recessive loss of function. All four published missense substitutions made in the mouse enzyme lose about 90% of activity [PMID:37863926 "the activity assay shows that all the mutants lose about 90% of the activity"]; R370W and W374C hit the substrate pocket, T251M and T463M destabilise FAD binding. No assay of a human variant protein gives a residual-activity figure. gnomAD shows no constraint against heterozygous loss of function, as expected for a recessive enzyme defect.
5. **Phenotype.** Raised plasma and urinary D-lactate is universal; gout and hyperuricaemia in the Bedouin, Melanesian, Vietnamese and Moroccan families; neurodevelopmental features in others, each with a second possible cause [PMID:40678184 "Altogether, there is no obvious correlation between the type of pathogenic variant of the LDHD gene and the phenotype."].
6. **Localisation.** Mitochondrion is secure (human proteome, human overexpression, mouse immunofluorescence). Inner membrane is supported by rat fractionation and a human "membrane flavoprotein" description; the face is unresolved (matrix side in rat liver [PMID:11955284 "it is localized in the matrix phase of the mitochondrial inner membrane"] against cytochrome c reduction).

## Decisions worth recording

- `GO:0003824` catalytic activity (IEA): TOO_GENERAL, not MODIFY, because the InterPro signatures behind the row do not identify substrate or acceptor (maintainer ruling of 2026-11-14). The zebrafish ldhd review, written before the ruling, uses MODIFY for the same row.
- `GO:0004457` lactate dehydrogenase activity (IDA, PMID:38373542): MODIFY to GO:0140170 on the paper's own evidence. The GO definition of GO:0004457 names NAD+ although the term is the parent of the FAD and cytochrome terms; recorded as a proposed ontology change.
- `GO:0008720` D-lactate dehydrogenase (NAD+) activity (IBA): MODIFY to GO:0140170 as a lateral acceptor correction, consistent with the zebrafish review and the PTHR11748 family review (PAINT node PTN000202298, verdict UNRESOLVED).
- `GO:0005515` protein binding (IPI, CSRP3): REMOVE under the protein-binding policy; the interaction is kept in the findings.
- `GO:0005743` mitochondrial inner membrane (TAS, Reactome): ACCEPT, with the topology recorded as a knowledge gap.
- No NEW annotation was added. A matrix or intermembrane-space row was not added because the two available lines disagree. Mn2+ binding was not added because it is shown only for the mouse enzyme.
- Publication notation problems (not database defects): PMID:37021930 prints c.206C>T for rs1035398551, which is c.206T>C p.Val69Ala; its p.(AlaGly432fsTer58) mixes isoform 2 residue numbering with the isoform 1 frameshift length. The Sloth deletion is written c.1_930del although exons 1-7 of NM_194436 end at c.958 (`results/isoform_exons.json`); left as printed.
- Curation gap, not a knowledge gap: mouse Ldhd and yeast DLD1 have no review in this repository; UniProt does not cite PMID:38413804 (recorded as a source defect, MISSING_STATEMENT).

## OpenScientist runs

Launched 2026-11-26 through `just gene-hypothesis-research openscientist human LDHD ...` (three iterations, 7200 s timeout). Local bioinformatics results were not passed to the prompts.

| Slug | Question | Final status, 2026-11-26 23:25 UTC |
|---|---|---|
| `isoform1-insert-dispensable` | Is the isoform-1-only segment a lineage-restricted, dispensable insertion? | First run stopped by the 2 h job limit; narrowed rerun (2 iterations) cancelled at its 5400 s timeout (job 5fb612b8-25f0-40f5-9950-900a81e054fb). No report; not retried |
| `t463m-catalytic-loop-destabilisation` | Does p.Thr463Met act by destabilising the catalytic loop? | First run stopped by the 2 h job limit; narrowed rerun (2 iterations) cancelled at its 5400 s timeout (job 64afe1f1-463d-4eb8-8a50-89678e5d471c). No report; not retried |
| `ims-facing-inner-membrane-topology` | Does the catalytic domain face the intermembrane space? | First run cancelled at the 7200 s OpenScientist ceiling (job be69918f-f9fd-4ebc-8593-1d4173b20b88); narrowed proteomics-lookup rerun cancelled at its 5400 s timeout (job b71b2653-3cca-4c5d-97fc-9af377e0e353). No report; not retried |

The OpenScientist gene-level deep-research run (`just deep-research-openscientist human LDHD`) was also stopped at the 2 h limit and wrote nothing; it was not restarted. Seven OpenScientist jobs were launched in all and none returned a report, including single-question reruns, which points to an upstream problem on the day and not to scope. No conclusion in the review depends on any of these runs; the three questions remain open and are recorded as knowledge gaps or suggested experiments.

Topology follow-up done locally while the run was pending: MitoCarta3.0 lists LDHD as MIM with no APEX_matrix and no APEX_IMS evidence (`LDHD-bioinformatics/RESULTS.md`, section 6), so the proteomics resource most likely to settle the face does not.

---

# Evidence digest
Conventions: every `QUOTE:` is a verbatim substring (whitespace-normalised) of the cached
`publications/PMID_<id>.md`. Lines starting `NOTE` are my own reading and carry no quote.
Cache status is given per paper. FT = full text cached; ABS = abstract only.

Numbering key (my reading of the UniProt record `LDHD-uniprot.txt`, not a quote):
isoform 1 = Q86WU2-1, 507 aa, NM_153486 (displayed); isoform 2 = Q86WU2-2, 484 aa, NM_194436.3
(MANE Select), lacking residues 211-233. All patient missense variants are numbered on isoform 1
(NM_153486.3). Mouse LDHD (Q7TNG8, 484 aa) numbering = human isoform-1 numbering minus 23 for
residues after the insertion (R370/W374/T463 -> R347/W351/T440; T251 -> T228).

---

## PMID:30931947 Monroe 2019 Nat Commun (FT) — first human LDHD deficiency; zebrafish ldhd KO + rescue

### Disease / patients
- Two unrelated patients, homozygous LOF variants, raised urinary and plasma D-lactate — QUOTE: "identification of two different homozygous variants resulting in enzymatic loss-of-function in LDHD, encoding lactate dehydrogenase D, in two unrelated patients with elevated D-lactate urinary excretion and plasma concentrations" — [PMID:30931947, abstract]
- Patient 1 is the original Duran 1977 D-lactic aciduria case — QUOTE: "The first patient, born of Sicilian parents from the same village, was originally described by Duran et al.17." — [PMID:30931947, results]
- Patient 1 urinary D-lactate — QUOTE: "he still had an extremely increased D-lactate excretion (mean: 1686 mmol per mol creatinine)" — [PMID:30931947, results]
- Patient 1 plasma D-lactate 0.7 mM — QUOTE: "Plasma analysis also revealed elevated D-lactate concentration (0.7 mM)" — [PMID:30931947, results]
- Patient 1 variant, transcript and zygosity — QUOTE: "identified a homozygous LDHD nonsynonymous variant NM_153486.3:c.1388C>T [https://www.ncbi.nlm.nih.gov/nuccore/NM_153486.3], p.(Thr463Met) (Fig. 3a). Both parents were heterozygous carriers." — [PMID:30931947, results]
- T463M population frequency / rsID — QUOTE: "it is present heterozygously in 27 individuals in the Genome Aggregation Database (gnomAD) and has recently been listed in dbSNP Build 151 as rs76487768825–28" — [PMID:30931947, results]
- Patient 1 parental relatedness confirmed by homozygosity — QUOTE: "Moreover, several large regions of homozygosity were observed, confirming relatedness of the parents (Supplementary Table 1)." — [PMID:30931947, methods]
- Patient 1 has a confounding de novo 11p13 deletion — QUOTE: "Array CGH analysis revealed a de novo 11p13 deletion, known to cause intellectual disability and explaining his syndromal features, though elevated D-lactate levels are not associated with this syndrome18." — [PMID:30931947, results]
- Patient 1 11p deletion (WAGR) judged causal for most of the phenotype — QUOTE: "which was concluded to be likely causal for most of the patient’s phenotype18,54,55" — [PMID:30931947, methods]
- Patient 2 variant, transcript and zygosity — QUOTE: "identifies a separate novel, homozygous nonsynonymous variant NM_153486.3:c.1122G>T, p.(Trp374Cys). Both the mother and the father are heterozygous carriers of the variant." — [PMID:30931947, Fig. 3 legend]
- Patient 2 ethnicity, consanguinity — QUOTE: "Patient 2 was the first child of consanguineous (first cousins) Moluccan parents (Indonesia), born after an uneventful pregnancy." — [PMID:30931947, methods]
- Patient 2 phenotype (West syndrome) — QUOTE: "He had a normal development until the age of 5 months when he developed seizures fitting West syndrome." — [PMID:30931947, methods]
- Patient 2 has a de novo CACNA1B variant considered to explain the epilepsy — QUOTE: "we consider the variant a strong candidate to explain the epilepsy phenotype of the patient" — [PMID:30931947, methods]
- Both patients: no acidosis — QUOTE: "We report two patients with increased D-lactate excretion and elevated D-lactate concentration in plasma, yet without acidosis." — [PMID:30931947, introduction]
- Antibiotics did not correct D-lactate (argues against bacterial origin) — QUOTE: "Repeated antibiotic treatments failed to correct D-lactate levels, making a bacterial origin of this elevated metabolite unlikely." — [PMID:30931947, results]
- Authors: LDHD LOF may be a metabolic phenotype only (neuro causality uncertain) — QUOTE: "given the phenotypic differences between our two patients, and the other genetic findings potentially explaining the rest of their phenotype, the loss-of-function LDHD phenotype in humans could represent a metabolic phenotype only" — [PMID:30931947, discussion]
- Authors: open whether LDHD deficiency has a clinical phenotype — QUOTE: "it remains to be elucidated whether LDHD deficiency is a biochemical anomaly only, or if it contributes to a human clinical phenotype" — [PMID:30931947, discussion]
- Summary statement, LOF — QUOTE: "we report two patients with different homozygous LDHD missense variants, both resulting in enzymatic loss-of-function leading to massive D-lactate excretion and increased D-lactate plasma concentrations" — [PMID:30931947, discussion]

### Other accumulated metabolites
- D-2-hydroxyisovalerate / D-2-hydroxyisocaproate raised in both patients — QUOTE: "Increased levels of D-2-hydroxyisovaleric acid and D-2-hydroxyisocaproic acid were observed in both of our patients." — [PMID:30931947, discussion]
- Chirality determined to be D — QUOTE: "the chirality of these increased metabolites was subsequently also determined to be in the D-isomer form (Fig. 2c–f)" — [PMID:30931947, results]
- Authors' cautious inference of a role in D-2-hydroxyacid metabolism — QUOTE: "could suggest a role for LDHD in the metabolism of these D-isomer metabolites, but more research is needed to clarify the mechanism of this little-known pathway" — [PMID:30931947, discussion]
- Bacterial origin of the branched-chain D-2-hydroxyacids not excluded — QUOTE: "An intestinal bacterial origin of the D-2-branched-chain hydroxyacids cannot be ruled out completely." — [PMID:30931947, discussion]

### Sources of D-lactate
- Exogenous and endogenous sources (methylglyoxal) — QUOTE: "D-lactate is acquired exogenously by consumption of foods, by metabolism of chemicals such as propylene glycol, by intestinal bacteria production, or endogenously by methylglyoxal metabolism—a toxic product that is converted to D-lactate4–8." — [PMID:30931947, introduction]

### Zebrafish model (function in vivo)
- ldhd mutant allele — QUOTE: "This line carries a disrupted essential donor splice site following exon 3 resulting in a premature stop codon (Allele sa15623; Zv9 chr25:g.13920446T>G)30." — [PMID:30931947, results]
- MZ ldhd−/− larvae: D-lactate up, L-lactate unchanged — QUOTE: "metabolic analysis revealed elevated levels of D-lactate, but not L-lactate, in ldhd−/− larvae compared to wildtype (Fig. 4b, c)" — [PMID:30931947, results]
- No morphological phenotype; fish viable and fertile — QUOTE: "ldhd−/− embryos showed no visible abnormalities compared to wildtype (Fig. 4a), and displayed no ocular abnormalities at 5 dpf (Supplementary Fig. 1)" — [PMID:30931947, results]
- Rescue by WT human LDHD mRNA — QUOTE: "ldhd−/− uninjected embryos showed a significant D-lactate increase that was restored to baseline levels by mRNA microinjection of the wildtype LDHD sequence" — [PMID:30931947, results]
- Patient variants fail to rescue — QUOTE: "microinjection of variant Thr463Met LDHD or Trp374Cys LDHD mRNA did not rescue the metabolic phenotype (Fig. 4b)" — [PMID:30931947, results]
- Stereospecificity inferred in vivo — QUOTE: "levels of L-lactate were not significantly altered among the different conditions, establishing that LDHD is stereospecific for D-lactate only (Fig. 4c)" — [PMID:30931947, results]
- Conclusion on activity of the variants — QUOTE: "This confirmed that LDHD is responsible for D-lactate metabolism, and that the homozygous variants present in our patients both result in decreased LDHD activity." — [PMID:30931947, results]
- Conclusion on the human gene — QUOTE: "We therefore conclude that LDHD is essential for human D-lactate metabolism." — [PMID:30931947, discussion]
- Construct used the isoform-2 transcript although variants are named on NM_153486.3 — QUOTE: "Human LDHD cDNA (accession number NM_194436.1) in the entry vector pCMV-ENTRY (Origene, Rockville, MD, USA) was inserted into the expression vector pCS2+/GW" — [PMID:30931947, methods]
- NOTE: no in vitro enzyme assay of the human variants in this paper; "loss-of-function"/"decreased activity" rests on failure of zebrafish rescue (no % activity given).

---

## PMID:37863926 Jin 2023 Nat Commun (FT) — mouse LDHD crystal structures, substrate spectrum, Mn2+, disease-variant analysis

NOTE: all residue numbers in this paper are MOUSE LDHD (mLDHD, construct residues 22–484) unless prefixed hLDHD. The cached text contains NO Ldhd knockout-mouse experiment and NO PDB accession codes for the mLDHD structures (the Data availability section is not in the cache); the only PDB IDs present are comparators 7QH2 and 6LPN. Kinetics use the artificial PMS/DCIP acceptor pair.

### Molecular function / cofactors
- Reaction and scope (abstract) — QUOTE: "We demonstrate that mLDHD is an Mn2+-dependent general dehydrogenase which exhibits catalytic activity for D-lactate and other D-2-hydroxyacids containing hydrophobic moieties, but no activity for their L-isomers or D-2-hydroxyacids containing hydrophilic moieties." — [PMID:37863926, abstract]
- Family membership, FAD not NAD — QUOTE: "belong to the 2-hydroxyacid dehydrogenase subfamily of the VAO/PCMH flavoprotein family, all members of which consist of a conserved FAD-binding domain and a variable substrate-binding domain, and use FAD rather than NAD as cofactor23,24,39" — [PMID:37863926, introduction]
- FAD bound (spectral) and monomer in solution — QUOTE: "The purified mLDHD protein exhibits a characteristic yellow color of FAD with maximum absorbance at 450 nm, and exists as a monomer in solution (Supplementary Fig. 2a)." — [PMID:37863926, results]
- FAD stoichiometry — QUOTE: "the molar ratio of FAD:protein is 0.73 ± 0.04 (mean ± SEM) in the wild-type (WT) mLDHD protein" — [PMID:37863926, results]
- FAD non-covalent, tight — QUOTE: "There is a non-covalently bound FAD at the active site, which is apparently derived from the expression system, indicating that FAD binds to mLDHD tightly." — [PMID:37863926, results]
- No activity without metal — QUOTE: "As expected, the EDTA-treated mLDHD has no activity in the absence of metal ions (Fig. 1a)." — [PMID:37863926, results]
- Metal preference Mn2+ > Co2+ > Ni2+ > Ca2+; none with Mg/Zn/Cd/Cu — QUOTE: "mLDHD exhibits the highest activity in the presence of Mn2+, and moderate to weak activity in the presence of Co2+, Ni2+ and Ca2+ (about 49%, 16% and 11% of the activity compared to Mn2+, respectively), but no measurable activity in the presence of Mg2+, Zn2+, Cd2+, and Cu2+ (Fig. 1a)" — [PMID:37863926, results]
- Metal is a cofactor — QUOTE: "It is evident that the divalent cation serves as a cofactor but not an activator for mLDHD." — [PMID:37863926, results]
- Mn2+ optimum and pH optimum — QUOTE: "mLDHD exhibits optimal specific activity with the Mn2+ concentration in the range of 30–200 μM (Supplementary Fig. 3)" — [PMID:37863926, results]
- pH optimum 7.4 — QUOTE: "mLDHD displays the maximum specific activity at pH 7.4 (Fig. 1b)" — [PMID:37863926, results]
- Kinetics for D-lactate (mouse enzyme, PMS/DCIP) — QUOTE: "with a Vmax of 1.22 ± 0.01 μmol·min−1·mg−1, a KM of 122.0 ± 4.5 μM and a kcat of 61.0 ± 0.6 min−1" — [PMID:37863926, results]
- No activity and no binding for L-lactate — QUOTE: "mLDHD exhibits no activity for L-lactate and has no detectable binding with L-lactate. These results indicate that mLDHD has high stereo-selectivity for D-lactate over L-lactate." — [PMID:37863926, results]
- Branched-chain D-2-hydroxyacids are better substrates than D-lactate — QUOTE: "mLDHD can convert D-2-hydroxyisovalerate, D-2-hydroxyisocaproate and D-2-hydroxy-3-methylvalerate into 2-ketoisovalerate, 2-ketoisocaproate, and 2-keto-3-methylvalerate, respectively, with comparable Vmax and kcat values and significantly decreased KM values compared to those for D-lactate, resulting in substantially increased catalytic efficiencies (5.5-8.0 folds)" — [PMID:37863926, results]
- Not a substrate: D-3-hydroxybutyrate — QUOTE: "however, mLDHD shows no activity towards D-3-hydroxybuyrate (Fig. 1d and Table 1)" — [PMID:37863926, results]
- Linear D-2-hydroxyacids C4–C6 are substrates — QUOTE: "mLDHD also exhibits activity towards D-2-hydroxybutyrate, D-2-hydroxyvalerate and D-2-hydroxyhexanoate with comparable Vmax and kcat values and moderately decreased KM values compared to these for D-lactate" — [PMID:37863926, results]
- Not substrates: glycolate, D-malate, D-2-hydroxyglutarate, D-2-hydroxy-3-aminopropanoate — QUOTE: "we examined whether mLDHD has activity towards glycolate and D-2-hydroxyacids with hydrophilic moieties attached to the C2 atom such as D-2-hydroxy-3-amino-propanoate, D-malate and D-2-hydroxyglutarate (Supplementary Fig. 4). The results show that mLDHD has no activity towards these hydroxyacids (Fig. 1d)." — [PMID:37863926, results]
- Summary of substrate scope — QUOTE: "mLDHD is an Mn2+-dependent general dehydrogenase for a broad range of D-2-hydroxyacids with small to moderate-size hydrophobic moieties at the C2 atom. However, it has no activity for glycolate or D-2-hydroxyacids with hydrophilic moieties at the C2 atom." — [PMID:37863926, results]
- Table 1 row, D-lactate (Vmax, KM µM, kcat min−1, kcat/KM) — QUOTE: "D-lactate (D-LAC)Pyruvate (PYR)1.22 ± 0.01122.0 ± 4.561.0 ± 0.60.50" — [PMID:37863926, Table 1]
- Table 1 row, D-2-hydroxyisovalerate (KM 13.9 µM) — QUOTE: "D-2-hydroxyisovalerate (D-2-HIV)2-ketoisovalerate (2-KIV)1.11 ± 0.0213.9 ± 1.255.5 ± 0.93.99" — [PMID:37863926, Table 1]
- Table 1 row, DL-2-hydroxyisocaproate (KM 16.4 µM) — QUOTE: "DL-2-hydroxyisocaproate (DL-2-HIC)2-ketoisocaproate (2-KIC)0.902 ± 0.01716.4 ± 0.745.1 ± 0.82.75" — [PMID:37863926, Table 1]
- "Secondary metabolic enzyme" judgement from kcat — QUOTE: "This indicates that mLDHD is a secondary metabolic enzyme, which is in agreement with the high tissue-specific expression of mLDHD43 and the miniscule amount of D-lactate (and very likely other D-2-hydroxyacids) in the human body under normal physiological conditions3." — [PMID:37863926, results]
- Assay electron acceptors are artificial — QUOTE: "In our in vitro activity assay, phenazine methosulfate (PMS) was used as the primary oxidant followed by 2,6-dichloroindophenol (DCIP)." — [PMID:37863926, results]
- Physiological acceptor declared unknown by these authors — QUOTE: "However, the primary oxidant under physiological conditions is unknown, and thus it remains unclear whether mLDHD would function as an oxidase when molecular oxygen is used as the oxidant or a dehydrogenase when other electron acceptor(s) are used as the oxidant in a coupled oxidation-reduction reaction." — [PMID:37863926, results]

### Structure
- Structures solved and resolution — QUOTE: "we determined the crystal structure of wild-type (WT) mLDHD in FAD-bound form (mLDHDFAD, 1.70 Å resolution) and in complex with FAD, Mn2+, and D-lactate (mLDHDFAD+Mn+D-LAC, 1.73 Å resolution) (Supplementary Data 1)" — [PMID:37863926, results]
- One molecule per asymmetric unit — QUOTE: "In all structures, there is one mLDHD molecule in the asymmetric unit" — [PMID:37863926, results]
- Domain organisation — QUOTE: "The FAD-binding subdomains A and B are colored in pink and green, the substrate-binding domain in orange, and the C-terminal domain in yellow, respectively." — [PMID:37863926, Fig. 2 legend]
- Active site location — QUOTE: "The active site resides at the interface of the FAD-binding domain and the substrate-binding domain, and is composed of the FAD-binding site and the substrate-binding site (Fig. 2b)." — [PMID:37863926, results]
- Substrate-loading channel residues (mouse numbering) — QUOTE: "formed by both hydrophilic and hydrophobic residues, including Glu58, Thr99, Gly159, Ala160, His348, Asn349, and Tyr352 (Fig. 2b)" — [PMID:37863926, results]
- Mn2+ ligands (mouse numbering): His398, His405, Glu442 + flavin O4 + substrate — QUOTE: "Mn2+ forms six coordination bonds in an octahedral geometry with the side chains of His398, His405, and Glu442, the O4 atom of the flavin moiety of FAD, and the C1-carboxyl and C2-hydroxyl groups of D-lactate (Fig. 3b)" — [PMID:37863926, results]
- Arg347 binds substrate carboxylate (mouse; = human isoform-1 Arg370) — QUOTE: "the C1-carboxyl group of D-lactate also forms two hydrogen bonds with the sidechain of Arg347" — [PMID:37863926, results]
- Catalytic/binding residue assignment — QUOTE: "residues His398, His405, and Glu442 are responsible for the Mn2+ binding, and Arg347 and His443 for the substrate/product binding (Fig. 3b, d). Mutations of these residues to alanine all lead to complete abrogation of the activity" — [PMID:37863926, results]
- His443 as catalytic base (mouse; = human isoform-1 His466, UniProt ACT_SITE) — QUOTE: "The sidechain of His443 recognizes the C2-hydroxyl group and acts as a Lewis base to extract a proton from the hydroxyl group." — [PMID:37863926, results]
- Hydride transfer to FAD N5 — QUOTE: "the hydride ion on the C2 atom is abstracted by the N5 atom of the flavin moiety of FAD, leading to formation of the C2-keto group and the flavin anion" — [PMID:37863926, results]
- Two subsites — QUOTE: "The substrate-binding site of mLDHD consists of a positively charged pocket (subsite A) to bind Mn2+ and the glycolate moiety of substrate and a hydrophobic pocket (subsite B) to bind the hydrophobic moiety of substrate." — [PMID:37863926, results]
- Subsite B residues (mouse) — QUOTE: "The subsite B of mLDHD is a large, hydrophobic pocket consisting of Trp351, Ile407, Val101 and Ser365 with considerable flexibility to accommodate a variety of hydrophobic moieties of small to medium size (Fig. 3a)." — [PMID:37863926, discussion]
- Why L-lactate is excluded (docking) — QUOTE: "To avoid steric conflicts between L-lactate and FAD, the C2 atom of L-lactate is pushed away from the N5 atom of FAD (3.6 Å for L-lactate vs. 3.1 Å for D-lactate)." — [PMID:37863926, results]
- Structural homologues with PDB IDs (comparators, not LDHD) — QUOTE: "identified two best candidates: A. woodii LctD (PDB: 7QH2)49 with a Z-score of 47.2 and human D2HGDH (PDB: 6LPN)40 with a Z-score of 44.9" — [PMID:37863926, discussion]
- Contrast with D2HGDH substrate specificity — QUOTE: "Human D2HGDH has high activity for D-2-hydroxyglutarate and D-malate40. Mouse LDHD has a broad specificity for D-2-hydroxyacids containing hydrophobic moieties at the C2 atom." — [PMID:37863926, discussion]
- Human vs mouse sequence relation; human protein insoluble in E. coli — QUOTE: "Human and mouse LDHDs share high sequence identity (81.5%) and similarity (92.6%). The major difference is that human LDHD (hLDHD) contains an insertion of 23 residues (residues 210–232) compared to mouse LDHD (mLDHD) (Supplementary Fig. 1)." — [PMID:37863926, results]
- Human insertion is a surface loop far from the active site (AlphaFold comparison) — QUOTE: "This insertion is positioned far away from the FAD-binding site and the substrate-binding site, and thus is unlikely to affect the binding of FAD and/or substrate as well as the catalytic reaction (Supplementary Fig. 11)." — [PMID:37863926, results]
- N-terminal presequence — QUOTE: "The N-terminal 1–21 residues of mLDHD are suggested to be a consensus mitochondrial targeting sequence and thus were removed." — [PMID:37863926, methods]

### Disease variants mapped onto the structure (human isoform-1 -> mouse numbering)
- Residue correspondence — QUOTE: "The T251M, R370W, W374C, and T463M mutations of hLDHD correspond to T228M, R347W, W351C, and T440M of mLDHD, respectively." — [PMID:37863926, results]
- All four mouse-equivalent mutants lose ~90% activity on three substrates — QUOTE: "the activity assay shows that all the mutants lose about 90% of the activity towards D-lactate, D-2-hydroxyisovalerate and DL-2-hydroxyisocaproate (Fig. 4a and Supplementary Table 1)" — [PMID:37863926, results]
- Thermostability reduced — QUOTE: "the melting temperatures (Tm) of the mutants are decreased by 10-15 °C, indicating that these mutations impair the thermostability of mLDHD (Supplementary Fig. 10b)" — [PMID:37863926, results]
- FAD retained by R347W/W351C, lost by T228M/T440M — QUOTE: "the R347W and W351C mutants retain the FAD characteristic absorption peak, indicative of FAD binding albeit with lower occupancies; in contrast, the T228M and T440M mutants do not exhibit the FAD characteristic absorption peak, suggesting the absence of FAD binding (Supplementary Fig. 10c–f)" — [PMID:37863926, results]
- R347W (human R370W) mechanism — QUOTE: "Modeling study shows that the R347W mutation causes steric conflicts with the substrate and thus disrupts the substrate binding (Fig. 4c)." — [PMID:37863926, results]
- W351C (human W374C) mechanism — QUOTE: "The W351C mutation disrupts these hydrophobic interactions, leading to destabilization of the conformation of the subsite B and thus impairment of the substrate binding." — [PMID:37863926, results]
- T228M (human T251M) mechanism — QUOTE: "As Glu226 on this loop has direct interactions with FAD, the T228M mutation might destabilize the conformation of the η4-β7 loop and hence affect the FAD binding." — [PMID:37863926, results]
- T440M (human T463M) mechanism — QUOTE: "The T440M mutation causes steric clashes with the backbones of His443 and Gly444, leading to distortion of the α11-α12 loop and displacements of His443 and Glu442, which subsequently interfere with the binding of FAD, substrate and metal ion." — [PMID:37863926, results]
- Overall conclusion on the variants — QUOTE: "the disease-associated mutations either disrupt the substrate binding (R347W and W351C) or the FAD binding (T228M and T440M), leading to abolishment of the enzymatic activity" — [PMID:37863926, results]

### Localisation / physiology statements (secondary, cited from earlier work)
- Inner-membrane localisation asserted (cites refs 8,41,42; not shown in this paper) — QUOTE: "FAD-dependent D-LDHs were also identified in mammals including human and mouse, which are localized in the mitochondrial inner membrane and share high sequence similarity with yeast D-LDH (DLD1, Supplementary Fig. 1)8,41,42" — [PMID:37863926, introduction]
- Expression — QUOTE: "Human D-LDH (also called LDHD) is highly expressed in tissues with high metabolic rates and abundant mitochondria43." — [PMID:37863926, introduction]
- Sources of D-lactate — QUOTE: "In humans, D-lactate can be derived from food, metabolism of intestinal bacteria, or endogenous glyoxalase pathway." — [PMID:37863926, discussion]
- Proposed link to BCAA metabolism (branched-chain ketoacid products) — QUOTE: "we demonstrate that besides BCAA catabolism, BCKAs can also be generated by oxidation of branched-chain D-2-hydroxyacids (D-2-hydroxyisovalerate, D-2-hydroxyisocaproate and D-2-hydroxy-3-methylvalerate) catalyzed by LDHD" — [PMID:37863926, discussion]
- Hedged BCAA conclusion — QUOTE: "Thus, LDHD may play an important role not only in the metabolism of branched-chain D-2-hydroxyacids but also the metabolism of BCAAs." — [PMID:37863926, discussion]
- Proposed biomarkers — QUOTE: "These substrates can serve as potential biomarkers of LDHD deficiency, providing differential diagnostic criteria for D-lactic acidosis patients with LDHD mutations or with short bowel syndrome." — [PMID:37863926, discussion]
- Disease summary by these authors — QUOTE: "LDHD deficiency is caused by loss-of-function mutations8,43,44. Clinically, LDHD deficiency is marked by elevated levels of D-lactate in urine and plasma and manifested by neurological symptoms, hyperuricemia and gout8,44." — [PMID:37863926, discussion]

---

## PMID:38413804 To 2024 Nat Metab, PMF-seq (FT) — human LDHD passes electrons from D-lactate to cytochrome c

- Headline claim — QUOTE: "We demonstrate that human D-lactate dehydrogenase specifically conveys electrons from D-lactate into cytochrome c to support mitochondrial membrane polarization." — [PMID:38413804, abstract]
- Prior state of knowledge; inner-membrane association is cited, not shown — QUOTE: "While human LDHD is known to be associated with the mitochondrial inner membrane22, to the best of our knowledge, its role in electron transfer from d-lactate to cytochrome c has never been directly demonstrated." — [PMID:38413804, results]
- Yeast/plant precedent — QUOTE: "d-lactate can feed into the respiratory chain via the enzyme d-lactate dehydrogenase (LDHD), which transfers electrons directly to cytochrome c by oxidizing d-lactate17,18" — [PMID:38413804, results]
- LDHD KO human cells (A375, HepG2): D-lactate-driven membrane potential blunted — QUOTE: "although they could mount a membrane potential response to ascorbate/TMPD (an artificial substrate combination that feeds directly into cytochrome c), their response to d-lactate was blunted (Fig. 3c)" — [PMID:38413804, results]
- Purified human LDHD is a dimer on gel filtration — QUOTE: "Human LDHD, which has a predicted molecular weight of ~50 kDa, ran as a dimer during gel filtration chromatography (Fig. 3d,e)." — [PMID:38413804, results]
- Direct electron transfer to cytochrome c with purified enzyme — QUOTE: "Using the purified LDHD, we could confirm direct electron transfer from d-lactate to cytochrome c by monitoring its haem absorbance (Fig. 3f)." — [PMID:38413804, results]
- Human-enzyme kinetics with cytochrome c as acceptor — QUOTE: "found the kcat and KM of this reaction to be 103 min−1 and 112 μM, respectively" — [PMID:38413804, results]
- D-2-hydroxybutyrate also reduces cytochrome c — QUOTE: "we identified d-2-hydroxybutyrate as another LDHD substrate that can be used to reduce cytochrome c (Fig. 3g)" — [PMID:38413804, results]
- Authors' conclusion — QUOTE: "human cells can modestly energize their mitochondria in an LDHD-dependent manner by directly transferring electrons from d-lactate to cytochrome c" — [PMID:38413804, results]
- Methylglyoxal sensitivity unchanged in LDHD KO cells (argues against an essential detox role in these cells) — QUOTE: "we tested the wild-type and KO cells’ sensitivity to methylglyoxal but saw little difference (Extended Data Fig. 5b,c)" — [PMID:38413804, results]
- Recombinant protein was human isoform 2 (484 aa, MANE) made in Pichia with a yeast presequence — QUOTE: "A Pichia codon-optimized construct containing the mitochondrial targeting sequence of DLD1 from Komagataella phaffii, followed by human LDHD isoform 2, a C-terminal TEV cleavage site, and a 10× histidine tag" — [PMID:38413804, methods]
- Assay conditions — QUOTE: "The reaction buffer contained 50 mM potassium phosphate pH 8.5, 200 µM bovine heart cytochrome c (Sigma) and the required concentration of substrate." — [PMID:38413804, methods]
- NOTE: electron transfer to cytochrome c implies the acceptor-facing side is the intermembrane space (cytochrome c is an IMS protein); the authors do not state a topology. This conflicts with de Bari 2002 (matrix face) — see conflicts.

---

## PMID:31638601 Drabkin 2019 JCI (ABS only; `fetch-pmid --force` got HTTP 403 from PMC, and the PubMed MCP full-text tool also returned empty for PMC6877321)

- Variant sits in the putative catalytic site; raises blood D-lactate — QUOTE: "gout can be caused by a mutation in LDHD within the putative catalytic site of the encoded d-lactate dehydrogenase, resulting in augmented blood levels of d-lactate" — [PMID:31638601, abstract]
- Proposed mechanism: renal D-lactate secretion exchanged for urate reabsorption — QUOTE: "Consequent excessive renal secretion of d-lactate in exchange for uric acid reabsorption culminated in hyperuricemia and gout." — [PMID:31638601, abstract]
- Tissue expression — QUOTE: "LDHD expression is enriched in tissues with a high metabolic rate and abundant mitochondria" — [PMID:31638601, abstract]
- Mitochondrial localisation (overexpressed human LDHD in cells) — QUOTE: "d-lactate dehydrogenase resides in the mitochondria of cells overexpressing the human LDHD gene" — [PMID:31638601, abstract]
- R370W does not mislocalise — QUOTE: "Notably, the p.R370W mutation had no effect on protein localization." — [PMID:31638601, abstract]
- Mouse D-lactate injection — QUOTE: "injection of d-lactate into naive mice resulted in hyperuricemia" — [PMID:31638601, abstract]
- Generalisation — QUOTE: "hyperuricemia and gout can result from the accumulation of metabolites whose renal excretion is coupled to uric acid reabsorption" — [PMID:31638601, abstract]
- NOTE (not in cache, could not read full text): the abstract does not name the transporter (URAT1/SLC22A12 or other), the cDNA change, the transcript, zygosity, the ethnicity or D-lactate values. Those details are available only second-hand from the cached comparison tables of Kwong 2021 and Sloth 2025 (quoted below): Bedouin-Israeli consanguineous kindred, homozygous c.1108C>T p.(Arg370Trp) on NM_153486.3, plasma D-lactate 3.16 ± 0.63 mM, no neurological symptoms.

---

## PMID:34258137 Kwong 2021 JIMD Rep (FT; cached text is fragmented at citation markers)

- Variants (abstract) — QUOTE: "we identified compound heterozygous variants in the LDHD gene, which encodes the d-lactate dehydrogenase, consisting of a splice site variant c.469+1dupG and a missense variant c.752C>T, p.(Thr251Met)" — [PMID:34258137, abstract]
- Transcript for both variants, segregation figure — QUOTE: "Two LDHD heterozygous variants, NM_153486.3: c.469+1dupG and c.752C>T, p.(Thr251Met) were confirmed by genomic DNA sequencing." — [PMID:34258137, Fig. 1 legend]
- Carriers: father splice, mother missense — QUOTE: "The father is the carrier of the intronic splice site variant and the mother is the carrier of the missense variant (Figure 1A)." — [PMID:34258137, genetic analysis]
- Splice allele not expressed (cDNA from fibroblasts) — QUOTE: "Sanger sequencing of the cDNA revealed that only the allele with the missense variant was expressed while cDNA with the splice site variant was not identified (Figure 1A)." — [PMID:34258137, RT-PCR]
- Ethnicity, non-consanguineous — QUOTE: "Our patient was 14 years old and born of a nonconsanguineous Chinese couple with no relevant family history." — [PMID:34258137, case report]
- Serum D-lactate — QUOTE: "The serum d-lactate level was subsequently detected to be elevated (0.61 mmol/L, reference value: 0-0.25 mmol/L)." — [PMID:34258137, abstract]
- Neurological phenotype — QUOTE: "We report here a patient with developmental delay, cerebellar ataxia, and transient hepatomegaly." — [PMID:34258137, abstract]
- Ataxia transient — QUOTE: "Mild cerebellar ataxia was detected at 5 years of age with resolution after 10." — [PMID:34258137, case report]
- Urinary organic acids — QUOTE: "She had persistent increase in lactate and organic acids excretion including 3‐hydroxybuyrate, 2‐hydroxyisovalerate, 2‐hydroxy‐3‐methylvalerate, and 2‐hydroxyisocaproate in urine." — [PMID:34258137, case report]
- Plasma BCAA normal — QUOTE: "The plasma amino acid profile was unremarkable with normal levels of branched chain amino acid." — [PMID:34258137, case report]
- Urate marginally raised, no gout — QUOTE: "Blood uric acid of our patient was marginally raised at 316 μmol/L (normal 105‐300 μmol/L) and no gout arthropathy was identified." — [PMID:34258137, discussion]
- Complex IV mildly reduced in fibroblasts — QUOTE: "It revealed reduction in complex IV activity (221 mU/UCII; reference: 288‐954)." — [PMID:34258137, enzyme analysis]
- Authors doubt D-lactate itself explains complex IV result — QUOTE: "it seems unlikely that elevated d‐lactate as observed in the patient's plasma is responsible for the reduced complex IV activity observed in the cultured fibroblasts" — [PMID:34258137, discussion]
- LDHD expression in fibroblasts unknown — QUOTE: "However, whether the enzyme is expressed in fibroblasts is at present unknown." — [PMID:34258137, discussion]
- Causality for neurological features uncertain — QUOTE: "The association of LDHD deficiency with the neurological features and the additional clinical presentations remained elusive." — [PMID:34258137, discussion]
- Monroe patients' neuro signs possibly explained by other defects — QUOTE: "the neurological signs of the two patients in the first study could be potentially explained by the additional genetic defects identified" — [PMID:34258137, discussion]
- Metabolic phenotype is the consistent part — QUOTE: "Other than the clinical presentations, the metabolic phenotypes can be well explained by LDHD mutations in all the reports." — [PMID:34258137, discussion]
- Drabkin kindred as summarised here: gout, no neuro — QUOTE: "The affected members of the kindred presented with hyperuricemia and gout arthropathy with no neurological symptoms reported." — [PMID:34258137, discussion]
- Drabkin kindred D-lactate and urate (table cell) — QUOTE: "Average plasma d‐lactate concentration: 3.16 ± 0.63 mM" — [PMID:34258137, Table 1]
- Urate-competition mechanism as phrased here (no transporter named) — QUOTE: "lactate and organic acid including beta‐hydroxybutyrate may compete with and reduce the renal clearance of uric acid leading to high level of serum uric acid associated with gout" — [PMID:34258137, discussion]
- Tissue expression (GTEx + Drabkin RT-PCR) — QUOTE: "human LDHD transcripts were abundant in tissues with a high metabolic rate in which liver, skeletal muscle, heart, and colon had the highest expression levels" — [PMID:34258137, discussion]
- Methylglyoxal source; inner-membrane localisation cited from rat liver — QUOTE: "A previous study demonstrated that rat liver mitochondria can take up external d‐lactate, metabolize it by d‐lactate dehydrogenase located in mitochondrial inner membrane." — [PMID:34258137, discussion]
- D-lactate sources — QUOTE: "It is derived from exogenous source including food consumption, intestinal carbohydrate‐fermenting bacteria production, or endogenously in a minor methylglyoxal metabolism pathway converting toxic methylglyoxal to d‐lactate." — [PMID:34258137, introduction]
- Normal circulating D-lactate — QUOTE: "Circulating d‐lactate exists in a very low concentration (5‐20 μmol/L) in normal individuals." — [PMID:34258137, introduction]

## PMID:32907636 (FT) — WES of paediatric suspected mitochondrial disease, southern China (first report of the Kwong patient)

- LDHD listed among non-mitochondrial-disease genes — QUOTE: "Twelve patients (18%) had mutations in 10 non-MD-associated genes, i.e. ATP1A3, ALDH5A1, ARX, FA2H, KCNT1, LDHD, NEFL, NKX2-2, TBCK, and WAC." — [PMID:32907636, results]
- Patient 23 row: variants and diagnosis (no transcript given in the row) — QUOTE: "LDHDc.469+1dup and c.752C>T, p.(Thr251Met)D-lactic aciduria" — [PMID:32907636, Table 1]
- Complex IV deficiency called secondary — QUOTE: "secondary complex IV deficiency was detected in two non-MD patients with ARX and LDHD mutations" — [PMID:32907636, discussion]
- NOTE: same individual as Kwong 2021 (female, infancy onset, 13 yo in this table; Kwong states the variants "have been reported in our previous study"). Count once.

---

## PMID:40678184 Sloth 2025 JIMD Rep (FT) — homozygous deletion of LDHD exons 1–7; literature comparison

### New patient
- Variant and transcript (isoform-2 / MANE numbering) — QUOTE: "involving exon one to seven of the LDHD gene (NM_194436.3c: 1_930del, p.M1_Q310del)" — [PMID:40678184, case presentation]
- Deletion also removes two other genes — QUOTE: "The loss involved the first exons of the LDHD gene in addition to ZFP1 (zinc finger protein, OMIM # 617230) and CTRB2 (Chymotrypsinogen B2, OMIM #619620)." — [PMID:40678184, case presentation]
- Zygosity and carriers — QUOTE: "Analysis of the parents' genetic material confirmed heterozygosity for the same deletion in both parents." — [PMID:40678184, case presentation]
- Family origin / relatedness — QUOTE: "The patient's parents are from the same village in Iraq and distantly related." — [PMID:40678184, case presentation]
- Phenotype — QUOTE: "The patient was referred to us at the age of 3 years with mild to moderate psycho‐motor developmental delay and metabolic acidosis." — [PMID:40678184, case presentation]
- D-lactate values — QUOTE: "Analysis of D‐lactate using a D‐lactate assay showed elevated D‐lactate at 1.4 mmol/mol creatinine (ref: < 0.021 mmol/mol creatinine). P‐D‐lactate was elevated at 1.2 mmol/L (ref: < 0.026 mmol/L)." — [PMID:40678184, case presentation]
- Acid-base — QUOTE: "Acid–base balance showed decreased pH at 7.24, base excess at −4.8 mmol/L, and reduced standard‐bicarbonate at 19.5 mmol/L; two measurements of p‐L‐lactate were normal at 0.9 and 1.5 mmol/L, respectively." — [PMID:40678184, case presentation]
- Urate — QUOTE: "Urate was slightly elevated at 0.38 (mmol/L; ref: 0.12–0.32)." — [PMID:40678184, case presentation]
- Urine organic acids — QUOTE: "A urine metabolic screening showed elevated excretion of 2‐hydroxyisovaleric acid and 2‐hydroxyisocaproic acid, as well as traces of 2‐hydroxy‐3‐methylvaleric acid and very increased excretion of lactate." — [PMID:40678184, case presentation]
- Plasma amino acids normal — QUOTE: "Metabolic analysis showed normal amino acids and acylcarnitines in plasma." — [PMID:40678184, case presentation]
- Authors' causal judgement for this patient (with caveat) — QUOTE: "though it cannot formally be ruled out that ZFP1 and CTRB2 contribute to the patient's phenotype, we find it likely that the metabolic findings and his neurodevelopmental symptoms are due to the LDHD defect" — [PMID:40678184, discussion]

### Cohort statements
- Number of reported patients — QUOTE: "pathogenic variants in the LDHD gene have been identified in 18 other patients (from seven families) described in other reports" — [PMID:40678184, discussion]
- Zygosity across cohort — QUOTE: "all patients, except one, have homozygous pathogenic variants in the LDHD gene of varying types" — [PMID:40678184, discussion]
- Confounding second genetic findings — QUOTE: "In five patients, genetic variants in genes other than the LDHD gene have been observed, making it difficult to know which clinical features are caused by the LDHD variants." — [PMID:40678184, discussion]
- Universal biochemical feature — QUOTE: "the clinical symptoms vary among patients with pathogenic variants in the LDHD gene, but an elevated level of D-lactate in plasma and urine is found in all patients" — [PMID:40678184, abstract]
- Phenotypic spectrum — QUOTE: "with some patients having only increased plasma urate/gout and others presenting with neurological findings and early‐onset psycho‐motor developmental delay" — [PMID:40678184, discussion]
- Uncertainty about the neurological fraction — QUOTE: "The true fraction of patients with neuro‐developmental signs is uncertain because of the co‐occurrence of other diseases with probable neurological impact in three patients from this group, including 11p syndrome, decreased activity of complex IV of the respiratory chain, and West syndrome [2, 4]." — [PMID:40678184, discussion]
- Attribution difficulty — QUOTE: "Therefore, in these patients, it is difficult to determine whether the clinical picture can solely be attributed to the LDHD deficiency." — [PMID:40678184, discussion]
- No genotype–phenotype correlation — QUOTE: "Altogether, there is no obvious correlation between the type of pathogenic variant of the LDHD gene and the phenotype." — [PMID:40678184, discussion]
- Other D-2-hydroxyacids only reported in the neuro group (possibly ascertainment) — QUOTE: "elevated levels of D‐2‐hydroxyacids other than D‐lactate were not mentioned in the literature but may not have been analyzed in this setting [11, 12]" — [PMID:40678184, discussion]
- Disease/gene MIM numbers — QUOTE: "human D‐lactate dehydrogenase deficiency (OMIM 245450). This disease is caused by pathogenic variants in the LDHD gene (OMIM 607490) leading to decreased activity of LDHD." — [PMID:40678184, introduction]
- EC number and reaction — QUOTE: "The formed or absorbed D‐lactate can be oxidized, catalyzed by the enzyme D‐lactate dehydrogenase (EC: 1.1.2.4 LDHD), into pyruvate [1]." — [PMID:40678184, introduction]
- Sources of D-lactate — QUOTE: "D‐lactate can originate from exogenous sources like food products as well as endogenously via the methylglyoxal metabolic pathway [1, 4, 5, 6]." — [PMID:40678184, introduction]

### Sloth Table 2 — every reported patient/family (columns in cached order: Drabkin; Bardin x3; Monroe/Duran; Monroe; Kwong; Sloth)
Column header as cached — QUOTE: "Drabkin et al. [12]Bardin et al. [11]Bardin et al. [11]Bardin et al. [11]Monroe et al. [2], Duran et al. [13]Monroe et al. [2]Kwong et al. [4]Our patient" — [PMID:40678184, Table 2]

NOTE: the cached table is a flattened cell stream; column assignment below is by cell order (8 columns) and was cross-checked against the primary papers where cached. Reconstructed table (my words):

| # | Report | Family / ethnicity (as given by Sloth) | Consanguinity | Variant (as printed in Sloth Table 2) | Transcript | Zygosity | Neuro | Gout / urate | D-lactate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Drabkin 2019 | Bedouin-Israeli kindred | yes | c.1108C>T p.(Arg370Trp) | NM_153486.3 | homozygous | none reported | gout in adults and children; plasma urate adults 10.34 ± 1.84 mg/dL, children 6.75 ± 0.7 mg/dL | plasma 3.16 ± 0.63 mmol/L; urine 32.08 ± 5.77 mmol/L |
| 2 | Bardin 2023 fam. 1 | Melanesian, 3 affected sibs | no | "c.206 T>C; rs1035398551 p.(Val69Ala)" (Bardin abstract prints c.206C>T, no protein change) | NM_153486.3 | homozygous | none reported | early-onset gout from 13, 16, 21 y; urate 0.71, 0.74, 0.94 mmol/L | serum 0.306, 0.558, 0.632 mmol/L; urine 21.5, 7.8, 18.1 mmol/L |
| 3 | Bardin 2023 fam. 2 | Vietnamese, 2 affected sibs | no | c.1363dupG p.(AlaGly432fsTer58) (Sloth calls it "nonsense"; Bardin says frameshift) | NM_153486.3 | homozygous | one sib severe neurological features at 34 y, normal earlier; other none | gout from 21 and 9 y; urate 0.55, 0.58 mmol/L | not measured |
| 4 | Bardin 2023 isolated | "Parents from Algeria" (Bardin abstract: "a Moroccan man") | not mentioned | c.752C>T p.(Thr251Met) | NM_153486.3 | homozygous | none reported | gout from 19 y; urate 0.46 mmol/L | plasma > 0.5 mmol/L; urine 6.15 mmol/L |
| 5 | Monroe 2019 P1 (= Duran 1977) | Sicilian (Italy) | some degree | c.1388C>T p.(Thr463Met) | NM_153486.3 | homozygous | severe mental/motor delay, behavioural problems, ID (also de novo 11p13 deletion) | not mentioned | plasma 0.7 mmol/L; urine 1686 mmol/mol creatinine |
| 6 | Monroe 2019 P2 | Moluccan (Indonesia) | yes | c.1122G>T p.(Trp374Cys) | NM_153486.3 | homozygous | West syndrome, delay, hypotonia (also de novo CACNA1B p.Arg477Cys) | not mentioned | plasma 1.1–1.2 mmol/L |
| 7 | Kwong 2021 (= patient 23 of PMID:32907636) | Chinese | no | c.469+1dupG and c.752C>T p.(Thr251Met) | NM_153486.3 | compound heterozygous | delayed development, mild transient ataxia, mild central hypotonia; complex IV deficiency | urate 0.32 mmol/L (marginal), no gout | serum 0.61 mmol/L |
| 8 | Sloth 2025 | Iraqi parents (Danish boy) | some degree | deletion exons 1–7, c.1_930del p.M1_Q310del (plus ZFP1, CTRB2) | NM_194436.3 | homozygous | psychomotor delay, hypotonia, PDD-NOS | urate 0.38 mmol/L (slightly raised) | plasma 1.2 mmol/L; urine 1.4 mmol/mol creatinine |

Supporting cell quotes:
- Family row, col 1 — QUOTE: "Bedouin‐Israeli kindred. Consanguineous" — [PMID:40678184, Table 2]
- Family row, cols 2–3 — QUOTE: "Melanesian family, three affected siblings. Non‐consanguineous Vietnamese family, two affected siblings. Non‐consanguineous" — [PMID:40678184, Table 2]
- Family row, cols 4–5 — QUOTE: "Parents from Algeria Consanguinity not mentioned Parents from the same Sicilian village in Italy. Share some degree of consanguinity" — [PMID:40678184, Table 2]
- Family row, cols 6–8 — QUOTE: "Parents from Moluccas, Indonesian Consanguineous Parents from China. Non‐consanguineous Parents from the same Iraqi village Share some degree of consanguinity" — [PMID:40678184, Table 2]
- Neuro row, Vietnamese family — QUOTE: "One of the patients developed severe neurological features at the age of 34 years, but was normal earlier in life" — [PMID:40678184, Table 2]
- Neuro row, Monroe P1 — QUOTE: "Severe delay in mental development, delay in motor development, behavioral problems, and intellectual disability" — [PMID:40678184, Table 2]
- Neuro row, Kwong — QUOTE: "Delayed mental development evolving into limited intelligence, mild transient ataxia, and mild central hypotonia" — [PMID:40678184, Table 2]
- Gout onset ages (Bardin families) — QUOTE: "Early‐onset gout Started at age 13, 16, and 21 years, respectively Early‐onset gout Started at age 21 and 9 years, respectively Early‐onset gout Started at age 19 years" — [PMID:40678184, Table 2]
- Drabkin gout — QUOTE: "Gout arthropathy in both adults and children" — [PMID:40678184, Table 2]
- D-lactate, Drabkin plasma — QUOTE: "Elevated average plasma D‐lactate: 3.16 ± 0.63 mmol/L (ref: in healthy controls: undetectable, normal levels: < 0.043 mmol/L)" — [PMID:40678184, Table 2]
- D-lactate, Drabkin urine — QUOTE: "Elevated average D‐lactate in urine: 32.08 ± 5.77 mmol/L" — [PMID:40678184, Table 2]
- D-lactate, Melanesian family — QUOTE: "Serum D‐lactate: 0.306 mmol/L, 0.558 mmol/L, and 0.632 mmol/L Elevated D‐lactate in urine: 21.5 mmol/L, 7.8 mmol/L, and 18.1 mmol/L" — [PMID:40678184, Table 2]
- D-lactate, Vietnamese (not measured) and Algerian/Moroccan patient — QUOTE: "Not measured Plasma D‐lactate: > 0.5 mmol/L Elevated D‐lactate in urine: 6.15 mmol/L" — [PMID:40678184, Table 2]
- D-lactate, Monroe P1, P2 — QUOTE: "Plasma D‐lactate: 0.7 mmol/L Elevated D‐lactate excretion at 1686 mmol/mol creatinine Plasma D‐lactate: 1.1–1.2 mmol/L Elevated D‐lactate excretion" — [PMID:40678184, Table 2]
- D-lactate, Sloth patient — QUOTE: "Plasma D‐lactate: 1.2 mmol/L (ref: < 0.026 mmol/L, n = 10) Elevated D‐lactate in urine: 1.4 mmol/mol creatinine (ref: < 0.021 mmol/mol creatinine, n = 10)" — [PMID:40678184, Table 2]
- Other D-2-hydroxyacids row (not mentioned for the four gout families) — QUOTE: "Other D‐2‐hydroxyacidsNot mentionedNot mentionedNot mentionedNot mentionedElevated 2‐hydroxyisovaleric acid and 2‐hydroxyisocaproic acid in plasma and urine" — [PMID:40678184, Table 2]
- Uric acid, Drabkin — QUOTE: "Adults: 10.34 mg/dL ± 1.84 mg/dL (normal levels: 3.5–7.2 mg/dL) Children: 6.75 mg/dL ± 0.7 mg/dL (normal levels: 2–6.2 mg/dL)" — [PMID:40678184, Table 2]
- Uric acid, Bardin families — QUOTE: "Elevated serum uric acid at 0.71, 0.74, and 0.94 mmol/L, respectivelyElevated serum uric acid at 0.55 and 0.58 mmol/L, respectivelyElevated serum uric acid at 0.46 mmol/L (ref: 0.24 mmol/L—0.51 mmol/L)" — [PMID:40678184, Table 2]
- Variant, Drabkin — QUOTE: "Homozygous missense variant c.1108C>T, p. (Arg370Trp) (NM_153486.3)" — [PMID:40678184, Table 2]
- Variant, Melanesian family — QUOTE: "Homozygous variant c.206 T>C; rs1035398551 p.(Val69Ala) (NM_153486.3)" — [PMID:40678184, Table 2]
- Variant, Vietnamese family — QUOTE: "Homozygous nonsense variant c.1363dupG, p. (AlaGly432fsTer58) (NM_153486.3)" — [PMID:40678184, Table 2]
- Variant, Algerian/Moroccan patient — QUOTE: "Homozygous missense variant c.752C>T, p. (Thr251Met) (NM_153486.3)" — [PMID:40678184, Table 2]
- Variant, Monroe P1 — QUOTE: "Homozygous missense variant c.1388C>T, p. (Thr463Met) (NM_153486.3)" — [PMID:40678184, Table 2]
- Variant, Monroe P2 — QUOTE: "Homozygous missense variant c.1122G>T, p. (Trp374Cys) (NM_153486.3)" — [PMID:40678184, Table 2]
- Variant, Kwong — QUOTE: "Compound heterozygous splice site variant c.469 + 1dupG, (NM_153486.3) and missense variant c.752C>T, p. (Thr251Met) (NM_153486.3)" — [PMID:40678184, Table 2]
- Variant, Sloth — QUOTE: "Homozygous deletion, p.M1_Q310del (NM_194436.3)" — [PMID:40678184, Table 2]
- Other variants, Vietnamese family (RHBG frameshift) — QUOTE: "Homozygous undescribed frameshift variant of the RHBG gene c.1064dupT, p. (Val357GlyfsTer10) (NM_020407.5)" — [PMID:40678184, Table 2]
- Other variants, Monroe P1/P2 — QUOTE: "De novo 11p13 deletion (11p deletion syndrome) Heterozygous de novo variant in CACNA1B c.1429C>T, p. (Arg477Cys) (NM_000718.3), thought to explain West syndrome" — [PMID:40678184, Table 2]
- Other findings, Kwong — QUOTE: "No other genetic variants identified, but mitochondrial complex IV deficiency was found" — [PMID:40678184, Table 2]

---

## PMID:37021930 Bardin 2023 Rheumatology (ABS only)

- Three families, three ethnicities, homozygous — QUOTE: "We demonstrated linkage of juvenile-onset gout to homozygous carriage of three rare distinct LDHD variants in three different ethnicities." — [PMID:37021930, abstract]
- Melanesian family variant as printed in the abstract (no protein consequence stated) — QUOTE: "In a Melanesian family, the variant was (NM_153486.3: c.206C>T; rs1035398551)" — [PMID:37021930, abstract]
- Melanesian homozygotes vs non-homozygotes: urate handling and D-lactate — QUOTE: "homozygotes had higher hyperuricaemia (P = 0.02), lower fractional clearance of urate (P = 0.002), and higher levels of d-lactate in blood (P = 0.04) and urine (P = 0.06)" — [PMID:37021930, abstract]
- Vietnamese family frameshift — QUOTE: "very severe juvenile-onset gout was linked to homozygote carriage of an undescribed LDHD variant (NM_153486.3: c.1363dupG) leading to a frameshift followed by a stop codon, p.(AlaGly432fsTer58)" — [PMID:37021930, abstract]
- Moroccan patient, T251M homozygous — QUOTE: "a Moroccan man, with early-onset and high d-lactaturia, whose family was unavailable for testing, was homozygous for another rare LDHD variant [NM_153486.3: c.752C>T, p.(Thr251Met)]" — [PMID:37021930, abstract]
- Inheritance and diagnostic clue — QUOTE: "Rare, damaging LDHD variants can cause autosomal recessive early-onset gout, the diagnosis of which can be suspected by measuring high d-lactate levels in the blood and/or urine." — [PMID:37021930, abstract]
- NOTE: the abstract gives no protein change for c.206; "P69L" is NOT in the cache. Residue 69 of Q86WU2-1 is Val (checked against `LDHD-uniprot.txt`), which fits Sloth's "c.206 T>C p.(Val69Ala)" and not a Pro69 substitution; the abstract's "C>T" and Sloth's "T>C" disagree in direction. Needs the Bardin full text or dbSNP rs1035398551 to settle.

---

## PMID:38373542 Stefan 2024 Arch Biochem Biophys (ABS only) — recombinant human DLDH isoforms

- Two human isoforms from alternative splicing — QUOTE: "This translates into the expression of two human DLDH (hDLDH) isoforms, the molecular mass of which is expected to differ by 2.7 kDa." — [PMID:38373542, abstract]
- Stereospecific; larger isoform more active — QUOTE: "hDLDH is strictly stereospecific, with the larger isoform (hDLDH-1) featuring higher activity at the expense of d-lactate when compared to its smaller counterpart (hDLDH-2)" — [PMID:38373542, abstract]
- Oxalate inhibition — QUOTE: "hDLDH is strongly inhibited by oxalate, as indicated by a Ki equal to 1.2 μM for this dicarboxylic acid" — [PMID:38373542, abstract]
- Oligomeric state: hexamer (isoform 1) and tetramer (isoform 2) — QUOTE: "hDLDH-1 and hDLDH-2 were determined, by means of gel filtration and dynamic light scattering experiments, to be a hexamer and a tetramer, respectively" — [PMID:38373542, abstract]
- FAD cofactor — QUOTE: "we identified FAD as the cofactor of hDLDH, and we report here a model of FAD binding by the human d-lactate dehydrogenase" — [PMID:38373542, abstract]
- Disease variants (numbered W323C / T412M here) reduce activity — QUOTE: "the mutations W323C and T412 M negatively affect the activity of hDLDH, most likely by impairing the enzyme electron-acceptor site" — [PMID:38373542, abstract]
- NOTE: W323C/T412M = W374C/T463M minus 51, i.e. apparently numbering of a construct lacking the N-terminal presequence (UniProt predicts transit peptide 1–52); my inference, the abstract does not explain the numbering. The abstract gives no Km/kcat and does not name the electron acceptor.

---

## PMID:12127981 Flick & Konieczny 2002 BBRC (ABS only) — cloning; CSRP3/MLP interaction; mouse mitochondrial localisation

- Identification plus CSRP3 interaction, human and mouse — QUOTE: "the identification and initial characterization of putative human and murine D-lactate dehydrogenases (DLD) that can interact with the muscle-specific cysteine-rich protein CRP3/MLP" — [PMID:12127981, abstract]
- Similarity to yeast D-LDH proteins — QUOTE: "the human and mouse transcripts encode novel proteins that display strong similarities to the yeast D-lactate dehydrogenase proteins DLD1, AIP2, and YEL071W" — [PMID:12127981, abstract]
- Expression pattern — QUOTE: "Expression analysis of the mammalian proteins indicates widespread distribution with transcripts present in striated muscle tissues and a variety of other tissue types." — [PMID:12127981, abstract]
- Mitochondrial localisation of the MOUSE protein, by immunofluorescence — QUOTE: "Immunofluorescence subcellular localization of the mouse DLD protein indicates that it resides within mitochondria, a feature shared by many dehydrogenases." — [PMID:12127981, abstract]
- NOTE: the abstract does not name the interaction assay (UniProt cites this paper for "Interacts with CSRP3" and for isoform 2 plus tissue specificity); no sub-mitochondrial resolution; no enzyme assay — the paper calls the proteins "putative".

---

## PMID:41812695 Jiang 2026 Metabolism (ABS only) — CSRP3 binds LDHD in skeletal muscle

- Binding and the mapped region — QUOTE: "CSRP3 binds to D-lactate dehydrogenase (LDHD) via a specific 33-amino acid region, promoting D-lactate metabolism in skeletal muscle." — [PMID:41812695, abstract]
- Downstream claim — QUOTE: "This interaction regulates mitochondrial morphology, biogenesis, oxidative phosphorylation efficiency, and TCA cycle activity" — [PMID:41812695, abstract]
- System used — QUOTE: "experimental model systems involving live mice and cell lines to determine the role of CSRP3 in driving mitochondrial metabolic reconfiguration" — [PMID:41812695, abstract]
- Title claim about LDHD activity — QUOTE: "CSRP3 promotes skeletal muscle remodeling toward aerobic metabolism and enhances exercise endurance through increasing LDHD activity." — [PMID:41812695, title]
- NOTE: the abstract does not say which protein's 33-aa region, nor which species' proteins were used for the binding assay; mouse is the in vivo model. This is the second, independent report of the CSRP3-LDHD interaction (first: PMID:12127981).

---

## PMID:11955284 de Bari 2002 Biochem J (ABS only) — rat liver mitochondria: D-lactate transport and the matrix face of the inner membrane

- D-lactate supports respiration and membrane potential, P/O = 2 — QUOTE: "externally added D-lactate causes oxygen uptake by mitochondria [P/O ratio (the ratio of mol of ATP synthesized to mol of oxygen atoms reduced to water during oxidative phosphorylation)=2] and membrane potential (Delta(psi)) generation" — [PMID:11955284, abstract]
- Inhibitor profile places entry downstream of complex I — QUOTE: "in processes that are rotenone-insensitive, but inhibited by antimycin A and cyanide" — [PMID:11955284, abstract]
- Sub-mitochondrial localisation: matrix face of the inner membrane (SMP assay) — QUOTE: "the activity of the putative flavoprotein (D-lactate dehydrogenase) was detected in inside-out submitochondrial particles, but not in mitochondria and mitoplasts, as it is localized in the matrix phase of the mitochondrial inner membrane" — [PMID:11955284, abstract]
- Three D-lactate translocators — QUOTE: "three novel separate translocators exist to mediate D-lactate traffic across the mitochondrial inner membrane: the D-lactate/H(+) symporter" — [PMID:11955284, abstract]
- Antiporters — QUOTE: "the D-lactate/oxoacid antiporter (which mediates both the D-lactate/pyruvate and D-lactate/oxaloacetate exchanges) and D-lactate/malate antiporter" — [PMID:11955284, abstract]
- Physiological interpretation — QUOTE: "The D-lactate translocators and the D-lactate dehydrogenase could account for the removal of the toxic methylglyoxal from cytosol, as well as for D-lactate-dependent gluconeogenesis." — [PMID:11955284, abstract]
- NOTE: rat, isolated organelles, activity-based ("putative flavoprotein"); the gene product was not identified as LDHD in this work.

## PMID:23333299 de Bari 2013 FEBS Lett (ABS only) — same group, human prostate cells

- Mitochondrial D-LDH is a membrane flavoprotein, higher in cancer cells — QUOTE: "This is due to the mitochondrial D-lactate dehydrogenase, a membrane flavoprotein, the activity and protein level of which are higher in PC-3 than in PNT1A cells, as detected by both kinetic and immunological analysis." — [PMID:23333299, abstract]
- Energy-competent D-lactate metabolism in human cells — QUOTE: "We show that mitochondria from both cancer (PC-3) and normal (PNT1A) prostate cells can metabolize D-lactate in an energy competent manner." — [PMID:23333299, abstract]
- Malate export — QUOTE: "D-Lactate can enter prostate mitochondria and cause the export of newly synthesized malate in a carrier-mediated manner" — [PMID:23333299, abstract]

## PMID:22296683 Ling 2012 Nutr Metab (FT) — tissue differences in mitochondrial D-lactate oxidation (rat)

- Cofactor and tissue dependence — QUOTE: "Cellular D-lactate is metabolized by mitochondrial D-lactate dehydrogenase (DDH) using FAD as cofactor [26,27]. The expression of DDH is tissue dependent and therefore affects the usage of D-lactate in different tissues [26,27]." — [PMID:22296683, introduction]
- Brain oxidises D-lactate poorly because DDH is low — QUOTE: "due to low expression levels of DDH in the brain, the rate of oxidation of D-lactate in the brain is considerably slower compared to that of L-lactate [26,27]" — [PMID:22296683, introduction]
- Measured activity differences — QUOTE: "DLA dehydrogenase activities were 61% and 51% lower in brain and heart mitochondria compared to liver, respectively, whereas LLA dehydrogenase activities were similar across all three tissues." — [PMID:22296683, abstract]
- Functional consequence — QUOTE: "DLA was a poor respiratory substrate in brain and heart mitochondria and inhibited LLA and pyruvate usage in these tissues." — [PMID:22296683, abstract]
- Proposed relevance to D-lactate neurotoxicity — QUOTE: "an accumulation of D-lactate in the brain and heart tissue may represent a secondary disorder of mitochondrial function by interfering with L-lactate and pyruvate metabolism" — [PMID:22296683, discussion]
- Liver capacity — QUOTE: "Relatively high D-lactate dehydrogenase activities in liver mitochondria likely maintain efficient oxidative phosphorylation in these mitochondria" — [PMID:22296683, discussion]

## PMID:31173890 de Bari 2019 Ageing Res Rev (ABS only) — glyoxalase route as the endogenous source

- Methylglyoxal detoxification route and its products — QUOTE: "Methylglyoxal is mainly detoxified via cytosolic glyoxalase route comprising glyoxalase 1 and glyoxalase 2 with the production of S-D-lactoylglutathione and D-lactate as intermediate and end-product, respectively." — [PMID:31173890, abstract]
- Intramitochondrial D-LDH contributes to methylglyoxal elimination and energy — QUOTE: "Due to the existence of mitochondrial carriers and intramitochondrial glyoxalase 2 and D-lactate dehydrogenase, the transport and metabolism of both S-D-lactoylglutathione and D-lactate in mitochondria can contribute to methylglyoxal elimination, cellular antioxidant power and energy production." — [PMID:31173890, abstract]
- Methylglyoxal as a glucose by-product — QUOTE: "the increase in methylglyoxal production, a physiological cytotoxic by-product of glucose catabolism" — [PMID:31173890, abstract]

---

## PMID:37582812 Lv 2023 Signal Transduct Target Ther (ABS only) — CDK7-YAP-LDHD axis in oesophageal cancer

- Transcriptional control of LDHD — QUOTE: "cyclin-dependent kinase 7 (CDK7) phosphorylates nuclear Yes-associated protein 1 (YAP) at S127 and S397 sites and enhances its transcription function, which promotes D-lactate dehydrogenase (LDHD) protein expression" — [PMID:37582812, abstract]
- Claimed function in cancer stem-like cells — QUOTE: "the CDK7-YAP-LDHD axis helps ESCC-CSCs escape from ferroptosis induced by D-lactate and generates pyruvate to satisfy energetic demands for their elevated self-renewal potential" — [PMID:37582812, abstract]
- Mitochondrial site of catabolism — QUOTE: "mitochondrial D-lactate catabolism is a necessary initiating oncogenic event during tumorigenesis of esophageal squamous cell carcinoma (ESCC)" — [PMID:37582812, abstract]
- Expression/prognosis — QUOTE: "LDHD is enriched significantly in ESCC-CSCs rather than differentiated tumor cells and high LDHD status is connected with poor prognosis in ESCC patients" — [PMID:37582812, abstract]

## PMID:832430 Duran 1977 Clin Chim Acta (ABS only; PubMed holds title only, no abstract text)

- Title only — QUOTE: "D-lactic aciduria, an inborn error of metabolism?" — [PMID:832430, title]
- NOTE: this is the index case later shown to be homozygous T463M (Monroe 2019 Patient 1). No abstract text is cached, so nothing else can be quoted.

## PMID:12024214 Enomoto 2002 Nature (ABS only) — URAT1/SLC22A12, the candidate exchanger behind the gout mechanism

- URAT1 identity — QUOTE: "we identify the long-hypothesized urate transporter in the human kidney (URAT1, encoded by SLC22A12), a urate anion exchanger regulating blood urate levels" — [PMID:12024214, abstract]
- Human urate reabsorption is efficient — QUOTE: "because humans have an effective renal urate reabsorption system, despite their evolutionary loss of hepatic uricase by mutational silencing" — [PMID:12024214, abstract]
- NOTE: cached as background for the Drabkin exchange mechanism. The cached abstract does NOT mention lactate or D-lactate as the counter-anion, and no cached LDHD paper names URAT1. Do not attribute the transporter identity to Drabkin 2019 from the cache.

## PMID:31784723 Onuora 2020 Nat Rev Rheumatol (title only in cache)
- QUOTE: "LDHD mutation leads to hyperuricaemia and gout." — [PMID:31784723, title]
- NOTE: research-highlight piece on Drabkin 2019; cache has no abstract body, so it supports nothing beyond the title.

---

## Open questions / conflicts

1. **Residue numbering of the same two variants in three systems.** Patients: W374C and T463M on NM_153486.3 / isoform 1 (Monroe, Sloth, UniProt VARIANT 374 and 463). Jin's mouse enzyme: W351C and T440M, with the correspondence stated explicitly. Stefan: "W323C and T412 M" — 51 less than isoform-1 numbering, consistent with numbering a presequence-less construct, but the abstract never says so. Any review text must state which numbering it uses.
2. **Which isoform/transcript is the reference.** UniProt displays isoform 1 (507 aa, NM_153486) while MANE Select is isoform 2 (484 aa, NM_194436.3). Monroe named variants on NM_153486.3 but expressed NM_194436.1 cDNA; Sloth described its deletion on NM_194436.3 (p.M1_Q310del); PMF-seq purified "human LDHD isoform 2". Isoform 1 differs by the 23-residue insertion 211–233, which Jin places on the surface away from both sites.
3. **Oligomeric state.** Monomer in solution for mouse LDHD and one molecule per asymmetric unit (Jin); dimer on gel filtration for human isoform 2 (PMF-seq); hexamer (isoform 1) and tetramer (isoform 2) by gel filtration plus DLS (Stefan). Three methods, three answers; UniProt hedges to "Could form homooligomers".
4. **Physiological electron acceptor.** Jin explicitly leaves it unknown (PMS/DCIP in vitro); PMF-seq shows direct reduction of cytochrome c by purified human enzyme and LDHD-dependent D-lactate-driven membrane potential in cells. Reviews should credit the acceptor claim to PMID:38413804, not to the mouse structural paper.
5. **Sub-mitochondrial localisation and topology.** de Bari: matrix face of the inner membrane in rat liver (inside-out SMP activity, not in mitoplasts). PMF-seq and Jin assert inner-membrane association by citation only; electron transfer to cytochrome c implies an IMS-facing active site. Direct human evidence is only "mitochondrion" (Flick, mouse immunofluorescence; Drabkin, overexpressed human protein). UniProt records only `Mitochondrion` by similarity.
6. **Bardin's Melanesian variant.** Bardin abstract: "c.206C>T" with no protein consequence. Sloth Table 2: "c.206 T>C ... p.(Val69Ala)". Residue 69 of Q86WU2-1 is Val. The direction of the substitution and the protein change need the Bardin full text or dbSNP rs1035398551; "P69L" appears in neither cached file.
7. **Enzyme activity of the human variants.** No cached paper reports % residual activity for a human variant protein. The "~90% loss" figure is for the four corresponding MOUSE mutants (Jin); the human evidence is failure of zebrafish rescue (Monroe) and a qualitative statement for W323C/T412M (Stefan).
8. **Causality of the neurological phenotype.** Monroe, Kwong and Sloth all hedge; three of the neuro patients carry a second plausible cause (11p13 deletion, CACNA1B, complex IV deficiency), and the gout families with the highest D-lactate (Drabkin, 3.16 mM) were neurologically unaffected. The Vietnamese sibling who became severely affected at 34 y also carries a homozygous RHBG frameshift.
9. **Gout mechanism.** The exchange of renal D-lactate secretion for urate reabsorption is stated only in the Drabkin abstract, which names no transporter; URAT1/SLC22A12 is an inference from PMID:12024214 and is not asserted in any cached LDHD paper.
10. **Methylglyoxal detoxification as a function.** Asserted widely (de Bari, Kwong) but PMF-seq found no methylglyoxal-sensitivity difference in LDHD KO human cells. D-2-hydroxyacid/BCKA metabolism (Jin) is the better-evidenced broader function.
11. **Ldhd knockout mouse.** None found in the cached corpus or in the PubMed searches run here. The only mouse in vivo datum is D-lactate injection into naive mice causing hyperuricaemia (Drabkin abstract); the only whole-animal LOF model is the zebrafish ldhd sa15623 line.
12. **D-2-hydroxyglutarate is explicitly NOT a substrate** (Jin), which separates LDHD from D2HGDH; useful against any D-2-hydroxyglutarate dehydrogenase annotation propagated by family similarity.
