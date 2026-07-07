# SLC22A5 (OCTN2, O76082) — review notes

## Summary of gene function
SLC22A5 / OCTN2 is a plasma-membrane, sodium-dependent, high-affinity L-carnitine
transporter of the SLC22 (MFS, TC 2.A.1.19) family. It couples Na+ symport to carnitine
uptake (1 Na+ : 1 carnitine), Km ~4–20 µM for (R)-carnitine [file UniProt CATALYTIC
ACTIVITY RHEA:72091; PMID:9685390 "Km value of 4.34 microM"; PMID:10966938 "K(m)) of
4.8 +/- 0.3 microM for L-carnitine"]. It also transports organic cations (e.g. TEA)
in a Na+-independent, lower-affinity manner [PMID:10454528 "OCTN2 transports organic
cations without involving Na(+), but it transports carnitine only in the presence of
Na(+)"]. Carnitine uptake feeds the mitochondrial carnitine shuttle (CPT1/CACT/CPT2)
for long-chain fatty-acid beta-oxidation, and OCTN2 drives renal tubular carnitine
reabsorption (>95% of filtered carnitine) [PMID:17274673].

## Core function
- MF: carnitine transmembrane transporter activity (GO:0015226); also
  (R)-carnitine transmembrane transporter activity (GO:1901235); Na+-coupled symport.
- BP: carnitine transmembrane transport (GO:1902603) / (R)-carnitine transmembrane
  transport; renal reabsorption; carnitine import feeding fatty-acid oxidation.
- CC: plasma membrane (GO:0005886), apical/brush-border in epithelia (GO:0016324,
  GO:0031526); basal membrane in Sertoli cells (GO:0009925).

## Disease
Loss-of-function biallelic variants cause Systemic Primary Carnitine Deficiency
(CDSP / CUD, MIM 212140, MONDO:0008919): hypoketotic hypoglycemia + acute metabolic
decompensation in infancy, and cardiomyopathy / skeletal myopathy; treatable with
oral L-carnitine [PMID:9916797 "loss of OCTN2 function causes SCD"; dismech
Primary_Carnitine_Deficiency.yaml].

## Substrate breadth (polyspecific / secondary activities — genuine but non-core)
- Betaine (glycine betaine) [PMID:10966938 "hOCTN2 mediated transport of betaine"];
  dimethylglycine [file UniProt RHEA:76591; PMID:33124720 "Dimethylglycine, known to
  interact with SLC22A5"].
- Acyl-carnitines: acetyl-, propionyl-, butyryl- [PMID:17855766 butyryl-L-carnitine
  via OCTN2, high-affinity].
- Organic cations / drugs (TEA, quinidine, verapamil, cimetidine, many DrugBank
  substrates) — Na+-independent, lower affinity.
- Bacterial quorum-sensing pentapeptide CSF (competence & sporulation factor) uptake
  in intestinal epithelia [PMID:18005709].

## Localization
- Plasma membrane (multipass) [file UniProt SUBCELLULAR LOCATION Cell membrane].
- Apical / brush-border in kidney proximal tubule, intestine, placenta, cornea/conjunctiva
  [PMID:15238359 placental BBM; PMID:17274673 Caki-1 apical; PMID:18641280 ocular apical].
- Basal membrane of Sertoli cells at blood-testis barrier [PMID:35307651].
- Isoform 3 (OCTN2VT) retained in ER, non-functional [PMID:17509700].
- Extracellular exosome (urinary) — HDA proteomics, incidental [PMID:19056867].
- Cytosol/cytoplasm ISS annotations (from mouse O70594) — not a functional location;
  the transporter is an integral membrane protein.

## Regulation / partners
- PDZK1 binds OCTN2 C-terminus (last 4 aa) and stimulates carnitine transport capacity
  ~6-fold [PMID:15523054]. This is the informative interaction; bare protein-binding IPIs
  (HMGCS1, keratins, KRTAP6-3, MTUS2, NOTCH2NLC from HT interactome screens) are
  uninformative.
- Intestinal expression induced by IFN-γ and TNF-α [PMID:20722056].
- Carnitine transport stimulated by membrane cholesterol [PMID:33334877].

## Annotations to treat cautiously
- GO:0005524 ATP binding (IEA, InterPro IPR045915) & KW Nucleotide-binding: OCTN2 is a
  secondary active (Na+-symport) MFS transporter, NOT an ATP-driven pump. This IEA is a
  spurious InterPro→GO mapping; MARK_AS_OVER_ANNOTATED / effectively wrong.
- GO:0005737 cytoplasm, GO:0005829 cytosol (ISS from O70594): mislocalization; integral
  membrane protein. Over-annotation.
- GO:0150104 transport across blood-brain barrier: OCTN2 is at the BBB and takes up
  carnitine there [PMID:23877104 IMP], but the NAS refs (26590417, 30280653) are generic
  BBB reviews — keep MF/IMP, the review NAS are weak.
- GO:0034341 / GO:0034612 (response to IFN-γ / TNF): these are gene-expression/regulation
  responses (OCTN2 is induced), non-core.
- GO:0009609 response to symbiotic bacterium & GO:0060731 positive regulation of
  intestinal epithelial structure maintenance (PMID:18005709 IMP): downstream biology of
  CSF uptake, non-core.
- PMID:23567998 (gabapentin/LAT1) IDA for GO:0015651/GO:0015697: abstract is about LAT1;
  cannot verify OCTN2 quaternary-ammonium assay from cache → UNDECIDED (defer to curator).

## Deep research
`just deep-research-falcon` failed (script TypeError: `dict | None` under the runtime
python); no falcon DR file generated. Grounded review in UniProt record, GOA, cached
publications/PMID_*.md, and dismech Primary_Carnitine_Deficiency.yaml. Did NOT fabricate
a -deep-research-*.md.
