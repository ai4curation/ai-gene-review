# Deep Research Report: gacA (PSEPK)

## Gene identity

The review target requested as `gacA` in *Pseudomonas putida* KT2440 maps to UniProt `Q88FJ6`. UniProt records the gene name as `uvrY`, the ordered locus name as `PP_4099`, and the protein name as "Response regulator GacA (Global activator)." The protein is 212 aa long and contains a receiver domain plus a C-terminal LuxR-type helix-turn-helix output domain, with a predicted phosphoacceptor Asp54. This is the expected architecture of a transcriptionally acting two-component response regulator. [file:PSEPK/gacA/gacA-uniprot.txt "RecName: Full=Response regulator GacA"] [file:PSEPK/gacA/gacA-uniprot.txt "DOMAIN          3..119"] [file:PSEPK/gacA/gacA-uniprot.txt "DOMAIN          141..206"] [file:PSEPK/gacA/gacA-uniprot.txt "MOD_RES         54"]

## High-confidence KT2440 functions

### 1. Upstream regulator of adhesin expression and biofilm development

The most direct KT2440 evidence ties the Gac system to transcriptional control of the two major adhesin loci `lapA` and `lapF`, which organize the transition from early attachment to mature biofilm architecture. The key KT2440 paper states that both adhesin genes are controlled by GacS/GacA and describes the system as a master regulator of the biofilm program. [PMID:24488315 "Both lapA and lapF are under the control of the two-component regulatory system GacS/GacA"] [PMID:24488315 "The two-component system GacS/GacA appears as a master regulator of the process"]

Independent support comes from a KT2442 mutant screen, where a `gacS` insertion produced a moderate biofilm defect. That does not isolate GacA biochemically, but it reinforces that the same two-component system contributes to biofilm development in the lab strain lineage. [PMID:27190143 "A mutation in gacS, encoding the sensor element of the GacS/GacA two-component system, also had a moderate effect on biofilm formation"]

### 2. Contributor to c-di-GMP-associated surface phenotypes

In KT2440, a genetic dissection of the high-c-di-GMP crinkly-colony phenotype recovered GacA as one of the global regulators needed for the lifestyle shift associated with elevated c-di-GMP. This places GacA in the regulatory network that connects phosphorelay signaling to surface-associated behavior. [PMID:27489550 "Among the bacterial determinants found in this screen are the global transcriptional regulators GacA, AlgU and FleQ"]

The same paper also notes that GacS/GacA is essential for `rpoS` expression in KT2440, offering a mechanistic route by which GacA can influence broad stationary-phase and biofilm-associated outputs even when direct GacA promoter binding has not yet been mapped. [PMID:27489550 "the two component system GacS/GacA is essential for the expression of rpoS in KT2440"]

### 3. Positive regulator of K1 type VI secretion system expression

More recent KT2440 work extends the GacA regulon beyond biofilm-associated genes. The K1 type VI secretion system (T6SS), which supports interbacterial competition and plant-protective activity, is positively regulated by GacS-GacA and repressed by RetS. This indicates that GacA is part of a broader lifestyle-control module spanning both surface colonization and contact-dependent antagonism. [PMID:36748579 "expression of the K1-T6SS gene cluster is positively regulated by the GacS-GacA two-component regulatory system (TCS) and repressed by the RetS sensor kinase"]

## Conserved mechanistic interpretation

The broader Gac/Rsm literature describes GacA/UvrY proteins as phosphorelay-activated transcription regulators that trigger expression of one or more small RNAs, which then sequester Rsm/Csr translational repressors. This is the standard mechanistic framework for interpreting GacA-like regulators across gamma-proteobacteria. [PMID:18047567 "the conserved GacS/GacA (BarA/UvrY) two-component system positively controls the expression of one to five genes specifying small RNAs"] [PMID:11768529 "GacS senses a still-unknown signal and activates, via a phosphorelay mechanism, the GacA transcription regulator, which in turn triggers the expression of target genes"]

For KT2440 specifically, this framework is highly plausible, but I did not find direct evidence in the examined papers that identifies the precise small RNA promoters or demonstrates purified GacA binding to a defined target promoter. Because of that gap, the safest curation stance is:

- strong support for `phosphorelay signal transduction system`
- strong support for `phosphorelay response regulator activity`
- good support for transcription-factor-related DNA binding
- conservative treatment of direct promoter-binding claims in KT2440

## Strain-specific downstream outputs outside KT2440

Other *P. putida* strains show the same regulatory module governing quorum sensing, cyclic lipopeptide biosynthesis, and carbon-storage/polymer phenotypes:

- WCS358: GacA positively regulates the `ppuI` quorum-sensing synthase. [PMID:15345437 "GacA positively regulating ppuI expression"]
- PCL1445: putisolvin biosynthesis depends on GacA/GacS. [PMID:16109938 "putisolvin biosynthesis of PCL1445 was found to be dependent on the GacA/GacS two-component signaling system"]
- RW10S2: WLIP production is downstream of a GacS-dependent branch. [PMID:22544260 "Expression of wlpR is dependent on gacS"]
- CA-3: PHA synthesis is connected to a GacS/GacA-rsm cascade. [PMID:23291549 "gene homologues of the GacS/GacA-rsm small RNA (sRNA) regulatory cascade"]

These strain-level observations strengthen the interpretation of GacA as a pleiotropic lifestyle regulator, but they should not automatically be converted into KT2440-specific GO terms without direct support in the KT2440 lineage.

## Curation summary

The most defensible core picture for KT2440 is that GacA is a phosphorelay response regulator and DNA-binding transcription regulator upstream of biofilm-associated adhesin control, c-di-GMP-linked surface behavior, and at least one antagonistic output (K1-T6SS). The cleanest GO additions are therefore `GO:0000156 phosphorelay response regulator activity`, `GO:0003700 DNA-binding transcription factor activity`, and `GO:1900192 positive regulation of single-species biofilm formation`, while keeping broader transcription-regulation terms as non-core.

## Remaining uncertainties

- Direct GacA DNA-binding targets in KT2440 remain incompletely mapped.
- The extent to which KT2440 outputs are mediated through canonical `rsmY/rsmZ`-type RNAs versus additional regulators is not clear from the examined literature.
- The signal sensed by GacS in KT2440 remains unresolved in the sources reviewed here.
