# FASN (Fatty acid synthase) — review notes

UniProt: P49327 (FAS_HUMAN). HGNC:3594. Gene on chromosome 17. 2511 aa. Ubiquitous
expression, prominent in brain, lung, liver, mammary gland, adipose. Evidence at
protein level (PE 1). All provenance below is grounded in the local UniProt record
(`file:human/FASN/FASN-uniprot.txt`), the GOA TSV, and cached `publications/PMID_*.md`.

## Identity and overall function

FASN is the mammalian (metazoan) cytosolic **type I fatty acid synthase**, a large
multifunctional homodimeric "megasynthase" (~273 kDa per protomer) that carries out
the entire cycle of **de novo long-chain saturated fatty acid biosynthesis**, producing
mainly **palmitate (C16:0)** from acetyl-CoA and malonyl-CoA using NADPH.

- UniProt FUNCTION: "Fatty acid synthetase is a multifunctional enzyme that catalyzes
  the de novo biosynthesis of long-chain saturated fatty acids starting from acetyl-CoA
  and malonyl-CoA in the presence of NADPH. This multifunctional protein contains 7
  catalytic activities and a site for the binding of the prosthetic group
  4'-phosphopantetheine of the acyl carrier protein ([ACP]) domain."
  [file:human/FASN/FASN-uniprot.txt, ECO:0000269 from PubMed:16215233, 16969344, 26851298, 7567999, 8962082, 9356448].
- Overall reaction (EC 2.3.1.85): "acetyl-CoA + n malonyl-CoA + 2n NADPH + 2n H(+) =
  a long-chain fatty acid + (n+1) CoA + n CO2 + 2n NADP(+)."
  [file:human/FASN/FASN-uniprot.txt].
- Pathway: "Lipid metabolism; fatty acid biosynthesis." [file:human/FASN/FASN-uniprot.txt].

## Seven catalytic activities + ACP (all recombinantly demonstrated in the human enzyme)

The full-length MBP-hFAS "catalyzed palmitate synthesis from acetyl-CoA, malonyl-CoA,
and NADPH and exhibited all of the partial activities of FAS at levels comparable with
those of the native human enzyme purified from HepG2 cells... the products of MBP-hFAS
are mainly palmitic acid (> 90%)" [PMID:8962082 "catalyzed palmitate synthesis from
acetyl-CoA, malonyl-CoA, and NADPH and exhibited all of the partial activities of FAS"].
Domain I (KS + acetyl/malonyl transacylases + beta-hydroxyacyl dehydratase) and domains
II+III (enoyl and beta-ketoacyl reductases, ACP, thioesterase) were dissected and shown
to carry their respective partial activities [PMID:8962082].

Component activities / EC numbers (all ECO:0000269 in UniProt from PubMed:7567999,
8962082, 9356448; several also 26851298):
- [ACP] S-acetyltransferase — GO:0004313 — EC 2.3.1.38 (MAT, bifunctional)
- [ACP] S-malonyltransferase — GO:0004314 — EC 2.3.1.39 (MAT, bifunctional)
- 3-oxoacyl-[ACP] synthase (condensing / beta-ketoacyl synthase, KS) — GO:0004315 — EC 2.3.1.41
- 3-oxoacyl-[ACP] reductase (NADPH) (beta-ketoacyl reductase, KR) — GO:0004316 — EC 1.1.1.100
- (3R)-hydroxyacyl-[ACP] dehydratase (DH) — GO:0019171 — EC 4.2.1.59
- enoyl-[ACP] reductase (NADPH) (ER) — GO:0141148 — EC 1.3.1.39
- fatty acyl-[ACP] hydrolase / thioesterase (TE) — GO:0016297 — EC 3.1.2.14
- ACP domain carries the 4'-phosphopantetheine prosthetic group (phosphopantetheinylation
  at Ser-2156) [file:human/FASN/FASN-uniprot.txt, PubMed:7567999].

Note GOA has specific EXP/IDA annotations (PMID:26851298, PMID:8962082) for GO:0004316,
GO:0004313, GO:0004315, GO:0019171, GO:0141148 — i.e. individual partial reactions were
directly assayed on the human enzyme.

## Domain architecture (UniProt feature table + structural papers)

Domain order N→C: KS (1-406) — MAT/acyl+malonyl transferase region (429-817) — DH
(PKS/mFAS DH, 838-1108; N- and C-terminal hotdog folds) — ER (1635-1863) — KR
(beta-ketoacyl reductase, 1864-2118) — ACP/Carrier (2121-2198) — TE thioesterase
(2207-2511) [file:human/FASN/FASN-uniprot.txt]. Cryo-EM/structure papers describe an
X-shaped/pseudo-symmetric homodimer with a condensing region (KS, LD, MAT) and a
modifying region (DH, ΨME, ΨKR, ER, KR, ACP, TE), plus catalytically dead pseudo-domains
(ΨKR, ΨME) [PMID:37308485 "the modifying region—dehydratase (DH), pseudo-methyltransferase
(ΨME), pseudo-ketoacyl reductase (ΨKR), enoyl reductase (ER), ketoacyl reductase (KR),
acyl carrier protein (ACP), and thioesterase (TE) domains"]. Active sites: KS Cys-161,
His-293, His-331; malonyltransferase Ser-581; DH His-878/His-1031; TE Ser-2308/His-2481
[file:human/FASN/FASN-uniprot.txt].

## ACP shuttling mechanism (Nature 2025)

"In mammals, a single gene encodes six catalytically active domains and a flexibly
tethered acyl carrier protein (ACP) domain that shuttles intermediates between active
sites for fatty acid biosynthesis" [PMID:39979457]. "FASN is the primary enzyme in DNL
that condenses cytosolic acetyl-CoA and malonyl-CoA into the 16-carbon saturated fatty
acid palmitate" [PMID:39979457 "FASN is the primary enzyme in DNL that condenses cytosolic
acetyl-CoA and malonyl-CoA into the 16-carbon saturated fatty acid palmitate"]. Both human
and mouse FASN "formed stable homodimers in solution." Ppant arm on Ser-2156 of the ACP
traced to catalytic His-878 of the DH domain; ACP-DH and ACP-ER interface mutations reduce
both in vitro activity and cellular de novo lipogenesis (palmitate ^13C labeling) — this is
the ComplexPortal IPI basis for GO:0005835 (fatty acid synthase complex) and the NAS
GO:0046949 (fatty-acyl-CoA biosynthetic process) [PMID:39979457].

## Subunit / complex / regulation

- SUBUNIT: "Homodimer which is arranged in a head to tail fashion" [file:human/FASN/FASN-uniprot.txt,
  PubMed:17618296, 18022563]. Interacts with CEACAM1 (insulin/phosphorylation-dependent;
  reduces FAS activity). ComplexPortal CPX-26624 "Fatty acid synthase complex" (homodimer).
- ACTIVITY REGULATION: activated by S-nitrosylation which promotes dimerization
  (Cys-1471, Cys-2091); inhibited by cerulenin (covalent, condensing enzyme) and orlistat
  (thioesterase) [file:human/FASN/FASN-uniprot.txt; PMID:26851298 "S-nitrosylation of FAS
  at Cys(1471)and Cys(2091)... increased its enzymatic activity"]. Key lipogenic enzyme in
  adipocytes; S-nitrosylation increases during adipogenesis [PMID:26851298 "FAS, a key
  lipogenic enzyme in adipocytes"].
- ACP holo-enzyme formation: AASDHPPT (human holo-ACP synthase / PPTase) attaches the
  phosphopantetheine to the ACP domain; structure of ACP domain (2119-2207) in complex with
  AASDHPPT and CoA [file:human/FASN/FASN-uniprot.txt, PubMed:18022563]. This is the basis of
  the IPI protein-binding annotation to Q9NRN7 (AASDHPPT) — a functional, mechanistically
  meaningful interaction, not a generic one.

## Localization

- Cytoplasm / cytosol is the primary site [file:human/FASN/FASN-uniprot.txt SUBCELLULAR
  LOCATION "Cytoplasm"; HPA IDA GO:0005829; PMID:17081065]. Also detected in melanosome
  fractions by MS [file:human/FASN/FASN-uniprot.txt "Melanosome"; PMID:17081065].
- Many "membrane", "plasma membrane", "extracellular exosome" annotations are from large
  proteomic surveys (HDA / high-throughput IDA); FASN is a soluble cytosolic enzyme, so
  these are contaminant/secondary localizations best kept non-core.

## Context / disease roles (non-core)

- **Antiviral / proviral (host factor):** FASN activity required for SARS-CoV-2 replication;
  FASN knockout impairs replication, rescued by fatty-acid supplementation [PMID:34320401
  "FASN knockout results in significantly impaired SARS-CoV-2 replication that can be rescued
  with fatty acid supplementation"]. GOA term GO:0044788 "host-mediated perturbation of viral
  process" IDA is the "microbial infection" FUNCTION line in UniProt. Also HCV NS5B interaction
  [PMID:23427160].
- **Immunometabolism:** FAMIN (LACC1, Q8IV20) "formed a complex with fatty acid synthase (FASN)
  on peroxisomes and promoted flux through de novo lipogenesis" [PMID:27478939 "FAMIN formed a
  complex with fatty acid synthase (FASN) on peroxisomes and promoted flux through de novo
  lipogenesis"].
- **Cancer:** FASN is overexpressed in many solid tumors (breast, prostate, liver, lung); drug
  target (denifanstat/TVB-2640, orlistat, cerulenin) [PMID:37308485].

## Protein-interaction (IPI/HDA) annotations — mostly generic "protein binding"

GOA lists several GO:0005515 IPI interactions: AASDHPPT/Q9NRN7 (functional; PPTase),
LACC1/FAMIN (Q8IV20; peroxisomal DNL complex), HTT (P42858), ADIPOQ (Q15848), LNX1 (Q8TBB1),
HIF1A (Q16665), HCV NS5B (Q99IB8), plus cadherin binding (GO:0045296, HDA, E-cadherin
interactome PMID:25468996) and RNA binding (GO:0003723, HDA, mRNA-interactome captures
PMID:22658674, 22681889). Per policy, IPI "protein binding" is kept but marked over-annotated
(uninformative); the AASDHPPT and LACC1 interactions are the most biologically meaningful.
identical protein binding (GO:0042802) reflects the well-established homodimer.

## Curation summary

Core = the overall fatty acid synthase activity (GO:0004312, MF) plus its component partial
activities (GO:0004313, GO:0004314, GO:0004315, GO:0004316, GO:0019171, GO:0141148, GO:0016297),
the fatty acid biosynthetic process (GO:0006633, BP), cytosol location (GO:0005829, CC), and the
homodimeric fatty acid synthase complex (GO:0005835). Peripheral/context terms (viral, osteoblast
differentiation, exosome/membrane/plasma-membrane locations, RNA/cadherin/protein binding,
response-to-nutrient, ether-lipid, generic transferase/oxidoreductase parent terms) are kept
non-core or flagged as over-annotations. No experimental annotation is removed; a few clearly
non-FASN or root-parent IEA terms are handled per policy.
