# bdbD: manual annotation review, 2026-11-06

Target: O32218, Bacillus subtilis strain 168 (NCBITaxon:224308). Normal fetch-gene seed and all original payloads/raw hashes were frozen in `.cache/module-audit-logs/dsbab-20261106/bacillus/seed-baseline.json` before curation. Falcon was attempted normally once and returned HTTP 403 (authentication failure); no provider report was created.

## Evidence and limits

PMID:19535335 directly demonstrates BdbD membrane association, peptide disulfide transfer and calcium-dependent modulation of redox potential. The pACN2 soluble construct was made from 1A1 genomic DNA; its deposited 3EU3 sequence exactly equals reference O32218 residues 30–222 plus Met and LEHHHHHH. The source-analysis identity proof records raw response hashes and the direct comparison, independent of imperfect SIFTS alignment boundaries. A soluble-domain assay is not a purified full BdbC/BdbD quinone-coupled turnover experiment. The frozen UniProt signal-cleavage prediction (1–36) is not used to override direct membrane association; the paper does not sequence the native N terminus.

PMID:11744713 was read in full from the institutional repository after normal force-fetch retained only the abstract. Figure 1 and Table I identify strain 168 and derivatives. Active extracellular E. coli PhoA decreases in bdbD mutants and is not restored by inducing bdbC; proteins lacking disulfides provide controls. ComGC protein abundance and transformability depend on both genes, but the authors explicitly acknowledge the lack of direct ComGC folding evidence. This distinguishes catalytic participation in oxidative folding from inferred native-substrate identity and from mere necessity for transformation. No transformation, sporulation, or cytochrome-maturation NEW is proposed. Full acquired PDF/text is ignored; only short exact excerpts and provenance are retained.

PMID:11844773 supplies genetic redox-pair evidence and conserved BdbC cysteine/topology/arginine features. PMID:19535335 notes that BdbC lacks the external loop involved in the E. coli DsbA/DsbB interaction. Therefore the BdbC recycling role is inferred and no menaquinone-specific turnover or identical interface is asserted. Loss of oxidation can suppress CcdA deficiency; that does not make every oxidation event productive. The SpoVD/sporulation context is likewise not treated as a native positive biosynthesis function.

The current QuickGO definition of GO:0015035 is reversible: “Catalysis of the reaction: a protein with reduced sulfide groups = a protein with oxidized disulfide bonds.” Its label does not exclude oxidation. BdbD's specific Ca binding is supported by structure/metal analysis and a redox effect, not generic binding. Protein folding is supported by catalytic chemistry plus PhoA functionality; comparator oxidases E. coli DsbA and P. putida DsbA also carry this process.

PMID:20713508 and PMID:22882210 explicitly warn that detergent-resistant fractions are not equivalent to lipid rafts. Their primary B. subtilis background is NCIB3610; strain 168 is used for cloning. GO:0045121 specifies sterol/sphingolipid-enriched domains, so all inherited raft claims are UNDECIDED without denying bacterial microdomains. Plasma-membrane location is supported independently.

## Curation outcome

All original annotation payloads are preserved. Three justified additions: protein-disulfide reductase activity (oxidizing direction), calcium ion binding and protein folding. Only the catalytic oxidase role is core; calcium modulates it. All six original location rows remain.
