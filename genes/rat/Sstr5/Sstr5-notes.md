# Sstr5 (Rattus norvegicus) -- Research Notes

## Gene Identity

- UniProt: P30938 (SSR5_RAT)
- Gene symbol: Sstr5 (rat nomenclature)
- Full name: Somatostatin receptor type 5
- 363 amino acids, 7TM GPCR, class A rhodopsin-like

## Key Literature

### Cloning and initial characterization

[PMID:1362243] O'Carroll et al. (1992) Mol Pharmacol. Cloned the receptor from rat pituitary cDNA library. Originally designated "SSTR4" in this paper (nomenclature was later revised to SSTR5). Key findings:
- "SRIF-28 was the most potent competitor of 125I-Tyr11-SRIF binding, with a approximately 30-fold greater affinity for the receptor than that of SRIF"
- "binding of 125I-Tyr11-SRIF was markedly reduced in the presence of Na+ ions and GTP, indicating coupling of rAP6-26 receptors to inhibitory G proteins"
- "forskolin-induced cAMP accumulation was inhibited by SRIF and SRIF-28, thus confirming that the rAP6-26 cDNA encodes a functional receptor protein"
- "a approximately 2.6 kilobase mRNA encoding the receptor was present in the pituitary but not in the liver, small intestine, kidney, pancreas, cerebellum, or cortex"

### Human homolog characterization

[PMID:7908405] Panetta et al. (1994) Mol Pharmacol. Cloned the human SSTR5. Key for rat:
- Confirmed preferential affinity for somatostatin-28 over somatostatin-14 (12.6-fold, Ki = 0.19 nM vs 2.24 nM for human)
- "hSSTR5 is coupled to pertussis toxin-sensitive G proteins" confirming Gi/o coupling
- SSTR5 mRNA "selectively localized in the anterior lobe" of rat pituitary by ISH
- Corrected the C-terminal sequence of the rat receptor (363 aa, not 383 aa)

### Glucocorticoid regulation

[PMID:14512709] Park et al. (2003) Neuroendocrinology. This is the basis for the IEP annotation for GO:0071385 (cellular response to glucocorticoid stimulus):
- "High-dose DEX resulted in a decrease in sst1-sst4 mRNA and an increase in sst5 mRNA, independent of adrenal status"
- "DEX also decreased sst2, sst3 and sst4 mRNA levels and increased sst5 mRNA levels by short-term in vitro application (10 nM, 4 h) in primary rat pituitary cell cultures"
- The sst5 increase is distinctive: all other subtypes decreased. This supports the IEP annotation.
- Mechanism: partially indirect via somatostatin-mediated effects rather than purely direct glucocorticoid action.

### Palmitoylation by ZDHHC5

[PMID:21820437] Kokkola et al. (2011) FEBS Lett:
- "ZDHHC5 and SSTR5 are colocalized at the plasma membrane and can be efficiently coimmunoprecipitated from transfected cells"
- "Coexpression of ZDHHC5 in HEK293 cells increased palmitoylation of SSTR5 whereas knock-down of endogenous ZDHHC5 by siRNAs decreased it"
- This was the first palmitoyltransferase identified for any GPCR.

### SSTR5 knockout mouse studies -- insulin and glucose

[PMID:12511609] Strowski et al. (2003) Mol Endocrinol. sst5 KO mice:
- "sst(5) KO mice exhibited decreased blood glucose and plasma insulin levels and increased leptin and glucagon concentrations"
- "sst(5) KO mice displayed decreased susceptibility to high fat diet-induced insulin resistance"
- "sst(5) mediates SRIF inhibition of pancreatic insulin secretion and contributes to the regulation of glucose homeostasis and insulin sensitivity"
- This is in mouse, but directly supports the ISO annotations for rat (regulation of insulin secretion, glucose homeostasis)

[PMID:16026801] Wang et al. (2005) J Surg Res. Aging SSTR5 KO mice:
- At 12 months, "SSTR5-/- mice had basal hypoglycemia and improved glucose intolerance associated with hyperinsulinemia"
- "SSTR5 and SSTR1 play a pivotal role in insulin secretion and glucose regulation in mice"

[PMID:15349106] Wang et al. (2004) Surgery. SSTR1/5 double KO:
- "SSTR1/5 -/- mice also had significant increase of both basal and glucose-stimulated insulin levels in vitro"
- Confirms SSTR5 as negative regulator of insulin secretion

### SSTR5 regulation of PDX-1

[PMID:22669743] Zhou et al. (2012) Mol Endocrinol:
- "SSTR5 is a negative regulator for PDX-1 expression"
- "SSTR5 may mediate the inhibitory effects of somatostatin and its analogs on insulin expression/secretion and cell proliferation via down-regulating PDX-1"

### SSTR2/SSTR5 heterodimerization

[PMID:18653781] Grant et al. (2008) Mol Endocrinol:
- "SSTR2 and SSTR5 heterodimerize" (confirmed by co-IP and photobleaching FRET)
- "The SSTR2-selective agonist L-779,976 is more efficacious at inhibiting adenylate cyclase, activating ERK1/2, and inducing the cyclin-dependent kinase inhibitor p27(Kip1) in cells expressing both SSTR2 and SSTR5 compared with SSTR2 alone"
- "cell growth inhibition by L-779,976 treatment was markedly extended in coexpressing cells"
- This supports the UniProt comment about heterodimerization with SSTR2 enhancing growth inhibition.

### GLP-1 and SSTR5

[PMID:33434183] Jepsen et al. (2021) JCI Insight:
- "the selective SSTR5 antagonist (SSTR5a) stimulated glucose-induced GLP-1 secretion"
- "mice lacking the SSTR5R showed increased glucose-induced GLP-1 secretion"
- SSTR5 modulates glucose homeostasis in part through the intestinal GLP-1 system

## BioReason Report Errors

The BioReason SFT report (Sstr5-deep-research-bioreason.md) contains several errors:

1. **Ligand preference reversed**: The functional summary states "a strong preference for the 14-residue form" -- this is WRONG. SSTR5 has preferential affinity for somatostatin-28 (28-residue), not somatostatin-14. This is clearly stated in the original cloning paper [PMID:1362243] which found ~30-fold preference for SRIF-28 over SRIF-14.

2. **Cytoplasmic localization claim**: The report claims "The receptor resides at the plasma membrane and cycles through cytoplasmic trafficking pools" and predicts GO:0005737 (cytoplasm). While internalization/recycling is a general GPCR property, there is no specific evidence for SSTR5 cytoplasmic pools in the existing GOA annotations or literature for rat.

3. **Appetite-regulatory system crosstalk**: The report speculates about "Crosstalk with appetite-regulatory systems (appetite-regulating hormone; C-flanking peptide of NPY)" -- this is unsupported speculation, not grounded in the SSTR5 rat literature.

4. **No additional GO predictions**: The GO Term Predictions sections are empty, despite the model claiming various functions in its reasoning trace. This suggests the model could not produce confident term predictions.

## Summary of Core Biology

Sstr5 encodes somatostatin receptor type 5, a Gi/o-coupled GPCR that preferentially binds somatostatin-28 with high affinity. It is prominently expressed in the rat pituitary anterior lobe and small intestine, with lower levels in pancreatic islets. Upon ligand binding, it inhibits adenylyl cyclase, reducing intracellular cAMP. Through this signaling, SSTR5 acts as a negative regulator of insulin secretion from pancreatic beta cells and participates in glucose homeostasis. SSTR5 expression in pituitary is upregulated by glucocorticoids (dexamethasone), providing a link between the stress axis and somatostatinergic tone. The receptor can heterodimerize with SSTR2, enhancing the growth-inhibitory signaling of SSTR2. SSTR5 is palmitoylated at Cys-320 by the palmitoyltransferase ZDHHC5, which may regulate its membrane localization and G-protein coupling efficiency.
