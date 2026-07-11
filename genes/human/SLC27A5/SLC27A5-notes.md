# SLC27A5 (BACS / FATP5 / VLCS-H2) review notes

UniProtKB: Q9Y2P5. Human, liver-specific.

## Core biology (grounded in UniProt + cached primary literature)

SLC27A5 encodes bile acyl-CoA synthetase (BACS; also FATP5, VLCS-H2 / VLACS-related).
It is a member of the ATP-dependent AMP-binding enzyme (acyl-CoA synthetase) family and
is predominantly expressed in liver ([PMID:10479480 "hVLCS-H2 is expressed primarily in
liver"]).

Molecular function: ATP-dependent activation (thioesterification to CoA) of substrates.
- **Bile acids (its principal physiological role):** activates the primary C24 bile acids
  cholate and chenodeoxycholate, and the secondary bile acids deoxycholate and
  lithocholate, to their CoA thioesters — the obligatory step before BAAT-catalysed
  glycine/taurine conjugation ([PMID:10749848 "Unconjugated bile acids must be activated
  to their CoA thioesters before conjugation to taurine or glycine can occur"];
  [PMID:11980911 "this enzyme also activates chenodeoxycholate, the secondary bile acids
  deoxycholate and lithocholate"]). Km = 2.8 uM for cholate (UniProt).
- Also activates the C27 precursor THCA in vitro ([PMID:11980911]).
- **Long-chain / very-long-chain fatty acids:** activates C18:0, C20:0, C24:0, C26:0
  to acyl-CoA ([PMID:10479480 "For all substrates tested (C18:0, C20:0, C24:0, C26:0),
  the hVLCS-H2 catalyzed activity was significantly increased"]). EC 6.2.1.3 (LCFA) and
  6.2.1.7 (cholate-CoA / choloyl-CoA synthetase).

Biological process:
- Bile acid **re-activation and re-conjugation / recycling** from the enterohepatic
  circulation is the proposed primary function; NOT de novo bile acid synthesis
  ([PMID:10749848 "consistent with a role for hVLCS-H2 in the re-activation and
  re-conjugation of bile acids entering liver from the enterohepatic circulation rather
  than in de novo bile acid synthesis"]; [PMID:11980911 "the primary function of homolog
  2 is in the reactivation and recycling of C24 bile acids"]). UniProt: "Plays an
  important role in hepatic fatty acid uptake and bile acid reconjugation and recycling
  but not in de novo synthesis of bile acids".
- Hepatic long-chain fatty-acid uptake / import: FATP5 contributes to LCFA uptake into
  liver ([PMID:20530735 "LCFA uptake was reduced by 40%"] — note this paper's knockdown
  is FATP2; the fatty-acid transport role of FATP5 is from PMID:20448275/UniProt].

Subcellular location: Endoplasmic reticulum membrane, multi-pass membrane protein
([PMID:10479480 "the protein was associated with the endoplasmic reticulum but not with
peroxisomes"]; UniProt SUBCELLULAR LOCATION "Endoplasmic reticulum membrane ... Cell
membrane"). Topology: N-terminal cytoplasmic, two TM helices (31-51, 56-76), then a large
cytoplasmic catalytic domain (77-690) ([PMID:11980911 topology]).

## Annotation decisions

- MF core: cholate-CoA ligase (GO:0047747) IDA from PMID:10749848 — ACCEPT, core.
- MF core: long-chain fatty acid-CoA ligase (GO:0004467) — ACCEPT (IBA/TAS/IEA); core.
- MF: very long-chain fatty acid-CoA ligase (GO:0031957) IDA (PMID:10479480, 11980911) —
  ACCEPT; supported by C24:0/C26:0 activation.
- BP core: bile acid biosynthetic process (GO:0006699) IDA PMID:11980911 + Reactome TAS —
  ACCEPT (this is the pathway to which CoA activation contributes).
- BP: bile acid metabolic process (GO:0008206) — ACCEPT (broader, correct).
- LCFA transport / import / transmembrane transporter activity — the "transporter"
  interpretation of FATPs is debated (many argue FATPs drive uptake via
  vectorial acylation, i.e. the synthetase activity, not a channel). The IBA/IDA
  transporter-activity annotations are kept but not treated as the core MF. IDA
  GO:0005324 from PMID:20530735 is a genuine transport-activity assay; ACCEPT/keep
  non-core.
- Plasma membrane (IBA, IEA): keep non-core; minor PM pool for FA uptake.
- protein binding GO:0005515 IPI (PMID:32296183, HuRI high-throughput, MEOX2): bare
  protein binding, high-throughput Y2H, no functional interpretation -> MARK_AS_OVER_ANNOTATED.
- Ensembl-projected (GO_REF:0000107) protein-containing complex / complex binding: no
  evidence SLC27A5 acts in a stable complex; ortholog-projected, uninformative ->
  MARK_AS_OVER_ANNOTATED.
- fatty acid transmembrane transporter activity GO:0015245 (ARBA IEA): redundant/less
  precise generic transporter term -> MARK_AS_OVER_ANNOTATED.

## Reactome
- R-HSA-159425 / 192137 / 193407 / 193711: SLC27A5 (BACS) CoA-conjugation reactions on
  ER membrane (cytosolic substrates). Titles as in cache.
- R-HSA-193766: not found in current Reactome ContentService (404) and cache empty;
  retired reaction id. Kept as-is with a descriptive title; flagged UNVERIFIED.
</content>
</invoke>
