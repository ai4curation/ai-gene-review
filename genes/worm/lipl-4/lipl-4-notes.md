# lipl-4 Research Notes

## Gene Overview
lipl-4 (K04A8.5) encodes a lysosomal acid lipase in C. elegans with sequence and functional similarity to human LIPA (lysosomal acid lipase). It is a key enzyme in the lysosome-to-nucleus retrograde lipid signaling pathway that promotes longevity.

## Core Pathway: LIPL-4 → LBP-8 → NHR-49/NHR-80

The central discovery is that LIPL-4 generates lipid signaling molecules in the lysosome, which are then transported to the nucleus by the lipid chaperone LBP-8 to activate transcription factors NHR-49 and NHR-80 [PMID:25554789 "Lysosomal signaling molecules regulate longevity in Caenorhabditis elegans"].

### Key lipid signals produced by LIPL-4:
1. **Oleoylethanolamide (OEA)** - an N-acylethanolamine fatty acid derivative. OEA directly binds LBP-8 (with ~3x higher affinity than fatty acids) and NHR-80 (Kd ~7.8 µM). OEA supplementation extends lifespan [PMID:25554789].
2. **Omega-6 PUFAs** (AA, DGLA) - these activate autophagy, extending lifespan [PMID:23392608 "omega-6 Polyunsaturated fatty acids extend life span through the activation of autophagy"].

## Enzymatic Activity
- Triacylglycerol lipase (EC 3.1.1.3) [PMID:21906946 "Autophagy and lipid metabolism coordinately modulate life span"]
- Lipid hydrolysis activity decreased in lipl-4(tm4417) loss-of-function at pH 4.5 but not pH 7.4 [PMID:25554789 "Lipid hydrolysis activity was decreased in lipl-4(tm4417) loss-of-function mutants at pH 4.5 but not at pH 7.4"]
- Optimal at acidic pH (consistent with lysosomal function)

## Subcellular Localization
- FLAG-tagged LIPL-4 localized to intestinal lysosomes [PMID:25554789 "FLAG-tagged LIPL-4 protein was localized to intestinal lysosomes"]
- Also detected in cytoplasm [PMID:23392608]
- Signal peptide required for lysosomal targeting and longevity effect [PMID:25554789 "Constitutive expression of LIPL-4 without the signal peptide (lipl-4 Tg no SP), which was not targeted to the lysosome, caused little extension of lifespan"]

## Longevity Function
- Constitutive expression extends lifespan by ~55% [PMID:25554789]
- Requires lysosomal localization (no SP version has little lifespan effect) [PMID:25554789]
- Requires LBP-8, NHR-49, and NHR-80 for longevity effect [PMID:25554789]
- Required for germline-less (glp-1) longevity [PMID:21906946]
- Additive with dietary restriction (eat-2) longevity [PMID:25554789]

## Autophagy Connection
- LIPL-4 overexpression induces autophagy [PMID:21906946]
- Autophagy required for LIPL-4-mediated longevity [PMID:21906946]
- LIPL-4 and autophagy are interdependent: autophagy maintains LIPL-4 lipase activity; lipl-4 required for autophagy induction [PMID:21906946]
- Omega-6 PUFAs produced by LIPL-4 activate autophagy in both worms and human cells [PMID:23392608]

## Regulation
- Upregulated by fasting in intestine [PMID:23392608, PMID:23604316]
- Regulated by MXL-3 and HLH-30 (TFEB homolog) transcription factors [PMID:23604316]
- Induced in germline-less animals (glp-1) in a DAF-16-dependent manner [PMID:21423649]
- TOR inhibition induces lipl-4 expression [PMID:21906946]

## Downstream Signaling
- LIPL-4 Tg increases acs-2 transcription >15-fold (NHR-49/NHR-80 dependent) [PMID:25554789]
- Promotes mitochondrial beta-oxidation [PMID:30713071]
- OEA production requires NAPE-PLD (nape-1) [PMID:25554789]
