# DEGS1 (O15121) — curation notes

## Identity
- HGNC:13709; DEGS1 / DES1 / MLD / MIG15; "Sphingolipid delta(4)-desaturase DES1".
- 323 aa, ER multi-pass membrane protein; fatty acid desaturase type 1 family, DEGS subfamily.
- Three conserved histidine boxes (His box-1 89–93, box-2 128–132, box-3 259–263); di-iron center;
  cytochrome b5 / NAD(P)H electron-transfer coupled.

## Core function (well established)
- Catalyzes the FINAL step of de novo ceramide biosynthesis: introduces a 4,5-trans double bond into
  dihydroceramide (an N-acylsphinganine) to form ceramide (an N-acylsphing-4-enine).
  EC 1.14.19.17; Rhea:46544; O2- and Fe(II)-[cytochrome b5]-dependent.
- GO MF present in GOA and used for core_functions: GO:0042284 sphingolipid delta-4 desaturase activity
  (def matches UniProt catalytic activity / Rhea:46544). This is the exact current GOA MF term.
- BP: ceramide biosynthetic process (GO:0046513); sphingolipid biosynthetic process (GO:0030148).
- CC: endoplasmic reticulum membrane (GO:0005789), cytoplasmic (cytosolic) face; multi-pass.

## Key supporting evidence (verbatim-quotable)
- PMID:11937514 (Ternes 2002) — identified/characterized the human sphingolipid Δ4-desaturase
  (dihydroceramide desaturase); UniProt uses it for EC 1.14.19.17 catalytic activity.
- PMID:30620337 (Pant 2019, full text available) — "This enzyme catalyzes the insertion of a Δ4,5-
  trans double bond into dihydroceramide (DhCer) to convert it to ceramide (Cer), in the final step of
  the de novo Cer biosynthesis pathway"; "endoplasmic reticulum lipid desaturase DEGS1"; loss causes
  hypomyelinating leukodystrophy (HLD18); myelin development/maintenance role.
- PMID:30620338 (Karsai 2019) — "DEGS1, which catalyzes the last step in the ceramide synthesis
  pathway"; A280V patient variant reduces enzyme activity ~80%; increase in dihydro sphingolipid
  species; HLD18. IMP evidence for GO:0042284 and IMP for myelin maintenance.
- Reactome R-HSA-428259 "DEGS1 dehydrogenates dihydroceramide" — cytosolic face of ER; part of an
  enzyme complex with cytochrome b5 (Fe2+) refreshed by NADH.

## Secondary / moonlighting
- Retinol isomerase (isomerase-2) activity in retinal Müller cells (PMID:23143414; EC 5.2.1.-;
  GO:0050251 retinol isomerase activity, IDA). Genuine second activity but distinct from core de novo
  ceramide role; keep as non-core.
- Myristoylation (Gly-2) can retarget part of the enzyme to mitochondria and raise ceramide/apoptosis
  (PMID:19647031). Explains the mitochondrion / mitochondrial membrane localizations (secondary).

## Localization notes
- ER membrane is the primary/functional site (multiple EXP: PMID:9188692, 19647031, 30620338;
  Reactome; UniProt SubCell). GO:0098554 cytoplasmic side of ER membrane (IDA) is the specific
  is_active_in term — strongest CC.
- Mitochondrion / mitochondrial membrane (EXP PMID:19647031, 30620338; HPA IDA) — real but secondary,
  myristoylation-dependent; keep as non-core.
- PMID:1317856 is about serine palmitoyltransferase / 3-dehydrosphinganine reductase / sphinganine
  N-acyltransferase (upstream ceramide-synthesis enzymes) in mouse liver ER, establishing the cytosolic
  orientation of de novo sphingolipid-synthesis enzymes at the ER. Used as GO_REF source for
  DEGS1 ceramide-biosynthesis + cytosolic ER-face annotations by the curator (UOS_MCB). Abstract-only
  in cache; do not overrule the experimental curator — ACCEPT.
- Plasma membrane / specific granule membrane (Reactome R-HSA-6799350, neutrophil degranulation) —
  over-annotation from bulk granule proteomics; not a functional DEGS1 site. MARK_AS_OVER_ANNOTATED.

## Interactions
- PMID:32296183 (HuRI) — bare protein_binding IPIs with ARLN (Q8WVX3-2) and SEMA4G (Q9NTN9-2),
  high-throughput binary interactome; uninformative for MF. Per policy: MARK_AS_OVER_ANNOTATED
  (not REMOVE) for bare protein binding IPI.

## Other GOA terms adjudicated
- GO:0009055 electron transfer activity (TAS PMID:9188692) — DEGS1 receives electrons from cyt b5;
  it is the desaturase acceptor, not itself an electron-transfer carrier. Over-annotation / better
  captured by the desaturase MF. MARK_AS_OVER_ANNOTATED.
- GO:0006636 unsaturated fatty acid biosynthetic process (TAS PMID:9188692) — DEGS1 desaturates the
  sphingoid base of a ceramide, not free fatty acids; the sphingolipid/ceramide BP terms are correct.
  MARK_AS_OVER_ANNOTATED.
- GO:0006686 sphingomyelin / GO:0006688 glycosphingolipid biosynthetic process (IDA, UOS_MCB) —
  downstream complex-sphingolipid processes DEGS1 feeds via ceramide; defer to experimental curator
  but non-core. KEEP_AS_NON_CORE.
- GO:0006629 lipid metabolic process, GO:0016020 membrane, GO:0003824 catalytic activity — correct but
  generic IEA parents of more specific accepted terms. MARK_AS_OVER_ANNOTATED (too general).
</content>
</invoke>
