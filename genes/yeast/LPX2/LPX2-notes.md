# LPX2 (YKL050C) — curation notes

UniProt: **P35736** (YKF0_YEAST); systematic name **YKL050C**; SGD standard name **LPX2**
(assigned 2022 by Yifrach et al.). SGD:S000001533. Taxon: *S. cerevisiae* S288C
(NCBITaxon:559292). 922 aa, ~103 kDa.

> **Identity resolution note.** `just fetch-gene yeast LPX2` failed because UniProt's
> `gene_exact:LPX2` query returns nothing — UniProt has NOT yet adopted the SGD standard
> name LPX2 and still lists the entry only under `OrderedLocusNames=YKL050C`
> (RecName: "Uncharacterized protein YKL050C"). Resolved via SGD (LPX2 → YKL050C → P35736)
> and re-fetched with `--uniprot-id P35736`. This mirror between an old ORF name and a
> new gene-symbol name is itself a small piece of the "dark gene" story.

## Summary of what is KNOWN

- **Name / proposed function.** SGD name "LPX2" = "**Lipase of PeroXisomes 2**"
  [SGD name_description: "Lipase of PeroXisomes"]. Proposed in the peroxisome-proteome
  paper Yifrach et al. 2022 [PMID:36164978, "The identification of Ykl050c as a peroxisomal
  matrix protein (Fig 2D) alongside our lipidomic results and its clear lipase activity as
  previously reported (Ploier et al, 2013) propose that Ykl050c is an additional newly
  identified peroxisomal lipase, hence we named Ykl050c, Lpx2 (Lipase of Peroxisomes 2)."].

- **Localization: peroxisomal matrix (experimental).** Yifrach 2022 place Ykl050c in the
  peroxi-ome as a matrix protein [PMID:36164978, "Our work uncovers also Ykl050c as part of
  the peroxi‐ome ..."; "The identification of Ykl050c as a peroxisomal matrix protein
  (Fig 2D)"]. This is the basis of the GOA **GO:0005777 peroxisome IDA (SGD, PMID:36164978)**
  annotation. SGD adds that "peroxisomal, nuclear and cytosolic localization is dependent on
  the presence of oleate" [SGD locus description] — i.e. localization is condition-dependent
  (oleate = peroxisome-inducing carbon source).

- **Lipidomic phenotype of the deletion.** Δykl050c had the single largest effect on the
  yeast lipidome in glucose medium, specifically an **increase in lyso-phosphatidylglycerol
  (LPG)** [PMID:36164978, "Δykl050c shows the most significant change in glucose conditions,
  with an increase of LPG lipids." ; "This strain showed significantly higher levels of
  lyso‐phosphatidylglycerol (LPG; Fig 4F)."]. This is a genetic/phenotypic association, not a
  direct enzymatic assignment.

- **Reported lipase activity.** Yifrach 2022 attribute "clear lipase activity" of Ykl050c to
  Ploier et al. 2013 [PMID:24187129]. **Caveat:** the Ploier 2013 abstract (all we can access
  — `full_text_available: false`) names **Ayr1p** as the novel triacylglycerol lipase and
  confirms **Lpx1p**; it does NOT mention Ykl050c in the abstract. Ykl050c was one of the
  GXSXG-motif candidate hydrolases screened; the specific "clear lipase activity" statement
  lives in the Ploier full text / supplement, which is not in our cache. So the biochemical
  lipase claim for LPX2 is second-hand and NOT directly verifiable from cached text.

- **Regulation.** Expression is induced by the AZF1 transcription factor
  [UniProt CC INDUCTION, ECO:0000269|PubMed:16467472; PMID:16467472 Slattery 2006]. AZF1
  activates carbon/energy-metabolism genes in glucose — consistent with a metabolic role.

- **Post-translational regulation.** SGD: "target of SCFCdc4 ubiquitin ligase complex"
  [SGD locus description; derived from Tang et al. 2005, PMID:16338374, a genome-wide screen
  for phospho-dependent SCF substrates — abstract-only in our cache, gene-specific data in
  supplement]. Consistent with the UniProt disordered regions carrying multiple
  phospho-sites (LPX2 appears in yeast phosphoproteome datasets, e.g. PMID:33491328,
  PMID:37845410).

- **Family / orthology.** LPX2 is the whole-genome-duplication (WGD) **paralog (ohnolog) of
  EIS1** [SGD locus description: "LPX2 has a paralog, EIS1, that arose from the whole genome
  duplication"]. PANTHER **PTHR28298 / :SF1 "EISOSOME PROTEIN 1"** groups P35736 together with
  *S. cerevisiae* Eis1 (Q05050) and Eis1 orthologs across budding yeasts (K. lactis,
  C. glabrata, Z. rouxii, Lachancea, S. pombe SPCC63.14). InterPro **IPR024527 "Eisosome1"**,
  Pfam **PF12757 "Eisosome1"**. So the sole domain-family signal for this protein is
  *eisosome/EIS1 ancestry*, NOT a hydrolase fold.

## Inline domain / sequence analysis (done in-conversation, no sub-agent)

- **No recognized hydrolase/α-β-hydrolase domain.** UniProt lists exactly one domain family
  (EIS1/Eisosome1, PF12757) and no catalytic-domain features. There is no InterPro
  α/β-hydrolase, lipase, esterase, or GDSL signature on P35736.

- **Massively disordered.** UniProt annotates six MobiDB-lite disordered regions
  (1–27, 34–53, 687–730, 751–778, 791–821, 834–922) plus multiple polar / basic-acidic /
  low-complexity biased regions. Much of the 922-aa protein is predicted intrinsically
  disordered — atypical for a folded lipase.

- **GXSXG "lipase motif" search (done here on the P35736 sequence).** Exactly ONE canonical
  GXSXG nucleophile-elbow motif is present: **G875-F-S877-Q-G879 (GFSQG)**. Critically it lies
  *inside* the C-terminal disordered/low-complexity region (UniProt disorder 834–922,
  low-complexity 871–880). A catalytic GXSXG in a true lipase sits on the nucleophile elbow of
  a folded α/β-hydrolase core; a lone GXSXG buried in a disordered tail is a weak, plausibly
  coincidental match and is NOT structural evidence for a lipase active site. (A second, non-
  catalytic-context GDSK is at pos 101.) => Sequence does not independently corroborate a
  lipase fold; the lipase hypothesis rests on the Ploier/Yifrach functional data, not on domain
  architecture.

- **No obvious C-terminal PTS1.** The protein ends "...SFFKEVI" (…E-V-I). A classic PTS1 is a
  C-terminal S/A/C-K/R/H-L tripeptide (e.g. SKL); "-EVI"/"-KEVI" is not a canonical PTS1, and
  there is no annotated PTS1/PTS2 in UniProt. If LPX2 is truly a peroxisomal *matrix* protein,
  its import route (PTS1 variant, PTS2, or piggy-back) is unresolved — a real knowledge gap.

## What is NOT known (dark-gene gaps)

1. **Molecular function is unproven.** No direct, reproducible enzymatic assay on purified
   LPX2 is available to us. "Lipase" is a proposal (name + Ploier attribution + deletion
   lipidome) not an established activity. Substrate specificity is unknown (Yifrach explicitly
   frame Lpx1/Lpx2/Fsh3 as acting "on different lipid substrates" — i.e. undetermined).
2. **Domain–function conflict.** The only sequence-family signal is EIS1/eisosome ancestry,
   which has nothing to do with lipid hydrolysis; yet the experimental phenotype/localization
   point to peroxisomal lipid metabolism. Whether LPX2 retained an EIS1-like structural role,
   neofunctionalized into a lipase, or does something else entirely is unresolved.
3. **In-vivo role / phenotype.** Beyond the glucose-medium LPG lipidome shift, there is no
   growth phenotype, pathway placement, or β-oxidation contribution demonstrated for LPX2
   specifically; the "release fatty acids for β-oxidation / maintain peroxisomal membrane
   morphology" idea is a *speculative model* in Yifrach for the Lpx1/Lpx2/Fsh3 set, not an
   LPX2-specific result ["All of the above may suggest that the peroxisomal lipases Lpx1,
   Lpx2, and possibly also Fsh3, act on the peroxisomal membrane or on intraperoxisomal
   vesicles to release fatty acids for β‐oxidation and in doing so also help to maintain
   normal peroxisomal membrane morphology."].
4. **Localization determinants.** Oleate-dependent tri-compartment (peroxisome/nucleus/
   cytosol) distribution and the peroxisomal import signal are uncharacterized.
5. **Physiological relevance of AZF1 induction and SCF/Cdc4 turnover** to LPX2 function is
   unknown.

## Annotation-by-annotation plan (GOA has 3 rows)

- **GO:0005777 peroxisome, IDA, PMID:36164978** — ACCEPT (experimental IDA, curator/SGD;
  matrix localization directly supported). Could optionally note more specific
  GO:0005782 peroxisomal matrix in core_functions.
- **GO:0003674 molecular_function, ND, GO_REF:0000015** — this is a placeholder "no data" root
  annotation. Standard handling: mark as the root/ND placeholder (KEEP_AS_NON_CORE /
  note it reflects unknown MF; do not treat as core). MF genuinely unknown.
- **GO:0008150 biological_process, ND, GO_REF:0000015** — root/ND placeholder, same handling.
- **GO:0070941 eisosome assembly, IBA, GO_Central** — NOTE: this IBA is in UniProt's GO
  cross-refs (DR GO:0070941 ... IBA:GO_Central) but is NOT in the QuickGO GOA TSV we fetched
  (only the 3 rows above are). It is a phylogenetic inference propagated from the EIS1 side of
  PTHR28298. LPX2 (peroxisomal-matrix paralog of EIS1) has no experimental eisosome role and
  its localization is inconsistent with the plasma-membrane eisosome. If it appears in the
  review it should be MARK_AS_OVER_ANNOTATED (over-propagated paralog IBA), argued on
  biological grounds (allowed for electronic IBA). Since it is not in the GOA TSV, it is not a
  required row; will document in notes and knowledge_gaps rather than fabricate a GOA row.

## References worth citing
- PMID:36164978 Yifrach 2022 — peroxi-ome; naming; matrix localization; LPG lipidome. HIGH.
- PMID:24187129 Ploier 2013 — hydrolase screen; source of the "lipase activity" attribution.
  HIGH. Full text available: it DID test Ykl050cp (named among GXSXG candidates; overexpression
  proposed a TG-mobilization role) but confirmed in-vivo lipolytic activity only for Lpx1p and
  Ayr1p — all other candidates including Ykl050cp did NOT exhibit lipolytic activity in vivo. So
  this is a NEGATIVE direct result for LPX2; Yifrach 2022's "clear lipase activity" attribution
  is an overstatement, and this strengthens the MF-unknown conclusion.
- PMID:16467472 Slattery 2006 — AZF1 regulates LPX2 expression (UniProt-curated). MEDIUM.
- PMID:16338374 Tang 2005 — SCF/Cdc4 substrate screen (SGD-curated turnover). LOW/MEDIUM.
