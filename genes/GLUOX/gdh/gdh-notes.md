# gdh (P27175, DHG_GLUOX) notes

Gluconobacter oxydans 621H membrane-bound PQQ-dependent quinoprotein glucose
dehydrogenase (mGDH), locus GOX0265. Reviewed (Swiss-Prot) entry, but PE level 3
(inferred from homology); no GO annotation in GOA is experimental, all 7 rows are IEA.

No deep-research provider was available for this review; these notes are a manual
literature survey (PubMed searches, cached publications, CMMMech record sources).

## Identity and sequence

- UniProt: 808 aa; N-terminal hydrophobic region with predicted helices
  (UniProt FT SIGNAL 1..33 plus TRANSMEM 35..54, 59..76, 94..108, 123..138, all
  ECO:0000255), followed by the large PQQ beta-propeller domain (Pfam PF01011,
  InterPro IPR017511 PQQ_mDH, NCBIfam TIGR03074 PQQ_membr_DH, CDD cd10280 PQQ_mGDH).
  PANTHER PTHR32303:SF4 (QUINOPROTEIN GLUCOSE DEHYDROGENASE).
- Caveat: UniProt annotates a cleavable signal peptide (1..33) and `Flags: Precursor`.
  For the E. coli ortholog the N-terminal hydrophobic segments form the membrane anchor
  (five helices). Whether residues 1..33 of P27175 are really cleaved, or form a first
  uncleaved TM helix, is not established in any paper I found. Recorded as a
  suggested question and, after PR review, also as a SUSPECTED UniProt source defect
  on the plasma membrane row.
- The sequence was first determined from strains P1/P2 by Cleton-Jansen et al.
  [PMID:1833618 "P1 can oxidize only D-glucose, whereas P2 is also capable of the
  oxidation of the disaccharide maltose"]; the P2 maltose-oxidizing form differs by a
  single residue [PMID:1833618 "This mutation could be ascribed to a 1 bp substitution
  resulting in the replacement of His 787 by Asn."]. UniProt records this as the
  VARIANT at 788 (H -> N, P2 form); numbering differs by one between paper and entry.
  The genome sequence of 621H [PMID:15665824] supplies the current sequence.

## Function

- Catalytic activity: D-glucose + ubiquinone = D-glucono-1,5-lactone + ubiquinol
  (EC 1.1.5.2, RHEA:22152), PQQ cofactor (UniProt). The product is the lactone;
  hydrolysis to gluconic acid is spontaneous or lactonase-mediated and is not an mGDH
  activity.
- Direct biochemistry on GOX0265 itself: Meyer et al. overproduced and purified it
  [PMID:22790543 "The membrane-bound PQQ-dependent glucose dehydrogenase (mGDH), encoded by gox0265, was used as
  model protein for homologous membrane protein production"] and [PMID:22790543
  "membranes from the overexpression strain had a five- and threefold
  increase of mGDH activity and oxygen consumption rates, respectively"]; the
  quinol-oxidase limitation they report places the enzyme upstream of the respiratory
  quinone pool [PMID:22790543 "indicating that the terminal quinol oxidases of the respiratory chain were rate
  limiting"]. The abstract states the enzyme was "purified to homogeneity" and is
  "a membrane integral quinoprotein". Full text not available in the cache.
- Overexpression in DSM 2343 (= ATCC 621H) increased gluconic acid
  [PMID:16892291 "the resulting strains overproducing the membrane-bound
  glucose dehydrogenase showed an increased gluconic acid formation"].
- Loss of function (ortholog in strain N44-1): mgdH inactivation abolished gluconate
  and ketogluconate formation [PMID:20453146 "Both mutant strains completely consumed the glucose but produced neither
  gluconate nor the secondary products 2-ketogluconate and 2,5-diketogluconate."].
- Peters et al. made clean deletions of all membrane-bound dehydrogenases in 621H and
  assigned substrate spectra by whole-cell DCPIP assays [PMID:23519735]; abstract-only
  in cache, so substrate details for mGDH are not quoted.
- Substrate breadth: 621H Delta-mgdh produced no xylonate on xylose
  [PMID:23381123 "These experimental observations suggested that the mgdh
  gene was responsible for the conversion of xylose to xylonate in G. oxydans"]. So the
  enzyme is an aldose (glucose, xylose) dehydrogenase in vivo; no GO term proposed for
  xylose oxidation (would be a separate MF, evidence is a knockout phenotype only).

## Bioleaching relevance (CMMMech context)

- Schmitz et al. 2021 (strain NRRL B-58, not 621H) built a transposon knockout
  collection: [PMID:34795278 "This is produced by periplasmic glucose oxidation by the pyrroloquinoline quinone (PQQ)-dependent membrane-bound glucose dehydrogenase (mGDH)"];
  [PMID:34795278 "δmgdh reduced bioleaching by 97%."] (retorted phosphor powder).
  They also caution [PMID:34795278 "gluconic acid alone fails to explain bioleaching by G. oxydans"].
- Follow-up engineering (B58): [PMID:40425722 "G. oxydans ΔpstS, P112:mgdh produced REE-bioleaching that was 53.1% higher than wild-type."]
  on allanite ore.
- These are B58 data on the B58 mgdh ortholog; I did not compute B58 vs 621H identity.
  They support the biological role (gluconic-acid production drives acidification and
  REE release in laboratory leaching), not 621H-specific claims.

## CMMMech claims vs. evidence (do not edit CMMMech; for the record)

CMMMech grounds ~9 records (allanite-concentrate, dunite, enstatite,
fluorescent-lamp-phosphor, neodymium, olivine-group, phosphogypsum,
spent-fluid-catalytic-cracking-catalyst, spent-nickel-metal-hydride-batteries) to P27175.

1. The causal-graph node description "Periplasmic quinoprotein glucose dehydrogenase"
   is loose: the protein is an integral inner (cytoplasmic) membrane protein whose PQQ
   domain faces the periplasm (UniProt: "Cell inner membrane; Multi-pass membrane
   protein; Periplasmic side"). It is not a soluble periplasmic enzyme.
2. `functional_role` says mGDH oxidizes glucose "to D-glucono-1,5-lactone/gluconic
   acid". mGDH makes the lactone; gluconic acid arises by hydrolysis. Minor, but the
   enzyme does not itself make the acid.
3. Strain proxy: the leaching organisms are B58 (NRRL B-58), DSM 3503, or unspecified
   isolates, while P27175 is the 621H entry. The records' annotation notes do say this
   is a reference representative, which is appropriate; the ortholog identity has not
   been verified in this review.
4. Gene-level evidence exists only in some records' contexts: the B58 δmgdh phenotype on
   phosphor powder [PMID:34795278] and mgdh overexpression on allanite [PMID:40425722].
   For dunite, enstatite, NiMH, FCC catalyst, and phosphogypsum, the records themselves
   correctly note no gene-level test; mechanism attribution there is by inference
   from G. oxydans glucose physiology, and should stay `partial`.
5. Schmitz et al. show gluconic acid alone does not reproduce biolixiviant leaching, so
   mGDH should not be presented as the sole determinant of leaching efficiency.

## GO decisions (summary)

- Accept GO:0008876 (core MF) and GO:0005886 plasma membrane.
- General terms (membrane, oxidoreductase activity, CH-OH donors) -> MODIFY to the
  specific terms already carried.
- quinone binding -> MODIFY to pyrroloquinoline quinone binding (GO:0070968).
- outer membrane-bounded periplasmic space (InterPro2GO from IPR001479, a signature
  shared with soluble periplasmic PQQ dehydrogenases) -> ACCEPT the compartment term;
  the error is the located_in relation (should be is_active_in for a membrane-integral
  enzyme), filed as a SUSPECTED WRONG_QUALIFIER source defect. This matches the
  ortholog review genes/PSEPK/gcd, which adds periplasmic space with is_active_in as
  NEW. An earlier draft replaced it with GO:0098567 periplasmic side of plasma
  membrane; dropped because leaflet terms do not fit a multi-pass protein.
- NEW: non-phosphorylated glucose catabolic process (GO:0019595). Comparators:
  genes/PSEPK/gcd makes the same NEW call; modules/pseudomonad_2_ketogluconate_loop.yaml
  has GO:0019595 as its concept with Gcd (P15877) as the part-1 exemplar (that module
  is restricted to Pseudomonas; G. oxydans is an Acetobacteraceae implementation of
  the same step). QuickGO (checked 2026-10-28) shows P15877 carries GO:0019595 from
  EcoCyc, EXP, PMID:2228962, with qualifier acts_upstream_of_or_within. The PMID:2228962
  abstract is about cloning and sequencing gcd and does not itself describe the process,
  so it is not quoted as support.
- GO:0008876 label: GOA uses the newer name "glucose dehydrogenase (PQQ, quinone)
  activity"; authored slots keep "quinoprotein glucose dehydrogenase activity", the
  label in the validation ontology version.

---

**Correction (2026-11-23, issue #6783)**

The review carried a `NEW` row on **GO:0019595 "non-phosphorylated glucose
catabolic process"** (IC, PMID:20453146), and the same id under
`core_functions[].directly_involved_in`. That term is **obsolete** in the current
ontology (verified against QuickGO, GO release 2026-11-21, where it resolves as
"obsolete non-phosphorylated glucose catabolic process"). GO's obsoletion comment:
*"This term was obsoleted because it overlaps other GO terms: glucose 1-phosphate
catabolic process ; GO:0019255 and Entner-Doudoroff pathway ; GO:0061678."* There
is no `replaced_by`, only those two `consider` targets.

Candidates weighed:

- **GO:0019255 glucose 1-phosphate catabolic process** (live) — rejected. It
  requires a phosphorylated hexose. No phosphorylated intermediate occurs anywhere
  in the periplasmic route; mGDH oxidizes free D-glucose directly to
  D-glucono-1,5-lactone.
- **GO:0061678 Entner-Doudoroff pathway** (live) — rejected. Its definition is
  conversion of a carbohydrate "to pyruvate and either glyceraldehyde or
  glyceraldehyde-3 phosphate by dehydration and aldol cleavage via a gluconate or
  6-phosphogluconate intermediate". mGDH performs none of that chemistry: it is a
  periplasmic, membrane-anchored oxidase upstream of and physically separated from
  any cytoplasmic ED enzymes, and in *G. oxydans* most of its product leaves the
  cell as gluconic acid. Asserting ED here would fail CLAUDE.md's participation
  test — the entity that performs the dehydration and the aldol cleavage is not
  this protein.
- **GO:0046178 D-gluconate biosynthetic process** — the obvious third candidate,
  and it is **also obsolete** in the current release, with the comment *"The reason
  for obsoletion is that D-gluconate is formed as a product of glucose and glucose
  1-phosphate catabolism, and is not the output of a dedicated biosynthetic
  process."* Worth recording, because that ruling is what settles the choice: GO
  itself places the formation of gluconate from glucose **inside glucose
  catabolism**. (GO:0046177 D-gluconate catabolic process is obsolete too;
  GO:0019521 D-gluconate metabolic process is live but is a bare metabolic grouping
  whose only remaining child is the obsoleted biosynthetic term, and it says nothing
  about glucose.)
- **GO:0006007 glucose catabolic process** (live) — chosen. It is the direct parent
  under which the obsoleted GO:0019595 sat, it is true of this enzyme, and GO's own
  GO:0046178 obsoletion comment licenses it for gluconate formation. Its other live
  children (GO:0019658 bifid shunt, GO:0061621 canonical glycolysis, GO:0061633
  transport-coupled glycolytic process, GO:0061718 glucose catabolic process to
  pyruvate) are all wrong for a periplasmic oxidase, so GO:0006007 is the most
  specific live term available.

**Decision: the `NEW` row was restated at GO:0006007 glucose catabolic process**
(evidence, qualifier and quotes unchanged), `core_functions[].directly_involved_in`
updated to match, and the `reason` rewritten to argue for that term and record why
each alternative was rejected. The gene's GOA record carries no biological-process
annotation at all, so the row still adds coverage rather than restating something.

**A `proposed_new_terms` entry was added** ("periplasmic oxidative glucose
catabolic process", parent GO:0006007), because the granularity was lost to the
obsoletions rather than to the evidence: the direct, non-phosphorylative,
extracytoplasmic oxidation of glucose is a real and widespread peripheral pathway
in the *Acetobacteraceae* and the pseudomonads, and neither obsoletion addressed
it. GO:0006007 does not distinguish it from glycolysis.

**Elsewhere in the corpus (not edited here).** The same obsolete id is asserted in
two other places, both of which need the same correction in their own PRs:
`genes/PSEPK/gcd/gcd-ai-review.yaml` (a `NEW` IMP row, plus
`core_functions[].directly_involved_in`), and
`modules/pseudomonad_2_ketogluconate_loop.yaml` (as the module's top-level
concept). Separately, QuickGO on 2026-11-23 still shows *E. coli* Gcd
(UniProtKB:P15877) annotated to GO:0019595 from EcoCyc on EXP evidence
(PMID:2228962, `acts_upstream_of_or_within`) — i.e. GOA has not yet propagated the
obsoletion, so there is no upstream remapping to follow.
