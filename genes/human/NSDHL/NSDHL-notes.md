# NSDHL (Q15738) review notes

## Identity / function
NSDHL = NAD(P)-dependent steroid dehydrogenase-like protein; UniProt RecName
**Sterol-4-alpha-carboxylate 3-dehydrogenase, decarboxylating** (EC 1.1.1.170).
It is the C4-demethylation-complex enzyme that, after MSMO1 (sterol C4-methyl
oxidase) has oxidised a C4 methyl group to a carboxylate, catalyses the
**NAD(P)+-dependent 3-beta-hydroxysteroid dehydrogenation + decarboxylation of the
4-alpha-carboxysterol**, yielding a 3-oxo(3-keto) sterol + CO2; a 3-ketosteroid
reductase (HSD17B7) then regenerates the 3-beta-ol. Iterated twice this strips
both C4 methyls. Member of the 3-beta-HSD (SDR) family.

UniProt CATALYTIC ACTIVITY (Rhea) [file:human/NSDHL/NSDHL-uniprot.txt]:
- "a 3beta-hydroxysteroid-4alpha-carboxylate + NADP(+) = a 3-oxosteroid + CO2 + NADPH" RHEA:34771, EC 1.1.1.170
- NAD(+) variant RHEA:34775 (= GO:0102175)
- multiple specific substrates: 4alpha-carboxyzymosterol, 4beta-methylzymosterol-4alpha-carboxylate (RHEA:33447), 4alpha-carboxy-4beta-methyl-5alpha-cholest-8-en-3beta-ol, 4alpha-carboxy-5alpha-cholest-8-ene-3beta-ol
- PATHWAY: "Steroid biosynthesis; zymosterol biosynthesis; zymosterol from lanosterol: step 4/6."

## Localization
ER membrane, single-pass membrane protein; C-terminal motif (370-373) "Prevents
secretion from ER"; also lipid droplet. UniProt SUBCELLULAR LOCATION:
"Endoplasmic reticulum membrane {ECO:0000269|PubMed:21129721}; Single-pass
membrane protein. Lipid droplet {ECO:0000250|UniProtKB:Q9R1J0}." TRANSMEM 298-318.
HPA IDA (GO_REF:0000052) and LIFEdb (GO_REF:0000054) both put it at ER; PMID:21498505
& PMID:14741744 are lipid-droplet proteomics/LD studies (IDA lipid droplet).

## Catalytic residues / structure
ACT_SITE 172 (proton acceptor); BINDING 176 NAD+. Homodimer (PMID:32140747,
crystal 6JKG/6JKH with NAD). Rossmann NAD(P)-binding fold (CDD cd09813
3b-HSD-NSDHL-like_SDR).

## Disease
- CHILD syndrome (MIM 308050): X-linked dominant, male-lethal; congenital
  hemidysplasia with ichthyosiform erythroderma and limb defects. [PMID:10710235,
  PMID:11907515]
- CK syndrome (MIM 300831): X-linked recessive; intellectual disability, cortical
  malformation, microcephaly; temperature-sensitive hypomorphic alleles. [PMID:21129721]
- Mouse orthologs: bare patches (Bpa) / striated (Str) X-linked dominant male-lethal. [PMID:10369263]

## GO term adjudication highlights
- GO:0000252 (3b-HSD [NAD(P)+]/C4-decarboxylase) = CORE MF. Supported by EXP
  (PMID:10369263 Reactome), ISS from mouse Q9R1J0, IEA (ARBA/Rhea), TAS Reactome. ACCEPT.
- GO:0102175 (NAD+ variant) = accept, more specific NAD+ form of the same activity.
- GO:0016616 (oxidoreductase, CH-OH donor, NAD(P) acceptor) = correct parent, IBA+InterPro; ACCEPT (non-core, general).
- GO:0003854 (3b-hydroxy-Delta5-steroid dehydrogenase (NAD+) activity) = classic
  steroidogenic 3b-HSD reaction (pregnenolone->progesterone), NOT NSDHL's
  C4-decarboxylating reaction. Family-level over-specific/wrong-branch. Old 2003
  PINC TAS. MODIFY -> GO:0000252.
- CC ER / ER membrane / lipid droplet: all well supported, ACCEPT.
- Cholesterol biosynthetic process (GO:0006695), cholesterol metabolic process
  (GO:0008203), steroid biosynthetic process (GO:0006694): ACCEPT; GO:0006695 is the
  precise core BP.
- protein binding GO:0005515 x2 (PMID:32296183 HuRI Y2H binary; PMID:32814053 NDD
  interactome) = uninformative high-throughput IPI; MARK_AS_OVER_ANNOTATED (per policy,
  not REMOVE). Interactors ATXN1/RHBDD1/TMX2 from UniProt IntAct.

## core_functions
- MF: GO:0000252
- BP directly_involved_in: GO:0006695 cholesterol biosynthetic process
- CC located_in: GO:0005789 endoplasmic reticulum membrane
