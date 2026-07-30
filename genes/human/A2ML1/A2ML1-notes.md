# A2ML1 (alpha-2-macroglobulin-like protein 1) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(`A2ML1-deep-research-affinage.md`) plus UniProt A8K2U0, the GOA TSV and the primary
literature.

## Provider caveat (gate tripped)

The affinage record for A2ML1 **failed its trust gate**: affinage's own head-to-head
self-evaluation scored it `pairwise = loss` against the curated UniProt reference
(recorded in the record's own `self_evaluation_pairwise` frontmatter field). Everything taken from it was therefore re-verified against the
cited PMIDs before use. In the event the narrative held up well — its core claim
(secreted broad-spectrum alpha-2-macroglobulin-family protease inhibitor of stratified
epithelia) matches UniProt and PMID:16298998 exactly. Where it is weakest is exactly where
the gate would predict: it presents the Noonan-syndrome association as a finding and only
then notes the refutation, and it offers no molecular detail on the trapping mechanism that
defines this family.

## What the protein is

A2ML1 is a **secreted, monomeric, ~180 kDa member of the alpha-2-macroglobulin (α2M)
protease-inhibitor family (MEROPS I39)**, and the first α2M-family member found in
epidermis [PMID:16298998, "Therefore, alpha2ML1 is the first alpha2M family member detected
in the epidermis."]. UniProt annotates a cleaved signal peptide (1–17), a mature chain
(18–1454), the diagnostic **bait region** (695–726) and the **isoglutamyl cysteine
thioester** crosslink (970↔973)
[file:human/A2ML1/A2ML1-uniprot.txt, "Isoglutamyl cysteine thioester (Cys-Gln)"].

The mechanism is the α2M "trap": a protease cleaves the bait region, the inhibitor undergoes
a conformational change that entraps the enzyme, and the thioester is hydrolysed to form a
covalent bond to the protease
[file:human/A2ML1/A2ML1-uniprot.txt, "Is able to inhibit all four classes of proteinases by a"].
The covalent step was shown directly for A2ML1
[PMID:16298998, "alpha2ML1 binds covalently to these proteases, a feature shared with other
members of the family."].

## Inhibitory spectrum — endopeptidases across catalytic classes

Recombinant A2ML1 inhibits **chymotrypsin (serine), papain (cysteine), thermolysin (metallo),
subtilisin A (serine)** and weakly elastase, but **not trypsin**
[PMID:16298998, "Recombinant alpha2ML1 displayed inhibitory activity toward chymotrypsin,
papain, thermolysin, subtilisin A, and to a lesser extent, elastase but not trypsin."].

All of these are **endopeptidases**, which matters for the GO calls:

- The IDA `GO:0030414 peptidase inhibitor activity` is the *parent* of the IEA
  `GO:0004866 endopeptidase inhibitor activity`. The experimental data support the more
  specific child, so the IDA is `MODIFY`ed up to `GO:0004866` — which is also the term A2M
  itself carries by IDA/IBA/IEA. The IEA is `ACCEPT`ed as already correct.
- The IDA `GO:0052548 regulation of endopeptidase activity` is sign-neutral, but every
  measured effect is inhibition. `MODIFY` to `GO:0010951 negative regulation of endopeptidase
  activity`.

The chymotrypsin-like kallikrein **KLK7** is a physiologically meaningful target: it is a
desquamation protease of the stratum corneum, and A2ML1 binds it covalently
[PMID:16298998, "Incubation with chymotrypsin and the chymotrypsin-like kallikrein 7 protease"].
This supports a `NEW GO:0002020 protease binding` annotation alongside the inhibitor activity —
the covalent complex is a demonstrated binding event, not merely inferred from inhibition.

## Localisation — the missing compartment

GOA has only `GO:0005576 extracellular region` (plus an exosome HDA). The primary paper gives
a much more specific, and currently unannotated, intracellular location: A2ML1 sits in
**keratinosomes** (= epidermal lamellar bodies / lamellar granules / Odland bodies) in the
granular layer before secretion
[PMID:16298998, "alpha2ML1 was detected within keratinosomes in the granular layer of the
epidermis, and as a secreted product in the extracellular"].

`GO:0097209 epidermal lamellar body` is the exact term ("a specialized secretory organelle
found in keratinocytes…"), so this is proposed as a `NEW` IDA annotation. This is the single
most informative annotation missing from A2ML1's GOA record.

## Expression and disease (recorded, not annotated)

- Expressed mainly in **epidermal granular keratinocytes**, up-regulated during keratinocyte
  differentiation [PMID:16298998, "mainly in the epidermis granular keratinocytes"]. Expression
  pattern, not a function — no process annotation made.
- **Desquamation**: UniProt and the primary paper both hedge ("May play an important role
  during desquamation"). Speculative; recorded in `suggested_questions`, not annotated.
- **Otitis media** susceptibility (MIM:166760) is the established disease link, supported by
  human pedigree/LOD data and an *A2ml1*-knockout mouse with spontaneous middle-ear disease
  [PMID:26121085; PMID:38759260 via the affinage report]. Disease association, not a GO
  process.
- **Paraneoplastic pemphigus**: A2ML1 is the p170 autoantigen [PMID:20805888]. Being an
  autoantigen is not a molecular function.
- **Noonan-like syndrome**: reported for heterozygous A2ML1 variants with zebrafish support
  [PMID:24939586], but a later systematic segregation analysis across RASopathy families found
  the variants inherited from unaffected parents alongside alternative causal aberrations
  [PMID:33082526]. Contested; not used. The affinage narrative does report both sides.

## Summary of curation actions

| Term | Evidence | Action |
|---|---|---|
| `GO:0004866` endopeptidase inhibitor activity | IEA | ACCEPT (core MF) |
| `GO:0030414` peptidase inhibitor activity | IDA | MODIFY → `GO:0004866` |
| `GO:0052548` regulation of endopeptidase activity | IDA | MODIFY → `GO:0010951` |
| `GO:0005576` extracellular region | IEA, IDA | ACCEPT (core CC) |
| `GO:0070062` extracellular exosome | HDA | KEEP_AS_NON_CORE |
| `GO:0002020` protease binding | IPI (proposed) | NEW |
| `GO:0097209` epidermal lamellar body | IDA (proposed) | NEW |
