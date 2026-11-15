# aroQ (P9WPX7, Mycobacterium tuberculosis H37Rv, Rv2537c) review notes

## Provenance of this notes file

Provider deep research was unavailable for this review (no deep-research provider key in
the session), so no `aroQ-deep-research-*.md` file exists. These notes were compiled by the
reviewer from the cached publications in `publications/` (PMID:12387860 and PMID:1910148
were fetched for this review), the UniProt record (`aroQ-uniprot.txt`), the cached
Reactome reaction R-MTU-964851, the PTHR21272 family review
(`interpro/panther/PTHR21272/PTHR21272-review.yaml`, for which AroQ is the reference
protein) and one UniProt REST query recorded below.

Family: PANTHER PTHR21272 (CATABOLIC 3-DEHYDROQUINASE), subfamily PTHR21272:SF3, under the
PAINT root node PTN000479790; InterPro IPR001874/IPR018509/IPR036441, Pfam PF01220,
NCBIfam TIGR01088, HAMAP MF_00169, PROSITE PS01029. No PAINT IRD/IKR loss on the AroQ
lineage (`just paint-losses MYCTU aroQ`).

## Gene and evolutionary origin

- Cloned with aroB; unrelated to the E. coli-type (type I) biosynthetic DHQase but similar
  to the fungal catabolic DHQases.
  [PMID:1910148 "Surprisingly, the deduced M. tuberculosis 3-dehydroquinase amino acid sequence showed no similarity to other characterised prokaryotic biosynthetic 3-dehydroquinases (bDHQases)."]
  [PMID:1910148 "This finding indicates a common ancestral origin for genes encoding the catabolic dehydroquinases of fungi and the biosynthetic dehydroquinases present in some prokaryotes."]
- Reviewer check (UniProt REST, 2026-11-11): `query=ec:4.2.1.10 AND organism_id:83332`
  returned only P9WPX7 (aroQ, Rv2537c), so AroQ is the only annotated 3-dehydroquinase of
  M. tuberculosis H37Rv and must supply the shikimate-pathway step.

## Activity and structure

- Type II 3-dehydroquinase (EC 4.2.1.10), 3-dehydroquinate = 3-dehydroshikimate + H2O.
  Purified recombinant enzyme:
  [PMID:1329726 "The M. tuberculosis type-II 3-dehydroquinase has been purified in bulk from overproducing strains of E. coli to greater than 95% homogeneity."]
  [PMID:1329726 "The protein is extremely heat-stable, is active as a homododecamer and has the lowest reported Km value of any type-II 3-dehydroquinase."]
  The gene also supported quinate growth when expressed in a fungal qutE mutant:
  [PMID:1329726 "shown to encode quinate-inducible 3-dehydroquinase activity that allows a qutE- mutant strain of A. nidulans to utilize quinate as sole carbon source."]
  This shows catalytic capacity in a heterologous catabolic pathway, not a catabolic role
  in M. tuberculosis.
- Mechanism: [PMID:10360352 "the type II enzymes catalyze a trans-dehydration via an enolate intermediate."]
  Gourley et al. solved the M. tuberculosis type II structure (PDB 2DHQ in the UniProt
  record) together with a type I enzyme:
  [PMID:10360352 "Both enzymes function as part of the shikimate pathway, which is essential in microorganisms and plants for the biosynthesis of aromatic compounds including folate, ubiquinone and the aromatic amino acids."]
- Active site (UniProt FT, structure-based): Tyr-25 proton acceptor, His-102 proton donor,
  Arg-20 transition-state stabilizer; many inhibitor complexes (PDB 1H05, 2Y71, 4KI7 ...).
- Substrate recognition by polyanions: [PMID:12387860 "The interactions between the polyanionic ligands phosphate and sulphate and the type II dehydroquinases from Streptomyces coelicolor and Mycobacterium tuberculosis have been characterised using a combination of structural and kinetic methods."]
- Quaternary structure: homododecamer (UniProt SUBUNIT, from PMID:10360352, PMID:12387860).

## Pathway role

- Reactome R-MTU-964851: [Reactome:R-MTU-964851 "Unlike fungi DHQ dehydratases, AroQ doesn't take part in catabolism reactions (Moore et al, 1992)."]
- UniProt PATHWAY: chorismate biosynthesis, step 3/7. AroQ is thus the biosynthetic
  DHQase of M. tuberculosis. The PTHR21272 family review judges the PAINT quinate
  catabolism IBD at the family root (PTN000479790) TOO_DEEP: it is seeded only by A. nidulans
  QutE and passes the catabolic process to the bacterial biosynthetic AroQ enzymes.

## Localization

- Soluble cytosolic enzyme (no signal peptide or transmembrane segment; small 147-residue
  dodecamer). Reactome places the reaction in the cytosol.
