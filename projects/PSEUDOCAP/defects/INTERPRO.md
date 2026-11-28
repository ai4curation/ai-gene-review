# Source-record defects for INTERPRO

9 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** InterPro:IPR004136
- **Subject:** UniProtKB:Q9I4V0
- **Field:** GO_ID
- **Change:** check GO:0018580 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA1024/PA1024-ai-review.yaml`

The InterPro2GO mapping IPR004136 (NMO) -> GO:0018580 nitronate monooxygenase activity (resource InterPro / InterPro2GO) puts NMO activity on PA1024 (Q9I4V0). Ball et al. 2016 (PMID:27502282) showed that the purified enzyme lacks NMO activity and is an NADH:quinone reductase. The authors report that this NQR class covers more than 490 sequences in the NMO family. Restrict the mapping, for example by moving it to a subfamily-level entry for true NMOs, or by suppressing it for PA1024-like sequences. A NOT annotation to GO:0018580 on Q9I4V0, citing PMID:27502282, would also be justified.

> which define a new class of NADH:quinone reductases and are present in more than 490 hypothetical proteins in the GenBank
> — PMID:27502282

## 2. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** InterPro:IPR000667
- **Subject:** UniProtKB:Q9HZG1
- **Field:** interpro2go
- **Change:** remove GO:0006508 from interpro2go
- **Recorded in:** `genes/PSEAE/PA3047/PA3047-ai-review.yaml`

Resource is InterPro (InterPro2GO; assigned_by InterPro in GOA). The InterPro2GO mapping of IPR000667 (Peptidase S13) to GO:0006508 proteolysis is applied to this low-molecular-mass penicillin-binding protein, whose substrate is peptidoglycan (stem peptides and crosslinks), not protein. The signature records the serine D,D-peptidase fold; the mapping should be reviewed for the PBP members of the entry.

## 3. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** InterPro:IPR017783
- **Subject:** UniProtKB:Q9HTH6
- **Field:** GO ID
- **Change:** delete the record asserting GO:0015871
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/Q9HTH6/Q9HTH6-ai-review.yaml`

InterPro2GO maps IPR017783 (ABC_choline_sub-bd, NCBIfam TIGR03414) to choline transport. The signature also matches the carnitine-specific CaiX proteins, so the InterPro mapping over-applies the choline substrate.

## 4. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** InterPro:IPR017783
- **Subject:** UniProtKB:Q9HTH6
- **Field:** GO ID
- **Change:** GO:0033265 → GO:0050997
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/Q9HTH6/Q9HTH6-ai-review.yaml`

InterPro2GO maps IPR017783 (ABC_choline_sub-bd) to choline binding. The signature also matches carnitine-specific CaiX, which does not bind choline.

## 5. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** InterPro:IPR006108|InterPro:IPR006176|InterPro:IPR022694
- **Subject:** UniProtKB:Q9HTH8
- **Field:** GO ID
- **Change:** delete the record asserting GO:0006631
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cdhA/cdhA-ai-review.yaml`

InterPro2GO maps IPR006108/IPR006176/IPR022694 (3-hydroxyacyl-CoA dehydrogenase domains) to fatty acid metabolic process. The L-carnitine dehydrogenase subfamily (IPR026578, HAMAP MF_02129) shares these domains but does not act on fatty acids; the InterPro mapping should exclude it.

## 6. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** InterPro:IPR008567
- **Subject:** UniProtKB:Q9HTH7
- **Field:** GO ID
- **Change:** GO:0043720 → GO:0016747
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/cdhC/cdhC-ai-review.yaml`

InterPro2GO maps IPR008567 (BKACE) to the substrate-specific 3-keto-5-aminohexanoate cleavage activity, but the family is substrate-diverse; members such as CdhC act on 3-dehydrocarnitine. The InterPro mapping should use a substrate-neutral parent.

## 7. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** InterPro:IPR003481
- **Subject:** UniProtKB:Q9K3C5
- **Change:** check GO:0009424 (alternatives in the explanation)
- **Likely cause:** LEGACY_ALIAS
- **Recorded in:** `genes/PSEAE/fliD/fliD-ai-review.yaml`

InterPro2GO (resource: InterPro; GO_REF:0000002) maps IPR003481 (FliD_N, the N-terminal domain of the flagellar cap protein FliD) to GO:0009424 bacterial-type flagellum hook. FliD forms the cap at the distal tip of the filament; the hook-filament junction proteins are FlgK (HAP1) and FlgL (HAP3), and GO:0009424 is defined as the portion of the flagellum connecting filament to basal body. The legacy name "hook-associated protein 2" is the likely source of the mapping, which appears on every FliD entry (for example P24216, P16328, P39738, Q9K3C5). Please review and either retire the mapping or point it at GO:0009421, which IPR040026 already maps to. (FliD has been observed at the distal end of the hook-basal body in filament-less Salmonella mutants, which is why this is raised as a query rather than a straight deletion.)

> A FliD (also called HAP2) oligomer forms the cap protein complex that is located at the tip of the flagellar filament (Yonekura et al.
> — PMID:27664419

## 8. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** InterPro:IPR028359
- **Subject:** UniProtKB:G3XD94
- **Change:** GO:0016628 → GO:0016616 (oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpA/wbpA-ai-review.yaml`

InterPro2GO: IPR028359 (UDP-ManNAc/GlcNAc dehydrogenase) maps to GO:0016628 (CH-CH group of donors). Family members (WbpA EC 1.1.1.136, WecC EC 1.1.1.336) oxidise the C6 hydroxymethyl group of the sugar, a CH-OH donor. The mapping should be GO:0016616.

## 9. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** InterPro:IPR007812
- **Subject:** UniProtKB:P25060
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0009276
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/xcpY/xcpY-ai-review.yaml`

The InterPro2GO mapping of IPR007812 (T2SS protein GspL) includes GO:0009276 Gram-negative-bacterium-type cell wall. That term is a subclass of GO:0009274 peptidoglycan-based cell wall, so it asserts location in the peptidoglycan layer. GspL proteins are bitopic inner-membrane subunits of the type II secretion assembly platform: for P. aeruginosa XcpY (P25060) the topology was mapped experimentally (PubMed:8763961) as cytoplasmic 1-233, transmembrane 234-254 and periplasmic 255-382, and the family is described throughout as an inner-membrane component. Please remove GO:0009276 from the IPR007812 mapping; GO:0005886 plasma membrane and GO:0015627 type II protein secretion system complex already cover the location correctly.

> SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:8763961}; CC Single-pass membrane protein {ECO:0000269|PubMed:8763961}.
> — file:PSEAE/xcpY/xcpY-uniprot.txt
