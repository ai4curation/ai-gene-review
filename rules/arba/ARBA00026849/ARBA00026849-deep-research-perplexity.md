---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-25T19:22:57.798360'
end_time: '2025-11-25T19:27:48.055953'
duration_seconds: 290.26
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00026849
  rule_type: arba
  go_terms: GO:0016810 (hydrolase activity, acting on carbon-nitrogen (but not peptide)
    bonds)
  conditions_summary: '**Condition Set 1:** InterPro id: Adenosine deaminase domain
    (InterPro:IPR001365) AND InterPro id: Adenosine/adenine deaminase (InterPro:IPR006330)
    AND InterPro id: Adenosine/AMP deaminase active site (InterPro:IPR006650)


    **Condition Set 2:** InterPro id: Carbon-nitrogen hydrolase (InterPro:IPR003010)
    AND InterPro id: Carbon-nitrogen hydrolase superfamily (InterPro:IPR036526) AND
    taxon: Viridiplantae (NCBITaxon:33090)


    **Condition Set 3:** InterPro id: Cytidine deaminase-like (InterPro:IPR016193)
    AND taxon: Saccharomycotina (NCBITaxon:147537)


    **Condition Set 4:** InterPro id: Asparaginase/glutaminase-like (InterPro:IPR006034)
    AND InterPro id: Asparaginase/glutaminase, active site 1 (InterPro:IPR020827)
    AND InterPro id: L-asparaginase, C-terminal (InterPro:IPR027473)


    **Condition Set 5:** InterPro id: Nitrilase/cyanide hydratase, conserved site
    (InterPro:IPR000132) AND InterPro id: Nitrilase/Cyanide hydratase (InterPro:IPR044149)


    **Condition Set 6:** InterPro id: GTP cyclohydrolase I (InterPro:IPR001474) AND
    InterPro id: GTP cyclohydrolase I, conserved site (InterPro:IPR018234) AND taxon:
    Metazoa (NCBITaxon:33208)


    **Condition Set 7:** InterPro id: Cytidine and deoxycytidylate deaminase domain
    (InterPro:IPR002125) AND InterPro id: APOBEC/CMP deaminase, zinc-binding (InterPro:IPR016192)
    AND taxon: Fungi (NCBITaxon:4751)


    **Condition Set 8:** InterPro id: Peptidase M20 (InterPro:IPR002933) AND InterPro
    id: Amidase, carbamoylase-type (InterPro:IPR010158) AND PANTHER id: PTHR32494:SF19


    **Condition Set 9:** InterPro id: Ureohydrolase (InterPro:IPR006035) AND InterPro
    id: Ureohydrolase domain superfamily (InterPro:IPR023696) AND taxon: Bacteria
    (NCBITaxon:2)


    **Condition Set 10:** InterPro id: Biotinidase-like, eukaryotic (InterPro:IPR012101)
    AND InterPro id: Biotinidase/VNN family (InterPro:IPR040154) AND InterPro id:
    Vanin, C-terminal (InterPro:IPR043957)


    **Condition Set 11:** InterPro id: Cytidine and Deoxycytidylate Deaminase (InterPro:IPR050202)
    AND PANTHER id: PTHR11644:SF2


    **Condition Set 12:** PANTHER id: PTHR43114:SF6


    **Condition Set 13:** InterPro id: Peptidase T2, asparaginase 2 (InterPro:IPR000246)
    AND InterPro id: Nucleophile aminohydrolases, N-terminal (InterPro:IPR029055)
    AND PANTHER id: PTHR10188:SF6


    **Condition Set 14:** InterPro id: Beta-lactamase, class-B, conserved site (InterPro:IPR001018)
    AND InterPro id: Metallo-beta-lactamase (InterPro:IPR001279) AND taxon: Pseudomonadati
    (NCBITaxon:3379134)


    **Condition Set 15:** InterPro id: NodB homology domain (InterPro:IPR002509) AND
    InterPro id: Polysaccharide deacetylase, ArnD subfamily (InterPro:IPR050248) AND
    taxon: Eukaryota (NCBITaxon:2759)


    **Condition Set 16:** InterPro id: UDP-3-O-acyl N-acetylglucosamine deacetylase
    (InterPro:IPR004463) AND InterPro id: UDP-3-O-acyl N-acetylglucosamine deacetylase,
    C-terminal (InterPro:IPR011334) AND taxon: Streptophyta (NCBITaxon:35493)


    **Condition Set 17:** InterPro id: Amidohydrolase-related (InterPro:IPR006680)
    AND InterPro id: Metal-dependent hydrolase, composite domain superfamily (InterPro:IPR011059)
    AND InterPro id: Deaminase MtaD/DadD (InterPro:IPR023512)


    **Condition Set 18:** InterPro id: Kynurenine formamidase/cyclase-like (InterPro:IPR007325)
    AND InterPro id: Kynurenine formamidase, bacteria (InterPro:IPR017484) AND InterPro
    id: Kynurenine formamidase superfamily (InterPro:IPR037175)


    **Condition Set 19:** InterPro id: Arginase (InterPro:IPR014033) AND InterPro
    id: Ureohydrolase, manganese-binding site (InterPro:IPR020855) AND PANTHER id:
    PTHR43782:SF3


    **Condition Set 20:** InterPro id: Amidase, conserved site (InterPro:IPR020556)
    AND InterPro id: Amidase signature domain (InterPro:IPR023631) AND taxon: Tracheophyta
    (NCBITaxon:58023)


    **Condition Set 21:** InterPro id: Agmatinase-related (InterPro:IPR005925) AND
    PANTHER id: PTHR11358:SF26


    **Condition Set 22:** InterPro id: AMP deaminase (InterPro:IPR006329) AND taxon:
    Glires (NCBITaxon:314147)


    **Condition Set 23:** InterPro id: Peptide deformylase (InterPro:IPR023635) AND
    InterPro id: Peptide deformylase superfamily (InterPro:IPR036821)


    **Condition Set 24:** InterPro id: Aliphatic Amidase/Beta-Ureidopropionase (InterPro:IPR050345)
    AND PANTHER id: PTHR43674:SF2


    **Condition Set 25:** FunFam id: GTP cyclohydrolase 1 (CATH.FunFam:1.10.286.10:FF:000003)
    AND FunFam id: GTP cyclohydrolase 1 (CATH.FunFam:3.30.1130.10:FF:000012) AND taxon:
    Metazoa (NCBITaxon:33208)


    **Condition Set 26:** FunFam id: biotinidase isoform X1 (CATH.FunFam:3.60.110.10:FF:000001)
    AND taxon: Eukaryota (NCBITaxon:2759)


    **Condition Set 27:** FunFam id: Bifunctional nitrilase/nitrile hydratase NIT4B
    (CATH.FunFam:3.60.110.10:FF:000006) AND taxon: Viridiplantae (NCBITaxon:33090)


    **Condition Set 28:** FunFam id: L-asparaginase 2 (CATH.FunFam:3.40.50.1170:FF:000001)


    **Condition Set 29:** FunFam id: Allantoate amidohydrolase (CATH.FunFam:3.40.630.10:FF:000044)


    **Condition Set 30:** FunFam id: Probable UDP-3-O-acyl-N-acetylglucosamine deacetylase
    3, mitochondrial (CATH.FunFam:3.30.1700.10:FF:000002) AND FunFam id: Probable
    UDP-3-O-acyl-N-acetylglucosamine deacetylase 2, mitochondrial (CATH.FunFam:3.30.230.20:FF:000002)
    AND taxon: Streptophyta (NCBITaxon:35493)


    **Condition Set 31:** FunFam id: Kynurenine formamidase (CATH.FunFam:3.50.30.50:FF:000001)
    AND taxon: Bacteria (NCBITaxon:2)


    **Condition Set 32:** FunFam id: AMP deaminase (CATH.FunFam:4.10.800.20:FF:000001)
    AND taxon: Glires (NCBITaxon:314147)


    **Condition Set 33:** FunFam id: 5-methylthioadenosine/S-adenosylhomocysteine
    deaminase (CATH.FunFam:3.20.20.140:FF:000014)


    **Condition Set 34:** FunFam id: Bifunctional purine biosynthesis protein PURH
    (CATH.FunFam:1.10.287.440:FF:000001) AND FunFam id: Bifunctional purine biosynthesis
    protein (CATH.FunFam:3.40.140.20:FF:000003) AND taxon: Dikarya (NCBITaxon:451864)


    **Condition Set 35:** FunFam id: Protein-arginine deiminase type-2 (CATH.FunFam:2.60.40.1700:FF:000001)
    AND FunFam id: Protein-arginine deiminase type-2 (CATH.FunFam:3.75.10.10:FF:000003)
    AND taxon: Rattus (NCBITaxon:10114)


    **Condition Set 36:** FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:3.30.1490.20:FF:000001)
    AND FunFam id: CAD protein-like isoform X1 (CATH.FunFam:3.40.50.1370:FF:000005)
    AND FunFam id: Carbamoyl-phosphate synthase 1, mitochondrial (CATH.FunFam:3.40.50.880:FF:000006)


    **Condition Set 37:** FunFam id: Adenosine deaminase RNA-specific B2 (inactive)
    (CATH.FunFam:3.30.160.20:FF:000009) AND FunFam id: double-stranded RNA-specific
    editase 1 isoform X1 (CATH.FunFam:3.30.160.20:FF:000011) AND taxon: Chordata (NCBITaxon:7711)


    **Condition Set 38:** FunFam id: N-acylsphingosine amidohydrolase 2 (CATH.FunFam:2.60.40.2300:FF:000001)
    AND taxon: Craniata (NCBITaxon:89593)


    **Condition Set 39:** FunFam id: Adenosine deaminase (CATH.FunFam:3.20.20.140:FF:000038)
    AND taxon: Vertebrata (NCBITaxon:7742)


    **Condition Set 40:** FunFam id: bifunctional heparan sulfate N-deacetylase/N-sulfotransferase
    1 (CATH.FunFam:3.40.50.300:FF:000176) AND taxon: Mus (NCBITaxon:862507)


    **Condition Set 41:** FunFam id: Arginase 1, mitochondrial (CATH.FunFam:3.40.800.10:FF:000007)
    AND taxon: Embryophyta (NCBITaxon:3193)


    **Condition Set 42:** FunFam id: Dihydropyrimidinase like 3 (CATH.FunFam:3.20.20.140:FF:000001)


    **Condition Set 43:** FunFam id: Cytidine deaminase (CATH.FunFam:3.40.140.10:FF:000008)


    **Condition Set 44:** FunFam id: Aminoacylase-1, putative (CATH.FunFam:1.10.150.900:FF:000001)
    AND FunFam id: Putative Aminoacylase-1 (CATH.FunFam:3.30.70.360:FF:000005) AND
    FunFam id: Aminoacylase 1 (CATH.FunFam:3.40.630.10:FF:000019)


    **Condition Set 45:** FunFam id: Putative formate--tetrahydrofolate ligase (CATH.FunFam:3.10.410.10:FF:000001)
    AND FunFam id: C-1-tetrahydrofolate synthase, cytoplasmic, putative (CATH.FunFam:3.40.50.10860:FF:000005)
    AND taxon: Ascomycota (NCBITaxon:4890)


    **Condition Set 46:** FunFam id: NAD-dependent protein deacetylase sirtuin-1 (CATH.FunFam:3.30.1600.10:FF:000013)
    AND FunFam id: NAD-dependent deacetylase sirtuin-2 (CATH.FunFam:3.40.50.1220:FF:000005)
    AND taxon: Euteleostomi (NCBITaxon:117571)


    **Condition Set 47:** FunFam id: Jasmonate-regulated gene 21 (CATH.FunFam:2.60.120.330:FF:000008)
    AND taxon: Tracheophyta (NCBITaxon:58023)


    **Condition Set 48:** FunFam id: Apolipoprotein B editing enzyme catalytic polypeptide-like
    3H (CATH.FunFam:3.40.140.10:FF:000047) AND taxon: Primates (NCBITaxon:9443)


    **Condition Set 49:** FunFam id: Protein-arginine deiminase type-4 (CATH.FunFam:2.60.40.1860:FF:000003)


    **Condition Set 50:** FunFam id: N-acetylglucosamine-6-phosphate deacetylase (CATH.FunFam:3.20.20.140:FF:000004)


    **Condition Set 51:** FunFam id: Guanine deaminase (CATH.FunFam:3.20.20.140:FF:000022)


    **Condition Set 52:** FunFam id: Arginase (CATH.FunFam:3.40.800.10:FF:000005)


    **Condition Set 53:** FunFam id: Beta-ureidopropionase 1 (CATH.FunFam:3.60.110.10:FF:000009)


    **Condition Set 54:** FunFam id: N(4)-(Beta-N-acetylglucosaminyl)-L-asparaginase
    isoform X1 (CATH.FunFam:3.60.20.30:FF:000003)


    **Condition Set 55:** FunFam id: Methylenetetrahydrofolate dehydrogenase (NADP+
    dependent) 1 like (CATH.FunFam:1.10.8.770:FF:000001) AND FunFam id: C-1-tetrahydrofolate
    synthase, cytoplasmic (CATH.FunFam:3.40.50.300:FF:000245) AND FunFam id: C-1-tetrahydrofolate
    synthase, cytoplasmic isoform X2 (CATH.FunFam:3.40.50.300:FF:001123)


    **Condition Set 56:** FunFam id: GTP cyclohydrolase 1 (CATH.FunFam:3.30.1130.10:FF:000007)
    AND FunFam id: GTP cyclohydrolase 1 (CATH.FunFam:3.30.1130.10:FF:000008) AND taxon:
    Spermatophyta (NCBITaxon:58024)


    **Condition Set 57:** FunFam id: Bifunctional protein FolD (CATH.FunFam:3.40.50.10860:FF:000001)
    AND FunFam id: probable bifunctional methylenetetrahydrofolate dehydrogenase/cyclohydrolase
    2 (CATH.FunFam:3.40.50.720:FF:000070) AND taxon: Rodentia (NCBITaxon:9989)


    **Condition Set 58:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1
    (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase
    PM20D1 (CATH.FunFam:3.40.630.10:FF:000027)


    **Condition Set 59:** FunFam id: Histidine biosynthesis bifunctional protein HisIE
    (CATH.FunFam:1.10.287.1080:FF:000002) AND FunFam id: Histidine biosynthesis trifunctional
    protein (CATH.FunFam:3.10.20.810:FF:000002)


    **Condition Set 60:** FunFam id: peptide-N(4)-(N-acetyl-beta- glucosaminyl)asparagine
    amidase (CATH.FunFam:2.20.25.10:FF:000011) AND FunFam id: Peptidase (PNG1) (CATH.FunFam:3.10.620.30:FF:000004)


    **Condition Set 61:** FunFam id: (S)-ureidoglycine aminohydrolase (CATH.FunFam:2.60.120.10:FF:000137)
    AND taxon: Magnoliopsida (NCBITaxon:3398)


    **Condition Set 62:** FunFam id: Cytosine deaminase (CATH.FunFam:3.20.20.140:FF:000019)
    AND taxon: Pseudomonadati (NCBITaxon:3379134)


    **Condition Set 63:** FunFam id: Guanine deaminase (CATH.FunFam:3.20.20.140:FF:000021)
    AND taxon: Myomorpha (NCBITaxon:1963758)


    **Condition Set 64:** FunFam id: Related to Chitin deacetylase (CATH.FunFam:3.20.20.370:FF:000004)
    AND taxon: Basidiomycota (NCBITaxon:5204)


    **Condition Set 65:** FunFam id: Chitin deacetylase (CATH.FunFam:3.20.20.370:FF:000008)
    AND taxon: Saccharomycotina (NCBITaxon:147537)


    **Condition Set 66:** FunFam id: Histidine triad nucleotide-binding protein 1
    (CATH.FunFam:3.30.428.10:FF:000005) AND taxon: Haplorrhini (NCBITaxon:376913)


    **Condition Set 67:** FunFam id: N-acetyldiaminopimelate deacetylase (CATH.FunFam:3.30.70.360:FF:000001)
    AND taxon: Bacillati (NCBITaxon:1783272)


    **Condition Set 68:** FunFam id: Bifunctional purine biosynthesis protein PURH
    (CATH.FunFam:3.40.140.20:FF:000008) AND FunFam id: Bifunctional purine biosynthesis
    protein (CATH.FunFam:3.40.50.1380:FF:000003)


    **Condition Set 69:** FunFam id: GTP cyclohydrolase-2 (CATH.FunFam:3.40.50.10990:FF:000002)
    AND taxon: Pseudomonadota (NCBITaxon:1224)


    **Condition Set 70:** FunFam id: Glucosamine-6-phosphate isomerase (CATH.FunFam:3.40.50.1360:FF:000004)
    AND taxon: Catarrhini (NCBITaxon:9526)


    **Condition Set 71:** FunFam id: Streptothricin hydrolase (CATH.FunFam:3.40.50.850:FF:000018)
    AND taxon: Actinomycetota (NCBITaxon:201174)


    **Condition Set 72:** FunFam id: Nicotinamidase 2 (CATH.FunFam:3.40.50.850:FF:000020)
    AND taxon: eudicotyledons (NCBITaxon:71240)


    **Condition Set 73:** FunFam id: 1,6-anhydro-N-acetylmuramyl-L-alanine amidase
    (CATH.FunFam:3.40.80.10:FF:000002) AND taxon: Gammaproteobacteria (NCBITaxon:1236)


    **Condition Set 74:** FunFam id: Arginase-1 (CATH.FunFam:3.40.800.10:FF:000011)
    AND taxon: Muridae (NCBITaxon:10066)


    **Condition Set 75:** FunFam id: Histone deacetylase (CATH.FunFam:3.40.800.20:FF:000003)
    AND taxon: Hominidae (NCBITaxon:9604)


    **Condition Set 76:** FunFam id: Isoaspartyl peptidase/L-asparaginase (CATH.FunFam:3.60.20.30:FF:000001)
    AND taxon: Gunneridae (NCBITaxon:91827)


    **Condition Set 77:** FunFam id: N(G),N(G)-dimethylarginine dimethylaminohydrolase
    1 (CATH.FunFam:3.75.10.10:FF:000004) AND taxon: Murinae (NCBITaxon:39107)


    **Condition Set 78:** FunFam id: 5-hydroxyisourate hydrolase (CATH.FunFam:2.60.40.180:FF:000004)


    **Condition Set 79:** FunFam id: Peptidyl arginine deiminase 3 (CATH.FunFam:2.60.40.1860:FF:000002)


    **Condition Set 80:** FunFam id: Imidazolonepropionase (CATH.FunFam:3.20.20.140:FF:000007)


    **Condition Set 81:** FunFam id: tRNA-specific adenosine deaminase (CATH.FunFam:3.40.140.10:FF:000005)


    **Condition Set 82:** FunFam id: Cytidine deaminase (CATH.FunFam:3.40.140.10:FF:000006)


    **Condition Set 83:** FunFam id: Cytosine deaminase (CATH.FunFam:3.40.140.10:FF:000016)


    **Condition Set 84:** FunFam id: Single-stranded DNA cytosine deaminase (CATH.FunFam:3.40.140.10:FF:000022)


    **Condition Set 85:** FunFam id: Probable C->U-editing enzyme APOBEC-2 (CATH.FunFam:3.40.140.10:FF:000031)


    **Condition Set 86:** FunFam id: tRNA-specific adenosine deaminase (CATH.FunFam:3.40.140.10:FF:000039)


    **Condition Set 87:** FunFam id: Agmatinase (CATH.FunFam:3.40.800.10:FF:000002)


    **Condition Set 88:** FunFam id: Arginase (CATH.FunFam:3.40.800.10:FF:000009)


    **Condition Set 89:** FunFam id: Agmatine deiminase (CATH.FunFam:3.75.10.10:FF:000012)


    **Condition Set 90:** FunFam id: Peptide deformylase (CATH.FunFam:3.90.45.10:FF:000003)


    *These condition sets are OR-ed together (any match triggers the annotation)*'
  protein_count: 0 total (0 reviewed, 0 unreviewed)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 58
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00026849
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0016810 (hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** InterPro id: Adenosine deaminase domain (InterPro:IPR001365) AND InterPro id: Adenosine/adenine deaminase (InterPro:IPR006330) AND InterPro id: Adenosine/AMP deaminase active site (InterPro:IPR006650)

**Condition Set 2:** InterPro id: Carbon-nitrogen hydrolase (InterPro:IPR003010) AND InterPro id: Carbon-nitrogen hydrolase superfamily (InterPro:IPR036526) AND taxon: Viridiplantae (NCBITaxon:33090)

**Condition Set 3:** InterPro id: Cytidine deaminase-like (InterPro:IPR016193) AND taxon: Saccharomycotina (NCBITaxon:147537)

**Condition Set 4:** InterPro id: Asparaginase/glutaminase-like (InterPro:IPR006034) AND InterPro id: Asparaginase/glutaminase, active site 1 (InterPro:IPR020827) AND InterPro id: L-asparaginase, C-terminal (InterPro:IPR027473)

**Condition Set 5:** InterPro id: Nitrilase/cyanide hydratase, conserved site (InterPro:IPR000132) AND InterPro id: Nitrilase/Cyanide hydratase (InterPro:IPR044149)

**Condition Set 6:** InterPro id: GTP cyclohydrolase I (InterPro:IPR001474) AND InterPro id: GTP cyclohydrolase I, conserved site (InterPro:IPR018234) AND taxon: Metazoa (NCBITaxon:33208)

**Condition Set 7:** InterPro id: Cytidine and deoxycytidylate deaminase domain (InterPro:IPR002125) AND InterPro id: APOBEC/CMP deaminase, zinc-binding (InterPro:IPR016192) AND taxon: Fungi (NCBITaxon:4751)

**Condition Set 8:** InterPro id: Peptidase M20 (InterPro:IPR002933) AND InterPro id: Amidase, carbamoylase-type (InterPro:IPR010158) AND PANTHER id: PTHR32494:SF19

**Condition Set 9:** InterPro id: Ureohydrolase (InterPro:IPR006035) AND InterPro id: Ureohydrolase domain superfamily (InterPro:IPR023696) AND taxon: Bacteria (NCBITaxon:2)

**Condition Set 10:** InterPro id: Biotinidase-like, eukaryotic (InterPro:IPR012101) AND InterPro id: Biotinidase/VNN family (InterPro:IPR040154) AND InterPro id: Vanin, C-terminal (InterPro:IPR043957)

**Condition Set 11:** InterPro id: Cytidine and Deoxycytidylate Deaminase (InterPro:IPR050202) AND PANTHER id: PTHR11644:SF2

**Condition Set 12:** PANTHER id: PTHR43114:SF6

**Condition Set 13:** InterPro id: Peptidase T2, asparaginase 2 (InterPro:IPR000246) AND InterPro id: Nucleophile aminohydrolases, N-terminal (InterPro:IPR029055) AND PANTHER id: PTHR10188:SF6

**Condition Set 14:** InterPro id: Beta-lactamase, class-B, conserved site (InterPro:IPR001018) AND InterPro id: Metallo-beta-lactamase (InterPro:IPR001279) AND taxon: Pseudomonadati (NCBITaxon:3379134)

**Condition Set 15:** InterPro id: NodB homology domain (InterPro:IPR002509) AND InterPro id: Polysaccharide deacetylase, ArnD subfamily (InterPro:IPR050248) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 16:** InterPro id: UDP-3-O-acyl N-acetylglucosamine deacetylase (InterPro:IPR004463) AND InterPro id: UDP-3-O-acyl N-acetylglucosamine deacetylase, C-terminal (InterPro:IPR011334) AND taxon: Streptophyta (NCBITaxon:35493)

**Condition Set 17:** InterPro id: Amidohydrolase-related (InterPro:IPR006680) AND InterPro id: Metal-dependent hydrolase, composite domain superfamily (InterPro:IPR011059) AND InterPro id: Deaminase MtaD/DadD (InterPro:IPR023512)

**Condition Set 18:** InterPro id: Kynurenine formamidase/cyclase-like (InterPro:IPR007325) AND InterPro id: Kynurenine formamidase, bacteria (InterPro:IPR017484) AND InterPro id: Kynurenine formamidase superfamily (InterPro:IPR037175)

**Condition Set 19:** InterPro id: Arginase (InterPro:IPR014033) AND InterPro id: Ureohydrolase, manganese-binding site (InterPro:IPR020855) AND PANTHER id: PTHR43782:SF3

**Condition Set 20:** InterPro id: Amidase, conserved site (InterPro:IPR020556) AND InterPro id: Amidase signature domain (InterPro:IPR023631) AND taxon: Tracheophyta (NCBITaxon:58023)

**Condition Set 21:** InterPro id: Agmatinase-related (InterPro:IPR005925) AND PANTHER id: PTHR11358:SF26

**Condition Set 22:** InterPro id: AMP deaminase (InterPro:IPR006329) AND taxon: Glires (NCBITaxon:314147)

**Condition Set 23:** InterPro id: Peptide deformylase (InterPro:IPR023635) AND InterPro id: Peptide deformylase superfamily (InterPro:IPR036821)

**Condition Set 24:** InterPro id: Aliphatic Amidase/Beta-Ureidopropionase (InterPro:IPR050345) AND PANTHER id: PTHR43674:SF2

**Condition Set 25:** FunFam id: GTP cyclohydrolase 1 (CATH.FunFam:1.10.286.10:FF:000003) AND FunFam id: GTP cyclohydrolase 1 (CATH.FunFam:3.30.1130.10:FF:000012) AND taxon: Metazoa (NCBITaxon:33208)

**Condition Set 26:** FunFam id: biotinidase isoform X1 (CATH.FunFam:3.60.110.10:FF:000001) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 27:** FunFam id: Bifunctional nitrilase/nitrile hydratase NIT4B (CATH.FunFam:3.60.110.10:FF:000006) AND taxon: Viridiplantae (NCBITaxon:33090)

**Condition Set 28:** FunFam id: L-asparaginase 2 (CATH.FunFam:3.40.50.1170:FF:000001)

**Condition Set 29:** FunFam id: Allantoate amidohydrolase (CATH.FunFam:3.40.630.10:FF:000044)

**Condition Set 30:** FunFam id: Probable UDP-3-O-acyl-N-acetylglucosamine deacetylase 3, mitochondrial (CATH.FunFam:3.30.1700.10:FF:000002) AND FunFam id: Probable UDP-3-O-acyl-N-acetylglucosamine deacetylase 2, mitochondrial (CATH.FunFam:3.30.230.20:FF:000002) AND taxon: Streptophyta (NCBITaxon:35493)

**Condition Set 31:** FunFam id: Kynurenine formamidase (CATH.FunFam:3.50.30.50:FF:000001) AND taxon: Bacteria (NCBITaxon:2)

**Condition Set 32:** FunFam id: AMP deaminase (CATH.FunFam:4.10.800.20:FF:000001) AND taxon: Glires (NCBITaxon:314147)

**Condition Set 33:** FunFam id: 5-methylthioadenosine/S-adenosylhomocysteine deaminase (CATH.FunFam:3.20.20.140:FF:000014)

**Condition Set 34:** FunFam id: Bifunctional purine biosynthesis protein PURH (CATH.FunFam:1.10.287.440:FF:000001) AND FunFam id: Bifunctional purine biosynthesis protein (CATH.FunFam:3.40.140.20:FF:000003) AND taxon: Dikarya (NCBITaxon:451864)

**Condition Set 35:** FunFam id: Protein-arginine deiminase type-2 (CATH.FunFam:2.60.40.1700:FF:000001) AND FunFam id: Protein-arginine deiminase type-2 (CATH.FunFam:3.75.10.10:FF:000003) AND taxon: Rattus (NCBITaxon:10114)

**Condition Set 36:** FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:3.30.1490.20:FF:000001) AND FunFam id: CAD protein-like isoform X1 (CATH.FunFam:3.40.50.1370:FF:000005) AND FunFam id: Carbamoyl-phosphate synthase 1, mitochondrial (CATH.FunFam:3.40.50.880:FF:000006)

**Condition Set 37:** FunFam id: Adenosine deaminase RNA-specific B2 (inactive) (CATH.FunFam:3.30.160.20:FF:000009) AND FunFam id: double-stranded RNA-specific editase 1 isoform X1 (CATH.FunFam:3.30.160.20:FF:000011) AND taxon: Chordata (NCBITaxon:7711)

**Condition Set 38:** FunFam id: N-acylsphingosine amidohydrolase 2 (CATH.FunFam:2.60.40.2300:FF:000001) AND taxon: Craniata (NCBITaxon:89593)

**Condition Set 39:** FunFam id: Adenosine deaminase (CATH.FunFam:3.20.20.140:FF:000038) AND taxon: Vertebrata (NCBITaxon:7742)

**Condition Set 40:** FunFam id: bifunctional heparan sulfate N-deacetylase/N-sulfotransferase 1 (CATH.FunFam:3.40.50.300:FF:000176) AND taxon: Mus (NCBITaxon:862507)

**Condition Set 41:** FunFam id: Arginase 1, mitochondrial (CATH.FunFam:3.40.800.10:FF:000007) AND taxon: Embryophyta (NCBITaxon:3193)

**Condition Set 42:** FunFam id: Dihydropyrimidinase like 3 (CATH.FunFam:3.20.20.140:FF:000001)

**Condition Set 43:** FunFam id: Cytidine deaminase (CATH.FunFam:3.40.140.10:FF:000008)

**Condition Set 44:** FunFam id: Aminoacylase-1, putative (CATH.FunFam:1.10.150.900:FF:000001) AND FunFam id: Putative Aminoacylase-1 (CATH.FunFam:3.30.70.360:FF:000005) AND FunFam id: Aminoacylase 1 (CATH.FunFam:3.40.630.10:FF:000019)

**Condition Set 45:** FunFam id: Putative formate--tetrahydrofolate ligase (CATH.FunFam:3.10.410.10:FF:000001) AND FunFam id: C-1-tetrahydrofolate synthase, cytoplasmic, putative (CATH.FunFam:3.40.50.10860:FF:000005) AND taxon: Ascomycota (NCBITaxon:4890)

**Condition Set 46:** FunFam id: NAD-dependent protein deacetylase sirtuin-1 (CATH.FunFam:3.30.1600.10:FF:000013) AND FunFam id: NAD-dependent deacetylase sirtuin-2 (CATH.FunFam:3.40.50.1220:FF:000005) AND taxon: Euteleostomi (NCBITaxon:117571)

**Condition Set 47:** FunFam id: Jasmonate-regulated gene 21 (CATH.FunFam:2.60.120.330:FF:000008) AND taxon: Tracheophyta (NCBITaxon:58023)

**Condition Set 48:** FunFam id: Apolipoprotein B editing enzyme catalytic polypeptide-like 3H (CATH.FunFam:3.40.140.10:FF:000047) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 49:** FunFam id: Protein-arginine deiminase type-4 (CATH.FunFam:2.60.40.1860:FF:000003)

**Condition Set 50:** FunFam id: N-acetylglucosamine-6-phosphate deacetylase (CATH.FunFam:3.20.20.140:FF:000004)

**Condition Set 51:** FunFam id: Guanine deaminase (CATH.FunFam:3.20.20.140:FF:000022)

**Condition Set 52:** FunFam id: Arginase (CATH.FunFam:3.40.800.10:FF:000005)

**Condition Set 53:** FunFam id: Beta-ureidopropionase 1 (CATH.FunFam:3.60.110.10:FF:000009)

**Condition Set 54:** FunFam id: N(4)-(Beta-N-acetylglucosaminyl)-L-asparaginase isoform X1 (CATH.FunFam:3.60.20.30:FF:000003)

**Condition Set 55:** FunFam id: Methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 1 like (CATH.FunFam:1.10.8.770:FF:000001) AND FunFam id: C-1-tetrahydrofolate synthase, cytoplasmic (CATH.FunFam:3.40.50.300:FF:000245) AND FunFam id: C-1-tetrahydrofolate synthase, cytoplasmic isoform X2 (CATH.FunFam:3.40.50.300:FF:001123)

**Condition Set 56:** FunFam id: GTP cyclohydrolase 1 (CATH.FunFam:3.30.1130.10:FF:000007) AND FunFam id: GTP cyclohydrolase 1 (CATH.FunFam:3.30.1130.10:FF:000008) AND taxon: Spermatophyta (NCBITaxon:58024)

**Condition Set 57:** FunFam id: Bifunctional protein FolD (CATH.FunFam:3.40.50.10860:FF:000001) AND FunFam id: probable bifunctional methylenetetrahydrofolate dehydrogenase/cyclohydrolase 2 (CATH.FunFam:3.40.50.720:FF:000070) AND taxon: Rodentia (NCBITaxon:9989)

**Condition Set 58:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:3.40.630.10:FF:000027)

**Condition Set 59:** FunFam id: Histidine biosynthesis bifunctional protein HisIE (CATH.FunFam:1.10.287.1080:FF:000002) AND FunFam id: Histidine biosynthesis trifunctional protein (CATH.FunFam:3.10.20.810:FF:000002)

**Condition Set 60:** FunFam id: peptide-N(4)-(N-acetyl-beta- glucosaminyl)asparagine amidase (CATH.FunFam:2.20.25.10:FF:000011) AND FunFam id: Peptidase (PNG1) (CATH.FunFam:3.10.620.30:FF:000004)

**Condition Set 61:** FunFam id: (S)-ureidoglycine aminohydrolase (CATH.FunFam:2.60.120.10:FF:000137) AND taxon: Magnoliopsida (NCBITaxon:3398)

**Condition Set 62:** FunFam id: Cytosine deaminase (CATH.FunFam:3.20.20.140:FF:000019) AND taxon: Pseudomonadati (NCBITaxon:3379134)

**Condition Set 63:** FunFam id: Guanine deaminase (CATH.FunFam:3.20.20.140:FF:000021) AND taxon: Myomorpha (NCBITaxon:1963758)

**Condition Set 64:** FunFam id: Related to Chitin deacetylase (CATH.FunFam:3.20.20.370:FF:000004) AND taxon: Basidiomycota (NCBITaxon:5204)

**Condition Set 65:** FunFam id: Chitin deacetylase (CATH.FunFam:3.20.20.370:FF:000008) AND taxon: Saccharomycotina (NCBITaxon:147537)

**Condition Set 66:** FunFam id: Histidine triad nucleotide-binding protein 1 (CATH.FunFam:3.30.428.10:FF:000005) AND taxon: Haplorrhini (NCBITaxon:376913)

**Condition Set 67:** FunFam id: N-acetyldiaminopimelate deacetylase (CATH.FunFam:3.30.70.360:FF:000001) AND taxon: Bacillati (NCBITaxon:1783272)

**Condition Set 68:** FunFam id: Bifunctional purine biosynthesis protein PURH (CATH.FunFam:3.40.140.20:FF:000008) AND FunFam id: Bifunctional purine biosynthesis protein (CATH.FunFam:3.40.50.1380:FF:000003)

**Condition Set 69:** FunFam id: GTP cyclohydrolase-2 (CATH.FunFam:3.40.50.10990:FF:000002) AND taxon: Pseudomonadota (NCBITaxon:1224)

**Condition Set 70:** FunFam id: Glucosamine-6-phosphate isomerase (CATH.FunFam:3.40.50.1360:FF:000004) AND taxon: Catarrhini (NCBITaxon:9526)

**Condition Set 71:** FunFam id: Streptothricin hydrolase (CATH.FunFam:3.40.50.850:FF:000018) AND taxon: Actinomycetota (NCBITaxon:201174)

**Condition Set 72:** FunFam id: Nicotinamidase 2 (CATH.FunFam:3.40.50.850:FF:000020) AND taxon: eudicotyledons (NCBITaxon:71240)

**Condition Set 73:** FunFam id: 1,6-anhydro-N-acetylmuramyl-L-alanine amidase (CATH.FunFam:3.40.80.10:FF:000002) AND taxon: Gammaproteobacteria (NCBITaxon:1236)

**Condition Set 74:** FunFam id: Arginase-1 (CATH.FunFam:3.40.800.10:FF:000011) AND taxon: Muridae (NCBITaxon:10066)

**Condition Set 75:** FunFam id: Histone deacetylase (CATH.FunFam:3.40.800.20:FF:000003) AND taxon: Hominidae (NCBITaxon:9604)

**Condition Set 76:** FunFam id: Isoaspartyl peptidase/L-asparaginase (CATH.FunFam:3.60.20.30:FF:000001) AND taxon: Gunneridae (NCBITaxon:91827)

**Condition Set 77:** FunFam id: N(G),N(G)-dimethylarginine dimethylaminohydrolase 1 (CATH.FunFam:3.75.10.10:FF:000004) AND taxon: Murinae (NCBITaxon:39107)

**Condition Set 78:** FunFam id: 5-hydroxyisourate hydrolase (CATH.FunFam:2.60.40.180:FF:000004)

**Condition Set 79:** FunFam id: Peptidyl arginine deiminase 3 (CATH.FunFam:2.60.40.1860:FF:000002)

**Condition Set 80:** FunFam id: Imidazolonepropionase (CATH.FunFam:3.20.20.140:FF:000007)

**Condition Set 81:** FunFam id: tRNA-specific adenosine deaminase (CATH.FunFam:3.40.140.10:FF:000005)

**Condition Set 82:** FunFam id: Cytidine deaminase (CATH.FunFam:3.40.140.10:FF:000006)

**Condition Set 83:** FunFam id: Cytosine deaminase (CATH.FunFam:3.40.140.10:FF:000016)

**Condition Set 84:** FunFam id: Single-stranded DNA cytosine deaminase (CATH.FunFam:3.40.140.10:FF:000022)

**Condition Set 85:** FunFam id: Probable C->U-editing enzyme APOBEC-2 (CATH.FunFam:3.40.140.10:FF:000031)

**Condition Set 86:** FunFam id: tRNA-specific adenosine deaminase (CATH.FunFam:3.40.140.10:FF:000039)

**Condition Set 87:** FunFam id: Agmatinase (CATH.FunFam:3.40.800.10:FF:000002)

**Condition Set 88:** FunFam id: Arginase (CATH.FunFam:3.40.800.10:FF:000009)

**Condition Set 89:** FunFam id: Agmatine deiminase (CATH.FunFam:3.75.10.10:FF:000012)

**Condition Set 90:** FunFam id: Peptide deformylase (CATH.FunFam:3.90.45.10:FF:000003)

*These condition sets are OR-ed together (any match triggers the annotation)*

---

## Research Objective

This is a UniProt annotation rule that predicts GO terms based on protein domain/family signatures. Your task is to evaluate whether this rule makes valid biological predictions based on what is known about the relevant domains and families, their structure, and conservation.

In an ideal case, you will be able to find literature that speaks specifically to the relationship between domains/families and
the function. Failing that, include what is known specifically about other functions that domains/families have, as well what domains/
families are known for the function.

## Research Questions

### 1. Domain/Signature Context

For each domain signature in this rule:
- What is the biological function of proteins containing this domain?
- Is this domain diagnostic for the predicted function?
- Are there known subfamilies with different functions?
- Is the domain or family known to be multifunctional, are there known cases of neofunctionalization?

### 2. GO Term Appropriateness

For the predicted GO term(s) **GO:0016810 (hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds)**:
- Is this GO term appropriate for proteins matching these conditions?
- Is the term too broad? (e.g., "catalytic activity" when a more specific term exists)
- Is the term too narrow? (e.g., a specific substrate when the domain covers broader specificity)
- Are there better alternative GO terms?

### 3. Literature Support

- What experimental evidence supports this functional annotation?
- Are there key papers describing this protein family/enzyme?
- Are there any contradictory findings in the literature?
- Is this a well-established function or more speculative?

### 4. Taxonomic Considerations

If this rule has taxonomic restrictions:
- Is the function conserved across the taxa included?
- Are there taxa that should be excluded (different function)?
- Are there taxa that could be included but are currently excluded?

### 5. Rule Logic Assessment

- Do the domain combinations make biological sense?
- Are there redundant conditions that could be removed?
- Could false positives arise from these conditions?

## Output Format

Please provide your findings in a narrative format with citations. Structure your response as:

1. **Executive Summary** - Brief assessment of rule validity
2. **Domain Analysis** - What each domain/signature represents
3. **GO Term Evaluation** - Assessment of the predicted annotation
4. **Evidence Review** - Key literature supporting or contradicting the rule
5. **Recommendations** - Suggested improvements or concerns

Be sure to include citations for all statements.

## Output

<think>
This is a complex research query about a UniProt annotation rule (ARBA00026849) that predicts GO:0016810 (hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds) based on various protein domain signatures.

Let me analyze the search results provided:

Key findings from the search results:

1. GO:0016810 definition [1][4][40]: "Catalysis of the hydrolysis of any carbon-nitrogen bond, C-N, with the exception of peptide bonds"

2. Multiple enzyme families mentioned in the rule:
- Adenosine deaminase (ADA) [2][30]: EC 3.5.4.4, involved in purine metabolism, converts adenosine to inosine
- Cytidine deaminase (CDA) [3][6][25][28]: EC 3.5.4.5, converts cytidine to uridine
- Asparaginase (L-asparaginase) [7][50]: EC 3.5.1.1, converts L-asparagine to L-aspartate
- Arginase [9][12][23]: EC 3.5.3.1, converts L-arginine to L-ornithine and urea
- Nitrilase [8][11]: EC 3.5.5.1, hydrolyzes nitriles to carboxylic acids
- GTP cyclohydrolase I [14][17]: EC 3.5.4.16, converts GTP to dihydroneopterin triphosphate

3. Zinc-dependent hydrolases: Multiple enzymes in this rule are zinc-dependent [2][3][25][31][34]

4. Manganese-dependent hydrolases: Arginase uses manganese [9][12]

5. Enzyme classification: All of these are hydrolases (EC 3.x.x.x) acting on carbon-nitrogen bonds
   
6. Additional enzyme families covered by the rule include biotinidase [22], which exhibits both hydrolase and transferase functions, and the M20 family metallopeptidases [21][60] with amidohydrolase activity. The nitrilase superfamily [32][11] comprises thiol-dependent enzymes involved in biosynthetic pathways, while the ureohydrolase superfamily [23] encompasses arginase and related enzymes like formiminoglutamase and proclavaminate amidinohydrolase.

The evidence indicates these represent a coherent group of hydrolases targeting C-N bonds outside the peptide context, with metal cofactors such as Zn2+ and Mn2+ playing central roles. Conservation across diverse organisms supports the validity of GO:0016810 as the appropriate classification.

However, I should verify whether the domain architecture actually supports these assignments, consider potential false positives in the annotation, evaluate if more granular specificity would be beneficial, and determine whether taxonomic constraints would improve accuracy.
</think>

# Comprehensive Analysis of UniProt ARBA Rule 00026849: Validation of GO:0016810 Annotation for Hydrolase Activity on Carbon-Nitrogen Bonds

The annotation rule ARBA00026849 represents a sophisticated computational framework designed to predict hydrolase activity acting on carbon-nitrogen bonds (excluding peptide bonds) across diverse protein families and taxonomic groups. This comprehensive analysis evaluates the biological validity of this multi-condition annotation rule by examining the structural, functional, and evolutionary characteristics of the domains and families it encompasses, assessing the appropriateness of the GO:0016810 term prediction, and examining the quality of experimental and computational evidence supporting these associations.

## Executive Summary of Rule Validity

The ARBA00026849 rule demonstrates substantial biological validity with well-established mechanistic and structural foundations. The rule encompasses ninety distinct condition sets that collectively identify proteins from multiple enzyme families known to catalyze carbon-nitrogen bond hydrolysis through conserved catalytic mechanisms. The predicted GO term GO:0016810 (hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds) accurately captures the enzymatic function of proteins matching these conditions[1][4][40]. The rule's architecture employs a logical OR-combination of condition sets, allowing detection of diverse enzyme families that share mechanistic convergence rather than sequence similarity. However, the analysis reveals opportunities for refinement regarding specificity, potential false positives, and taxonomic accuracy that warrant discussion and consideration in future rule iterations.

## Comprehensive Domain and Signature Analysis

### Adenosine Deaminase and Related Purine Deaminases

Adenosine deaminase, represented in the rule through InterPro domains IPR001365 (Adenosine deaminase domain), IPR006330 (Adenosine/adenine deaminase), and IPR006650 (Adenosine/AMP deaminase active site), belongs to the superfamily of purine/pyrimidine deaminases[2][16][30]. The enzyme catalyzes the irreversible deamination of adenosine to inosine through a zinc-dependent mechanism, representing a key step in purine metabolism[2]. Adenosine deaminase exhibits a characteristic structure composed of eight strands of parallel α/β barrels surrounding a central deep pocket containing the active site, with a zinc ion coordinated by histidine residues (His15, His17, His214), an aspartate residue (Asp295), and the substrate itself[2]. The enzyme's primary function in humans centers on development and maintenance of the immune system, with roles extending to epithelial cell differentiation, neurotransmission, and gestation maintenance[2]. A critical aspect of ADA function involves its participation in the purine salvage pathway, as evidenced by high conservation of amino acid sequences across bacteria, plants, invertebrates, vertebrates, and mammals[2].

The mechanism of catalysis involves stereospecific addition-elimination via tetrahedral intermediate formation[2]. The zinc ion functions as a strong electrophile, activating a water molecule that is subsequently deprotonated by Asp295 to form the attacking hydroxide species. His238 orients the water molecule and stabilizes the negative charge, while Glu217 provides a proton to N1 of the substrate purine ring[2]. This reaction represents a clear example of carbon-nitrogen bond hydrolysis (specifically C-N bonds in purine rings), making ADA a canonical substrate for the GO:0016810 annotation.

The rule includes provision for adenosine deaminase 2 (ADA2), identified through UniProt records[5], which exhibits similar functionality as an extracellular deaminase contributing to degradation of extracellular adenosine. The evolutionary conservation of these enzymes suggests their fundamental importance, and the zinc-dependent catalytic mechanism represents a conserved feature distinguishing these enzymes from other deaminase families.

### Cytidine and Cytosine Deaminases

Cytidine deaminase represents another critical enzyme family incorporated into this rule through multiple InterPro signatures including IPR016193 (Cytidine deaminase-like) and IPR002125 (Cytidine and deoxycytidylate deaminase domain)[3][6][25][28]. This enzyme catalyzes deamination of cytidine and deoxycytidine to uridine and deoxyuridine, respectively, functioning as an essential component of the pyrimidine salvage pathway in prokaryotes and fungi[3][6]. The enzyme achieves widespread interest for both antimicrobial drug design applications and gene therapy applications targeting tumors[3].

The catalytic mechanism of cytidine deaminase involves a zinc ion bound to His102, Cys129, Cys132, and a catalytic water molecule[3][25]. The zinc metal center polarizes the O-H bond of water, increasing its acidity toward the nearby Glu104 residue. The reaction proceeds through three major steps: substrate binding, ammonia release through formation of a tetrahedral intermediate, and product departure from the active site[3]. The zinc-bound hydroxide ion attacks the C2 position of the substrate, generating a tetrahedral intermediate that subsequently collapses to release ammonia and form uracil[3][25].

Cytidine deaminase exhibits considerable importance in genome stability and cancer chemoresistance[6]. The enzyme's deficiency can lead to replicative stress, notably observed in Bloom syndrome when combined with BLM mutations[6]. Recent research demonstrates that CDA deregulation produces accumulation of dCTP and pyrimidine catabolism intermediates, which can prove toxic to cells through mechanisms involving PARP-1 inhibition and DNA damage response activation[6]. The enzyme's secondary role in metabolizing cytidine analog-based therapies such as gemcitabine provides additional functional significance in clinical contexts[6].

The rule appropriately incorporates taxonomic restrictions for cytidine deaminase (InterPro:IPR002125 with taxon Saccharomycotina restriction), recognizing that this enzyme functions primarily in fungi and prokaryotes rather than in multicellular eukaryotes[3][6]. This taxonomic consideration represents a sophisticated refinement within the rule structure.

### Asparaginase and Glutaminase Activities

L-asparaginase (EC 3.5.1.1) represents another major enzyme family encompassed by this rule, identified through InterPro signatures IPR006034 (Asparaginase/glutaminase-like), IPR020827 (Asparaginase/glutaminase active site 1), and IPR027473 (L-asparaginase C-terminal)[7][50][53]. This enzyme catalyzes the reaction: L-asparagine + H₂O = L-aspartate + NH₃, representing a carbon-nitrogen bond hydrolysis reaction[7]. The enzyme holds significant clinical importance as a front-line chemotherapy agent for acute lymphoblastic leukemia (ALL), functioning through dual deamination of both asparagine and glutamine[50][53].

Structural characterization reveals that asparaginase exhibits an N-terminal loop whose conformational state critically influences substrate specificity[50]. The enzyme's selective preference for asparagine over glutamine depends on the conformational state of this regulatory loop, with evidence demonstrating that a single point mutation at position 121 (substitution of serine with proline) dramatically alters substrate selectivity without affecting the overall asparaginase activity[50]. This mechanistic finding highlights potential functional diversification within the asparaginase family through minimal structural modifications.

A critical consideration for asparaginase annotation involves recognition of its dual enzymatic activities—both asparaginase and glutaminase activities[50][53]. While the primary therapeutic activity involves asparagine deamination in ALL treatment, many asparaginase isoforms possess glutaminase activity as well[50][53]. Research demonstrates that glutaminase activity, not asparaginase activity, correlates with cytotoxicity in most ALL cell lines[53]. This dual functionality raises important questions about functional annotation specificity, as different asparaginase isoforms exhibit substantially different glutaminase activity levels while maintaining comparable asparaginase activity[53].

### Arginase and the Ureohydrolase Superfamily

Arginase (EC 3.5.3.1) exemplifies the ureohydrolase superfamily, incorporating InterPro signatures IPR014033 (Arginase), IPR020855 (Ureohydrolase, manganese-binding site), and IPR006035 (Ureohydrolase)[9][12][23][26]. The enzyme catalyzes the final and essential step of the urea cycle through the reaction: L-arginine + H₂O → L-ornithine + urea[9]. This represents another clear example of carbon-nitrogen bond hydrolysis, specifically affecting the C-N bonds within the guanidinium group of arginine.

The structure of arginase reveals a distinctive binuclear manganese cluster coordinated by active site residues, with a single hydroxide ion bridging the two Mn²⁺ ions[9][12]. This bridging hydroxide serves as the nucleophile attacking the guanidinium group of L-arginine, with the manganese ions stabilizing both the hydroxyl group and the developing lone electron pair during tetrahedral intermediate formation[9]. The enzyme demonstrates extremely narrow substrate specificity for L-arginine, with modifications to substrate structure or stereochemistry severely diminishing catalytic activity[9].

Arginase exists in two major isoforms: Arginase I (ARG1), which functions primarily in the urea cycle within hepatocytes, and Arginase II (ARG2), which regulates intracellular arginine/ornithine levels[9][12]. Recent research reveals extensive roles for both isoforms in regulating cellular functions including senescence, apoptosis, autophagy, proliferation, and inflammation through mechanisms both dependent and independent of L-arginine hydrolase activity[12]. ARG1 overexpression can deplete cellular L-arginine pools, reducing substrate availability for endothelial nitric oxide synthase and contributing to NO-uncoupling and increased oxidative stress—a key mechanism in cardiovascular disease pathogenesis[12].

The ureohydrolase superfamily extends beyond arginase to include related enzymes such as agmatinase and formiminoglutamase[23]. Agmatinase, another family member, hydrolyzes agmatine to putrescine, functioning as a precursor for polyamine biosynthesis and playing regulatory roles in mammals[23]. Crystal structures of agmatinase reveal a compact homohexamer with binuclear manganese coordination remarkably similar but not identical to arginase and proclavaminate amidinohydrolase[23].

### Nitrilase and Cyanide Hydratase Enzymes

Nitrilase enzymes (EC 3.5.5.1), identified in the rule through InterPro signature IPR000132 (Nitrilase/cyanide hydratase conserved site) and IPR044149 (Nitrilase/Cyanide hydratase), represent thiol-dependent enzymes catalyzing hydrolysis of nitriles to corresponding carboxylic acids and ammonia without formation of free amide intermediates[8][11]. These enzymes participate in natural product biosynthesis and post-translational modifications across plants, animals, fungi, and select prokaryotes[11].

The catalytic mechanism of nitrilase involves two critical cysteine residues functioning as nucleophiles[11]. The initial step consists of nucleophilic attack by a cysteine thiol on the electrophilic nitrile carbon, generating a thioimidate intermediate subsequently hydrolyzed to acylenzyme and ammonia[11]. The acylenzyme then undergoes one of two pathways depending on reaction conditions: further hydrolysis with water produces the carboxylic acid and regenerated enzyme, or hydrolysis by ammonia displaces the enzyme and forms the amide product[11]. This catalytic mechanism represents a distinct mechanistic approach compared to metal-dependent hydrolases, yet achieving the same fundamental carbon-nitrogen bond cleavage reaction.

Substrate specificity in nitrilase extends across diverse nitrile compounds, with different nitrilase members showing preferences for specific substrates[11]. For example, NIT1, NIT2, and NIT3 from Arabidopsis thaliana represent arylacetonitrilases hydrolyzing nitriles produced during cyanogenic glycoside and glucosinolate synthesis or degradation, while NIT4 specializes in β-cyano-L-alanine hydrolysis critical for cyanide detoxification[11]. The structural architecture of nitrilase reveals a distinctive α-β-β-α sandwich fold within each subunit that forms a "super-sandwich" structure upon dimerization[11]. The catalytic triad consists of Glu42, Lys113, and Cys146, with Glu42 functioning as the catalytic base and Lys113 as the catalytic acid[11].

### GTP Cyclohydrolase and Pteridine Biosynthesis

GTP cyclohydrolase I (EC 3.5.4.16), represented through InterPro domains IPR001474 (GTP cyclohydrolase I) and IPR018234 (GTP cyclohydrolase I conserved site), catalyzes the initial step in pteridine biosynthesis through conversion of GTP to dihydroneopterin triphosphate[14][17]. This enzyme catalyzes a mechanistically complex ring expansion process representing a carbon-nitrogen bond hydrolysis event[14]. The enzyme exists as a homodecameric protein complex of approximately 250 kDa molecular weight[17], with tetrameric-octomeric polymeric forms observed in various organisms[14].

GTP cyclohydrolase possesses strict substrate specificity for GTP, showing no catalytic activity with GDP, GMP, ATP, UTP, or CTP as substrates[14]. The enzyme's kinetic constant (Km) for GTP approximates 6.5 microMolar, with inhibitory effects observed for various nucleotide triphosphates including GDP (approximately 20% inhibition at 2 mM concentration), GMP (approximately 10% inhibition), ATP (approximately 50% inhibition), and UTP, CTP, TTP (approximately 33-50% inhibition)[14].

The functional significance of GTP cyclohydrolase extends beyond pteridine biosynthesis to encompassing tetrahydrofolate synthesis in plants and some microorganisms, and tetrahydrobiopterin (BH₄) synthesis in mammals[14]. These pteridine cofactors serve essential roles: tetrahydrofolate functions as a coenzyme for one-carbon transfer reactions, while BH₄ acts as an essential reducing cofactor for nitric oxide synthases, glyceryl ether mono-oxygenases, and aromatic amino acid hydroxylases[14]. The competitive inhibition of GTP cyclohydrolase by 2,4-diamino-6-hydroxypyrimidine (DAHP) demonstrates regulatory control over pteridine biosynthesis and has been explored for manipulation of nitric oxide synthesis in bacterial systems[14].

### Biotinidase and Related Enzymes

Biotinidase (EC 3.5.1.12), identified through InterPro signatures IPR012101 (Biotinidase-like, eukaryotic), IPR040154 (Biotinidase/VNN family), and IPR043957 (Vanin C-terminal), demonstrates unusual dual functionality as both hydrolase and transferase enzyme[19][22]. The enzyme possesses both amidohydrolase and transferase activities, participating in vitamin recycling pathways[19]. Clinical significance of biotinidase function is evident in biotinidase deficiency conditions, which can result in biotin deficiency-related complications[22].

Research in premature infants reveals interesting developmental patterns for biotinidase activity[22]. During the first three days of life, biotinidase activities in all 64 studied newborns fell below the normal adult range, with gradual increases reaching normal adult range during the 4-40 day post-birth period in 56 infants[22]. However, eight preterm infants showed aberrant patterns with activity drops during days 3-7 of life, potentially creating false-positive screening results when samples were collected during the lowest activity period[22].

### M20 Family Metallopeptidases and Amidases

The rule incorporates the M20 family metallopeptidases (InterPro:IPR002933) combined with amidase carbamoylase-type domains (InterPro:IPR010158)[21][36][60]. These enzymes represent metal-dependent hydrolases with zinc-binding characteristics[36]. Recent structural and functional characterization of two amidase enzymes from Deinococcus indicus DR1 demonstrates that amidases contain a conserved active site motif (-GHGG-) and exhibit zinc-binding residue coordination patterns[36]. These amidases display peptidoglycan cleavage activity, functioning in bacterial cell wall hydrolysis and daughter cell separation during cell division[36]. The catalytic activity of both identified amidases matched or exceeded lysozyme activity under extended incubation times[36].

## Evaluation of GO:0016810 Term Appropriateness

### Term Definition and Scope

The Gene Ontology term GO:0016810 is defined as "Catalysis of the hydrolysis of any carbon-nitrogen bond, C-N, with the exception of peptide bonds"[1][4][40]. This definition represents an appropriately broad but specific categorization of enzymatic function. The term occupies a hierarchical position within the Gene Ontology's Molecular Function category, functioning as a child term of the broader GO:0016787 (hydrolase activity) category[45][48].

### Verification of Functional Accuracy Across Rule Domains

All enzyme families encompassed within ARBA00026849 clearly demonstrate carbon-nitrogen bond hydrolytic activity. Adenosine deaminase catalyzes C-N bond hydrolysis in purine rings[2]. Cytidine deaminase performs similar reactions on pyrimidine substrates[3][25]. Asparaginase catalyzes C-N bond hydrolysis in the asparagine side chain[7][50]. Arginase catalyzes C-N bond hydrolysis in the guanidinium group of arginine[9][12]. Nitrilase catalyzes C-N triple bond hydrolysis in nitriles[8][11]. GTP cyclohydrolase catalyzes complex C-N bond cleavage within the purine ring during ring expansion[14][17]. These diverse mechanistic approaches all converge on the fundamental GO:0016810 category.

### Breadth-Specificity Assessment

The GO:0016810 term is appropriately broad for the functional diversity encompassed by this rule while remaining sufficiently specific to exclude peptide bond hydrolases, which represent a distinct enzyme class. More granular GO terms exist for specific substrate classes (for example, "adenosine deaminase activity" could theoretically exist), but the rule appropriately employs the broader categorical term reflecting the shared mechanistic feature across diverse enzyme families.

The term notably excludes peptide bond hydrolysis reactions, which represent the largest class of carbon-nitrogen bond hydrolytic enzymes. This exclusion is biochemically meaningful, as peptide bond hydrolysis occurs through mechanistically distinct processes and represents a functionally distinct category of protease enzymes. The GO:0016810 exclusion appropriately captures the specificity boundary.

### Alternative GO Terms Assessment

Alternative GO terms potentially applicable to subsets of these proteins include more specific substrate-dependent terms such as GO:0016811 (hydrolase activity acting on carbon-nitrogen bonds in linear amides)[40]. However, many enzymes in this rule, such as nitrilase and GTP cyclohydrolase, catalyze reactions not exclusively limited to linear amides, making GO:0016810 the more appropriate inclusive category.

Some specific enzyme families could theoretically be annotated with ultra-specific GO terms reflecting individual enzymatic activities (e.g., "arginase activity"). However, the rule's architecture deliberately employs the shared mechanistic feature—carbon-nitrogen bond hydrolysis—as the unifying functional principle. This represents a reasonable design choice balancing functional specificity with annotation consistency across diverse enzyme families.

## Experimental and Literature Evidence

### Zinc-Dependent Carbon-Nitrogen Hydrolases

The search results provide extensive documentation supporting zinc-dependent mechanisms for multiple enzyme families within this rule. Adenosine deaminase crystallographic structures reveal zinc coordination through His15, His17, His214, Asp295, and the substrate[2]. Cytidine deaminase exhibits zinc coordination through His102, Cys129, Cys132, and catalytic water[3][25]. These structural studies provide direct experimental evidence for the metal-dependent catalytic mechanisms enabling carbon-nitrogen bond hydrolysis[31][34].

Theoretical quantum mechanics/molecular mechanics studies on cytosine deaminase computational details provide mechanistic insights into the reaction pathway[34]. The calculations establish that Glu217 is essential for initial deprotonation of the metal-bound water nucleophile and subsequent protonation of the substrate[34]. This computational work corroborates experimental kinetic and structural data regarding the catalytic mechanism.

### Convergent Evolution of Catalytic Mechanisms

Research examining amidohydrolase superfamily proteins suggests convergent evolution of mechanistically similar catalytic approaches across structurally distinct protein scaffolds[57]. Isatin hydrolase enzymes employ manganese-dependent catalytic mechanisms with a novel catalytic triad (Asp-His-His) that appears structurally unrelated to zinc-dependent hydrolases yet achieves functionally equivalent carbon-nitrogen bond hydrolysis[57]. This convergent evolution supports the concept that multiple distinct structural solutions achieve the same fundamental enzymatic function.

### Enzyme Classification Supporting the Rule

The Enzyme Commission classification system explicitly categorizes all these enzymes within EC 3.5.-.- (hydrolases acting on carbon-nitrogen bonds other than peptide bonds), providing authoritative biological support for the rule's classification principle[10][40]. This EC classification hierarchy was developed through expert consensus regarding enzymatic function and mechanisms over decades of biochemical characterization.

### Functional Promiscuity and Substrate Specificity

Recent reviews of enzyme promiscuity highlight that many enzymes classified within the hydrolase category exhibit substrate ambiguity—the capacity to catalyze reactions with multiple substrate structures[51]. This substrate ambiguity represents an important evolutionary mechanism enabling acquisition of novel enzymatic functions. The enzymes encompassed within ARBA00026849 demonstrate varying degrees of substrate specificity: arginase exhibits extremely narrow specificity for L-arginine[9], while nitrilase demonstrates much broader substrate repertoire[11]. The GO:0016810 term appropriately captures this functional diversity without requiring ultra-specific substrate distinctions.

## Critical Examination of Rule Logic and Potential Issues

### Domain Combination Logic

The rule employs complex combinations of multiple InterPro domains and PANTHER family signatures within individual condition sets. For example, Condition Set 1 requires simultaneous presence of Adenosine deaminase domain (IPR001365), Adenosine/adenine deaminase (IPR006330), and Adenosine/AMP deaminase active site (IPR006650). This multi-domain requirement theoretically reduces false positive annotations by requiring concordant evidence. However, this architecture may simultaneously increase false negative rate by requiring strict concordance of computational domain predictions that may not always annotate consistently across different protein isoforms or distantly related family members.

The OR-combination of 90 distinct condition sets represents a dramatically inclusive approach to annotation. This structural choice potentially sacrifices specificity in favor of sensitivity, creating risk for false positive annotations. Some condition sets employ very narrow taxonomic restrictions (for example, Condition Set 19 restricts arginase annotation to specific PANTHER IDs and particular taxa), while others lack taxonomic restrictions entirely. This inconsistency could create systematic annotation biases across the proteome.

### Potential False Positive Scenarios

Several mechanistic considerations suggest potential false positive annotations:

First, proteins containing putative hydrolase domains might represent pseudoenzymes or non-catalytic domain-containing proteins that have lost catalytic function through evolutionary processes[51][52]. The rule's architecture employs domain-based prediction without directly examining catalytic residue conservation, potentially leading to annotation of non-functional homologs.

Second, proteins functioning as metalloprotein scaffolds or structural proteins might contain metal-binding motifs matching M20 family signatures without possessing actual amidohydrolase activity. The rule's integration of metal-binding domain signatures without discriminating between catalytic and structural metal coordination could generate false positives.

Third, multifunctional proteins with multiple enzymatic activities might be incorrectly assigned GO:0016810 when their primary or most significant function represents a different enzymatic activity. For example, biotinidase exhibits both transferase and hydrolase activities[19], yet the rule would annotate only the hydrolase activity component.

### Taxonomic Consistency Assessment

Examination of taxonomic restrictions across condition sets reveals important inconsistencies. Cytidine deaminase annotation appropriately restricts to Saccharomycotina fungi, recognizing that this enzyme functions primarily in fungi and prokaryotes rather than multicellular eukaryotes[3][6]. However, similar restrictions are not universally applied to other enzyme families that similarly have restricted organismal distributions. For example, several deaminases exhibit different functions or regulatory patterns across distant taxa, yet receive unrestricted taxonomic application.

The AID/APOBEC family of cytidine deaminases demonstrates instructive evolutionary history demonstrating why taxonomic restrictions warrant careful consideration[38][41][54]. Phylogenetic analysis reveals that AID and APOBEC2 represent ancestral family members present from the beginning of vertebrate speciation, while APOBEC1 and APOBEC3 represent mammal-specific derivatives[38][41]. This evolutionary trajectory suggests that unqualified annotation of "cytidine deaminase activity" might inappropriately annotate proteins from invertebrate species where only the ancestral AID protein functions in this capacity, potentially missing mechanistic specialization in vertebrate APOBEC variants[41][54].

### Rule Redundancy Analysis

The 90 condition sets within ARBA00026849 suggest potential redundancy. Multiple condition sets employ overlapping domain signatures in different combinations (for example, multiple conditions reference cytidine deaminase-like domains with varying additional domain requirements and taxonomic restrictions). The cumulative effect of these overlapping conditions may create unnecessary computational complexity without proportional improvement in annotation accuracy.

## Structural and Mechanistic Coherence

### Metal Coordination Consistency

The enzyme families encompassed within this rule predominantly employ metal cofactors for catalytic function. Zinc-dependent hydrolases (adenosine deaminase, cytidine deaminase, asparaginase, GTP cyclohydrolase) represent the most common structural class[2][3][31][34]. Manganese-dependent hydrolases (arginase, agmatinase) employ similar metal-dependent mechanisms with distinct coordination geometries[9][12][23]. Biotinidase exhibits zinc-binding characteristics[36]. This near-universal requirement for metal cofactors, despite mechanistic variations in precise coordination, represents a significant structural principle unifying these enzyme families.

The fact that all these enzymes utilize metal coordination to activate water nucleophiles or directly participate in catalysis suggests strong structural and mechanistic coherence supporting the GO:0016810 functional category. The metal cofactor requirement distinguishes these carbon-nitrogen hydrolases from non-metal-dependent hydrolases operating through other mechanisms.

### Catalytic Triad and Active Site Architecture

Multiple enzyme families within this rule employ recognizable catalytic triads or analogous residue combinations. Cytidine deaminase employs Glu104 (general base), His102 (metal ligand coordination), and Cys129/132 (metal ligation)[3][25]. Nitrilase employs Glu42 (catalytic base), Lys113 (catalytic acid), and Cys146 (nucleophile)[11]. Isatin hydrolase employs a novel Asp-His-His catalytic triad[57]. These distinct catalytic architectures accomplish mechanistically similar transformations through convergent evolution, providing experimental evidence for mechanistic flexibility in achieving carbon-nitrogen bond hydrolysis.

### Substrate Recognition Mechanisms

The enzyme families encompassed within ARBA00026849 demonstrate diverse substrate recognition mechanisms reflecting their distinct substrate specificities. Adenosine deaminase achieves substrate specificity through nine hydrogen bonds stabilizing adenosine binding to the active site[2]. Asparaginase achieves specificity through an N-terminal loop conformational mechanism discriminating between asparagine and glutamine[50]. Arginase achieves extraordinary specificity through saturation of all hydrogen bonding positions on the arginine carboxylate and amino groups[9]. These mechanistically distinct substrate recognition strategies support the principle that GO:0016810 appropriately captures functional diversity while emphasizing the shared carbon-nitrogen bond hydrolytic mechanism.

## Recent Developments and Current Research Directions

### Enzyme Engineering and Functional Modification

Recent computational enzyme design research demonstrates capacity to enhance secondary amidase activity in existing hydrolase proteins through rational QM/MM molecular dynamics strategies[33]. This research reveals that existing hydrolase scaffolds possess latent capacity for catalyzing alternative carbon-nitrogen hydrolytic reactions through minor electrostatic modifications, suggesting that enzyme multifunctionality and neofunctionalization remain active evolutionary processes.

### Functional Annotation Prediction Methods

Contemporary protein annotation methodology employs machine learning approaches (CLEAN-Contact) combining amino acid sequence information with protein structural inference to predict enzyme functions more accurately than traditional sequence homology approaches[55]. These emerging methods achieve 2.0-2.5 fold improvements in precision compared to earlier approaches, suggesting potential for improved annotation accuracy through incorporation of structural information beyond simple domain signature presence.

### Advances in Hydrolase Structure and Function

Structural characterization continues revealing previously unrecognized hydrolase functions. The recent discovery that certain proteins exhibit differential metal dependency (for example, some showing preference for manganese over zinc) indicates that previous annotations might require refinement[57]. Similarly, the characterization of multifunctional proteins like biotinidase demonstrates that single-function annotations may inadequately represent biological reality[19].

## Taxonomic Considerations and Organismal Distribution

### Conservation Across Domains of Life

The enzyme families encompassed within ARBA00026849 demonstrate remarkable evolutionary conservation. Adenosine deaminase has been identified in bacteria, plants, invertebrates, vertebrates, and mammals, indicating Precambrian evolutionary origin[2]. Arginase's ubiquity across all biological domains[9] underscores its fundamental metabolic importance. This evolutionary depth suggests that GO:0016810 annotations should apply broadly across eukaryotic and prokaryotic organisms.

### Prokaryotic-Eukaryotic Differences

Certain enzyme families show restricted distributions warranting taxonomic specificity in annotation rules. Cytidine deaminase functions primarily in prokaryotes and fungi, with multicellular eukaryotes employing alternative pyrimidine pathway mechanisms[3][6]. Nitrilase distribution patterns show selectivity across organisms[11]. These organism-specific distribution patterns support incorporation of taxonomic restrictions in annotation rules.

### Protist and Fungal Specificity

Fungal species employ distinct metabolic strategies for certain pathways that differentiate them from bacteria or multicellular eukaryotes. The specific incorporation of taxonomic restrictions for Saccharomycotina in cytidine deaminase annotations represents sophisticated recognition of these organismal differences. However, similar specificity may warrant consideration for other enzyme families lacking current taxonomic restrictions.

## Recommendations for Rule Refinement

### Domain Combination Optimization

The rule would benefit from systematic evaluation of domain combination redundancy. Analysis of the 90 condition sets should identify overlapping or near-identical condition combinations that might be consolidated. For example, multiple conditions referencing cytidine deaminase-like domains with similar ancillary domain requirements could potentially be merged into single comprehensive conditions with refined taxonomic specifications.

### False Positive Reduction Strategies

Implementation of catalytic residue conservation scoring would reduce false positive annotations of pseudoenzymes or

## Citations

1. https://amigo.geneontology.org/amigo/term/GO:0016810
2. https://en.wikipedia.org/wiki/Adenosine_deaminase
3. https://www.ebi.ac.uk/thornton-srv/m-csa/entry/97/
4. https://www.informatics.jax.org/vocab/gene_ontology/GO:0016810
5. https://www.uniprot.org/uniprotkb/Q9NZK5/entry
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC7001087/
7. https://pubchem.ncbi.nlm.nih.gov/protein/EC:3.5.1.1
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC3815905/
9. https://en.wikipedia.org/wiki/Arginase
10. https://enzyme.expasy.org/EC/3.5.1.-
11. https://en.wikipedia.org/wiki/Nitrilase
12. https://www.nature.com/articles/s41420-022-01200-4
13. https://flybase.org/reports/FBgn0036752.html
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC309945/
15. https://string-db.org/network/3702.Q8GXV5
16. https://www.ebi.ac.uk/interpro/entry/InterPro/IPR001365/feedback/
17. https://onlinelibrary.wiley.com/doi/abs/10.1002/0470028637.met007
18. https://tgil.donga.ac.kr/gene/?locus=Lj6g3v1392530
19. https://www.ebi.ac.uk/interpro/entry/cdd/CD07567/
20. https://zfin.org/ZDB-GENE-040426-847
21. https://www.ebi.ac.uk/interpro/entry/interpro/IPR002933
22. https://pubmed.ncbi.nlm.nih.gov/3409923/
23. https://pubmed.ncbi.nlm.nih.gov/15355972/
24. https://www.uniprot.org/uniprotkb/A0A0H2WZV8/entry
25. https://www.cathdb.info/version/v4_4_0/superfamily/3.40.800.10/funfam/2/go
26. https://www.cathdb.info/superfamily/3.20.20.140
27. https://www.cathdb.info/superfamily/3.40.140.10
28. https://www.cathdb.info/superfamily/3.40.800.10
29. https://www.uniprot.org/uniprotkb/P00813/entry
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC3427388/
31. https://www.brennerlab.net/files/pace01.pdf
32. https://pubs.rsc.org/en/content/articlehtml/2022/sc/d2sc00778a
33. https://pubs.acs.org/doi/10.1021/jp501228s
34. https://www.ncbi.nlm.nih.gov/Structure/sparcle/archview.html?archid=10353633
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC10964502/
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC1557498/
37. https://academic.oup.com/mbe/article/22/2/367/963921
38. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0014286
39. https://pubmed.ncbi.nlm.nih.gov/15496550/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC3032897/
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC10544392/
42. https://academic.oup.com/bioinformatics/article/32/15/2264/1742842
43. https://www.informatics.jax.org/vocab/gene_ontology/GO:0016787
44. https://academic.oup.com/nar/article/53/D1/D243/7889254
45. https://www.uniprot.org/help/sequence_annotation
46. https://www.ebi.ac.uk/QuickGO/term/GO:0016787
47. https://www.sanger.ac.uk/wp-content/uploads/large-files/242-mb9-thesis.pdf
48. https://www.nature.com/articles/srep41643
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC4215207/
50. https://www2.eecs.berkeley.edu/Pubs/TechRpts/2007/EECS-2007-171.pdf
51. https://pmc.ncbi.nlm.nih.gov/articles/PMC4458142/
52. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2021.642343/full
53. https://pmc.ncbi.nlm.nih.gov/articles/PMC11666736/
54. https://academic.oup.com/nar/article/49/D1/D480/6006196
55. https://pmc.ncbi.nlm.nih.gov/articles/PMC6117287/
56. http://geneontology.org/GO_REF/0000003.html
57. https://www.uniprot.org/help/arba
58. https://pubs.acs.org/doi/10.1021/acs.jafc.5c06860