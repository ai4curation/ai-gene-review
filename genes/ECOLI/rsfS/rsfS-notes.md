# rsfS notes (P0AAT6)

## 2026-10-28 review session
- fetch-gene resolved P0AAT6 (IOJAP_ECOLI, GeneID 945237); GOA has 19 rows (18 stub entries; duplicated IDA rows from PMID:22829778 assigned by both EcoCyc and UniProt collapse).
- PMID:22829778 full text read. Core: binds uL14 on 50S, blocks 30S joining, inhibits translation in vitro and in stationary phase in vivo
  [PMID:22829778 "We conclude that RsfA blocks association of the ribosomal subunits to functional 70S ribosomes."].
- Deletion has no visible assembly defect [PMID:22829778 "Our results do not indicate any assembly defects as deletion strains of rsfA appear to have perfectly assembled ribosomes"],
  but RsfS sits on late pre-50S with ObgE/RluD/DarP [PMID:33639093, abstract only] and accumulates on pre-50S when 30S maturation is delayed
  [PMID:41965359 "Upregulated RsfS levels safeguard the 50S subunits until 30S assembly is complete."].
- PMID:33639093 is abstract only in cache; relied on curated UniProt FUNCTION text (ECO:0000269) for ObgE GTPase stimulation.
- PMID:18304323 (cytosol proteomics) does not name YbeB in the cached main text; the protein is presumably in supplementary tables. Accepted, since cytosol is consistent with all other evidence.

## Decisions
- protein binding rows (5): REMOVE per protein-binding policy; uL14 interaction captured via ribosomal large subunit binding.
- cytoplasm rows: MODIFY -> cytosol (GO:0005829), supported by IDA proteomics and 50S binding; cytoplasm is not one of the root-organelle exception terms.
- GO:0042256 cytosolic ribosome assembly (UniRule IEA): its definition is joining of the subunits into a functional ribosome, which RsfS antagonises; MODIFY -> GO:0000027 ribosomal large subunit assembly (participation in pre-50S maturation network), recorded as source defect (PROBABLE).
- Hibernation: GO:0141014 cytosolic ribosome hibernation exists (is_a negative regulation of cytoplasmic translation) but in QuickGO it is carried only by fungal IEA rows; the E. coli hibernation factors RMF (P0AFW2), RaiA (P0AD49) and HPF (P0AFX0) do not carry it (they use GO:0017148, GO:0045900, GO:0022611 etc.), and whether RsfS is a hibernation or biogenesis factor is debated [PMID:35790407]. No NEW row; raised as a question.
- No GO MF term for "ribosome subunit anti-association"; kept GO:0043023 ribosomal large subunit binding as core MF.
