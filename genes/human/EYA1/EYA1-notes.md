# EYA1 (Q99502) curation notes

Automated deep research was not available for this session (falcon 402, OpenAI 401); these notes
are from cached publications, the UniProt record and targeted web searches.

## Identity and domains
- Eyes absent homolog 1; N-terminal proline/serine/threonine-rich transactivation region and a
  conserved ~270 aa C-terminal Eya domain (ED) that belongs to the HAD phosphatase superfamily.
  [PMID:19497856 "There are four mammalian members ( EYA1–4 ), each containing an N-terminal transactivation domain ( 5 ), and a highly conserved ∼270-amino acid C-terminal Eya domain (ED), also referred to as the eya homologous region."]
- Family-level: Eya is a non-thiol HAD protein tyrosine phosphatase (Drosophila eya)
  [PMID:14628053 "propose a function for it as a non-thiol-based protein tyrosine phosphatase"].

## Transcriptional coactivator for SIX proteins
- EYA has no DNA-binding domain; SIX supplies DNA binding, EYA transactivation
  [PMID:19497856 "As a complex, the SIX and EYA proteins are believed to form a bipartite transcription factor where SIX confers DNA binding and EYA confers transactivation activity."].
- Six2/4/5 translocate Eya1 into the nucleus; synergistic activation of myogenin promoter
  [PMID:10490620 "Coexpression of Six2, Six4, or Six5 induced nuclear translocation of Eya1, Eya2, and Eya3, which were otherwise distributed in the cytoplasm."].
- Human EYA1 is cytoplasmic without SIX1 and nuclear with SIX1; SIX1 V17E BOR mutant fails
  [PMID:19497856 "we observed that in the absence of SIX1, EYA1 was localized in the cytoplasm"].
- Eya phosphatase switches Six1-Dach from repression to activation
  [PMID:14628042 "The phosphatase function of Eya switches the function of Six1-Dach from repression to activation, causing transcriptional activation through recruitment of co-activators."].
- SUMO1 modification of EYA1 inhibits its transcriptional activity; Akt phosphorylation reduces it
  [PMID:24954506 "SUMOylation inhibits Eya1 transcription activity"]. EYA1 is the substrate, so
  "protein sumoylation" (ISS) is a substrate-type annotation, not participation.

## Protein tyrosine phosphatase / H2AX pY142
- Cook et al. 2009: HA-Eya1 dephosphorylates H2AX pY142 in vitro; D323A dead mutant inactive;
  Eya1 siRNA increases pY142 after IR; rescue requires catalytic activity
  [PMID:19234442 "Wild-type Eya effectively removed the phosphotyrosine mark from H2AX, while the phosphatase-inactive mutant Eya proteins (Eya1 D323A or Eya3 D246A) had little or no effect"].
- Ser/Thr activity: the same paper reports minimal activity toward a pSer H2AX peptide (Eya3 ED) and
  says Eya primarily acts as a tyrosine phosphatase in vivo
  [PMID:19234442 "subsequent data has indicated that, in-vivo, Eya primarily functions as a tyrosine phosphatase"].
  Ser/Thr phosphatase annotations (EXP + IEA) therefore look like over-annotation for EYA1.
- Krishnan et al. 2009 showed EYA2/EYA3 (not EYA1) specificity for H2AX Y142 [PMID:19351884].
- BOR missense mutations abolish EYA1 phosphatase activity whereas ocular-defect mutations do not
  [PMID:16797546 "BOR-associated mutations lead to a loss of phosphatase activity in Eya1 proteins, while mutations associated with ocular defects yield Eya1 proteins with near normal levels of phosphatase activity."].

## Organ development
- Mouse Eya1-/- lack ears and kidneys; Six but not Pax expression depends on Eya1
  [PMID:10471511 "Eya1 homozygotes lack ears and kidneys due to defective inductive tissue interactions and apoptotic regression of the organ primordia."].
- Human: BOR syndrome (branchial, ear, kidney), usually no eye anomalies; rare EYA1 missense variants
  in congenital cataract / anterior segment anomalies
  [PMID:10655545 "with usually no anomalies in the eye"].

## Relevance to retinal determination network module
- EYA1 is the human ortholog used as representative of the Eya node. Molecular functions
  (coactivator, PTP) are conserved, but mammalian EYA1's organ roles are ear/kidney/branchial/muscle;
  eye involvement is minor (cataract/anterior segment), not retinal specification. A family-level
  annoton is fine, but the "eye development" process should be grounded on fly eya, not EYA1.

## 2026-10-24 — accepted annotation evidence integration

The two independently accepted annotation lanes are combined without changing any accepted review. All 31 imported contexts and the two inherited NEW assertions are retained in their original positions. The resulting dispositions are 15 ACCEPT, 5 MODIFY, 7 KEEP_AS_NON_CORE, 3 UNDECIDED, 1 REMOVE and the 2 inherited NEW assertions. No additional annotation or publication quotation was created. All 60 inherited quotation paths and reference associations remain exact. The preceding journal is historical and remains byte-for-byte unchanged; the qualifications below supersede its broader interpretations where specified.

Ser/Thr catalysis remains unresolved rather than absent. The 2009 minimal-pSer comparison tested an Eya3 fragment, not full-length EYA1. Later positive EYA1 preparation activity and human PP2A association must be considered alongside the multistep-purified Eya1 aPKC study, whose actual supplementary image includes a positive insect-cell lysate control. Those sources do not settle intrinsic catalysis by the three natural human products. The positive H2AX tyrosine-phosphatase evidence is preserved, with Eya3-specific recruitment, rescue and chromatin experiments separated from EYA1 assays. [PMID:19234442](https://pmc.ncbi.nlm.nih.gov/articles/PMC2692521/), [PMID:27795300](https://pmc.ncbi.nlm.nih.gov/articles/PMC5192086/), [PMID:29535359](https://pmc.ncbi.nlm.nih.gov/articles/PMC5849647/), [PMID:33472197](https://pmc.ncbi.nlm.nih.gov/articles/PMC8118085/).

All four protein-binding contexts identify SIX1, supporting the specific transcription-factor partner class. AP-MS cellular association, HuRI binary screening, mouse Eya1/Six reporter activity and EYA2/EYA3-specific biochemistry remain distinct. The two inherited NEW assertions are reassessed conserved coactivation claims; they are not newly manufactured coverage gaps or human-product-specific assays. Cytoplasmic EYA1 is positive evidence, not an established inactive storage pool. Mouse Eya1/Six organogenesis supports a contextual morphogenetic role, while precise auditory-perception participation remains unresolved. [PMID:10490620](https://pmc.ncbi.nlm.nih.gov/articles/PMC84678/), [PMID:15141091](https://pmc.ncbi.nlm.nih.gov/articles/PMC419562/), [PMID:19497856](https://pmc.ncbi.nlm.nih.gov/articles/PMC2742842/), [PMID:14628042](https://doi.org/10.1038/nature02083).

The PAINT judgment is assessed through the actual ancestral tree, alignment and IBD placement, including legitimate self-WITH evidence and explicit current-versus-imported donor differences. Current HPA nuclear staining and Reactome nucleoplasm participants retain their own resolution and product limits. EYA1 is an ATM phosphorylation substrate in the modeled reaction, not its kinase. The SUMO transfer is removed only after tracing actual donor and independent original experiments: EYA1 is modified by the conjugation machinery, without demonstrated work attaching SUMO. Its positive regulation by SUMO remains biological context. [PMID:16990542](https://doi.org/10.1126/science.1128406), [PMID:24954506](https://doi.org/10.1038/onc.2014.179).

Six shared reference assessments preserve separately labeled direct and database read scopes, including differences in pixel and supplementary access. The 23 original ordered reference identities/findings remain exact; five genuine normal references are appended. Publication caches were not rewritten to reflect separately recovered originals. The normal union contains 37 immutable records; selected dependencies are 21 cited publications, one Reactome record and two PAINT auxiliaries. Two genuine machine files are separately compared with committed preimages and are byte-identical. The three natural products remain 592, 559 and 557 residues, without functional-equivalence claims.

This is the annotation checkpoint. The legacy biological description, two ordered cores, questions, experiments and status are intentionally unchanged until the separate synthesis phase. Their preserved COMPLETE field is not a newly computed completion result. The source guide records operative public locators and access limitations; canonical validation, rendering and publication are outside this checkpoint.


## 2026-10-24 — synthesis of the two established activities

The two existing core positions now distinguish SIX-associated transcriptional coactivation from protein tyrosine dephosphorylation in the H2AX damage response. The first role rests on positive mouse Eya1/Six reporter experiments with promoter-site controls, supported independently by human EYA1–SIX1 association and EYA1 localization in human cells. It does not depend on interpreting a protein interaction screen as a coactivation assay. The myogenin reporter work in PMID:10490620 uses mouse Eya1 in COS7 cells; the Eya1 insert species/accession in PMID:15141091 is not supplied in the inspected Methods. PMID:19497856 tests EYA1 nuclear localization, but its purified binding and reporter experiments use EYA2. The detailed phosphatase-dependent coactivator recruitment and SIX1–DACH switch experiments in PMID:14628042 predominantly concern Eya3. Those historical family-level statements remain at their exact quotation positions and are contextual support, not new EYA1-specific demonstrations. No constitutive SIX1–DACH–EYA1 complex or universal catalytic requirement for coactivation is asserted.

The second role retains the independently supported general protein tyrosine phosphatase activity and explicitly identifies H2AX Tyr142 as a substrate. PMID:19234442 Figure 4B tests affinity-isolated Eya1 against histone H2AX with the Eya1 D323A control; Figure 4C tests endogenous human EYA1 depletion. Figure 2D places tagged Eya1 at irradiation-induced nuclear foci. The peptide-specificity experiment is bacterial Eya3, as are the detailed I-PpoI/MDC1 experiments and the plotted rescue. The main text reports an additional murine Eya1 rescue in a supplement that was not inspected. Repair-factor binding was measured in peptide/extract experiments, so the synthesis describes regulation of repair-permissive chromatin rather than EYA1 executing DNA strand restoration. The original's co-purifying Eya1/Eya3 observations do not establish an obligatory complex in every cell type. PMID:14628052 supplies independent purified mouse Eya1-domain tyrosine-phosphatase evidence.

Current GO:0140793 describes H2AX Tyr142 phosphate hydrolysis and reaches GO:0006338 through histone-state/chromatin relations. It does not currently have GO:0004725 in its captured ancestry. The core therefore retains GO:0004725 and describes the established substrate-specific reaction explicitly; no nonexistent ontology entailment is claimed and no extra activity is created merely to cover the classification mismatch. Chromatin remodeling and positive regulation of DNA repair are nonredundant process facets here; remodeling denotes changing the histone state, not an ATP-dependent nucleosome motor. The accepted inner-ear morphogenesis annotation remains a conserved gene-level developmental role. A specific otic promoter mechanism is not invented to place it in a molecular-function unit. Nucleus is retained as the activity location; nucleoplasmic HPA observations do not locate every reaction or every natural product.

The positive EYA1 phosphothreonine reports are preserved without making an intrinsic Ser/Thr phosphatase core. PMID:27795300 measures activity of EYA1 affinity preparations. PMID:29535359 explicitly finds human EYA1 associated with PP2A, while its decisive partner-dependence experiments use mouse Eya3. PMID:33472197 reports an active multistep-purified Eya1 preparation without detectable B55α and includes positive insect-cell antibody controls in Figure S6; its construct/product and internal S2/Sf9 and residue-numbering ambiguities remain explicit. These observations motivate catalyst-attribution experiments, not a claim of universal EYA1 inactivity or universal PP2A dependence. The three natural human products (592, 559 and 557 residues) remain distinct, with no transfer of all assay outcomes to each one.

All accepted annotation decisions, reference assessments and inherited findings remain unchanged at this synthesis stage. Historical journal paragraphs describe their original checkpoints. The new description is standalone biology; the questions and paired experiments address the remaining mechanistic and product boundaries.
