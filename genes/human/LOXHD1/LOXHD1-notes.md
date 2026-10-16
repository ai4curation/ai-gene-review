# LOXHD1 review notes

## Reference synthesis (2026-08-10)

### Blockers and evidence boundaries

- No direct molecular-function or nanoscale-localization experiment in human cochlear
  hair cells was found. The mechanistic evidence is from mouse cochlear hair cells, with
  human evidence principally genetic. [PMID:19732867 "Based on the studies in mice, we
  screened DNA from human families segregating deafness and identified a mutation in
  LOXHD1, which causes DFNB77, a progressive form of autosomal-recessive nonsyndromic
  hearing loss (ARNSHL)."]
- The foundational cache is abstract-only (`full_text_available: false`), even though its
  metadata lists PMCID PMC2771534. Claims from PMID:19732867 are therefore restricted to
  verbatim abstract statements; detailed assays and isoform identity were not inferred.
- The 2021 physiology study tested two mouse mutations affecting PLAT repeat 10, not a
  clean deletion of all isoforms. One engineered nonsense allele underwent
  nonsense-associated altered splicing, so its phenotype cannot automatically establish
  the requirement for every domain or isoform. [PMID:33707295 "Using two mouse mutants of
  LOXHD1-PLAT10, we demonstrated here that inner hair cell (IHC) mechanotransduction
  currents were drastically reduced at P11, in contrast to the wild-type (WT)-like MET
  currents observed at P7."]
- The 2024 study addresses that limitation with a mouse genomic deletion intended to
  remove all PLAT-repeat-coding exons. Its co-immunoprecipitation assays used tagged,
  overexpressed proteins in HEK293T cells; they demonstrate selective association under
  those conditions, not a direct binding interface or a fixed-stoichiometry complex.
  [PMID:39256406 "These experiments demonstrate that LOXHD1 interacts selectively in
  vitro with TMC1 but not with TMC2."]
- Human UniProt Q8IVV2 lists four splice isoforms, 15 Pfam PLAT matches in the displayed
  sequence, and protein evidence at transcript level. It does not establish which human
  isoform performs the cochlear function. [file:human/LOXHD1/LOXHD1-uniprot.txt
  "CC       Event=Alternative splicing; Named isoforms=4;"] [file:human/LOXHD1/LOXHD1-uniprot.txt
  "PE   2: Evidence at transcript level;"]
- A 13-PLAT-repeat short isoform has been experimentally characterized in Ewing-sarcoma
  cells, where it is driven from an alternative transcription start site. This is a
  disease-context boundary, not evidence for normal cochlear isoform use.
  [PMID:35705030 "The short isoform LOXHD1 contains 33 exons and codes for 1891 aa protein
  containing 13 PLAT and 1 coiled-coil domains (Figure 2B)."]

### Prioritized direct-function evidence

1. The strongest evidence supports LOXHD1 as a nonenzymatic component of the mature
   auditory mechanotransduction apparatus. In mouse inner hair cells, it maintains TMC1
   at the tips of shorter stereocilia near the lower tip-link force-transmission site.
   [PMID:39256406 "Overall, these SUB-immunogold-SEM experiments support that LOXHD1 is
   required for the maintenance of TMC1 in IHC stereocilia. Importantly, LOXHD1 is also
   critical for maintenance of TMC1 within the first 100 nm of the row 2 tips, where the
   tip links insert and where the mechanical stimuli are received."]
2. LOXHD1 dependence is selective for the mature TMC1 configuration rather than the
   developmental TMC2 configuration. Heterologous co-immunoprecipitation found selective
   association with TMC1, and the mouse deletion displaced TMC1 while sparing TMC2.
   [PMID:39256406 "These experiments demonstrate that LOXHD1 interacts selectively in
   vitro with TMC1 but not with TMC2."]
3. Earlier mouse physiology established a developmental requirement for LOXHD1 after the
   first postnatal week: mechanotransduction currents declined by P11 despite retained
   gross bundle structure and key tip-link complex proteins. [PMID:33707295 "The Loxhd1
   MET defect was novel, as it occurred without an altered hair bundle structure or
   mislocalization of key upper (Harmonin) or lower (LHFPL5) TL complex proteins."]
4. The original mouse study localizes LOXHD1 along the mature stereociliary membrane and
   shows that mutation perturbs hair-cell function without blocking initial
   stereociliary development. [PMID:19732867 "Stereociliary development is unaffected in
   samba mice, but hair cell function is perturbed and hair cells eventually degenerate."]
5. Human evidence directly establishes disease relevance—biallelic LOXHD1 variation can
   cause progressive autosomal-recessive nonsyndromic hearing loss—but does not by itself
   define molecular activity. [PMID:19732867 "Based on the studies in mice, we screened
   DNA from human families segregating deafness and identified a mutation in LOXHD1,
   which causes DFNB77, a progressive form of autosomal-recessive nonsyndromic hearing
   loss (ARNSHL)."]

### Curation implications

- Do not infer lipoxygenase catalytic activity from the name. The protein consists of
  repeated PLAT/LH2 domains, and no LOXHD1-catalyzed reaction or substrate was identified.
- `stereocilium` and `sensory perception of sound` are strongly supported conserved
  annotations. A more precise role in hair-cell mechanotransduction is supported by mouse
  primary studies, but any human annotation should state the orthology/model boundary.
- Interaction language should be assay-calibrated: use "co-immunoprecipitates with" or
  "associates with" for TMC1, CIB2, LHFPL5 and PCDH15 unless direct binding is separately
  demonstrated. Do not imply a single stable complex containing every partner.

## Finishing pass (2026-09-04, PAINT no-IBA project)

Final quality pass over LOXHD1-ai-review.yaml for the PAINT "human no-IBA" project.

- Re-checked all six GOA-derived entries (all ACCEPT) and the two proposed NEW ISO
  refinements (GO:0050910 detection of mechanical stimulus involved in sensory
  perception of sound; GO:0032426 stereocilium tip); all actions were found justified
  and retained. The mouse-vs-human evidence boundary is consistently stated
  [PMID:33707295 "Using two mouse mutants of LOXHD1-PLAT10, we demonstrated here that
  inner hair cell (IHC) mechanotransduction currents were drastically reduced at P11,
  in contrast to the wild-type (WT)-like MET currents observed at P7."].
- Cleared the last validation warning by adding
  file:human/LOXHD1/LOXHD1-deep-research-falcon.md as a reference and citing it in the
  GO:0050910 NEW entry. The reliance is genuine: the deep-research synthesis
  independently supports the no-molecular-function decision
  [file:human/LOXHD1/LOXHD1-deep-research-falcon.md "No catalytic residues, reaction,
  substrate specificity, kinetic constants, or small-molecule products have been
  established."] and the ISO framing
  [file:human/LOXHD1/LOXHD1-deep-research-falcon.md "equivalent nanoscale localization
  in human cochlear tissue has not been demonstrated in the retrieved sources"]. Its
  reference_review notes that it is grounded chiefly in the Research Square preprint of
  the Wang et al. work whose peer-reviewed version (PMID:39256406) this review cites
  directly.
- Validation now clean (0 errors, 0 warnings); status advanced DRAFT -> COMPLETE (set
  by hand to the update-status tool's expected value; the tool only reports mismatches).
- Notable curation finding: the "no-IBA" premise does not hold. PTHR45901-paint.tsv
  carries IBDs at PTN000093787 (GO:0032420 and GO:0007605, taxon Amniota, dated
  20220323) and the human GOA contains the matching IBA rows since 2022. Both were
  adjudicated SOUND in the new family review
  (interpro/panther/PTHR45901/PTHR45901-review.yaml); the finer 2021/2024-era terms
  (GO:0050910, GO:0032426) are recorded there as subfamily-scoped term_assessments for
  the LOXHD1 clade (PTHR45901:SF3), with the explicit warning that auditory terms must
  never migrate to the family root - PANTHER's official family name ("PROTEIN
  CBG12474") comes from an uncharacterized nematode member.
