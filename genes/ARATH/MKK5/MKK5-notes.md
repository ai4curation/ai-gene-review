# MKK5 curation notes

Session 2026-10-06, added for the stomatal_lineage_development module (where MKK4/MKK5 are representative members of the redundant MAPKK step). Fetched by accession (Q8RXG3, alias MKK5); UniProt entry verified (M2K5_ARATH, At3g21220). Falcon deep research not attempted (provider returned HTTP 402 for all other genes this session).

## Key findings
- MKK4/MKK5 act downstream of YODA and upstream of MPK3/MPK6 in stomatal development [PMID:17259259 "We further establish that the MKK4/MKK5-MPK3/MPK6 module is downstream of YODA, a MAPKKK."]; loss gives clustered stomata, activation abolishes stomatal fate [PMID:17259259 "Loss of function of MKK4/MKK5 or MPK3/MPK6 disrupts the coordinated cell fate specification of stomata versus pavement cells, resulting in the formation of clustered stomata."].
- YDA phosphorylates MKK4 [PMID:22307275 "BIN2 phosphorylates YDA to inhibit YDA phosphorylation of its substrate MKK4"]; MAPKKK5 phosphorylates MKK4/MKK5 activation loops [PMID:27679653].
- Immune MAPK cascade downstream of FLS2 [PMID:11875555 "Here we identify a complete plant MAP kinase cascade (MEKK1, MKK4/MKK5 and MPK3/MPK6)..."].
- Inflorescence architecture downstream of ERECTA [PMID:23263767]; floral organ abscission downstream of HAE/HSL2 [PMID:18809915].
- AIK1-MKK5-MPK6 ABA module [PMID:27913741 "Bimolecular fluorescence complementation analysis showed that MPK3, MPK6, and AIK1 interact with MKK5."]; MEK5(DD) induces ethylene and HR-like death [PMID:18268539].

## Curation decisions
- Core MF: MAP kinase kinase activity (GO:0004708, IEA accepted; EXP Ser/Tyr kinase rows accepted).
- NEW: negative regulation of stomatal complex development (IGI, PMID:17259259).
- Mitochondrion ISM MARK_AS_OVER_ANNOTATED; cell division IMP MARK_AS_OVER_ANNOTATED (regulatory, not participatory); stress granule kept non-core.
- Protein binding: MPK3/MPK6 rows MODIFIED to MAP kinase binding; AIK1 and MAPKKK5 to MAPKKK binding; BASL, SLOMO, ILK4 REMOVED.

## 2026-10-09: combined with independent review

Reconciled with an independent review written from the chitin-perception angle (PR 4451). Rows were matched by term, evidence code and reference; 29 of 40 GOA rows already agreed.

Decisions changed relative to the previous version of this file:
- GO:0106310 protein serine kinase activity (EXP PMID:11875555; IEA GO_REF:0000116): ACCEPT -> MODIFY to GO:0004708 MAP kinase kinase activity. The demonstrated activity is dual Thr/Tyr phosphorylation of the MPK3/MPK6 TEY loop; the serine label comes from the EC 2.7.12.2 -> Rhea expansion (UniProt CATALYTIC ACTIVITY lists Ser, Thr and Tyr Rhea reactions, all EC 2.7.12.2 citing PMID:11875555). The same issue is raised as a question.

Kept from the previous version (other review disagreed):
- The 6 MPK3/MPK6/MAPKKK interaction rows stay MODIFY to MAP kinase binding (GO:0051019) / MAPKKK binding (GO:0031435), in line with the MKK4 review; the other review removed all 9 protein-binding rows. The disagreement is recorded in suggested_questions.
- Mitochondrion ISM stays MARK_AS_OVER_ANNOTATED (the other review had REMOVE). Checking PMID:19516975 showed that MKK5 really does have an N-terminal sequence predicted as a chloroplast transit peptide [PMID:19516975 "at least two members, MKK4 and MKK5, were predicted to contain a chloroplast transit sequence"], so a claim of "no targeting peptide" does not hold. Organellar import of MKK5 itself has not been tested. Note: PMID:19516975 is an MKK4 chloroplast-import paper. It is cited only for background (MKK4/5 dually phosphorylate MPK3/6) and for this prediction.
- Cell division IMP stays MARK_AS_OVER_ANNOTATED (the other review had KEEP_AS_NON_CORE, matching MPK6): MKK5 regulates root cell division and does not take part in it.
- Defense response to other organism (IBA/IEA/IMP) stays ACCEPT, matching MKK4. Immune signalling is a principal role of the MKK4/MKK5 pair. The other review kept these rows as non-core.
- NEW GO:2000122 negative regulation of stomatal complex development (IGI PMID:17259259) is kept. The stomatal_lineage_development module annotates the MKK4/MKK5 annoton with it, and MKK4 carries the same NEW row. Participation: MKK5 performs the YODA -> MPK3/MPK6 phosphorylation relay step.

Merged from the other review: description detail on Thr-215/Ser-221 activation and the MAPKKK3/MAPKKK5 immune heads; the CERK1-PBL27-MAPKKK5 chitin evidence and PMID:35652263 added to the immune core function; suggested questions on GO:0002752 PRR signalling (left as a question, for consistency with MKK4/MPK3/MPK6; MAPKKK5 has it via a curator IGI) and on camalexin regulation (GO:1901183; supported by gain of function only [PMID:18378893 "DEX treatment of GVG-MKK4 DD or GVG-MKK5 DD Arabidopsis plants also led to camalexin induction"]); a question on the ABA-specific role of MKK5; two experiments (phosphosite mapping; conditional MKK4 depletion in mkk5). The falcon deep-research quote was re-checked against the repo copy and is verbatim.

Provenance carried over from the other review's notes:
- MAPKKK5 phosphorylates MKK5 directly [PMID:27679653 "The kinase domain of MAPKKK5 directly phosphorylated MKK4K108R and MKK5K99R (Fig 8B)"]
- Cytosolic site of MAPKKK5-MKK5 interaction [PMID:27679653 "MAPKKK5 interacts with MKK2, MKK4, and MKK5 mainly in the cytosol"]
- AIK1 activates MKK5 [PMID:27913741 "AIK1 was localized in the cytoplasm and shown to activate MKK5 by protein phosphorylation"]
- YDA-MKK4/MKK5-MPK3/MPK6 in inflorescence [PMID:23263767 "the YDA-MKK4/MKK5-MPK3/MPK6 cascade functions downstream of the ER receptor in regulating localized cell proliferation"]
