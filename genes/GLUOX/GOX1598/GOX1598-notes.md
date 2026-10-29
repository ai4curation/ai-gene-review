# GOX1598 / Q5FQK7 (*Gluconobacter oxydans* 621H) — curation notes

Reviewer journal for the ai-gene-review of UniProtKB **Q5FQK7** (`Q5FQK7_GLUOX`,
ordered locus name **GOX1598**, 362 aa, strain 621H, NCBITaxon:290633).

No deep-research provider was available for this review, so the literature work
below is my own (PubMed E-utilities, UniProt REST, QuickGO, the cached
publications and the local PAINT/PANTHER data).

## 1. What the entry actually is

- Unreviewed **TrEMBL** entry, protein existence **`PE 4: Predicted`**, created
  from the 621H genome submission and never curated.
- The protein name and EC number are **submitter-supplied**, not curated:
  `DE   SubName: Full=Putative oxidoreductase {ECO:0000313|EMBL:AAW61339.1};`
  and `EC=1.1.1.- {ECO:0000313|EMBL:AAW61339.1}`. `ECO:0000313` is
  annotation imported unchecked from the submitter, so per the repository's
  UniProt-quote rules neither the name nor the EC number is usable as support.
  The `Oxidoreductase` keyword carries `ECO:0000256|ARBA:ARBA00023002` in
  addition to the same submitter evidence — also not support.
- There is **no** `CC FUNCTION`, no `CC SUBCELLULAR LOCATION`, no `FT ACT_SITE`,
  no `FT BINDING`. The single feature is a Pfam-derived
  `FT DOMAIN 29..353 NADP-dependent oxidoreductase`
  (`ECO:0000259|Pfam:PF00248`).
- Signature matches (these *are* usable as evidence of family membership):
  `Pfam PF00248 Aldo_ket_red`, `SUPFAM SSF51430 NAD(P)-linked oxidoreductase`,
  `CDD cd19094 AKR_Tas-like`, `Gene3D 3.20.20.100`,
  `PANTHER PTHR43364:SF4` / `PTHR43364`, `InterPro IPR023210 / IPR036812 /
  IPR050523`, `eggNOG COG0667`.
- So: a predicted **aldo-keto reductase (AKR) superfamily** protein. Nothing more
  is asserted by the record.

## 2. GOA is empty — and that is not a GOA error

`GOX1598-goa.tsv` has a header and no rows. Confirmed live against QuickGO:

```
https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:Q5FQK7
-> {"numberOfHits":0,"results":[],...}
```

The reason is mechanical rather than a judgement about this protein: **none of
the three InterPro entries it matches has an interpro2go mapping.** Checked
against the current GO external2go file
(`https://ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/interpro2go`, 30128
lines): `IPR023210`, `IPR036812` and `IPR050523` are all absent. Note that this
is specific to the entries *this* protein matches, not to the superfamily: other
AKR entries are mapped, and *E. coli* Tas (P0A9T4) does get `GO:0016491` by
`IEA GO_REF:0000002` through `IPR020471`, which Q5FQK7 does not match. That
contrast is load-bearing for the scoping of the source defect, so here is the
query it was read from (2026-10-29):

```
https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:P0A9T4
-> 5 rows, including
   GO:0016491 | IEA | GO_REF:0000002 | withFrom InterPro:IPR020471 | assignedBy InterPro
   GO:0008106 | NAS | PMID:14517983  | withFrom none                | assignedBy EcoCyc
   GO:0034198 | IMP | PMID:9560382   | EcoliWiki
   GO:0005829 | IBA | GO_REF:0000033 | withFrom PANTHER:PTN000199734, UniProtKB:P0A9T4
   GO:0005829 | IDA | PMID:18304323  | EcoCyc
```

The same query is the source of the statement, used in the annotation `reason`,
that Tas's `GO:0008106` rests **only** on `NAS:EcoCyc`: that term appears on
exactly one row. There is
also no PANTHER-family GO mapping for `PTHR43364` (`go_terms: null` in
`PTHR43364-metadata.yaml`), and no IBA row — indeed no GOA row at all — for
Q5FQK7, so nothing was propagated to it (see §3).

I have recorded the missing `IPR023210` → `GO:0016491` mapping as a
`source_defects` entry (`requested_change: ADD`, `resource: OTHER` = InterPro /
GO external2go) on the one annotation row in this review. IPR023210 *is* the AKR
catalytic domain, so a safe oxidoreductase-activity mapping is defensible; I did
not propose anything more specific, because the **oxidised donor group** is not
uniform across the entry's matches. IPR023210 also matches human AKR1D1
(P51857), a Delta(4)-3-oxosteroid 5-beta-reductase of EC 1.3.1.3
(`ECO:0000269`), whose donor is a CH-CH group — `GO:0016628` — while `GO:0016616`
and `GO:0008106` both sit under `GO:0016614` (CH-OH group of donors). QuickGO's
is_a ancestor sets confirm `GO:0016616` and `GO:0016628` share no ancestor below
`GO:0016491`, so `GO:0016491` is the most specific term that holds for every
match.

An earlier draft of this section, and of the `source_defects` `explanation` that
ships to the InterPro/GO external2go maintainers, gave **cofactor** heterogeneity
("members with different cofactors (NAD and NADP)") as the reason to stop above
`GO:0016616`. That rationale is withdrawn: `GO:0016616` is itself *"...NAD **or**
NADP as acceptor"*, so it already accommodates both the NADP(+)- and the
NAD(+)-dependent members and cofactor heterogeneity is no obstacle to it. The
conclusion — `GO:0016491` and nothing narrower — is unchanged; only its reason
is. A second, weaker point in the same direction: IPR023210 also matches the
voltage-gated potassium channel beta subunits (e.g. Q13303/KCNAB2), whose
experimentally supported function is Kv channel regulation and whose aldo-keto
reductase activity is annotated only *by similarity*, with no physiological
substrate identified. (Note that these subunits are **not** non-catalytic, as is
sometimes said: UniProt does credit them with NADPH-dependent aldoketoreductase
activity on an in-vitro substrate range, just without a physiological substrate
and without direct experimental support in the human entry.)

## 3. PAINT / PTHR43364 — nothing propagates here

`interpro/panther/PTHR43364/PTHR43364-paint.tsv` holds 8 node annotations:

| node | term | evidence | seeds | taxon scope |
|---|---|---|---|---|
| PTN000199503 | GO:0005794, GO:0005829, GO:0009407 | IBD | RGD/human AKR7 genes | taxon:33154 (Opisthokonta) |
| PTN000199527 | GO:0046223 | IBD | RGD:628635, UniProtKB:O95154 | — |
| PTN000199613 | GO:0005829 | IBD | UniProtKB:P76187, P77735 | — |
| PTN000199659 | GO:0005737, GO:0008106 | IBD | plant/pombe/rat/human members | — |
| PTN000199734 | GO:0005829 | IBD | UniProtKB:P0A9T4 (*E. coli* Tas) | taxon:1236 (Gammaproteobacteria) |

The decisive fact is on the target's own side, and it is the only one this table
can support: **GOA gives Q5FQK7 no IBA row — no row of any kind — so no
PAINT-derived annotation reached it.** There is therefore no propagation to argue
with, and no `propagation_review` is needed anywhere in this review.

I am deliberately *not* making a claim about where this protein sits in the tree.
This TSV carries nodes, GO ids, seeds and taxon scopes and **no tree topology**,
so it cannot establish which of these nodes Q5FQK7 descends from; an earlier
draft of this file said PAINT "placed no ancestral node annotation on the lineage
this protein descends from", which the file cannot show and which is in any case
misleading, since `PTN000199659` does carry `GO:0008106` (F, IBD). The two
observations that *are* readable here are narrower: the node seeded by Tas
(`PTN000199734`), the characterised protein that names the `AKR_Tas-like` CDD
branch (`cd19094`) this protein matches, carries only a
**cytosol** cellular-component claim and is scoped to Gammaproteobacteria, which
does not include this alphaproteobacterium; and no node in the file is seeded by
a *G. oxydans* or other alphaproteobacterial member. Neither of those is the
reason Q5FQK7 has no IBA; the absence of any GOA row for it is.

PTHR43364's official name is `NADH-SPECIFIC METHYLGLYOXAL REDUCTASE-RELATED` and
the subfamily's is `NAD(P)-LINKED OXIDOREDUCTASE SUPERFAMILY PROTEIN`
(from `interpro/panther/panther.obo`). The subfamily is a mixed bin: AKR7A2/A3
(aflatoxin B1 aldehyde reductase), YdjG (methylglyoxal reductase), YajO, IolS,
YhdN, YccK, Tas, Rv2298, plus fungal and uncharacterised bacterial members.
Nothing substrate-specific transfers from it.

Those names are read off `interpro/panther/PTHR43364/PTHR43364-entries.csv`, and
that file is a **sample, not the membership list**: it has 55 rows (21 of them
`:SF4`) against the family's own metadata counters of `proteins: 68362` in
`subfamilies: 11`. So it is usable for "here are named members of this
subfamily", which is all it is used for above, and it is **not** usable for any
count or any "all members are X" claim. An earlier draft of this section and of
`RESULTS.md` said the subfamily contains "a dozen uncharacterised bacterial
members" on the strength of this file; no such number is supportable from it, and
the substrate-heterogeneity conclusion does not need one — it follows from the
named characterised members (AKR7A2/A3, YdjG, IolS, Tas) having unrelated
substrates. If a membership number is ever needed, the metadata counters are the
artifact to cite; a row count in an `*-entries.csv` never is.

## 4. My own sequence analysis

`GOX1598-bioinformatics/` (see `RESULTS.md`) maps curated `ACT_SITE`/`SITE`/
`BINDING` features of five reviewed AKRs onto Q5FQK7 by pairwise alignment, with
no hard-coded residue numbers.

- The **AKR catalytic tetrad is complete and unmutated**: Asp62, Tyr67, Lys101,
  His147 of Q5FQK7 are identical to the curated catalytic residues of all five
  references, which agree with each other on those positions.
- **The characterised protein to reason from is *E. coli* Tas (P0A9T4)**, and the
  evidence that designates it is the entry's own `CDD cd19094 AKR_Tas-like`
  cross-reference, which names the Tas-like branch of the superfamily
  independently of any identity figure. Tas is *also* the most similar of the five
  references aligned here, at **50.4% identity** — but that ranks those five
  proteins only. It is a solved-structure NADP(H)-dependent aldo-keto reductase
  [PMID:14517983 "Crystal structure of the Escherichia coli Tas protein, an NADP(H)-dependent aldo-keto reductase."].
  Tas's own physiological substrate is not established either.

  **Withdrawn wording.** Earlier drafts of this file, of `RESULTS.md`, of the
  top-level `description`, of a `findings[].statement` and of a `knowledge_gaps`
  entry called Tas the protein's *"closest reviewed relative"* / *"closest
  characterised relative"*. That is a superlative over reviewed UniProt, and
  `map_akr_catalytic_sites.py` cannot establish it: it aligns five hand-picked
  references (`REFERENCES` at lines 44-50) and runs **no database search**, so the
  identity column ranks those five and nothing else. The superlative is withdrawn
  everywhere and is no longer asserted anywhere in this review; the claim it was
  carrying — that Tas is the right characterised relative to reason from — now
  rests on `CDD cd19094`, which designates the subgroup directly. The 50.4% figure
  itself stands: it is a real number from a real alignment, now stated with its
  bound.
- **Cofactor preference is not resolvable.** The conserved pocket positions are
  shared by NADP(+)-using references (Tas, IolS, AKR7A2, AKR1B1) and the
  NAD(+)-using one (YdjG), and the AKR1B1 residues that read the 2'-phosphate
  (K263, S264, R269, E272, N273) are *not* conserved in Q5FQK7.
- **No substrate is assignable.** The non-His substrate-contact residues of
  AKR7A2 and AKR1B1 map to non-identical residues or to gaps.

That is exactly enough to support one molecular-function annotation at the
reaction-class level — `GO:0016616` *oxidoreductase activity, acting on the CH-OH
group of donors, NAD or NADP as acceptor* — and no more. I deliberately did not
propose `GO:0008106` *alcohol dehydrogenase (NADP+) activity* (the term Tas
carries, and only by `NAS:EcoCyc`), because that term names NADP+ specifically and
the analysis cannot distinguish NAD from NADP. I also did not propose any
cofactor-binding term for the same reason, nor any cellular-component term: the
protein has no signal peptide, lipobox or transmembrane segment, which is a single
line of evidence pointing at the cytoplasm, and the repository's standard is at
least two agreeing lines before adding a compartment.

## 5. PubMed: nothing on this protein

- `GOX1598` as a PubMed query returns **0 hits** (E-utilities, 2026-10-28).
- The entry's only cited reference is the 621H genome paper
  [PMID:15665824 "we sequenced the complete genome of G. oxydans 621H."], which
  reports the genome, not this gene.
- Searching *Gluconobacter oxydans* + aldo-keto reductase returns 10 records,
  none of which names GOX1598 or Q5FQK7.

So `UNDECIDED` would be the right action for any claim about what this protein
does *in vivo*; there is no literature to be undecided about for the one
sequence-based claim I do make, which is argued from signatures and my own
alignment.

## 6. IMPORTANT: the CMMMech grounding for this accession is a locus-tag collision

This protein entered our queue through CMMMech
(`/home/user/CMMMech/data/records/neodymium.yaml`), which grounds a causal-graph
node `gox1598_putative_oxidoreductase` to `UniProtKB:Q5FQK7` with:

> `functional_role: Putative oxidoreductase GOX1598 (GO_1598) whose clean deletion in
> Gluconobacter oxydans B58 increased neodymium extraction from synthetic Mon2 mixed
> phosphate by ~111% relative to proxy wild-type.`

Three things in that are wrong, and they compound. **CMMMech is read-only for
this work, so this is recorded here and in the PR body rather than fixed**; these
are errors in CMMMech's own fields, not in GOA/UniProt/InterPro, so they are not
`source_defects` either.

1. **`GO_1598` is not `GOX1598`.** The experiment is in
   [PMID:40301604] (Marecos et al. 2025, *Commun Biol* 8:682), whose strain is
   *G. oxydans* **NRRL B-58**, a different strain from 621H with its own genome
   annotation: [PMID:34795278 "Gluconobacter oxydans strain NRRL B-58 (GoB58) was obtained from the American Type Culture Collection (ATTC), Manassas, VA."]
   and that genome has 3283 ORFs
   [PMID:34795278 "oxydans B58 genome and identified 3283 open reading frames"],
   against 2,432 chromosomal ORFs in 621H
   [PMID:15665824 "chromosome consists of 2,702,173 base pairs and contains 2,432 open reading"].
   The `GO_####` and `GOX####` series are unrelated numberings.
2. **The paper's `GO_1598` is a different enzyme entirely.** Its Table 2 and
   Discussion state
   [PMID:40301604 "GO_1598 codes for the orotate phosphoribosyltransferase enzyme PyrE which catalyzes the production of orotidine monophosphate (OMP), using phosphoribosyl diphosphate (PRPP) and orotate"].
   Orotate phosphoribosyltransferase is EC 2.4.2.10, a type I PRTase — it is not
   an aldo-keto reductase and shares no fold with Q5FQK7. The 621H counterpart of
   the gene the paper disrupted is **`pyrE` = GOX1998 = UniProtKB:Q5FPG2**
   ("Orotate phosphoribosyltransferase (OPRT) (OPRTase) (EC 2.4.2.10)", UniProt
   REST query on proteome UP000006375). The same collision affects the sibling
   grounding in that record: the paper's `GO_1096` is
   [PMID:40301604 "GO_1096 codes for the GTP-binding protein TypA which has been linked to stress response"],
   whose 621H counterpart is `bipA` = GOX0636 = Q5FT83, *not* the `gcvH`
   (glycine cleavage system H) that CMMMech labels `GO_1096`. The word "glycine"
   does not occur anywhere in PMID:40301604.
3. **It was not a clean deletion.** The paper distinguishes transposon
   disruptions (δ) from markerless deletions (Δ) explicitly, and only `GO_1096`
   was made as a clean deletion and an overexpression strain. `δGO_1598` is a
   transposon disruption mutant, and the +111% figure is for that disruption.
   The paper also records that `δGO_1598` did **not** change biolixiviant pH.

**Consequence for this review:** PMID:40301604 supports nothing about Q5FQK7. It
is kept in `references` with `relevance: LOW` and a `reference_review` recording
why, so the negative finding is not lost. No bioleaching, metal-binding or
nucleotide-metabolism annotation is made for this protein, and the +111%
phenotype is not cited as evidence for anything here.

Separately — and this is the deeper point the brief asked about — even if the
locus tags *had* matched, a disruption mutant extracting more neodymium would not
license a process annotation. That is necessity/perturbation evidence about a
downstream outcome, and GO's `involved_in` requires the gene product to perform
some of the work of the process. The paper's own proposed mechanism is that
losing the enzyme leaves more of its **substrate** (orotate) around to chelate
lanthanides
[PMID:40301604 "One way that the disruption of GO_1598 could increase bioleaching is by increasing availability of orotate, which is known to chelate metals"] —
i.e. the metal binding is done by a small molecule, not by the protein, and the
protein's loss is what helps. Nothing there is participation by the gene product.

## 7. Consistency with the sibling GLUOX reviews

`gdh` (P27175), `pqqC` (Q9L3B2), `pstS` (Q5FTI1) and `pstC` were reviewed on
parallel branches from the same CMMMech record. Those four are genuine
Swiss-Prot/well-grounded entries in pathways the literature ties to
biolixiviant production, and their reviews cite PMID:40425722 and PMID:34795278
for strain-B58 phenotypes while annotating the 621H proteins on family and
curated-function grounds. This review is consistent with that approach but
reaches a much weaker conclusion, for a reason specific to this accession: the
phenotype CMMMech attached to it belongs to a different gene (§6), and the entry
itself carries no curated function.

Note for whoever reviews `gcvH`/Q5FRY1 from the same CMMMech record: the
`GO_1096` grounding there has the same defect (§6, point 2).

## 8. Actions taken in the review file

- One annotation row, `action: NEW`: `GO:0016616` *oxidoreductase activity,
  acting on the CH-OH group of donors, NAD or NADP as acceptor*, `evidence_type:
  ISS`, `qualifier: enables`, supported by the UniProt signature lines and by
  `file:GLUOX/GOX1598/GOX1598-bioinformatics/RESULTS.md`. It carries the
  interpro2go `source_defects` entry from §2.
- One `core_functions` entry at the same level, with the substrate, cofactor and
  physiological role stated as unknown in `knowledge_gaps`.
- `suggested_questions` and `suggested_experiments` aimed at the three real
  unknowns: cofactor specificity, substrate, and whether this locus has any role
  in *G. oxydans* oxidative metabolism at all.
