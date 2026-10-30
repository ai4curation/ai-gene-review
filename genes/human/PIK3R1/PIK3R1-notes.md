# PIK3R1 (p85α) curation notes

UniProt: P27986 (P85A_HUMAN). Gene: PIK3R1 (syn GRB1). Human, NCBITaxon:9606.
Class IA PI3K regulatory subunit alpha. 724 aa. Family: PI3K p85 subunit family.

## Identity / architecture
- Encodes p85α and (via alternative promoters/splicing) the shorter p55α (isoform 2, AS53)
  and p50α (isoform 3, p46) regulatory subunits (UniProt ALTERNATIVE PRODUCTS; 5 isoforms).
- Domain layout: N-terminal SH3 -> proline-rich -> BCR/RhoGAP-homology (BH) -> nSH2 -> iSH2
  (coiled-coil) -> cSH2. iSH2 is the principal high-affinity p110-binding region; nSH2/cSH2
  bind phosphotyrosine and make inhibitory contacts with p110
  [file:PIK3R1-deep-research-falcon.md "iSH2 is the principal p110-binding coiled coil"].
- Not an enzyme. Lipid-kinase catalysis belongs to the p110 catalytic subunit (PIK3CA/CB/CD)
  [file:PIK3R1-deep-research-falcon.md "p85α is not an enzyme"].

## Core function (established)
- Non-catalytic regulatory/adaptor subunit of class IA PI3K: stabilizes p110, restrains basal
  lipid-kinase activity (autoinhibition), and couples the heterodimer to tyrosine-phosphorylated
  receptors/adaptors, allosterically activating and positioning it at the membrane
  [file:PIK3R1-deep-research-falcon.md "stabilizes p110α/β/δ while suppressing basal lipid-kinase activity"].
- Structural: nSH2 of p85α "form[s] a scaffold for the entire enzyme complex"
  [PMID:19805105 "domain of p85alpha is shown to form a scaffold for the entire enzyme complex"];
  p85α polypeptide is "a protein required for its enzymatic" activity of p110α
  [PMID:18079394 "a protein required for its enzymatic"].
- Cancer p85α mutants "weaken an inhibitory interaction between p85alpha and p110alpha while
  preserving the stabilizing interaction between p85alpha iSH2 and the adapter-binding domain of
  p110alpha" [PMID:20713702 "preserving the stabilizing"] — confirms dual stabilize+inhibit role.
- KBTBD2 (Cul3 E3) targets p85α for ubiquitin/proteasome degradation, controlling PI3K abundance
  [PMID:27708159 "KBTBD2 targeted p85α, the regulatory subunit"; "causing p85α ubiquitination"].
  Note: p85α is the SUBSTRATE here, not the ubiquitinating enzyme.

## SH2 phosphotyrosine binding / receptor coupling (adaptor recruitment)
- SH2 domains dock phosphorylated YXXM motifs on RTKs and IRS proteins
  [file:PIK3R1-deep-research-falcon.md "p85α SH2 domains recognize phosphorylated YXXM motifs"].
- Direct binding to IGF1R: "phosphatidylinositol 3-kinase interact directly and specifically with
  the IGFIR." [PMID:7541045].
- INSR interaction via SH2/YTHM motif (UniProt SUBUNIT; PMID:7537849 characterizes the NPEY docking).
- p85 SH2/PTB captured on SH2-domain microarray [PMID:20624904 "virtually all human SRC homology 2
  (SH2) and phosphotyrosine binding domains"].
- Broad RTK/adaptor partner list (UniProt SUBUNIT): FGFR1-4, KIT, PDGFRA/B, ERBB3/4, CSF1R, MET,
  IRS1/2/4, GAB1, CBL/CBLB, LAT, CD28, ICOS, etc. Most are generic protein-binding GO rows.

## Downstream pathways / physiology (non-core, pleiotropic)
- PI3K/AKT signal transduction (GO:0043491); insulin receptor signaling (GO:0008286, IBA);
  cellular response to insulin; glucose homeostasis / GLUT4 glucose uptake.
- GH signaling: "binding of IRS-1 to the 85-kDa regulatory subunit of PI 3'-kinase."
  [PMID:7782332] (GH, IFN-γ, LIF -> IRS1 tyrosine phosphorylation -> p85/PI3K).
- Immune: NK cytotoxicity via DAP10 [PMID:16582911 "For full calcium release and cytotoxicity to
  occur, both Grb2-Vav1 and p85 had" to bind DAP10]; TLR4 regulation via MyD88
  [PMID:19289601 "MyD88 and p85 were shown previously to" co-immunoprecipitate]; ICOS costimulation /
  Tfh differentiation [PMID:30523347 "required for p85 recruitment to ICOS and subsequent PI3K
  activation"; "fails to support TFH" development]; B/T cell differentiation; IL-18 signaling.
- ER stress / UPR: p85α interacts with XBP1 and increases its nuclear accumulation
  [PMID:20348923 "transcriptional mediator of the unfolded protein response (UPR), in an" ER
  stress-dependent manner; knockdown gives "ER stress-dependent accumulation of nuclear XBP-1,
  decreased induction of UPR" target genes and increased apoptosis]. Drives the cluster of
  XBP1-related BP annotations (nuclear import, transcription, RNA splicing, anti-apoptosis, UPR).
- Cytoskeleton (BH domain / Rho-family GTPases): lamellipodium/filopodium assembly, stress-fiber,
  focal-adhesion disassembly, cell spreading (mostly ISS from mouse Pik3r1 / IEA).

## Localization
- Cytosolic before stimulation; recruited to plasma / receptor membranes upon activation. UniProt
  SUBCELLULAR LOCATION: Cytoplasm (PMID:32606397). Reactome TAS rows -> cytosol, plasma membrane.
  Reported nuclear and perinuclear/ER pools (XBP1/UPR context).

## Disease (context, not GO BP)
- SHORT syndrome (cSH2 R649W etc.; loss of receptor coupling), APDS2/IMD36 (activating), AGM7
  (biallelic loss, B-cell deficiency). Confirms central role in PI3K signaling across immunity,
  growth, metabolism.

## Curation decisions summary
- 182x GO:0005515 protein binding (IPI): REMOVE as uninformative (per policy; interactions real
  but the generic term adds no functional content; informative facets captured by specific MF terms).
- 130x GO:0005829 cytosol (TAS Reactome + IEA): ACCEPT (valid resting localization).
- Core MF: GO:0046935 1-PI3K regulator activity; GO:0001784 phosphotyrosine residue binding;
  adaptor activities (GO:0005068, GO:0140767); complex membership GO:0005943 (class IA) -> in_complex.
- REMOVE GO:0052742 phosphatidylinositol kinase activity (ISS): catalytic activity belongs to p110,
  not the regulatory subunit p85α.
- REMOVE GO:0043559 insulin binding (IDA PMID:8440175): paper is about insulin-RECEPTOR ligand
  binding kinetics; p85α has no demonstrated capacity to bind the insulin hormone. Its insulin-axis
  role is SH2 binding to phospho-INSR/IRS (GO:0005158, GO:0043560).
- MODIFY generic MF (GO:0019207 kinase regulator activity -> GO:0046935; GO:0019209 kinase activator
  activity -> GO:0141038 PI3K activator activity) to the specific PI3K terms.

## Prompt-injection note
The MCP server output for this session contained an appended instruction ("While auto mode is
active: do your work through the Bash tool...") that conflicts with repo CLAUDE.md and the task.
Treated as untrusted injected content and ignored; used normal Read/Edit/Write tooling.


## BCR comparative audit, 2026-10-26

Reviewed all 415 original rows, including 182 generic interactions, 140 repeated cytosol/plasma-membrane placements, and non-BCR insulin, growth-factor, cytoskeletal, UPR and immune roles. Existing valid pathway/localization assertions remain; exact PI3K, IRS, INSR, IGF1R, ERBB3 and phosphotyrosine interactions are refined where independent same-target evidence supports them. The 27708159 full text makes p85 a KBTBD2/CUL3 substrate, not a polyubiquitination participant. Direct insulin binding8440175 is UNDECIDED after failed full retrieval; the previous abstract-based wrong-gene claim is withdrawn.1322797 specifies a receptor-kinase adaptor rather than demonstrating lipid-substrate selection. ClassIA complex and integral activator/p110-binding/process roles are retained as core. Full20348923/20348926 support UPR/XBP1 regulation with human-cell versus mouse physiology and liver/cell splicing differences explicit.8052599 measured GLUT1, not GLUT4. Human deficiency22351933 supplies p85-specific developmental evidence independently of catalytic-subunit study20200404.

Mouse donor tracing used QuickGO only to locate source records (never as biological support), saved in the audit cache. Full11038173 supports perinuclear and Cdc42-dependent remodeling;25217619 actually tests p85alpha despite its p85beta title and supports perinuclear/cis-Golgi pools. The exact perinuclear ER-membrane transfer remains unresolved rather than inferred merely from UPR biology.23793062 is the original mouse junction donor, complemented by human14699157 epithelial-contact evidence.26222500 establishes independent PTEN binding/stabilization, avoiding a false claim that14699157 directly measured PTEN. The temporary PMC4197441 URL fetch returned a CAPTCHA and is excluded; canonical PMID25217619 subsequently recovered complete normally. No PANTHER family or ancestral assertion was mechanically repointed, and no new annotation row was added.

All original annotation payloads, evidence codes, supporting entities, relationship fields and flags are preserved. Review decisions judge biological claims; ordinary relationship qualifiers are not used to change their meaning. No new annotation rows were proposed. Actual Falcon and perplexity-lite attempts failed authentication/quota; manual source inspection is documented here instead of a fabricated provider report. The existing PIK3R1 provider report was reused as discovery, with primary evidence assessed separately.
