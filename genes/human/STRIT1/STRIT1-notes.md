# STRIT1 (DWORF) review notes

## 2026-09-30 — initial review (claude-code, MICROPROTEINS project)

### Identity
- UniProt P0DN84 (DWORF_HUMAN), 35 aa, PE1. Single C-terminal TM helix (14-34), NMR
  structure 7MPA. HGNC name "small transmembrane regulator of ion transport 1". HPA:
  group-enriched in skeletal muscle and tongue.
- Encoded by a transcript previously annotated as lncRNA LOC100507537
  [PMID:26816378 "The Dworf RNA transcript is annotated as NONCODE lncRNA gene NONMMUG026737 (12) in mice and lncRNA LOC100507537 in the University of California, Santa Cruz, human genome"].
- Mouse ortholog P0DN83 (34 aa). "Unless otherwise noted, further studies focused on the
  murine homolog of DWORF" [PMID:26816378].
- Belongs with PLN, SLN, MRLN (myoregulin), ERLN, ALN (another-regulin) to the "regulin"
  SERCA-regulatory micropeptides [PMID:28436536 "Phospholamban, sarcolipin and myoregulin inhibit SERCA, while DWORF stimulates it by displacing these inhibitory proteins"].

### Function — the discovery paper (mouse)
- [PMID:26816378 "Based on gain- and loss-of-function studies, our results demonstrate that DWORF enhances SR Ca2+ uptake and myocyte contractility through its displacement of the inhibitory peptides PLN, SLN, and MLN from SERCA (Fig. 4C)."]
- Co-IP with all SERCA isoforms (COS7); binding of PLN/SLN/MLN to SERCA reduced by DWORF.
- In COS7 with SERCA2a, DWORF alone did not change Ca affinity: [PMID:26816378 "These results indicate that DWORF counteracts the effect of inhibitory peptides rather than directly stimulating SERCA pump activity"]. Repeated in the DCM mouse paper [PMID:30299255 "Cells expressing SERCA2a and DWORF in the absence of PLN do not exhibit enhanced SERCA activity (purple), indicating that DWORF exerts its’ stimulatory effect on SERCA through the displacement of PLN."].
- KO soleus: decreased SERCA Ca affinity; slowed post-tetanic relaxation [PMID:26816378 "however, at tetanus-inducing frequencies, relaxation rates were significantly slowed in Dworf KO muscles after tetanus (Fig. 3F)."].
- Localization: GFP-DWORF in SR-like striations in FDB fibres, ER in COS7.
- Human data in that paper is only expression: [PMID:26816378 "DWORF mRNA was also down-regulated in ischemic failing human hearts"].

### Human experimental function evidence (not captured in GOA!)
- Li et al. 2021 JBC used the **human** DWORF and human SERCA2a in HEK293 cells:
  [PMID:33581112 "The tagRFP (hereafter “RFP”) gene was similarly fused to the N terminus of the human DWORF or PLB gene."]
  - Ca-ATPase assays: [PMID:33581112 "We observed that DWORF activates SERCA2a directly, in the absence of PLB, by enhancing the Ca-ATPase apparent calcium affinity"]
  - Dual mechanism: [PMID:33581112 "In our model, DWORF binds to SERCA2a, displacing PLB, and activates SERCA via two distinct mechanisms"]
  - Mutagenesis: [PMID:33581112 "Using site-directed mutagenesis, we identified two DWORF residues, P15 and W22 (in the human isoform), as essential for activation of SERCA2a."]
- Fisher et al. 2021 eLife: purified recombinant human DWORF co-reconstituted with rabbit
  SERCA1a increases turnover [PMID:34075877 "Recombinant human DWORF was expressed as a maltose-binding protein (MBP) fusion with a TEV cleavage site for removal of MBP."; "Here, we show that DWORF is a direct activator of SERCA, increasing its turnover rate in the absence of phospholamban."]
- Phillips et al. 2023: human sequences, FRET; homo- and hetero-oligomers with PLN, SLN,
  ALN, ELN [PMID:36523160 "human sequences of all micropeptides (PLB, SLN, DWORF, ALN, and ELN) were labeled"].
- Cleary et al. 2022: DWORF binds E1P/E2P states preferentially [PMID:35605666]; Bovo 2024:
  PLN phosphorylation promotes DWORF activation in HEK293 with human SERCA2a [PMID:38823350].
- Fisher 2025: Leu12/Pro15 required; P15 substitutions turn DWORF into an inhibitor [PMID:40910871].
- So: the "direct activation" question is disputed between labs (Olson: displacement only;
  Thomas/Young/Robia: direct activation plus displacement). Both mechanisms give net SERCA
  activation, so an activator-of-transporter MF holds regardless.

### GOA assessment
- Human GOA: 45 IPI protein binding, all from HuRI Y2H (PMID:32296183). None of the 45
  partners is SERCA or a regulin; nearly all are membrane proteins (aquaporins, tetraspanins,
  SLCs, GPCRs, syntaxins, BSCL2) — the typical sticky-TM-helix pattern of Y2H. REMOVE all
  (uninformative; not claiming false).
- Function rows (enzyme activator activity, regulation of ATPase-coupled Ca transporter
  activity, positive regulation of Ca import into SR, regulation of slow-twitch contraction,
  SR membrane) are all ISS from mouse P0DN83 (whose own annotations are IDA/IMP from
  PMID:26816378/30299255). The human IDA-grade evidence (PMID:33581112, 34075877) was never
  used by GO curators — UniProt uses it in the FUNCTION comment (ECO:0000269) but GO rows remain ISS.
- MF refinement: GO:0008047 enzyme activator activity -> GO:0001671 ATPase activator
  activity and GO:0141109 transporter activator activity. Comparator: human PLN has
  GO:0042030 ATPase inhibitor activity (IDA) and GO:0141110 transporter inhibitor activity
  (IDA PMID:19708671); mouse Pln GO-CAM 62f58d8800005094 uses ATPase inhibitor activity.
  DWORF is the mirror-image regulin, so the activator counterparts are the matched terms.
- GO-CAM: no model in gocams/index.tsv contains STRIT1/P0DN84 (or mouse Dworf). Only a mouse
  Pln model (62f58d8800005094) covers SERCA regulation.
- No PAN-GO/IBA annotations (UniProt: "0 GO annotations based on evolutionary models").

### Open issues
- Is DWORF protein present in human heart? The mouse antibody does not recognize human DWORF
  [PMID:35605666 "did not react with human DWORF"]; human protein-level detection in tissue
  is limited.
