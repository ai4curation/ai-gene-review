# ERLIN1 (SPFH1 / ER lipid raft-associated protein 1) review notes

UniProt: O75477 (ERLN1_HUMAN), 348 aa. Synonyms SPFH1, KE04, C10orf69. HGNC:16947.
Single-pass type II ER membrane protein with an SPFH/prohibitin (band 7) domain in the ER lumen.
Belongs to the band 7/mec-2 (prohibitin/stomatin/flotillin) family. Associates with lipid-raft-like
ER membrane domains. Disease: autosomal recessive spastic paraplegia SPG62 (variant G50V).

## Core biology
1. **ERLIN1/ERLIN2 complex mediating ERAD of IP3 receptors.** ERLIN1 (SPFH1) and ERLIN2 (SPFH2) form a
   heteromeric ~2 MDa ring-shaped complex that binds IP3R tetramers and mediates their ERAD with the E3
   ligase RNF170.
   [PMID:19240031 "the ER membrane protein SPFH1 and its homolog SPFH2 form a heteromeric approximately 2 MDa complex that binds to IP(3)R tetramers"]
   [PMID:19240031 "RNA interference-mediated depletion of SPFH1 and SPFH2 blocks IP(3)R"]
   ComplexPortal CPX-7121 "ERLIN1-ERLIN2 complex". In complex with ERLIN2, interacts with RNF170.
2. **Cholesterol binding / SREBP regulation.** Erlins bind cholesterol cooperatively and restrict SREBP
   activation, promoting ER retention of the SCAP-SREBP-Insig complex; they regulate cellular cholesterol
   homeostasis and cholesterol/fatty-acid biosynthesis.
   [PMID:24217618 "Erlins bound cholesterol with specificity and strong cooperativity"]
   [PMID:24217618 "define erlins as novel cholesterol-binding proteins that are directly involved in regulating the SREBP machinery"]
   [PMID:24217618 "promote stability of the SREBP-Scap-Insig complex"]
3. **Sterol-accelerated HMGCR ERAD (gp78/AMFR module).** ERLIN1 interacts with the gp78/AMFR and
   SYVN1/HRD1 ER ubiquitin ligases; SPFH2/TMUB1 link gp78 to sterol-accelerated ERAD of HMG-CoA reductase.
   [PMID:21343306 "we identify two ER membrane proteins, SPFH2 and TMUB1, as associated proteins of mammalian gp78"]
4. **Lipid-raft ER domains.** Erlin-1/2 are prohibitin-family proteins that define lipid-raft-like domains
   of the ER.
   [PMID:16835267 "Erlin-1 and erlin-2 are novel members of the prohibitin family of proteins that define lipid-raft-like domains of the ER"]
5. **USP25/cholesterol/virus.** USP25 deubiquitinates and stabilizes ERLIN1; Usp25-Erlin1/2 activity
   limits cholesterol flux to restrict virus infection (PMID:37683630, not cached — referenced via UniProt).

## Annotation assessment summary
- ER membrane (GO:0005789) / ER (GO:0005783): core compartment → ACCEPT (many redundant Reactome TAS CFTR/CD274
  ERAD-machinery annotations → ACCEPT as correct compartment but non-core specifics).
- ERLIN1/2 complex / ERAD of IP3R (GO:0036503 ERAD pathway IDA): core → ACCEPT.
- cholesterol binding (GO:0015485 IDA): core MF → ACCEPT.
- SREBP signaling (GO:0032933), regulation/negative regulation of cholesterol biosynthesis (GO:0045540/45541),
  negative regulation of fatty acid biosynthesis (GO:0045717): SREBP/sterol role → ACCEPT.
- membrane raft (GO:0045121 NAS): lipid-raft ER domains → ACCEPT (non-core).
- ubiquitin protein ligase binding (GO:0031625 IEA InterPro): consistent with AMFR/SYVN1/RNF170 E3 interactions → ACCEPT (informative).
- protein-containing complex (GO:0032991): generic → KEEP_AS_NON_CORE.
- protein binding (GO:0005515) IPI: uninformative → KEEP_AS_NON_CORE.
- Do NOT over-claim catalytic MF: ERLIN1 is a scaffold/lipid-binding SPFH protein, not an enzyme.

## Falcon deep-research findings (incorporated 2026-06)

Falcon corroborates the existing review (ERLIN1/2 ring complex, IP3R ERAD with RNF170, cholesterol
binding, SREBP restriction, lipid-raft ER domains) and adds three verifiable, mostly newer references:

- ERLIN1/2 scaffolds bridge the full-length isoform of TMUB1 with the E3 ligase RNF170 (conserved
  luminal N-terminal motif binding adjacent ERLIN SPFH domains), and restrict cholesterol
  esterification, thereby favouring ER-to-Golgi cholesterol transport and regulating Golgi morphology
  and the secretory pathway. [PMID:38782601 "we demonstrate a role of ERLIN scaffolds in limiting
  cholesterol esterification, thereby favouring cholesterol transport from the ER to the Golgi
  apparatus and regulating Golgi morphology and the secretory pathway"] (PubMed-verified;
  doi:10.26508/lsa.202402620; Veronese et al. 2024). NEW mechanism (TMUB1-L/RNF170 bridging +
  cholesterol esterification/SOAT1 + secretory pathway) beyond the prior single-client IP3R-ERAD
  model. Added as a top-level reference (relevance HIGH). Loss of ERLINs abolished the TMUB1-RNF170
  interaction; reported SOAT1 tendency to increase in DKO (log2FC 0.40, q=0.07), ER tubule collapse,
  Golgi fragmentation, lipid-droplet accumulation, avasimibe (SOAT1 inhibitor) rescue.
- Largest SPG62 case series to date: 13 individuals from six families with biallelic ERLIN1 variants,
  childhood-onset slowly progressive predominantly pure spastic paraparesis (possible cerebellar /
  peripheral-nerve involvement); three new variants predicted to disrupt the bell-shaped ERLIN1/ERLIN2
  ring. [PMID:39367212 "Biallelic pathogenic ERLIN1 variants induce a rare, predominantly pure,
  spastic paraparesis, with possible cerebellar and peripheral nerve involvement"] (PubMed-verified;
  doi:10.1007/s00439-024-02702-0; Cogan et al. 2024). Expands disease genetics beyond the G50V variant
  noted in the prior review. Added as a top-level reference (relevance HIGH).
- ERLIN1 is a host factor required for efficient hepatitis C virus infection; it is a cholesterol-
  binding ER detergent-resistant-membrane protein, and its knockdown reduces HCV RNA replication
  initiation, viral protein expression, and infectious virus production downstream of entry/primary
  translation. [PMID:31810281 "erlin-1 protein is required early in the infection, downstream of cell
  entry and primary translation, specifically to initiate RNA replication, and later in the infection
  to support infectious virus production"] (PubMed-verified; doi:10.3390/cells8121555; Whitten-Bauer
  et al. 2019). Corroborates the cholesterol-homeostasis/ER-raft role already in the review (which
  also has the USP25-Erlin1/2 antiviral angle via PMID:37683630). Added as a top-level reference
  (relevance MEDIUM).
- Manganelli 2021 (PMID:34572057, already a review reference) plus its companion paper
  (doi:10.1080/15548627.2020.1834207) describe ERLIN1 at MAM raft-like microdomains interacting with
  AMBRA1 to support starvation-induced autophagy initiation. Not added as a new annotation/reference;
  noted here as additional context for a potential MAM/autophagy role.
- Note: none of the three new references were cached in publications/, so no paraphrased
  supporting_text was added to existing annotations (reference validator requires verbatim cached
  substrings). They were added as top-level references with reference_review only.
