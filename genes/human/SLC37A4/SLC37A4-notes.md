# SLC37A4 (G6PT / G6PT1) — curation notes

UniProtKB: O43826 (G6PT1_HUMAN). Gene: SLC37A4 (HGNC:4061). Synonyms: G6PT, G6PT1,
glucose-6-phosphate translocase, TRG-19. 429 aa, multi-pass ER membrane protein.

Deep research: falcon provider is out of credits (HTTP 402); no
`-deep-research-falcon.md` generated. Review grounded in the UniProt record, seeded
GOA, and cached `publications/PMID_*.md`.

## Core biology (verified)

SLC37A4/G6PT is the **glucose-6-phosphate:inorganic-phosphate antiporter of the ER
membrane**. It moves cytosolic glucose-6-phosphate (G6P) into the ER lumen in exchange
for luminal inorganic phosphate (Pi), delivering the G6P substrate to the luminal
active site of the glucose-6-phosphatase catalytic subunits (G6PC1 in liver/kidney/
intestine; G6PC3 ubiquitously incl. neutrophils). Belongs to the MFS,
organophosphate:Pi antiporter (OPA) family (TC 2.A.1.4).

- Dual G6P/Pi antiporter, reconstituted proteoliposomes: [PMID:18337460 "our results suggest that G6PT has a dual role as a G6P and a P(i) transporter and that GSD-Ib and GSD-Ic are deficient in the same G6PT gene"].
- Physiological ER G6P transporter, couples to G6Pase-α; primary function is to
  translocate G6P from cytoplasm into ER lumen for hydrolysis: [PMID:21949678 "The primary function of G6PT is to translocate G6P from the cytoplasm into the lumen of the ER for hydrolysis into glucose and Pi"]; [PMID:21949678 "only G6PT/SLC37A4 matches the characteristics of the physiological ER G6P transporter"].
- ER-localized multitransmembrane protein required for transporting G6P into ER:
  [PMID:33964207 "SLC37A4 encodes an endoplasmic reticulum (ER)-localized multitransmembrane protein required for transporting glucose-6-phosphate (Glc-6P) into the ER"].
- Import of G6P into ER done by G6PT1, spans membrane; ER retrieval signal (KKXX):
  [PMID:32884905 "Import of glucose-6-phosphate into the ER is done by the glucose-6-phosphate transporter (G6PT1), encoded by the SLC37A4 gene"].
- Original cloning; ER retention motif; liver/kidney expression; associated with
  glucose-6-phosphatase: [PMID:9428641 "This protein presents at its carboxy terminus the consensus motif for retention in the endoplasmic reticulum"], [PMID:9428641 "The encoded protein is therefore most likely the glucose 6-phosphate translocase that is functionally associated with glucose-6-phosphatase"].
- GSD1b caused by inactivation of G6P transport; contributes to neutropenia:
  [PMID:10026167 "mutations uncovered in GSD-1b patients disrupt G6P transport"].
- Signature motif required for microsomal G6P transport:
  [PMID:12560945 "in G6PT the signature motif is a functional element required for microsomal glucose-6-phosphate transport"].

## Isoform 2 (O43826-2, variant vG6PT)

Isoform 2 (VSP_006171; includes a 66-bp exon-7 giving +22 aa in luminal loop 4) is also
an active microsomal G6P transporter and functions in glucose homeostasis:
[PMID:11140953 "we demonstrate that vG6PT is also active in microsomal G6P transport"],
[PMID:11140953 "which works together with glucose-6-phosphatase to maintain glucose homeostasis"].
Note: isoform-specific annotations in GOA (GO:0015152, GO:0015760, GO:0042593 on
O43826-2) reflect what was tested (the variant), not a function unique to isoform 2 —
both isoforms transport G6P.

## Localization

ER membrane, multi-pass, 10–12 TM (UniProt: 12 TM helices resolved by cryo-EM; older
literature says 10). ER retrieval signal at C-terminus. Structures (2025 cryo-EM,
PMID:41136424, PMID:41225049) show monomer, pseudo-two-fold N/C domains, central G6P
pocket; inhibited by chlorogenic acid & vanadate. (These structural PMIDs are not in
GOA and not cached; not used for supporting_text.)
- ER membrane loc, WT resides in ER: [PMID:32884905 "The wildtype protein resides in the ER of HepG2 tetoff cells"].

## Disease

- GSD Ib (MIM:232220): metabolic phenotype (fasting hypoglycemia, hepatomegaly, lactic
  acidemia, hyperlipidemia, hyperuricemia) PLUS neutropenia, neutrophil dysfunction,
  IBD-like features. GSD Ic/Id historically ascribed to a separate Pi transporter are
  now known to be the same G6PT gene (PMID:18337460).
- CDG2W (MIM:619525): dominant, R423* removes ER retention signal → mislocalization to
  Golgi → congenital disorder of glycosylation with liver dysfunction & coagulopathy
  (PMID:32884905, PMID:33964207).

## Annotation review decisions (summary)

- MF GO:0061513 (G6P:Pi antiporter) — the definitive molecular function. Multiple EXP/
  IDA/IBA/TAS. ACCEPT (core). Duplicates all accepted.
- MF GO:0015152 (glucose-6-phosphate transmembrane transporter activity) — correct,
  slightly less informative than the antiporter term but valid. ACCEPT (core).
- MF GO:0022857 (transmembrane transporter activity, IEA/InterPro) — correct but far too
  general given the specific antiporter term. MARK_AS_OVER_ANNOTATED.
- MF GO:0005515 (protein binding, IPI, BIK interaction, PMID:32296183/HuRI) — bare
  protein binding, uninformative; per policy MARK_AS_OVER_ANNOTATED (not REMOVE).
- BP GO:0015760 (glucose-6-phosphate transport) — direct core process. ACCEPT.
- BP GO:0035435 (phosphate ion transmembrane transport) — correct (the antiport moves Pi
  the other way). ACCEPT / KEEP_AS_NON_CORE (the Pi leg is the counter-substrate).
- BP GO:0006094 (gluconeogenesis, TAS Reactome) & GO:0006006 (glucose metabolic process,
  NAS) — SLC37A4 enables the terminal step of both gluconeogenesis and glycogenolysis by
  supplying G6P to G6Pase; these are legitimate but broad process roles.
  KEEP_AS_NON_CORE (contributory, not the molecular function).
- BP GO:0042593 (glucose homeostasis, IDA on isoform 2) — central physiological role.
  ACCEPT / core-adjacent.
- BP GO:0055085 (transmembrane transport, IEA) — correct but general. KEEP_AS_NON_CORE.
- CC GO:0005789 (ER membrane) — correct, well supported (IDA, EXP, IBA, IEA, TAS). ACCEPT.
- CC GO:0005783 (ER, NAS) — correct but less specific than ER membrane. KEEP_AS_NON_CORE.
- CC GO:0016020 (membrane, IEA/HDA/NAS) — trivially true, far less specific than ER
  membrane. MARK_AS_OVER_ANNOTATED.
</content>
</invoke>
