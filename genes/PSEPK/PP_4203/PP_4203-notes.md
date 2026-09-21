# PP_4203 (Q88F95) curation notes — PSEPK ETF:quinone oxidoreductase

## Identity

- UniProt Q88F95, locus PP_4203, 560 aa, *Pseudomonas putida* KT2440
  (NCBITaxon:160488).
- Electron transfer flavoprotein-ubiquinone oxidoreductase, EC 1.5.5.1.
  The local record gives the reaction explicitly
  [file:PSEPK/PP_4203/PP_4203-uniprot.txt "Reaction=a ubiquinone + reduced
  [electron-transfer flavoprotein] = a ubiquinol + oxidized [electron-transfer
  flavoprotein] + H(+)"; Rhea:RHEA:24052] and the one-line function
  ["Accepts electrons from ETF and reduces ubiquinone."].
- Two cofactors, both from RuleBase RU366068:
  ["Name=FAD; Xref=ChEBI:CHEBI:57692;"] and
  ["Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;" / "Note=Binds 1 [4Fe-4S]
  cluster."].
- Encoded immediately downstream of the ETF pair etfA (PP_4201) and etfB
  (PP_4202), i.e. the canonical *etfA-etfB-etfQO* arrangement.

## Curation decisions and why

### GO:0050660 flavin adenine dinucleotide binding — added as NEW

GOA has the [4Fe-4S] cofactor (GO:0051539, GO_REF:0000104, UniRule
UR001252760) but not the FAD, even though the UniProt record asserts both from
the same rule. The omission matters because the flavin is the catalytically
decisive centre: in the pig-liver structure the UQ-flavin distance is shorter
than the UQ-cluster distance and the redox potentials are similar, so
[PMID:17050691 "the very similar redox potentials of FAD and the cluster
strongly suggest that the flavin, not the cluster, transfers electrons to UQ"].
The stoichiometry is conserved to the bacteria: human, porcine and
*Rhodobacter sphaeroides* ETF-QO
[PMID:18037314 "sphaeroides ETF-QO each contain a single [4Fe-4S](2+,1+)
cluster and one equivalent of FAD"]. The paralogous alpha subunit etfA already
carries GO:0050660 in GOA, so this is a gap in the electronic annotation of
PP_4203, not a new biological claim.

Note this is deliberately *not* filed under `proposed_new_terms`: GO:0050660
already exists, so the right mechanism is an `existing_annotations` entry with
`action: NEW`, not a request for a new ontology term.

### GO:0005737 cytoplasm — MODIFY to GO:0005886 plasma membrane

ETF-QO reduces a membrane-embedded quinone, so a soluble cytoplasmic
assignment misplaces the activity rather than merely under-specifying it. The
pig-liver crystal structure establishes that
[PMID:17050691 "is a monotopic integral membrane protein"], with a
membrane-binding surface forming a hydrophobic plateau, and the enzyme is
described as a [PMID:18037314 "membrane-bound electron transfer protein that
links primary flavoprotein dehydrogenases with the main respiratory chain"]
across human, porcine and *R. sphaeroides* forms — the last of which is
bacterial, which is what licenses the transfer to a *Pseudomonas* protein.
GO:0005886 carries "cytoplasmic membrane" and "bacterial inner membrane" as
exact synonyms (OLS), so it is the correct bacterial target.

MODIFY rather than MARK_AS_OVER_ANNOTATED, so the gene retains a
cellular-component term instead of being left with none.

**Caveat recorded as a knowledge gap on the annotation.** PP_4203's UniProt
record has no SUBCELLULAR LOCATION line and no Membrane keyword, and the
OpenScientist report is explicit that
[file:PSEPK/PP_4203/PP_4203-deep-research-openscientist.md "there is no direct
topological/proteomic membrane-localization datum for PP_4203"]. The
localization is inferred from the orthologs and from the substrate, not
measured.

### Upstream donors are identifiable, contra the first draft

The original `description` said the record "does not identify the upstream
substrate dehydrogenases". That was wrong once the deep research was added, and
is now corrected. Because ETF can only be reoxidised by ETF-QO, PP_4203 is the
single obligatory return path for electrons from the organism's flavoprotein
dehydrogenases — chiefly the acyl-CoA dehydrogenases of fatty-acid
beta-oxidation and of branched-chain amino-acid/isovalerate catabolism.

## Reference verification (PubMed esummary, 2026-09-21)

The OpenScientist report cites nine PMIDs, five of which are not in
`publications/`. Checked the three load-bearing uncached ones against PubMed
directly:

| PMID | Verified as | Used here? |
|---|---|---|
| 24794972 | "Identification and characterization of an acyl-CoA dehydrogenase from Pseudomonas putida KT2440…", Microbiology (Reading) 2014 | Not cited (not cached); the 21-ACAD claim is reported in the research file only |
| 20937244 | "The electron transfer flavoprotein: ubiquinone oxidoreductases", Biochim Biophys Acta 2010 | Not cited (not cached) |
| 42239388 | "Exercise based Intervention For Metabolic Inflexibility Linked With Lipid Storage Myopathy Using Innovative CRISPR Etf-QO Mutant Knock-in Models", **bioRxiv preprint**, 2026-05-20 | **Deliberately not cited** |

PMID:42239388 resolves to a real record but it is an unreviewed 2026 bioRxiv
preprint, and the research file leans on it for a headline statement of ETF-QO's
core function. That claim is fully covered by the peer-reviewed PMID:17050691
and PMID:20937244, so nothing is lost by declining to cite the preprint.

Also note **PMID:18625020 is *Pseudomonas aeruginosa*, not *P. putida***
(cached title: "Biochemical characterization of isovaleryl-CoA dehydrogenase
(LiuA) of Pseudomonas aeruginosa…"). The research file uses it as a
*Pseudomonas* donor example; it is a reasonable genus-level illustration but is
not a KT2440 result, and it is not cited in the review YAML for that reason.

## Open questions

- Direct confirmation of cytoplasmic-membrane association and monotopic
  topology for Q88F95 (fractionation + immunoblot, or fluorescent fusion).
- Which of KT2440's acyl-CoA dehydrogenases dominate flux through PP_4203 in
  vivo, and whether the PP_0312/PP_0313 pair also feeds this same ETF-QO or
  requires a different quinone-reducing partner.
