# PA3760 (Q9HXN5) notes

## Identity

- UniProt Q9HXN5 (TrEMBL, unreviewed, PE 3), 842 aa, locus PA3760, no gene
  name. Fetched accession matches the worklist entry (rank 23). The folder is
  named by locus tag.
- Multidomain fused PTS protein: an N-terminal EIIA (glucose type,
  PS51093 PTS EIIA type-1, residues 24-128, active-site His76), an HPr
  domain (PS51350, residues 173-261, with HPr His and Ser sites PS00369 and
  PS00589), and a full-length Enzyme I (PTS_EIN PF05524, PEP-utilizers
  PF00391, PEP-utilizers_C PF02896, NCBIfam TIGR01417 PTS_I_fam). PANTHER
  PTHR46244:SF6. TCDB 4.A.1.1.15 (PTS glucose-glucoside family).
- This is the EI/HPr/EIIA partner of PA3761 (EIIBC). The two genes sit at
  the end of a glucosamine-utilisation operon. PAO1 has two other EI-type
  proteins: FruI (PA3562, the fused EI/HPr/EIIA of the fructose PTS) and PtsP
  (EI-Ntr).

## Literature

- Johnson et al. 2008 (PMID:18833300, full text). This is the only functional
  study of PA3760. It used a PathoGenesis Mini-Tn5 mutant in strain PAK and
  ran a Biolog screen with plate confirmation.
  [PMID:18833300 "The second cluster of PTS genes encodes a putative fused enzyme I/HPr/enzyme IIA and a putative enzyme IIBC. These two genes are located at the end of a putative operon encoding glucosamine utilization genes, suggesting N-acetylglucosamine as a potential substrate for the PTS transporter."]
  [PMID:18833300 "Knockouts in either PA3760 or PA3761 were defective in growth on N-acetylglucosamine as a sole carbon source, based on both Biolog and growth data (Table 2)."]
  [PMID:18833300 "As for the fructose PTS genes, expression of the N-acetylglucosamine PTS genes was induced by their apparent transported substrate (Table 3)."]
  qRT-PCR showed 5.2-fold induction of PA3760 by GlcNAc (Table 3). Table 2
  lists the PA3760 mutant as unable to grow on N-acetyl-D-glucosamine.
- PubMed searches (PA3760, nagF/nagE, P. aeruginosa N-acetylglucosamine PTS)
  found no other study of this protein.

## Interpretation

- The genetic phenotype (no growth on GlcNAc), the substrate induction and the
  operon context all agree, and PA3760 has the domains needed to phosphorylate
  an EIIBC. Participation in GlcNAc uptake through the PTS is therefore well
  supported for PA3760. The protein does part of the work: it relays the
  phosphoryl group from PEP through EI, HPr and EIIA to the PA3761 EIIBC,
  which phosphorylates GlcNAc during translocation. FruI is still present in
  the PA3760 mutant but does not substitute, so PA3760 is the EI for this
  system.
- A Tn5 insertion in PA3760 could also be polar on PA3761. That does not
  matter for the claim, because both are subunits of the same PTS.
- The electronic "kinase activity" row is a keyword mapping. In GO,
  PEP-protein phosphotransferase activity (EC 2.7.3.9) sits under
  "phosphotransferase activity, nitrogenous group as acceptor", not under
  kinase activity.

## PseudoCAP IBA-seed assessment

PTN000532509 is an Enzyme I node that also carries a GO:0008965 IBD seeded by
E. coli PtsI (P08839) and E. coli PtsP (P37177, EI-Ntr). Its 43 GO:0015764 leaf
IBAs (25 taxa) include general PtsI proteins (E. coli, Salmonella, B. subtilis,
S. aureus, Streptococcus, Chlamydia, Mycoplasma, Neisseria and others), the
nitrogen-PTS PtsP/EI-Ntr proteins (E. coli, Salmonella, Yersinia, Geobacter,
Shewanella, Bradyrhizobium, Coxiella, and P. aeruginosa G3XD36), multiphosphoryl
transfer proteins dedicated to other sugars (FruB, E. coli FryA and PtsA),
P. aeruginosa FruI, and PA3760.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000532509 | GO:0015764 N-acetylglucosamine transport | 1 (sole) | 43 (25 taxa) | GO:0015764, IMP, PMID:18833300 (PseudoCAP) | OVER-SPECIFIC | The seed is sound for PA3760: no growth on GlcNAc, GlcNAc induction and the operon context agree. The node term does not fit the clade. Enzyme I is a general PTS component, so a single sugar substrate is arbitrary for general PtsI. EI-Ntr (PtsP) works in the nitrogen-regulatory PTS, not sugar uptake. FruB, FryA, PtsA and P. aeruginosa FruI belong to systems for other sugars. FruI cannot replace PA3760 for GlcNAc growth, and the FruI mutant is defective only on fructose. The IBD should be withdrawn, or moved to a node confined to the GlcNAc-dedicated fused EIIA-HPr-EI clade if one exists. |

A GO_CENTRAL source defect is filed on the IBA row (CHECK: withdraw or
re-place the IBD). The PseudoCAP IMP row itself is correct, so no PseudoCAP
defect is filed.

## Decisions summary

- ACCEPT: PEP-protein phosphotransferase activity (IBA, IEA); N-acetylglucosamine
  transport (IMP, IBA, the latter with a GO_CENTRAL node defect); PTS
  (IEA); cytoplasm (IEA).
- MODIFY: kinase activity, transferase activity, and transferase activity
  transferring phosphorus-containing groups (IEA) -> PEP-protein
  phosphotransferase activity.

## Leaf evidence check (2026-11-06)

Audit of the `GO_CENTRAL` defect on PTN000532509, which previously argued from
what the other leaves of the Enzyme I node are *called*. Leaf membership
confirmed with `panther_tree.py node PTN000532509 --leaves` (43 leaves, 25
taxa); UniProt entries fetched from `rest.uniprot.org`.

| Leaf | Name and its evidence | Experimental annotations found | Verdict |
|---|---|---|---|
| P08839 (E. coli ptsI) | Curated `RecName` "Phosphoenolpyruvate-protein phosphotransferase", ECO:0000303|PubMed:2960675; EC 2.7.3.9 ECO:0000269|PubMed:12705838 | `GO:0008965` EXP; `GO:0005737` EXP; `GO:0005829` HDA; `GO:0042802` IPI. Curated FUNCTION with ECO:0000269 ×3 states it is the "General (non sugar-specific) component" of the PTS | SURVIVES, and is now the strongest claim: experimentally non-sugar-specific, so it cannot inherit a GlcNAc-specific process |
| P37177 (E. coli ptsP, EI-Ntr) | Curated `RecName`, ECO:0000303|PubMed:8973315; EC 2.7.3.9 ECO:0000269|PubMed:10473571 | `GO:0008965` IDA:EcoCyc; `GO:0006468` IDA:EcoCyc | SURVIVES. The EI-Ntr identity is additionally a domain fact: GAF domain (Pfam PF01590, PROSITE PS50813) absent from PtsI |
| Q9HY55 (P. aeruginosa PA3562, "fruI") | `RecName` and EC from **ARBA** (ECO:0000256|ARBA:ARBA00012232) — a predicted name; gene name `fruI` is ECO:0000313|EMBL (submitter) | None in UniProt (all IEA/IBA/UniRule). **But** PMID:18833300, the paper that seeds this IBD, reports the PA3562 knockout failing to grow on D-fructose and fructose induction of the gene | SURVIVES on the experiment, not the name. Same subfamily (PTHR46244:SF6) and same organism as PA3760, yet dedicated to a different sugar |
| P77439 (E. coli fryA, MTP 1) | `RecName` ECO:0000305|PubMed:11361063; PE 1 | No experimental GO; `GO:0008965` ISS | Name claim dropped. Retained claim is the domain fact: type-2 fructose-class EIIA (PF00359, PS51094, IPR004715 `PTS_IIA_fruc`) + HPr + EI |
| P32670 (E. coli ptsA, MTP 2) | `RecName` ECO:0000303|PubMed:7773398; PE 3 | None; `GO:0008965` ISS, two NAS rows from ComplexPortal | As above — domain fact only |
| P45597 (X. campestris fruB) | `RecName` ECO:0000303|PubMed:7496537; PE 3 | None; `GO:0008965` ISS | As above — domain fact only |

PA3760 itself (Q9HXN5) carries a **type-1** PTS EIIA domain (Pfam PF00358,
PROSITE PS51093, PS00371), while all four fused multiphosphoryl leaves carry
the **type-2** fructose-class EIIA; P08839 and P37177 carry no EIIA or HPr
domain at all. That domain split, not the names `fruB`/`ptsA`/`fruI`, is what
the node-level objection now rests on, together with the PA3562 growth
phenotype and the experimental non-specificity of E. coli PtsI.

Confidence raised PROBABLE -> CONFIRMED: PMID:18833300 is cached full text and
states the decisive PA3562 fact outright, and the domain content is primary
data checked here.
