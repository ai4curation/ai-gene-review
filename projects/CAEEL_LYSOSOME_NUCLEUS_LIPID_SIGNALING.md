# C. elegans Lysosome-to-Nucleus Lipid Signaling (OEA Pathway)

## Overview

The LIPL-4/LBP-8/NHR-80 pathway is a lysosome-to-nucleus retrograde lipid signaling axis that promotes longevity in *C. elegans*. The lysosomal lipase LIPL-4 generates oleoylethanolamide (OEA) and omega-6 PUFAs, which are chaperoned by the fatty acid-binding protein LBP-8 to the nucleus, where OEA directly binds and activates the nuclear receptor NHR-80. NHR-80 heterodimerizes with NHR-49 to drive transcription of fatty acid desaturases (fat-5/6/7) and beta-oxidation genes (acs-2). This pathway is required for germline-mediated (glp-1) longevity and is separable from insulin/IGF (daf-2) and dietary restriction longevity pathways.

Key reference: Folick et al. 2015 (PMID:25554789)

## Model Species

**Primary: Caenorhabditis elegans (worm)**
- UniProt species code: CAEEL

## Core Pathway Architecture

```
Lysosome                        Cytoplasm                   Nucleus
┌──────────────┐               ┌──────────────┐          ┌──────────────────────┐
│  LIPL-4      │  OEA/PUFAs   │              │          │  NHR-80 + NHR-49     │
│  (acid lipase)├──────────────►  LBP-8 ──────────────►  │  (HNF4 homologs)     │
│              │               │  (FABP)      │          │        │              │
│  TAG → OEA   │               │              │          │  fat-5/6/7, acs-2    │
└──────────────┘               └──────────────┘          └──────────────────────┘
```

### Signal Generation
- **lipl-4** - Lysosomal acid lipase; generates OEA and omega-6 PUFAs from TAG hydrolysis

### Signal Transport
- **lbp-8** - Fatty acid-binding protein (FABP); shuttles OEA from lysosome to nucleus via NLS

### Nuclear Reception
- **nhr-80** - Nuclear hormone receptor (HNF4 homolog); direct OEA receptor (Kd ~7.8 uM)
- **nhr-49** - Nuclear hormone receptor (HNF4 homolog); heterodimerization partner; does NOT bind OEA directly

## Gene Review Status

| Gene | UniProt | Status | Annotations | Core Functions | Notes |
|------|---------|--------|-------------|----------------|-------|
| lipl-4 | Q94252 | IN_PROGRESS | 14 reviewed | Yes | Lysosomal acid lipase, signal generator |
| lbp-8 | O02324 | IN_PROGRESS | 17 reviewed | Yes | Lipid chaperone, lysosome-to-nucleus shuttle |
| nhr-80 | Q8ITW8 | IN_PROGRESS | 16 reviewed | Yes | OEA receptor, desaturase regulator |
| nhr-49 | O45666 | IN_PROGRESS | 28 reviewed | Yes (3) | Orphan NHR; fatty acid metabolism, longevity, hypoxia |

## Missing Genes

### High Priority
- **nhr-49** - Essential heterodimerization partner of NHR-80. Regulates both desaturation (with NHR-80) and beta-oxidation (with NHR-66). Does NOT bind OEA directly but is required for pathway output. More pleiotropic than NHR-80 (also regulates sphingolipid metabolism). nhr-49 mutants have dramatic lifespan reduction (~41%) and fat storage increase.

### Lower Priority (Downstream/Contextual)
- **fat-5**, **fat-6**, **fat-7** - Delta-9 desaturase targets of NHR-80/NHR-49 transcriptional regulation
- **acs-2** - Acyl-CoA synthetase for beta-oxidation; >15-fold induced by LIPL-4 Tg
- **hlh-30** - TFEB homolog that regulates lipl-4 expression (already reviewed in this repo)
- **daf-16** - FOXO; regulates lipl-4 induction in germline-less context (already reviewed)
- **glp-1** - Notch receptor; germline proliferation; glp-1 mutants are the canonical longevity context

## Key Publications

- PMID:25554789 - Folick et al. 2015 - Discovery of OEA as lysosomal lipid signal; LBP-8 as chaperone; NHR-80 as OEA receptor
- PMID:31292465 - Hughes et al. 2019 - LBP-8 crystal structure; ligand binding characterization
- PMID:21906946 - Lapierre et al. 2011 - LIPL-4 and autophagy coordinate longevity
- PMID:23392608 - O'Rourke & Ruvkun 2013 - Omega-6 PUFAs from LIPL-4 activate autophagy
- PMID:16839188 - Brock et al. 2006 - NHR-80 regulates delta-9 desaturases
- PMID:22511885 - Pathare et al. 2012 - NHR-49/NHR-80 coordinate lipid metabolism
- PMID:21423649 - Goudeau et al. 2011 - NHR-80 links germline loss to longevity via fat-6

## Cross-References to Other Projects

- Longevity/aging overlap with genes in multiple existing projects (daf-16, hlh-30)
- Autophagy connection via omega-6 PUFA signaling (see CAEEL_PROTEOSTASIS)
