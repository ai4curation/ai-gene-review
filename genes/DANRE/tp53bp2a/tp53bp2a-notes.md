# tp53bp2a notes

## Setup and provenance

- Fetched with `just fetch-gene` on F1R419 (TrEMBL, "apoptosis-stimulating of p53 protein 2a
  isoform X1", 1060 aa); 11 GOA rows (6 IBA-derived rows incl. IBA/IEA duplicates, 2 IMP from
  PMID:24362258). ZFIN ZDB-GENE-040516-8, Ensembl ENSDARG00000009136, chromosome 13.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid, so no `-deep-research-*.md` was generated. Literature searched by hand via Europe PMC
  (queries: `"tp53bp2a"`, `"tp53bp2b"`, `"aspp2a"`, `"aspp2b"`, `zebrafish AND "ASPP2"`,
  title searches for ASPP2/53BP2 and p53, Par-3, polarity).
- Part of DANRE_DUPLICATION batch 4 (random sample, seed 20260928); paralog tp53bp2b. Ensembl
  Compara dates the tp53bp2a/tp53bp2b duplication to Osteoglossocephalai (teleost level); gar
  ENSLOCG00000015726 is a one-to-many orthologue of both copies; medaka one-to-one orthologues are
  ENSORLG00000007284 (tp53bp2a) and ENSORLG00000000954 (tp53bp2b) (Ensembl REST, 2026-09-28).

## Zebrafish literature

Only one functional paper studies either copy, and it studies both together (abstract only in cache):

- Knockdown/overexpression: both copies restrain embryonic growth, not developmental timing
  [PMID:24362258 "Here, we show that zebrafish Aspp2a and Aspp2b negatively regulate embryonic growth without affecting developmental rate."]
- Both inhibit Akt signalling, reversed by active Akt
  [PMID:24362258 "Aspp2a and 2b inhibit Akt signaling. This inhibition was reversed by coinjection of myr-Akt1, a constitutively active form of Akt1."]
- Both bind Irs-1; the effect needs the ankyrin repeats and SH3 domain
  [PMID:24362258 "Zebrafish Aspp2a and Aspp2b physically bound with Irs-1, and the growth inhibitory effects of ASPP2/Aspp2 depend on the presence of their ankyrin repeats and SH3 domains."]
- Human ASPP2 acts the same way in fish
  [PMID:24362258 "Human ASPP2 had similar effects on body growth in zebrafish embryos."]
- ZFIN curates RT-PCR and whole-mount in situ data from this paper for both copies
  (ZDB-PUB-140220-26): both detected in all ten adult tissues tested and throughout development,
  with whole-organism in situ annotations only (no restricted domain recorded)
  ([output.txt](tp53bp2a-bioinformatics/output.txt), section 6).
- No mutant, morphant-only phenotype on apoptosis, or p53 interaction has been reported for
  either zebrafish copy.

## Mammalian ASPP2 (ancestral function)

- ASPP family defined as p53 cofactors for apoptosis
  [PMID:11684014 "ASPP proteins interact with p53 and specifically enhance p53-induced apoptosis but not cell cycle arrest."]
- Structure: ankyrin repeats + SH3 bind the p53 DNA-binding core
  [PMID:8875926 "The crystal structure of the p53 core domain bound to the 53BP2 protein, which contains an SH3 (Src homology 3) domain and four ankyrin repeats, revealed that (i) the SH3 domain binds the L3 loop of p53 in a manner distinct from that of previously characterized SH3-polyproline peptide complexes, and (ii) an ankyrin repeat, which forms an L-shaped structure consisting of a beta hairpin and two alpha helices, binds the L2 loop of p53."]
- Polarity / junctions: binds Par-3, maintains tight/adherens junctions
  [PMID:20619750 "Mechanistically, ASPP2 maintains the integrity of tight/adherens junctions."]
  [PMID:20619750 "ASPP2 binds Par-3 and controls its apical/junctional localization without affecting its expression or Par-3/aPKC lambda binding."]
- PP1/YAP scaffold at tight junctions
  [PMID:25360797 "Here we report that the tumour suppressor ASPP2 forms an apical-lateral polarity complex at the level of tight junctions in polarised epithelial cells, acting as a scaffold for protein phosphatase 1 (PP1) and junctional YAP via dedicated binding domains."]

## Own analysis (tp53bp2a-bioinformatics/)

See [RESULTS.md](tp53bp2a-bioinformatics/RESULTS.md). Summary: the copies are 60.9% identical
overall, each ~60% identical to human TP53BP2, but the four ankyrin repeats are 90-100% identical
to human in both; the SH3 domain and the N-terminal Ras-associating (ubiquitin-like) domain are
present in both. Divergence is concentrated in the disordered middle region. Relative-rate test
against gar not significant. Expression: tp53bp2a dominates from gastrula to larva in the whole-
embryo time course (e.g. 91 vs 4 TPM at 50% epiboly); both are maternally provided, tp53bp2b drops
during gastrulation and organogenesis and rises again in larvae; both have broad adult Bgee calls,
tp53bp2a usually higher. No conserved local synteny was detected between the two copies.

## Curation decisions (summary)

- p53 binding (IBA, IEA): accept - ankyrin/SH3 p53-binding module intact.
- IMP rows from PMID:24362258: accept negative regulation of PI3K/AKT; modify chordate embryonic
  development to negative regulation of multicellular organism growth (the paper's actual claim).
- NEW: insulin receptor substrate binding (IPI, PMID:24362258).
- signal transduction (IEA via RA domain) modified to the specific PI3K/AKT term.
- nucleus / perinuclear: kept as non-core (ASPP2 is mainly cytoplasmic/junctional).
