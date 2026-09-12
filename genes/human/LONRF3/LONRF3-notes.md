# LONRF3 reference audit

## Evidence blockers and core boundary

- No direct LONRF3 biochemical study was identified. The current evidence does not demonstrate intrinsic E2-dependent ubiquitin-transfer activity, LONRF3 autoubiquitylation, ubiquitylation or degradation of a substrate, ubiquitin-chain linkage, or a RING-mutant requirement. The GO:0061630 annotation is IBA phylogenetic inference, not direct LONRF3 experimentation.
- The direct LONRF2 protein-quality-control results must not be transferred to LONRF3. LONRF2's abnormal TDP-43, hnRNP M and ALDOA substrates are paralog-specific evidence unless LONRF3 is independently tested.
- No experimentally supported LONRF3 subcellular localization was found. UniProt lists cytoplasm only as an electronic ARBA annotation; none of the three GOA interaction papers localizes endogenous LONRF3.
- No physiological LONRF3 complex is established. The seven GOA partners come from three systematic binary-interaction resources and should not be treated as substrates, stable-complex members, or pathway assignments without orthogonal endogenous evidence.
- The PubMed-indexed HIV-Tat paper (PMID:23898208) is associated with an NCBI GeneRIF stating that Tat downregulates LONRF3 in primary T cells, but `publications/PMID_23898208.md` contains no LONRF3/RNF127 occurrence. The relevant result appears to depend on uncached supplementary expression data, so it is not used as functional evidence here.
- A PubMed search for `LONRF3 OR RNF127` returned recent prognostic/transcriptomic association studies but no gene-specific biochemical characterization. These association studies do not establish molecular function.

## Interaction-screen evidence and limitations

- PMID:20195357 used in vitro mRNA display: [PMID:20195357, "Here we present the first large-scale IR data set obtained using mRNA display for 50 human transcription factors (TFs), including 12 transcription-related proteins."] GOA associates LONRF3 with PHB1. The paper reports an overall property of the screen—[PMID:20195357, "The core data set (966 IRs; 943 PPIs) displays a verification rate of 70%."]—but the cached article does not establish individual orthogonal validation or functional consequence for LONRF3-PHB1.
- PMID:25416956 is a proteome-scale binary map: [PMID:25416956, "Here, we describe a systematic map of ?14,000 high-quality human binary protein-protein interactions."] GOA assigns APPBP2 and NOTCH2NLA as LONRF3 partners. Neither is shown to be a LONRF3 ubiquitination substrate or an endogenous complex member.
- PMID:32296183 describes HuRI as [PMID:32296183, "Here we present a human 'all-by-all' reference interactome map of human binary protein interactions, or 'HuRI'."] GOA assigns CYSRT1, DES, CTAG1B and TRAF2 as LONRF3 partners. The paper's own framing—[PMID:32296183, "HuRI is a systematic proteome-wide reference that links genomic variation to phenotypic outcomes."]—supports using these as hypothesis-generating binary contacts, not gene-specific mechanism.

## Protein architecture, isoforms and the Lon-peptidase hazard

- UniProt Q496Y0 describes a 759-aa canonical protein with TPR repeats at 67-100, 243-276, 278-310 and 312-344; RING-type zinc fingers at 158-196 and 467-505; and a predicted Lon N-terminal domain at 546-755.
- The name “LON peptidase N-terminal domain and RING finger protein 3” must not be interpreted as evidence of peptidase or ATP-dependent protease activity. LONRF3 contains the Lon **N-terminal substrate-binding** module but lacks the AAA+ ATPase and protease catalytic domains of complete Lon proteases. No proteolysis assay for LONRF3 was found.
- Isoform 2 (Q496Y0-2) lacks residues 313-353. This essentially removes TPR4 while retaining TPR1-3, both RING fingers, and the C-terminal Lon N-terminal domain.
- Isoform 3 (Q496Y0-3) replaces residues 605-610 and lacks residues 611-759. It retains all four TPR repeats and both RING fingers but truncates most of the Lon N-terminal domain.
- None of the cached interaction papers identifies the tested LONRF3 isoform in its main text, and no isoform-specific functional comparison was found. An annotation to a specific isoform would therefore require checking the exact construct in supplementary interaction data.

## Curation implications

- `ubiquitin protein ligase activity` is plausible from two RING domains and supported by IBA, but remains inferred for LONRF3; it should not be summarized as experimentally demonstrated intrinsic activity.
- `metal ion binding` is a defensible domain-based electronic inference for RING zinc coordination, not a measured free-metal-binding function.
- Generic `protein binding` annotations preserve the outputs of the interaction resources but are not informative core molecular functions. The named partners are candidates for follow-up, not substrates.
- The decisive unresolved experiments are an E2-dependent reconstituted ubiquitination assay with wild-type and RING-mutant LONRF3, endogenous substrate discovery with rescue controls, and endogenous localization/proximity mapping across isoforms.
