# PGLS (human) — 6-phosphogluconolactonase — review notes

UniProt: O95336 (6PGL_HUMAN); HGNC:8903; EC 3.1.1.31; 258 aa; chr19.
Family: glucosamine/galactosamine-6-phosphate isomerase family, 6-phosphogluconolactonase subfamily.
InterPro: IPR005900 (6PGL_DevB), IPR039104 (6PGL), IPR006148 (Glc/Gal-6P isomerase). CDD cd01400 (6PGL). PANTHER PTHR11054.

## Core biology

PGLS is the **second enzyme of the oxidative branch of the pentose phosphate pathway
(oxiPPP)**. It hydrolyses **6-phospho-D-glucono-1,5-lactone** (the product of G6PD,
the first oxiPPP enzyme) to **6-phospho-D-gluconate** (the substrate of the third
enzyme, 6PGD/PGD). RHEA:12556; EC 3.1.1.31.

- UniProt FUNCTION: "Hydrolysis of 6-phosphogluconolactone to 6-phosphogluconate."
  [file:human/PGLS/PGLS-uniprot.txt]
- UniProt PATHWAY: pentose phosphate pathway; D-ribulose 5-phosphate from
  D-glucose 6-phosphate (oxidative stage): step 2/3. [ECO:0000269|PubMed:10518023]

### Identification / catalytic activity (PMID:10518023, Collard et al. 1999)
Human cDNA cloned; protein expressed in E. coli, purified, and "shown to be
6-phosphogluconolactonase, the enzyme catalyzing the second step of the pentose
phosphate pathway." Homologous to bacterial devB and to the C-terminal part of
human hexose-6-phosphate dehydrogenase; related to glucosamine-6-phosphate
isomerases. This is the source of the EXP/IDA MF and pentose-phosphate-shunt BP
annotations. full_text_available: false (abstract only).

### Enzymatic role clarified by NMR (PMID:11457850, Miclet et al. 2001)
"6-Phosphogluconolactonase is the second enzyme of the oxidative branch and
catalyzes the hydrolysis of 6-phosphogluconolactones, the products of glucose
6-phosphate oxidation by glucose-6-phosphate dehydrogenase." Key point: the
δ-form (1→5) is the only G6PD product and the only PGLS substrate; it can undergo
slow spontaneous hydrolysis but can also rearrange to the γ-form (1→4), a "dead
end." PGLS "activity accelerates hydrolysis of the delta form, thus preventing its
conversion into the gamma form" and "guards against the accumulation of
delta-6-phosphogluconolactone, which may be toxic through its reaction with
endogenous cellular nucleophiles." IDA MF (PMID:11457850). full_text_available: false.

### PGLS in oxiPPP / signaling (PMID:31586547, Gao et al. 2019, Mol Cell)
Full text available. Confirms PGLS as "the second oxiPPP enzyme" that "converts 6PGL
to 6-phosphogluconate (6PG)." Knockdown of PGLS reduces oxiPPP flux, decreases 6PG,
accumulates 6PGL (δ and γ), increases ROS, and activates AMPK via decreased PP2A
activity; reduces cell proliferation/tumor growth in xenografts. This is the basis
for the IMP `acts_upstream_of_or_within` GO:0009051 annotation — genetic perturbation
of PGLS alters oxiPPP output. The paper's headline mechanistic finding (γ-6PGL → Src →
PP2A → AMPK) is a downstream signaling consequence, not a molecular function of PGLS
itself; the annotation appropriately uses the metabolic-branch BP term.

## Localization
- Cytosolic. UniProt SUBCELLULAR LOCATION: Cytoplasm (ECO:0000250). Reactome
  R-HSA-71296 states "Cytosolic 6-phosphogluconolactonase (PGLS)". HPA IDA cytosol +
  IBA cytosol. This is the core/consensus location.
- HPA IDA nucleoplasm (GO:0005654): HPA immunofluorescence also scores nucleoplasm.
  Small soluble metabolic enzymes are commonly detected in the nucleoplasm by IF;
  no described nuclear function. Keep as non-core.
- Extracellular exosome (GO:0070062), two HDA proteomics datasets (PMID:23533145
  prostatic-secretion/urine exosomes; PMID:19056867 urinary exosomes). Bulk
  MS detection in secreted vesicles; abundant cytosolic enzymes routinely appear in
  exosome proteomes. Non-core; over-annotation from high-throughput MS.
- IEA cytoplasm (GO:0005737, UniProt SubCell mapping): broad-but-correct parent of
  cytosol. Accept.

## protein binding (IPI, GO:0005515) — two annotations
- PMID:21044950 (Lee et al. 2011, Mol Cell Proteomics): genome-wide split-YFP (BiFC)
  complementation screen for **telomere** signaling regulators; PGLS (with TERF2IP/
  RAP1, IntAct with UniProtKB:Q9NYB0) is one of >300 hits, "the majority ... have not
  been previously linked to telomere biology." High-throughput, uncharacterized;
  bare `protein binding` is uninformative. MARK_AS_OVER_ANNOTATED (do not REMOVE per
  policy; it is a real IPI, not clearly wrong).
- PMID:32296183 (Luck et al. 2020, HuRI): human all-by-all binary interactome
  (Y2H-based); PGLS–BLMH (UniProtKB:Q13867). Systematic, no PGLS-specific functional
  follow-up. Bare `protein binding` uninformative. MARK_AS_OVER_ANNOTATED.
- Both interactions are also recorded in the UniProt INTERACTION block (BLMH Q13867;
  TERF2IP Q9NYB0), i.e. IntAct-curated but with no functional interpretation for PGLS.

## Disease
No well-established Mendelian disease associated with PGLS (unlike G6PD). MIM 604951
is the gene entry. Reviewed here as the middle step of the oxidative PPP.

## Reference reliability
- PMID:10518023, 11457850, 31586547: HIGH relevance, VERIFIED (directly establish the
  enzyme's identity/activity/pathway role).
- PMID:21044950, 32296183: interactome screens, LOW relevance to PGLS function; the
  citations are correct (VERIFIED) but only support a bare interaction.
- PMID:23533145, 19056867: exosome proteomics, LOW relevance; VERIFIED as MS detection.
- Reactome R-HSA-71296 / R-HSA-71336: HIGH relevance, VERIFIED.

## Core functions (author-supplied, strictly validated)
- MF: GO:0017057 6-phosphogluconolactonase activity (confirmed current label, MF).
- BP: GO:0009051 pentose-phosphate shunt, oxidative branch (confirmed current label, BP).
- CC: GO:0005829 cytosol (confirmed current label, CC).
