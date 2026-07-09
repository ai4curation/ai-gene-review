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
