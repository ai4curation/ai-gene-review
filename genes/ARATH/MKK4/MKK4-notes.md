# MKK4 curation notes

Session 2026-10-06, added for the stomatal_lineage_development module (where MKK4/MKK5 are representative members of the redundant MAPKK step). Fetched by accession (O80397, alias MKK4); UniProt entry verified (M2K4_ARATH, At1g51660). Falcon deep research not attempted (provider returned HTTP 402 for all other genes this session).

## Key findings
- MKK4/MKK5 act downstream of YODA and upstream of MPK3/MPK6 in stomatal development [PMID:17259259 "We further establish that the MKK4/MKK5-MPK3/MPK6 module is downstream of YODA, a MAPKKK."]; loss gives clustered stomata, activation abolishes stomatal fate [PMID:17259259 "Loss of function of MKK4/MKK5 or MPK3/MPK6 disrupts the coordinated cell fate specification of stomata versus pavement cells, resulting in the formation of clustered stomata."].
- YDA phosphorylates MKK4 [PMID:22307275 "BIN2 phosphorylates YDA to inhibit YDA phosphorylation of its substrate MKK4"]; MAPKKK5 phosphorylates MKK4/MKK5 activation loops [PMID:27679653].
- Immune MAPK cascade downstream of FLS2 [PMID:11875555 "Here we identify a complete plant MAP kinase cascade (MEKK1, MKK4/MKK5 and MPK3/MPK6)..."].
- Inflorescence architecture downstream of ERECTA [PMID:23263767]; floral organ abscission downstream of HAE/HSL2 [PMID:18809915].
- Non-canonical chloroplast stromal import of MKK4 [PMID:19516975] - kept non-core.

## Curation decisions
- Core MF: MAP kinase kinase activity (GO:0004708). IDA from PMID:9878570 accepted deferring to curator (abstract only, centred on MKK2/MEK1).
- NEW: negative regulation of stomatal complex development (IGI, PMID:17259259) - MKK4 performs the phosphorylation relay step, so it does part of the work.
- Protein binding: MPK3/MPK6 rows MODIFIED to MAP kinase binding; MAPKKK5 row to MAPKKK binding; BRX, MYB73, KNAT1, TIFY8, ILK4 rows REMOVED.

## 2026-10-09: combined with independent review

Reconciled this review with an independent review written from the chitin-perception angle (PR 4451). Both reviews used the same GOA file (40 rows), so every row matched. Rows where the decision changed relative to this file:

- **nucleus** (HDA PMID:15610358, IEA GO_REF:0000044, ISM GO_REF:0000122): ACCEPT -> KEEP_AS_NON_CORE. The nuclear GFP signal is credible, but the activating MAPKKK-MKK4 step is mainly cytosolic [PMID:27679653 "MAPKKK5 interacts with MKK2, MKK4, and MKK5 mainly in the cytosol"]. Nucleus removed from the core_functions locations.
- **pollen-pistil interaction** (IGI PMID:32890733): KEEP_AS_NON_CORE -> UNDECIDED. The cached record is abstract-only, and the abstract names MKK1/2/3/7/9 + MPK3/MPK4. The WITH/FROM list is MKK1 (AT4G26070), MKK2 (AT4G29810), MKK7 (AT1G18350), MKK9 (AT1G73500), MPK3 (AT3G45640) and AT1G51660 (MKK4 itself), with no MKK3 (AT5G40440). That points to a possible MKK3/MKK4 identifier swap, but the full text cannot be checked, so the row is left UNDECIDED (not removed) and raised as a question.
- **protein serine kinase activity** (IEA RHEA:17989): ACCEPT -> MODIFY to GO:0004708 MAP kinase kinase activity. This is an EC 2.7.12.2 expansion artefact: MKK4 phosphorylates the Thr/Tyr of the MPK3/MPK6 activation loop, and no serine-directed substrate activity is documented.

Disagreements resolved in favour of this file:
- **Protein binding IPI rows with MPK3/MPK6 or MAPKKK5 as partner** (8 rows): the other review REMOVEd all 13 protein binding rows. I kept the MODIFY to GO:0051019 MAP kinase binding / GO:0031435 MAPKKK binding. The annotation-reviewer policy prefers MODIFY when the paper supports a more informative MF, these interactions are the functional docking partners of the cascade, and the MKK5 review on main makes the same choice. The other 5 rows (BRX, MYB73, KNAT1, TIFY8, ILK4/AT3G58760) are REMOVEd in both reviews.
- **defense response to other organism** (IBA, IEA, IMP PMID:11875555): the other review used KEEP_AS_NON_CORE; I kept ACCEPT. PRR-triggered immune signalling is one of the two principal roles of the MKK4/MKK5 pair, directly shown in PMID:11875555 and PMID:35652263, and the MKK5 review on main also ACCEPTs it.
- **NEW GO:2000122 negative regulation of stomatal complex development** (IGI PMID:17259259): kept. It is used by the stomatal_lineage_development module. MKK4 performs a phosphorylation step of the relay, so it does part of the work. Comparators: EPF2 carries it in GOA, and the YDA and ERECTA reviews carry it.

Additions from the other review:
- Core function evidence for the chitin branch [PMID:27679653 "a possible phospho‐signaling pathway consisting of CERK1–PBL27–MAPKKK5–MKK4/MKK5–MPK3/MPK6"], MKK4DD specificity for MPK3/MPK6 [PMID:18378893], and the YDA vs MAPKKK3/5 split [PMID:35652263].
- Camalexin rests on gain-of-function evidence only [PMID:18378893 "DEX treatment of GVG-MKK4 DD or GVG-MKK5 DD Arabidopsis plants also led to camalexin induction"]. As a result, no camalexin term and no cell surface PRR signalling term (GO:0002752) were added; both are raised as questions, consistent with MKK5/MPK3/MPK6.
- Activation-loop sites T-224/S-230 [PMID:27679653 "Therefore, we substituted the S/TxxxxxS/T motif residues, T‐224/S‐230 of MKK4 and T‐215/S‐221 of MKK5 with alanine."].
- Wound-induced ethylene (Li et al. 2018, from deep research; not cached): the mkk4 knockdown has a small effect compared with mkk5. No term was added.
- Chloroplast stroma stays non-core (in vitro import into pea chloroplasts only). This is supported by a quote from the repo deep-research file, re-checked verbatim.
