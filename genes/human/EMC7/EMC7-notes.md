# EMC7 (Q9NPA0) review notes

## Identity and structure
EMC7 (Endoplasmic reticulum membrane protein complex subunit 7; synonyms C11orf3, C15orf24, HT022, UNQ905/PRO1926) is a 242-aa **single-pass type I membrane protein** of the ER and a constitutive subunit of the **ER membrane protein complex (EMC)**.

- Topology (from UniProt FT, PMID:32439656): signal peptide 1-23 (cleaved after Ser-23), **lumenal domain 24-159**, single transmembrane helix 160-180, cytoplasmic tail 181-242 (with a disordered/low-complexity C-terminus 217-242).
  - [file:human/EMC7/EMC7-uniprot.txt "TOPO_DOM        24..159"], [file:human/EMC7/EMC7-uniprot.txt "Lumenal"], [file:human/EMC7/EMC7-uniprot.txt "TRANSMEM        160..180"].
- The lumenal portion forms a **beta-sandwich** ("Beta_sandwich_EMC7", Pfam PF09430 EMC7_beta-sandw; SUPFAM "Starch-binding domain-like"). This carbohydrate-binding-like fold is the basis of the IEA carbohydrate binding annotation, but there is no evidence EMC7 actually binds carbohydrate; the fold is structural.
  - [file:human/EMC7/EMC7-uniprot.txt "Beta_sandwich_EMC7"], [file:human/EMC7/EMC7-uniprot.txt "Starch-binding domain-like"].
- Belongs to the EMC7 family. [file:human/EMC7/EMC7-uniprot.txt "Belongs to the EMC7 family."]

## Core role: EMC complex membership + ER membrane localization
EMC7 is one of ~9 subunits of the EMC, a conserved **co- and post-translational transmembrane-domain insertase/chaperone** of the ER that inserts newly synthesized membrane proteins energy-independently.

- EMC complex membership: [file:human/EMC7/EMC7-uniprot.txt "Component of the ER membrane protein complex (EMC)."]; experimentally identified in the EMC by affinity proteomics [PMID:22119785] and present in cryo-EM EMC structures [PMID:32439656, PMID:32459176].
- Subcellular location: [file:human/EMC7/EMC7-uniprot.txt "Endoplasmic reticulum membrane"]; [file:human/EMC7/EMC7-uniprot.txt "Single-pass type I membrane protein"].
- EMC function (whole-complex): [file:human/EMC7/EMC7-uniprot.txt "enables the energy-independent insertion into endoplasmic\nCC       reticulum membranes of newly synthesized membrane proteins"]; required for cotranslational insertion of multipass membrane proteins and post-translational insertion of tail-anchored (TA) proteins [file:human/EMC7/EMC7-uniprot.txt "required for the\nCC       post-translational insertion of tail-anchored/TA proteins in\nCC       endoplasmic reticulum membranes"].

## EMC7 is a LUMENAL, NON-CATALYTIC subunit
The catalytic insertase machinery (hydrophilic vestibule) is formed by **EMC3 and EMC6** in the membrane (PMID:32439656 abstract: "occurs via an enclosed hydrophilic vestibule within the membrane formed by the subunits EMC3 and EMC6"). EMC7's bulk is a lumenal beta-sandwich plus one TM helix; it is a peripheral/architectural subunit, not the catalytic core.

Therefore for EMC7:
- **CORE = EMC complex membership (GO:0072546) + ER membrane (GO:0005789).**
- The insertase **molecular function** annotations (GO:0032977 membrane insertase activity, `contributes_to`) and the **BP** insertion terms (GO:0045050, GO:0071816) describe the whole-complex activity to which EMC7 contributes; they are correct (note `contributes_to` qualifier is appropriate for a complex member) but the insertase MF should NOT be elevated to EMC7's own core catalytic function. Keep BP insertion terms as genuine EMC-mediated processes EMC7 is involved in.

## protein binding (GO:0005515, IPI) entries
Eight IPI protein-binding annotations from interactome/IntAct screens. Per CLAUDE.md, bare `protein binding` is uninformative -> KEEP_AS_NON_CORE. Partners are recorded in the UniProt IntAct block and in the goa WITH/FROM column:
- PMID:28514442 -> PDIA4 (P13667). [file:human/EMC7/EMC7-uniprot.txt "P13667: PDIA4"]
- PMID:28734904 (Wntless interactome) -> WLS (Q5T9L3-1). [file:human/EMC7/EMC7-uniprot.txt "Q5T9L3-1: WLS"]
- PMID:31286866 (Wntless splicing/PPI) -> WLS (Q5T9L3-1). [file:human/EMC7/EMC7-uniprot.txt "Q5T9L3-1: WLS"]
- PMID:32296183 (HuRI binary interactome) -> CYSRT1 (A8MQ03), NOTCH2NLC (P0DPK4), KRTAP5-9 (P26371), KRTAP1-1 (Q07627), MEOX2 (Q6FHY5), KRTAP5-2 (Q701N4). [file:human/EMC7/EMC7-uniprot.txt "A8MQ03: CYSRT1"]
- PMID:33961781 (BioPlex) -> PDIA4 (P13667). [file:human/EMC7/EMC7-uniprot.txt "P13667: PDIA4"]

WLS (Wntless) is itself an EMC substrate/client, so the WLS interactions plausibly reflect EMC client engagement; the HuRI keratin-associated-protein hits are likely sticky binary Y2H artifacts. None elevate to core; all KEEP_AS_NON_CORE.

## carbohydrate binding (GO:0030246, IEA InterPro)
From the SUPFAM "Starch-binding domain-like"/carbohydrate-binding-like fold (IPR013784). This is a fold-homology electronic inference with no experimental support; EMC7 is not known to bind carbohydrate. Over-propagated IEA -> MARK_AS_OVER_ANNOTATED (or REMOVE-candidate). Using MARK_AS_OVER_ANNOTATED to be conservative.

## membrane (GO:0016020, IDA/NAS)
Generic "membrane" — correct but less informative than ER membrane (GO:0005789). KEEP_AS_NON_CORE / MODIFY to ER membrane is debatable; the IDA (PMID:22119785) is real but generic. Keep as non-core (parent of the specific ER membrane term).

## Annotation tally (21 in goa, deduped from goa.tsv rows 2-28; stub has 21 entries)
- EMC complex (GO:0072546): IBA, IPI (PMID:32439656), IDA (PMID:22119785) — all ACCEPT (CORE).
- ER membrane (GO:0005789): IEA, NAS (PMID:29242231), EXP (PMID:22119785), IDA (PMID:32439656) — ACCEPT (CORE).
- carbohydrate binding (GO:0030246): IEA — MARK_AS_OVER_ANNOTATED.
- protein binding (GO:0005515) x6 IPI rows in stub — KEEP_AS_NON_CORE.
- membrane insertase activity (GO:0032977) x2 IMP contributes_to — KEEP_AS_NON_CORE (whole-complex MF; EMC7 non-catalytic, contributes_to qualifier appropriate).
- protein insertion by stop-transfer (GO:0045050) IDA + 2x IMP — ACCEPT (EMC process; non-core relative to complex membership but a genuine function).
- tail-anchored insertion (GO:0071816) IDA — ACCEPT (EMC process).
- membrane (GO:0016020) IDA + NAS — KEEP_AS_NON_CORE (generic).

## References to verify
All EMC mechanism papers (29242231, 29809151, 30415835, 32439656) have cached full text (32439656 abstract-only). Interaction papers all cached. Per guidelines, do not REMOVE experimental IMP/IDA/IPI just because a cached abstract foregrounds the whole complex; these are complex-member annotations and are appropriate.
