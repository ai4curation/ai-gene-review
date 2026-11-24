# BRUMA gp29 curation notes

## 2026-11-24

- Automated deep research was attempted with Falcon and the configured Perplexity Lite fallback,
  but neither provider was available in this checkout. The review therefore used a manual pass over
  the P67877 UniProtKB/Swiss-Prot entry and local publication caches.
- GP29 is the Brugia cuticular glutathione-peroxidase homolog. The primary cloning abstract identifies
  gp29 as the major soluble cuticular glycoprotein of lymphatic filariae and as a homolog of glutathione
  peroxidase, with a predicted signal peptide and two N-linked glycosylation sites [PMID:1631065, "We
  have cloned and identified the major cuticular glycoprotein (gp29) of lymphatic filarial nematode
  parasites as a homolog of the antioxidant enzyme glutathione peroxidase."].
- The modeling paper provides the directly quoteable tetramer evidence for Brugia spp. gp29 but does
  not biochemically measure B. malayi P67877 substrate preference in the cached abstract [PMID:7681545,
  "Experimental data showed that Brugia spp. gp29 has four subunits, and a tetrameric form of gp29 has
  also been modelled."].
- The closest activity lead is the Brugia pahangi gp29 paper whose title reports heterologous membrane
  protection from lipid peroxidation [PMID:8631385]. Its local cache is title-only, so it is useful
  context for the suggested phospholipid-hydroperoxide follow-up but not enough on its own to add
  GO:0047066 for B. malayi P67877.
- Direct B. malayi excretory-secretory proteomics detected P67877 in microfilarial, adult-female and
  adult-male ESP, supporting extracellular-region annotation and the host-interface antioxidant model
  [PMID:18958170, "gp29 (P67877), a glutathione peroxidase believed to act as a lipid hydroperoxidase,
  protecting parasite membranes from peroxidation caused by oxygen free radicals [66]-[68], was
  identified in all 3 ESP sets."].
- C. elegans gpx-5 is the existing worm ortholog review to cross-check. Its review is more conservative
  because GPX-5 has no biochemical assay showing glutathione dependence; in contrast, the Brugia P67877
  entry is reviewed in Swiss-Prot and carries EC 1.11.1.9 plus the gp29-specific Brugia sequence,
  modeling, and secretion literature.
