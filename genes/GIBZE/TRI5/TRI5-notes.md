# TRI5 (Q00909, FGSG_03537) — Fusarium graminearum trichodiene synthase

## Identity
- Trichodiene synthase, EC 4.2.3.6, RHEA:12052; Pfam PF06330 (TRI5); UniProt: "catalyzes the isomerization and cyclization of farnesyl pyro-phosphate to form trichodiene, the first cyclic intermediate in the biosynthetic pathway for trichothecenes".
- Deep research: genes/GIBZE/TRI5/TRI5-deep-research-falcon.md (Edison/falcon).

## Molecular function
- [PMID:30664933 "The first step in DON synthesis is catalyzed by the sesquiterpene synthase (STS), Tri5 (trichodiene synthase), resulting in the cyclization of farnesyl diphosphate (FPP) to produce the sesquiterpene trichodiene."]
- Recombinant enzyme: [PMID:30664933 "Tri5 was cloned and expressed in E. coli and shown to produce primarily trichodiene in addition to minor, related cyclization products."]
- Non-catalytic role: [PMID:30664933 "Our results indicate that the Tri5 protein, but not its enzymatic activity, is also required for the synthesis of non-trichothecene related sesquiterpenes and the formation of toxisomes."] The proposed physical interaction with ER-anchored TRI1/TRI4/TRI11 is a model only.

## Location
- [PMID:30664933 "While it is established that Tri5 is a cytosolic enzyme (22,55,71) it also is enriched in the vicinity of the toxisome, seemingly within the layers of cytosol separating stacks of ER cisternae"]

## Pathway / virulence (indirect)
- [PMID:8589414 "The disrupted gene, Tri5, encodes the enzyme trichodiene synthase, which catalyzes the first step in trichothecene biosynthesis."]
- [PMID:18179606 "The tri5 mutant, which is unable to produce DON, exhibited reduced pathogenicity on wheat ears, causing only discrete eye-shaped lesions on spikelets which failed to infect the rachis."] Fully pathogenic on Arabidopsis floral tissue.
- [PMID:20507460 "all disruption mutants caused disease symptoms on the inoculated spikelet, but the symptoms did not spread into other spikelets."] Host- and chemotype-dependent.
- [PMID:38877764 "Deletion of TRI5 eliminates the ability of F. graminearum to synthesize DON"]
- Virulence is a property of DON (ribosome inhibitor acting in host cells), not of the TRI5 protein: necessity, not participation. No host-interaction BP term proposed.

## GO term checks (QuickGO, 2026-10-02)
- No "trichothecene biosynthetic process" term; GO:0106110 vomitoxin biosynthetic process (DON) exists, is_a descendant of GO:0016106 sesquiterpenoid biosynthetic process and GO:0043386 mycotoxin biosynthetic process.
- Comparator: GO:0106110 has a single annotation in GOA — to the TRI5 gene product under accession A0A1I9FCV5 (FG03537.1, TAS, PMID:38877764). So curators already apply this term to TRI5; used as MODIFY replacement for the InterPro IEA.

## Decisions
- GO:0016106 IEA -> MODIFY to GO:0106110.
- GO:0016838 IEA -> ACCEPT (correct EC 4.2.3 parent).
- GO:0045482 IEA, IMP -> ACCEPT.
- NEW GO:0005829 cytosol (TAS, PMID:30664933).
