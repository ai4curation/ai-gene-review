---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/TOMM20
affinage_run_date: 2026-06-10T10:51:55
uniprot_accession: Q15388
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 37
citation_count: 37
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for TOMM20 (human)

## Current model (mechanistic narrative)

TOMM20 is the principal cytosolic receptor of the mitochondrial outer-membrane TOM translocase, recognizing N-terminal presequences to direct cleavable preproteins into the matrix, inner membrane, and intermembrane space [PMID:2557158, PMID:8132642]. It is anchored in the outer membrane by an N-terminal hydrophobic segment in an Nin-Ccyto orientation, leaving an all-α-helical cytosolic domain that captures presequences as amphiphilic helices within a hydrophobic groove [PMID:1661031, PMID:10721992]; recognition is dynamic, sampling multiple bound orientations on a sub-millisecond timescale, with an N-terminal presequence element conferring targeting specificity and a C-terminal element raising import efficiency [PMID:17948058, PMID:21173275]. Tom20 operates not in isolation but as a co-receptor system: it cooperates with Tom22 in sequential presequence recognition and with Tom70 in handling internal-signal carriers, displacing Hsp70/Hsp90 chaperones from Tom70 via its C-terminal DDVE motif [PMID:9252394, PMID:18063580, PMID:21771790]. Its transmembrane segment is integrated into the membrane and docked into the TOM complex by the assembly factor Mim1, and within the assembled holo complex Tom20 is a dynamically associated, mobile gatekeeper stabilized by interactions with Tom22, Tom40, and Tom6 that gate preprotein entry into the Tom40 pore [PMID:18187149, PMID:34347503, PMID:37579144, PMID:39071881]. Beyond canonical import, Tom20 can directly insert VDAC into lipid bilayers independently of the Tom40 pore [PMID:10352015], promotes translation-coupled localization of nuclear-encoded mitochondrial mRNAs to the mitochondrial surface [PMID:19858288], and serves as a docking platform for stress signaling: PINK1 tethers TOM to TIM23 through the Tom20 cytosolic domain to drive mitophagy [PMID:38416681], while ROS-induced oxidation of Tom20 recruits Bax to trigger caspase-3/GSDME pyroptosis [PMID:30287942]. TOMM20 levels and function are controlled by ubiquitination through SCF-Fbxo7 and HUWE1 E3 ligases [PMID:27503909, PMID:38184713], and it acts as a platform recruiting FEM1B-CRL2 to degrade PLD6 and regulate mitochondrial morphology [PMID:40263465]. In Parkinson's disease, modified α-synuclein binds TOM20 with high affinity, blocking the TOM20-TOM22 interaction and impairing protein import, respiration, and membrane potential [PMID:27280685].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0140104 molecular carrier activity, GO:0038024 cargo receptor activity, GO:0044183 protein folding chaperone, GO:0060089 molecular transducer activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-9609507 Protein localization, R-HSA-9612973 Autophagy, R-HSA-5357801 Programmed Cell Death, R-HSA-1643685 Disease
- **partners:** TOMM22, TOMM70, TOMM40, PINK1, FBXO7, HUWE1, FEM1B, AIP
- **complexes:** TOM complex (mitochondrial outer membrane translocase)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1989 | High | MOM19 (TOMM20) is a 19 kDa mitochondrial outer membrane protein that functions as an import receptor; IgG and Fab fragments against MOM19 inhibit high-affinity binding and import of precursor proteins destined for multiple mitochondrial subcompartments (matrix, inner membrane, intermembrane space), but not ADP/ATP carrier or cytochrome c. | PMID:2557158 | Cell |
| 1991 | High | MOM19 is anchored in the outer mitochondrial membrane via an NH2-terminal hydrophobic sequence with the rest forming a cytosolic hydrophilic domain; its targeting to mitochondria is independent of protease-accessible surface receptors and occurs via direct assembly with the general insertion site (GIP). | PMID:1661031 | Science |
| 1994 | High | Deletion of MOM19 (yeast TOMM20) strongly impairs import of cleavable preproteins but only slightly inhibits import of non-cleavable ADP/ATP carrier and phosphate carrier, establishing MOM19 as the primary receptor for presequence-containing preproteins. | PMID:8132642 | The Journal of biological chemistry |
| 1994 | High | Depletion of MOM19 in Neurospora crassa causes severe mitochondrial biogenesis defects including loss of cristae, reduced cytochromes, and impaired protein import; additionally, loss of MOM19 leads to decreased MOM22 levels and reduced import through MOM22, revealing a functional interdependence. | PMID:8120088 | The Journal of cell biology |
| 1995 | High | MOM22 and MOM19 cooperate as a presequence receptor complex at the mitochondrial surface; both bind preproteins in a reversible, salt-sensitive manner dependent on electrostatic interactions between presequence positive charges and MOM22's acidic cytosolic domain; MOM19 and MOM22 can be cross-linked with high efficiency. | PMID:7556061 | The EMBO journal |
| 1995 | High | Human TOMM20 (huMas20p) is inserted into the outer mitochondrial membrane in Nin-Ccyto orientation, can functionally complement delta mas20 yeast respiratory defects, and antibodies against its soluble domain inhibit import of diverse precursor proteins including uncoupling protein. | PMID:7589431 | FEBS letters |
| 1997 | High | Purified cytosolic domains of Tom20, Tom22, and Tom70 each bind mitochondrial preproteins independently but with different specificities: Tom20 binds both presequence-containing and internal-signal preproteins; Tom22 selectively binds presequence preproteins in a salt-sensitive manner; Tom70 preferentially binds preproteins with internal targeting information. A synthetic presequence peptide competes for Tom20 and Tom22 but not Tom70 binding. | PMID:9252394 | The Journal of biological chemistry |
| 1997 | High | The linker segment (charged amino acid-rich region between the membrane anchor and TPR motif) of rat Tom20 is essential for its receptor function; the TPR motif and C-terminal acidic cluster are dispensable. Tom20N69 (anchor + linker only) complements delta tom20 yeast growth and import defects. | PMID:9218491 | The Journal of biological chemistry |
| 2000 | High | NMR structure of rat Tom20 cytosolic domain in complex with an aldehyde dehydrogenase presequence reveals an all alpha-helical structure with a hydrophobic groove accommodating the presequence as an amphiphilic helix; binding is mediated mainly by hydrophobic rather than ionic interactions despite the importance of positive charges for import. | PMID:10721992 | Cell |
| 2000 | High | The mitochondrial targeting signal of Tom20 requires moderate TMD hydrophobicity and a net positive charge within five residues of the COOH-terminal flanking region; high TMD hydrophobicity or loss of positive charges redirects Tom20 to the ER-Golgi. SRP recognizes the TMD but with reduced affinity; the positive COOH-terminal charge inhibits SRP-induced translation arrest. | PMID:11038175 | The Journal of cell biology |
| 1999 | High | Tom20, Tom22, and Tom70 cytosolic domains bind to linear peptide segments of preproteins with differential specificity: Tom20 preferentially binds presequence segments; Tom22 binds the C-terminal presequence/N-terminal mature protein junction; Tom70 and Tom20 both bind multiple internal regions of non-cleavable carriers (phosphate carrier), whereas charge is not a critical determinant for internal targeting sequences. | PMID:10347216 | The Journal of biological chemistry |
| 1999 | High | Tom20 directly inserts newly synthesized VDAC into lipid bilayers as a functional transmembrane channel, bypassing the Tom40 translocation pore; synthetic liposomes containing only the cytosolic domain of human Tom20 are sufficient for this insertion activity. | PMID:10352015 | The Journal of cell biology |
| 2001 | High | Tom20 binds different segments (N-terminal or C-terminal regions) in different presequences; the binding is mediated by hydrophobic interactions and the bound presequence orientation is the same regardless of which segment is perturbed. | PMID:11237589 | Journal of molecular biology |
| 2003 | High | AIP (arylhydrocarbon receptor-interacting protein) binds to the COOH-terminal acidic segment of Tom20 via its TPR domain and forms a ternary complex with Tom20 and mitochondrial preproteins; AIP has chaperone-like activity that prevents preproteins from losing import competency. | PMID:14557246 | The Journal of cell biology |
| 2003 | Medium | The cytosolic domains of Tom20 and Tom22 possess chaperone-like activity that prevents substrate proteins from aggregating; Tom20 binds unfolded substrate proteins regardless of presequence presence, and a presequence peptide inhibits this chaperone activity, suggesting the presequence-binding and chaperone-active sites are identical or adjacent. | PMID:14699115 | The Journal of biological chemistry |
| 2007 | High | Tom20 recognizes mitochondrial presequences through dynamic equilibrium among multiple bound states (multiple-mode interaction); crystal structures with disulfide-tethered presequences show two unique relative orientations of the presequence, and NMR 15N relaxation analyses indicate sub-millisecond timescale motion at the Tom20-presequence interface. | PMID:17948058 | The EMBO journal |
| 2007 | High | Tom20 and Tom22 are involved in the same step or sequential steps of the same targeting signal recognition pathway; selective protease cleavage of either receptor domain causes similar import impairment across multiple substrate classes and import pathways. | PMID:18063580 | The Journal of biological chemistry |
| 2007 | High | The transmembrane segment of Tom20 contains critical residues required for its docking into the TOM complex; this docking is catalyzed by the assembly factor Mim1/Tom13. Mutations destabilizing the TMD or deletion of Mim1 prevent Tom20 from functioning as an import receptor. | PMID:18187149 | Journal of molecular biology |
| 2007 | High | Mim1 is required for integration of Tom20 into the outer mitochondrial membrane; Mim1 functions as a homo-oligomer via GXXXG dimerization motifs in its transmembrane segment; mutations in the GXXXG motifs abolish oligomerization and Mim1 function, preventing Tom20 membrane integration. | PMID:18177669 | Journal of molecular biology |
| 2010 | High | Tom20 mediates localization of mRNAs encoding mitochondrial proteins to the mitochondrial surface in a translation-dependent manner requiring features within the encoded mitochondrial targeting signal; tom20Δ yeast show reduced mitochondrial association of most mitochondrial mRNAs, and tom20Δ puf3Δ double knockouts show additive growth defects. | PMID:19858288 | Molecular and cellular biology |
| 2010 | High | Tom20 has a dual role in mitochondrial protein import: an N-terminal binding element in the presequence is essential for mitochondrial targeting specificity, while a C-terminal element increases import efficiency at a step prior to inner membrane translocation, revealed by NMR mapping and in vitro import/cross-linking experiments. | PMID:21173275 | Proceedings of the National Academy of Sciences |
| 2011 | High | Tom20 interacts with the TPR clamp domain of Tom70 via a conserved C-terminal DDVE motif, as shown by cross-linking on mitochondria from HeLa cells and co-precipitation/NMR with purified proteins; Tom20 competes with Hsp70/Hsp90 for Tom70 binding, suggesting a chaperone displacement mechanism for preprotein release from Tom70. | PMID:21771790 | The Journal of biological chemistry |
| 2011 | Medium | Tom20 is distributed in nanoscale clusters in the outer mitochondrial membrane; cluster density correlates with mitochondrial membrane potential and follows an inner-cellular gradient from perinuclear to peripheral mitochondria, adjusted to cellular growth conditions. | PMID:21799113 | Proceedings of the National Academy of Sciences |
| 2016 | High | Posttranslationally modified α-synuclein binds with high affinity to the TOM20 presequence receptor, preventing TOM20-TOM22 co-receptor interaction and impairing mitochondrial protein import; this results in deficient respiration, elevated ROS, and loss of membrane potential. Modest knockdown of α-synuclein maintained import in a PD model; TOM20 overexpression preserved import. | PMID:27280685 | Science translational medicine |
| 2016 | Medium | SCFFbxo7/PARK15 ubiquitin ligase ubiquitinates TOMM20, and TOMM20 ubiquitination promotes mitophagy; TOMM20 protein levels correlate with Fbxo7 expression (stabilizing effect). PD-associated Fbxo7 mutations do not impair TOMM20 ubiquitination. | PMID:27503909 | The Biochemical journal |
| 2018 | High | ROS-induced oxidation and oligomerization of Tom20 enables Bax recruitment to mitochondria; oxidized Tom20 facilitates cytochrome c release to activate caspase-3, which then cleaves GSDME to trigger pyroptosis. This Tom20-Bax-caspase-GSDME pathway mediates iron-driven pyroptotic cell death in melanoma cells. | PMID:30287942 | Cell research |
| 2019 | Medium | Celastrol blocks PINK1-dependent mitophagy by disrupting the direct association between PINK1 and TOM20 both in vitro and in vivo; PINK1 directly and strongly associates with TOM20 (and more weakly with TOM70); celastrol also disrupts PINK1 complex formation and sequesters PINK1 into high-molecular-weight aggregates upon mitochondrial depolarization. | PMID:30885942 | The Journal of biological chemistry |
| 2021 | Medium | Tom20 controls the mitochondrial localization of Bcl2; upon apoptosis induction, Bcl2 is translocated from ER through MAM to mitochondria, and this transfer is dependent on TOM20. A small TOM20-Bcl2 interaction domain potentiates Bcl2's anti-apoptotic properties, suggesting the TOM20-Bcl2 interaction is pro-apoptotic. | PMID:33589622 | Cell death & disease |
| 2021 | Medium | Tom20 is dynamically associated with the TOM complex; single-particle tracking in human cells shows Tom20 has higher lateral membrane mobility than Tom7/TOM core. Post-translational ligation of Tom20 to Tom7 (reducing Tom20 mobility) or high substrate loading both decrease Tom20 diffusion, suggesting dynamic association is functionally relevant for active import. | PMID:34347503 | Molecular biology of the cell |
| 2022 | High | Cryo-EM structure of the human TOM complex at 2.53 Å (core) and 3.74 Å (holo with Tom20 and Tom22 cytosolic domains) reveals that Tom20 and Tom22 share a similar three-helix bundle structural feature in the cytosolic domain; structure-guided mutagenesis shows the Tom22 cytosolic domain H1 helix is critical for presequence binding. | PMID:35733257 | Proceedings of the National Academy of Sciences |
| 2023 | High | Cryo-EM structures of the TOM core complex (3.3 Å) and holo complex including Tom20 (6-7 Å) from Neurospora crassa reveal Tom20 has a transmembrane helix and cytoplasmic receptor domain and acts as a dynamic gatekeeper; the structure shows Tom20 interactions with other TOM subunits and a bound preprotein, supporting a dynamic gating mechanism for preprotein entry into the pore. | PMID:37579144 | Proceedings of the National Academy of Sciences |
| 2024 | High | Upon mitochondrial stress, PINK1 forms a supercomplex with TOM and TIM23 in human cells, dopamine neurons, and midbrain organoids; PINK1 tethers TOM to TIM23 through an interaction between the PINK1 N-terminal-C-terminal extension module and the cytosolic domain of Tom20. Disruption of this interaction (by designer or PD-associated PINK1 mutations) inhibits downstream mitophagy. | PMID:38416681 | Proceedings of the National Academy of Sciences |
| 2024 | High | Cryo-EM structure of the human TOM holo complex (∼6 Å) reveals the intact Tom20 receptor, showing only one Tom20 subunit at the center of the complex stabilized by extensive interactions with Tom22, Tom40, and Tom6; the structure suggests different receptors can work simultaneously for efficient preprotein translocation. | PMID:39071881 | PNAS nexus |
| 2024 | Medium | HUWE1 E3 ubiquitin ligase directly ubiquitinates TOMM20 and regulates its degradation; HUWE1 also regulates TOMM20 degradation via the PARKIN-mediated pathway. HUWE1 overexpression impairs mitochondrial function (ATP generation, membrane potential), increases ROS and apoptosis, sensitizing CRC cells to oxaliplatin. | PMID:38184713 | Oncogene |
| 2025 | High | FEM1B (substrate receptor of CRL2 E3 ligase) physically interacts with TOM20, and this interaction facilitates FEM1B-mediated ubiquitination and degradation of PLD6, a regulator of mitochondrial dynamics. Disruption of the FEM1B-TOM20 interaction impairs PLD6 degradation and causes mitochondrial morphology defects phenocopying PLD6 overexpression. | PMID:40263465 | Nature chemical biology |
| 2025 | Medium | TOMM20 physically interacts with androgen receptor (AR) and stabilizes AR protein in prostate cancer cells; TOMM20 depletion reduces cytoplasmic and nuclear AR protein levels and promotes AR degradation via the SKP2-mediated ubiquitin-proteasome pathway, independently of heat shock proteins; TOMM20 knockdown reduces AR binding to androgen response elements and AR-target gene transcription. | PMID:40044984 | Oncogene |
| 2024 | Medium | TOM20 directly binds sideroflexin-3 (SFXN3) in the mitochondrial outer membrane, and proximity ligation assay shows PCBP2 (cytosolic Fe(II) chaperone) is proximal to TOM20 at the mitochondrial surface; this establishes a PCBP2-TOM20-SFXN3 axis as a pathway for iron entry into mitochondria. | PMID:38599240 | Free radical research |

## Citations

- PMID:10347216
- PMID:10352015
- PMID:10721992
- PMID:11038175
- PMID:11237589
- PMID:14557246
- PMID:14699115
- PMID:1661031
- PMID:17948058
- PMID:18063580
- PMID:18177669
- PMID:18187149
- PMID:19858288
- PMID:21173275
- PMID:21771790
- PMID:21799113
- PMID:2557158
- PMID:27280685
- PMID:27503909
- PMID:30287942
- PMID:30885942
- PMID:33589622
- PMID:34347503
- PMID:35733257
- PMID:37579144
- PMID:38184713
- PMID:38416681
- PMID:38599240
- PMID:39071881
- PMID:40044984
- PMID:40263465
- PMID:7556061
- PMID:7589431
- PMID:8120088
- PMID:8132642
- PMID:9218491
- PMID:9252394
