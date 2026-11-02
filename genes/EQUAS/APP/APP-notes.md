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

## 2026-10-23 — PR #5309 second review: quotes that did not support their terms

The reviewer found that many quotes used to replace the ortholog GOA listing were verbatim but did not
state the term they supported. Validation only checks that a quote is a substring of its source, so it
cannot catch this. Every quote added in that pass was re-read against one question: does this sentence
state this term, for this gene product, at this specificity?

**Wrong-gene donor (GO:0008285).** The only donor is a human IDA assigned by UniProt
(P05067, PMID:22944668, 2017-04-25). That paper is about the antimicrobial activity of human islet amyloid
polypeptide (IAPP, amylin) ["Human islet amyloid polypeptide (hIAPP) shows an antimicrobial activity
towards two types of clinically relevant bacteria."]. Its cached abstract never mentions APP or
amyloid-beta and contains no proliferation assay. The row is now UNDECIDED, with a PROBABLE
`WRONG_GENE_PRODUCT` source defect on the upstream UniProt row (requested change CHECK; candidate correct
product IAPP, UniProtKB:P10997, verified by UniProt REST). `genes/human/APP` still ACCEPTs this IDA; that
file is outside this PR and should get the same treatment.

**Re-supported with a quote that states the claim.** Where possible these use the donor paper or a
curated human UniProt line tied to a PubMed id:
- signaling receptor binding: Abeta42 interacts with FPR2 (UniProt), and CD74 interacts with APP while
  "it also serves as a receptor for macrophage migration inhibitory factor" (PMID:19849849, the IPI
  donor, cached in full). These replace "Functions as a cell surface receptor", which states the inverse
  relation, and "Correctly scoped to the APP subfamily.", which states nothing about function.
- early endosome and early endosome membrane: "Early endosome {ECO:0000269|PubMed:20580937}" plus
  "Single-pass type I membrane protein". A type I membrane protein in early endosomes is in their
  membrane; the reason says so. This replaces "colocalize in endosomal and Golgi compartments".
- enzyme binding: direct PSEN1 binding (PMID:30630874) and IDE binding (PMID:17051221) from UniProt,
  replacing the ADAM19 sAPPalpha quote, which reports a processing outcome rather than binding.
- protein serine/threonine kinase binding: LRRK2 binding (PMID:28720718), replacing ROCK2
  phosphorylation of APP.
- membrane raft: "Also binds GPC1 in lipid rafts." (UniProt), replacing a PANTHER scope sentence.
- perinuclear region: the full SORL1 sentence ending "...cytoplasm and perinuclear regions". The
  earlier quote had been cut off before "perinuclear".
- neuron projection: "Cell projection, growth cone {ECO:0000269|PubMed:10341243}."
- positive regulation of synaptic transmission, cholinergic: "oAβ42 activates both homomeric α7- and
  heteromeric α7β2-nAChR subtypes" (PMID:33239400, the donor), added beside the CHRNA7 binding line.
- positive regulation of inflammatory response: Aβ "stimulates the nuclear transcription factor κB
  (NF-κB) signaling, leading to the secretion of inflammatory cytokines" (PMID:29961672, the donor,
  full text).
- positive regulation of ERK1/2 cascade: "chronic activation of the ERK MAPK cascade ... via α7
  nAChRs" (PMID:11404397, full text), replacing a sentence about the generic MAPK cascade.
- amyloid fibril formation: an oligomer that "can form and coexist in parallel with the well-known
  cross-β-sheet fibrils" (PMID:26138908).
- microglial cell activation: the full TLR2 sentence, which names "cultured microglia and macrophages".

**UNDECIDED: the donor text does not state the term.** All of these donors are cached abstract-only,
except PMID:23382219, which is cached in full. The abstracts were read in full, and none mentions the
term's specific entity:
- astrocyte activation and astrocyte activation involved in immune response (PMID:15457210,
  PMID:23152628). The UniProt "mononuclear phagocytes" line is about a different cell type.
- positive and negative regulation of gene expression (PMID:22198949). One TLR2 sentence supported both
  directions while naming no gene.
- positive regulation of chemokine, IL-1β and IL-6 production (PMID:22406537), and of TNF production
  (PMID:22198949). No cytokine is named in either abstract.
- dendritic spine and dendritic shaft (PMID:11988176). The abstract is about ASIC and does not mention
  APP. The 23931995 sentence ("dendritic APP/BACE-1-containing vesicles") still supports dendrite, but
  it cannot tell spines from shafts. This donor may also be mis-keyed, but no source defect was filed
  because the full text was not read.
- signaling receptor complex (PMID:23382219, full text). That paper is a PX-FERM cargo-recognition
  study in which APP appears only as a previously identified SNX17 cargo. It is a possible source defect
  but was not filed.
- positive regulation of the JNK cascade (PMID:23921129). JNK is never mentioned.
- modulation of EPSP (PMID:20974225), regulation of spontaneous synaptic transmission (PMID:15457210)
  and positive regulation of non-canonical NF-κB signalling (PMID:15457210). None of these is measured
  or mentioned.
- cellular response to amyloid-beta (PMID:29518356). In that paper the responding entity is microglia
  expressing TREM2.
- positive regulation of amyloid fibril formation (PMID:19660551). The paper characterises Abeta
  assemblies in J20 mice but does not test regulation.

**Kept as they were, after the check:**
- dendrite: PMID:23931995 places APP vesicles in dendrites.
- Golgi-associated vesicle, growth cone, synapse, axonogenesis, signaling receptor activator activity,
  regulation of presynapse assembly and synapse organization: the reviewer verified these.
- learning and learning or memory: these are MARK_AS_OVER_ANNOTATED, and their quotes support the
  phenotype-not-participation reason.
- negative regulation of LTP and regulation of long-term neuronal synaptic plasticity:
  "Aβ-induced inhibition of long-term potentiation" supports both.
- calcium-mediated signalling (Abeta raises cytosolic Ca2+), amyloid-beta complex (oligomeric states),
  receptor ligand activity (direct TLR2–Aβ42 interaction) and glycolysis.
- positive regulation of protein metabolic process: this is MARK_AS_OVER_ANNOTATED, and its quote
  shows the indirect MAPK coupling that the reason describes.

**Out of scope.** `genes/EQUAS/APP/APP-protnlm-predictions-review.yaml` (and
`genes/EQUAS/HOXA2/HOXA2-protnlm-predictions-review.yaml`) still quote the ortholog GOA listing. There it
backs an LSP verdict about annotation state, not a biological claim. Whether to change that is a separate
decision, and those files were left untouched.

Row tally for this file (EQUAS/APP): 15 re-supported (including perikaryon, which had no support before; PMID:10341243 was added to references) and 18 set to UNDECIDED. GO:0008285 was MARK_AS_OVER_ANNOTATED and is now UNDECIDED with the source defect. Microglia development keeps MARK_AS_OVER_ANNOTATED with the fuller TLR2 sentence.
