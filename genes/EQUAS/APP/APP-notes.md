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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Deep research: `just deep-research EQUAS APP --provider falcon` failed ("Exception: Failed to authenticate" from the Edison client), so no deep-research file exists; this re-review uses the cached donor publications, the human UniProt record and the PANTHER family review.

### Identity
- A0A9L0JJJ9 is a full-length product, not a fragment: 770 aa, aligns end to end with human APP770 (P05067) at 97.9% identity with no gaps [file:EQUAS/APP/APP-bioinformatics/RESULTS.md "aligned pairs 770; identical 754; identity over aligned pairs 97.92%"]. It is the KPI-containing APP770 splice form; Kunitz, E2, amyloid-beta 1-42, TM and intracellular regions are identical to human.
- PANTHER: the donkey UniProt record does list a family, PTHR23103:SF7 AMYLOID-BETA PRECURSOR PROTEIN [file:EQUAS/APP/APP-uniprot.txt "PTHR23103:SF7; AMYLOID-BETA PRECURSOR PROTEIN"], the same subfamily as human, mouse and rat APP. The family review (interpro/panther/PTHR23103/PTHR23103-review.yaml) defines SF7 as the vertebrate APP orthologs under Euteleostomi node PTN002749606, the only subfamily with the amyloid-beta region. No disagreement about placement.

### Evolutionary grounding
- PAINT places plasma membrane, cell surface, Golgi, early endosome, membrane raft, signaling receptor binding and signaling receptor activator activity at the APP node PTN002749606 (SF7), so these reach donkey APP by descent. Axonogenesis and CNS development sit at the Bilateria node PTN000559854 (supported by fly APPL). The amyloid-beta-dependent terms are subfamily-only by construction, and donkey Abeta is human-type.
- The Ensembl Compara rows are pairwise orthology transfers from human P05067 (one-to-one ortholog in the same SF7 clade), so the orthology is sound; the open question for each row is whether the human donor annotation itself describes APP doing the work.

### Main finding: donor annotations are mostly Alzheimer-model phenotypes
Reading the cached donor abstracts shows that most human process annotations come from studies in which overexpressed mutant APP, or applied amyloid-beta, acts through a receptor whose knockout modifies the outcome (RAGE PMID:15457210/22406537, TLR2 PMID:22198949, PrP PMID:20445063, FcgRIIb PMID:23921129, alpha7 nAChR PMID:20974225). Where amyloid-beta acts as a receptor ligand (cytokine production, glial activation, kinase cascades, calcium signalling) I kept the rows as non-core. Where the row asserts participation in something the donor study shows amyloid-beta damaging, or an organism-level phenotype, I changed them to MARK_AS_OVER_ANNOTATED:
- learning or memory, learning: deficits of AD transgenic mice [PMID:11140684 "Mice that overexpress the human mutant amyloid precursor protein (hAPP) show learning deficits"].
- neuron projection maintenance (was ACCEPT): the transgene causes axonal degeneration that PrP deletion rescues [PMID:20445063 "deletion of PrP(C) expression rescues 5-HT axonal degeneration, loss of synaptic markers, and early death in APPswe/PSen1DeltaE9 transgenic mice"].
- positive regulation of long-term synaptic potentiation: the transgene blocks agonist-enhanced LTP [PMID:20974225 "in the Tg mice the application of SSR180711 did not result in an increase in LTP beyond control levels"].
- positive regulation of glycolysis: metabolic phenotype of APP/PS1 microglia [PMID:29061364 "revealed genotype-related increases in glycolysis, accompanied by increased PFKFB3"].
- microglia development: the donor measures activation, not development (TLR2 study PMID:22198949).
- positive regulation of T cell migration: the donor (PMID:19660551) is about Abeta assembly forms in J20 mice.
- negative regulation of cell population proliferation: the donor (PMID:22944668) is about antimicrobial amyloid peptides; abstract-only, so I did not assert a mis-attribution.
- nuclear envelope lumen -> UNDECIDED (single IDA, not verifiable). dendritic spine / shaft ACCEPT -> KEEP_AS_NON_CORE (dendritic APP documented, PMID:23931995; sub-dendritic detail not verifiable).

### Citation fix
The previous version cited `APP-bioinformatics/ortholog_experimental_goa.txt` (a listing of ortholog GO annotations) as supporting_text for 69 rows. That cites annotations as evidence for themselves, so I replaced every such citation with quotes from the donor publications, the human UniProt record, the PANTHER family review, or the donkey UniProt family line. The listing stays in the references with a review note.

### Relative
Closest characterised relative by phylogeny is human APP (P05067), same PANTHER subfamily SF7 and one-to-one Compara ortholog; it has a complete review at genes/human/APP/APP-ai-review.yaml. Mouse App (P12023, also SF7) is reviewed too. No modules in modules/ contain APP (the kallikrein-kinin module's "APP" is aminopeptidase P).
