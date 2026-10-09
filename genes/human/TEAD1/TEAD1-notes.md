# TEAD1 (human, P28347) - curation notes

**Automated deep research was unavailable** (no deep-research provider keys in this
environment). These notes were written manually from the cached publications in
`publications/` (checking `full_text_available:` for each) and the UniProt record. No
`-deep-research-*.md` file exists for this gene.

## Identity and domains

- TEA domain DNA-binding transcription factor (TEF-1); four human paralogs TEAD1-4.
- Domain layout: [PMID:20123905 "TEAD contains an N-terminal TEA DNA-binding domain ( Anbanandam et al. 2006 ) and a C-terminal region responsible for YAP interaction"].
- Motif: UniProt FUNCTION: binds "SPH and GT-IIC 'enhansons' (5'-GTGGAATGT-3') and activates" transcription; also the M-CAT motif.
- Mouse mTEF-1 is the ubiquitous M-CAT (A element) binding factor of the beta-MHC promoter
  [PMID:8396764 "The in vitro transcription/translation product of mTEF-1 cDNA bound to the A element, and the DNA binding property of mTEF-1 was identical to that of the A2 factor."] (abstract only).
- Disease: Sveinsson chorioretinal atrophy, TEAD1 Y406H, in the YAP-binding interface.

## Core function: DNA-binding partner of YAP/TAZ

- [PMID:18579750 "Since YAP does not have DNA-binding activity, these data strongly indicate that TEAD plays a major role in mediating the binding of YAP to gene promoters."]
- ChIP-on-chip: [PMID:18579750 "Interestingly, our results demonstrated that YAP and TEAD1 co-occupy >80% of the promoters pulled down by either of them"].
- CTGF reporter: [PMID:18579750 "the activation was further enhanced by TEAD1 coexpression ( Fig. 3B )"].
- **Paralog caveat**: the knockdowns used one shRNA against three paralogs
  [PMID:18579750 "Indeed, these shRNAs were able to knock down TEAD1, TEAD3, and TEAD4 concurrently but not TEAD2 (Supplemental Fig. S1C)."].
  TEAD1 was not in the Gal4-TF screen library and was tested separately
  [PMID:18579750 "TEAD1 was not present in our Gal4-TF library, but it could also be potently activated by YAP ( Fig. 1A )."].
  TEAD1-specific evidence is ChIP, reporter, dominant-negative TEAD1-deltaC and the TEAD1 fusion experiments.
- TAZ: all four TEADs co-purify with TAZ [PMID:19324877 "Notably, all four TEAD family members, TEAD1, TEAD2, TEAD3, and TEAD4, were identified with high scores."];
  TEAD1 activated by TAZ separately; TEAD3/4 more potently than TEAD1/2. The CTGF-promoter dominant
  negative is TEAD1-deltaC [PMID:19324877 "TEAD1 ΔC functions as a dominant negative probably by competing with endogenous TEAD for binding to target gene promoters."].
- Structure (YAP 50-171 with TEAD1 194-411, PDB 3KYS): [PMID:20123905 "YAP and TEAD form a heterodimer"];
  Y406 is the key TEAD1 residue [PMID:20123905 "The ability of Y406A and Y406H to be activated by YAP was abolished in both Gal4-TEAD1 and CTGF reporter assays"].
- Cofactors: VGLL4 [PMID:15140898 "Like other Vgl factors, Vgl-4 physically interacts with TEF-1 in an immunoprecipitation assay."];
  fly Vestigial [PMID:9869635 "In vitro, Vg binds directly to both Sd and its human homolog, Transcription Enhancer Factor-1."].
- miR-222 promoter in gastric cancer cells (TEAD1-specific siRNA + ChIP):
  [PMID:26045994 "ChIP results revealed that TEAD1 factually binds to Site A and Site B within the potential miR-222 promoter ( Figure 4D )."].
- PTM: AARS1 lactylates TEAD1 K108 [PMID:38512451 "directly catalyzed lactylation of YAP at K90 and TEAD1 at K108"].

## GO-CAM

`gocams/index.tsv` has TEAD1 in two human models: 6690711d00001771 (AARS1 mediates
lactylation of YAP1 and TEAD1, promoting activation of Hippo signaling) and
6690711d00001806 (SIRT1 delactylation). In both, TEAD1 is typed as GO:0003700
DNA-binding transcription factor activity, part of GO:0035329 hippo signaling, in
GO:0005634 nucleus. Consistent with the core functions chosen here.

## Ancestral vs animal-specific

- **Ancestral, pre-Holozoa:** TEA-domain DNA-binding TF activity. TEAD family members exist in
  fungi [PMID:38729842 "TEAD family members were identified in Drosophila, the filamentous fungus A. nidulans, and S. cerevisiae (Figure 2), and were found to regulate wing development, [37], sporulation [38], and pseudohyphal growth [39], respectively."].
  The PAINT IBA node PTN000216669 includes yeast TEC1 (SGD:S000000287) among donors, consistent with this.
- **Ancestral, Holozoa:** docking of a Yorkie-type coactivator. Holozoan Sd/TEAD homologs keep the YAP-binding tyrosine
  [PMID:22832104 "Indeed, these holozoan species contain homologues of Sd/TEAD with the C-terminal Y460 residue known to be important for YAP-TEAD interaction"];
  Capsaspora Co-Sd and Co-Yki co-IP and co-activate a Hippo-responsive reporter in fly cells
  [PMID:22832104 "epitope-tagged Co-Sd and Co-Yki immunoprecipitated with each other in Drosophila S2R+ cells (Figure 4A), demonstrating their ability to form a protein complex."];
  [PMID:22832104 "co-expression of Co-Sd and Co-Yki stimulated the transcription of the HRE-luciferase reporter in Drosophila S2R+ cells"].
  In Capsaspora itself, hyperactive coYki phenotypes need the TEAD-binding residue
  [PMID:38517944 "We found that, in contrast to coYki 4SA, the expression of a coYki 4SA F123A mutant did not affect cell or aggregate morphology (Figure 7)."]
  (indirect: coSd was not perturbed). A VGLL4/Tgi ortholog is also in Capsaspora
  [PMID:38729842 "An ortholog of the transcriptional corepressor Tgi/VGLL4, which interacts with Sd/TEAD and maintains Hippo pathway target genes in a state of default repression, is also present in the Capsaspora genome [7, 55] (Figure 2)."].
  The review frames TEAD as predating Yorkie, with Yorkie joining the two modules
  [PMID:38729842 "The fact that Sd/TEAD apparently predates Yorkie in evolutionary history suggests a model in which the Hippo-Warts kinase module and a TEAD transcription factor functioned in unlinked signaling modules"].
- **Choanoflagellates:** PMID:38729842 does not report TEAD experiments in choanoflagellates; it notes that
  their Yorkie TEAD-binding helices are poorly conserved and
  [PMID:38729842 "The degree to which choanoflagellate Yorkie orthologs interact with Sd/TEAD proteins is therefore currently unclear"].
- **Animal-specific:** growth/proliferation control and organ development. In Capsaspora,
  [PMID:38729842 "Targeted deletion of coYki does not affect cell proliferation under any condition examined [46]"],
  so the proliferation output of YAP/TAZ-TEAD is not evidently ancestral. Embryonic organ development
  (IBA on PTN000931329) and cardiac/muscle roles are animal recruitments.

## Decisions summary

- ACCEPT: DNA-binding TF activity rows (IBA/ISA/IDA/IMP/IEA), cis-regulatory DNA binding, activator activity,
  hippo signaling (all 5 rows; GO convention places the TEAD effectors here), TEAD-YAP complex, nucleus/nucleoplasm/chromatin,
  transcription regulator complex, positive regulation of transcription.
- MODIFY: DNA binding (TAS) -> GO:0000978; positive regulation of cell growth -> GO:0008284 (assays measure cell number);
  protein binding with YAP1/WWTR1/Vg -> GO:0001223 transcription coactivator binding; with VGLL4 -> GO:0001221.
- REMOVE: protein binding with RAD51 (2 BioPlex rows) and PFKM-only row (uninformative).
- KEEP_AS_NON_CORE: embryonic organ development (IBA), positive regulation of miRNA transcription.
- MARK_AS_OVER_ANNOTATED: protein-containing complex assembly (IMP).
- PMID:28473536 (methyl-SELEX): cached text has no TEAD1 result; accepted, deferring to the curator.
