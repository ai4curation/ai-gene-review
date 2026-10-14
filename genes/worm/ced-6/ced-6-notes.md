# ced-6 notes

## Deep research status (2026-10-05)

No provider deep-research file exists for this gene. Providers were unavailable in this environment (Falcon returned 402, the OpenAI key was invalid, perplexity was not installed), as for ced-1 and MEGF10. The synthesis below was made by hand from cached publications. Every claim carries an inline citation and quote.

## Identity

- UniProtKB:O76337 (F56D2.7), the orthologue of human GULP1. It has an N-terminal PTB domain and a proline/serine-rich C-terminal half [PMID:9635426 "The CED-6 protein contains a phosphotyrosine binding domain at its N terminus and a proline/serine-rich region in its C-terminal half"].
- It dimerizes [PMID:10734103 "we demonstrate that CED-6 dimerizes through a leucine zipper domain that is immediately adjacent to the PTB domain"].
- PANTHER: UniProt and PANTHER's own classification agree, placing it in PTHR11232:SF77 (unlike ced-1). Its IBA engulfment node in the module is PTN000132688.

## Core: CED-1 signaling adaptor in engulfing cells

- It acts in the engulfing cell [PMID:9635426 "Genetic mosaic analysis demonstrates that ced-6 acts within engulfing cells"].
- Its PTB domain binds the NPXY motif of CED-1 [PMID:11729193 "The phosphotyrosine binding domain of GULP was necessary and sufficient for this interaction"]. This was confirmed with point mutants [PMID:35929733 "The CED-6 and CED-1-CT interaction depends on CED-1-CT NPXY motif and the CED-6 PTB domain"].
- Actin reorganization [PMID:15744306 "CED-1, CED-6 and CED-7 are required for actin reorganization around the apoptotic cell corpse"].
- Clathrin/AP2 hub [PMID:23696751 "the CED-6 adaptor protein directly interacts with CHC-1 and individual components of the AP2 complex"]. The authors' model is an actin hub, not vesicle cargo loading [PMID:23696751 "we propose that the formation of a protein complex by CED-1, CED-6, AP2 and CHC-1 provides a hub for recruitment and assembly of actin for cell corpse engulfment"].
- Receptor turnover [PMID:35929733 "These results indicate that CED-6 mediated recruitment of TRIM-21 to the AC surface."].

## Death-promoting role (non-core)

- Engulfment genes promote death of weakly signalled cells [PMID:11449278 "mutations in engulfment genes enhance the frequency of this cell survival"]. Also [PMID:11449279 "can also function to actively kill cells"].
- The Denning 2013 and Chen 2013 (CED-8) papers use ced-6(n2095) only as a clearance-defective background [PMID:23505386 "we used mutations (e.g., ced-1(e1735), ced-6(n2095) or ced-7(n1996)) that cause defects in cell-corpse engulfment and result in the persistence of many embryonic cell corpses into larval stages"]. This is the background-genotype variant of the clearance-defect pattern in `projects/APOPTOSIS/ASSAY_READOUT_OVERANNOTATION.md`.
- 6-OHDA neurodegeneration [PMID:29346382 "We found that mutation in ced-6, in contrast to mutation in ced-2, led to a measurable suppression of dopaminergic neurodegeneration in the ttr-33 mutant background"]. This is not annotated in GOA and is not proposed: it is a consequence of the engulfment role.

## Wnt paper (Cabello 2010)

- The spindle, left/right and DTC IGIs with mom-5 are over-annotations. The paper reports a role for the CED-1/6/7 branch in DTC migration as [PMID:20126385 "at most a minor role, if any"], and no ced-6 spindle phenotype.
