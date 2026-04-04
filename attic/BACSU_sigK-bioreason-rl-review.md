# BioReason-Pro RL Review: sigK (Bacillus subtilis)

Source: sigK-deep-research-bioreason-rl.md

- **Correctness**: 2/5
- **Completeness**: 1/5

## What It Got Right

BioReason correctly identifies the protein as a sigma-70 family transcription initiation factor and correctly maps the domain architecture: region 2 (IPR013325/IPR007627) for -10 recognition, region 3/4 (IPR013324/IPR007630) for -35 recognition, and the HTH element (IPR001387) in region 4. The mechanistic description of sigma-70 factor function (open complex formation, promoter engagement) is accurate. Inferring cytoplasmic localization is correct.

## What It Got Wrong

The formal GO molecular function output is GO:0005515 (protein binding) — the same systematic failure seen in all other sigma factor reviews. The correct term, GO:0016987 (sigma factor activity), is clearly stated in the prose but absent from the formal GO annotation output.

More seriously, the cellular component output places SigK in the nucleus (GO:0005634) and associated nuclear compartments (membrane-bounded organelle, intracellular membrane-bounded organelle). This is a prokaryote — there is no nucleus. This is a fundamental biological error. It also lists "endonuclease complex" (GO:1905348) and "catalytic complex" (GO:1902494) as cellular components, which are completely wrong for a sigma factor in a bacterium.

The biological process list includes numerous negative regulation terms (negative regulation of DNA-templated transcription, negative regulation of RNA biosynthetic process, etc.), which are not appropriate for SigK. Sigma factors are positive regulators of transcription initiation from their cognate promoters. SigK does not negatively regulate transcription in the sense implied by these terms.

## What Was Missed

SigK has uniquely complex biology that BioReason entirely misses:

- The "skin" (skinBs) element: In strain 168, the sigK gene is split by a ~48 kb prophage-like element. The functional sigK ORF is only reconstituted when the SpoIVCA site-specific recombinase excises this element during sporulation. This is one of the most unusual gene activation mechanisms in bacterial biology and is completely absent from the BioReason output.
- Pro-sigK processing: SigK is synthesized as an inactive precursor (pro-sigK) with a 20-amino-acid N-terminal propeptide. This propeptide must be cleaved by the intramembrane metalloprotease SpoIVFB for activation. BioReason does not mention this.
- The regulatory cascade controlling SpoIVFB: BofA and SpoIVFA hold SpoIVFB inactive until forespore-secreted proteases SpoIVB and CtpB cleave these inhibitors. This intercellular signaling pathway — forespore signals to mother cell to activate SigK — is the core logic of sigK activation and is completely absent.
- The sigma factor antagonist complex (GO:1903865) involving pro-sigK, SpoIVFB, BofA, and SpoIVFA is documented by IntAct interaction data (PMID:19805276) and is not mentioned.
- The SigK regulon: coat proteins (cotA, cotB, cotD, cotE, cotH), cortex genes, and germination genes are not mentioned.
- The feed-forward network with GerE (which both represses some SigK-activated genes and activates additional late genes) is absent.
- Mother cell specificity: SigK is the late mother cell sigma factor, not a general sporulation factor. This spatial specificity is not captured.
- The protein binding interaction with SpoIVFB documented by IPI evidence (PMID:19805276) is not mentioned.

## Summary

BioReason provides a generic sigma-70 factor description that would apply to any sporulation sigma, missing the three defining features of SigK biology: (1) gene reconstitution by skin element excision, (2) pro-sigma activation by regulated intramembrane proteolysis, and (3) intercellular signaling via forespore-to-mother-cell communication. The formal GO output contains the egregious eukaryotic cellular component annotations (nucleus, endonuclease complex) and defaults again to uninformative "protein binding" for the molecular function. This is the weakest of the six sigma factor reviews.
