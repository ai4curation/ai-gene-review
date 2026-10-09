# RPTOR (Q8N122) review notes

## 2026-10-09: GO annotation review

Provider deep research was unavailable in this environment (no provider API keys),
so this is a manual literature synthesis with inline provenance.

RPTOR / Raptor (Regulatory-associated protein of mTOR) is the defining,
substrate-recruiting scaffold subunit of mTOR complex 1 (mTORC1). The core complex
is MTOR + RPTOR + MLST8 [file:genes/human/RPTOR/RPTOR-uniprot.txt "which contains MTOR, MLST8 and RPTOR"].
Raptor has two non-catalytic adaptor roles that together make it the heart of
nutrient signaling to growth:

1. **Substrate-recruiting (enzyme-substrate) adaptor.** Raptor binds the ~5-residue
   TOR signaling (TOS) motifs of mTORC1 substrates and regulators and presents them
   to the MTOR kinase active site [PMID:29236692 "binds to a ~5 amino acid Tor signaling sequence (TOS) motif present in the 4EBP1 and S6K1 substrates"].
   It is "an essential scaffold for the mTOR-catalyzed phosphorylation of 4EBP1"
   [PMID:12150926 "raptor is an essential scaffold for the mTOR-catalyzed"] and
   "strongly enhances the mTOR kinase activity toward p70alpha"
   [PMID:12150926 "it strongly enhances the mTOR kinase activity toward p70alpha"].
   TOS-mediated binding is required for substrate phosphorylation
   [PMID:12747827 "the TOS motif functions as a docking site"];
   the RNC/caspase-like N-terminal domain of Raptor faces the catalytic cavity and
   is noncatalytic [PMID:27909983 "Raptor shows no caspase activity and therefore may bind to TOS"].
   The PRAS40 inhibitor blocks these sites [PMID:29236692 "PRAS40 inhibits both substrate-recruitment"].
   Substrates/regulators recruited via TOS include EIF4EBP1 (4E-BP1), EIF4EBP2 (4E-BP2),
   RPS6KB1 (S6K1), SIRT1 and PRAS40/AKT1S1.

2. **Lysosomal-membrane / Rag-GTPase adaptor.** On amino-acid sufficiency, active
   Rag heterodimers (GTP-RagA/B : GDP-RagC/D) bind Raptor and recruit mTORC1 to the
   lysosomal surface, where Rheb activates it
   [PMID:26588989 "the active Rag heterodimers physically bind to the Raptor subunit of mTORC1 and thus recruit mTORC1 to lysosomes"],
   [PMID:20381137 "mTOR and raptor co-localized with LAMP2"]. mTORC1 "docks on the
   lysosome through the direct interaction of Raptor with the lysosome-associated Rag
   GTPase" [PMID:31601708 "docks on the lysosome through the direct interaction of Raptor with the lysosome-associated Rag GTPase"],
   and mutations in the Raptor "claw" that disrupt Rag binding block lysosomal
   recruitment [PMID:31601708 "Mutations that disrupted Rag-Raptor binding inhibited mTORC1 lysosomal"].
   A raptor-Rheb15 fusion that forces mTORC1 onto the lysosome makes signaling
   Rag/Ragulator-independent [PMID:20381137 "it did not reduce the amino acid-insensitive mTORC1 activity observed in raptor-Rheb15 expressing cells"].

**Raptor as a regulatory hub (PTMs).** Raptor is the convergence point for many
upstream signals, almost all acting by tuning its two adaptor functions:
- AMPK phosphorylates Raptor (Ser722/Ser792) under energy stress, inducing 14-3-3
  binding and inhibiting mTORC1 [PMID:18439900 "AMPK directly phosphorylates the mTOR binding partner raptor on two"], [PMID:18439900 "this phosphorylation induces 14-3-3 binding"].
- NLK phosphorylates Raptor Ser863 under osmotic stress to disrupt Rag binding
  [PMID:26588989 "inhibits mTORC1 lysosomal localization and thereby"].
- PKA (downstream of GPCR/cAMP) phosphorylates Raptor Ser791 to inhibit mTORC1
  [PMID:31112131 "GPCR signaling inhibits mTORC1 via PKA phosphorylation of Raptor"].
- EP300/p300 acetylates Raptor Lys1097 (driven by the leucine metabolite acetyl-CoA),
  promoting Rag binding and activation [PMID:30197302 "EP300-mediated acetylation of the mTORC1 regulator,"], [PMID:32561715 "This acetylation event is necessary for raptor binding to RRAG proteins on the lysosome"].
- OGT O-GlcNAcylates Raptor (Thr700) on glucose sufficiency to promote Rag binding
  [PMID:37541260 "threonine 700 facilitates the interactions between Raptor and Rag"].
- OTUB1 deubiquitinates/stabilizes Raptor [file:genes/human/RPTOR/RPTOR-uniprot.txt "Deubiquitinated by OTUB1 via a non-"].

**Localization.** Lysosome membrane (active), cytoplasm/cytosol (inactive pool), and
cytoplasmic stress granules under arsenite/oxidative stress
[file:genes/human/RPTOR/RPTOR-uniprot.txt "In arsenite-stressed cells, accumulates in stress"].
There is no evidence Raptor itself is nuclear; nucleoplasm annotations trace to
Reactome models of nuclear mTORC1 at Pol III genes, not to observed Raptor
localization.

**Downstream outputs** (all via mTORC1, not Raptor-autonomous): cell growth and cell
size, protein/lipid/nucleotide synthesis, suppression of autophagy (ULK1/ATG13/TFEB),
Pol III transcription, and metabolic gene networks. These are correct for the complex
but are mostly non-core for Raptor's own molecular function.

## Decisions (non-ACCEPT action classes)

- **GO:0005515 protein binding (IPI rows).** Per the project policy, generic protein
  binding is replaced by an informative MF where the paper supports one, and removed
  otherwise (removal does not deny the interaction). Rows whose partner is a TOS-motif
  **substrate/regulator that Raptor presents to MTOR** (EIF4EBP1 Q13541, EIF4EBP2
  P70445, RPS6KB1 P23443, rat Rps6kb1 P67999, SIRT1 Q96EB6) were MODIFIED to
  GO:0140767 enzyme-substrate adaptor activity. All other GO:0005515 rows (MTOR,
  MLST8, and the many regulators/screen partners — DEPTOR, PIH1D1, G3BP1, SPAG5,
  HTR6, Rab1A, BRAT1, PREX1, MTMR3, BRAF, MAPK8, LARP1, GTF3C2, LARS1, SNAT7/SLC38A7,
  Tel2/Tti1, PKCζ, SIK3) were REMOVED as uninformative; complex membership
  (GO:0031931) and specific process rows capture the biology. These interactions are
  real; removal only drops the non-informative term.
- **GO:0004674 protein serine/threonine kinase activity (contributes_to, IDA).**
  MODIFIED to GO:0140767. Raptor is noncatalytic [PMID:27909983 "Raptor shows no caspase activity and therefore may bind to TOS"];
  the kinase is MTOR. Raptor's informative contribution is substrate presentation.
- **GO:0030295 protein kinase activator activity (IDA).** MODIFIED to GO:0140767.
  The "activation" Raptor provides is substrate recruitment/presentation, not
  allosteric kinase activation [PMID:12150926 "it strongly enhances the mTOR kinase activity toward p70alpha"].
- **GO:0030291 protein ser/thr kinase inhibitor activity (IDA, PMID:12718876).**
  MARK_AS_OVER_ANNOTATED. Raptor's association can conditionally restrain MTOR kinase
  activity [PMID:12718876 "stabilizes the interaction of raptor with mTOR"], but
  assigning a standalone kinase-inhibitor MF misrepresents an essential positive
  scaffold; this is an over-annotation, not a core function.
- **KEEP_AS_NON_CORE.** Downstream/tissue/stress outputs that are true for mTORC1 but
  not Raptor's core adaptor activity: endothelial proliferation, DNA damage response,
  xenobiotic response, social behavior, osteoclast/odontoblast differentiation,
  glycolysis / lipid biosynthesis / pentose-phosphate shunt, Pol III transcription,
  G1/S transition, hypoxia/osmotic stress responses, and the rat-ortholog neuronal
  localizations (dendrite, neuronal cell body).
- **MARK_AS_OVER_ANNOTATED.** ARBA-generated over-general IEAs (regulation of cell
  communication, regulation of signaling); nucleoplasm (Reactome, propagated from
  modeled nuclear-mTORC1 composition, not observed Raptor localization).
