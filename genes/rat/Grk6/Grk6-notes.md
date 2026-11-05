# Grk6 (rat) review notes

## Accession
The task named the unreviewed TrEMBL entry A0ABK0L927. `just fetch-gene rat Grk6` resolved the
Swiss-Prot entry P97711 instead. Both are Grk6 with the same RGD id (RGD:61986) and GeneID 59076
(A0ABK0L927 record checked via UniProt REST), and the GOA file is keyed to P97711, so P97711 was
reviewed.

## Evidence summary
- Core: GPCR kinase activity (GO:0004703), mediating homologous desensitization of GPCR signaling
  (GO:0002029). Rat-specific experimental support: beta-AR desensitization in myometrial cells
  [PMID:12810562 "These results strongly suggest that endogenous GRK6 mediate homologous beta-AR
  desensitization in myometrial cells."]; M1 mAChR desensitization in hippocampal neurons
  [PMID:15115810 "overexpression of wild-type GRK6 increased receptor desensitization"];
  partial contribution under picrotoxin [PMID:17908240 "inhibition of endogenous GRK6 appeared to
  partially prevent picrotoxin-enhanced M1 mACh receptor desensitization (Fig. 3e)."].
- Location: palmitoylation-dependent membrane association [PMID:7961702; PMID:9819198]; substrates
  are plasma-membrane GPCRs; the generic membrane row was refined to plasma membrane.
- Beta-adrenergic receptor kinase activity (GO:0047696) is a sibling of, not a child of,
  GO:0004703 in GO (checked with OAK); supported by in vitro phosphorylation of beta2AR by GRK6
  [PMID:9819198] and by the rat myometrium study.
- LPS response row is expression-only (IEP) -> over-annotation.
- General kinase terms (protein kinase activity, Ser/Thr kinase activity) refined to GO:0004703;
  signal transduction and regulation of signal transduction refined to GO:0002029.

## Decisions on PMID:12810562 IDA rows
Abstract only; the abstract reports dominant-negative and antibody inhibition experiments (which
would usually be IMP). Curators had the full text; function is well established for GRK6, so
accepted and deferred to the curator.
