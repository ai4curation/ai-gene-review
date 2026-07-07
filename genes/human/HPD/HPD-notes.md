# HPD (4-hydroxyphenylpyruvate dioxygenase) — review notes

UniProtKB:P32754 (HPPD_HUMAN), gene HGNC:5147, HGNC symbol HPD. 393 aa, homodimer.

## Core biology (verified)
- HPD/HPPD catalyzes the **second step of tyrosine catabolism**: 3-(4-hydroxyphenyl)pyruvate + O2 → homogentisate + CO2 (Rhea:16189, EC 1.13.11.27). Unusual reaction: oxidative decarboxylation + aromatic ring hydroxylation + side-chain migration in a single active site. [UniProt CATALYTIC ACTIVITY; PMID:1339442; PMID:34047349; PMID:37794595]
- Non-heme **Fe(2+)-dependent dioxygenase** (VOC/glyoxalase-like double domain). Binds 1 Fe(2+) per subunit via His183, His266, Glu349 (2-His-1-carboxylate facial triad). [UniProt COFACTOR + BINDING; PMID:37794595]
- **Homodimer** of identical subunits. [PMID:1339442]
- Liver-enriched (HPA "Tissue enriched (liver)"). Reaction is cytosolic. [Reactome R-HSA-71163; PMID:41317403 "The tyrosine metabolic process is usually thought to occur in the cytoplasm"]
- Pathway: L-phenylalanine degradation → acetoacetate + fumarate, step 3/6 (UniPathway UPA00139). HPD is upstream of HGD (homogentisate 1,2-dioxygenase, alkaptonuria) in the same tyrosine-degradation pathway. [dismech Alkaptonuria.yaml]

## Drug target
- Molecular **target of nitisinone (NTBC)** (DrugBank DB00348), used to treat hereditary tyrosinemia type I (FAH deficiency) by blocking the pathway upstream of the toxic maleylacetoacetate/fumarylacetoacetate/succinylacetone intermediates. [UniProt ACTIVITY REGULATION; PMID:37794595; PMID:41317403]

## Disease
- **Tyrosinemia type III (TYRSN3, MIM:276710)**: autosomal recessive; HPD deficiency itself; high blood tyrosine, urinary tyrosine derivatives, ± seizures/mild intellectual disability. [PMID:10942115; PMID:11073718; UniProt DISEASE]
- **Hawkinsinuria (HWKS, MIM:140350)**: autosomal DOMINANT; the N241S variant produces the aberrant cyclic metabolite hawkinsin. [PMID:17560158; PMID:20677779; PMID:26226126]

## Scrutinized annotations

### GO:0001734 mRNA m(6)A methyltransferase activity — KEEP_AS_NON_CORE (not REMOVE)
- Source PMID:41317403 (Wang et al., Adv Sci 2026), full_text_available: true. This is a genuine, substantial EXPERIMENTAL paper: in vitro methylation with recombinant human HPD purified from E. coli (no accessory proteins), SAM binding (SPR/thermal shift), H183A/H266A + CMI-motif mutants abolish activity, eCLIP/MeRIP-seq RRACH motif, HPD-knockout mouse shows reduced global m6A. Authors themselves call it a **moonlighting** function sharing the tyrosine active-site pocket.
- Per CLAUDE.md policy: never REMOVE an experimental (IDA) annotation whose full text supports it. It IS surprising/unusual (a Fe-dioxygenase acting as a SAM-dependent RNA methyltransferase) and UniProt flags it with a CAUTION note. Therefore KEEP but mark **non-core** (moonlighting; secondary; cancer/ferroptosis context), NOT the core enzymatic identity.
- The IEA duplicate (GO_REF:0000120, from RHEA:55584|EC:2.1.1.348) is an electronic propagation of that same single-paper claim → MARK_AS_OVER_ANNOTATED (premature to auto-propagate an unusual moonlighting activity as if it were the primary EC identity).

### GO:0016701 oxidoreductase, single donors + O2 incorporation — MODIFY → GO:0003868
- InterPro2GO parent term; correct branch but too general. Replace with the specific child GO:0003868 (already present). MODIFY.

### GO:0005515 protein binding (IPI, PMID:31537781) — KEEP_AS_NON_CORE
- Experimental IPI with defined partners (TTC36 Q9BYT3? actually with/from A6NLP5=TTC36, Q96FA3=?, Q9BYT3=?). The paper (full text) shows HPD interacts with molecular chaperone TTC36, kinase STK33, and E3 ligase PELI1 — a stability/degradation regulatory axis (T382 phosphorylation → PELI1 ubiquitylation). These are regulatory interactions, not the core catalytic MF. Bare "protein binding" is uninformative (CLAUDE.md), but policy says don't remove experimental IPI; keep as non-core. No single informative adapter MF term fits (HPD is the substrate of regulation, not an adapter).

### Ensembl-Compara / membrane localizations
- IBA is_active_in Golgi membrane (GO:0000139) and ER membrane (GO:0005789) + matching IEA(SubCell)/ISS(from mouse P32755): UniProt lists these as ECO:0000250 (by-similarity to mouse) peripheral-membrane locations. HPD is fundamentally a soluble cytosolic enzyme; membrane association is weakly supported (by-similarity only). Keep as non-core (KEEP_AS_NON_CORE) — do not elevate to core; the reaction is cytosolic.
- Nucleus (GO:0005634) IDA (PMID:41317403) + IEA(SubCell)/ISS: tied to the moonlighting nuclear m6A function → non-core.
- Cytosol (GO:0005829, TAS Reactome) and cytoplasm (GO:0005737) = core location of the dioxygenase reaction. ACCEPT cytosol as core.
- Extracellular exosome (GO:0070062, HDA PMID:19056867): large-scale urinary-exosome proteomics; common contaminant-type localization → KEEP_AS_NON_CORE.

## Core functions
- MF: GO:0003868 4-hydroxyphenylpyruvate dioxygenase activity
- BP: GO:0006572 L-tyrosine catabolic process
- CC: GO:0005829 cytosol
- Metal binding (Fe/metal ion) is a supporting MF (GO:0046872 metal ion binding — present in UniProt DR as IEA-KW, not in GOA TSV; captured as core-function trait).
