# al-1 (P21334, NCU00552) — Neurospora crassa phytoene desaturase (albino-1)

## Identity

- UniProt P21334, entry name CRTI_NEUCR; gene `al-1`, ORF NCU00552, linkage group I.
- 595 aa precursor. RecName "Phytoene desaturase"; EC 1.3.99.-; AltNames "Albino-1
  protein", "Phytoene desaturase (3,4-didehydrolycopene-forming)"
  [file:NEUCR/al-1/al-1-uniprot.txt].
- Family: carotenoid/retinoid oxidoreductase family (CrtI-type), FAD/NAD(P)-binding
  fold [file:NEUCR/al-1/al-1-uniprot.txt "Belongs to the carotenoid/retinoid
  oxidoreductase family"]. InterPro IPR002937 (Amino_oxidase), IPR014105
  (Carotenoid/retinoid_OxRdtase), IPR008150 (Phytoene_DH_bac_CS); PANTHER PTHR43734
  PHYTOENE DESATURASE (SF1); TIGRFAM crtI_fam.
- Identity check positive: this is unambiguously the N. crassa carotenoid desaturase,
  not a same-symbol gene from another organism (deep research executive conclusion;
  UniProt; PMID:2144609 which cloned al-1 as the carotenoid gene).

## Core molecular function

Single CrtI-type FAD-dependent desaturase that introduces up to FIVE double bonds into
15-cis-phytoene, unlike bacterial CrtI which stops at four (lycopene). Direct
biochemical evidence: Al-1 expressed in E. coli, purified, and assayed
[PMID:11017770 "an active enzyme was isolated which catalyzed the stepwise introduction"
/ "of up to five double bonds into the substrate phytoene"]. Major products
3,4-didehydrolycopene and lycopene [PMID:11017770 "products were 3, 4-didehydrolycopene
and lycopene"]. Desaturation intermediates zeta-carotene, neurosporene and lycopene are
themselves accepted as substrates [PMID:11017770 "intermediates, zeta-carotene,
neurosporene, and lycopene, were also accepted as"]. Cofactor is NAD, distinguishing it
from bacterial CrtI [PMID:11017770 "the cofactor involved in the dehydrogenation
reaction was NAD for Al-1"; file:NEUCR/al-1/al-1-uniprot.txt "Name=NAD(+);
Xref=ChEBI:CHEBI:57540"].

UniProt records five sequential Rhea catalytic-activity reactions
(RHEA:30603, 30607, 30611, 30623, 30979) covering
phytoene -> phytofluene -> zeta-carotene -> neurosporene -> lycopene ->
3,4-didehydrolycopene [file:NEUCR/al-1/al-1-uniprot.txt "phytoene into
3,4-didehydrolycopene via the intermediates phytofluene" / "zeta-carotene, neurosporene
and lycopene, by introducing up to five"]. KM 30 uM phytoene, 32 uM lycopene
[file:NEUCR/al-1/al-1-uniprot.txt "KM=30 uM for phytoene"]. Pathway assignment
"Carotenoid biosynthesis; lycopene biosynthesis".

The five products of Al-1 (phytofluene, zeta-carotene, neurosporene, lycopene,
3,4-didehydrolycopene) are all hydrocarbon carotenes, so the activity contributes to
both carotenoid biosynthetic process (GO:0016117) and carotene biosynthetic process
(GO:0016120, QuickGO: "formation of carotenes, hydrocarbon carotenoids").

Substrate boundary: gamma-carotene is NOT a substrate, so torulene must arise by
cyclization of 3,4-didehydrolycopene rather than desaturation of gamma-carotene
[PMID:11017770 "gamma-carotene is not accepted as a substrate by Al-1"]. Al-1 also
desaturates 1-hydroxyneurosporene and 1-hydroxylycopene (UniProt).

## Pathway context

GGPP --(al-2 phytoene synthase)--> 15-cis-phytoene --(AL-1, 5 desaturations)-->
3,4-didehydrolycopene --(al-2 cyclase)--> torulene --(CAO-2 cleavage)-->
apo-4'-lycopenal ... --(YLO-1)--> neurosporaxanthin. AL-1 sits between al-2's synthase
step and al-2's cyclase step; it does NOT catalyse cyclization or cleavage. Downstream
sequence confirmed by [PMID:18812228 "cyclization of 3,4-didehydrolycopene (C40)";
"represents the end-product"]. Modelled in production GO-CAM 62f58d8800000065
(Carotenoid biosynthesis, N. crassa): al-1 appears as five sequential GO:0016166
activities. al-1 is the fungal CrtI-type exemplar in
modules/carotene_backbone_biosynthesis.yaml (crti_activity annoton, PANTHER PTHR43734).

## Regulation / phenotype

al-1 mutants are albino (block converting colorless phytoene into colored carotenes).
Expression is blue-light photoinduced via the White Collar Complex
[PMID:2144609 "Carotenoid biosynthesis is regulated by blue light during growth of
Neurospora"; "the level of al-1 mRNA increased over 70-fold in photoinduced";
file:NEUCR/al-1/al-1-uniprot.txt "The expression is subject to photoinduction"].
The gene encodes a 595-residue polypeptide homologous to prokaryotic carotenoid
dehydrogenases [PMID:2144609 "The gene encodes a 595-residue polypeptide";
"carotenoid-biosynthetic enzyme phytoene dehydrogenase"].

## Localization

No direct localization experiment for AL-1 (deep research). UniProt calls it a
single-pass membrane protein based on a predicted C-terminal transmembrane helix
[file:NEUCR/al-1/al-1-uniprot.txt "TRANSMEM        574..594"; "Single-pass membrane"].
Membrane association is the reasonable inference given a predicted TM helix and the
hydrophobic polyene substrates, so GO:0016020 membrane is retained (general, inferred).

## Cached publication status

- PMID:11017770 (Hausmann & Sandmann 2000) — abstract only (full_text_available: false),
  but abstract states each biochemical result relied upon here (five-step desaturation,
  products, intermediates, NAD cofactor). Source of both IDA rows.
- PMID:2144609 (Schmidhauser 1990) — abstract only; cloning + photoregulation.
- PMID:18812228 (Estrada 2008) — abstract only; downstream apocarotenoid/neurosporaxanthin
  sequence, confirms AL-1 product feeds cyclization.

## Annotation decisions (summary)

- GO:0016166 phytoene dehydrogenase activity (IDA, IEA) — ACCEPT (core MF, direct assay).
- GO:0016117 carotenoid biosynthetic process (IDA, IBA, IEA) — ACCEPT (core BP).
- GO:0016491 oxidoreductase activity (IBA, IEA) — ACCEPT as correct general parent of the
  specific GO:0016166; IBA node placement not overruled; not core (superseded by GO:0016166).
- GO:0008299 isoprenoid biosynthetic process (IEA) — ACCEPT, correct but general ancestor
  (carotenoids are isoprenoids); non-core.
- GO:0016020 membrane (IEA) — ACCEPT, inferred from predicted C-terminal TM helix; general.
- NEW: GO:0016120 carotene biosynthetic process — AL-1 catalyses the desaturations that
  form the hydrocarbon carotenes phytofluene, zeta-carotene, neurosporene, lycopene and
  3,4-didehydrolycopene; it does the work, so participation test passes. Not a
  descendant/ancestor of GO:0016117 (per ontology), so non-redundant; the sibling
  P. ananatis crtB carries GO:0016120 for the same product class.

No REMOVE actions: the GOA set contains no paralog IEA over-annotations (no squalene
synthase or GGPP synthase activity) and no generic protein binding.
