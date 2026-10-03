# coYki (Capsaspora owczarzaki Yorkie/YAP/TAZ ortholog) - curation notes

**Automated deep research was unavailable** (no deep-research provider key in this
environment). These notes were built manually from the cached full text of the papers
in `publications/`. No `-deep-research-*.md` file exists for this gene.

## Identity

- UniProt A0A0D2WY30 (TrEMBL, unreviewed, 610 aa), "WW domain-containing protein";
  ORF name CAOG_007866 (UniProt) = CAOG_07866 (older Broad locus format used in
  the key resources table of PMID:35659869: "GenBankCAOG_07866").
- Gene named coYki in Phillips et al. 2022/2024; "Co-Yki"/"CoYki" in
  Sebé-Pedrós et al. 2012.
- InterPro: two WW domains (278-310, 340-373 in the UniProt model), IPR051583 YAP1
  family; PANTHER PTHR17616:SF8 "TRANSCRIPTIONAL COACTIVATOR YORKIE".
- Single Yorkie/YAP/TAZ ortholog in the genome [PMID:38517944 "generating a mutant of
  the single Yorkie/YAP/TAZ ortholog found in the genome (coYki)"].

### Sequence-numbering caveat (my own observation, not from a paper)

Phillips & Pan 2024 describe residue F123 of coYki as aligning with human YAP1 F95
(TEAD-binding). In the UniProt model A0A0D2WY30 the YAP1 motif `LPDSFFKPP`
(YAP1 S94/F95/F96) corresponds to `LPASFFRSP` at residues 54-62 (F58/F59), and there
is no Phe at position 123. HXRXXS motifs in the UniProt model sit at 20, 82, 114
and 235 (four motifs, matching the "four HXRXXS motifs" of the papers). So either the
published coYki cDNA (5'/3' RACE-checked in PMID:22832104) has a longer N-terminus
than the UniProt gene model, or the papers use a different numbering. Not resolved;
raised as a suggested question.

## Domain architecture and predicted function

- Conserved WW domains, phosphoregulatory sites and N-terminal TEAD-binding domain
  [PMID:35659869 "Protein domain architecture is conserved between Capsaspora Yorkie
  (coYki) and animal YAP/TAZ/Yorkie proteins, including conservation of tandem WW
  domains, phosphoregulatory sites, and an N-terminal TEAD-binding domain (TBD)"].
- [PMID:22832104 "all these non-metazoan Yki homologs contain highly conserved
  functional sites like the Hippo pathway responsive phosphorylation site S168/127 and
  the N-terminal homology region that is critical for interaction with Sd/TEAD
  transcription factor"].

## Heterologous activity in Drosophila (PMID:22832104) - demonstrated, but not in Capsaspora

- Co-Yki alone, overexpressed in the fly eye, does not cause overgrowth (small rough
  eye) [PMID:22832104 "overexpression of Co-Yki (GMR>Co-Yki) did not result in any
  tissue overgrowth, but rather caused a small and rough eye phenotype"].
- Co-Yki + Co-Sd (Capsaspora Scalloped/TEAD) together give massive overgrowth
  [PMID:22832104 "co-expression of Co-Yki and Co-Sd (GMR>Co-Sd+Co-Yki) resulted in
  massive tissue overgrowth resembling that caused by co-expression of their
  Drosophila counterparts"].
- Target genes Diap1 and Ex induced [PMID:22832104 "showed a marked upregulation of
  Diap1 and Ex staining posterior to the morphogenetic furrow"].
- Physical interaction (co-IP, epitope-tagged, S2R+ cells) and HRE-luciferase
  activation [PMID:22832104 "epitope-tagged Co-Sd and Co-Yki immunoprecipitated with
  each other in Drosophila S2R+ cells (Figure 4A), demonstrating their ability to form
  a protein complex"]; [PMID:22832104 "co-expression of Co-Sd and Co-Yki stimulated the
  transcription of the HRE-luciferase reporter in Drosophila S2R+ cells"].
- Co-Hpo phosphorylates/inhibits Co-Yki in S2R+ [PMID:22832104 "Co-Hpo significantly
  inhibited Co-Sd/Co-Yki-mediated activation of the diap1 HRE-luciferase reporter in
  S2R+ cells"]; [PMID:22832104 "expression of Co-Hpo induced phosphorylation of Co-Yki
  in S2R+ cells, and this phosphorylation was further enhanced by co-expression of
  Dm-Wts"].
- Note the "growth-regulatory activity" is a property shown in Drosophila tissue, not
  in Capsaspora, where coYki does not control proliferation (below).

## In Capsaspora (PMID:35659869, PMID:38517944) - demonstrated

### Knockout (coYki -/-, TBD replaced on both alleles by homologous recombination)
- [PMID:35659869 "replacing the putative TBD from each allele of the coYki gene with a
  distinct selectable antibiotic marker"].
- No proliferation phenotype [PMID:35659869 "we observed no significant difference in
  cell proliferation between WT and coYki -/- cells in either condition"]; EdU in
  aggregates also unchanged.
- Aggregates flatter, less circular, same size [PMID:35659869 "coYki -/- aggregates
  were asymmetric and less circular than WT aggregates"].
- Increased cell-substrate adhesion, normal cell-cell adhesion [PMID:35659869
  "indicating that coYki negatively regulates cell"] (the full sentence contains an
  en dash; see paper).
- Ectopic actin-depleted blebs, rescued by coYki transgene
  [PMID:35659869 "a phenotype that was rescued in coYki -/- cells expressing a coYki
  transgene"]; [PMID:35659869 "These results suggest that the protrusions observed in
  coYki -/- cells are actin-depleted blebs"].
- Blebbistatin suppresses blebbing and rescues aggregate shape [PMID:35659869
  "blebbistatin also rescued the abnormal morphology of coYki -/- aggregates"].
- RNA-seq: 1205 DE genes (397 down, 808 up in mutant); actin-binding genes enriched
  among up-regulated; no proliferation/cell-cycle enrichment [PMID:35659869 "This
  analysis revealed 1205 differentially expressed genes, including 397 downregulated"];
  [PMID:35659869 "no enrichment was detected in functional categories of cell
  proliferation or the cell cycle"]. Authors flag possible transcription-independent
  action [PMID:35659869 "we cannot formally exclude the possibility that coYki may also
  regulate cytoskeletal dynamics in a transcription-independent manner"].
- Two integrin-beta genes upregulated in mutant [PMID:35659869 "two integrin-β genes
  (CAOG_05058 and CAOG_01283) are upregulated in coYki -/- cells"].

### Localization
- mScarlet-coYki (transient, WT cells) is cytoplasm-enriched; 4SA mutant uniform or
  nuclear [PMID:35659869 "Cells transfected with mScarlet-coYki showed mScarlet
  enriched in the cytoplasm relative to the nucleus"]; [PMID:35659869 "the majority of
  cells transfected with mScarlet-coYki 4SA showed uniform mScarlet signal throughout
  the cell or enriched mScarlet signal in the nucleus"].
- In coHpo-/- and coWts-/- cells, mScarlet-coYki nuclear >= cytoplasmic
  [PMID:38517944 "the majority of coHpo-/- and coWts-/- cells showed nuclear levels of
  mScarlet-coYki greater than or equal to that seen in the cytoplasm"];
  [PMID:38517944 "these results show that the Capsaspora Hippo kinase cascade regulates
  coYki by cytoplasmic sequestration"].
- Density regulation of coYki localization was NOT examined in these papers (I found no
  experiment varying cell density and scoring coYki localization).

### Hyperactive coYki (PMID:38517944)
- coYki 4SA stable transgene phenocopies coHpo/coWts loss (increased aggregate cell
  packing, elongated adherent cells) [PMID:38517944 "stable transgenic expression of
  coYki 4SA resulted in increased cell packing of Capsaspora aggregates"].
- Requires the TEAD-binding residue: [PMID:38517944 "in contrast to coYki 4SA, the
  expression of a coYki 4SA F123A mutant did not affect cell or aggregate morphology"];
  [PMID:38517944 "This result indicates that these phenotypes are mediated by the
  transcriptional activity of coYki."]
- 107-gene "core Hippo pathway" DE set shared by coYki, coHpo, coWts mutants; enriched
  in membrane proteins and laminin G domain proteins.
- No direct coYki-coSd interaction or ChIP has been done in Capsaspora itself.

## Annotation decisions (summary)

| Term | Action | Reason |
|---|---|---|
| GO:0003713 transcription coactivator activity | ACCEPT | Co-Sd/Co-Yki activates HRE reporter and Diap1/Ex (heterologous); F123A abolishes 4SA phenotypes in Capsaspora |
| GO:0005634 nucleus | ACCEPT | nuclear in kinase mutants and 4SA; regulated nuclear entry |
| GO:0005737 cytoplasm | ACCEPT | predominantly cytoplasmic in WT cells (sequestration) |
| GO:0035329 hippo signaling | ACCEPT | coHpo/coWts regulate coYki localization in Capsaspora; coYki is the effector named in the GO definition; YAP1 and yki carry the term |
| GO:0045944 positive regulation of transcription by RNA polymerase II | ACCEPT | HRE-luciferase / Diap1 induction with Co-Sd; transcription-dependent phenotypes |
| NEW GO:0140297 DNA-binding transcription factor binding | IPI | co-IP with Co-Sd in S2R+ cells |

Track C note (ORIGINS_OF_MULTICELLULARITY): none of the five TreeGrafter/ARBA rows is
an animal-specific process mis-propagated to a unicellular protein. "hippo signaling"
is a signalling-cassette term, not a multicellular process, and it is experimentally
supported in Capsaspora itself. No row asserts regulation of cell proliferation or
organ size, which the knockout data contradict. No process NEW terms proposed:
blebbing, cell-substrate adhesion and aggregate shape phenotypes are necessity
evidence downstream of an unidentified transcriptional program (fails participation
test as a direct process annotation).
