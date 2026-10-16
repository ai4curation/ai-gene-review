# nsf-1 (UniProt Q94392) — Vesicle-fusing ATPase (NSF), C. elegans

## Identity
- Reviewed entry NSF_CAEEL, N-ethylmaleimide-sensitive fusion protein, AAA+ ATPase (EC 3.6.4.6); homohexamer; PANTHER PTHR23078:SF3 (from `nsf-1-uniprot.txt`). UniProt function text is "By similarity" (Golgi/ER-Golgi transport); no worm-specific synaptic annotation in GOA.
- Two isoforms from separate promoters expressed in distinct tissues; NSF-1L is expressed in the uterus including the anchor cell [PMID:16769048 "There are two NSF-1 isoforms, which are expressed in distinct tissues through two separate promoters. NSF-1L is expressed in the uterus, including the AC."].

## Function
- Conserved role: NSF with alpha-SNAP (SNAP-1) uses ATP hydrolysis to disassemble cis-SNARE complexes after fusion, recycling SNAREs for further rounds (family-level; the GOA IEA/IBA rows for ATP hydrolysis activity and SNARE complex disassembly capture this).
- Worm-specific evidence: a missense nsf-1 mutation blocks fusion of the uterine anchor cell with the utse cell-autonomously, establishing NSF-1 as a membrane-fusion factor in vivo [PMID:16769048 "We find that defect is due to a missense mutation in the nsf-1 gene, which encodes N-ethylmaleimide-sensitive factor (NSF), an intracellular membrane fusion factor."; "We find that nsf-1 is required cell-autonomously in the AC for its fusion with the utse."]. Cell-cell fusion in C. elegans is executed by EFF-1/AFF-1 fusogens; the NSF requirement presumably reflects SNARE-dependent vesicular trafficking of fusion machinery, though the abstract does not state the mechanism.
- Post-fusion cis-SNARE disassembly is the canonical role at synapses; the unc-18 docking paper explicitly considers UNC-18 protecting syntaxin "after N-ethyl-maleimide–sensitive factor (NSF)-mediated disassembly of the cis-SNARE complex" [PMID:12973353 "UNC-18 could bind and protect syntaxin after N-ethyl-maleimide–sensitive factor (NSF)-mediated disassembly of the cis-SNARE complex."].

## Interactions (high-throughput)
- Y2H interactome hits: pas-2 proteasome subunit [PMID:11559592], mig-5 (interactome map) [PMID:14704431], and a polarity-protein Y2H/phenotypic map [PMID:26780296]. These are systematic screens; none defines an NSF-1 function.

## Expression regulation
- nsf-1 is among the genes whose expression depends on the IRE-1/XBP-1 unfolded-protein-response pathway in microarray studies (HEP evidence) [PMID:16184190 "About 84% of i-UPR genes (170 out of 202 genes) were regulated by both ire-1 and xbp-1 (Figure 3A; Table S1)."]. Transcriptional regulation by the UPR does not make NSF-1 a participant in the UPR.

## Curation notes
- No GOA row records the synaptic cis-SNARE disassembly role for nsf-1; the module treats NSF-1 as the worm exemplar of the NSF annoton by family conservation (PTHR23078). Core functions below rest on the ATP hydrolysis and SNARE complex disassembly rows plus the anchor-cell fusion genetics.

## Additional literature not cited by GOA (from deep research)
- A 2023 study (PMID:36835643, MitoSNARE assembly and disassembly factors regulate basal autophagy and aging in C. elegans) reports that nsf-1 RNAi reduces mitochondrial mass and autophagosome abundance and that neuron-specific or non-neuronal nsf-1 inhibition shortens lifespan. These are RNAi/systems-level phenotypes: the deep-research report itself cautions that "These opposing phenotypes are consistent with the need for a balanced SNARE assembly–disassembly cycle; they do not show that every phenotype arises from one direct NSF-1/S..." [file:worm/nsf-1/nsf-1-deep-research-falcon.md]. No NEW process annotation is proposed from them, since the entity performing each step is the SNARE/autophagy machinery that NSF-1 recycles, not NSF-1 itself.
- For the anchor-cell requirement, AFF-1 is the direct fusogen, so NSF-1 most likely supports trafficking of the fusion machinery rather than fusing the membranes [file:worm/nsf-1/nsf-1-deep-research-falcon.md "Subsequent discovery that AFF-1 is the direct fusogen makes it more likely that NSF-1 supports vesicular delivery, positioning, or recycling of fusion machinery rather than directly fusing the two plasma membranes."].
