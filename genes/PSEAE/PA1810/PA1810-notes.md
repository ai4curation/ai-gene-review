# PA1810 (OppB) review notes

## Identity

- UniProt unreviewed entry, 615 aa, SBP_bac_5 (PF00496), Peptide/Ni-binding (IPR030678), PANTHER PTHR30290:SF64. SignalP signal peptide.
- The opp-fabI operon paper calls the gene oppB but gives no PA numbers. The protein lengths fix the mapping
  [PMID:23979749 "OppA (609 amino acids) and OppB (615 amino acids) are closely related (42.5% identity in CLUSTALW alignments)"]:
  Q9I2T3/PA1811 is 609 aa (OppA), Q9I2T4/PA1810 is 615 aa (OppB). PseudoCAP assigned the same IMP row to both loci.

## Literature

- Opp of P. aeruginosa is a binding protein-dependent ABC importer, oppA oppB oppC oppD oppE then fabI
  [PMID:23979749 "The first two genes, oppA and oppB , whose coding sequences overlap, contain type I signal peptides; thus, they are probably periplasmic binding proteins."].
- Both binding proteins are needed and neither substitutes for the other
  [PMID:23979749 "This mutant analysis also indicated that both OppA and OppB periplasmic binding proteins were required for pacidamycin uptake and that they cannot compensate for each other."].
  Here, the pacidamycin-resistant transposon mutant PAM1194 maps to oppB, and the unmarked oppB deletion PAO1284 is highly resistant while still expressing OppA.
- Opp transports a dipeptide
  [PMID:23979749 "The Opp system was shown to be a bona fide oligopeptide transport system by demonstrating that transport of PAβN is impaired in opp mutants."].
- The authors suggest a heteromeric binding protein
  [PMID:23979749 "indicative of an oligomeric binding protein requiring both OppA and OppB subunits"].

Literature search (2026-11-05): the PubMed MCP and NCBI E-utilities returned server errors all session, and
Europe PMC search was intermittently unavailable (HTTP 503), so the searches for "PA1811", "PA1810" and
"Pseudomonas aeruginosa Opp oligopeptide" returned nothing usable. The review rests on PMID:23979749 (full text
cached, PMC3811240, read in full), the UniProt record and QuickGO queries of the other seeds.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN008624512 | GO:0015833 peptide transport | 7 | 228 (38 taxa) | GO:0006857 oligopeptide transport, IMP, PMID:23979749 | SOUND | Full text read: defined oppB mutant loses uptake of the peptide antibiotic pacidamycin; Opp transports PAbetaN. A periplasmic binding protein takes part in transport directly. | E. coli OppA P23843 (IDA GO:0006857), DppA P23847 (IMP/EXP dipeptide transport), YejA P33913 (IDA GO:0006857), GsiB P75797 (EXP glutathione transport), MppA P77348 (EXP murein tripeptide transport); PA1811 (same PseudoCAP row) | Yes; five E. coli seeds with experimental annotations (QuickGO, 2026-11-05) |

No `source_defects` were recorded: the PseudoCAP row is sound, and the IBD is sound and suits a clade of
SBP family 5 peptide-binding proteins. The node is shared with PA1811; the assessment is the same on both
genes and is recorded in full here and in genes/PSEAE/PA1811/PA1811-notes.md.

Other IBA rows on this gene (not PseudoCAP-seeded):

- GO:1904680 peptide transmembrane transporter activity (PTN008624512, seeded by M. tuberculosis OppA P9WGU5, MTBBASE IDA): accepted.
- GO:0030288 outer membrane-bounded periplasmic space (PTN008624519, seed E. coli YejA): accepted.
- GO:0042884 microcin transport (PTN008624519, seeded only by E. coli YejA): marked as over-annotated. Microcin C uptake is
  a YejA substrate specificity; nothing links P. aeruginosa Opp to microcins. Not a PseudoCAP issue, so no defect is filed
  here; the node term is a candidate for PAINT review at that subnode.

## Action summary

ACCEPT 4 (GO:0006857 IMP, GO:0030288 IBA, GO:0043190 IEA, GO:1904680 IBA); TOO_GENERAL 2 (GO:0015833 IBA,
GO:0042597 IEA); MODIFY 1 (GO:0055085 to GO:0035672); MARK_AS_OVER_ANNOTATED 1 (GO:0042884 IBA).
