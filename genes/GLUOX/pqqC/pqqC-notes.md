# pqqC (GOX0985, Q9L3B2) — Gluconobacter oxydans 621H — curation notes

No provider deep-research report was generated for this gene (no deep-research API
keys in this environment). These notes are a manual literature review using PubMed,
the cached publications cited below, and the UniProt record.

## Identity

- UniProtKB:Q9L3B2 (PQQC_GLUOX), Swiss-Prot reviewed, 239 aa, ordered locus GOX0985,
  G. oxydans 621H (NCBITaxon:290633). Protein existence level 3 (inferred from homology).
- The record's recommended name, EC 1.3.3.11, FUNCTION, CATALYTIC ACTIVITY and PATHWAY
  lines all carry HAMAP-Rule MF_00654 evidence. Family assignment: HAMAP MF_00654,
  NCBIfam TIGR02111 (PQQ_syn_pqqC), InterPro IPR011845 (PqqC), Pfam PF03070, PANTHER
  PTHR40279 (PQQC-LIKE PROTEIN).
- The PANTHER subfamily PTHR40279:SF3 carries the official name "4-AMINOBENZOATE
  SYNTHASE", but its members in `interpro/panther/PTHR40279/PTHR40279-entries.csv` are
  overwhelmingly reviewed PqqC proteins (e.g. A3PMI4, A4XTR2, A5FUM6, all named
  "Pyrroloquinoline-quinone synthase", gene `pqqC`). This is a subfamily-naming
  artifact, not evidence that GOX0985 makes 4-aminobenzoate; no annotation in this
  review depends on it.
- UniProt reference 1 (Felder et al. 2000) sequenced the cluster from strain ATCC 9937;
  sequence conflicts at residue 69 and 88-89 relative to the 621H genome sequence.

## Molecular function (by homology to characterized PqqC)

- Characterized PqqC is the terminal enzyme of PQQ biosynthesis: ring cyclization plus
  eight-electron oxidation of the late precursor AHQQ to PQQ
  [PMID:15148379 "catalyzes the final step in the pathway in a reaction that involves ring"].
- PqqC is a cofactorless oxidase
  [PMID:15148379 "PqqC is unusual in that it transfers redox equivalents to"]
  and the H2O2/O2 stoichiometry was measured
  [PMID:15148379 "determine the stoichiometry of H2O2 formation and O2 uptake during the"].
  UniProt/Rhea (RHEA:10692) give the net reaction as AHQQ + 3 O2 = PQQ + 2 H2O2 +
  2 H2O + H(+).
- G. oxydans PqqC itself has not been purified or assayed. The molecular function call
  for GOX0985 rests on membership of a tight, single-function family (HAMAP rule plus
  TIGRFAM plus InterPro), which is good support for membership-based function.
- Localization: UniProt annotates no signal peptide, no transmembrane segment and no
  SUBCELLULAR LOCATION. PQQ synthesis is generally held to be cytoplasmic with export
  of mature PQQ to periplasmic quinoproteins, but that is a single inferential line for
  this entry, so no cellular-component annotation is proposed here.

## G. oxydans genetics and the bioleaching context

- Felder et al. 2000 characterized a Tn5 glucose-dehydrogenase-deficient mutant of
  G. oxydans IFO 3293 whose insertion was in a pqqE-like ORF; acid production was
  restored by exogenous PQQ
  [PMID:11111029 "acid production could be restored by addition of the coenzyme"],
  and the ATCC 9937 cluster was cloned with
  [PMID:11111029 "It has five genes pqqA-E."]. Abstract only; pqqC was not individually
  mutated in what the abstract reports.
- Schmitz et al. 2021 (Nat Commun) built a whole-genome transposon knockout collection
  in G. oxydans B58. A pqqC disruption produced the least acidic biolixiviant of all
  tested strains
  [PMID:34795278 "The most alkaline biolixiviant was produced by a disruption in the PQQ synthesis system, δpqqC, at pH 4.71."]
  and strongly reduced rare-earth extraction from retorted phosphor powder
  [PMID:34795278 "δpqqC reduced bioleaching by ≈94%."]. The authors read this as loss of
  the mGDH cofactor
  [PMID:34795278 "Disruption mutants that knocked out the synthesis of mGDH’s essential redox cofactor, PQQ, also produced significant reductions in biolixiviant acidity."].
- Schmitz et al. 2025 (Commun Biol) restate the same dependency when motivating their
  engineered strains
  [PMID:40425722 "disruption of genes required for synthesis of the mGDH co-factor PQQ25, including the pqqABCDE operon and tldD and tldE genes, also produces large reductions in REE-bioleaching in G. oxydans24"].

These are strain-B58 phenotypes, i.e. necessity evidence for the PQQ biosynthetic
pathway in acid production, not a direct assay of the GOX0985 gene product's catalysis.
They support the biological-process annotation already present and are quoted in the
review as corroboration, not as the primary basis for the molecular-function call.

## CMMMech framing vs. evidence

CMMMech grounds Q9L3B2 in nine records (neodymium, phosphogypsum, fluorescent-lamp
phosphor, spent NiMH batteries, spent FCC catalyst, allanite concentrate, dunite,
enstatite, olivine group) with the `functional_role` "Pyrroloquinoline-quinone synthase
(EC 1.3.3.11) catalyzing the final ring-closure and oxidation steps of PQQ cofactor
biosynthesis required for holo-Gdh activity". Two caveats worth recording (CMMMech is
not edited here):

1. The enzymology attributed to this accession is inferred from the PqqC family (HAMAP
   rule-based, PE 3), not demonstrated for the 621H protein. The role statement reads as
   a settled biochemical fact for this entry.
2. The mutant evidence behind "required for holo-Gdh activity" comes from G. oxydans
   B58 transposon strains (PMID:34795278) and from strain IFO 3293 pqqE (PMID:11111029),
   not from 621H GOX0985. Several records cite leaching sources (e.g. antonick2019,
   rasoulnia_2021, reed_2016, lee2025, klug_2026) that use gluconic acid or G. oxydans
   lixiviant but, as far as the record evidence text shows, say nothing about PqqC
   itself; the protein example is a mechanistic annotation imported into those records
   rather than a claim those sources make. Laboratory bioleaching percentages should not
   be read as industrial performance.

## Review calls

Both GOA rows (GO:0018189 PQQ biosynthetic process, involved_in, IEA GO_REF:0000120;
GO:0033732 pyrroloquinoline-quinone synthase activity, enables, IEA GO_REF:0000120) are
accepted. They are exactly the two claims the family assignment and the pathway
literature support, at the right granularity. No NEW terms are proposed: a cytoplasm
annotation would rest on a single inferential line, and process terms such as gluconic
acid biosynthesis or any bioleaching-related process describe what downstream mGDH does
with the PQQ product, not work PqqC performs.
