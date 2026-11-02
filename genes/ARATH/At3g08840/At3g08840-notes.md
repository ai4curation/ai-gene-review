# At3g08840 (A0A1I9LPE3) review notes

Deep research via `just deep-research-falcon` was not available in this session (auth
failure), so the literature survey below was done manually with PubMed searches
(2026-10-19). No `-deep-research-*.md` file was created.

Context: projects/RAR_MISANNOTATION.md (re-examination of Wei et al. 2020,
[PMID:32470107 "we applied the approach to 20 commonly studied species in two
recent UniProt-GOA releases and identified 250 potential misannotations"]). Wei et al.
flagged the IBA `GO:0009252 peptidoglycan biosynthetic process` on this protein; that row
is no longer in GOA. The MF IBA `GO:0008716 D-alanine-D-alanine ligase activity`
(PTN000566166; donors E. coli DdlB P07862, DdlA P0A6J8, M. tuberculosis Ddl P9WP31) remains.

## Identity

- 949 aa TrEMBL entry, "D-alanine-D-alanine ligase family"; two tandem Ddl modules
  (Pfam Dala_Dala_lig_N PF01820 x2, Dala_Dala_lig_C PF07478 x2; two ATP-grasp domains
  223-452 and 672-925); PANTHER PTHR23132:SF0. PROSITE PS00843 and PS00844 (D-Ala-D-Ala
  ligase signatures) both match (file:ARATH/At3g08840/At3g08840-uniprot.txt).
- Called At-DDL in the moss literature. The fused two-module architecture is shared with
  moss and Selaginella DDL [PMID:27325639 "DDL genes with two Ddl regions each encoding the
  Ddl_N and ATP-grasp_4 domains are also found in the genomes of many sequenced plants,
  including the spikemoss S . moellendorffii ( XP_002983726 ) ( Banks et al., 2011 ) and
  Arabidopsis (At3g08840)"].
- Note: Machida et al. 2006 abstract says Arabidopsis has "two genes for D-Ala-D-Ala ligase
  (Ddl)" [PMID:16618924 "the genome of Arabidopsis thaliana contains five genes that are
  essential for peptidoglycan synthesis, MurE, MurG, two genes for D-Ala-D-Ala ligase (Ddl),
  and the gene for translocase I (MraY)"]. Later work treats At3g08840 as the single fused
  DDL gene (the two "genes" were probably the two halves/ two models); Hirano et al. 2016
  analysed one locus.

## Localization

- Chloroplast stroma by MS proteomics (Zybailov 2008, HDA row). Hirano et al. restate this:
  [PMID:27325639 "Although according to mass spectrometry analyses, At-DDL localizes to the
  stroma of chloroplasts ( Zybailov et al., 2008 )"].
- Moss DDL transit peptide-GFP is plastidial [PMID:27325639 "Polyethylene glycol ( PEG
  )-mediated transformation using these plasmids resulted in GFP fluorescence in the
  chloroplasts of P . patens , corroborating the plastid localization prediction"].
- The ISM `cytoplasm` (AtSubP) row is a prediction; chloroplast is technically part of
  cytoplasm in GO but the specific supported location is chloroplast stroma.

## Function: what is and is not known

- Moss ortholog: genuine D-Ala:D-Ala ligase in plastid peptidoglycan synthesis needed for
  plastid division. Knockout -> macrochloroplasts; D-Ala accumulates; rescued by
  D-Ala-D-Ala but not LA-LA, DA-LA, LA-DA or D-Ala [PMID:27325639 "These results confirm
  that Pp-DDL functions as a d -Ala: d -Ala ligase."]; EDA-DA labelling shows a
  peptidoglycan layer around moss chloroplasts.
- Arabidopsis: two T-DNA lines (SALK_092419 At-ddl-1, SAIL_906_E06 At-ddl-2) lack
  transcript but have no chloroplast morphology defect [PMID:27325639 "we observed no
  defects in chloroplast morphology in either of two T-DNA-tagged lines ( Figure 5 ),
  confirming that DDL is not involved in plastid division in Arabidopsis"].
- Activity not tested [PMID:27325639 "The d -Ala: d -Ala ligase activity of At-DDL also
  remains unconfirmed."]. Authors suggest possible change of function, as for AtMurE
  [PMID:27325639 "Similarly, it is possible that the function of DDL may have changed in
  Arabidopsis."].
- No Pbp in Arabidopsis [PMID:16618924 "no Pbp gene was found in A.
  thaliana"]; angiosperms generally retain only MurE, Ddl, MraY, MurG
  [PMID:41351887 "Generally, many angiosperm genomes, including Arabidopsis, have only MurE,
  Ddl, MraY, and MurG genes, which may have been repurposed by exaptation."].
  Sugita et al. 2025 speculate AtDdl acts in D-amino acid metabolism [PMID:41351887 "but this gene may be involved in d‐amino acid metabolism"].
- Precedent for repurposing: AtMurE is required for chloroplast biogenesis/PEP-dependent
  transcription, not division, and does not complement moss murE [PMID:18036201 "These
  results suggest that AtMurE is functionally divergent from the bacterial and moss MurE
  proteins."]. Interesting counterpoint: gymnosperm MurE (Larix) rescues the Arabidopsis
  murE albino phenotype [PMID:28158764 "the expression of LgMurE cDNA completely rescued
  the albefaction defects in A. thaliana but did not rescue the macrochloroplast phenotype
  in P. patens"], and spruce MurE has bona fide MurE enzymatic activity and also rescues
  the Arabidopsis mutant [PMID:41351887 "Enzymatic assay of recombinant PaMurE proteins
  revealed they catalyze the same reaction performed by their bacterial MurE homologs."].
  That is, an enzymatically active MurE can fulfil the Arabidopsis "repurposed" role -
  so loss of the division role does not imply loss of the ancestral catalytic activity.
  By analogy, At-DDL may retain ligase activity while the downstream pathway is gone.
- Review of plastid PG evolution: loss happened independently several times
  [PMID:19647785 "we propose that the loss of peptidoglycan occurred independently at least
  three times during plant evolution"].
- D-Ala-D-Ala dipeptide occurs in seed plants (tobacco) [PMID:27325639 "The functions of DDL
  and d -Ala in seed plants remain unknown, although this dipeptide was detected in
  Nicotiana tabacum and Phalaris tuberosa as early as the 1970s"].

PubMed searches with no additional Arabidopsis DDL-specific primary literature:
"Arabidopsis D-alanine D-alanine ligase" (0 hits); "(D-Ala-D-Ala OR D-alanyl-D-alanine) AND
(plant OR Arabidopsis OR chloroplast)" (only moss/bacterial/irrelevant hits);
"plastid peptidoglycan Arabidopsis MurE ..." (7 hits, all cited above).

## Bioinformatics

See At3g08840-bioinformatics/RESULTS.md. Summary: C-terminal module carries both PROSITE
Ddl signatures, active-site Glu and all three Mg2+ ligands of E. coli DdlB; the N-terminal
module has a diverged Mg2+-binding loop. The same pattern (including a Ser150->Cys in
module 2) is present in the moss DDL, whose ligase function is genetically supported, so
there is no Arabidopsis-specific loss of catalytic residues.

## Verdicts

- Wei et al. BP flag (peptidoglycan biosynthetic process): conclusion holds for
  Arabidopsis (no Pbp; no plastid phenotype; pathway incomplete), though their stated
  reason (plant walls are cellulose) is wrong - the relevant compartment is the plastid,
  and the IBA node is correct for bryophytes/lycophytes/gymnosperms.
- MF IBA D-Ala-D-Ala ligase: node placement defensible (target inside the plant DDL clade;
  moss member functionally supported); no target-specific evidence of catalytic loss.
  Accept, flagging that it is biochemically untested in Arabidopsis.
