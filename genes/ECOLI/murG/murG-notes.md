# murG (P17443) curation notes

Escherichia coli K-12 MurG (b0090, JW0088), 355 aa, glycosyltransferase family 28
(GT-B fold), MurG subfamily (HAMAP MF_00033, NCBIfam TIGR01133, CAZy GT28).

No deep-research file was generated for this gene; these notes were compiled
manually from the cached publications and the UniProt record. FEBA fitness data
could not be fetched (no FEBA data source reachable); murG is in any case
essential.

## Function

- MurG catalyses the last intracellular step of peptidoglycan subunit assembly:
  transfer of GlcNAc from UDP-GlcNAc to lipid I
  (undecaprenyl-PP-MurNAc-pentapeptide) to give lipid II
  [PMID:1649817 "In vitro assays for phospho-MurNAc-pentapeptide translocase and N-acetylglucosaminyl transferase activities finally confirm the identification of the murG gene product as the transferase that catalyzes the conversion of lipid intermediate I to lipid intermediate II in the peptidoglycan synthesis pathway."].
- Depletion rapidly blocks peptidoglycan synthesis with accumulation of
  UDP-GlcNAc, UDP-MurNAc-pentapeptide and lipid I [PMID:1649817 "The inactivation of the murG gene rapidly inhibits peptidoglycan synthesis in exponentially growing cells."].
- Purified (His-tagged) MurG is active and complements in vivo; ramoplanin
  inhibits it [PMID:10338150 "The enzymatic activity of each purified MurG protein was determined and found to be inhibited to the same extent by ramoplanin."].
- Crystal structures: apo 1.9 A [PMID:10892798] and with UDP-GlcNAc 2.5 A
  [PMID:12538870 "MurG is an essential glycosyltransferase that forms the glycosidic linkage between N-acetyl muramyl pentapeptide and N-acetyl glucosamine in the biosynthesis of the bacterial cell wall."].
  The N-terminal domain binds the acceptor and probably the membrane
  [PMID:10892798 "Structural analysis suggests that the C-terminal domain contains the UDP-GlcNAc binding site while the N-terminal domain contains the acceptor binding site and likely membrane association site."].
  UniProt records kinetic constants (Km 0.053 mM for lipid I and UDP-GlcNAc,
  kcat 837 min-1) and mutagenesis of T15, H18, N127, S191, Q288 (PMID:12538870).

## Substrate specificity and GO term choice

E. coli lipid I carries meso-diaminopimelate (meso-DAP) at position 3 of the stem
peptide. GO splits the reaction into two sibling terms (both direct children of
GO:0008375 acetylglucosaminyltransferase activity; neither is_a the other):

- GO:0050511 "undecaprenyldiphospho-muramoylpentapeptide
  beta-N-acetylglucosaminyltransferase activity": definition specifies the
  **L-Lys** stem peptide (Gram-positive type, EC 2.4.1.227 as written in GO).
- GO:0051991 (meso-DAP stem peptide; RHEA:31227), which is the reaction UniProt
  records for E. coli MurG.

So the E. coli-appropriate term is GO:0051991. The GO:0050511 rows (IBA, UniRule
IEA, EcoliWiki IDA, EcoCyc IMP) are essentially right but on the Lys-type sibling;
they are MODIFY to GO:0051991, not REMOVE. The PAINT node PTN000470572 spans
DAP- and Lys-type bacteria; there is no single GO term covering MurG activity
irrespective of the stem-peptide residue, which is a GO structure issue
(raised as a suggested question).

## Location

- Membrane-associated after fractionation [PMID:1649817 "In cell fractionation experiments, the transferase is essentially associated with membranes when it is recovered."].
- Trypsin probing of maxicell spheroplasts shows peripheral association with the
  inner (cytoplasmic) face of the inner membrane
  [PMID:8449890 "we show that this enzyme is peripherally associated with the inner face of the cytoplasmic membrane"].
- Immunofluorescence: dispersed in the envelope with enrichment at the division
  site; midcell localization needs a mature divisome, lateral localization needs
  MreCD [PMID:17640276 "MurG exhibited a random distribution in the cell envelope with a relatively higher intensity at the division site."].
- Cytoplasmic side is supported by two independent lines (protease protection,
  PMID:8449890; acceptor lipid I head group is cytoplasmic and the structure
  places the membrane-association site in the acceptor domain, PMID:10892798),
  so a NEW GO:0009898 cytoplasmic side of plasma membrane row is added beside
  the accepted plasma membrane rows.

## Interactions

- Co-immunoprecipitation with MreB and MraY [PMID:17640276 "Investigating this by immunoprecipitation revealed the association of MurG with MreB and MraY in the same protein complex."].
- High-throughput interactions with YfiF (TAP, PMID:15690043; Y2H, PMID:24561554)
  and with YhcB/ZapG (B2H, PMID:27335665, PMID:33895137). None defines a MurG
  molecular function; all GO:0005515 rows are REMOVE under the protein-binding
  policy.

## Keyword process terms

The current GOA set for P17443 has no UniProt-keyword "cell division" or
"regulation of cell shape" IEA rows, so nothing to judge there. MurG supplies
lipid II to both the elongasome and the divisome, but it does not itself
regulate cell shape or execute division; such terms should not be added.

## Module consistency

modules/peptidoglycan_precursor_biosynthesis.yaml (murG_activity annoton) uses
GO:0050511 with P17443 as representative. For E. coli (meso-DAP) the specific
term is GO:0051991; the module should either use GO:0051991 for the DAP-type
members or note that GO:0050511 is the Lys-type sibling.
