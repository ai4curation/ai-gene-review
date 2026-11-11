# Abhd14a (rat) — review notes

Family-coordinated review of rat `Abhd14a` (`UniProtKB:Q5I0C4`, `RGD:1309721`, `PANTHER:PTHR46197:SF1`, 242 aa).

## 1. Orthology, membrane topology, and `PMID:42469586` attribution

Rat `Abhd14a` (`Q5I0C4`, 242 aa, `sequence_version: 1`) is the 1:1 mammalian ortholog of human `ABHD14A` (`Q9BUJ0`) and mouse `Abhd14a` (`Q922Q6`, *Dorz1*) in `PANTHER:PTHR46197:SF1` (`PROTEIN ABHD14A`). Like human and mouse ABHD14A, it has an N-terminal type II signal-anchor transmembrane segment (`FT TRANSMEM 6..26`), lumenal N-glycosylation (`Asn38`), and an intact Ser142-Asp193-His220 alpha/beta-hydrolase catalytic triad oriented toward the secretory lumen rather than the cytosol.

## 2. Review of the 6 existing GOA rows

1. **`GO:0000139` (`Golgi membrane`, `IDA` `PMID:42469586`, assigned by UniProt) -> `KEEP_AS_NON_CORE` (with `source_defects` `CHECK` on `UNIPROT`)**:
   - `PMID:42469586` (Gupta, Dhaware & Kamat, *Biochemistry* Aug 2026) is abstract-only in our cache (`full_text_available: false`). Its abstract explicitly states: *"Here, we provide the first functional characterization of the human enzyme ABHD14A... heterologous overexpression of an ABHD14A-GFP fusion variant in HEK293T cells was performed. Here, we found that the ABHD14A-GFP fusion protein is catalytically active and localizes specifically to the Golgi apparatus"*.
   - Per `AGENTS.md` ("Do not overrule curators from incomplete evidence"), we do **not** `REMOVE` this experimental `IDA` row because the full text may also include a rat construct or rat cell assay; however, we mark it `KEEP_AS_NON_CORE` (overexpressed GFP fusion localization, endogenous physiological function still unknown) and record a `PROBABLE` `source_defects` (`CHECK`, `resource: UNIPROT`) asking UniProt to verify whether the `IDA` from `PMID:42469586` assayed rat `Q5I0C4` directly or human `Q9BUJ0` (in which case rat `Q5I0C4` should carry `ISS` from `Q9BUJ0` rather than `IDA`).
2. **`GO:0016020` (`membrane`, `IEA` `GO_REF:0000044`) -> `MARK_AS_OVER_ANNOTATED`**:
   - Harmonized with human `ABHD14A` (`Q9BUJ0`) and mouse `Abhd14a` (`Q922Q6`).
3. **`GO:0005737` (`cytoplasm`, `IBA` `PTN002475422`, `IEA` `GO_REF:0000044`, `ISO` `GO_REF:0000121` from `MGI:MGI:1915894`) -> `ACCEPT` (harmonized with `human/ABHD14A` and `mouse/Abhd14a`)**:
   - Retained consistently across all `SF1` orthologs with the explicit topological caveat that only the short N-terminal tail of this type II membrane protein is cytoplasmic whereas the Ser142-Asp193-His220 catalytic domain faces the Golgi/secretory lumen.
4. **`GO:0016407` (`acetyltransferase activity`, `ISS` `GO_REF:0000024` from `UniProtKB:Q9BUJ0`) -> `MARK_AS_OVER_ANNOTATED`**:
   - Based on CoA-enhanced cleavage of synthetic *p*-nitrophenyl acetate by an engineered N-terminally truncated human ABHD14A construct in vitro (`PMID:42469586`), with no physiological acetyl donor or acceptor identified; marked `MARK_AS_OVER_ANNOTATED` per `projects/ENZYME_SPECIFICITY.md` and harmonized with mouse `Abhd14a`.
