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
