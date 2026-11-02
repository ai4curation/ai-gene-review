# DGUOK (Q16854) review notes

Human deoxyguanosine kinase, mitochondrial. Deep research via falcon was unavailable
(provider out of credits, HTTP 402); this review is grounded in the UniProt record,
the seeded GOA TSV, and the cached publications.

## Core biology
- DGUOK is the **purine arm** of the mitochondrial deoxyribonucleoside salvage pathway.
  It phosphorylates the purine deoxyribonucleosides **deoxyguanosine (dGuo) and
  deoxyadenosine (dAdo)** (also deoxyinosine, arabinosyl-guanine, cladribine) to their
  monophosphates (dGMP, dAMP) inside the **mitochondrial matrix**, using ATP (or another
  NTP) as phosphate donor [PMID:8706825 "phosphorylation of purine deoxyribonucleosides in the"; PMID:17073823 "rate-limiting phosphorylation of the purine deoxynucleosides, using a nucleoside"].
- Highest efficiency for deoxyguanosine (EC 2.7.1.113); also acts on deoxyadenosine
  (EC 2.7.1.76) [UniProt CATALYTIC ACTIVITY, EC=2.7.1.113 / EC=2.7.1.76].
- Together with TK2 (pyrimidine arm), it supplies dNTPs for **mtDNA replication in
  non-proliferating/post-mitotic tissues**, where cytosolic de-novo dNTP synthesis is
  down-regulated [PMID:11687801 "mtDNA synthesis depends solely on the mitochondrial"].
- Homodimer; structure solved as complex with dATP (PDB 2OCP) [UniProt SUBUNIT].
- DCK/DGK family; ~46-48% identity to cytosolic deoxycytidine kinase (DCK)
  [PMID:8692979; UniProt SIMILARITY].

## Localisation
- Mitochondrion / mitochondrial matrix; nuclear-encoded with cleaved N-terminal
  mitochondrial transit peptide (residues 1-39) [UniProt SUBCELLULAR LOCATION; TRANSIT].
- The **nucleus** HDA annotation (PMID:21630459) is from a sperm-nucleus proteome
  catalogue (403 proteins co-isolated); not a validated functional localisation — treat
  as over-annotation / contaminant, not core.

## Disease
- MTDPS3: hepatocerebral mitochondrial DNA depletion syndrome (infantile liver failure +
  neurologic features) [UniProt DISEASE MTDPS3; PMID:12205643, PMID:15639197].
- NCPH1: non-cirrhotic portal hypertension (N46S) [PMID:26874653, PMID:17073823].
- PEOB4: adult-onset progressive external ophthalmoplegia / mtDNA multiple deletions
  [PMID:23043144].

## Annotation-review reasoning highlights
- MF core: GO:0004138 deoxyguanosine kinase activity and GO:0004136 deoxyadenosine kinase
  activity — both strongly experimentally supported (EXP/IDA/TAS) and are the core MF.
- GO:0004137 **deoxycytidine kinase activity** (IBA only): DGUOK is purine-specific; dCyd
  is the substrate of the paralog DCK, not DGUOK. This IBA over-reaches from the family
  tree; MARK_AS_OVER_ANNOTATED (do not attribute dCK activity to DGUOK).
- GO:0019136 deoxynucleoside kinase activity (IEA): correct but generic parent; ACCEPT
  as a valid broad umbrella.
- GO:0005524 ATP binding (IEA): supported by structure/ligand binding; ACCEPT.
- GO:0005737 cytoplasm (IBA is_active_in): DGUOK is matrix-resident; the pan-family IBA
  reflects the cytosolic paralogs (DCK etc.). MARK_AS_OVER_ANNOTATED — the specific,
  correct compartment is mitochondrion/matrix.
- BP:
  - GO:0106383 dAMP salvage (IDA, PMID:19221117): ACCEPT, core process (dAMP product).
  - GO:0046122 purine deoxyribonucleoside metabolic process (IDA, PMID:8706825): ACCEPT,
    core process.
  - GO:0008617 guanosine metabolic process (TAS, PMID:8692979): substrate is
    2'-deoxyguanosine, not guanosine; slightly mis-specified. MODIFY toward
    GO:0046122 (purine deoxyribonucleoside metabolic process).
  - GO:1901135 carbohydrate derivative metabolic process (ARBA IEA): extremely generic
    umbrella; KEEP_AS_NON_CORE.
  - GO:0010977 negative regulation of neuron projection development (Ensembl ortholog IEA
    from rat): not a demonstrated DGUOK function in human; over-propagated ortholog
    transfer. REMOVE (clearly wrong IEA inference).
  - GO:0042775 mitochondrial ATP synthesis coupled electron transport (Ensembl ortholog
    IEA from rat): DGUOK is a salvage kinase, not an OXPHOS/ETC component; the mtDNA-
    depletion phenotype secondarily affects the respiratory chain but DGUOK is not
    *involved_in* electron transport. REMOVE (clearly wrong IEA inference).
- CC mitochondrion (multiple IBA/IEA/ISS/IDA/HTP/TAS) and mitochondrial matrix (TAS):
  ACCEPT; matrix is the most specific correct location.
- protein binding IPIs (PMID:33961781 BioPlex, PMID:40205054 cell-map): both interactome
  screens; WITH/FROM = DCK (P27707). Bare "protein binding" is uninformative;
  MARK_AS_OVER_ANNOTATED per policy (do not REMOVE IPI). DGUOK-DCK is a documented
  interaction in the UniProt INTERACTION block.
</content>
</invoke>


## 2026-10-17 evidence reassessment

This entry supersedes the earlier action rationale while preserving it as a record. The [source guide](DGUOK-source-guide.md) gives public originals, figure/table locators, source-role distinctions and access limits.

The full original [PMID:8692979, Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC38970/) reports low dCyd phosphorylation. The earlier absolute purine-specificity and paralog-leakage claims are therefore withdrawn. The actual PAINT lineage contains the relevant ancestral nodes, and target self-evidence is legitimate. The inherited dCyd activity remains non-core. Human mitochondrial-enriched fibroblast assays ([PMID:17073823](https://pmc.ncbi.nlm.nih.gov/articles/PMC1798436/)) and muscle assays ([PMID:23043144](https://pmc.ncbi.nlm.nih.gov/articles/PMC3501975/)) corroborate dA/dG phosphorylation without proving equal activity of all six products. dIno yields dIMP; it is not another source of dGMP or dAMP.

The sperm-nucleus contamination rationale is also withdrawn. The coauthor's original supporting catalogue in thesis Appendix 8.2/Table 8.1 identifies Q16854 with two peptides and 13.4% coverage. The specialized nuclear detection is retained as non-core; no nuclear catalytic mechanism is inferred. Broad cytoplasm includes organelles and is compatible with matrix residence. Matrix-specific replacements cite independent human evidence and the explicit Reactome catalyst, rather than claiming each localization source resolved that compartment.

The two DCK interactions are retained with the supported kinase-binding partner class. Exact BioPlex records and the released U2OS edge establish co-complex associations, not purified direct binding, native mitochondrial heterodimers or activation. Rat-source tracing recovers genuine neurite and respiratory phenotype experiments. The neurite effect is retained as context-specific; electron-transport assignment is marked as mechanistically over-annotated because DGUOK supplies nucleotide precursors rather than performing electron transfer.

All 32 historical source dictionaries and six product objects remain intact. Current QuickGO source-version differences are described separately. The two core entries represent two reactions of one enzyme; no new annotation is proposed. Existing publication and provider files remain unchanged. The current provider attempt failed authentication/quota checks, and the source guide records the manual evidence used instead.


## 2026-10-17 ATP-binding and source-anchor clarification

ATP binding is retained as a true component of the enzyme mechanism, rather than replaced by kinase terms from a different ontology branch. The recombinant human assay uses ATP directly ([PMID:8692979](https://pmc.ncbi.nlm.nih.gov/articles/PMC38970/), p.7259, Enzyme Assays/Table 1). The [source guide](DGUOK-source-guide.md) now exposes the original low dCyd activity sentence and exact table values without altering the abstract-only publication cache. Focused cache-valid quotations were added to selected assertions, within a 25-word total per paper including inherited note quotations.

The two rat-source annotations describe different kinds of claims. The positive neurite screen supports a contextual negative-regulatory phenotype ([PMID:18007665](https://pubmed.ncbi.nlm.nih.gov/18007665/)); the exact DGUOK rat-validation panel remains inaccessible and is retained with explicit curator deference. This does not identify a direct axonal mechanism. In contrast, the respiratory phenotype reflects nucleotide supply and mtDNA integrity ([PMID:30404003](https://pmc.ncbi.nlm.nih.gov/articles/PMC6289059/), Figure 3), without demonstrating electron transfer by DGUOK. The non-core versus over-annotation distinction follows those term definitions, not different treatment of the same ortholog.

The homodimer is supported by curated structural evidence, and the mitochondrial targeting sequence remains a prediction rather than a newly mapped cleavage site. No equal-function claim is made for the six alternative products. Prior notes, including superseded judgments and inherited markup, are retained unchanged.
