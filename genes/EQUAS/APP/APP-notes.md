# APP (donkey, A0A9L0JJJ9) notes

## Sources
- Donkey UniProt A0A9L0JJJ9 (unreviewed; function/location text from RuleBase/ARBA, ECO:0000256).
- Human APP P05067 UniProt (genes/human/APP/APP-uniprot.txt) and the human review genes/human/APP/APP-ai-review.yaml (used as a baseline; donkey decisions are my own and are in places more conservative).
- Ortholog experimental GO (human P05067, mouse P12023, rat P08592) from QuickGO: APP-bioinformatics/ortholog_experimental_goa.txt — these are the donors behind every donkey Ensembl Compara (GO_REF:0000107) row.
- Alignment: APP-bioinformatics/RESULTS.md.

## Biology (human ortholog)
- Full-length APP: [file:human/APP/APP-uniprot.txt "Functions as a cell surface receptor and performs"] functions on neurons relevant to neurite growth, neuronal adhesion and axonogenesis; trans-dimerization promotes synaptogenesis (PubMed:25122912).
- KPI-containing isoforms (APP751/770) inhibit serine proteases [file:human/APP/APP-uniprot.txt "isoforms that contain the BPTI domain possess protease inhibitor"].
- Binds heparin and collagen to regulate neurite outgrowth [file:human/APP/APP-uniprot.txt "extracellular matrix such as heparin and collagen I and IV."].
- Amyloid-beta peptides chelate/reduce Cu, Zn, Fe [file:human/APP/APP-uniprot.txt "Amyloid-beta peptides are lipophilic metal chelators with"]; Abeta42 can activate phagocytes and elicit inflammatory responses.
- Trafficking: ER -> Golgi -> plasma membrane, rapid clathrin-mediated internalization to endosomes; secretory transport vesicles; soluble ectodomain released after alpha-secretase cleavage; AICD/gamma-CTF in cytoplasm and nucleus.
- Cytoplasmic YENPTY motif binds PTB/PID domains (APBB/FE65, APBA/X11, DAB1, NUMB, SHC1).

## Donkey sequence
- APP770 isoform, 97.9% identity; KPI, E2, Abeta1-42, TM and intracellular domain identical; donkey Abeta is human-type [file:EQUAS/APP/APP-bioinformatics/RESULTS.md].

## Decision principles
- Neuronal surface receptor/adhesion, axonogenesis, synapse organization, KPI protease inhibition, heparin and metal binding, and the trafficking compartments: ACCEPT.
- Effects of the cleaved amyloid-beta peptide in disease/inflammation models (glial activation, cytokine production, LTP inhibition, fibril formation, kinase cascades) and vague gene-expression rows: KEEP_AS_NON_CORE. They are activities of a fragment of this gene product, largely from IGI/IMP studies of Abeta, and not the physiological core function.
- Generic parents entailed by accepted children (endopeptidase inhibitor activity, membrane, endomembrane system, neuron projection): TOO_GENERAL.
- ARBA "regulation of protein metabolic process", "molecular function activator activity" and the Compara "positive regulation of protein metabolic process": MARK_AS_OVER_ANNOTATED (consistent with the human review).
- Nuclear and cytoplasmic rows reflect the AICD/gamma-CTF fragment: KEEP_AS_NON_CORE.
