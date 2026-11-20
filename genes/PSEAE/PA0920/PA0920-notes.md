# PA0920 (Q9I537) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol, worklist rank 37)

No deep-research provider was available; these notes are my own reading of the UniProt record, the cited
paper and four further Braunschweig (Moser lab) papers found by PubMed search and cached with
`just fetch-pmid`. Only PMID:21392131 has full text in the cache; the others are abstract-only (the PubMed
MCP returned no PMC full text for PMC4553816 beyond the abstract and Significance statement).

## Identity

- *P. aeruginosa* PAO1 locus PA0920, UniProt Q9I537 (unreviewed), 881 aa; 14 predicted TM helices
  (residues 36-542) followed by the cytoplasmic LPG_synthase_C catalytic domain (Pfam PF09924, residues
  565-853); Pfam PF03706 LPG_synthase_TM; NCBIfam NF033480 bifunc_MprF; PANTHER PTHR34697:SF2.
- The UniProt name "Phosphatidylglycerol lysyltransferase" (EC 2.3.2.3) and the lysyl-tRNA catalytic
  activity line are ARBA predictions (ECO:0000256|ARBA). They are wrong for this protein: PA0920 is the
  alanyl-phosphatidylglycerol synthase (A-PGS).

## Literature

- Discovery: *P. aeruginosa* makes alanyl-PG under acidic growth [PMID:19087229 "The opportunistic bacterium
  Pseudomonas aeruginosa synthesizes significant amounts of an additional phospholipid, identified as 2'
  alanyl-phosphatidylglycerol (A-PG), when exposed to acidic growth conditions."]. Deletion abolishes it
  [PMID:19087229 "The P. aeruginosa deletion mutant DeltaPA0920 failed to synthesize A-PG."] and
  heterologous expression confers it on *E. coli* [PMID:19087229 "Heterologous overproduction of PA0920 in
  Escherichia coli resulted in the formation of significant amounts of A-PG, otherwise not synthesized by E.
  coli."]. In vitro activity [PMID:19087229 "tRNA(Ala)-dependent catalysis was demonstrated."]; inner
  membrane location [PMID:19087229 "The enzyme was identified as an integral component of the inner
  membrane."]; acid-induced transcription [PMID:19087229 "indicated a 4.4-fold acid-activated
  transcription"].
- Mechanism: the C-terminal domain is the minimal catalytic core [PMID:21392131 "identify the minimal core
  domain of this transmembrane protein, which is capable of alanyl-phosphatidylglycerol biosynthesis"]; the
  PG head group is specifically recognised [PMID:21392131 "the polar head group of the phospholipid is
  specifically recognized by the enzyme"]. Immunogold places the epitope at the cytosolic face of the inner
  membrane [PMID:21392131 "almost exclusively decorate the cytosolic part of the inner membrane"].
- Structure (the PseudoCAP-cited paper): crystal structure of the A-PGS catalytic domain, tunnel for PG and
  aminoacyl-tRNA, substrate recognition with misacylated tRNAs [PMID:26261323 "Here we present the X-ray
  crystallographic structure of the catalytic domain of A-PGS from the opportunistic human pathogen
  Pseudomonas aeruginosa."]; [PMID:26261323 "Substrate recognition of A-PGS versus L-PGS was investigated
  using misacylated tRNA variants."]. "Lipid homeostasis" appears only in the general framing
  [PMID:26261323 "Lipid homeostasis is a fundamental process for understanding antimicrobial
  susceptibility."]; the paper does not measure lipid levels or their maintenance in cells.
- Specificity: P. aeruginosa naturally makes A-PG, not L-PG [PMID:22267511 "chimeric mutant strains
  producing lysyl-phosphatidylglycerol (L-PG) instead of the naturally occurring alanyl-phosphatidylglycerol
  (A-PG)"]. A-PGS and L-PGS specificity is not encoded in an obvious motif [PMID:22267511 "the specificity of
  an individual enzyme is not reflected in terms of a characteristic sequence motif"], a caution for
  propagating the alanyl-specific term by phylogeny.
- Homeostasis is set by a second enzyme: the periplasmic A-PG hydrolase PA0919, encoded downstream, tunes
  A-PG levels [PMID:23792962 "Analysis of the polar lipid content of the deletion mutant ΔPA0919 indicated
  significantly enlarged levels of alanyl-PG."]; [PMID:23792962 "The elucidated enzymatic activity implies a
  new regulatory circuit for the appropriate tuning of cellular alanyl-PG concentrations."].

## Is 'phospholipid homeostasis' PA0920's own process?

No. GO:0055091 is the maintenance of a steady-state phospholipid level. PA0920 performs one biosynthetic
step: it transfers alanine from Ala-tRNA(Ala) to PG, making A-PG. The steady state (acid-dependent level of
A-PG) emerges from the synthase together with acid-regulated transcription and the PA0919 hydrolase; the
"lipid homeostasis" wording in the cited paper's abstract is framing, not a reported result (full text not read). The gene's own process is A-PG
synthesis, i.e. GO:0008654 phospholipid biosynthetic process (no aminoacyl-PG-specific GO term exists; an
NTR could be requested). The homeostasis term is therefore a consequence-level over-annotation for PA0920.

It is worse at the node: QuickGO (2026-10-28) shows PTN002162750 passes GO:0055091 to 26 leaves, among
them the fungal ergosteryl-3beta-O-glycine synthases ErgS of *Aspergillus fumigatus* (Q4WB70) and
*Yarrowia lipolytica* (Q6C7J3), whose UniProt function (PubMed:35131263) is tRNA-dependent glycylation of
ergosterol, a sterol, not a phospholipid. The leaves also include *S. aureus*, *B. subtilis* and *Listeria*
MprF (L-PGS), *M. tuberculosis* LysX2 (Rv1619), *Streptomyces* and green-algal proteins. None of the
comparator leaves carries an experimental GO annotation; all their function annotations come from PA0920.

## Annotation decisions

- GO:0047637 phosphatidylglycerol alanyltransferase activity (IDA PseudoCAP; IBA): ACCEPT, core MF.
- GO:0050071 phosphatidylglycerol lysyltransferase activity (IEA from ARBA EC 2.3.2.3): REMOVE; the enzyme
  is the alanyl-specific synthase and P. aeruginosa makes no L-PG. Defect recorded against UniProt/ARBA.
- GO:0055091 phospholipid homeostasis (IDA PseudoCAP; IBA): MODIFY to GO:0008654 phospholipid
  biosynthetic process. PseudoCAP and GO_CENTRAL defects recorded.
- GO:0005886 plasma membrane (IEA SubCell): ACCEPT; direct evidence (PMID:19087229, PMID:21392131).

## PseudoCAP IBA-seed assessment

Leaf counts in QuickGO (2026-10-28) differ from the worklist (older PAINT release): PTN002162750 now carries
26 GO:0055091 and 24 GO:0016755 leaves; PTN005059806 carries 55 GO:0047637 leaves (diverse bacteria,
Myxococcus, Planctomycetes, the archaeon Methanosarcina acetivorans Q8TMG3), each also getting the two
upper-node terms.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002162750 | GO:0055091 phospholipid homeostasis | 1 (sole) | 14 (12 taxa) in worklist; 26 in QuickGO | GO:0055091, IDA, PMID:26261323 (PseudoCAP) | WRONG | The abstract describes a crystal structure and in vitro substrate-recognition study and no homeostasis data (full text not read). PA0920's own process is A-PG biosynthesis; homeostasis is a system-level consequence involving the PA0919 hydrolase. The node also contains ergosteryl-glycine synthases (ErgS) that do not modify phospholipids, so the term is wrong for part of the clade even if read loosely. |
| PTN002162750 | GO:0016755 aminoacyltransferase activity | 1 (sole) | 12 (10 taxa) in worklist; 24 in QuickGO | GO:0047637, IDA, PMID:26261323 (PseudoCAP) | SOUND | Direct in vitro tRNA-dependent alanylation of PG by the A-PGS catalytic domain (also PMID:19087229, PMID:21392131). The generic aminoacyl-transfer term fits every known member (A-PGS, L-PGS, ErgS all transfer an aminoacyl group from aminoacyl-tRNA to a lipid). |
| PTN005059806 | GO:0047637 phosphatidylglycerol alanyltransferase activity | 1 (sole) | 2 (2 taxa) in worklist; 55 in QuickGO | GO:0047637, IDA, PMID:26261323 (PseudoCAP) | SOUND | Seed is direct biochemistry, and A-PGS sequences form a recognisable group (PMID:22267511). Caveat: Arendt et al. report that A-PG vs L-PG specificity is not marked by a sequence motif, so with one seed and now 55 leaves the alanyl-specific node term should be re-checked against the nine orthologs whose specificity that paper determined. |

## Audit 2026-10-29: confidence matched to what was read

PMID:26261323 is still abstract-only: the PubMed MCP returns abstract and
Significance only for PMC4553816, and PMC/Europe PMC/PNAS full text was not
retrievable. The PSEUDOCAP WRONG_TERM defect (homeostasis IDA -> phospholipid
biosynthetic process) rests on the abstract describing no homeostasis assay,
so it is lowered from PROBABLE to SUSPECTED. The GO_CENTRAL defect on
PTN002162750 stays PROBABLE: besides the seed paper, it rests on positive
facts (QuickGO leaves include sterol-modifying ErgS enzymes). The UNIPROT EC
defect stays CONFIRMED: the PMID:19087229 abstract states the decisive fact
outright (DeltaPA0920 loses A-PG; the protein was named A-PG synthase).
PMID:26261323 reference correctness changed from MISCITED to UNVERIFIED.
No action changes.
