# DNAJC10 (ERdj5 / Macrothioredoxin) research notes

## Identity
- UniProt Q8IXB1 (DJC10_HUMAN), 793 aa precursor (signal 1-32). HGNC:24637. EC 1.8.4.2.
- RecName: "Endoplasmic reticulum disulfide reductase DNAJC10". KDEL-type ER retention (790-793).
- Domain architecture: N-terminal J domain (35-100, HPD motif 63-65) + SIX thioredoxin-fold domains;
  four redox-active Trx domains (Trx1-4) with CXXC active sites (disulfides 158-161, 480-483, 588-591,
  700-703); two redox-inactive Trxb regions. [file:human/DNAJC10/DNAJC10-uniprot.txt FT DOMAIN/DISULFID]
- Trx domains 3 and 4 are the primary reductase domains (Trx4 most efficient). [uniprot DOMAIN]

## DUAL function (the key point): reductase + BiP co-chaperone
- ER disulfide reductase: binds substrates and catalyzes reduction/removal of non-native (improper)
  disulfide bonds. EC 1.8.4.2 (protein-disulfide + 2 glutathione = protein-dithiol + GSSG).
  [PMID:23769672 "ERdj5 acts as the ER reductase, both preparing misfolded proteins for degradation and
  catalyzing the folding of proteins that form obligatory non-native disulfides."]
- J-domain co-chaperone of BiP/HSPA5 (ER Hsp70): interacts via J domain/HPD in an ATP-dependent manner;
  required for ERdj5 activity in both folding and degradation.
  [PMID:12411443 "ERdj5 interacts via its DnaJ domain with BiP in an ATP-dependent manner."]
  [file:human/DNAJC10/DNAJC10-uniprot.txt "Interacts (via its J domain) with HSPA5; this interaction is
  required for DNAJC10 activity in both protein folding and degradation."]
  H63Q (HPD->QPD) prevents BiP binding [uniprot MUTAGEN His-63].

## Roles
- ERAD: reduces disulfides in misfolded glycoproteins recognized by EDEM1, enabling retrotranslocation
  and degradation. [PMID:18400946 "ERdj4 and ERdj5 are required for endoplasmic reticulum-associated
  protein degradation of misfolded surfactant protein C." ; "ERdj4 and ERdj5 promote turnover of
  misfolded SP-C and this activity is dependent on their ability to stimulate BiP ATPase activity."]
- Productive folding: required for efficient folding/secretion of LDLR by reducing non-native disulfides.
  [PMID:23769672 "for one of the identified substrates, the low-density lipoprotein receptor (LDLR),
  ERdj5 is required not for degradation, but rather for efficient folding."]
- ER-stress apoptosis: ERdj5 overexpression promotes ER-stress-induced apoptosis in neuroblastoma by
  down-regulating the UPR. [PMID:19122239 "ERdj5 promoted apoptosis in tunicamycin, thapsigargin, and
  bortezomib-treated cells."] -- this is an overexpression phenotype; KEEP_AS_NON_CORE.
- Cooperation with BiP for ERAD substrate reduction. [PMID:37739037 "cooperation between ERdj5 and BiP"]

## GOA WITH-partner key
- P11021 = BiP/HSPA5 (ER Hsp70). Q8IWF2 = FOXRED2. Q5HYA8 = ? (interactome).

## Review logic
CORE MFs (dual):
- protein-disulfide reductase activity (GO:0015035, IDA PMID:23769672): ACCEPT, CORE.
- Hsp70 protein binding (GO:0030544, IPI BiP): ACCEPT, CORE (J-domain BiP co-chaperone).
Other MF:
- disulfide oxidoreductase activity (GO:0015036, ISS/IEA): ACCEPT (parent of reductase activity).
- oxidoreductase activity acting on sulfur group disulfide acceptor (GO:0016671, IBA/ISS): ACCEPT.
- protein-disulfide reductase (glutathione) activity (GO:0019153, IEA RHEA EC:1.8.4.2): ACCEPT (the EC reaction).
- misfolded protein binding (GO:0051787, IDA/IBA): ACCEPT (binds misfolded substrates).
- protein-folding chaperone binding (GO:0051087, IDA): ACCEPT (binds BiP).
- ATPase binding (GO:0051117, IPI BiP): ACCEPT/KEEP_AS_NON_CORE (binds BiP ATPase; informative-ish).
- ATPase activator activity (GO:0001671, IEA Ensembl): J domain stimulates BiP ATPase -> ACCEPT (supported
  by PMID:18400946 "stimulate BiP ATPase activity").
- protein binding (GO:0005515, IPI x2 FOXRED2/Q5HYA8): bare term KEEP_AS_NON_CORE.
BP:
- ERAD pathway (GO:0036503, IMP PMID:18400946 / IEA): ACCEPT, CORE BP.
- protein folding in ER (GO:0034975, IDA): ACCEPT.
- response to ER stress (GO:0034976, IDA): KEEP_AS_NON_CORE.
- IRE1-mediated UPR (GO:0036498, IBA): KEEP_AS_NON_CORE.
- intrinsic apoptotic signaling in response to ER stress (GO:0070059, IDA): KEEP_AS_NON_CORE (overexpression).
CC:
- ER lumen (GO:0005788, IBA/IEA/EXP/IDA): ACCEPT.
- ER (GO:0005783, IEA/IDA): ACCEPT.
- ER chaperone complex (GO:0034663, IDA part_of): ACCEPT.
- membrane (GO:0016020, HDA): MARK_AS_OVER_ANNOTATED (soluble ER-lumenal protein; proteomics fraction).
