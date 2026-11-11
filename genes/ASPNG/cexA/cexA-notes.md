# cexA (CexA, citrate exporter A) — Aspergillus niger — review notes

UniProtKB:A0A254TZW7 (CEXA_ASPNG; strain ATCC 64974 / N402 genome entry, NCBITaxon:5061).
A second Swiss-Prot entry, UniProtKB:G3Y4N5 (CEXA_ASPNA, strain ATCC 1015,
NCBITaxon:380704), carries the identical 524-aa sequence (checked by comparing the
SQ blocks of the two cached UniProt files: zero differences). Both are reviewed in
parallel; see `genes/ASPNA/cexA/`.

No deep-research provider was available; these notes are my own literature review
from cached publications (all PMIDs below are cached in `publications/`).

## Identity and nomenclature

- Gene identifiers: CBS 513.88 An17g01710; ATCC 1015 protein ID 1165828
  (ASPNIDRAFT2_1165828). [PMID:31062025 "with ATCC 1015 protein IDs 1165828 (A. niger CBS 513.88: An17g01710, A. niger NRRL3: 06350)"]
- Named "CitT" by Odoni et al. in a preprint, then renamed CexA following Steiger et al.
  [PMID:31062025 "Therefore, adhering to the nomenclature given by (Steiger et al. 2019), we refer to this transporter protein as CexA."]
- Citation check of the brief: the Odoni et al. 2019 paper is FEMS Microbiology
  Letters 366:fnz071 (PMID:31062025), not Nat Commun or mBio. Steiger et al. 2019 is
  Metabolic Engineering 52:224-231 (PMID:30553933). Both verified against the cached
  PubMed records.

## Function

- Major facilitator superfamily, DHA1 subfamily membrane transporter, 12 predicted TM
  helices (UniProt FT TRANSMEM, ECO:0000255).
  [PMID:30553933 "The encoding homologous protein CexA belongs to the major facilitator superfamily subclass DHA1 and members of this family work as drug-H+ antiporter."]
- Gene disruption abolishes citrate secretion in A. niger; heterologous expression in
  S. cerevisiae causes citrate secretion; overexpression raises citrate titres.
  [PMID:30553933 "The disruption of this gene completely abolishes citric acid secretion, which indicates that this protein is the main citric acid transporter in A. niger."]
  [PMID:30553933 "The gene can be heterologously expressed in Saccharomyces cerevisiae, which leads to the secretion of citric acid during the growth on glucose."]
- Independent identification by comparative transcriptomics, confirmed by yeast expression.
  [PMID:31062025 "we found accumulation of citrate in the extracellular medium in S. cerevisiae when heterologous gene expression was induced (Fig. 3)"]
- Deletion in N402 background: citrate export almost abolished, oxalate more than doubles, glyoxylate shunt activated; citrate uptake unaffected.
  [PMID:34071072 "The citT knock-out almost completely abolished citrate export under otherwise citrate promoting conditions."]
  [PMID:34071072 "We show that the citT gene is responsible for active A. niger citrate export, but not for citrate uptake."]
- Energetics and specificity (S. cerevisiae expression, 14C-citrate): low-affinity
  import also measurable (Km 43.7 mM at pH 5.5), proton-motive-force independent,
  consistent with facilitated diffusion; only tricarboxylates (citrate, isocitrate)
  compete. GFP fusion localises to the plasma membrane.
  [PMID:37216016 "Citrate uptake was independent of the proton motive force and compatible with a facilitated diffusion mechanism."]
  [PMID:37216016 "Citric and isocitric acids, but not monocarboxylic (acetate, lactate) or dicarboxylic acids (succinate, malate, α-ketoglutarate), were able to inhibit the uptake of labelled citric acid, suggesting that only tricarboxylates are able to bind to CexA"]
  [PMID:37216016 "We also determined protein subcellular localization by GFP tagging, with seven amino acid substitutions affecting CexA protein expression at the plasma membrane."]
  So although the family name is "drug-H+ antiporter", there is no evidence for H+
  coupling for CexA; GO:0071913 (citrate *secondary active* transmembrane transporter
  activity) should NOT be used. The general GO:0015137 is the right MF.
- Regulation: Mn(II) represses cexA transcription; Mn deficiency (and intracellular
  citrate/acetyl-CoA accumulation) induces it.
  [PMID:38076415 "manganese(II) ions suppress transcription of the citrate exporter cexA in Aspergillus niger, causing citric acid secretion to decrease."]
  [PMID:39377610 "Mn2+ deficiency also triggers upregulation of the cexA gene, which encodes the citrate exporter."]
- The Yarrowia lipolytica exporter Cex1 (UniProtKB:Q6C8F0) complements an A. niger
  citrate export-deficient strain (abstract only).
  [PMID:32990722 "Likewise, expression of YALI0D20196p complemented the ability to secrete citrate in an export-deficient strain of Aspergillus niger, confirming a citrate export function of YALI0D20196p."]

## UniProt free-text issue (not a GO source defect)

The INDUCTION comment in both entries reads "Expression is repressed by Mg(2+) ions
and up-regulated under manganese deficiency (PubMed:38076415, PubMed:39377610)". The
cited papers concern manganese(II), not magnesium (see the PMID:38076415 quote above).
"Mg(2+)" is very probably a typo for "Mn(2+)". Not a GOA row, so recorded here rather
than in `source_defects`; worth reporting to UniProt.

## Annotation review summary

All GOA rows are consistent with the literature. Experimental rows (IDA/IMP/IGI/EXP/IC)
accepted. Broad IEA rows (membrane, transmembrane transporter activity, transmembrane
transport) MODIFY to the specific terms the gene already carries. No NEW rows: the
only extra candidate was a tricarboxylate/isocitrate term, but isocitrate was shown to
compete for binding, not to be transported.

## CMMMech grounding assessment

CMMMech grounds 33 records (~44 protein-example entries, all `supports: partial`) on
A0A254TZW7 or G3Y4N5 with a functional_role of the form "Plasma-membrane MFS citrate
exporter CexA that secretes intracellularly synthesized citric acid into the
extracellular medium, driving organic-acid acidification and metal chelation".

- The transport part is well supported (above), but it rests on laboratory
  citrate-production and heterologous-expression studies; the CMMMech records (mineral
  bioleaching / biomineralization) did not assay cexA. "partial" is the right status.
- "Driving acidification and metal chelation/mobilization" is downstream chemistry of
  secreted citric acid, not an activity of CexA. No cited CexA study measured metal
  solubilization.
- Records that invoke CexA for **oxalate** outcomes (whewellite, humboldtine,
  glushinskite, moolooite, lindbergite, "metal chelation/oxalate co-precipitation"):
  CexA is not an oxalate transporter (dicarboxylates do not compete, PMID:37216016),
  and deleting cexA *increases* oxalate secretion more than two-fold (PMID:34071072
  "resulting in a more than two-fold higher concentration of oxalate in the medium").
  Grounding oxalate-mediated mineral formation on CexA overstates the evidence; an
  oxalate-biosynthesis protein (oxaloacetate acetylhydrolase, OahA) would be a more
  direct anchor for those records.
- **Manganese** records (birnessite, hausmannite, manganese-ore, falottaite...): Mn(II)
  represses cexA transcription (PMID:38076415), so in Mn-releasing leach systems CexA
  activity and citrate output may be suppressed. The records should not assume
  CexA-driven citrate secretion under Mn-sufficient conditions.
- Locus note: CMMMech annotation_notes for G3Y4N5 give "locus ASPNIDRAFT_56962"; the
  UniProt entry lists ORF names ASPNIDRAFT2_1165828 and ASPNIDRAFT_57285 (and an EMBL
  EHA22412.1 gene model flagged as erroneous). ASPNIDRAFT_56962 does not appear in the
  entry; the CMMMech locus should be checked.
