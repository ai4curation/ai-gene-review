# HGSNAT (Q68CP4) review notes

Human HGSNAT (heparan-alpha-glucosaminide N-acetyltransferase; TMEM76). EC 2.3.1.78.
Deep research: falcon out of credits (HTTP 402); grounded in UniProt (`HGSNAT-uniprot.txt`),
GOA (`HGSNAT-goa.tsv`), and cached publications.

## Core biology
- Lysosomal **membrane** transmembrane transacetylase — unique among the four HS-degradation
  enzymes in being a membrane-bound *transferase* (the others are soluble hydrolases/sulfatases).
- Catalyzes the essential step of **heparan sulfate catabolism**: transfers an acetyl group from
  **cytosolic acetyl-CoA** onto the free amino group of the terminal non-reducing
  alpha-glucosamine of intralysosomal HS/heparin, producing N-acetyl-alpha-glucosamine so that
  NAGLU (alpha-N-acetylglucosaminidase) can then remove it. [UniProt FUNCTION;
  PMID:19823584 "which catalyses transmembrane / acetylation of the terminal glucosamine residues
  of heparan sulfate prior to / their hydrolysis by alpha-N-acetylglucosaminidase"]
- Reaction: alpha-D-glucosaminyl-[heparan sulfate](n) + acetyl-CoA = N-acetyl-alpha-D-glucosaminyl-[heparan
  sulfate](n) + CoA + H+ (RHEA:15125; EC 2.3.1.78). GO:0015019 is the exact-match MF term.
- Membrane topology: 11 TM helices (polytopic / multi-pass); N-terminal luminal domain,
  active-site His297 (UniProt ACT_SITE; PMID:20650889 proposes His that accesses cytoplasmic
  acetyl-CoA). Signal sequence present but not cleaved; targeted to lysosome via
  AP-mediated tyrosine/dileucine motifs in C-terminal cytoplasmic tail.
- Homooligomer (~440 kDa); homooligomerization required for activity; precursor (77 kDa)
  cleaved intralysosomally into 29-kDa alpha and 48-kDa beta chains — cleavage essential for
  activation [PMID:20650889].

## Localization
- Lysosome membrane, multi-pass (UniProt; PMID:16960811, 17033958, 17897319).
- Confirmed by IDA immunofluorescence colocalization with LAMP-2 (PMID:19823584, 20650889),
  HDA lysosomal-membrane proteomics (PMID:17897319), and multiple Reactome TAS.
- Reactome also places HGSNAT in neutrophil specific/tertiary granule membranes and plasma
  membrane (neutrophil degranulation, R-HSA-6798695). These are secretory-pathway/degranulation
  contexts, not the core lysosomal catabolic function; kept as non-core.

## Disease
- MPS IIIC / Sanfilippo syndrome C (MIM 252930): autosomal recessive lysosomal storage disease;
  HS accumulation; severe CNS neurodegeneration. Most missense mutations cause misfolding/ER
  retention (PMID:19823584).
- Retinitis pigmentosa 73 (RP73, MIM 616544) — non-syndromic (PMID:25859010).

## GOA MF term used for core_functions
GO:0015019 "heparan-alpha-glucosaminide N-acetyltransferase activity" (exact GOA term; current,
non-obsolete; = EC 2.3.1.78 / RHEA:15125). BP core = GO:0030200 "heparan sulfate proteoglycan
catabolic process". CC = GO:0005765 "lysosomal membrane".

## Annotation decisions (summary)
- GO:0015019 MF (IBA, IEA, 2x TAS Reactome): ACCEPT — core catalytic function, exact-match term.
- GO:0030200 BP (IBA, IEA): ACCEPT — core catabolic pathway.
- GO:0005765 lysosomal membrane (IBA is_active_in, IEA, TAS x3, HDA, IDA x2): ACCEPT — core location.
- GO:0016746 acyltransferase activity (IDA x2): MODIFY -> GO:0015019 (parent of the specific MF; the
  IDA measured N-acetyltransferase activity, so the specific term is warranted).
- GO:0007041 lysosomal transport (IDA, PMID:20650889): MARK_AS_OVER_ANNOTATED — the paper studies
  biogenesis/AP-mediated *targeting* of HGSNAT to lysosomes, not HGSNAT acting as a transporter in
  the "lysosomal transport" (cargo transport) sense; over-annotation of the trafficking observation.
- GO:0051259 protein complex oligomerization (IDA, PMID:20650889): KEEP_AS_NON_CORE — real
  (homooligomerization required for activity) but a biogenesis/assembly process, not the core MF/BP.
- GO:0005886 plasma membrane (TAS Reactome x2): KEEP_AS_NON_CORE — neutrophil-degranulation
  exocytosis context, not the core lysosomal location.
- GO:0035579 specific granule membrane / GO:0070821 tertiary granule membrane (TAS Reactome):
  KEEP_AS_NON_CORE — neutrophil granule contexts (degranulation pathway).
