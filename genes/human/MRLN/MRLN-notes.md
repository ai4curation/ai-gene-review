# MRLN (myoregulin, P0DMT0) — curation notes

## 2026-09-30 — initial review (claude-code)

### Identity
- 46-aa single-pass (type II; N-terminus cytosolic, 3 C-terminal residues lumenal) transmembrane
  micropeptide encoded in exon 3 of a transcript previously annotated as a lncRNA (LINC00948 in human).
  [PMID:25640239 "we identified a vertebrate RNA transcript annotated as a lncRNA (LINC00948 in humans and AK009351 in mice)"]
  [PMID:25640239 "a highly conserved 46 amino acid micropeptide, which we named myoregulin (MLN)"]
- Human vs mouse sequence (UniProt FASTA, fetched 2026-09-30):
  - human P0DMT0 `MTGKNWILISTTTPKSLEDEIVGRLLKILFVIFVDLISIIYVVITS`
  - mouse Q9CV60 `MSGKSWVLISTTSPQSLEDEILGRLLKILFVLFVDLMSIMYVVITS`
  - The SERCA-binding hydrophobic motif residues mutated in mouse (L29, F30, F33) and the
    unusual TM Asp35 and Lys27 are all conserved in human. ISS transfer is well justified.
- UniProt: TCDB 1.A.50.3.1 (phospholamban family); InterPro IPR049526; PAN-GO: 0 annotations
  (no PANTHER family/IBA coverage).
- HPA: tissue enhanced in skeletal muscle and tongue.

### Function (mostly mouse / heterologous)
- Co-localises with SERCA1 in SR of adult mouse muscle (GFP-MLN electroporation), SR/ER fraction
  in C2C12. [PMID:25640239 "The GFP-MLN fusion protein localized in a repeating pattern that alternated with the myosin A band and overlapped with the localization of an mCherry-SERCA1 fusion protein within the SR"]
- Co-IP with SERCA1, SERCA2a, SERCA2b; L29A/F30A/F33A abolish binding.
  [PMID:25640239 "the HA-MLN fusion protein formed a stable complex with SERCA1 (skeletal muscle-specific), SERCA2a (cardiac and slow skeletal muscle-specific) and SERCA2b (ubiquitous) isoforms"]
- Ca-ATPase assay in HEK293 homogenates: increased KCa, no Vmax change.
  [PMID:25640239 "Similar to the effects of PLN and SLN, expression of MLN caused a significant reduction in the rate of Ca2+ uptake, measured as an increase in KCa"]
- KO mouse: increased SR Ca2+ and ~31% longer treadmill running.
  [PMID:25640239 "Genetic deletion of MLN in mice enhances Ca(2+) handling in skeletal muscle and improves exercise performance."]
- Mechanistic discrepancy: in co-reconstituted proteoliposomes with rabbit SERCA1a and synthetic MLN
  (Young / Espinoza-Fonseca labs), MLN lowers Vmax without changing KCa.
  [PMID:34445594 "Using a membrane reconstitution system, we have found that MLN selectively alters the Vmax of SERCA with no effect on the KCa of SERCA (Figure 5B and Table 1)."]
  [PMID:37014032 "Instead, Asp35 controls SERCA inhibition by populating a bound-like orientation of MLN."]
  [PMID:37918638 "replacing Lys27 with Asn significantly enhances the inhibitory potency of MLN"]
  Species of the synthetic MLN peptide is not stated in the cached text of these papers
  (34445594 states MD models used "Full-length human MLN"). Either way, inhibition of the pump is
  consistent; only the kinetic mechanism (KCa vs Vmax) differs. UniProt's human FUNCTION text says
  "decreasing the apparent affinity of the ATPase for Ca(2+)" — this is contested by the reconstitution data.
- FRET/co-IP: homo-oligomerises but binds SERCA as a monomer.
  [PMID:31449798 "Micropeptides formed avid homo-oligomers with high-order stoichiometry"]
- Family context: MLN/PLN/SLN share the SERCA-binding motif; ALN/ELN in non-muscle cells.
  [PMID:27923914 "We note a remarkable overlap in the distribution of individual micropeptides with major SERCA isoforms (SERCA1 with MLN, SERCA2a with PLN, SERCA2b with ALN, and SERCA3 with ELN)"]
- Evolution: regulins related to FXYD; MRLN in CCDC6–SLC16A9 neighbourhood.
  [PMID:28436536 "Mammalian myoregulin is flanked by CCDC6 and SLC16A9 genes"]

### Human-cell evidence (not in GOA)
- Human DMD immortalized myotubes / myoblasts: MLN shRNA improves SR Ca2+ content; NR1D1 represses
  MLN transcription. [PMID:35917173 "Whereas MLN overexpression in healthy myotubes reduced SR calcium content (Supplemental Figure 2, I and J), shRNA against MLN improved SR calcium content in DMD immortalized myotubes (Supplemental Figure 2, K and L)."]
  [PMID:35917173 "Stable MLN silencing in immortalized DMD human myoblasts was achieved using a Dharmacon SMARTvector lentiviral shRNA delivery system"]
- Human AC16 cardiomyocyte line: MLN knockdown raises SERCA2a activity.
  [PMID:41348974 "SERCA2a activity was significantly elevated upon MLN knockdown (Figure 5A)"]
  Caveat: AC16 is a transformed hybrid line; MLN is not normally a cardiac peptide
  (PMID:25640239 reported no cardiac expression in mouse). Supports human SERCA inhibition
  by endogenous MLN, but physiological cardiac relevance is uncertain.
- Human heart mRNA and rat Langendorff (PMID:38246425, abstract only; preliminary).

### GO annotation assessment
- GOA human has 7 rows: enzyme inhibitor activity (ISS, IEA), ER membrane (IEA is_active_in),
  SR membrane (ISS, IEA), negative regulation of calcium ion import into SR (ISS).
- Mouse Q9CV60 source annotations: GO:0004857 IDA (UniProt), GO:1902081 IDA/IMP, GO:1901895 IDA
  (PMID:27923914), GO:0033017 IDA, GO:0005789 IDA, protein binding IPI.
- Comparators: human PLN (P26678) has GO:0042030 ATPase inhibitor activity (IDA+IBA) and
  GO:0141110 transporter inhibitor activity (IDA); SLN (O00631) has GO:0004857 ISS and
  GO:1901895 IDA. The mouse Pln GO-CAM (gocams 62f58d8800005094) types Pln's activity as
  GO:0042030 ATPase inhibitor activity in ER membrane.
- Ontology note: GO:0005388 P-type calcium transporter activity is NOT a descendant of
  catalytic activity / ATP hydrolysis activity in current GO (is_a transporter + ATP-dependent
  activity). So GO:0004857 "enzyme inhibitor activity" (reduces a catalytic activity) is a
  loose fit; GO:0042030 ATPase inhibitor activity is what curators use for PLN (IBA, GO-CAM)
  and is directly supported by ATPase assays. MODIFY → GO:0042030.
- GO:1901895 negative regulation of ATPase-coupled calcium transmembrane transporter activity:
  MLN performs the inhibition itself (direct binding to SERCA), passes the participation test;
  comparators PLN and SLN (same role) both carry it by IDA. Propose NEW (IMP, human AC16 data).
- GO-CAM: no model in gocams/index.tsv contains MRLN/P0DMT0 (checked 2026-09-30).
