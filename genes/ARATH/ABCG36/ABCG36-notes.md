# ABCG36 (PEN3 / PDR8 / At1g59870; UniProt Q9XIE2) — curation notes

## Identity
Full-size PDR-type ABCG transporter (two NBD + TMD modules, reverse topology). Synonyms PEN3,
PDR8. Plasma-membrane resident; enriched at the outer lateral domain of root epidermal cells and
focally recruited to fungal penetration sites/papillae in leaves.

## Molecular function (what it transports)
- Camalexin: direct ATP-dependent export [PMID:37146609 "we provide evidence that ABCG36 catalyzes the direct, ATP-dependent export of camalexin across the plasma membrane"].
- IBA (auxin precursor) efflux [PMID:19648296 "We found that pdr8 mutants display defects in efflux of the auxin precursor IBA"]; redundant with ABCG37 [PMID:20498067 "ABCG37 and its homolog ABCG36 act redundantly at outermost root plasma membranes and, unlike established IAA transporters from the PIN and ABCB families, transport IBA out of the cells."]. Wild-type does not export IAA (deep research, Aryal 2019; file:ARATH/ABCG36/ABCG36-deep-research-falcon.md).
- Indole-glucosinolate (PEN2 pathway) products: [PMID:26023163 "This metabolic pathway directs the intracellular biosynthesis and activation of tryptophan-derived indole glucosinolates for subsequent PEN3-mediated efflux across the plasma membrane at pathogen contact sites."]; 4MeOI3M shown as substrate by Matern 2019 (deep research; not cached).
- Cadmium: [PMID:17355438 "these data strongly support a role for AtPDR8 as an efflux pump of Cd(2+) or Cd conjugates at the plasma membrane of Arabidopsis cells"]. Species unresolved.
- Substrate preference switch: [PMID:37146609 "Phosphorylation of ABCG36 by QSK1 unilaterally represses IBA export, allowing camalexin export by ABCG36 conferring pathogen resistance."]
- Ca2+ sensor interactions (CaM7 etc.) [PMID:26315018 "we confirmed PEN3-CaM interaction in vitro and in vivo by PEN3 pull-down with CaM Sepharose, CaM overlay assay and bimolecular fluorescence complementation"].

## Localization
- PM [PMID:16473969 "PEN3/PDR8 tagged with green fluorescent protein localized to the plasma membrane in uninfected cells. In infected leaves, the protein concentrated at infection sites."]
- Cycles through TGN [PMID:28434950 "We provide evidence that PEN3 undergoes continuous endocytic cycling from the PM to the trans-Golgi network (TGN)."]
- ER only as biosynthetic transit (EAP3 needed for ER exit) [PMID:29085068 "specifically mediates PEN3 exit from the endoplasmic reticulum"].
- Not vacuole [PMID:19095898 "PEN3 localizes to the plasma membrane, not the vacuole"]; NOT chloroplast (TAIR IDA negation). Mitochondrial/chloroplast/vacuolar proteomics hits are likely contaminants.

## Biological roles
- Pre-invasive (nonhost) defense vs fungi: Blumeria, E. pisi, P. cucumerina, Colletotrichum, Phakopsora, Fusarium (PMIDs 16473969, 20605856, 26315018, 29085068, 37146609).
- Oomycetes and Pseudomonas (PMIDs 16473969, 24889055, 23815470) — same export mechanism, secondary.
- Recruitment to penetration sites triggered by PAMP perception (flg22, chitin) via PRRs [PMID:23836668]. ABCG36 is a downstream cargo, not a component of the PRR signaling pathway.
- pen3 SA hyperactivation, chlorosis and resistance to adapted E. cichoracearum are secondary [PMID:16473969 "intracellular accumulation of these toxins in pen3 may secondarily activate the salicylic acid pathway"].
- Root IBA homeostasis: root hair, cotyledon expansion, lateral root phenotypes are indirect consequences of reduced IBA efflux (IBA->IAA conversion required) [PMID:19648296].
- Drought/salt tolerance from overexpression (Na content) [PMID:20088904] — indirect.
- Root exudation of thymidine (pdr8) and coumarins (mostly ABCG37) [PMID:28623273] — exudation phenotypes, not metabolic processes.

## Curation decisions summary
- Core: ATP-dependent export of indolic defense metabolites (camalexin, IGS products) at PM/penetration sites -> defense response to fungus; IBA (auxin) efflux at the root epidermis PM.
- protein binding (CaM/CML/CBL4/KIC IPIs) -> MODIFY to calmodulin binding.
- Over-annotations: development terms (cotyledon, root, root hair), coumarin/thymidine metabolic process, indole glucosinolate catabolic process (PEN2 catalyses), PAMP receptor signaling pathway, SAR, negative regulation of defense response, heat (RNA-seq), mRNA binding (RIC), organelle proteomics HDA.
- Mitochondrion ISM prediction removed (contradicted by experimental PM localization).
- PMID:16877699 (PDR9/ABCG37 paper) supports "export from cell" only via background mention of pdr8; function itself is correct for ABCG36, kept.
- Necessity vs participation (project Q3): ABCG36 does perform a step of the defense response (export of antimicrobial indolics), so defense response to fungus is retained as core; the more mechanistic activity is captured by the transporter MF (ABC-type indole transporter activity). No GO term exists for camalexin/glucosinolate-product export.
