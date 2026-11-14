# SLC7A5 (LAT1 / 4F2 light chain) — curation notes

UniProt: Q01650 (LAT1_HUMAN). HGNC: SLC7A5. 507 aa, 12 transmembrane helices (LeuT/APC fold).
Gene family: SLC7 / amino acid-polyamine-organocation (APC) superfamily; PANTHER PTHR11785:SF315.

## Core identity

LAT1 is the **catalytic light chain of a heteromeric amino-acid transporter (HAT)**. It forms a
**disulfide-linked heterodimer with the heavy chain SLC3A2 (4F2hc / CD98hc)** via an interchain
disulfide (LAT1 Cys164 ↔ SLC3A2 Cys210). SLC3A2 is required for trafficking of LAT1 to the plasma
membrane and for transport activity [PMID:30867591 "4F2hc is essential for the transport activity";
"a type II membrane glycoprotein that is essential for the stability of LAT1 and for its localization
to the plasma membrane"]. The cryo-EM structure (3.3 Å) shows LAT1 in an inward-open state with
extensive LAT1–4F2hc contacts on the extracellular side, within the membrane, and intracellularly
[PMID:30867591].

## Mechanism: obligate Na+-independent antiporter (1:1 exchange)

System L / LAT1-4F2hc is an **obligatory amino-acid exchanger with 1:1 stoichiometry**, not a
uniporter/symporter/channel [PMID:11847106 "Quantification of amino acid influx and efflux by HPLC
demonstrated an obligatory amino acid exchange with 1:1 stoichiometry"; "the two system L amino acid
transporters that are implicated in cell growth (LAT1-4F2hc) and transcellular transport (LAT2-4F2hc)
are obligatory exchangers"]. UniProt lists ~30 Rhea exchange reactions, all of the form
`X(in) + L-phenylalanine(out) = X(out) + L-phenylalanine(in)` etc. — i.e. antiport. Transport is
**Na+- and pH-independent** [PMID:30867591 "catalyses the cross-membrane flux of large neutral amino
acids in a sodium- and pH-independent manner"]. Intracellular substrate availability limits the rate;
asymmetric affinities (high outside, low/mM inside) make the intracellular pool the controller
[PMID:11847106]. Because it is an exchanger, net cellular *accumulation* of EAAs (e.g. Leu) occurs by
coupling to the outward gradient of other amino acids (e.g. Gln efflux), which is the physiological
import role.

## Substrates

Large neutral/branched-chain/aromatic L-amino acids: Leu, Ile, Val, Phe, Tyr, Trp, His, Met (and more
weakly Gln, Cys, Ser, Ala, Gly, Pro) [PMID:11557028 "hLAT1 transports large neutral amino acids with
high affinity"; UniProt CATALYTIC ACTIVITY]. Km values in the low-µM range (Leu ~19.7 µM, Phe ~14.2 µM,
Trp ~21.4 µM; UniProt BIOPHYSICOCHEMICAL PROPERTIES).
- **Thyroid hormones / iodothyronines**: T4, T3, rT3, 3,3'-T2, and iodotyrosines (MIT, DIT)
  [PMID:11564694; PMID:26305885 "The L-type amino acid transporters LAT1 and LAT2 are known to
  facilitate TH transport"]. Km T3 ~0.8 µM, T4 ~7.9 µM.
- **L-DOPA** and 3-O-methyl-L-dopa (UniProt CATALYTIC ACTIVITY; neutral AA-like aromatic).
- **Drugs / xenobiotics**: gabapentin [PMID:23567998], pregabalin [PMID:30374619], melphalan,
  BCH (inhibitor), JPH203 (LAT1-selective inhibitor). LAT1 is a BBB drug-delivery route and
  anti-cancer target.
- **Toxicant mimicry**: methylmercury-L-cysteine complex [PMID:12117417]; S-nitroso-L-cysteine
  [PMID:15769744]; Trp/kynurenine exchange cycle [PMID:17896864 "immunoregulatory tryptophan
  influx/kynurenine efflux cycle"].

## Localization

Plasma membrane (apical in placental syncytiotrophoblast; basolateral/basal in some epithelia;
microvillus membrane) [PMID:11742812; PMID:26050671]. Recruited to the **lysosomal membrane** by
LAPTM4B, where it imports leucine into lysosomes to drive **mTORC1 activation** [PMID:25998567
"LAPTM4b recruits LAT1-4F2hc to lysosomes, leading to uptake of Leu into lysosomes, and is required
for mTORC1 activation"]. HPA "cytosol" IF staining is an antibody artifact for this polytopic membrane
protein. Found in extracellular exosomes (HDA proteomics).

## Physiology / downstream roles (indirect — LAT1 supplies amino acids, does not execute these)

- **Cell growth / cancer**: overexpressed in many tumors; supplies EAAs for growth; mTORC1 signalling.
- **Immune activation**: in CD3/CD28-activated human T cells LAT1 is induced (NF-κB/AP-1) and is the
  major EAA importer; its inhibition attenuates cytokine production (IL-4, IL-17, IFN-γ) via NF-κB/NFAT
  [PMID:24038088 "L-type amino acid transporter 1 (LAT1) is a major transporter for essential amino
  acids into activated human T cells"]. These are `acts_upstream_of` regulatory annotations, not LAT1's
  own molecular activity.
- **Blood-brain barrier / placenta**: transcellular neutral-AA and thyroid-hormone and drug transport.
- **HCV (microbial infection)**: SLC3A2-SLC7A5 complex facilitates viral entry and leucine-driven
  mTORC1 [PMID:30341327].

## Curation decisions (summary)

- Core MF: obligate amino-acid **antiporter activity** (GO:0015297, IDA PMID:11847106/17896864) acting
  on large neutral L-amino acids (GO:0015175 neutral L-amino acid TTA accepted); specific substrate and
  leucine-import rows accepted; thyroid-hormone transporter activity (GO:0015349) accepted as a genuine
  secondary function. Complex modeled via `in_complex` GO:1990184 amino acid transport complex (LAT1-4F2hc).
- `GO:0005515 protein binding` IPI rows (SLC3A2 P08195; LAPTM4B Q86VI4; Q6P1M3) → REMOVE per
  protein-binding policy; the SLC3A2 and LAPTM4B partnerships are functional and captured in the
  complex rows / reasons, not as bare binding.
- Broad umbrella terms entailed by accepted specific ones → TOO_GENERAL (amino acid TTA GO:0015171;
  L-amino acid TTA GO:0015179; transmembrane transporter activity GO:0022857; amino acid transport
  GO:0006865; amino acid transmembrane transport GO:0003333; L-amino acid transport GO:0015807;
  transmembrane transport GO:0055085; L-alpha-amino acid transmembrane transport GO:1902475).
- `GO:0016020 membrane` → MODIFY → GO:0005886 plasma membrane.
- `GO:0042605 peptide antigen binding` (ISS from Q7YQK4, 2006) → REMOVE (spurious electronic mapping;
  LAT1 has no MHC/antigen-presentation function).
- `GO:0005829 cytosol` (HPA IDA) → MARK_AS_OVER_ANNOTATED (artifactual for a 12-TM membrane protein).
- Rat-ortholog Ensembl IEA organismal-response projections (response to hyperoxia/muscle activity/
  mechanical stimulus/glucose starvation/LPS; liver regeneration; glial proliferation; VSMC apoptosis;
  cellular response to L-arginine [LAT1 does not transport cationic Arg]; positive regulation of its own
  leucine import) → MARK_AS_OVER_ANNOTATED. mTORC1-linked ones (neg. reg. autophagy; cellular response to
  amino acid stimulus) → KEEP_AS_NON_CORE.
- Lysosomal membrane, apical/basal/basolateral PM, microvillus membrane, exosome, BBB transport,
  immune acts_upstream_of, xenobiotic/drug transport, minor substrates (Pro, Ala) → KEEP_AS_NON_CORE.
