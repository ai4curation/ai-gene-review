# RPL39 (YJL189W, P04650) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative of
Neurospora NCU08990 (Q7S2X9). No ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon yeast RPL39 --fallback perplexity-lite` failed:
falcon (Edison) raised "Failed to authenticate"; the perplexity-lite fallback
returned HTTP 401 insufficient_quota. No deep-research file exists. The review
is based on literature retrieved from PubMed (esearch for L39/eL39/Rpl39/SPB2 +
yeast + ribosome) and cached in `publications/`.

### Evolutionary grounding

- UniProt P04650: PANTHER PTHR19970:SF0 (LARGE RIBOSOMAL SUBUNIT PROTEIN EL39);
  InterPro IPR000077 Ribosomal_eL39; Pfam PF00832; PROSITE PS00051. 51 aa, initiator
  Met removed [UniProt FT INIT_MET, ECO:0000269|PubMed:10601260].
- Human RPL39 (P62891) is also SF0; human RPL39L (Q96EH5) is SF22 (RIBOSOMAL
  PROTEIN EL39-LIKE 2). Yeast has a single RPL39 gene (no A/B paralog pair).
- PAINT (interpro/panther/PTHR19970/PTHR19970-paint.tsv): root node PTN000463054
  carries IBD GO:0022625 (seeds include SGD:S000003725 = this gene), GO:0003735 and
  GO:0002181. A separate eutherian node PTN004522638 carries GO:0007283
  spermatogenesis (RPL39L/mouse Rpl39l seeds); that term was deliberately not placed
  at the root, so it does not apply to yeast or to fungal SF0 members.

### Experimental findings in S. cerevisiae

- Structural component of the 60S subunit: MS of purified LSU [PMID:11983894],
  80S crystal structure [PMID:22096102]; UniProt SUBUNIT/SUBCELLULAR LOCATION lines
  cite PMID:22096102 with ECO:0000269.
- Lines the nascent polypeptide exit tunnel: UV crosslinking shows Rpl39 contacts
  nascent signal-anchor and hydrophilic segments in the exit region of the tunnel
  [PMID:24072706 "the SA was in contact with Rpl17 in the middle region and with Rpl39
  in the exit region of the tunnel"].
- Non-essential. rpl39 deletion / spb2 mutants: 4-fold increased error frequency,
  increased A-site binding, paromomycin hypersensitivity, reduced 60S/40S ratio,
  cold sensitivity [PMID:10852723 "Each of the two L39 mutants displayed a 4-fold
  increase of their error frequencies over the wild type."]. Peptidyltransferase kcat
  slightly increased without L39 [PMID:11434779].
- spb2 (RPL46 = RPL39) deletion bypasses the requirement for Pab1 [PMID:2408148].
- Combined deletion of RPL31A, RPL31B and RPL39 is lethal; RPL39 is a multicopy
  suppressor of rpl31 double mutant [PMID:18829863].
- 60S assembly: eL39 required for efficient processing of 27SB and 7S pre-rRNA and
  nuclear export of pre-60S; co-purifies with 27SB/7S-containing pre-60S particles;
  rpl39Δ increases protein misfolding/aggregation [PMID:35639884, full text].
- Interacts (GST pull-down) with Yih1 [PMID:22404850, abstract only]. Note the GOA
  IPI row lists UniProtKB:O55091 (mouse IMPACT) in WITH, consistent with the abstract
  "GST-IMPACT ... coprecipitated Rpl39".

### Decisions

- Core: structural constituent of ribosome; part of cytosolic large ribosomal
  subunit; cytoplasmic translation. All accepted.
- NEW GO:0000027 ribosomal large subunit assembly (IMP, PMID:35639884). Participation
  test: eL39 is itself incorporated into pre-60S particles and its rRNA contacts are
  needed for maturation (structural participation in assembly, not mere necessity of
  a substrate). Comparator check (QuickGO, taxon 559292): SGD annotates many yeast
  r-proteins to GO:0000027 by IMP (RPL3, RPL5, RPL10, RPL11A/B, RPL25, RPL33A,
  RPL40A/B, RPL15A/B, RPL36A/B...), so the convention exists for this role.
- Not added: protein folding / translational fidelity process terms (consequences of
  tunnel structure; kept in description and suggested questions).
- protein binding (Yih1/IMPACT) handled per protein-binding policy (REMOVE).
- Generic cytoplasm / ribosome / translation rows: MODIFY to the specific terms
  already carried (cytosolic large ribosomal subunit; cytoplasmic translation).
- Reactome cytosol rows: KEEP_AS_NON_CORE (correct, ribosome is cytosolic).
