# HK1 (Hexokinase-1, P19367) — review notes

## Summary of gene function

HK1 is the ubiquitously-expressed hexokinase isozyme (EC 2.7.1.1) that catalyses the
first committed step of glucose catabolism: ATP-dependent phosphorylation of D-glucose
to D-glucose 6-phosphate (G6P). G6P is then partitioned between glycolysis, the pentose
phosphate pathway, and glycogen synthesis. HK1 is a ~100 kDa protein arising from
duplication and fusion of an ancestral 50 kDa yeast-type hexokinase; the C-terminal half
carries the catalytic site while the N-terminal half carries a regulatory/allosteric
glucose-6-phosphate binding site (both halves fold as a hexokinase domain)
[PMID:1637300; PMID:3207429].

Key established facts:

- **Catalysis / substrate range.** Phosphorylates several D-hexoses — D-glucose,
  D-mannose, D-fructose, D-glucosamine, 2-deoxy-D-glucose — to their 6-phosphates
  (UniProt FUNCTION; PubMed:1637300, 25316723, 27374331). Does NOT phosphorylate
  N-acetyl-D-glucosamine (PubMed:27374331). The GOA MF terms glucokinase activity
  (GO:0004340), fructokinase activity (GO:0008865), mannokinase activity (GO:0019158),
  and glucosamine kinase activity (GO:0047931) are all facets of this broad
  hexose-kinase (hexokinase, GO:0004396) activity — HK1 is not a specialist for any of
  these individual sugars.
- **Product inhibition / allostery.** Allosteric enzyme inhibited by its product
  D-glucose 6-phosphate (PubMed:1637300); the C-terminal "mini-hexokinase" retains both
  catalysis and G6P inhibition.
- **Subcellular localization.** Cytosol, with a pool associated with the mitochondrial
  outer membrane via VDAC/porin; the N-terminal mitochondrial-binding peptide (residues
  1-10) mediates the association (PubMed:1985912). Erythrocyte and testis isoforms with
  altered N-termini cannot bind mitochondria. Dissociates from the OMM upon inhibition
  by N-acetyl-D-glucosamine, relocating to cytosol (PubMed:27374331). The mito-OMM
  association couples glycolysis to oxidative phosphorylation and is anti-apoptotic.
- **Moonlighting immune role.** In macrophages HK1 acts as a cytosolic pattern-recognition
  receptor: bacterial peptidoglycan-derived N-acetyl-D-glucosamine (NAG) inhibits HK1,
  causing it to dissociate from the mitochondrial outer membrane, which is sufficient to
  activate the NLRP3 inflammasome and IL-1β/IL-18 production (PubMed:27374331).
- **Regulation by c-Src.** c-Src binds and phosphorylates HK1 at Tyr732, lowering Km and
  raising Vmax by disrupting HK1 homodimer, enhancing glycolysis and tumour growth
  (PubMed:28054552).
- **Mitophagy.** Hexokinase activity (HK1/HK2) is required for recruitment of parkin to
  depolarized mitochondria (PubMed:23962723; abstract foregrounds HK2 but the study
  addresses hexokinases including HK1).

## Disease
- CNSHA5 (non-spherocytic hemolytic anemia, MIM 235700) — recessive, decreased RBC
  hexokinase activity (PubMed:7655856, 12393545).
- HMSNR / CMT (hereditary motor and sensory neuropathy, Russe type; MIM 605285)
  (PubMed:19536174, 34193129).
- RP79 (retinitis pigmentosa 79, dominant; MIM 617460) (PubMed:25190649, 25316723).
- NEDVIBA (neurodevelopmental disorder with visual defects and brain anomalies; MIM
  618547) (PubMed:30778173).

## Curation decisions (rationale)

Core: hexokinase activity (GO:0004396) MF; glycolytic process (GO:0006096) and glucose
metabolic process (GO:0006006) BP; cytosol (GO:0005829) CC. Mitochondrial-outer-membrane
association is a real, well-supported localization (accept CC), but the enzymatic core
function acts in the cytosol.

- The various single-sugar MF terms (glucokinase, fructokinase, mannokinase, glucosamine
  kinase) are ACCEPTed where experimental/Rhea/Reactome-backed, but flagged as facets of
  the broad hexokinase activity rather than substrate-specialist functions. Glucokinase
  activity (GO:0004340) as an IBA/ISS/Reactome term is the community convention for the
  glucose→G6P reaction of hexokinases; accepted.
- Bare `protein binding` (GO:0005515) IPIs (VDAC1, SRC, CFTR ×2) → MARK_AS_OVER_ANNOTATED
  (uninformative; underlying interactions are real but the term conveys no function).
- High-throughput mitochondrion localizations (HDA/HTP/IDA) accepted as non-core given
  the strong experimental OMM evidence.
- `peptidoglycan binding` (GO:0042834) and immune/IL-1β terms accepted (KEEP_AS_NON_CORE
  where non-core) — supported by PMID:27374331 as a genuine moonlighting function.
- GDP-mannose biosynthetic process (GO:0009298): HK1 does not synthesize GDP-mannose;
  it produces mannose-6-P which feeds upstream of that pathway → MARK_AS_OVER_ANNOTATED.

Deep research: falcon provider out of credits (HTTP 402); no -deep-research-falcon.md was
generated. Review grounded in UniProt P19367, seeded GOA, and cached publications.
