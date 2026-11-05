# park (parkin, Q7KTX7, FBgn0041100) - manual literature synthesis

No deep-research provider was available for this review. This summary was written by the
reviewer from cached publications in `publications/` and the UniProt record
(`park-uniprot.txt`). Every claim carries its provenance.

## Identity and domain architecture

- Drosophila melanogaster parkin, 482 aa, the single fly ortholog of human PRKN. UniProt
  places it in the RBR family, parkin subfamily: "Belongs to the RBR family. Parkin
  subfamily." [file:genes/DROME/park/park-uniprot.txt]
- Domains: N-terminal ubiquitin-like (Ubl, 30-99), RING0, RING1, IBR and RING2 (Rcat)
  zinc-binding domains; InterPro IPR003977 Parkin, IPR031127 E3_UB_ligase_RBR.
- Catalytic cysteine: Cys449 of the fly protein (Cys431 in human) on RING2 [PMID:23770917
  "A single cysteine residue (C449; C431 in human) is exposed on the β2–β3 loop"].

## Enzymatic activity

- RBR E3 ligase, E2-dependent: [PMID:17456438 "D. melanogaster Parkin exhibited UbcH8-dependent
  E3 ubiquitin-protein ligase activity"]; E2 binding is via RING1 [PMID:17456438 "D.
  melanogaster Parkin as an E3 ligase interacts with UbcH8 through its RING1 domain"].
- Autoubiquitination [PMID:17456438 "D. melanogaster Parkin existed in ubiquitinated form in
  vivo"]; autoubiquitination occurs only in cis [PMID:23770917 "parkin autoubiquitinates only in
  cis"].
- Activation by PINK1: phosphorylation of Ser94 in the Ubl [PMID:24901221 "we have shown that
  Parkin phosphorylation by PINK1 drives Parkin E3 activity in vivo"]; phospho-Ser94 is required
  for activation but not for translocation in the fly eye [PMID:27906179 "phosphorylation of
  Parkin by PINK1 is dispensable for its translocation but required for its activation"].
  An earlier paper reported a linker-region phosphorylation promoting translocation
  [PMID:18957282 "Parkin phosphorylation by PINK1 on its linker region promotes its
  mitochondrial translocation"].

## Substrates (fly proteins, or fly orthologs assayed)

- Marf (mitofusin): [PMID:20194754 "PINK1 and Parkin mediate the ubiquitination of the profusion
  factor Mfn on the outer surface of mitochondria"]; co-IP [PMID:20194754 "Immunoprecipitation
  assays revealed that upon coexpression Parkin-GFP is detected in precipitates of Mfn-Flag"];
  [PMID:24898855 "Parkin was used as a positive control and co-immunoprecipitated with Mfn as
  previously reported"].
- Porin/VDAC: mono- and polyubiquitination [PMID:32047033 "Porin mono- and polyubiquitination
  by Parkin occurred in a highly conserved manner"].
- Paris: [PMID:32138754 "parkin mediated ubiquitination of dPARIS targets it for proteosomal
  degradation, thereby promoting DA neuron survival in vivo"].
- Koi (LINC complex, in vitro): [PMID:29689197 "when performing in vitro ubiquitination assays,
  we found that Parkin can also mono-ubiquitinate Koi"].
- Septins peanut and Septin1: [PMID:17456438 "peanut and septin1, D. melanogaster septin
  proteins, were also ubiquitinated by D. melanogaster Parkin"].

## Localization

- Cytosolic at rest, recruited to mitochondria upon depolarization in a PINK1-dependent manner
  [PMID:20194754 "In wild-type Drosophila cells, Parkin-GFP typically showed a diffuse
  localization throughout the cytoplasm with occasional accumulations at mitochondria"];
  [PMID:24901221 "The Parkin and PINK1 genes encode a cytosolic ubiquitin-ligase"];
  [PMID:27906179 "Although Parkin colocalized with wild-type PINK1 and TOM20 on mitochondria"].
- Recruitment is transient and to the cytosolic face of the outer membrane; no ER or Golgi
  localization has been reported for the fly protein in the cached literature.

## Processes

- Mitophagy: [PMID:20194754 "Parkin was also required for CCCP-induced mitophagy in Drosophila
  cells"]; in vivo turnover [PMID:23509287 "parkin null mutants showed a significant overall
  slowing of mitochondrial protein turnover"]; developmental clearance of mitochondria in the
  intestine [PMID:37633267 "The E3 ubiquitin ligase Parkin functions downstream of PINK1 and is
  required for mitochondrial clearance while having the opposite function in ER clearance"];
  heart [PMID:24192653 "Parkin deficiency and resulting mitophagic disruption produces
  cardiomyopathy"].
- Mitochondrial dynamics: loss raises Marf and elongates mitochondria [PMID:20194754 "Loss of
  Drosophila PINK1 or parkin causes an increase in Mfn abundance in vivo and concomitant
  elongation of mitochondria"]; genetic interactions suggest the pathway promotes fission and/or
  inhibits fusion, but parkin is not part of the fission machinery [PMID:18799731 "These results
  suggest that pink1 and parkin are likely not core components of the drp1-mediated
  mitochondrial fission machinery"].
- Mutant phenotypes (downstream of mitochondrial dysfunction): muscle degeneration, male
  sterility [PMID:12642658 "Drosophila parkin null mutants exhibit reduced lifespan, locomotor
  defects, and male sterility"]; spermatid mitochondrial derivative defects [PMID:17123504];
  DA neuron degeneration [PMID:15911761]; JNK hyperactivation [PMID:16002472 "Parkin inhibits
  the JNK signaling pathway in an E3 activity-dependent manner"]; female sterility
  [PMID:20869429]; oxidative stress/metal sensitivity [PMID:20483372; PMID:21383066]; ATP
  synthase defects rescued by GstO1 [PMID:22219196 "expression of DmGSTO1 partially restores
  the activity and assembly of the mitochondrial F(1)F(0)-ATP synthase in parkin mutants"];
  circadian and memory phenotypes [PMID:28435104].
