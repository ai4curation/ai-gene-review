# CCDC50 (Coiled-coil domain-containing protein 50 / Ymer) — review notes

UniProt: Q8IVM0 (CCD50_HUMAN), 306 aa (isoform 1, major). HGNC:18111. Synonyms: C3orf6, Ymer.

## Domain architecture (UniProt)
- Coiled-coil (63–130).
- Large disordered C-terminal region (215–306).
- N-terminal acetylated (Ala-2), phosphorylated on Ser-5 and on tyrosine residues (EGF-induced).
- A short crystallized peptide (170–178, PDB 6LAN).
Note: Ymer harbors a "MIU"-type ubiquitin-interacting motif (reported in the literature) that binds K63-linked polyubiquitin; this is the molecular basis of its ubiquitin-binding behavior in NF-kB regulation and EGFR sorting.

## EGFR signaling / Ymer
- [PMID:15314609 "Temporal analysis of phosphotyrosine-dependent signaling networks"] — Ymer (CCDC50) identified as an EGF-induced tyrosine-phosphorylated protein involved in EGFR signaling. Basis of the UniProt FUNCTION "Involved in EGFR signaling" and the original "effector of EGF-mediated cell signaling" description. (Not cached; verified via UniProt reference list.)
- [PMID:17503326 "CCDC50 encodes Ymer, an effector of epidermal growth factor (EGF)-mediated cell signaling... suggested to inhibit down-regulation of the EGF receptor... Ymer is a soluble, cytoplasmic protein... colocalizes with microtubules of the mitotic apparatus"] — DFNA44 progressive hearing-loss mutation; expression restricted to cochlear pillar cells, stria vascularis, vestibular sensory epithelia. Supports cytoplasm/cytosol localization and the sensory perception of sound (GO:0007605) phenotype annotation (IMP, deafness).

## NF-kB / K63-polyubiquitin / innate immune signaling
- [PMID:18029035 "Involvement of Ymer in suppression of NF-kappaB activation by regulated interaction with lysine-63-linked polyubiquitin chain"] — Ymer interacts with A20 (TNFAIP3) and binds K63-linked polyubiquitin chains on RIP1/RIPK1; overexpression down-regulates NF-kB signaling, knockdown up-regulates it. Establishes K63-polyUb binding and a negative-regulator role in NF-kB signaling. Interactome (UniProt) includes OTUD7B, RIPK1, RNF8, ARRDC3, UBB — consistent with a ubiquitin-pathway scaffold.

## EGFR endosomal sorting / ubiquitin ligase binding
- [PMID:23418353 "The E3 ubiquitin ligases RNF126 and Rabring7 regulate endosomal sorting of the epidermal growth factor receptor"] — CCDC50/Ymer interacts with RNF126 (source of the IPI ubiquitin protein ligase binding GO:0031625 annotation). RNF126 functions in EGFR endosomal sorting downstream of c-Cbl. Connects Ymer to ubiquitin-dependent receptor sorting.

## Selective autophagy receptor (literature beyond cached set; context for review)
CCDC50/Ymer has been reported as a TBK1-binding selective autophagy receptor that recognizes K63-polyubiquitinated cargo and links it to LC3 — implicated in aggrephagy/reticulophagy and in negative regulation of antiviral innate immunity (RIG-I/MAVS) by delivering activated RIG-I/aggregated signaling components for autophagic degradation (e.g., Hou et al., Autophagy 2021). These roles are consistent with its K63-polyUb binding (PMID:18029035) and ubiquitin-ligase binding (PMID:23418353) but are not represented in the current GOA annotation set, so no existing annotation captures the autophagy-receptor MF directly. Recorded as a proposed gap / question.

## Localization
Cytoplasm / cytosol (HPA IDA; PMID:17503326). Associated with microtubules of cytoskeleton and mitotic apparatus (by similarity / PMID:17503326). No nuclear core role.

## Disease
DFNA44 autosomal dominant progressive hearing loss [MIM:607453] caused by CCDC50 variants [PMID:17503326].

## Annotation set (GOA): 8 annotations
1. GO:0005737 cytoplasm IBA (is_active_in) — localization OK; "is_active_in" qualifier unusual for a CC but reflects PAN-GO.
2. GO:0031625 ubiquitin protein ligase binding IBA — supported (RNF126 binding, PMID:23418353); enables.
3. GO:0005737 cytoplasm IEA (located_in) — OK.
4. GO:0005515 protein binding IPI (PMID:18029035) — A20/RIP1 K63-polyUb context; bare protein binding uninformative.
5. GO:0005515 protein binding IPI (PMID:32296183) — HuRI binary interactome.
6. GO:0005829 cytosol IDA (HPA, GO_REF:0000052) — OK core localization.
7. GO:0007605 sensory perception of sound IMP (PMID:17503326) — DFNA44 deafness phenotype; acts_upstream_of_or_within. Pleiotropic/tissue-specific.
8. GO:0031625 ubiquitin protein ligase binding IPI (PMID:23418353) — RNF126; supported.

## Key GO terms verified via QuickGO API
- GO:0031625 ubiquitin protein ligase binding (existing label correct).
- GO:0035973 aggrephagy; GO:0061709 reticulophagy; GO:0160247 autophagy cargo adaptor activity; GO:0032480 negative regulation of type I interferon production (candidate proposed terms / questions).
