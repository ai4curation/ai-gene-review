# Atg8a (Drosophila melanogaster) review notes

## Entry and fetch

- FlyBase FBgn0052672, CG32672, X chromosome. Reviewed accession: Q9W2S2 (isoform A, 121 aa,
  unreviewed TrEMBL entry, no FUNCTION comment). It carries 38 GOA rows, including the 8 PAINT
  IBA rows.
- A second UniProt entry for the same gene, X2JJA8, carries 20 rows, all but two of them
  FlyBase rows that also sit on Q9W2S2 (protein kinase binding IPI, protein tag activity ISS,
  macroautophagy, larval midgut cell programmed cell death, determination of adult lifespan IMP,
  regulation of protein ubiquitination, autophagosome, amphisome and autolysosome IDA). The two
  rows found only on X2JJA8 are determination of adult lifespan IGI (PMID:24244197) and a UniProt
  membrane IEA (GO_REF:0000044). This review covers only the Q9W2S2 rows (QuickGO annotation
  search for UniProtKB:X2JJA8, 2026-11-17).
- QuickGO annotation searches with `includeFields=taxonName` still returned HTTP 500 on
  2026-11-17, so the GOA file was fetched with the project's `fetch-gene` command wrapped to drop
  only that field and fill the taxon name from taxon 7227. The rows are otherwise as QuickGO serves
  them.
- Deep research: no Falcon/Perplexity keys in this environment; the FlyBase hand-written
  description (`Atg8a-deep-research-flybase.md`) is the only provider text.

## Literature searches run (PubMed E-utilities, 2026-11-17)

- `Atg8a[tiab] AND (GABA[tiab] OR Rdl[tiab] OR GABARAP[tiab]) AND Drosophila` (2 hits:
  PMID:38882929, a behavioural micropublication; PMID:29989488, LAMP2A and SNCA). Neither tests
  binding of Atg8a to any GABA receptor subunit. No fly study of Atg8a binding a GABA receptor was
  found.
- `Atg8a[tiab] AND mitophagy[tiab]` (12 hits; PMID:34459871 and PMID:40801807 used).
- `Atg8a[tiab] AND (ubiquitin ligase[tiab] OR E3[tiab])` (6 hits, none on an Atg8a-E3 interaction
  in the fly); `Atg8a[tiab] AND (ligase OR Mib1 OR Bruce OR parkin OR ubiquitination) AND
  Drosophila[tiab]` (8 hits); `Atg8a[tiab] AND (LIR OR AIM OR interacting region)` (15 hits;
  PMID:35226578, PMID:35649355, PMID:32460019 used).
- `Atg8a[tiab] AND (Plekhm1 OR HOPS OR Epg5 OR autophagosome-lysosome fusion OR autophagosome
  maturation) AND Drosophila` (5 hits); `Plekhm1 AND Drosophila` (3 hits); `Klp98A AND Atg8a`
  (1 hit, PMID:26763909).
- `Atg8a[tiab] AND lipidation[tiab] AND Drosophila[tiab]` (2 hits: PMID:40426043, PMID:33249988).
- `Atg8a[tiab] AND (climbing OR locomotor OR neuromuscular OR neurodegeneration) AND Drosophila`
  (28 hits; PMID:38701988 used) and `Atg8a[tiab] AND lifespan[tiab]` (24 hits; PMID:18059160).
- `insect GABA receptor subunits RDL LCCH3 GRD` (11 hits; PMID:20924418 used).

## What Atg8a is

- One of two fly Atg8-family proteins. On the PANTHER PTHR10969 tree (bioinformatics folder)
  Atg8a and Atg8b come from a Diptera-level duplication inside the GABARAP clade
  (PTN000861087), not the LC3 clade. Atg8a is 88% identical to human GABARAP and about 31% to
  LC3A/LC3B (`Atg8a-bioinformatics/RESULTS.md`). Atg8b is testis-restricted and dispensable for
  autophagy [PMID:33249988 "expression of Atg8b is restricted to the male germline and its loss
  causes male sterility without affecting autophagy"].
- Ubiquitin-like protein with Gly116 followed by five residues (MAKIN) that Atg4 removes.
  Conjugated to phosphatidylethanolamine by the Atg7/Atg3/Atg12-Atg5-Atg16 system
  [PMID:37248218 "we replaced the codon coding for the glycine near the C-terminus (Gly116, to be
  conjugated to PE) with a stop codon in the endogenous Atg8a locus (Atg8aG116*)"; PMID:23873149
  "Small amounts of lipidated Atg8a (Atg8a-II) were detected in wild-type midgut extracts, but not
  in either Atg7 or Atg8a mutant midguts"]. In vitro, Atg7 forms a thioester with Atg8a
  [PMID:23873149 "As expected, Uba1 and Atg7 were charged with ubiquitin and Atg8a, respectively"].
- The PE bond is covalent (amide to the ethanolamine head group). GO defines binding as
  "The selective, non-covalent, often stoichiometric, interaction of a molecule with one or more
  specific sites on another molecule" (GO:0005488, QuickGO 2026-11-17), and GO:0008429 is a child
  of it. Protein tag activity (GO:0031386) is defined for a protein "covalently attached ... to
  another protein". Neither definition fits a ubiquitin-like protein whose conjugation target is a
  lipid. No fly study shows Atg8a attached to a protein.

## Function in the fly (experimental)

- Autophagosome formation: Atg8a mutant enterocytes have fewer autophagosomes [PMID:37633267
  "By contrast, Atg8aΔ mutant intestine enterocytes exhibit decreased autophagosome structures"];
  lipidated Atg8a is required for autophagy [PMID:33249988 "lipidated Atg8a is required for
  autophagy, while its non-lipidated form is essential for developmentally programmed larval midgut
  elimination and viability"].
- Location: mCherry-Atg8a marks "all autophagic structures: phagophores, autophagosomes and
  autolysosomes" [PMID:25481477]; Atg8a-II is the "membrane-associated, faster migrating active
  form" [PMID:25481477]. Also seen in amphisomes (PMID:22863314) and autolysosomes (PMID:20713604)
  and at presynaptic boutons (PMID:27720484).
- LIR docking: Atg8a-LDS (K48A/Y49A) knock-in flies "cannot bind to LIRCPs", accumulate Ref(2)P,
  Kenny and ubiquitinated proteins and have a reduced lifespan, like Atg8a nulls [PMID:35649355].
  LIR partners in the fly include Atg1 (PMID:23043107), DOR/TP53INP (Y2H, PMID:14605208,
  PMID:37061542), Sequoia, YL-1 and Sir2 (PMID:32460019), GMAP (Golgi turnover, PMID:35649355),
  the ER-phagy receptors Atl and Trp1 [PMID:37633267 "Atl and Trp1 interact with Atg8a through
  putative LC3-interacting region (LIR) motifs"], and, by Y2H, Nedd4 (PMID:35226578).
- Mitophagy: in vps13d and pink1 mutant midgut cells Atg8a accumulates around mitochondria that
  fail to be cleared [PMID:34459871 "Atg8a puncta in these mutant cells were enlarged and seemed
  to localize around ATP5a-labeled mitochondria that failed to be degraded"]. BNIP3 carries a LIR
  and an Atg18a-binding MER motif that together are needed for mitophagy in remodelling muscle
  (PMID:40801807). No study found that measured mitochondrial retention in Atg8a mutant cells.
- Maturation and fusion: Klp98A, needed for autophagosome-lysosome fusion, associates with Atg8
  [PMID:27142690 "This function correlates with the association of Klp98A with the autophagosomal
  protein Atg8 and with the endolysosomal protein Rab14"]. In glial LC3-associated phagocytosis,
  Atg8a conjugation to phagosomes promotes their fusion with lysosomes (PMID:37248218).
- Lipidation-independent roles: non-lipidated Atg8a is needed for midgut elimination and viability
  (PMID:33249988); midgut removal needs Atg8a but not Atg7/Atg3 (PMID:23873149, PMID:25882046).
- Organismal: loss of Atg8a reduces lifespan and climbing and causes neuronal degeneration
  [PMID:38701988 "the loss of Atg8a affected autophagy and resulted in partial lethality, abnormal
  wings, decreased lifespan, and decreased climbing ability in flies"; PMID:18059160 "Mutations in
  the Atg8a gene (autophagy-related 8a) result in reduced lifespan, IUP accumulation and increased
  sensitivity to oxidative stress"].
- Starvation in fly experiments is a move to a sugar-only diet [PMID:25481477 "feeding larvae are
  usually transferred from a rich culture medium to 20% sucrose"], i.e. amino-acid deprivation.

## IBA rows (PANTHER PTHR10969)

- Root PTN000103522 (Eukaryota): autophagosome assembly, autophagosome membrane, mitophagy,
  autophagosome maturation, nitrogen starvation, PE binding.
  - assembly and membrane: ACCEPT, core; fly data agree.
  - mitophagy (seed human LC3B only): KEEP_AS_NON_CORE; Atg8a decorates mitophagic phagophores in
    the fly, one selective route of several.
  - maturation: KEEP_AS_NON_CORE; fly support is the Klp98A association and the analogous
    phagosome-lysosome fusion result. The GO definition ("Removal of PI3P and Atg8/LC3 ...") makes
    Atg8 the thing removed, so the term fits Atg8 only through its recruitment of fusion factors.
  - nitrogen starvation (seed Dictyostelium atg8a only): MODIFY to cellular response to amino acid
    starvation (GO:0034198), the stimulus actually used in fly autophagy work.
  - PE binding: MARK_AS_OVER_ANNOTATED. The PE link is real and defining, but covalent; GO binding is
    non-covalent. The same diagnosis applies to the ISS protein tag activity row. The other Atg8-family
    reviews in this repository (human GABARAP and MAP1LC3B, yeast ATG8, worm lgg-1) accept PE binding as
    GO's way of recording lipidation; this review departs from that and raises it as a question.
- PTN000103525 (duplication node above the GABARAP/LC3 split): ubiquitin protein ligase binding,
  seeded by human Atg8-family proteins. Fly: Nedd4 by Y2H only. KEEP_AS_NON_CORE (one class of LIR
  partner), as in the human reviews.
- PTN000861087 (Eumetazoa GABARAP clade): GABA receptor binding, seeded by rat and human GABARAP,
  whose partner is the GABA-A receptor gamma2 subunit [PMID:9892355 "GABARAP, which can interact
  with the gamma2 subunit of GABA(A) receptors"]. Insects have RDL, LCCH3 and GRD subunits rather
  than vertebrate gamma subunits [PMID:20924418 "including three RDL, one LCCH3, and one GRD
  subunit"]. No fly binding data (searches above). Atg8a keeps the GABARAP sequence (88% identity),
  so a binding capacity is not excluded, but nothing shows a fly partner. MARK_AS_OVER_ANNOTATED.

## Other decisions

- NEW: protein-membrane adaptor activity (GO:0043495), IMP from the Atg8a-LDS flies (PMID:35649355)
  with the lipidation data: the PE-anchored protein recruits LIR proteins to autophagic membranes.
  This gives the review a core MF that GO's definitions allow, in place of PE binding.
- Bare protein binding rows (DOR, Atg7): REMOVE per policy; the interactions are real.
- autophagy (PMID:33249988): MODIFY to macroautophagy. phagocytosis (PMID:37248218): MODIFY to
  phagosome-lysosome fusion, which the same paper shows.
- regulation of protein ubiquitination (PMID:17435236, abstract only): MARK_AS_OVER_ANNOTATED; the
  measured phenotype is accumulation of ubiquitinated proteins, a degradation defect.

## FlyBase description

"Autophagy-related 8a (Atg8a) encodes a ubiquitin-like protein that is conjugated to
phosphatidylethanolamine, and this lipid modification anchors it into the membrane of forming and
completed autophagosomes. Atg8a product has roles in autophagosome formation, maintaining
neuromuscular function and normal lifespan."

- Every claim traced: PE conjugation (PMID:23873149, PMID:37248218), membrane of forming and
  completed autophagosomes (PMID:25481477), autophagosome formation (PMID:37633267), neuromuscular
  function (PMID:38701988: climbing, muscle integrity, neuronal degeneration), lifespan
  (PMID:18059160, PMID:35649355). Correctness VERIFIED.
- Omissions: the LIR-docking role in selective autophagy, and the lipidation-independent essential
  roles (midgut removal, viability; PMID:33249988). The second is recorded as a MISSING_STATEMENT,
  because the text presents lipidation as the way Atg8a works.
- UniProt: unreviewed record without a FUNCTION comment, so no UniProt text to check.
