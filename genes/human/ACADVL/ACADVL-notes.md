# ACADVL (P49748) — Gene Review Notes
> Historical draft below contains superseded claims. See the 2026-09-26 full source audit appended below for the current evidence and decisions.

Human very-long-chain specific acyl-CoA dehydrogenase (VLCAD), mitochondrial. EC 1.3.8.9 (very-long-chain) / EC 1.3.8.8 (long-chain). HGNC:92. NCBITaxon:9606.

## Core identity and function

VLCAD catalyzes the first (rate-limiting committed) step of each cycle of mitochondrial fatty acid beta-oxidation (FAO): the FAD-dependent alpha,beta-dehydrogenation of acyl-CoA thioesters to the corresponding trans-2-enoyl-CoA, with the electron-transfer flavoprotein (ETF) as the physiological electron acceptor.

- VLCAD "is one of four flavoproteins which catalyze the initial step of the mitochondrial beta-oxidation spiral" [PMID:9461620 "Very long-chain acyl-CoA dehydrogenase (VLCAD) is one of four flavoproteins which catalyze the initial step of the mitochondrial beta-oxidation spiral"].
- The UniProt record describes the reaction as "the proR-proR stereospecific alpha, beta-dehydrogenation of fatty acyl-CoA thioesters using the electron transfer flavoprotein (ETF) as their physiologic electron acceptor, resulting in the formation of trans-2-enoyl-CoA" (file ACADVL-uniprot.txt FUNCTION section).
- Substrate specificity: VLCAD "acts specifically on fatty acyl-CoAs with saturated 12 to 24 carbons long primary chains" with optimum in the very-long-chain range; it is distinguished from MCAD/SCAD by its preference for C14-C24 substrates (ACADVL-uniprot.txt FUNCTION). Catalytic activity entries assign EC 1.3.8.9 (very-long-chain) [PMID:21237683] and EC 1.3.8.8 (long-chain).

## Catalytic / cofactor residues

- The catalytic base abstracting the alpha-proton: "Glu-422 of VLCAD has been presumed to be the catalytic residue that abstracts the alpha-proton in the alphabeta-dehydrogenation reaction. Replacing Glu-422 with glutamine (E422Q) caused a loss of enzyme activity by preventing the formation of a charge transfer complex between VLCAD and palmitoyl-CoA" [PMID:9461620 "Glu-422 of VLCAD has been presumed to be the catalytic residue that abstracts the alpha-proton in the alphabeta-dehydrogenation reaction. Replacing Glu-422 with glutamine (E422Q) caused a loss of enzyme activity by preventing the formation of a charge transfer complex between VLCAD and palmitoyl-CoA"]. (Numbering is for the mature protein; UniProt lists ACT_SITE at residue 462 in the precursor numbering.)
- FAD is the essential cofactor. Phe-418 (mature numbering) is required for FAD binding/reduction: "F418L and F418V contained no bound FAD... These data suggest that Phe-418 is involved in the binding and subsequent reduction of FAD" [PMID:9461620 "These data suggest that Phe-418 is involved in the binding and subsequent reduction of FAD"]. Loss of FAD destabilizes folding: "FAD-deficient VLCADs (F418L, F418V, and apo-VLCAD) showed increased sensitivity to trypsinization. Loss of FAD may change the folding of VLCAD subunit" [PMID:9461620 "FAD-deficient VLCADs (F418L, F418V, and apo-VLCAD) showed increased sensitivity to trypsinization"].
- UniProt COFACTOR: "Name=FAD" with evidence from PMID:18227065 and PMID:9461620.

## Quaternary structure and localization

- VLCAD is a homodimer of ~70 kDa subunits associated with the mitochondrial inner membrane: "Mature VLCAD is a homodimer of a 70-kDa protein associated with the mitochondrial membrane" [PMID:9599005 "Mature VLCAD is a homodimer of a 70-kDa protein associated with the mitochondrial membrane"]. This contrasts with the soluble, matrix tetrameric MCAD/SCAD/LCAD.
- Inner-membrane association precedes and is required for dimer assembly: "Newly synthesized VLCAD was present as a monomer and the major fraction was associated with the mitochondrial inner membrane... association of VLCAD protein with mitochondrial inner membrane is necessary for dimer assembly and formation of mature VLCAD" [PMID:9599005 "association of VLCAD protein with mitochondrial inner membrane is necessary for dimer assembly and formation of mature VLCAD"].
- The monomeric disease mutant S583W fails to associate with the membrane and remains soluble in the matrix: "a VLCAD monomeric mutant S583W... did not associate with the mitochondrial membrane after import and the major fraction remained in the mitochondrial matrix" [PMID:9599005 "a VLCAD monomeric mutant S583W, a novel mutation identified from a patient with VLCAD deficiency, did not associate with the mitochondrial membrane after import and the major fraction remained in the mitochondrial matrix"].
- UniProt SUBCELLULAR LOCATION: "Mitochondrion inner membrane; Peripheral membrane protein" (evidence PMID:9461620, PMID:9599005). The N-terminal 40-aa transit peptide is cleaved on import: "encoding the entire protein of 655 amino acids, including a 40-amino acid leader peptide and a 615-amino acid mature polypeptide" [PMID:7668252 "including a 40-amino acid leader peptide and a 615-amino acid mature polypeptide"].

## Tissue distribution

- "Predominantly expressed in heart and skeletal muscle" (ACADVL-uniprot.txt TISSUE SPECIFICITY, evidence PMID:17564966, PMID:8845838). This matches the clinical phenotype (cardiomyopathy, rhabdomyolysis).
- Unlike ACAD9/ACAD11, VLCAD is not the principal long-chain ACAD in cerebellum; in human cerebellum the ACAD9/ACAD11 pair "accommodates the full spectrum of long chain fatty acid substrates" [PMID:21237683 "The combination of ACAD11 with the newly characterized ACAD9 accommodates the full spectrum of long chain fatty acid substrates presented to mitochondrial β-oxidation in human cerebellum"].

## Disease

- VLCAD deficiency (ACADVLD; MIM:201475) is an inborn error of FAO. Three phenotypes: severe early-onset with cardiomyopathy/high mortality; a milder hepatic/hypoketotic-hypoglycemia form; and an adult myopathic form with rhabdomyolysis (ACADVL-uniprot.txt DISEASE).
- VLCAD was discovered as a novel FAO disorder: "Two of the patients... were found to have a novel disease, VLCAD deficiency, as judged from the results of very low palmitoyl-CoA dehydrogenase activity and the lack of immunoreactivity toward antibody raised to purified VLCAD" [PMID:8466512 "found to have a novel disease, VLCAD deficiency, as judged from the results of very low palmitoyl-CoA dehydrogenase activity and the lack of immunoreactivity toward antibody raised to purified VLCAD"].
- Restoring VLCAD partially restores beta-oxidation flux: "raising VLCAD activity to approximately 20% of normal control fibroblast activity raised palmitic acid beta-oxidation flux to the level found in control fibroblasts" [PMID:7668252 "raising VLCAD activity to approximately 20% of normal control fibroblast activity raised palmitic acid beta-oxidation flux to the level found in control fibroblasts"]. This is an IMP-grade functional demonstration of the FAO role.
- Cardiac/sudden death link: "VLCAD deficiency reduces myocardial fatty acid beta-oxidation and energy production and is associated with cardiomyopathy and sudden death in childhood" [PMID:7479827 "VLCAD deficiency reduces myocardial fatty acid beta-oxidation and energy production and is associated with cardiomyopathy and sudden death in childhood"]. This supports the BP "energy derivation by oxidation of organic compounds".

## Notes on specific GOA annotations

- **GO:0017099 very-long-chain fatty acyl-CoA dehydrogenase activity** (IDA PMID:9461620, IBA, IEA): core MF. This is the defining activity (EC 1.3.8.9). Strongly supported.
- **GO:0004466 long-chain fatty acyl-CoA dehydrogenase activity** (IDA PMID:7668252, TAS PMID:8466512, IEA): VLCAD also handles long-chain (C12-C18); EC 1.3.8.8. Acceptable; somewhat less specific than GO:0017099 but biologically correct (VLCAD activity is classically assayed with palmitoyl-CoA, C16).
- **GO:0003995 acyl-CoA dehydrogenase activity** (IMP PMID:9599005, IMP PMID:9461620, IEA): parent/general ACAD term. The two IMP annotations rest on mutant studies (S583W dimer-assembly mutant; E422Q/F418 catalytic-and-FAD mutants) that abolish/impair dehydrogenase activity — these are legitimate experimental annotations even though the abstracts foreground mechanism/assembly. Keep as non-core (subsumed by the specific VLCAD/LCAD terms).
- **GO:0050660 flavin adenine dinucleotide binding** (IDA PMID:9461620, IEA): core; FAD is the essential redox cofactor. Supported by PMID:9461620 FAD-binding mutant data and UniProt COFACTOR.
- **GO:0042802 identical protein binding** (IDA PMID:9461620, PMID:9599005): VLCAD is a homodimer; this captures homodimerization, supported by PMID:9599005. Keep (informative, not generic "protein binding").
- **GO:0000062 fatty-acyl-CoA binding** (IBA): substrate binding; reasonable IBA, non-core.
- **GO:0016627 oxidoreductase activity, acting on the CH-CH group of donors** (IEA InterPro): correct intermediate parent of ACAD activity. Non-core.
- **GO:0070991 medium-chain fatty acyl-CoA dehydrogenase activity** (IEA RHEA): VLCAD does have measurable activity toward shorter (C10-C12) substrates per the in-vitro Rhea mappings, but its physiological specificity is long/very-long chain. This is an over-annotation by Rhea EC mapping; mark as over-annotated.
- **GO:0006635 / GO:0033539 fatty acid beta-oxidation (using ACAD)** (multiple IDA/IMP/IEA/ISS): core BP. Well supported.
- **GO:0005743 mitochondrial inner membrane** (IEA SubCell): core CC, matches UniProt and PMID:9599005.
- **GO:0031966 mitochondrial membrane** (IDA PMID:16020546, IEA): PMID:16020546 is the ACAD9 paper (Ensenauer 2005); the membrane-association statement is for ACAD-9, not VLCAD. However VLCAD is independently and robustly localized to the inner/mitochondrial membrane (PMID:9599005), so the term itself is correct; less specific than inner membrane. Keep as non-core; do not REMOVE (experimental membrane localization of VLCAD is established).
- **GO:0005759 mitochondrial matrix** (TAS Reactome x2): VLCAD is a peripheral inner-membrane protein on the matrix side; Reactome places the beta-oxidation reactions in the matrix compartment. The mature dimer is membrane-associated, not soluble-matrix (PMID:9599005). Matrix is a less accurate CC than inner membrane; keep as non-core (the catalytic face is matrix-side).
- **GO:0042645 mitochondrial nucleoid** (IDA PMID:18063578): PMID:18063578 is a nucleoid proteomics study; metabolic enzymes co-purify with native nucleoids but were "not observed to cross-link to mtDNA" [PMID:18063578 "Several other metabolic proteins and chaperones identified in native nucleoids, including ATAD3, were not observed to cross-link to mtDNA"]. This is a co-purification artifact / peripheral association, not a genuine nucleoid localization. Mark as over-annotated.
- **GO:0030855 epithelial cell differentiation** (IEP PMID:21492153): from a Caco-2 differentiation proteomics screen where many lipid-metabolism proteins were up-regulated on differentiation. This is a correlative expression change, not a role of VLCAD in differentiation. Over-annotation.
- **GO:0001659 temperature homeostasis; GO:0045717 negative regulation of fatty acid biosynthetic process; GO:0046322 negative regulation of fatty acid oxidation; GO:0090181 regulation of cholesterol metabolic process** (IEA GO_REF:0000107 from mouse P50544; and ISS GO_REF:0000024 from P50544): these are all transferred from the **mouse LCAD ortholog (Acadl, P50544)**, NOT from a VLCAD ortholog. They derive from Acadl-knockout mouse phenotypes (thermoregulation, lipid regulation). Mapping LCAD-knockout phenotypes onto human VLCAD by ortholog transfer is a mis-transfer (the human ortholog of mouse Acadl is human ACADL, not ACADVL). These regulatory/whole-organism phenotypes are not demonstrated for human VLCAD and should be removed as incorrect electronic over-propagations.
- **GO:0005515 protein binding** (IPI PMID:32296183, with TAF1B/Q53T94): a single binary Y2H interaction from HuRI with the RNA Pol I factor TAF1B. Uninformative generic term and biologically implausible as a functional interaction for a mitochondrial inner-membrane FAO enzyme; mark as over-annotated.
- **GO:0015980 energy derivation by oxidation of organic compounds** (TAS PMID:7479827): legitimate higher-level BP; VLCAD-mediated FAO supplies myocardial energy (PMID:7479827). Keep as non-core (parent of beta-oxidation/energy role).

## Paralog/ortholog caution

- Mouse P50544 = Acadl (LCAD), not VLCAD. Several IEA/ISS annotations on human ACADVL were transferred from P50544 and reflect LCAD-knockout mouse biology (temperature homeostasis, regulation of fatty acid/cholesterol metabolism). These are not appropriate for human ACADVL.
- PMID:16020546 (Ensenauer 2005) and PMID:21237683 (He 2011) primarily characterize ACAD9/ACAD10/ACAD11. Where they touch VLCAD it is comparative; do not over-rely on them for VLCAD-specific claims, but the VLCAD membrane localization they support is independently established.

## Core function summary (for synthesis)

1. **Very-long-chain/long-chain acyl-CoA dehydrogenase (EC 1.3.8.9/1.3.8.8)** — FAD-dependent alpha,beta-dehydrogenation of C12-C24 acyl-CoA, first step of FAO; ETF electron acceptor; catalytic Glu, essential FAD. MF GO:0017099; BP GO:0006635; CC GO:0005743.
2. **FAD binding** as the obligate redox cofactor (GO:0050660).
3. **Homodimerization on the inner membrane** (GO:0042802 / inner-membrane CC) — quaternary-structure requirement for activity.

## 2026-09-26 full source audit (supersedes earlier decisions)

This audit supersedes the earlier annotation and ortholog interpretations above. In particular,
**P50544 is mouse Acadvl/VLCAD, not Acadl/LCAD**. The earlier removal recommendations,
no-cross-linking interpretation, and ACAD9-paper miscitation claim are withdrawn. The opening
“committed”/“rate-limiting” wording and claim that long-chain activity is a parent of very-long-chain
activity should also be read as superseded by the definition-based synthesis below.

### Baseline and access provenance

- Main at audit start: `488555581d3642ba24843fc05bcb6d6517dabcd9`; local review matched remote blob
  `f840362956e5df1b69588af45347a479c287c1a9`. HGNC:92/NCBI Gene37 confirms **ACADVL**; historical
  aliases include ACAD6, LCACD and VLCAD ([NCBI](https://www.ncbi.nlm.nih.gov/gene/37)).
- Existing COMPLETE review: 42 source rows, 12 cached PMIDs, no research-provider report.
  Open-PR searches included symbols and aliases; the apparent matches #3152 and #3105 were
  inspected for changed paths and contain no ACADVL files. No newer review was overwritten.
- All 12 cited publication caches were read. Three provide full text (PMIDs 18227065, 32296183,
  34800366); the remainder are abstract-only locally. The existing cached PMID15639194 was also
  read and added to references. No publication or machine-generated source cache was edited.
- A genuine Falcon attempt used the default command, `--fallback perplexity-lite --timeout 1200`,
  and `/tmp` uv cache/tool directories. Both attempts failed before invoking a provider because
  `uvx` could not resolve `pypi.org` to install `deep-research-client`. The wrapper exited 1;
  no provider report was generated and no provider process remained live. Manual primary-source
  research supplied this audit; no provider-named report was manufactured.
- Primary full text was separately recovered through Wiley (21492153), author-uploaded articles
  on ResearchGate (16020546, 18063578), and indexed PMC main text/caption (21237683). These routes
  do not change the immutable caches' `full_text_available` flags.

### Donor identity and regulatory evidence

[NCBI mouse Acadvl, Gene11370](https://www.ncbi.nlm.nih.gov/gene/11370) links **P50544** to Acadvl
and MGI:895149. The source GOA identifies P50544, with ENSMUSP00000099634 on Ensembl transfers.
The [MGI Acadvl graph](https://www.informatics.jax.org/marker/gograph/MGI%3A895149) displays the
four disputed process terms as mouse IMP assertions with J:95532. This is a graph generated in
March 2023; its date is recorded rather than represented as a new 2026 annotation release.

[PMID:15639194](https://pubmed.ncbi.nlm.nih.gov/15639194/) directly reports loss of cold tolerance
in both VLCAD- and LCAD-deficient mice. Temperature-homeostasis transfers are therefore retained
as non-core organismal consequences of fatty acid oxidation. The same abstract reports increased
hepatic oxidation-gene expression in both mutants, while its non-fasted lipogenesis discussion
foregrounds LCAD. Full study results and the exact J:95532-to-PMID mapping could not be recovered.
The six transfers for negative regulation of fatty acid synthesis, negative regulation of fatty
acid oxidation and regulation of cholesterol metabolism are **UNDECIDED**. Neither a wrong-paralog
claim nor the argument that a catalytic enzyme cannot exert indirect negative feedback is valid.
The original source identifiers remain intact.

### Substrate chemistry and catalytic scope

Live AmiGO definitions distinguish
[medium-chain GO:0070991](https://amigo.geneontology.org/amigo/term/GO%3A0070991),
[long-chain GO:0004466](https://amigo.geneontology.org/amigo/term/GO%3A0004466), and
[very-long-chain GO:0017099](https://amigo.geneontology.org/amigo/term/GO%3A0017099): their aliphatic
tail ranges are respectively 6–12, 13–22, and greater than 22 carbons. Long-chain and very-long-chain
activities are sibling specializations of acyl-CoA dehydrogenase activity, not parent/child terms.
The definitions concern substrate chemistry rather than the historical names MCAD, LCAD or VLCAD.

The human palmitoyl-CoA mutant assays [PMID:9461620], fibroblast flux rescue [PMID:7668252] and patient
enzyme assays [PMID:8466512] substantiate long-chain catalysis. They do not by themselves establish
the modern very-long-chain threshold. The original IDA very-long-chain row is retained with curator
deference rather than rejected from an incomplete abstract. The machine-fetched UniProt record
separately assigns C24-CoA reaction RHEA:47232 with PMID:21237683, and the human structure explains
how the cavity accommodates extended chains [PMID:18227065]. Structural cavity capacity is not
misrepresented as a turnover measurement.

The [primary ACAD10/11 article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3073726/) includes purified
VLCAD comparators (Figure 4F) and human muscle membrane activity in section 3.7. Its individual
figure rates were not re-extracted. UniProt's RHEA:47296 dodecanoyl-CoA reaction and the current GO
medium-chain definition support retention of boundary-range activity as **NON_CORE**, instead of
calling the Rhea mapping erroneous solely because ACADM is the main medium-chain enzyme.

Four broad catalytic MF rows are refined to the experimentally grounded long-chain reaction. The
broad energy-derivation process is refined to existing GO:0033539 coverage. That term describes the
beta-oxidation pathway employing an acyl-CoA dehydrogenase initial step; VLCAD performs that step,
not every reaction in the pathway. No NEW process annotation is introduced.

PAINT IBDs in `interpro/panther/PTHR43884/PTHR43884-paint.tsv` at PTN000856877 confirm the inherited
VLCAD-activity and fatty-acyl-CoA-binding assertions. The human descendant evidence is legitimate
support for node placement. No donor-count or circularity objection is made. InterPro catalytic
and FAD mappings, ARBA provenance, and Rhea substrate mappings were traced from GOA/UniProt.

### Localization and primary-source corrections

All organelle and mitochondrial-membrane rows retain their source resolution and are **ACCEPT**.
The [live HPA page](https://www.proteinatlas.org/ENSG00000072778-ACADVL/subcellular) reports supported
mitochondrial localization (HPA019006/HPA020595); this does not resolve matrix or inner membrane.
The MitoCoP full main article was inspected, but its individual ACADVL supplementary entry was not
independently re-extracted; the curated mitochondrial assertion is retained with targeted support.

[PMID16020546, author-uploaded full primary article](https://www.researchgate.net/publication/7723299_Human_Acyl-CoA_Dehydrogenase-9_Plays_a_Novel_Role_in_the_Mitochondrial_-Oxidation_of_Unsaturated_Fatty_Acids)
Methods and Figure 5 Results directly include VLCAD in human muscle fractionation. VLCAD sediments
with the membrane fraction. The old MISCITED designation is withdrawn; the paper's ACAD9-focused
title did not exclude experimental VLCAD controls.

The two Reactome records are distinct: R-HSA-1791069 is an expression event, whereas R-HSA-77299
is palmitoyl-CoA dehydrogenation. Matrix TAS rows remain contextual/non-core, distinguishing imported
protein and reaction-compartment placement from mature membrane-associated topology. Matrix is
not an ancestor of inner membrane. Wild-type membrane-dependent assembly and the soluble-matrix
S583W mutant are distinguished [PMID:9599005]; the structural analysis supports a matrix-facing
peripheral enzyme [PMID:18227065].

[PMID18063578, author-uploaded full primary article](https://www.researchgate.net/publication/5783906_The_Layered_Structure_of_Human_Mitochondrial_DNA_Nucleoids)
Table 1 places ACADVL/NP_000009 in Class I, present in both native and cross-linked preparations.
Native anti-TFAM/anti-mtSSB peptide counts are 3/0 and cross-linked preparations 1/2 are 3/0. Thus
the previous review's failure-to-cross-link claim was false. The Methods used HeLa mitochondria,
formaldehyde cross-linking, gradient purification and peptide identification. Retain nucleoid
association as non-core without proposing DNA-binding, replication or genome-maintenance functions.
The [GO nucleoid definition](https://amigo.geneontology.org/amigo/term/GO%3A0042645?relation=regulates)
is regional; direct DNA contact is not required of every localized protein.

### Expression and interaction evidence

[PMID21492153, full Wiley primary article](https://onlinelibrary.wiley.com/doi/10.1111/j.1440-169X.2011.01258.x)
Methods compare proliferating and day-17 differentiated Caco-2 cultures. Table 1 identifies ACADVL
with a 3.25-fold increase; the Discussion interprets lipid-enzyme changes as altered metabolic
turnover. Keep **MARK_AS_OVER_ANNOTATED** for differentiation participation. This is now based on
full study inspection; the IEP evidence code correctly records expression-pattern evidence.

The HuRI source [PMID:32296183] includes repeated screens, pair retests and broader validation.
GOA identifies TAF1B/Q53T94 as the partner; UniProt records three experiments. Remove generic
protein binding as functionally uninformative, without labeling the interaction an artifact from
compartment annotations. No unsupported replacement binding function is proposed. Pair-specific
raw assays were not independently reanalyzed. Homodimerization and substrate binding remain real
non-core properties, while FAD binding is integrated with the core catalytic mechanism.

### Final synthesis and checks

Two core entries describe the same enzyme's long-chain and very-long-chain substrate ranges,
with cofactor, homodimer and membrane information integrated rather than adding a separate FAD-only
physiological function. All 42 source annotation objects remain unchanged outside `review`.
Final actions: **20 ACCEPT, 9 KEEP_AS_NON_CORE, 6 UNDECIDED, 5 MODIFY, 1 REMOVE,
1 MARK_AS_OVER_ANNOTATED**. No NEW annotations or proposed ontology terms were added.

Final `just validate human ACADVL` passed without curation warnings; `just render human ACADVL`
passed. All 42 source-field objects and the GOA/UniProt bytes were verified unchanged. YAML trailing
spaces were removed with parsed-data equality checked. History validation and final file hashes are
recorded in `/tmp/ACADVL-audit-manifest.json`. No Git state or shared project file was changed.

Coordinator inspection of all 42 rows and both core entries found no blocking biological issue. Added the exact cached UniProt C24 catalytic reaction and its experimental attribution to the very-long-chain rows/core, distinguishing curated turnover evidence from structural cavity capacity. Abstract-only local PMID caches now carry explicit reference flags; externally accessed full text remains separately described above. Source assertions and action counts are unchanged.


## 2026-09-26: PR #3157 evidence-scope follow-up

This append-only entry supersedes the earlier final action count and energy-process refinement above. It also makes the nucleoid evidence explicit; the prior phrase “both native and cross-linked preparations” meant preparation categories, not every experiment. The current YAML reasons and biological questions now stand independently of the earlier draft. The history of the P50544/paralog and paper-attribution corrections remains in this journal.

### Nucleoid source and exact table interpretation

Independently re-read the [author-uploaded full primary article, PMID:18063578](https://www.researchgate.net/publication/5783906_The_Layered_Structure_of_Human_Mitochondrial_DNA_Nucleoids), Table 1 and its legend, Results, and Discussion. The table is legible in the indexed full article. The row is `Acyl-CoA dehydrogenase,VLC ACADVL NP_000009 3 0 3 0`. Its columns are:

| Preparation | Native, anti-TFAM | Native, anti-mtSSB | Cross-linked, preparation 1 | Cross-linked, preparation 2 |
| --- | ---: | ---: | ---: | ---: |
| Independent ACADVL peptides | 3 | 0 | 3 | 0 |

The legend defines these as independent LC-MS/MS peptide identifications with confidence above 90%. They are not abundance measurements. Detection occurred in one native preparation and one cross-linked preparation; the two zero columns preclude claiming identification in every preparation. Class I is the paper's operational core-nucleoid group and includes metabolic enzymes. Class II contains the native-only set, including ATAD3, discussed in the abstract. Thus the abstract does not assign all metabolic enzymes to the native-only set. Cross-linking can capture indirect contacts, and neither the table nor the classification establishes an ACADVL DNA-binding or genome-maintenance activity. The nucleoid row remains KEEP_AS_NON_CORE with this bounded biochemical support.

The exact table row is now quoted in `supporting_text_fulltext`; the generic abstract set-level quote was removed from this annotation. The immutable local cache is abstract-only, so `full_text_unavailable: true` remains correct. No cache was altered.

### Other source and ontology refinements

Re-read [PMID:16020546, full original Figure 5 Results and caption](https://www.researchgate.net/publication/7723299_Human_Acyl-CoA_Dehydrogenase-9_Plays_a_Novel_Role_in_the_Mitochondrial_-Oxidation_of_Unsaturated_Fatty_Acids). Human muscle mitochondrial matrix and membrane fractions were immunoblotted using anti-VLCAD, with purified enzyme controls. The result states that VLCAD pelleted with the membrane fraction; a short direct excerpt is now recorded in `supporting_text_fulltext`. The local cache remains abstract-only. This assay supports membrane-level localization; separate assembly and structural sources provide the finer inner-membrane context.

The [live AmiGO GO:0033539 page](https://amigo.geneontology.org/amigo/term/GO%3A0033539) and [GO:0006635 page](https://amigo.geneontology.org/amigo/term/GO%3A0006635), viewed 2026-09-26, display an inferred `is_a` ancestry through fatty acid oxidation/catabolism without GO:0015980. The [energy derivation page](https://amigo.geneontology.org/amigo/term/GO%3A0015980) places that process under GO:0006091. This checks the displayed `is_a` relationship, not an exhaustive assertion that no other relation can connect these processes. QuickGO/OLS API requests were unavailable. PMID:7479827 explicitly links VLCAD deficiency to diminished myocardial oxidation and energy production. Accordingly, retain GO:0015980 as KEEP_AS_NON_CORE; replacing it with already-present GO:0033539 would lose a supported distinct assertion.

The MitoCoP finding now quotes an actual cached dataset statement, while explicitly recording that the ACADVL supplementary identification was not independently re-extracted. Core descriptions positively distinguish C16-based long-chain activity from the C24 reaction and extended binding cavity. Both describe the same FAD-dependent membrane-associated homodimer. EC 1.3.8.9 and EC 1.3.8.8 match the fetched UniProt record; the membrane-associated architecture is distinguished from the soluble matrix tetramers SCAD, MCAD and LCAD.

Final actions are **20 ACCEPT, 10 KEEP_AS_NON_CORE, 6 UNDECIDED, 4 MODIFY, 1 REMOVE, 1 MARK_AS_OVER_ANNOTATED**. Only the energy row action changed in this follow-up. All 42 source assertions and all fetched GOA/UniProt/cache artifacts remain unchanged. Targeted validation, rendering, new history validation, and byte-based publication hashes are recorded in the follow-up manifest supplied to the coordinator. No Git or remote mutation was performed.
