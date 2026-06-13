# SEC63 (Q9UGP8, DNAJC23) review notes

## Identity / overview
SEC63 is a multi-pass ER membrane protein and an auxiliary component of the Sec61 translocon. It contains
a luminal J-domain (DnaJ/Hsp40-type, residues 104-165) plus two Sec63 domains. With SEC62 it forms the
SEC62-SEC63 subcomplex that supports cotranslational and post-translational translocation of precursor
polypeptides into the ER. The hallmark mechanism: the luminal J-domain recruits and stimulates the ATPase
activity of the ER Hsp70 chaperone BiP (HSPA5), driving BiP onto incoming polypeptides at the translocon
to ratchet/gate translocation. SEC63 is also required for efficient biogenesis of polycystin-1 (PKD1).
Loss-of-function SEC63 variants cause autosomal dominant polycystic liver disease (PCLD2).

- UniProt FUNCTION: "Mediates cotranslational and post-translational transport of certain precursor
  polypeptides across endoplasmic reticulum (ER)"; "May cooperate with SEC62 and HSPA5/BiP to facilitate
  targeting of small presecretory proteins into the SEC61 channel-forming translocon complex, triggering
  channel opening for polypeptide translocation to the ER lumen"; "Required for efficient PKD1/Polycystin-1
  biogenesis" [file:human/SEC63/SEC63-uniprot.txt].
- SUBUNIT: "The ER translocon complex consists of channel-forming core components SEC61A1, SEC61B and
  SEC61G and different auxiliary components such as SEC62 and SEC63" [file:human/SEC63/SEC63-uniprot.txt].
- DOMAIN: "J" domain 104-165; SEC63 domains 197-541 and 637-714; KW Chaperone. AltName "DnaJ homolog
  subfamily C member 23" (DNAJC23) [file:human/SEC63/SEC63-uniprot.txt].
- SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane; Multi-pass membrane protein"
  [file:human/SEC63/SEC63-uniprot.txt].
- MUTAGEN H132 (in J-domain HPD motif) "Reduces cotranslational translocation of APLN
  precursor/preproapelin" — links J-domain to translocation [file:human/SEC63/SEC63-uniprot.txt].

## Key functional evidence
- Sec61-Sec62-Sec63 association: PMID:10799540 "Mammalian Sec61 is associated with Sec62 and Sec63" —
  "The latter process is mediated by a membrane protein complex that consists of the Sec61p complex and
  the Sec62p-Sec63p subcomplex" [PMID:10799540].
- Translocation function / BiP cooperation: PMID:22375059, PMID:29719251 "Sec63 and the lumenal chaperone
  BiP act as auxiliary translocation components" [PMID:29719251].
- PCLD link / Nxn interaction: PMID:21251912 "we identified the cytosolic protein nucleoredoxin (NRX) as
  an interaction partner of human Sec63 ... Sec63 is linked to the Wnt signaling pathways and this
  interaction may be the reason why mutations in SEC63 can lead to PCLD" [PMID:21251912].

## Annotation review decisions
- Core role/MF: J-domain co-chaperone that recruits/stimulates BiP (HSPA5) ATPase; captured functionally
  via the translocation BP terms and Sec62/Sec63 complex CC. The cataloged molecular-function terms are
  limited (RNA binding HDA; signaling receptor activity TAS). The J-domain/BiP-regulator role is the most
  informative MF; it is documented in FUNCTION/DOMAIN and via the H132 (HPD) mutagenesis.
- Core CC: Sec62/Sec63 complex (GO:0031207); ER membrane (GO:0005789); ER (GO:0005783).
- Core BP: post-translational protein targeting to ER membrane (GO:0006620); post-translational
  translocation (GO:0031204); cotranslational targeting (GO:0006614).
- GO:0038023 signaling receptor activity (TAS, ProtInc): SEC63 is a translocon J-domain co-chaperone, not
  a signal-transduction receptor. MARK_AS_OVER_ANNOTATED.
- GO:0003723 RNA binding (IBA + HDA, PMID:22658674): SEC63 was captured in mRNA-interactome screens, but
  RNA binding is not an established function of this ER-membrane translocon co-chaperone; the IBA appears
  propagated from such high-throughput captures. The J-domain/Sec63 domains are not canonical RNA-binding
  modules. -> the HDA capture is real data (KEEP_AS_NON_CORE), but the IBA propagation is weakly supported
  -> MARK_AS_OVER_ANNOTATED for the IBA.
- GO:0016020 membrane (IDA): generic; KEEP_AS_NON_CORE (ER membrane is specific).
- GO:0006612 protein targeting to membrane (TAS): correct but generic parent; ACCEPT.
- protein binding (GO:0005515) IPI rows (PMID:21251912 Nxn; PMID:26871637 splicing-interactome):
  KEEP_AS_NON_CORE; the Nxn interaction is disease-relevant but bare term uninformative.

## Disease
PCLD2 (autosomal dominant polycystic liver disease) caused by SEC63 LoF/truncating variants
[file:human/SEC63/SEC63-uniprot.txt; PMID:15133510; PMID:28375157].

## Falcon deep-research findings (incorporated 2026-06)
- Substrate-specificity "rules" for SEC62/SEC63-dependent import directly establish SEC63 client
  selectivity: clients carry signal peptides with longer but less hydrophobic H-regions and lower
  C-region polarity, plus a slowly gating SP and downstream positive-charge cluster
  [PMID:32133789 "those previously unknown substrates share signal peptides (SP) with comparatively longer but less hydrophobic hydrophobic region of SP and lower carboxy-terminal region of SP (C-region) polarity"].
- SEC63 J-domain HPD motif is essential: mutating the conserved HPD (H132Q in the Falcon framing;
  H132 in UniProt mutagenesis) abolishes productive BiP interaction and fails to rescue Sec63
  depletion phenotypes (Falcon; consistent with UniProt MUTAGEN H132 and PMID:29719251).
- Paper explicitly links the SEC62/SEC63 substrate rules to the etiology of SEC63-linked polycystic
  liver disease [PMID:32133789 "contribute to our understanding of the etiology of SEC63-linked polycystic liver disease"].
- "Dynamic brace" gating model: Sec62/Sec63 can fully open / strongly brace open the Sec61 lateral
  gate, lowering the barrier for nonoptimal signal sequences to initiate translocation
  [Shao 2023, Mol Biol Cell, doi:10.1091/mbc.e21-09-0451 — review; not added as ref, mechanism already in review].
- Co-translational recruitment to paused translocation sites: marginally hydrophobic signal sequences/
  TMDs cause Sec61 pausing until Sec63-mediated BiP engagement releases the pause and ensures folding
  [already in review via PMID:36459117, Sun et al. 2022 JCB, doi:10.1083/jcb.202203070].
- Non-canonical IRE1alpha-SEC63-ACLY axis in HCC (already in review via PMID:37122003): ER stress
  -> IRE1alpha phosphorylates SEC63 at T537 -> SEC63 stabilizes ACLY and enters nucleus to raise
  acetyl-CoA / Snail1, promoting metastasis [Hu et al. 2023, J Exp Clin Cancer Res, doi:10.1186/s13046-023-02656-7].
- Clinical genetics (already in review via PMID:38689396): in a 2024 Japanese severe-PLD cohort
  (hTLV >1800 mL/m, n=49), 44/49 (90%) genetically solved; SEC63 = 1/44 (2%) [doi:10.34067/KID.0000000000000461].
- LOH/two-hit evidence for SEC63 cysts appears less frequent than PRKCSH/PKD genes (1/14 cysts, 7%)
  [Wills et al. 2016 EJHG, doi:10.1038/ejhg.2016.97 — not added as ref; background ADPLD genetics].
- Zimmermann 2025 review [PMID:41009394, doi:10.3390/ijms26188823] frames SEC63 as a substrate-
  selective Sec61 translocon accessory/co-chaperone — added as reference.
