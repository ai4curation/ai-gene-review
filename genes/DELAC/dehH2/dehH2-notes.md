# dehH2 (Q7DI63, Delftia acidovorans) — curation notes

## Identity

- UniProtKB **Q7DI63** (`Q7DI63_DELAC`), TrEMBL/unreviewed, 224 aa, plasmid **pUO1**,
  *Delftia acidovorans* strain B (NCBITaxon:80866; the strain was originally described as
  *Moraxella* sp. strain B).
- Gene name `dehH2` from the EMBL record BAB85580.1
  (`GN   Name=dehH2 {ECO:0000313|EMBL:BAB85580.1};`).
- EMBL cross-references on this entry: **AB049197/BAB85577.1, AB049198/BAB85580.1,
  AB063332/BAC81974.1**. RefSeq WP_011137954.1.
- UniProt protein name is RuleBase-derived: `RecName: Full=(S)-2-haloacid dehalogenase
  {ECO:0000256|RuleBase:RU368077}` with `EC=3.8.1.2`. There is no curated (ECO:0000269)
  functional statement on this entry; protein existence is `PE   3: Inferred from homology`.

## What the primary literature actually establishes

The enzyme behind this gene is **haloacetate dehalogenase H-2** of *Moraxella* sp. strain B,
one of two plasmid-borne haloacetate dehalogenases in that strain.

- Kawasaki et al. 1992 sequenced both structural genes and tied each ORF to a purified
  enzyme: [PMID:1512562 "Two genes encoding haloacetate dehalogenases, H-1 and H-2, are
  closely linked on a plasmid from Moraxella sp. strain B."] and [PMID:1512562 "The genes
  for H-1 and H-2, designated dehH1 and dehH2, respectively, had different sizes (885 bp and
  675 bp) and G+C contents (58.3% and 53.4%)."]. 675 bp = 224 codons plus stop, matching the
  224-aa Q7DI63 sequence.
- The two enzymes are unrelated: [PMID:1512562 "Sequence analysis revealed no homology
  between the two genes."] and [PMID:1512562 "We concluded that the dehalogenases H-1 and
  H-2 have no enzyme-evolutionary relationship."]. DehH1 is an α/β-hydrolase-fold
  fluoroacetate dehalogenase; DehH2 is a HAD-superfamily (type II / L-DEX-like) enzyme.
- **DehH2 is not a fluoroacetate dehalogenase**: [PMID:1512562 "H-1 predominantly acts on
  fluoroacetate, but H-2 does not."] This is the single most important functional fact about
  this protein and is the main thing that distinguishes it from its locus partner.
- Heterologous expression gives a haloacetate-dependent gain-of-function phenotype:
  [PMID:7579995 "The dehH2 gene introduced into the cells conferred iodoacetate resistance
  on them."] and [PMID:7579995 "The haloacetate dehalogenase gene, dehH2, cloned from
  Moraxella sp. strain B could be used a selection marker gene for vectors in Escherichia
  coli and Pseudomonas putida."] Iodoacetate is a haloacetate, so this is in-vivo evidence
  for C–halogen bond hydrolysis by DehH2 in two heterologous hosts.
- Genomic context: `dehH2` sits on the 8.9-kb class I composite transposon TnHad1 nested
  inside the class II transposon TnHad2 [PMID:11976102 "The dehH2 gene was carried on an
  8.9-kb class I composite transposon (TnHad1) that was flanked by two directly repeated
  copies of IS1071, IS1071L and IS1071R."], on the self-transmissible IncP-1β plasmid pUO1
  [PMID:14594853 "The self-transmissible plasmid pUO1 from Delftia acidovorans strain B
  carries two haloacetate-catabolic transposons, TnHad1 and TnHad2, and the mer genes for
  resistance to mercury."]. The whole haloacetate-catabolic cassette is therefore a mobile,
  horizontally transferable module, which is the interesting property from a bioremediation
  standpoint.

## Sequence/family evidence for the (S)-2-haloacid assignment

The UniProt record's `(S)-2-haloacid dehalogenase` / EC 3.8.1.2 name is a UniRule
(RuleBase:RU368077) inference, not a curated experimental statement. It is nonetheless well
grounded in signature evidence carried on the same record:

- `DR   NCBIfam; TIGR01428; HAD_type_II; 1.` — the HAD type II (L-2-haloacid dehalogenase)
  family model.
- `DR   CDD; cd02588; HAD_L2-DEX; 1.` and `DR   PRINTS; PR00413; HADHALOGNASE.`
- `DR   SFLD; SFLDF00045; 2-haloacid_dehalogenase; 1.`
- `DR   InterPro; IPR006328; 2-HAD.` (the signature behind the GO:0019120 IEA row)
- The sequence opens `MKKIEAIAFDMYGTLYD...`, the canonical HAD-superfamily motif I with the
  aspartate nucleophile, consistent with the hydrolytic, covalent-ester mechanism of this
  family rather than the Asp–His–Asp triad of DehH1-type fluoroacetate dehalogenases.

What is **not** established for DehH2 specifically is stereospecificity. The substrates it is
documented to act on (chloroacetate, iodoacetate) are achiral at C2, so no published
experiment on this protein tests (S)- versus (R)-2-haloacid preference. The EC 3.8.1.2
assignment is a family-level prediction. It is a reasonable one — the HAD type II family is
uniformly (S)/L-specific — but it should be read as inference, not measurement. Kept as
`ACCEPT` with that caveat recorded in the review, rather than removed, because family and
domain classification is legitimate support for membership-based function.

Historically the enzyme is classified under **EC 3.8.1.3** (haloacetate dehalogenase), the EC
number matching its discovery name and its demonstrated haloacetate activity. Both the
EC 3.8.1.2 (GO:0018784) and EC 3.8.1.3 (GO:0018785) claims are defensible and GO places the
two terms as siblings under GO:0019120, so the review accepts the UniRule row and adds
GO:0018785 as a `NEW` row rather than treating either as replacing the other.

## CMMMech cross-check (data/records/fluorine.yaml)

CMMMech grounds a causal-graph node `dehh2_haloacetate_dehalogenase` to
`UniProtKB:Q7DI63`. The identity grounding is correct (accession, entry name, TrEMBL status,
gene symbol, taxon and InterPro/Pfam identifiers all match the live UniProt record). Three
problems in CMMMech's own fields, noted here and **not** recorded as `source_defects`,
because `source_defects` is reserved for defects in GOA/UniProt/InterPro:

1. **The Dodge et al. 2024 evidence is attributed to the wrong protein.** Both CMMMech
   evidence blocks on the Q7DI63 protein example read "Purified from Delftia acidovorans
   strain B and sequenced by LC-MS/MS in Dodge et al. (2024); catalyzes hydrolytic
   defluorination of alpha-fluorophenylacetic acid and 2-fluoropropionic acid". Dodge et al.
   assayed **DehH1**, not DehH2. The paper's Methods state the enzyme by accession:
   [PMID:38063407 "Amino acid sequences of fluoroacetate dehalogenases from Rhodopseudomonas
   palustris strain CGA009 (RPA1163) (GenBank accession OPF91568.1) or Delftia acidovorans
   strain B (formerly Moraxella sp. strain B) (GenBank accession BAC81979.1) were used to
   generate codon-optimized gene sequences for expression in Pseudomonas putida"] and
   [PMID:38063407 "The pre-existing AlphaFold (37, 38) structure of the Delftia defluorinase
   (UniProt accession Q01398) was used for modeling interactions between the enzyme and
   different fluorinated ligands."]. GenBank BAC81979.1 and UniProt Q01398 are both DehH1
   (Q01398 = `DEH1_MORSB`, reviewed, "Haloacetate dehalogenase H-1", EC 3.8.1.3, 294 aa;
   BAC81979.1 is cross-referenced from Q7DI61, the TrEMBL DehH1 entry, 294 aa). Neither
   accession appears among Q7DI63's EMBL cross-references (BAB85577.1, BAB85580.1,
   BAC81974.1), and Q7DI63 is 224 aa. The paper's abstract likewise describes a single
   enzyme: [PMID:38063407 "The present study identified a broader substrate specificity in an
   enzyme originally studied for its activity on the natural product fluoroacetate."] DehH2 is
   not mentioned anywhere in the paper.
2. **The defluorination claim is specifically contradicted for DehH2.** Beyond being
   mis-attributed, "catalyzes hydrolytic defluorination" is the one activity the primary
   literature rules out for this enzyme: [PMID:1512562 "H-1 predominantly acts on
   fluoroacetate, but H-2 does not."] CMMMech should not carry a C–F cleavage claim on
   Q7DI63.
3. **Internal EC inconsistency.** The protein example lists `ec_numbers: [EC:3.8.1.2]` while
   its `functional_role` free text says "Haloacetate dehalogenase H-2 (EC 3.8.1.3; dehH2)".
   Both numbers have a defensible reading (see above), but the record states them as if they
   were one assignment. Note also that CMMMech grounds the partner node to the TrEMBL entry
   Q7DI61 when a reviewed Swiss-Prot entry for the same protein, Q01398, exists.

The CMMMech `functional_role` wording "co-encoded on the ... plasmid region transferred into
Pseudomonas putida" also blurs two different events: the pUO1/TnHad transposon mobility
described by Sota et al., and Dodge et al.'s construction of a recombinant *P. putida* strain
carrying a synthetic, codon-optimized **dehH1** cassette on pBBR1MCS-2. The dehH2 gene was
not part of the Dodge construct.

## Annotation calls

| Term | Evidence | Action | Basis |
|---|---|---|---|
| GO:0018784 (S)-2-haloacid dehalogenase activity | IEA, GO_REF:0000120 (RuleBase RU368077 / EC 3.8.1.2) | ACCEPT | HAD type II family membership from multiple independent signatures; stereospecificity itself untested on this protein |
| GO:0019120 hydrolase activity, acting on halide bonds, in C-halide compounds | IEA, GO_REF:0000002 (InterPro:IPR006328) | ACCEPT | The claim directly demonstrated for DehH2 (haloacetate dehalogenase; iodoacetate resistance) |
| GO:0018785 haloacetate dehalogenase activity | NEW (IC) | NEW | The enzyme's defining published activity, missing from GOA |

No cellular-component or biological-process annotations exist for this entry and none are
proposed: there is no localization evidence, and a haloacetate-catabolism process term would
require knowing which downstream pathway consumes the glycolate product in strain B, which
has not been established for this plasmid.

## Open questions

- Is DehH2 stereospecific on chiral 2-haloalkanoates (2-chloropropionate), and if so for
  which enantiomer? No published assay addresses this.
- What is the full halide range? Iodoacetate and the general "haloacetate" designation are
  documented; fluoroacetate is excluded; bromo-/chloroacetate kinetics for DehH2 specifically
  are in the pre-1990 Japanese-language literature not indexed in PubMed and were not
  obtained here.
