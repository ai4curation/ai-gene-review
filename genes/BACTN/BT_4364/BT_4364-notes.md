# BT_4364 / Lnb evidence notes

## 2026-11-07 — source-grounded review

In the VPI-5482 Δtdk background, deleting BT_4364 shifts both a heterologous Lpp reporter and endogenous BT_3736/BT_3183 lipoproteins to forms consistent with loss of one acyl chain; complementation restores triacylation. This establishes the native gene role in N-acylation, while no purified-Lnb activity or acyl-donor assay is reported.

[PMID:39495918, Identification and characterization of the lipoprotein N-acyltransferase in Bacteroides.] "In each case, complementation of the ΔBT_4364 strain with BT_4364 under the constitutive promoter us1311 was sufficient to restore triacylation." The biological product is triacylated lipoprotein; the assay does not identify a physiological acyl donor. The enzyme itself was not purified/reconstituted. This is a distinct protein architecture from canonical Lnt, and no Lnt donor chemistry or EC number is transferred.

The official locus/accession/taxon match is archived in `analysis/module_audits/bacterial_lipoprotein_maturation/lnb-consultation/`. Both targets have IPR025178 (Lnb, N-terminal periplasmic domain), IPR057436 (Lnb-like, transmembrane domain), PF13387, PF25221 and NCBIfam NF051878. The InterPro entries are domains, not a whole-family grant: IPR025178 also occurs with other domains. There is no PANTHER classification or IBA row to adjudicate. Membrane association is predicted from target architecture; a periplasm-facing domain does not make the whole multipass protein a soluble periplasmic protein. The core uses broad membrane placement without inventing a resolved compartment assay.

Only BT_4364 was mutated: "Only Lnb(C198S) could restore N-acylation activity to Δlnb cells, suggesting that C148 is essential for activity of Lnb" H49/N66 are modeled and conserved, not independently established catalytic residues. Q89ZL3 has H49/N66/C148/C198 but is395 aa in the current sequence, versus398 in the paper's description. That length difference remains unexplained. Q5LGL3 is408 aa; the BT residue numbers are not transferred to the B. fragilis protein. Reporter-rescue failure alone does not prove direct chemical participation of a residue independently of protein stability.

The zero-row seed is preserved. Two additions cover the demonstrated acyltransferase genus and direct participation in lipoprotein biosynthesis. Exact-role QuickGO comparators P23930 and Q88DN4 carry GO:0042158. MF and BP are distinct aspects and no duplicate parent/child process is added. GO:0016410 is obsolete; GO:0140186 has an inappropriate lysine-N6/acyl-CoA reaction. Downstream growth, morphology, client sorting, polysaccharide use and OMV changes do not justify additional direct process claims.

A genuine Falcon request was made and failed with HTTP403 authentication/access rejection; the log is archived and no provider report was fabricated. The publication and normal-fetch raw source files remain unchanged. All quotations above are from the full cached primary, not generated provider prose.


## PR 6184 source adjudication, 2026-11-07

Core localization is refined from membrane to plasma membrane as an inference from five predicted alpha-helical transmembrane segments and the extracytoplasmic DUF4105 domain (PMID:39495918), together with the mature lipoprotein reaction. This is not a native fractionation measurement. The paper's uncertainty about inner-versus-outer localization of lipoprotein clients does not describe Lnb itself. Existing BT_4364 construct-length/identity limits remain in the prior notes. A donor-agnostic specific N-acyltransferase proposal is added alongside the valid GO genus, without a NEW annotation, imported Lnt donor chemistry, or claim of purified Lnb activity.
