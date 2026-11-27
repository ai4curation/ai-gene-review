# ANAPC11 (Q9NYG5) curation notes

## Identity

Human ANAPC11 / APC11 is the 84-residue RING-H2 subunit of the anaphase-promoting
complex/cyclosome (APC/C). It belongs to the RING-box family with RBX1/ROC1 and
RBX2/SAG, from which it is distinguished by pairing specifically with the
cullin-related ANAPC2 rather than with canonical cullins
[PMID:10230407 "ROC1 and ROC2 commonly interact with all cullins while APC11 specifically interacts with APC2, a cullin-related APC subunit."].
The deep-research report (falcon) confirms the identity and notes 44% identity to
yeast Apc11p and 37% to RBX1 and RBX2
[file:human/ANAPC11/ANAPC11-deep-research-falcon.md "Human ANAPC11 shared 44% sequence identity with yeast Apc11p and 37% with each of RBX1/ROC1 and RBX2/SAG"].

## Core biology

- **Minimal ligase module.** A baculovirus-expressed APC2-APC11 heterodimer with
  Ubc4 (UBE2D) or UbcH10 (UBE2C) ubiquitinates securin and cyclin B1, but lacks
  D-box specificity on its own
  [PMID:11739784 "In combination with Ubc4 or UbcH10, a heterodimeric complex of APC2 and APC11 is sufficient to catalyze the ubiquitination of human securin and cyclin B1."]
  [PMID:11739784 "However, the minimal APC2/11 ubiquitin ligase module does not possess substrate specificity"].
- **Cullin binding and zinc.** APC11 and UbcH10 bind the C-terminal cullin
  homology domain of APC2; APC11 binds Zn2+ at 1:3, with the third zinc
  dispensable for activity
  [PMID:11739784 "Both APC11 and UbcH10 bind to the C-terminal cullin homology domain of APC2, whereas Ubc4 interacts with APC11 directly."]
  [PMID:11739784 "Zn(2+)-binding and mutagenesis experiments indicate that APC11 binds Zn(2+) at a 1:3 M ratio."].
- **E2 mechanism (structural).** In the atomic APC/C structure the Apc11 RING
  makes the canonical UBC-domain contact with UbcH10 for chain initiation and is
  repurposed to position the acceptor ubiquitin for Ube2S-mediated K11 elongation
  [PMID:26083744 "Activation of UbcH10 involves a canonical interaction between its UBC domain and Apc11RING"]
  [PMID:26083744 "whereas for Ube2S, Apc11RING is repurposed to position the acceptor ubiquitin for modification by the Ube2S-ubiquitin conjugate"].
  Coactivator binding and phosphorylation move the flexible Apc2-Apc11 module
  upward to allow E2 access
  [PMID:27120157 "In the active conformation, the platform subdomain containing subunits Apc1, Apc4 and Apc5 is shifted upward, inducing a large movement of the catalytic module to enable E2 access"].
- **Chain type.** The APC/C builds K11-linked chains
  [PMID:18485873 "We find that the APC/C triggers substrate degradation by assembling K11-linked ubiquitin chains"]
  and K11/K48-branched chains on mitotic regulators and quality-control substrates
  [PMID:29033132 "engineered a bispecific antibody to detect K11/K48-linked chains and identified mitotic regulators, misfolded nascent polypeptides, and pathological Huntingtin variants as their endogenous substrates."].
- **Cellular role.** APC11 depletion inactivates the APC/C, stabilises CDC20 and
  cyclin A during SAC signalling, and slows MCC release from the APC/C
  [PMID:21926987 "APC/C from APC11-depleted cells was markedly less active"]
  [PMID:21926987 "Depleting APC11, but not APC10, stabilised Cdc20 and Cyclin A during SAC signalling"].
- **Localization.** Cytoplasm and nucleus (UniProt, from GFP-fusion imaging in
  Chan et al. 2001, PMID:11573242, not cached)
  [file:human/ANAPC11/ANAPC11-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:11573242}. Nucleus {ECO:0000269|PubMed:11573242}."].
  HPA adds nucleoplasm and nucleolus; the nucleolar signal is uncorroborated.

## Curation decisions worth recording

1. **GO:0001664 G protein-coupled receptor binding (IEA, Ensembl Compara) -> REMOVE.**
   The WITH/FROM is UniProtKB:Q8K4P2 / ENSRNOP00000051837. Q8K4P2 is rat
   *Npb* (neuropeptide B), whose GO:0001664 annotations are RGD IMP
   (PMID:12118011), InterPro IPR013297 and a PAINT IBA on the neuropeptide
   family node. It is not an APC11 ortholog; the Compara projection mapped the
   wrong rat gene product onto ANAPC11. Demonstrably wrong electronic transfer.
2. **GO:0034450 ubiquitin-ubiquitin ligase activity (IDA, PMID:10230407) -> MODIFY to GO:0061630.**
   QuickGO definition: "Isoenergetic transfer of ubiquitin from one protein to an
   existing ubiquitin chain ... where both ... linkages are thioester bonds
   between the C-terminal glycine of ubiquitin and a sulfhydryl side group of a
   cysteine residue." That is transthiolation chemistry; a RING E3 has no
   catalytic cysteine. The paper's result ("catalyze isopeptide ligations to form
   polyubiquitin chains") is isopeptide chain formation, i.e. ubiquitin protein
   ligase activity, which the same paper already supports on ANAPC11.
3. **GO:0000278 mitotic cell cycle (TAS, PMID:11739784) -> MODIFY to GO:0007091.**
   Too shallow; the same paper supports GO:0045842 IDA and GO:0016567 IDA.
4. **GO:0005515 protein binding x2 (IPI, PMID:32814053; PEX1 and GRN) -> REMOVE.**
   Y2H interactome of neurodegenerative-disease proteins; uninformative, partners
   unrelated to APC/C biology; removal does not assert the pairs are false.
5. **GO:0031461 cullin-RING ubiquitin ligase complex (IEA ARBA) -> ACCEPT.**
   Checked via QuickGO: GO:0005680 is_a descendant of GO:0031461, so the row is
   a true parent (the ANAPC2 review chose MODIFY -> GO:0005680 for the same row;
   either is defensible, the parent is not wrong).
6. **Reactome TAS location rows (20 cytosol, 16 nucleoplasm) -> ACCEPT.** Both
   compartments host APC/C ligase activity (mitotic cytosol for APC/C-CDC20;
   nucleus for APC/C-CDH1 in late mitosis/G1 and for APC/C phosphorylation).
   Each row quotes its own Reactome summary.
7. **GO:0005730 nucleolus (HPA IDA) -> KEEP_AS_NON_CORE.** Single-antibody
   localization of an 84-aa protein with no known nucleolar APC/C activity.
8. **GO:0051445 regulation of meiotic cell cycle (NAS) -> KEEP_AS_NON_CORE**,
   matching the ANAPC2 review.
9. **All IBA rows -> ACCEPT.** PTN000129805 is the RING-box family node
   (ligase activity, cullin binding, ubiquitination, nucleus); PTN000129916 is
   the APC11-specific node (APC/C membership, positive regulation of
   metaphase/anaphase transition). Node placements make phylogenetic sense:
   the APC/C-specific functions are placed only on the APC11 subclade.

## Open points

- Yan et al. 2023 (bladder cancer) report ANAPC11-dependent K11-linked
  ubiquitination of FOXO3 but did not establish canonical APC/C/coactivator
  dependence
  [file:human/ANAPC11/ANAPC11-deep-research-falcon.md "the study did not establish that FOXO3 is a canonical APC/C substrate."].
  Not proposed as a NEW annotation.
- No NEW terms proposed; the GO-CAM 6348a65d00002236 already models ANAPC11
  with GO:0004842 in the APC/C, in agreement with this review.
