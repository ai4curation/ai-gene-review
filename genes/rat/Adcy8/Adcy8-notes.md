# Adcy8 (rat, P40146) review notes

## Session 1 (2026-10-28)

- fetch-gene resolved P40146 (Swiss-Prot ADCY8_RAT, RGD:2036, GeneID 29241); 142 GOA rows.
- No deep-research provider; literature compiled in `Adcy8-deep-research-manual.md`.
- Full text read: PMID:19305019, PMID:19158400, PMID:19444869, PMID:20410303, PMID:21771783,
  PMID:17335981 (mouse). The others are abstract-only in the cache.

### Core picture
Ca2+/calmodulin-stimulated transmembrane adenylyl cyclase (GO:0008294) of the plasma membrane
(raft/caveolar microdomains in non-excitable cells; presynaptic and extrasynaptic membrane in
neurons). It turns Ca2+ entry (store-operated via Orai1, or L-type channels) into cAMP/PKA signals
[PMID:8163524 "Adenylyl cyclase activity in membranes prepared from type VIII-transformed cells is
stimulated up to 40-fold by the addition of Ca2+/calmodulin"; PMID:19305019 "AC8 offers particularly
sophisticated regulatory possibilities"].

### Decisions worth flagging
- GO:0004016 rows MODIFIED to the more specific GO:0008294 (core MF, also carried by 7 rows).
- Postsynaptic density rows: Conti et al. (PMID:17335981) found AC8 "more robustly in the PAZ with
  only slight expression in the PSD". One rat ISS row derives from mouse Adcy1 (O88444), the paralog
  that is the PSD cyclase: recorded as a WRONG_WITH_FROM source defect.
- Neuroinflammatory response (from PMID:12441059, inflammatory pain/allodynia in AC1/8 DKO) and
  regulation of cellular response to stress (anxiety behaviour) look like wrong terms upstream;
  recorded as source defects (CHECK).
- GO:0010255 glucose mediated signaling pathway is defined via glucose-triggered gene expression;
  AC8's role is in glucose-evoked Ca2+/cAMP coincidence signalling, so MODIFY to GO:0071333.
- Apical/basolateral plasma membrane: mouse donor IDA (PMID:14585998) abstract-only and reports
  neuronal puncta; cannot verify a polarized epithelial assay: UNDECIDED.
- Clathrin-coated pit IDA (PMID:19158400): the full text only shows unglycosylated AC8 co-fractionating
  with beta-adaptin in non-raft membranes; MARK_AS_OVER_ANNOTATED.
- Bare protein binding: MODIFY where a specific MF exists (Orai1 -> transmembrane transporter binding;
  PRKAR2A -> PKA regulatory subunit binding; PPP2R5D -> PP2A binding), else REMOVE.
