# infB (IF2, P0A705) - Escherichia coli K-12 - review notes

## Identity

- UniProt P0A705, IF2_ECOLI, 890 aa, gene infB (b3168, JW3137); synonyms gicD, ssyG.
- Family: "Belongs to the TRAFAC class translation factor GTPase superfamily. Classic translation factor GTPase family. IF-2 subfamily." [file:ECOLI/infB/infB-uniprot.txt]
- PANTHER PTHR43381 (TRANSLATION INITIATION FACTOR IF-2-RELATED), subfamily PTHR43381:SF5. This family unites bacterial IF2 with the archaeal/eukaryotic aIF5B/eIF5B (yeast FUN12, human EIF5B), which is the true ortholog of IF2. Note that eukaryotic eIF2 (a heterotrimer whose gamma subunit is an EF-Tu-like GTPase) is NOT the IF2 ortholog despite the similar name.
- Mechanistic support for the eIF5B analogy: "The mechanism of action of IF2 seems to be different from that of tRNA carriers such as EF-Tu, SelB and eukaryotic initiation factor 2 (eIF2), instead resembling that of eIF5B, the eukaryotic subunit association factor." [PMID:20224578]
- Domain organisation (UniProt FT): disordered N-terminal region (MobiDB-lite, residues 45-304; N domain carries IF2_N repeats), tr-type G domain 389-558 with G1-G5 motifs, beta-barrel domain II, C-terminal domains (C1/C2; region 669-890 binds fMet-tRNA acceptor end in the literature).
- Three isoforms from alternative in-frame translation starts: alpha (codon 1), beta (GUG codon 158) and beta' (AUG codon 165) [PMID:1764105 "IF2 beta exists in two forms, IF2 beta and IF2 beta' with initiation codons 158 (GUG) and 165 (AUG)"]. Both alpha and beta forms are needed for optimal growth [PMID:1374802 "both forms of IF2 are required for maximal growth of the cell"].
- Essential gene: "Essential, it cannot be deleted." [file:ECOLI/infB/infB-uniprot.txt, CC DISRUPTION PHENOTYPE]

## Core biochemistry

- Essential initiation factor: "One of the essential components for the initiation of protein synthesis" [file:ECOLI/infB/infB-uniprot.txt CC FUNCTION]. Classic 1968-1971 reconstitution papers (PMID:4872321, PMID:4876939; no abstracts cached) established IF2 as one of three protein factors required for initiation-complex formation.
- fMet-tRNA binding: "Evidence is presented that suggests the formation of a complex between polypeptide chain-initiation factor IF 2, GTP, and fMet-tRNA(f)." [PMID:4943554]. The ternary complex is unstable in solution; on the kinetically preferred pathway IF2-GTP binds the 30S first and then recruits fMet-tRNA: "binding of IF2.GTP to the 30S ribosomal subunit precedes and is independent of fMet-tRNA(fMet) binding" [PMID:20224578]. IF2 thus has initiator-tRNA binding activity but acts on the ribosome rather than as a free carrier. Petersen et al. 1979 (PMID:393258, title only) reported specific interaction with fMet-tRNA(fMet).
- 30S binding: IF2 binds the 30S subunit through two sites - an N-domain "anchor" and a core interaction via the EF-Tu/EF-G domain II homolog: "using two separate active sites, IF2 establishes two interactions with the 30 S ribosomal subunit which have different properties and functions" [PMID:16935296]. IF2 and IF3 are the first factors to arrive on the 30S: "IF3 and IF2 are the first factors to arrive, forming an unstable 30S-IF2-IF3 complex." [PMID:22562136]
- GTPase: ribosome-dependent GTPase (PMID:4337107, title only: "Characterization of the ribosome-dependent guanosine triphosphatase activity of polypeptide chain initiation factor IF 2"). Kinetics: "IF2-dependent GTP hydrolysis was fast (30/s) followed by slow P(i) release from the complex (1.5/s)." [PMID:10790378]. UniProt: "Also involved in the hydrolysis of GTP during the formation of the 70S ribosomal complex." Interestingly GTP hydrolysis is not needed for fMet-tRNA adjustment or IF2 release per PMID:10790378 ("neither the adjustment of fMet-tRNA(fMet) in the P site nor the release of IF2 from the ribosome required GTP hydrolysis").
- Ribosomal stalk L12 CTD binds IF2 (NMR) [PMID:17070545 "L12 binds directly to the factors IF2, EF-Tu, EF-G, and RF3"] - a GTPase-factor recruitment contact shared by all translational GTPases; captured in GO only as bare protein binding (removed per policy).

## Regulatory / stress features

- ppGpp binding: "IF2 binds ppGpp at the same nucleotide-binding site and with similar affinity as GTP" and "ppGpp interferes with IF2-dependent initiation complex formation" [PMID:16968770]. ppGpp capture-compound proteomics recovered IF2 among translational GTPases: "For EF-G, EF-Tu, and IF2, the binding of ppGpp instead of GTP disrupts translation in vitro" [PMID:30559427]. Real, regulatory ligand binding (stringent-response coupling), not the evolved core activity -> non-core.
- Cold: IF2 levels rise ~3-fold relative to ribosomes after cold shock via promoter activation, mRNA stabilisation and translational bias [PMID:30916329 "the increased level of IF2 following cold stress depends on three mechanisms"]. Extra IF2 associates with immature ribosomal subunits; IF2 deltaN and GTPase-dead (E571K) mutants are cold-sensitive and accumulate immature particles [PMID:30916323 "two cold-sensitive IF2 mutations cause the accumulation of immature ribosomal particles"]. The N-terminal IDR is required for growth at 15 C and drives cold-induced phase separation with RNA [PMID:39975289 "this IDR was found to be required for growth at cold temperatures (15°C)"; "IF2's N-terminal IDR drives phase separation in E. coli and C. crescentus"]. In vivo, "when cells were cold-shocked for 1-hour we observed that IF2 localized into distinct puncta" [PMID:39975289]. PMID:39975289 is a bioRxiv preprint. Its discussion compares IF2 to eukaryotic eIF2alpha/beta/gamma; that analogy is about stress-granule biology, not orthology (the ortholog is eIF5B).
- The cold-sensitivity mutations (deltaN, E571K) also impair initiation (PMID:16935296 shows deltaN has altered IF1/GTP dependence), so the ribosome-assembly interpretation is plausible but not separable from initiation defects. I did not add ribosome assembly as a NEW term.

## Chaperone-like activity

- Caldas et al. 2000: IF2 and EF-G "promote the functional folding of citrate synthase and alpha-glucosidase after urea denaturation" and the authors conclude they "might be implicated in protein folding and protection from stress" [PMID:10625618, abstract only].
- Brandi et al. 2019: "IF2 is endowed with GTPase-associated chaperone activity that promotes refolding of denatured GFP" [PMID:30916323]; assays used S30R GFP model substrate in vitro.
- Judgement: real in vitro activity on model substrates, physiological relevance (e.g. for r-protein/rRNA folding during cold assembly) not established -> MARK_AS_OVER_ANNOTATED for GO:0006457 rows, consistent with the ENZYME_SPECIFICITY tier "real in vitro activity of unknown relevance".

## Localization

- UniProt: "Cytoplasm" (PMID:1764105). Cytosolic fraction proteomics (PMID:18304323, HDA-type, annotated IDA). Soluble ribosome-associated factor, no TM segments; a membrane-fraction detection in BN-PAGE complexome (PMID:16858726) most plausibly reflects co-sedimenting ribosomes/polysomes -> MARK_AS_OVER_ANNOTATED.
- Cytoplasm rows (EXP, IBA, IEA) are correct but general; the gene already carries cytosol (IDA, IBA) -> MODIFY to GO:0005829.

## PAINT

- `just paint-losses ECOLI infB`: "No IRD or IKR loss on this gene's lineage." IBA rows for GO:0003743, GO:0006413, GO:0005737 (PTN001897651) and GO:0005829 (PTN000562019) are on the IF2/eIF5B lineage, sound.

## Literature searched

Cached PubMed records for all GOA references (PMID:4872321, 4876939, 4943554, 4337107, 1764105, 10625618, 16858726, 16935296, 16968770, 17070545, 18304323, 30559427, 30916323, 30916329, 39975289) plus UniProt-cited PMID:393258, 1374802, 20224578, 22562136 and kinetic PMID:10790378.
