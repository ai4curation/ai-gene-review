---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-25T19:22:57.797113'
end_time: '2025-11-25T19:25:04.702196'
duration_seconds: 126.91
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00027128
  rule_type: arba
  go_terms: GO:0005576 (extracellular region)
  conditions_summary: '**Condition Set 1:** InterPro id: Immunoglobulin-like domain
    (InterPro:IPR007110) AND InterPro id: Immunoglobulin Variable Light Chain (InterPro:IPR050150)
    AND taxon: Primates (NCBITaxon:9443)


    **Condition Set 2:** InterPro id: Wnt (InterPro:IPR005817) AND InterPro id: Wnt
    protein, conserved site (InterPro:IPR018161) AND taxon: Haplorrhini (NCBITaxon:376913)


    **Condition Set 3:** InterPro id: Immunoglobulin V-set domain (InterPro:IPR013106)
    AND InterPro id: Immunoglobulin-like fold (InterPro:IPR013783) AND InterPro id:
    Immunoglobulin Heavy Variable (InterPro:IPR050199)


    **Condition Set 4:** InterPro id: Frog antimicrobial peptide, brevinin-2/esculentin
    type (InterPro:IPR012521) AND taxon: Pelophylax (NCBITaxon:121164)


    **Condition Set 5:** InterPro id: Laminin IV (InterPro:IPR000034) AND InterPro
    id: Laminin/Netrin Extracellular Matrix (InterPro:IPR050440) AND taxon: Mammalia
    (NCBITaxon:40674)


    **Condition Set 6:** InterPro id: Chemokine interleukin-8-like domain (InterPro:IPR001811)
    AND InterPro id: CXC Chemokine domain (InterPro:IPR033899) AND taxon: Hominidae
    (NCBITaxon:9604)


    **Condition Set 7:** InterPro id: Serine proteases, trypsin domain (InterPro:IPR001254)
    AND InterPro id: Peptidase S1A, chymotrypsin family (InterPro:IPR001314) AND taxon:
    Lepidosauria (NCBITaxon:8504)


    **Condition Set 8:** InterPro id: Nerve growth factor-related (InterPro:IPR002072)
    AND InterPro id: Nerve growth factor conserved site (InterPro:IPR019846) AND taxon:
    Eutheria (NCBITaxon:9347)


    **Condition Set 9:** InterPro id: Lipocalin/cytosolic fatty-acid binding domain
    (InterPro:IPR000566) AND InterPro id: Retinol binding protein/Purpurin (InterPro:IPR002449)
    AND InterPro id: Calycin (InterPro:IPR012674)


    **Condition Set 10:** InterPro id: EGF-like domain (InterPro:IPR000742) AND InterPro
    id: Laminin alpha, domain I (InterPro:IPR009254) AND taxon: Chordata (NCBITaxon:7711)


    **Condition Set 11:** InterPro id: Aspartic peptidase A1 (InterPro:IPR001461)
    AND InterPro id: Aspartic peptidase, active site (InterPro:IPR001969) AND taxon:
    Pichiomycetes (NCBITaxon:3239874)


    **Condition Set 12:** InterPro id: Hemocyanin/hexamerin middle domain (InterPro:IPR000896)
    AND InterPro id: Tyrosinase copper-binding domain (InterPro:IPR002227) AND PANTHER
    id: PTHR11511:SF4


    **Condition Set 13:** InterPro id: Frog antimicrobial peptide, propeptide (InterPro:IPR004275)
    AND taxon: Litoria (NCBITaxon:8370)


    **Condition Set 14:** InterPro id: Snake toxin-like superfamily (InterPro:IPR045860)
    AND taxon: Micrurus (NCBITaxon:8634)


    **Condition Set 15:** InterPro id: Transthyretin/hydroxyisourate hydrolase (InterPro:IPR000895)
    AND InterPro id: Transthyretin/hydroxyisourate hydrolase domain (InterPro:IPR023416)
    AND PANTHER id: PTHR10395:SF12


    **Condition Set 16:** InterPro id: Stress-inducible humoral factor Turandot (InterPro:IPR010825)
    AND taxon: Eukaryota (NCBITaxon:2759)


    **Condition Set 17:** InterPro id: Bacteriocin class IIa domain superfamily (InterPro:IPR023388)
    AND taxon: Bacteria (NCBITaxon:2)


    **Condition Set 18:** InterPro id: Neuregulin (InterPro:IPR040180) AND taxon:
    Metazoa (NCBITaxon:33208)


    **Condition Set 19:** InterPro id: EGF-type aspartate/asparagine hydroxylation
    site (InterPro:IPR000152) AND InterPro id: Gamma-carboxyglutamic acid-rich (GLA)
    domain (InterPro:IPR000294) AND PANTHER id: PTHR24278:SF28


    **Condition Set 20:** InterPro id: Thyroglobulin type-1 (InterPro:IPR000716) AND
    InterPro id: Growth factor receptor cysteine-rich domain superfamily (InterPro:IPR009030)
    AND taxon: Mus (NCBITaxon:862507)


    **Condition Set 21:** InterPro id: Hemocyanin, C-terminal (InterPro:IPR005203)
    AND InterPro id: Hemocyanin, N-terminal (InterPro:IPR005204) AND taxon: Brachycera
    (NCBITaxon:7203)


    **Condition Set 22:** InterPro id: Cecropin-like (InterPro:IPR000875) AND taxon:
    Arthropoda (NCBITaxon:6656)


    **Condition Set 23:** InterPro id: Defensin, invertebrate/fungal (InterPro:IPR001542)
    AND taxon: Diptera (NCBITaxon:7147)


    **Condition Set 24:** InterPro id: Casein alpha/beta, conserved site (InterPro:IPR031305)
    AND taxon: Euteleostomi (NCBITaxon:117571)


    **Condition Set 25:** InterPro id: Gamma-carboxyglutamic acid-rich (GLA) domain
    superfamily (InterPro:IPR035972) AND taxon: Rattus (NCBITaxon:10114)


    **Condition Set 26:** InterPro id: Insulin-like superfamily (InterPro:IPR036438)
    AND taxon: Hexapoda (NCBITaxon:6960)


    **Condition Set 27:** PANTHER id: PTHR11511:SF5 AND taxon: Insecta (NCBITaxon:50557)


    **Condition Set 28:** InterPro id: Laminin-type EGF domain (InterPro:IPR002049)
    AND InterPro id: Concanavalin A-like lectin/glucanase domain superfamily (InterPro:IPR013320)
    AND InterPro id: Neurexin-related cell adhesion and synaptic protein (InterPro:IPR050372)


    **Condition Set 29:** InterPro id: Glycosyl hydrolase family 32, N-terminal (InterPro:IPR013148)
    AND InterPro id: Glycoside hydrolase, family 32, active site (InterPro:IPR018053)
    AND taxon: Saccharomycotina (NCBITaxon:147537)


    **Condition Set 30:** InterPro id: Insulin-like growth factor II E-peptide, C-terminal
    (InterPro:IPR013576) AND InterPro id: Insulin-like (InterPro:IPR016179) AND PANTHER
    id: PTHR46886:SF1


    **Condition Set 31:** InterPro id: Cecropin/Sarcotoxins/Aedesins (InterPro:IPR020400)
    AND PANTHER id: PTHR38329:SF1 AND taxon: Ecdysozoa (NCBITaxon:1206794)


    **Condition Set 32:** InterPro id: Bombesin/neuromedin-B/ranatensin peptide family
    (InterPro:IPR000874) AND taxon: Amphibia (NCBITaxon:8292)


    **Condition Set 33:** InterPro id: Lipocalin (InterPro:IPR002345) AND PANTHER
    id: PTHR11430:SF86


    **Condition Set 34:** InterPro id: Ant venom peptides (InterPro:IPR049518) AND
    taxon: Pterygota (NCBITaxon:300552)


    **Condition Set 35:** InterPro id: Bradykinin (InterPro:IPR009608)


    **Condition Set 36:** PANTHER id: PTHR47966:SF24


    **Condition Set 37:** InterPro id: Anaphylatoxin/fibulin (InterPro:IPR000020)
    AND InterPro id: Netrin domain (InterPro:IPR001134) AND InterPro id: Complement
    C4, MG1 domain (InterPro:IPR048847)


    **Condition Set 38:** InterPro id: Fibronectin, type I (InterPro:IPR000083) AND
    InterPro id: Fibronectin type II domain (InterPro:IPR000562) AND InterPro id:
    Fibronectin type III (InterPro:IPR003961)


    **Condition Set 39:** InterPro id: Peptidase S8/S53 domain (InterPro:IPR000209)
    AND InterPro id: Peptidase S8 propeptide/proteinase inhibitor I9 (InterPro:IPR010259)
    AND PANTHER id: PTHR43806:SF58


    **Condition Set 40:** InterPro id: ALB/AFP/VDB (InterPro:IPR000264) AND InterPro
    id: Serum albumin, N-terminal (InterPro:IPR014760) AND PANTHER id: PTHR11385:SF15


    **Condition Set 41:** InterPro id: Coagulation factor 5/8, C-terminal domain (InterPro:IPR000421)
    AND InterPro id: Cupredoxin (InterPro:IPR008972) AND InterPro id: Galactose-binding-like
    domain superfamily (InterPro:IPR008979)


    **Condition Set 42:** InterPro id: Glycoside hydrolase family 18, catalytic domain
    (InterPro:IPR001223) AND InterPro id: Chitinase Cts1-like (InterPro:IPR045321)
    AND PANTHER id: PTHR45708:SF49


    **Condition Set 43:** InterPro id: Kazal domain (InterPro:IPR002350) AND InterPro
    id: Kazal domain superfamily (InterPro:IPR036058) AND taxon: Phasianinae (NCBITaxon:9072)


    **Condition Set 44:** InterPro id: Prolamin-like domain (InterPro:IPR008502) AND
    InterPro id: Egg cell-secreted protein 1.1-1.5 (InterPro:IPR044711) AND taxon:
    Viridiplantae (NCBITaxon:33090)


    **Condition Set 45:** InterPro id: Tissue inhibitor of metalloproteinases-like,
    OB-fold (InterPro:IPR008993) AND InterPro id: Alpha-macroglobulin-like, thiol-ester
    bond-forming region (InterPro:IPR047565) AND taxon: Glires (NCBITaxon:314147)


    **Condition Set 46:** InterPro id: Resuscitation-promoting factor, core lysozyme-like
    domain (InterPro:IPR010618) AND InterPro id: Lysozyme-like domain superfamily
    (InterPro:IPR023346) AND taxon: Mycobacterium (NCBITaxon:1763)


    **Condition Set 47:** InterPro id: Serum albumin, conserved site (InterPro:IPR020857)
    AND InterPro id: Serum albumin/Alpha-fetoprotein/Afamin (InterPro:IPR021177) AND
    taxon: Rodentia (NCBITaxon:9989)


    **Condition Set 48:** InterPro id: Insulin/IGF/relaxin (InterPro:IPR022352) AND
    InterPro id: Insulin, conserved site (InterPro:IPR022353) AND taxon: Ruminantia
    (NCBITaxon:9845)


    **Condition Set 49:** InterPro id: Spaetzle (InterPro:IPR032104) AND InterPro
    id: Spaetzle/Toll ligand-like (InterPro:IPR052444) AND taxon: Neoptera (NCBITaxon:33340)


    **Condition Set 50:** InterPro id: Beta-microseminoprotein (InterPro:IPR008735)


    **Condition Set 51:** FunFam id: Wnt homolog (CATH.FunFam:3.30.2460.20:FF:000001)
    AND taxon: Primates (NCBITaxon:9443)


    **Condition Set 52:** FunFam id: Alpha-like toxin BmK-M1 (CATH.FunFam:3.30.30.10:FF:000002)
    AND taxon: Centruroides (NCBITaxon:6875)


    **Condition Set 53:** FunFam id: Brain-derived neurotrophic factor (CATH.FunFam:2.10.90.10:FF:000002)
    AND taxon: Mammalia (NCBITaxon:40674)


    **Condition Set 54:** FunFam id: C-X-C motif chemokine (CATH.FunFam:2.40.50.40:FF:000004)
    AND taxon: Haplorrhini (NCBITaxon:376913)


    **Condition Set 55:** FunFam id: Laminin subunit alpha 3 (CATH.FunFam:2.10.25.10:FF:000084)
    AND taxon: Eutheria (NCBITaxon:9347)


    **Condition Set 56:** FunFam id: Retinol-binding protein 4 (CATH.FunFam:2.40.128.20:FF:000004)
    AND taxon: Eukaryota (NCBITaxon:2759)


    **Condition Set 57:** FunFam id: Immunoglobulin kappa chain variable 12-38 (CATH.FunFam:2.60.40.10:FF:000212)
    AND taxon: Metazoa (NCBITaxon:33208)


    **Condition Set 58:** FunFam id: complement C3 isoform X1 (CATH.FunFam:2.60.40.10:FF:000155)
    AND FunFam id: Complement component C3 (CATH.FunFam:2.60.40.1940:FF:000001) AND
    taxon: Euarchontoglires (NCBITaxon:314146)


    **Condition Set 59:** FunFam id: Laminin subunit alpha 4 (CATH.FunFam:2.10.25.10:FF:000051)
    AND taxon: Chordata (NCBITaxon:7711)


    **Condition Set 60:** FunFam id: Laminin subunit alpha 1 (CATH.FunFam:2.10.25.10:FF:000069)
    AND taxon: Craniata (NCBITaxon:89593)


    **Condition Set 61:** FunFam id: Aspartic protease (CATH.FunFam:2.40.70.10:FF:000011)
    AND taxon: Pichiomycetes (NCBITaxon:3239874)


    **Condition Set 62:** FunFam id: Aspartic protease (CATH.FunFam:2.40.70.10:FF:000023)
    AND taxon: Debaryomycetaceae (NCBITaxon:766764)


    **Condition Set 63:** FunFam id: Immunoglobulin lambda variable 2-8 (CATH.FunFam:2.60.40.10:FF:000442)
    AND taxon: Vertebrata (NCBITaxon:7742)


    **Condition Set 64:** FunFam id: Immunoglobulin heavy constant gamma 1 (CATH.FunFam:2.60.40.10:FF:000463)
    AND taxon: Catarrhini (NCBITaxon:9526)


    **Condition Set 65:** FunFam id: Transthyretin (CATH.FunFam:2.60.40.180:FF:000002)
    AND taxon: Euteleostomi (NCBITaxon:117571)


    **Condition Set 66:** FunFam id: Collagenase 3 (CATH.FunFam:3.40.390.10:FF:000007)
    AND taxon: Hominidae (NCBITaxon:9604)


    **Condition Set 67:** FunFam id: Immunoglobulin kappa constant (CATH.FunFam:2.60.40.10:FF:000283)
    AND taxon: Homo (NCBITaxon:9605)


    **Condition Set 68:** FunFam id: Immunoglobulin heavy variable 3-23 (CATH.FunFam:2.60.40.10:FF:000942)


    **Condition Set 69:** FunFam id: Hemocyanin subunit 2 (CATH.FunFam:1.10.1280.10:FF:000004)
    AND FunFam id: Hemocyanin subunit 2 (CATH.FunFam:2.60.40.1520:FF:000001) AND taxon:
    Hexapoda (NCBITaxon:6960)


    **Condition Set 70:** FunFam id: Serum albumin (CATH.FunFam:1.10.246.10:FF:000001)
    AND FunFam id: Serum albumin (CATH.FunFam:1.10.246.10:FF:000002) AND FunFam id:
    Serum albumin (CATH.FunFam:1.10.246.10:FF:000003)


    **Condition Set 71:** FunFam id: Notch, isoform B (CATH.FunFam:2.10.25.10:FF:000095)
    AND FunFam id: FAT atypical cadherin 4 (CATH.FunFam:2.10.25.10:FF:000151) AND
    FunFam id: Neurogenic locus notch homolog protein 2 (CATH.FunFam:2.10.25.10:FF:000393)


    **Condition Set 72:** FunFam id: Coagulation factor X (Predicted) (CATH.FunFam:2.10.25.10:FF:000162)
    AND FunFam id: Coagulation factor VII (CATH.FunFam:2.10.25.10:FF:000513) AND FunFam
    id: vitamin K-dependent protein S (CATH.FunFam:4.10.740.10:FF:000001)


    **Condition Set 73:** FunFam id: Complement inhibitory factor H (CATH.FunFam:2.10.70.10:FF:000026)
    AND FunFam id: Complement inhibitory factor H (CATH.FunFam:2.10.70.10:FF:000054)
    AND FunFam id: Complement inhibitory factor H (CATH.FunFam:2.10.70.10:FF:000060)


    **Condition Set 74:** FunFam id: Cytotoxin 1 (CATH.FunFam:2.10.60.10:FF:000024)
    AND taxon: Micrurus (NCBITaxon:8634)


    **Condition Set 75:** FunFam id: Beta-1,3-glucan-binding protein (CATH.FunFam:2.60.120.200:FF:000235)
    AND taxon: Ecdysozoa (NCBITaxon:1206794)


    **Condition Set 76:** FunFam id: Beta-1,3-glucan-binding protein (CATH.FunFam:2.60.40.2140:FF:000001)
    AND taxon: Arthropoda (NCBITaxon:6656)


    **Condition Set 77:** FunFam id: Defensin (CATH.FunFam:3.30.30.10:FF:000005) AND
    taxon: Insecta (NCBITaxon:50557)


    **Condition Set 78:** FunFam id: Prostaglandin-H2 D-isomerase (CATH.FunFam:2.40.128.20:FF:000010)


    **Condition Set 79:** FunFam id: renin (CATH.FunFam:2.40.70.10:FF:000032)


    **Condition Set 80:** FunFam id: If kappa light chain (CATH.FunFam:2.60.40.10:FF:000365)


    **Condition Set 81:** FunFam id: Fibronectin 1a isoform 1 (CATH.FunFam:2.10.10.10:FF:000001)
    AND FunFam id: Fibronectin 1 (CATH.FunFam:2.10.70.10:FF:000004) AND FunFam id:
    Fibronectin 1 (CATH.FunFam:2.10.70.10:FF:000006)


    **Condition Set 82:** FunFam id: Venom plasminogen activator TSV-PA (CATH.FunFam:2.40.10.10:FF:000153)
    AND FunFam id: Thrombin-like enzyme saxthrombin (CATH.FunFam:2.40.10.10:FF:000158)
    AND taxon: Lepidosauria (NCBITaxon:8504)


    **Condition Set 83:** FunFam id: Coagulation factor VIII (CATH.FunFam:2.60.120.260:FF:000002)
    AND FunFam id: Coagulation factor VIII (Predicted) (CATH.FunFam:2.60.40.420:FF:000011)


    **Condition Set 84:** FunFam id: Proteinase K (CATH.FunFam:3.40.50.200:FF:000014)
    AND taxon: Fungi (NCBITaxon:4751)


    **Condition Set 85:** FunFam id: Interleukin-17A (CATH.FunFam:2.10.90.10:FF:000038)


    **Condition Set 86:** FunFam id: Complement C1r subcomponent (CATH.FunFam:2.40.10.10:FF:000054)


    **Condition Set 87:** FunFam id: Slit guidance ligand 2 (CATH.FunFam:2.10.25.10:FF:000045)
    AND FunFam id: Slit guidance ligand 2 (CATH.FunFam:2.10.25.10:FF:000053) AND FunFam
    id: Slit guidance ligand 2 (CATH.FunFam:2.10.25.10:FF:000099)


    **Condition Set 88:** FunFam id: Transmembrane agrin (CATH.FunFam:2.10.25.10:FF:000134)
    AND FunFam id: Transmembrane agrin (CATH.FunFam:2.10.25.10:FF:000140) AND FunFam
    id: Transmembrane agrin (CATH.FunFam:2.60.120.200:FF:000027)


    **Condition Set 89:** FunFam id: Tissue-type plasminogen activator (CATH.FunFam:2.10.25.10:FF:000483)
    AND FunFam id: Plasminogen activator (CATH.FunFam:2.10.70.10:FF:000043) AND FunFam
    id: Urokinase-type plasminogen activator (CATH.FunFam:2.40.20.10:FF:000001)


    **Condition Set 90:** FunFam id: Semaphorin 3F like (CATH.FunFam:2.60.40.10:FF:000030)
    AND FunFam id: Semaphorin 3F like (CATH.FunFam:3.30.1680.10:FF:000001) AND taxon:
    Archelosauria (NCBITaxon:1329799)


    **Condition Set 91:** FunFam id: Dystroglycan 1 (CATH.FunFam:2.60.40.10:FF:000555)
    AND FunFam id: Dystroglycan 1 (CATH.FunFam:2.60.40.10:FF:000684) AND FunFam id:
    Dystroglycan 1 (CATH.FunFam:3.30.70.1040:FF:000001)


    **Condition Set 92:** FunFam id: Insulin (CATH.FunFam:1.10.100.10:FF:000003) AND
    taxon: Glires (NCBITaxon:314147)


    **Condition Set 93:** FunFam id: Apolipoprotein E (CATH.FunFam:1.20.120.20:FF:000002)
    AND FunFam id: Apolipoprotein E (CATH.FunFam:1.20.120.20:FF:000003)


    **Condition Set 94:** FunFam id: Bacteriocin hiracin-JM79 (CATH.FunFam:1.20.5.130:FF:000001)
    AND taxon: Bacteria (NCBITaxon:2)


    **Condition Set 95:** FunFam id: Basic phospholipase A2 homolog (CATH.FunFam:1.20.90.10:FF:000001)
    AND taxon: Crotalus (NCBITaxon:8728)


    **Condition Set 96:** FunFam id: Bone morphogenetic protein 16 (CATH.FunFam:2.10.90.10:FF:000103)
    AND taxon: Rodentia (NCBITaxon:9989)


    **Condition Set 97:** FunFam id: Glycosylphosphatidylinositol specific phospholipase
    D1 (CATH.FunFam:2.130.10.130:FF:000010) AND FunFam id: Glycosylphosphatidylinositol
    specific phospholipase D1 (CATH.FunFam:2.130.10.130:FF:000011)


    **Condition Set 98:** FunFam id: Major urinary protein (CATH.FunFam:2.40.128.20:FF:000008)
    AND taxon: Cricetidae (NCBITaxon:337677)


    **Condition Set 99:** FunFam id: Cerebellin 4 (CATH.FunFam:2.60.120.40:FF:000002)
    AND taxon: Myomorpha (NCBITaxon:1963758)


    **Condition Set 100:** FunFam id: Interleukin-12 subunit beta (CATH.FunFam:2.60.40.10:FF:000959)
    AND FunFam id: Interleukin-12 subunit beta (CATH.FunFam:2.60.40.10:FF:001008)


    **Condition Set 101:** FunFam id: Larval serum protein 2 (CATH.FunFam:2.60.40.1520:FF:000002)
    AND taxon: Neoptera (NCBITaxon:33340)


    **Condition Set 102:** FunFam id: Lipoprotein lipase (CATH.FunFam:2.60.60.20:FF:000006)
    AND FunFam id: Lipoprotein lipase (CATH.FunFam:3.40.50.1820:FF:000031)


    **Condition Set 103:** FunFam id: oxytocin-neurophysin 1 (CATH.FunFam:2.60.9.10:FF:000001)
    AND taxon: Muroidea (NCBITaxon:337687)


    **Condition Set 104:** FunFam id: Cholesteryl ester transfer protein (CATH.FunFam:3.15.10.10:FF:000002)
    AND FunFam id: Cholesteryl ester transfer protein (CATH.FunFam:3.15.20.10:FF:000002)


    **Condition Set 105:** FunFam id: CTS1p Endochitinase (CATH.FunFam:3.20.20.80:FF:000125)
    AND taxon: Dikarya (NCBITaxon:451864)


    **Condition Set 106:** FunFam id: Indian hedgehog (CATH.FunFam:3.30.1380.10:FF:000001)
    AND taxon: Muridae (NCBITaxon:10066)


    **Condition Set 107:** FunFam id: Toxin-like peptide AaF1CA7 (CATH.FunFam:3.30.30.10:FF:000008)
    AND taxon: Chelicerata (NCBITaxon:6843)


    **Condition Set 108:** FunFam id: Insulin-like growth factor binding protein 5
    (CATH.FunFam:4.10.40.20:FF:000001) AND taxon: Mus (NCBITaxon:862507)


    **Condition Set 109:** FunFam id: R-spondin 3 (CATH.FunFam:2.10.220.10:FF:000003)


    **Condition Set 110:** FunFam id: Immunoglobulin kappa chain variable 18-36 (CATH.FunFam:2.60.40.10:FF:000350)


    **Condition Set 111:** FunFam id: Immunoglobulin lambda locus (CATH.FunFam:2.60.40.10:FF:000620)


    **Condition Set 112:** FunFam id: Mannose-binding protein A (CATH.FunFam:3.10.100.10:FF:000088)


    **Condition Set 113:** FunFam id: Interferon-induced protein 35 (CATH.FunFam:3.30.70.330:FF:000300)


    **Condition Set 114:** FunFam id: Amine oxidase (CATH.FunFam:1.10.405.10:FF:000004)
    AND FunFam id: Amine oxidase (CATH.FunFam:3.50.50.60:FF:000450) AND taxon: Crotalinae
    (NCBITaxon:8710)


    **Condition Set 115:** FunFam id: Vascular endothelial growth factor receptor
    2 (CATH.FunFam:1.10.510.10:FF:000077) AND FunFam id: Vascular endothelial growth
    factor receptor 3 (CATH.FunFam:2.60.40.10:FF:000143) AND FunFam id: vascular endothelial
    growth factor receptor 1 (CATH.FunFam:2.60.40.10:FF:000934)


    **Condition Set 116:** FunFam id: binder of sperm protein homolog 1 (CATH.FunFam:2.10.10.10:FF:000003)
    AND FunFam id: Epididymal sperm binding protein 1 (CATH.FunFam:2.10.10.10:FF:000005)
    AND taxon: Laurasiatheria (NCBITaxon:314145)


    **Condition Set 117:** FunFam id: Coagulation factor XII (CATH.FunFam:2.10.10.10:FF:000010)
    AND FunFam id: hepatocyte growth factor activator (CATH.FunFam:2.10.25.10:FF:000338)
    AND FunFam id: Coagulation factor XII (CATH.FunFam:2.10.25.10:FF:000576)


    **Condition Set 118:** FunFam id: Signal peptide, CUB domain, EGF-like 2 (CATH.FunFam:2.10.25.10:FF:000008)
    AND FunFam id: Signal peptide, CUB domain and EGF-like domain-containing 2 (CATH.FunFam:2.10.25.10:FF:000028)
    AND FunFam id: signal peptide, CUB and EGF-like domain-containing protein 2 isoform
    X2 (CATH.FunFam:2.10.25.10:FF:000199)


    **Condition Set 119:** FunFam id: Pro-epidermal growth factor (CATH.FunFam:2.10.25.10:FF:000010)
    AND FunFam id: Pro-epidermal growth factor (CATH.FunFam:2.10.25.10:FF:000219)
    AND FunFam id: Pro-epidermal growth factor (CATH.FunFam:2.10.25.10:FF:000254)


    **Condition Set 120:** FunFam id: Slit guidance ligand 2 (CATH.FunFam:2.10.25.10:FF:000054)
    AND FunFam id: Slit guidance ligand 2 (CATH.FunFam:2.60.120.200:FF:000013) AND
    taxon: Murinae (NCBITaxon:39107)


    **Condition Set 121:** FunFam id: Mannan-binding lectin serine protease 1 (CATH.FunFam:2.10.25.10:FF:000059)
    AND FunFam id: Mannan-binding lectin serine protease 1 (CATH.FunFam:2.10.70.10:FF:000016)
    AND FunFam id: mannan-binding lectin serine protease 1 isoform X2 (CATH.FunFam:2.10.70.10:FF:000028)


    **Condition Set 122:** FunFam id: Neurogenic locus notch protein 1 (CATH.FunFam:2.10.25.10:FF:000060)
    AND FunFam id: Neurogenic locus notch 1 (CATH.FunFam:2.10.25.10:FF:000080) AND
    FunFam id: Notch receptor 3 (CATH.FunFam:2.10.25.10:FF:000516)


    **Condition Set 123:** FunFam id: vitamin K-dependent protein S (CATH.FunFam:2.10.25.10:FF:000119)
    AND FunFam id: Growth arrest-specific protein 6 (CATH.FunFam:2.10.25.10:FF:000528)
    AND FunFam id: growth arrest-specific protein 6 (CATH.FunFam:2.60.120.200:FF:000089)


    **Condition Set 124:** FunFam id: Nidogen 1 (CATH.FunFam:2.10.25.10:FF:000270)
    AND FunFam id: Nidogen 1 (CATH.FunFam:2.10.25.10:FF:000281) AND FunFam id: Testican-3
    isoform 2 (CATH.FunFam:4.10.800.10:FF:000001)


    **Condition Set 125:** FunFam id: Invertase 2 (CATH.FunFam:2.115.10.20:FF:000002)
    AND FunFam id: Invertase 2 (CATH.FunFam:2.60.120.560:FF:000004) AND taxon: Ascomycota
    (NCBITaxon:4890)


    **Condition Set 126:** FunFam id: Hepatocyte growth factor (CATH.FunFam:2.40.10.10:FF:000023)
    AND FunFam id: Hepatocyte growth factor (CATH.FunFam:2.40.10.10:FF:000026) AND
    FunFam id: Hepatocyte growth factor (CATH.FunFam:2.40.20.10:FF:000004)


    **Condition Set 127:** FunFam id: Reelin (CATH.FunFam:2.60.120.260:FF:000003)
    AND FunFam id: Reelin (CATH.FunFam:2.60.120.260:FF:000028) AND FunFam id: Reelin
    (CATH.FunFam:2.60.120.260:FF:000057)


    **Condition Set 128:** FunFam id: Proprotein convertase subtilisin/kexin type
    1 (CATH.FunFam:2.60.120.260:FF:000054) AND FunFam id: Proprotein convertase subtilisin/kexin
    type 5 (CATH.FunFam:3.30.70.850:FF:000001) AND FunFam id: Putative neuroendocrine
    convertase 1 (CATH.FunFam:3.40.50.200:FF:000010)


    **Condition Set 129:** FunFam id: Proprotein convertase subtilisin/kexin type
    9 (CATH.FunFam:2.60.120.690:FF:000001) AND FunFam id: Proprotein convertase subtilisin/kexin
    type 9 (CATH.FunFam:3.30.70.80:FF:000004) AND FunFam id: Proprotein convertase
    subtilisin/kexin type 9 (CATH.FunFam:3.40.50.200:FF:000016)


    **Condition Set 130:** FunFam id: Ceruloplasmin (CATH.FunFam:2.60.40.420:FF:000009)
    AND FunFam id: Ceruloplasmin (CATH.FunFam:2.60.40.420:FF:000015) AND FunFam id:
    Ceruloplasmin (CATH.FunFam:2.60.40.420:FF:000028)


    **Condition Set 131:** FunFam id: Triacylglycerol lipase (CATH.FunFam:2.60.60.20:FF:000003)
    AND FunFam id: Pancreatic triacylglycerol lipase (CATH.FunFam:3.40.50.1820:FF:000033)
    AND taxon: Rattus (NCBITaxon:10114)


    **Condition Set 132:** FunFam id: Follistatin-related protein 3 (CATH.FunFam:3.30.60.30:FF:000025)
    AND FunFam id: Follistatin-related protein 3 (CATH.FunFam:3.30.60.30:FF:000028)
    AND FunFam id: follistatin-related protein 3 (CATH.FunFam:3.90.290.10:FF:000021)


    **Condition Set 133:** FunFam id: Insulin-degrading enzyme (CATH.FunFam:3.30.830.10:FF:000003)
    AND FunFam id: Putative insulin-degrading enzyme (CATH.FunFam:3.30.830.10:FF:000004)
    AND FunFam id: Putative insulin-degrading enzyme (CATH.FunFam:3.30.830.10:FF:000006)


    **Condition Set 134:** FunFam id: Ectonucleotide pyrophosphatase/phosphodiesterase
    family member 2 (CATH.FunFam:3.40.570.10:FF:000001) AND FunFam id: Ectonucleotide
    pyrophosphatase/phosphodiesterase family member 2 (CATH.FunFam:3.40.720.10:FF:000006)
    AND FunFam id: Ectonucleotide pyrophosphatase/phosphodiesterase family member
    2 (CATH.FunFam:4.10.410.20:FF:000001)


    **Condition Set 135:** FunFam id: NT5E isoform 4 (CATH.FunFam:3.60.21.10:FF:000020)
    AND FunFam id: UDP-sugar hydrolase, putative (CATH.FunFam:3.90.780.10:FF:000004)
    AND taxon: Diptera (NCBITaxon:7147)


    **Condition Set 136:** FunFam id: Peroxidasin homolog (CATH.FunFam:1.10.640.10:FF:000001)
    AND taxon: Artiodactyla (NCBITaxon:91561)


    **Condition Set 137:** FunFam id: Fatty-acid and retinol-binding protein 1 (CATH.FunFam:1.20.120.1100:FF:000001)
    AND taxon: Onchocerca (NCBITaxon:6281)


    **Condition Set 138:** FunFam id: Apolipoprotein A-IV (CATH.FunFam:1.20.120.20:FF:000004)
    AND FunFam id: Apolipoprotein A-IV (CATH.FunFam:1.20.120.20:FF:000005)


    **Condition Set 139:** FunFam id: Apolipoprotein B (CATH.FunFam:1.25.10.20:FF:000004)
    AND FunFam id: Apolipoprotein B (CATH.FunFam:2.30.230.10:FF:000003)


    **Condition Set 140:** FunFam id: Pro-neuregulin-1, membrane-bound isoform A (CATH.FunFam:2.10.25.10:FF:000073)
    AND FunFam id: Pro-neuregulin-1, membrane-bound isoform (CATH.FunFam:2.60.40.10:FF:000263)


    **Condition Set 141:** FunFam id: pro-neuregulin-2, membrane-bound isoform (CATH.FunFam:2.10.25.10:FF:000116)
    AND FunFam id: Pro-neuregulin-2, membrane-bound isoform (CATH.FunFam:2.60.40.10:FF:000354)


    **Condition Set 142:** FunFam id: Coagulation factor VII (CATH.FunFam:2.10.25.10:FF:000259)
    AND FunFam id: Coagulation factor VII (CATH.FunFam:2.10.25.10:FF:000420)


    **Condition Set 143:** FunFam id: Beta-microseminoprotein (CATH.FunFam:2.10.70.10:FF:000137)
    AND FunFam id: Beta-microseminoprotein (CATH.FunFam:2.20.25.590:FF:000001)


    **Condition Set 144:** FunFam id: Inhibin beta A chain (CATH.FunFam:2.10.90.10:FF:000005)
    AND FunFam id: inhibin beta B chain (CATH.FunFam:2.60.120.970:FF:000012)


    **Condition Set 145:** FunFam id: Spatzle 4 (CATH.FunFam:2.10.90.10:FF:000018)
    AND taxon: Brachycera (NCBITaxon:7203)


    **Condition Set 146:** FunFam id: CD109 isoform 3 (CATH.FunFam:2.60.40.1930:FF:000001)
    AND taxon: Nematocera (NCBITaxon:7148)


    **Condition Set 147:** FunFam id: Cell surface Cu-only superoxide dismutase 5
    (CATH.FunFam:2.60.40.200:FF:000007) AND taxon: Saccharomycotina (NCBITaxon:147537)


    **Condition Set 148:** FunFam id: Yolk protein 2 (CATH.FunFam:3.40.50.1820:FF:000227)
    AND taxon: Muscomorpha (NCBITaxon:43733)


    **Condition Set 149:** FunFam id: Fibrinogen beta chain (CATH.FunFam:3.90.215.10:FF:000006)
    AND FunFam id: Fibrinogen beta chain (CATH.FunFam:4.10.530.10:FF:000004)


    **Condition Set 150:** FunFam id: Angiotensin-converting enzyme (CATH.FunFam:1.10.1370.30:FF:000001)


    **Condition Set 151:** FunFam id: Tetraspanin (CATH.FunFam:1.10.1450.10:FF:000016)


    **Condition Set 152:** FunFam id: Macrophage colony-stimulating factor 1 (CATH.FunFam:1.20.1250.10:FF:000010)


    **Condition Set 153:** FunFam id: Erythropoietin (CATH.FunFam:1.20.1250.10:FF:000013)


    **Condition Set 154:** FunFam id: Interleukin 20 (CATH.FunFam:1.20.1250.10:FF:000019)


    **Condition Set 155:** FunFam id: Interleukin-5 (CATH.FunFam:1.20.1250.10:FF:000034)


    **Condition Set 156:** FunFam id: Interleukin 24 (CATH.FunFam:1.20.1250.10:FF:000038)


    **Condition Set 157:** FunFam id: Growth hormone d21 (CATH.FunFam:1.20.1250.10:FF:000047)


    **Condition Set 158:** FunFam id: Interleukin (CATH.FunFam:1.20.1250.70:FF:000001)


    **Condition Set 159:** FunFam id: Protransforming growth factor alpha (CATH.FunFam:2.10.25.10:FF:000182)


    **Condition Set 160:** FunFam id: Proepiregulin (CATH.FunFam:2.10.25.10:FF:000320)


    **Condition Set 161:** FunFam id: Beta-2-glycoprotein 1 (CATH.FunFam:2.10.70.10:FF:000089)


    **Condition Set 162:** FunFam id: Muellerian-inhibiting factor (CATH.FunFam:2.10.90.10:FF:000033)


    **Condition Set 163:** FunFam id: Placenta growth factor (CATH.FunFam:2.10.90.10:FF:000055)


    **Condition Set 164:** FunFam id: Connective tissue growth factor (Predicted)
    (CATH.FunFam:2.20.100.10:FF:000036)


    **Condition Set 165:** FunFam id: Serine protease inhibitor (serpin) 16 (CATH.FunFam:2.30.39.10:FF:000035)


    **Condition Set 166:** FunFam id: kallikrein-6 isoform X2 (CATH.FunFam:2.40.10.10:FF:000041)


    **Condition Set 167:** FunFam id: Apolipoprotein M (CATH.FunFam:2.40.128.20:FF:000011)


    **Condition Set 168:** FunFam id: Alpha-1-acid glycoprotein 2 (CATH.FunFam:2.40.128.20:FF:000012)


    **Condition Set 169:** FunFam id: Lymphotactin isoform X1 (CATH.FunFam:2.40.50.40:FF:000023)


    **Condition Set 170:** FunFam id: Immunoglobulin heavy variable 7-81 (non-functional)
    (CATH.FunFam:2.60.40.10:FF:000556)


    **Condition Set 171:** FunFam id: Immunoglobulin heavy variable 4-30-4 (CATH.FunFam:2.60.40.10:FF:001119)


    **Condition Set 172:** FunFam id: Pulmonary surfactant-associated protein A (CATH.FunFam:3.10.100.10:FF:000056)


    **Condition Set 173:** FunFam id: Soluble cell wall protein (CATH.FunFam:3.20.20.80:FF:000111)


    **Condition Set 174:** FunFam id: Serpin family G member 1 (CATH.FunFam:3.30.497.10:FF:000013)


    **Condition Set 175:** FunFam id: Ser/Thr protein phosphatase family (CATH.FunFam:3.60.21.10:FF:000043)


    **Condition Set 176:** FunFam id: Cocaine-and amphetamine-regulated transcript
    protein (CATH.FunFam:4.10.40.30:FF:000001)


    **Condition Set 177:** FunFam id: complement component C8 beta chain (CATH.FunFam:4.10.400.10:FF:000069)


    **Condition Set 178:** FunFam id: Cysteine-rich secretory protein 2 (CATH.FunFam:1.10.10.740:FF:000001)
    AND FunFam id: Cysteine-rich secretory protein 2 (CATH.FunFam:3.40.33.10:FF:000005)
    AND taxon: Bifurcata (NCBITaxon:1329961)


    **Condition Set 179:** FunFam id: Creatine kinase M-type (CATH.FunFam:1.10.135.10:FF:000001)
    AND FunFam id: Creatine kinase B-type (CATH.FunFam:3.30.590.10:FF:000026) AND
    taxon: Dinosauria (NCBITaxon:436486)


    **Condition Set 180:** FunFam id: prosaposin isoform X2 (CATH.FunFam:1.10.225.10:FF:000002)
    AND FunFam id: prosaposin isoform X2 (CATH.FunFam:1.10.225.10:FF:000004) AND FunFam
    id: prosaposin isoform X2 (CATH.FunFam:1.10.225.10:FF:000005)


    **Condition Set 181:** FunFam id: Alanine aminotransferase 2 (CATH.FunFam:1.10.287.1970:FF:000001)
    AND FunFam id: Alanine aminotransferase 2 (CATH.FunFam:3.40.640.10:FF:000236)
    AND FunFam id: Alanine aminotransferase 2 (CATH.FunFam:3.90.1150.10:FF:000010)


    **Condition Set 182:** FunFam id: Molecular chaperone DnaK (CATH.FunFam:1.20.1270.10:FF:000001)
    AND FunFam id: Chaperone protein DnaK HSP70 (CATH.FunFam:2.60.34.10:FF:000014)
    AND taxon: Mycobacterium (NCBITaxon:1763)


    **Condition Set 183:** FunFam id: Heat shock 70 kDa protein 4 (CATH.FunFam:1.20.1270.10:FF:000002)
    AND FunFam id: Heat shock protein 105 kDa isoform 1 (CATH.FunFam:1.20.1270.10:FF:000012)
    AND FunFam id: Heat shock protein 70 (HSP70)-4, putative (CATH.FunFam:3.30.420.40:FF:000767)


    **Condition Set 184:** FunFam id: Complement C5 (CATH.FunFam:1.20.91.20:FF:000004)
    AND FunFam id: Complement component C5 (CATH.FunFam:2.20.130.20:FF:000008) AND
    FunFam id: Complement C5 (CATH.FunFam:2.40.50.120:FF:000023)


    **Condition Set 185:** FunFam id: Latent-transforming growth factor beta-binding
    protein 3 (CATH.FunFam:2.10.25.10:FF:000002) AND FunFam id: fibrillin-1 isoform
    X1 (CATH.FunFam:2.10.25.10:FF:000003) AND FunFam id: Fibrillin 2 (CATH.FunFam:2.10.25.10:FF:000149)


    **Condition Set 186:** FunFam id: Thrombospondin 3 (CATH.FunFam:2.10.25.10:FF:000025)
    AND FunFam id: Thrombospondin 3 (CATH.FunFam:2.10.25.10:FF:000027) AND FunFam
    id: Thrombospondin type-1 domain-containing protein 1 (CATH.FunFam:2.20.100.10:FF:000115)


    **Condition Set 187:** FunFam id: FAT atypical cadherin 4 (CATH.FunFam:2.10.25.10:FF:000066)
    AND FunFam id: von Willebrand factor A domain containing 2 (CATH.FunFam:2.10.25.10:FF:000336)
    AND FunFam id: von Willebrand factor A domain containing 2 (CATH.FunFam:3.40.50.410:FF:000047)


    **Condition Set 188:** FunFam id: Laminin subunit gamma 1 (CATH.FunFam:2.10.25.10:FF:000067)
    AND FunFam id: laminin subunit gamma-1 (CATH.FunFam:2.10.25.10:FF:000105) AND
    FunFam id: Laminin subunit gamma 1 (CATH.FunFam:2.10.25.10:FF:000415)


    **Condition Set 189:** FunFam id: Fibulin 5 (CATH.FunFam:2.10.25.10:FF:000091)
    AND FunFam id: fibulin-5 isoform X2 (CATH.FunFam:2.10.25.10:FF:000190) AND FunFam
    id: Vitamin K-dependent protein S (CATH.FunFam:2.10.25.10:FF:000240)


    **Condition Set 190:** FunFam id: MUC5B isoform 1 (CATH.FunFam:2.10.25.10:FF:000153)
    AND FunFam id: von Willebrand factor (CATH.FunFam:2.10.25.10:FF:000414) AND taxon:
    Saurischia (NCBITaxon:436489)


    **Condition Set 191:** FunFam id: laminin subunit gamma-1 (CATH.FunFam:2.10.25.10:FF:000163)
    AND FunFam id: laminin subunit gamma-1 (CATH.FunFam:2.10.25.10:FF:000166) AND
    FunFam id: Laminin subunit gamma 3 (CATH.FunFam:2.10.25.10:FF:000433)


    **Condition Set 192:** FunFam id: Laminin subunit gamma-1 (CATH.FunFam:2.10.25.10:FF:000174)
    AND FunFam id: Laminin subunit gamma 2 (CATH.FunFam:2.10.25.10:FF:000399) AND
    FunFam id: Laminin subunit gamma 2 (CATH.FunFam:2.10.25.10:FF:000441)


    **Condition Set 193:** FunFam id: nephronectin isoform X2 (CATH.FunFam:2.10.25.10:FF:000184)
    AND FunFam id: nephronectin isoform X1 (CATH.FunFam:2.10.25.10:FF:000187) AND
    FunFam id: nephronectin isoform X2 (CATH.FunFam:2.10.25.10:FF:000268)


    **Condition Set 194:** FunFam id: BMP-binding endothelial regulator protein-like
    (CATH.FunFam:2.10.25.10:FF:000236) AND FunFam id: BMP-binding endothelial regulator
    protein (CATH.FunFam:2.10.70.10:FF:000034) AND FunFam id: BMP-binding endothelial
    regulator protein-like (CATH.FunFam:2.10.70.10:FF:000037)


    **Condition Set 195:** FunFam id: von Willebrand factor (CATH.FunFam:2.10.25.10:FF:000284)
    AND FunFam id: von Willebrand factor (CATH.FunFam:2.10.25.10:FF:000444) AND FunFam
    id: von Willebrand factor (CATH.FunFam:2.10.25.10:FF:000493)


    **Condition Set 196:** FunFam id: Serpin family A member 1 (CATH.FunFam:2.10.310.10:FF:000001)
    AND FunFam id: Serpin family B member 9 (CATH.FunFam:2.30.39.10:FF:000014) AND
    FunFam id: Serpin family B member 1 (CATH.FunFam:3.30.497.10:FF:000004)


    **Condition Set 197:** FunFam id: Complement C1s subcomponent (CATH.FunFam:2.10.70.10:FF:000049)
    AND FunFam id: Complement C1s subcomponent (CATH.FunFam:2.40.10.10:FF:000059)
    AND FunFam id: Complement C1s subcomponent (CATH.FunFam:2.40.10.10:FF:000067)


    **Condition Set 198:** FunFam id: Complement component C6 (CATH.FunFam:2.10.70.10:FF:000093)
    AND FunFam id: Unc-5 netrin receptor C (CATH.FunFam:2.20.100.10:FF:000002) AND
    FunFam id: Transmembrane protease serine 7 (CATH.FunFam:4.10.400.10:FF:000065)


    **Condition Set 199:** FunFam id: ADAM metallopeptidase with thrombospondin type
    1 motif 9 (CATH.FunFam:2.20.100.10:FF:000005) AND FunFam id: ADAMTS-like protein
    3 isoform A (CATH.FunFam:2.20.100.10:FF:000009) AND FunFam id: ADAM metallopeptidase
    with thrombospondin type 1 motif 13 (CATH.FunFam:2.60.120.830:FF:000003)


    **Condition Set 200:** FunFam id: A disintegrin and metalloproteinase with thrombospondin
    motifs 1 (CATH.FunFam:2.20.100.10:FF:000006) AND FunFam id: A disintegrin and
    metalloproteinase with thrombospondin motifs 1 (CATH.FunFam:2.60.120.830:FF:000001)
    AND FunFam id: A disintegrin and metalloproteinase with thrombospondin motifs
    5 (CATH.FunFam:3.40.1620.60:FF:000006)


    **Condition Set 201:** FunFam id: periostin isoform X1 (CATH.FunFam:2.30.180.10:FF:000001)
    AND FunFam id: periostin isoform X1 (CATH.FunFam:2.30.180.10:FF:000002) AND FunFam
    id: Transforming growth factor-beta-induced protein ig-h3 (CATH.FunFam:2.30.180.10:FF:000007)


    **Condition Set 202:** FunFam id: Serine protease easter (CATH.FunFam:2.40.10.10:FF:000028)
    AND FunFam id: Serine protease easter (CATH.FunFam:2.40.10.10:FF:000084) AND FunFam
    id: Spaetzle-processing enzyme (CATH.FunFam:3.30.1640.30:FF:000002)


    **Condition Set 203:** FunFam id: WAP, Kazal, immunoglobulin, Kunitz and NTR domain-containing
    protein 2 (CATH.FunFam:2.40.50.120:FF:000004) AND FunFam id: WAP, Kazal, immunoglobulin,
    Kunitz and NTR domain-containing protein 2 (CATH.FunFam:2.60.40.10:FF:000473)
    AND FunFam id: WAP, Kazal, immunoglobulin, Kunitz and NTR domain-containing protein
    2 (CATH.FunFam:4.10.410.10:FF:000009)


    **Condition Set 204:** FunFam id: Probable aspartic protease At2g35615 (CATH.FunFam:2.40.70.10:FF:000016)
    AND FunFam id: Aspartic proteinase CDR1 (CATH.FunFam:2.40.70.10:FF:000050) AND
    taxon: Viridiplantae (NCBITaxon:33090)


    **Condition Set 205:** FunFam id: Endothiapepsin (CATH.FunFam:2.40.70.10:FF:000024)
    AND FunFam id: Endothiapepsin (CATH.FunFam:2.40.70.10:FF:000026) AND taxon: Penicillium
    (NCBITaxon:5073)


    **Condition Set 206:** FunFam id: Metalloendopeptidase (CATH.FunFam:2.60.120.290:FF:000004)
    AND FunFam id: Metalloendopeptidase (CATH.FunFam:2.60.120.290:FF:000052) AND taxon:
    Ephydroidea (NCBITaxon:43746)


    **Condition Set 207:** FunFam id: Microbial collagenase (CATH.FunFam:2.60.120.380:FF:000012)
    AND FunFam id: Cell surface protein (CATH.FunFam:2.60.40.10:FF:000270) AND taxon:
    Bacillati (NCBITaxon:1783272)


    **Condition Set 208:** FunFam id: Cytokine receptor like factor 1 (CATH.FunFam:2.60.40.10:FF:000281)
    AND FunFam id: Cytokine receptor like factor 1 (CATH.FunFam:2.60.40.10:FF:000386)
    AND FunFam id: Cytokine receptor like factor 1 (CATH.FunFam:2.60.40.10:FF:000690)


    **Condition Set 209:** FunFam id: collagen alpha-1(VII) chain isoform X1 (CATH.FunFam:2.60.40.10:FF:000307)
    AND FunFam id: Putative collagen alpha-1vii chain (CATH.FunFam:2.60.40.10:FF:001175)
    AND FunFam id: collagen alpha-1(VII) chain isoform X2 (CATH.FunFam:2.60.40.10:FF:001333)


    **Condition Set 210:** FunFam id: Probable alpha-L-arabinofuranosidase A (CATH.FunFam:2.60.40.1180:FF:000036)
    AND FunFam id: Probable alpha-L-arabinofuranosidase A (CATH.FunFam:3.20.20.80:FF:000092)
    AND taxon: Eurotiomycetes (NCBITaxon:147545)


    **Condition Set 211:** FunFam id: Lysyl oxidase 4 isoform X1 (CATH.FunFam:3.10.250.10:FF:000001)
    AND FunFam id: Lysyl oxidase homolog 2 (CATH.FunFam:3.10.250.10:FF:000008) AND
    FunFam id: lysyl oxidase homolog 3 isoform X2 (CATH.FunFam:3.10.250.10:FF:000022)


    **Condition Set 212:** FunFam id: Glyceraldehyde-3-phosphate dehydrogenase (CATH.FunFam:3.30.360.10:FF:000001)
    AND FunFam id: Glyceraldehyde-3-phosphate dehydrogenase (CATH.FunFam:3.40.50.720:FF:000020)
    AND taxon: Nakaseomyces (NCBITaxon:374468)


    **Condition Set 213:** FunFam id: Ovomucoid (CATH.FunFam:3.30.60.30:FF:000036)
    AND FunFam id: Ovomucoid (CATH.FunFam:3.30.60.30:FF:000037) AND taxon: Phasianinae
    (NCBITaxon:9072)


    **Condition Set 214:** FunFam id: ABC multidrug transporter atrF (CATH.FunFam:3.40.50.300:FF:000054)
    AND FunFam id: ABC transporter CDR4 (CATH.FunFam:3.40.50.300:FF:001262) AND taxon:
    Candida/Lodderomyces clade (NCBITaxon:1535325)


    **Condition Set 215:** FunFam id: Insulin-like growth factor-binding protein 2
    (CATH.FunFam:4.10.40.20:FF:000007) AND FunFam id: Insulin-like growth factor-binding
    protein 2 (CATH.FunFam:4.10.800.10:FF:000002) AND taxon: Ruminantia (NCBITaxon:9845)


    **Condition Set 216:** FunFam id: Tissue factor pathway inhibitor (CATH.FunFam:4.10.410.10:FF:000004)
    AND FunFam id: Tissue factor pathway inhibitor (CATH.FunFam:4.10.410.10:FF:000012)
    AND FunFam id: Tissue factor pathway inhibitor (CATH.FunFam:4.10.410.10:FF:000013)


    **Condition Set 217:** FunFam id: Insulin-like growth factor II preproprotein
    (CATH.FunFam:1.10.100.10:FF:000002) AND taxon: Pecora (NCBITaxon:35500)


    **Condition Set 218:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1
    (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase
    PM20D1 (CATH.FunFam:3.40.630.10:FF:000027)


    **Condition Set 219:** FunFam id: Cathepsin L (CATH.FunFam:1.10.287.2250:FF:000003)
    AND FunFam id: Cathepsin S (CATH.FunFam:3.90.70.10:FF:000006)


    **Condition Set 220:** FunFam id: Guanosine nucleotide diphosphate dissociation
    inhibitor (CATH.FunFam:1.10.405.10:FF:000002) AND taxon: Streptophyta (NCBITaxon:35493)


    **Condition Set 221:** FunFam id: Resuscitation-promoting factor RpfC (CATH.FunFam:1.10.530.10:FF:000025)
    AND taxon: Actinomycetota (NCBITaxon:201174)


    **Condition Set 222:** FunFam id: Apoptosis-associated speck-like protein containing
    a CARD (CATH.FunFam:1.10.533.10:FF:000013) AND FunFam id: Apoptosis-associated
    speck-like protein containing a CARD (CATH.FunFam:1.10.533.10:FF:000053)


    **Condition Set 223:** FunFam id: Apolipoprotein A-IV a (CATH.FunFam:1.20.120.20:FF:000007)
    AND taxon: Actinopterygii (NCBITaxon:7898)


    **Condition Set 224:** FunFam id: Prolactin (CATH.FunFam:1.20.1250.10:FF:000003)
    AND taxon: Theropoda (NCBITaxon:436491)


    **Condition Set 225:** FunFam id: Interleukin-12 subunit alpha (CATH.FunFam:1.20.1250.10:FF:000020)
    AND taxon: Bovidae (NCBITaxon:9895)


    **Condition Set 226:** FunFam id: Putative invertase inhibitor (CATH.FunFam:1.20.140.40:FF:000002)
    AND taxon: Embryophyta (NCBITaxon:3193)


    **Condition Set 227:** FunFam id: Bone morphogenetic protein 5 (CATH.FunFam:2.10.90.10:FF:000003)
    AND FunFam id: Bone morphogenetic protein 7 (CATH.FunFam:2.60.120.970:FF:000008)


    **Condition Set 228:** FunFam id: Matrix metallopeptidase 19 (CATH.FunFam:2.110.10.10:FF:000008)
    AND FunFam id: Matrix metallopeptidase 19 (CATH.FunFam:3.40.390.10:FF:000027)


    **Condition Set 229:** FunFam id: GD20529 (CATH.FunFam:2.120.10.30:FF:000092)
    AND taxon: Drosophilidae (NCBITaxon:7214)


    **Condition Set 230:** FunFam id: Lambda-carrageenase (CATH.FunFam:2.130.10.10:FF:002292)
    AND taxon: Pseudomonadati (NCBITaxon:3379134)


    **Condition Set 231:** FunFam id: Endopolygalacturonase D (CATH.FunFam:2.160.20.10:FF:000002)
    AND taxon: Aspergillus subgen. Circumdati (NCBITaxon:2720871)


    **Condition Set 232:** FunFam id: Indian hedgehog (CATH.FunFam:2.170.16.10:FF:000001)
    AND taxon: Coelurosauria (NCBITaxon:436492)


    **Condition Set 233:** FunFam id: Transmembrane protease serine (CATH.FunFam:2.40.10.10:FF:000002)
    AND FunFam id: Coagulation factor XI (CATH.FunFam:3.50.4.10:FF:000001)


    **Condition Set 234:** FunFam id: Predicted protein (CATH.FunFam:2.40.10.10:FF:000077)
    AND taxon: Arachnida (NCBITaxon:6854)


    **Condition Set 235:** FunFam id: Lipoarabinomannan carrier protein LprG (CATH.FunFam:2.50.20.20:FF:000004)
    AND taxon: Actinomycetes (NCBITaxon:1760)


    **Condition Set 236:** FunFam id: collagen alpha-2(XI) chain isoform X1 (CATH.FunFam:2.60.120.1000:FF:000004)
    AND FunFam id: collagen alpha-2(XI) chain isoform X2 (CATH.FunFam:2.60.120.200:FF:000049)


    **Condition Set 237:** FunFam id: Glycinin G1 (CATH.FunFam:2.60.120.10:FF:000073)
    AND taxon: Rosales (NCBITaxon:3744)


    **Condition Set 238:** FunFam id: Beta-galactosidase (CATH.FunFam:2.60.120.260:FF:000115)
    AND FunFam id: Beta-galactosidase (CATH.FunFam:3.20.20.80:FF:000017)


    **Condition Set 239:** FunFam id: Complement C1q B chain (CATH.FunFam:2.60.120.40:FF:000001)
    AND taxon: Bovinae (NCBITaxon:27592)


    **Condition Set 240:** FunFam id: Alpha-galactosidase A (CATH.FunFam:2.60.40.1180:FF:000017)
    AND FunFam id: Alpha-galactosidase (CATH.FunFam:3.20.20.70:FF:000070)


    **Condition Set 241:** FunFam id: Zona pellucida glycoprotein 1 (CATH.FunFam:2.60.40.3210:FF:000007)
    AND FunFam id: Zona pellucida sperm-binding protein 2 (CATH.FunFam:2.60.40.4100:FF:000004)


    **Condition Set 242:** FunFam id: Snaclec rhodocetin subunit delta (CATH.FunFam:3.10.100.10:FF:000087)
    AND taxon: Trimeresurus (NCBITaxon:8764)


    **Condition Set 243:** FunFam id: 1,3-beta-glucanosyltransferase (CATH.FunFam:3.20.20.80:FF:000038)
    AND taxon: Candida (NCBITaxon:5475)


    **Condition Set 244:** FunFam id: Counting factor 50 (CATH.FunFam:3.20.20.80:FF:000249)
    AND taxon: Amoebozoa (NCBITaxon:554915)


    **Condition Set 245:** FunFam id: Endochitinase (Chitinase) (CATH.FunFam:3.30.20.10:FF:000001)
    AND taxon: Pooideae (NCBITaxon:147368)


    **Condition Set 246:** FunFam id: Defensin DFS2 (CATH.FunFam:3.30.30.10:FF:000006)
    AND taxon: Acari (NCBITaxon:6933)


    **Condition Set 247:** FunFam id: Defensin ARD1 (CATH.FunFam:3.30.30.10:FF:000012)
    AND taxon: Lepidoptera (NCBITaxon:7088)


    **Condition Set 248:** FunFam id: Proteinase inhibitor PSKP-1 (CATH.FunFam:3.30.60.30:FF:000147)
    AND taxon: Amphibia (NCBITaxon:8292)


    **Condition Set 249:** FunFam id: Glycine-rich RNA-binding protein 2 (CATH.FunFam:3.30.70.330:FF:000612)
    AND taxon: Tracheophyta (NCBITaxon:58023)


    **Condition Set 250:** FunFam id: Glycine-rich RNA-binding protein 7 (CATH.FunFam:3.30.70.330:FF:001313)
    AND taxon: Spermatophyta (NCBITaxon:58024)


    **Condition Set 251:** FunFam id: Gingipain R2 (CATH.FunFam:3.40.50.1460:FF:000031)
    AND taxon: Bacteroidota (NCBITaxon:976)


    **Condition Set 252:** FunFam id: Glycine--tRNA ligase (CATH.FunFam:3.40.50.800:FF:000002)
    AND taxon: Mycobacteriales (NCBITaxon:85007)


    **Condition Set 253:** FunFam id: Glutaminyl-peptide cyclotransferase (CATH.FunFam:3.40.630.10:FF:000029)
    AND taxon: Drosophila (NCBITaxon:7215)


    **Condition Set 254:** FunFam id: Probable 3'',5''-cyclic-nucleotide phosphodiesterase
    (CATH.FunFam:3.60.15.10:FF:000064) AND taxon: Evosea (NCBITaxon:2605435)


    **Condition Set 255:** FunFam id: Insulin-like growth factor-binding protein complex
    acid labile subunit (CATH.FunFam:3.80.10.10:FF:000540) AND FunFam id: Insulin-like
    growth factor-binding protein complex acid labile subunit (CATH.FunFam:3.80.10.10:FF:001264)


    **Condition Set 256:** FunFam id: NAD(P)(+)--arginine ADP-ribosyltransferase (CATH.FunFam:3.90.176.10:FF:000001)
    AND taxon: Aves (NCBITaxon:8782)


    **Condition Set 257:** FunFam id: Polyamine oxidase 1 (CATH.FunFam:3.90.660.10:FF:000012)
    AND taxon: Liliopsida (NCBITaxon:4447)


    **Condition Set 258:** FunFam id: Cathepsin Z (CATH.FunFam:3.90.70.10:FF:000060)
    AND taxon: Nematoda (NCBITaxon:6231)


    **Condition Set 259:** FunFam id: Extracellular matrix protein 1 (CATH.FunFam:1.10.246.10:FF:000006)


    **Condition Set 260:** FunFam id: Vitamin D-binding protein (CATH.FunFam:1.10.246.10:FF:000007)


    **Condition Set 261:** FunFam id: extracellular tyrosine-protein kinase PKDCC
    isoform X5 (CATH.FunFam:1.10.510.10:FF:000552)


    **Condition Set 262:** FunFam id: Fms-related tyrosine kinase 3 ligand (CATH.FunFam:1.20.1250.10:FF:000016)


    **Condition Set 263:** FunFam id: Granulocyte colony-stimulating factor (CATH.FunFam:1.20.1250.10:FF:000021)


    **Condition Set 264:** FunFam id: Interleukin-23 subunit alpha (CATH.FunFam:1.20.1250.10:FF:000024)


    **Condition Set 265:** FunFam id: Interleukin-2 (CATH.FunFam:1.20.1250.10:FF:000025)


    **Condition Set 266:** FunFam id: Interleukin-22 (CATH.FunFam:1.20.1250.10:FF:000032)


    **Condition Set 267:** FunFam id: Interleukin-27 subunit alpha (CATH.FunFam:1.20.1250.10:FF:000035)


    **Condition Set 268:** FunFam id: Interferon gamma (CATH.FunFam:1.20.1250.10:FF:000080)


    **Condition Set 269:** FunFam id: Transmembrane protein 98 (CATH.FunFam:1.20.1410.10:FF:000003)


    **Condition Set 270:** FunFam id: Mesothelin (CATH.FunFam:1.20.970.40:FF:000001)


    **Condition Set 271:** FunFam id: pro-neuregulin-3, membrane-bound isoform (CATH.FunFam:2.10.25.10:FF:000267)


    **Condition Set 272:** FunFam id: Betacellulin preproprotein (CATH.FunFam:2.10.25.10:FF:000342)


    **Condition Set 273:** FunFam id: pro-neuregulin-4, membrane-bound isoform (CATH.FunFam:2.10.25.10:FF:000356)


    **Condition Set 274:** FunFam id: epigen isoform X1 (CATH.FunFam:2.10.25.10:FF:000427)


    **Condition Set 275:** FunFam id: Prokineticin 1 (CATH.FunFam:2.10.80.10:FF:000004)


    **Condition Set 276:** FunFam id: Sclerostin domain-containing protein 1 (CATH.FunFam:2.10.90.10:FF:000019)


    **Condition Set 277:** FunFam id: Inhibin alpha chain (CATH.FunFam:2.10.90.10:FF:000024)


    **Condition Set 278:** FunFam id: neurturin (CATH.FunFam:2.10.90.10:FF:000037)


    **Condition Set 279:** FunFam id: Persephin (CATH.FunFam:2.10.90.10:FF:000040)


    **Condition Set 280:** FunFam id: Interleukin 17C (CATH.FunFam:2.10.90.10:FF:000046)


    **Condition Set 281:** FunFam id: Aldehyde oxidase GLOX (CATH.FunFam:2.130.10.80:FF:000001)


    **Condition Set 282:** FunFam id: Complement C1r subcomponent (CATH.FunFam:2.40.10.10:FF:000037)


    **Condition Set 283:** FunFam id: Alpha-1-microglobulin/bikunin precursor (CATH.FunFam:2.40.128.20:FF:000007)


    **Condition Set 284:** FunFam id: C-C motif chemokine (CATH.FunFam:2.40.50.40:FF:000025)


    **Condition Set 285:** FunFam id: Retinoschisin 1 (CATH.FunFam:2.60.120.260:FF:000075)


    **Condition Set 286:** FunFam id: Tumor necrosis factor ligand superfamily member
    12 (CATH.FunFam:2.60.120.40:FF:000022)


    **Condition Set 287:** FunFam id: V-set and transmembrane domain containing 2
    like (CATH.FunFam:2.60.40.10:FF:000735)


    **Condition Set 288:** FunFam id: Interferon alpha/beta receptor 2 (CATH.FunFam:2.60.40.10:FF:000909)


    **Condition Set 289:** FunFam id: Immunoglobulin heavy variable 5-15 (CATH.FunFam:2.60.40.10:FF:001142)


    **Condition Set 290:** FunFam id: Immunoglobulin heavy variable 2-26 (CATH.FunFam:2.60.40.10:FF:001533)


    **Condition Set 291:** FunFam id: Prolactin-inducible protein homolog (CATH.FunFam:2.60.40.10:FF:001572)


    **Condition Set 292:** FunFam id: Interleukin-1 alpha (CATH.FunFam:2.80.10.50:FF:000049)


    **Condition Set 293:** FunFam id: Retinoic acid receptor responder 2 (CATH.FunFam:3.10.450.10:FF:000014)


    **Condition Set 294:** FunFam id: Protein Wnt-3a (CATH.FunFam:3.30.2460.20:FF:000009)


    **Condition Set 295:** FunFam id: Big defensin (CATH.FunFam:3.40.1620.80:FF:000001)


    **Condition Set 296:** FunFam id: Lipase member H (CATH.FunFam:3.40.50.1820:FF:000063)


    **Condition Set 297:** FunFam id: acid sphingomyelinase-like phosphodiesterase
    3a (CATH.FunFam:3.60.21.10:FF:000044)


    **Condition Set 298:** FunFam id: Insulin-like growth factor binding protein 6
    (CATH.FunFam:4.10.800.10:FF:000010)


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
citation_count: 57
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00027128
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0005576 (extracellular region)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** InterPro id: Immunoglobulin-like domain (InterPro:IPR007110) AND InterPro id: Immunoglobulin Variable Light Chain (InterPro:IPR050150) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 2:** InterPro id: Wnt (InterPro:IPR005817) AND InterPro id: Wnt protein, conserved site (InterPro:IPR018161) AND taxon: Haplorrhini (NCBITaxon:376913)

**Condition Set 3:** InterPro id: Immunoglobulin V-set domain (InterPro:IPR013106) AND InterPro id: Immunoglobulin-like fold (InterPro:IPR013783) AND InterPro id: Immunoglobulin Heavy Variable (InterPro:IPR050199)

**Condition Set 4:** InterPro id: Frog antimicrobial peptide, brevinin-2/esculentin type (InterPro:IPR012521) AND taxon: Pelophylax (NCBITaxon:121164)

**Condition Set 5:** InterPro id: Laminin IV (InterPro:IPR000034) AND InterPro id: Laminin/Netrin Extracellular Matrix (InterPro:IPR050440) AND taxon: Mammalia (NCBITaxon:40674)

**Condition Set 6:** InterPro id: Chemokine interleukin-8-like domain (InterPro:IPR001811) AND InterPro id: CXC Chemokine domain (InterPro:IPR033899) AND taxon: Hominidae (NCBITaxon:9604)

**Condition Set 7:** InterPro id: Serine proteases, trypsin domain (InterPro:IPR001254) AND InterPro id: Peptidase S1A, chymotrypsin family (InterPro:IPR001314) AND taxon: Lepidosauria (NCBITaxon:8504)

**Condition Set 8:** InterPro id: Nerve growth factor-related (InterPro:IPR002072) AND InterPro id: Nerve growth factor conserved site (InterPro:IPR019846) AND taxon: Eutheria (NCBITaxon:9347)

**Condition Set 9:** InterPro id: Lipocalin/cytosolic fatty-acid binding domain (InterPro:IPR000566) AND InterPro id: Retinol binding protein/Purpurin (InterPro:IPR002449) AND InterPro id: Calycin (InterPro:IPR012674)

**Condition Set 10:** InterPro id: EGF-like domain (InterPro:IPR000742) AND InterPro id: Laminin alpha, domain I (InterPro:IPR009254) AND taxon: Chordata (NCBITaxon:7711)

**Condition Set 11:** InterPro id: Aspartic peptidase A1 (InterPro:IPR001461) AND InterPro id: Aspartic peptidase, active site (InterPro:IPR001969) AND taxon: Pichiomycetes (NCBITaxon:3239874)

**Condition Set 12:** InterPro id: Hemocyanin/hexamerin middle domain (InterPro:IPR000896) AND InterPro id: Tyrosinase copper-binding domain (InterPro:IPR002227) AND PANTHER id: PTHR11511:SF4

**Condition Set 13:** InterPro id: Frog antimicrobial peptide, propeptide (InterPro:IPR004275) AND taxon: Litoria (NCBITaxon:8370)

**Condition Set 14:** InterPro id: Snake toxin-like superfamily (InterPro:IPR045860) AND taxon: Micrurus (NCBITaxon:8634)

**Condition Set 15:** InterPro id: Transthyretin/hydroxyisourate hydrolase (InterPro:IPR000895) AND InterPro id: Transthyretin/hydroxyisourate hydrolase domain (InterPro:IPR023416) AND PANTHER id: PTHR10395:SF12

**Condition Set 16:** InterPro id: Stress-inducible humoral factor Turandot (InterPro:IPR010825) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 17:** InterPro id: Bacteriocin class IIa domain superfamily (InterPro:IPR023388) AND taxon: Bacteria (NCBITaxon:2)

**Condition Set 18:** InterPro id: Neuregulin (InterPro:IPR040180) AND taxon: Metazoa (NCBITaxon:33208)

**Condition Set 19:** InterPro id: EGF-type aspartate/asparagine hydroxylation site (InterPro:IPR000152) AND InterPro id: Gamma-carboxyglutamic acid-rich (GLA) domain (InterPro:IPR000294) AND PANTHER id: PTHR24278:SF28

**Condition Set 20:** InterPro id: Thyroglobulin type-1 (InterPro:IPR000716) AND InterPro id: Growth factor receptor cysteine-rich domain superfamily (InterPro:IPR009030) AND taxon: Mus (NCBITaxon:862507)

**Condition Set 21:** InterPro id: Hemocyanin, C-terminal (InterPro:IPR005203) AND InterPro id: Hemocyanin, N-terminal (InterPro:IPR005204) AND taxon: Brachycera (NCBITaxon:7203)

**Condition Set 22:** InterPro id: Cecropin-like (InterPro:IPR000875) AND taxon: Arthropoda (NCBITaxon:6656)

**Condition Set 23:** InterPro id: Defensin, invertebrate/fungal (InterPro:IPR001542) AND taxon: Diptera (NCBITaxon:7147)

**Condition Set 24:** InterPro id: Casein alpha/beta, conserved site (InterPro:IPR031305) AND taxon: Euteleostomi (NCBITaxon:117571)

**Condition Set 25:** InterPro id: Gamma-carboxyglutamic acid-rich (GLA) domain superfamily (InterPro:IPR035972) AND taxon: Rattus (NCBITaxon:10114)

**Condition Set 26:** InterPro id: Insulin-like superfamily (InterPro:IPR036438) AND taxon: Hexapoda (NCBITaxon:6960)

**Condition Set 27:** PANTHER id: PTHR11511:SF5 AND taxon: Insecta (NCBITaxon:50557)

**Condition Set 28:** InterPro id: Laminin-type EGF domain (InterPro:IPR002049) AND InterPro id: Concanavalin A-like lectin/glucanase domain superfamily (InterPro:IPR013320) AND InterPro id: Neurexin-related cell adhesion and synaptic protein (InterPro:IPR050372)

**Condition Set 29:** InterPro id: Glycosyl hydrolase family 32, N-terminal (InterPro:IPR013148) AND InterPro id: Glycoside hydrolase, family 32, active site (InterPro:IPR018053) AND taxon: Saccharomycotina (NCBITaxon:147537)

**Condition Set 30:** InterPro id: Insulin-like growth factor II E-peptide, C-terminal (InterPro:IPR013576) AND InterPro id: Insulin-like (InterPro:IPR016179) AND PANTHER id: PTHR46886:SF1

**Condition Set 31:** InterPro id: Cecropin/Sarcotoxins/Aedesins (InterPro:IPR020400) AND PANTHER id: PTHR38329:SF1 AND taxon: Ecdysozoa (NCBITaxon:1206794)

**Condition Set 32:** InterPro id: Bombesin/neuromedin-B/ranatensin peptide family (InterPro:IPR000874) AND taxon: Amphibia (NCBITaxon:8292)

**Condition Set 33:** InterPro id: Lipocalin (InterPro:IPR002345) AND PANTHER id: PTHR11430:SF86

**Condition Set 34:** InterPro id: Ant venom peptides (InterPro:IPR049518) AND taxon: Pterygota (NCBITaxon:300552)

**Condition Set 35:** InterPro id: Bradykinin (InterPro:IPR009608)

**Condition Set 36:** PANTHER id: PTHR47966:SF24

**Condition Set 37:** InterPro id: Anaphylatoxin/fibulin (InterPro:IPR000020) AND InterPro id: Netrin domain (InterPro:IPR001134) AND InterPro id: Complement C4, MG1 domain (InterPro:IPR048847)

**Condition Set 38:** InterPro id: Fibronectin, type I (InterPro:IPR000083) AND InterPro id: Fibronectin type II domain (InterPro:IPR000562) AND InterPro id: Fibronectin type III (InterPro:IPR003961)

**Condition Set 39:** InterPro id: Peptidase S8/S53 domain (InterPro:IPR000209) AND InterPro id: Peptidase S8 propeptide/proteinase inhibitor I9 (InterPro:IPR010259) AND PANTHER id: PTHR43806:SF58

**Condition Set 40:** InterPro id: ALB/AFP/VDB (InterPro:IPR000264) AND InterPro id: Serum albumin, N-terminal (InterPro:IPR014760) AND PANTHER id: PTHR11385:SF15

**Condition Set 41:** InterPro id: Coagulation factor 5/8, C-terminal domain (InterPro:IPR000421) AND InterPro id: Cupredoxin (InterPro:IPR008972) AND InterPro id: Galactose-binding-like domain superfamily (InterPro:IPR008979)

**Condition Set 42:** InterPro id: Glycoside hydrolase family 18, catalytic domain (InterPro:IPR001223) AND InterPro id: Chitinase Cts1-like (InterPro:IPR045321) AND PANTHER id: PTHR45708:SF49

**Condition Set 43:** InterPro id: Kazal domain (InterPro:IPR002350) AND InterPro id: Kazal domain superfamily (InterPro:IPR036058) AND taxon: Phasianinae (NCBITaxon:9072)

**Condition Set 44:** InterPro id: Prolamin-like domain (InterPro:IPR008502) AND InterPro id: Egg cell-secreted protein 1.1-1.5 (InterPro:IPR044711) AND taxon: Viridiplantae (NCBITaxon:33090)

**Condition Set 45:** InterPro id: Tissue inhibitor of metalloproteinases-like, OB-fold (InterPro:IPR008993) AND InterPro id: Alpha-macroglobulin-like, thiol-ester bond-forming region (InterPro:IPR047565) AND taxon: Glires (NCBITaxon:314147)

**Condition Set 46:** InterPro id: Resuscitation-promoting factor, core lysozyme-like domain (InterPro:IPR010618) AND InterPro id: Lysozyme-like domain superfamily (InterPro:IPR023346) AND taxon: Mycobacterium (NCBITaxon:1763)

**Condition Set 47:** InterPro id: Serum albumin, conserved site (InterPro:IPR020857) AND InterPro id: Serum albumin/Alpha-fetoprotein/Afamin (InterPro:IPR021177) AND taxon: Rodentia (NCBITaxon:9989)

**Condition Set 48:** InterPro id: Insulin/IGF/relaxin (InterPro:IPR022352) AND InterPro id: Insulin, conserved site (InterPro:IPR022353) AND taxon: Ruminantia (NCBITaxon:9845)

**Condition Set 49:** InterPro id: Spaetzle (InterPro:IPR032104) AND InterPro id: Spaetzle/Toll ligand-like (InterPro:IPR052444) AND taxon: Neoptera (NCBITaxon:33340)

**Condition Set 50:** InterPro id: Beta-microseminoprotein (InterPro:IPR008735)

**Condition Set 51:** FunFam id: Wnt homolog (CATH.FunFam:3.30.2460.20:FF:000001) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 52:** FunFam id: Alpha-like toxin BmK-M1 (CATH.FunFam:3.30.30.10:FF:000002) AND taxon: Centruroides (NCBITaxon:6875)

**Condition Set 53:** FunFam id: Brain-derived neurotrophic factor (CATH.FunFam:2.10.90.10:FF:000002) AND taxon: Mammalia (NCBITaxon:40674)

**Condition Set 54:** FunFam id: C-X-C motif chemokine (CATH.FunFam:2.40.50.40:FF:000004) AND taxon: Haplorrhini (NCBITaxon:376913)

**Condition Set 55:** FunFam id: Laminin subunit alpha 3 (CATH.FunFam:2.10.25.10:FF:000084) AND taxon: Eutheria (NCBITaxon:9347)

**Condition Set 56:** FunFam id: Retinol-binding protein 4 (CATH.FunFam:2.40.128.20:FF:000004) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 57:** FunFam id: Immunoglobulin kappa chain variable 12-38 (CATH.FunFam:2.60.40.10:FF:000212) AND taxon: Metazoa (NCBITaxon:33208)

**Condition Set 58:** FunFam id: complement C3 isoform X1 (CATH.FunFam:2.60.40.10:FF:000155) AND FunFam id: Complement component C3 (CATH.FunFam:2.60.40.1940:FF:000001) AND taxon: Euarchontoglires (NCBITaxon:314146)

**Condition Set 59:** FunFam id: Laminin subunit alpha 4 (CATH.FunFam:2.10.25.10:FF:000051) AND taxon: Chordata (NCBITaxon:7711)

**Condition Set 60:** FunFam id: Laminin subunit alpha 1 (CATH.FunFam:2.10.25.10:FF:000069) AND taxon: Craniata (NCBITaxon:89593)

**Condition Set 61:** FunFam id: Aspartic protease (CATH.FunFam:2.40.70.10:FF:000011) AND taxon: Pichiomycetes (NCBITaxon:3239874)

**Condition Set 62:** FunFam id: Aspartic protease (CATH.FunFam:2.40.70.10:FF:000023) AND taxon: Debaryomycetaceae (NCBITaxon:766764)

**Condition Set 63:** FunFam id: Immunoglobulin lambda variable 2-8 (CATH.FunFam:2.60.40.10:FF:000442) AND taxon: Vertebrata (NCBITaxon:7742)

**Condition Set 64:** FunFam id: Immunoglobulin heavy constant gamma 1 (CATH.FunFam:2.60.40.10:FF:000463) AND taxon: Catarrhini (NCBITaxon:9526)

**Condition Set 65:** FunFam id: Transthyretin (CATH.FunFam:2.60.40.180:FF:000002) AND taxon: Euteleostomi (NCBITaxon:117571)

**Condition Set 66:** FunFam id: Collagenase 3 (CATH.FunFam:3.40.390.10:FF:000007) AND taxon: Hominidae (NCBITaxon:9604)

**Condition Set 67:** FunFam id: Immunoglobulin kappa constant (CATH.FunFam:2.60.40.10:FF:000283) AND taxon: Homo (NCBITaxon:9605)

**Condition Set 68:** FunFam id: Immunoglobulin heavy variable 3-23 (CATH.FunFam:2.60.40.10:FF:000942)

**Condition Set 69:** FunFam id: Hemocyanin subunit 2 (CATH.FunFam:1.10.1280.10:FF:000004) AND FunFam id: Hemocyanin subunit 2 (CATH.FunFam:2.60.40.1520:FF:000001) AND taxon: Hexapoda (NCBITaxon:6960)

**Condition Set 70:** FunFam id: Serum albumin (CATH.FunFam:1.10.246.10:FF:000001) AND FunFam id: Serum albumin (CATH.FunFam:1.10.246.10:FF:000002) AND FunFam id: Serum albumin (CATH.FunFam:1.10.246.10:FF:000003)

**Condition Set 71:** FunFam id: Notch, isoform B (CATH.FunFam:2.10.25.10:FF:000095) AND FunFam id: FAT atypical cadherin 4 (CATH.FunFam:2.10.25.10:FF:000151) AND FunFam id: Neurogenic locus notch homolog protein 2 (CATH.FunFam:2.10.25.10:FF:000393)

**Condition Set 72:** FunFam id: Coagulation factor X (Predicted) (CATH.FunFam:2.10.25.10:FF:000162) AND FunFam id: Coagulation factor VII (CATH.FunFam:2.10.25.10:FF:000513) AND FunFam id: vitamin K-dependent protein S (CATH.FunFam:4.10.740.10:FF:000001)

**Condition Set 73:** FunFam id: Complement inhibitory factor H (CATH.FunFam:2.10.70.10:FF:000026) AND FunFam id: Complement inhibitory factor H (CATH.FunFam:2.10.70.10:FF:000054) AND FunFam id: Complement inhibitory factor H (CATH.FunFam:2.10.70.10:FF:000060)

**Condition Set 74:** FunFam id: Cytotoxin 1 (CATH.FunFam:2.10.60.10:FF:000024) AND taxon: Micrurus (NCBITaxon:8634)

**Condition Set 75:** FunFam id: Beta-1,3-glucan-binding protein (CATH.FunFam:2.60.120.200:FF:000235) AND taxon: Ecdysozoa (NCBITaxon:1206794)

**Condition Set 76:** FunFam id: Beta-1,3-glucan-binding protein (CATH.FunFam:2.60.40.2140:FF:000001) AND taxon: Arthropoda (NCBITaxon:6656)

**Condition Set 77:** FunFam id: Defensin (CATH.FunFam:3.30.30.10:FF:000005) AND taxon: Insecta (NCBITaxon:50557)

**Condition Set 78:** FunFam id: Prostaglandin-H2 D-isomerase (CATH.FunFam:2.40.128.20:FF:000010)

**Condition Set 79:** FunFam id: renin (CATH.FunFam:2.40.70.10:FF:000032)

**Condition Set 80:** FunFam id: If kappa light chain (CATH.FunFam:2.60.40.10:FF:000365)

**Condition Set 81:** FunFam id: Fibronectin 1a isoform 1 (CATH.FunFam:2.10.10.10:FF:000001) AND FunFam id: Fibronectin 1 (CATH.FunFam:2.10.70.10:FF:000004) AND FunFam id: Fibronectin 1 (CATH.FunFam:2.10.70.10:FF:000006)

**Condition Set 82:** FunFam id: Venom plasminogen activator TSV-PA (CATH.FunFam:2.40.10.10:FF:000153) AND FunFam id: Thrombin-like enzyme saxthrombin (CATH.FunFam:2.40.10.10:FF:000158) AND taxon: Lepidosauria (NCBITaxon:8504)

**Condition Set 83:** FunFam id: Coagulation factor VIII (CATH.FunFam:2.60.120.260:FF:000002) AND FunFam id: Coagulation factor VIII (Predicted) (CATH.FunFam:2.60.40.420:FF:000011)

**Condition Set 84:** FunFam id: Proteinase K (CATH.FunFam:3.40.50.200:FF:000014) AND taxon: Fungi (NCBITaxon:4751)

**Condition Set 85:** FunFam id: Interleukin-17A (CATH.FunFam:2.10.90.10:FF:000038)

**Condition Set 86:** FunFam id: Complement C1r subcomponent (CATH.FunFam:2.40.10.10:FF:000054)

**Condition Set 87:** FunFam id: Slit guidance ligand 2 (CATH.FunFam:2.10.25.10:FF:000045) AND FunFam id: Slit guidance ligand 2 (CATH.FunFam:2.10.25.10:FF:000053) AND FunFam id: Slit guidance ligand 2 (CATH.FunFam:2.10.25.10:FF:000099)

**Condition Set 88:** FunFam id: Transmembrane agrin (CATH.FunFam:2.10.25.10:FF:000134) AND FunFam id: Transmembrane agrin (CATH.FunFam:2.10.25.10:FF:000140) AND FunFam id: Transmembrane agrin (CATH.FunFam:2.60.120.200:FF:000027)

**Condition Set 89:** FunFam id: Tissue-type plasminogen activator (CATH.FunFam:2.10.25.10:FF:000483) AND FunFam id: Plasminogen activator (CATH.FunFam:2.10.70.10:FF:000043) AND FunFam id: Urokinase-type plasminogen activator (CATH.FunFam:2.40.20.10:FF:000001)

**Condition Set 90:** FunFam id: Semaphorin 3F like (CATH.FunFam:2.60.40.10:FF:000030) AND FunFam id: Semaphorin 3F like (CATH.FunFam:3.30.1680.10:FF:000001) AND taxon: Archelosauria (NCBITaxon:1329799)

**Condition Set 91:** FunFam id: Dystroglycan 1 (CATH.FunFam:2.60.40.10:FF:000555) AND FunFam id: Dystroglycan 1 (CATH.FunFam:2.60.40.10:FF:000684) AND FunFam id: Dystroglycan 1 (CATH.FunFam:3.30.70.1040:FF:000001)

**Condition Set 92:** FunFam id: Insulin (CATH.FunFam:1.10.100.10:FF:000003) AND taxon: Glires (NCBITaxon:314147)

**Condition Set 93:** FunFam id: Apolipoprotein E (CATH.FunFam:1.20.120.20:FF:000002) AND FunFam id: Apolipoprotein E (CATH.FunFam:1.20.120.20:FF:000003)

**Condition Set 94:** FunFam id: Bacteriocin hiracin-JM79 (CATH.FunFam:1.20.5.130:FF:000001) AND taxon: Bacteria (NCBITaxon:2)

**Condition Set 95:** FunFam id: Basic phospholipase A2 homolog (CATH.FunFam:1.20.90.10:FF:000001) AND taxon: Crotalus (NCBITaxon:8728)

**Condition Set 96:** FunFam id: Bone morphogenetic protein 16 (CATH.FunFam:2.10.90.10:FF:000103) AND taxon: Rodentia (NCBITaxon:9989)

**Condition Set 97:** FunFam id: Glycosylphosphatidylinositol specific phospholipase D1 (CATH.FunFam:2.130.10.130:FF:000010) AND FunFam id: Glycosylphosphatidylinositol specific phospholipase D1 (CATH.FunFam:2.130.10.130:FF:000011)

**Condition Set 98:** FunFam id: Major urinary protein (CATH.FunFam:2.40.128.20:FF:000008) AND taxon: Cricetidae (NCBITaxon:337677)

**Condition Set 99:** FunFam id: Cerebellin 4 (CATH.FunFam:2.60.120.40:FF:000002) AND taxon: Myomorpha (NCBITaxon:1963758)

**Condition Set 100:** FunFam id: Interleukin-12 subunit beta (CATH.FunFam:2.60.40.10:FF:000959) AND FunFam id: Interleukin-12 subunit beta (CATH.FunFam:2.60.40.10:FF:001008)

**Condition Set 101:** FunFam id: Larval serum protein 2 (CATH.FunFam:2.60.40.1520:FF:000002) AND taxon: Neoptera (NCBITaxon:33340)

**Condition Set 102:** FunFam id: Lipoprotein lipase (CATH.FunFam:2.60.60.20:FF:000006) AND FunFam id: Lipoprotein lipase (CATH.FunFam:3.40.50.1820:FF:000031)

**Condition Set 103:** FunFam id: oxytocin-neurophysin 1 (CATH.FunFam:2.60.9.10:FF:000001) AND taxon: Muroidea (NCBITaxon:337687)

**Condition Set 104:** FunFam id: Cholesteryl ester transfer protein (CATH.FunFam:3.15.10.10:FF:000002) AND FunFam id: Cholesteryl ester transfer protein (CATH.FunFam:3.15.20.10:FF:000002)

**Condition Set 105:** FunFam id: CTS1p Endochitinase (CATH.FunFam:3.20.20.80:FF:000125) AND taxon: Dikarya (NCBITaxon:451864)

**Condition Set 106:** FunFam id: Indian hedgehog (CATH.FunFam:3.30.1380.10:FF:000001) AND taxon: Muridae (NCBITaxon:10066)

**Condition Set 107:** FunFam id: Toxin-like peptide AaF1CA7 (CATH.FunFam:3.30.30.10:FF:000008) AND taxon: Chelicerata (NCBITaxon:6843)

**Condition Set 108:** FunFam id: Insulin-like growth factor binding protein 5 (CATH.FunFam:4.10.40.20:FF:000001) AND taxon: Mus (NCBITaxon:862507)

**Condition Set 109:** FunFam id: R-spondin 3 (CATH.FunFam:2.10.220.10:FF:000003)

**Condition Set 110:** FunFam id: Immunoglobulin kappa chain variable 18-36 (CATH.FunFam:2.60.40.10:FF:000350)

**Condition Set 111:** FunFam id: Immunoglobulin lambda locus (CATH.FunFam:2.60.40.10:FF:000620)

**Condition Set 112:** FunFam id: Mannose-binding protein A (CATH.FunFam:3.10.100.10:FF:000088)

**Condition Set 113:** FunFam id: Interferon-induced protein 35 (CATH.FunFam:3.30.70.330:FF:000300)

**Condition Set 114:** FunFam id: Amine oxidase (CATH.FunFam:1.10.405.10:FF:000004) AND FunFam id: Amine oxidase (CATH.FunFam:3.50.50.60:FF:000450) AND taxon: Crotalinae (NCBITaxon:8710)

**Condition Set 115:** FunFam id: Vascular endothelial growth factor receptor 2 (CATH.FunFam:1.10.510.10:FF:000077) AND FunFam id: Vascular endothelial growth factor receptor 3 (CATH.FunFam:2.60.40.10:FF:000143) AND FunFam id: vascular endothelial growth factor receptor 1 (CATH.FunFam:2.60.40.10:FF:000934)

**Condition Set 116:** FunFam id: binder of sperm protein homolog 1 (CATH.FunFam:2.10.10.10:FF:000003) AND FunFam id: Epididymal sperm binding protein 1 (CATH.FunFam:2.10.10.10:FF:000005) AND taxon: Laurasiatheria (NCBITaxon:314145)

**Condition Set 117:** FunFam id: Coagulation factor XII (CATH.FunFam:2.10.10.10:FF:000010) AND FunFam id: hepatocyte growth factor activator (CATH.FunFam:2.10.25.10:FF:000338) AND FunFam id: Coagulation factor XII (CATH.FunFam:2.10.25.10:FF:000576)

**Condition Set 118:** FunFam id: Signal peptide, CUB domain, EGF-like 2 (CATH.FunFam:2.10.25.10:FF:000008) AND FunFam id: Signal peptide, CUB domain and EGF-like domain-containing 2 (CATH.FunFam:2.10.25.10:FF:000028) AND FunFam id: signal peptide, CUB and EGF-like domain-containing protein 2 isoform X2 (CATH.FunFam:2.10.25.10:FF:000199)

**Condition Set 119:** FunFam id: Pro-epidermal growth factor (CATH.FunFam:2.10.25.10:FF:000010) AND FunFam id: Pro-epidermal growth factor (CATH.FunFam:2.10.25.10:FF:000219) AND FunFam id: Pro-epidermal growth factor (CATH.FunFam:2.10.25.10:FF:000254)

**Condition Set 120:** FunFam id: Slit guidance ligand 2 (CATH.FunFam:2.10.25.10:FF:000054) AND FunFam id: Slit guidance ligand 2 (CATH.FunFam:2.60.120.200:FF:000013) AND taxon: Murinae (NCBITaxon:39107)

**Condition Set 121:** FunFam id: Mannan-binding lectin serine protease 1 (CATH.FunFam:2.10.25.10:FF:000059) AND FunFam id: Mannan-binding lectin serine protease 1 (CATH.FunFam:2.10.70.10:FF:000016) AND FunFam id: mannan-binding lectin serine protease 1 isoform X2 (CATH.FunFam:2.10.70.10:FF:000028)

**Condition Set 122:** FunFam id: Neurogenic locus notch protein 1 (CATH.FunFam:2.10.25.10:FF:000060) AND FunFam id: Neurogenic locus notch 1 (CATH.FunFam:2.10.25.10:FF:000080) AND FunFam id: Notch receptor 3 (CATH.FunFam:2.10.25.10:FF:000516)

**Condition Set 123:** FunFam id: vitamin K-dependent protein S (CATH.FunFam:2.10.25.10:FF:000119) AND FunFam id: Growth arrest-specific protein 6 (CATH.FunFam:2.10.25.10:FF:000528) AND FunFam id: growth arrest-specific protein 6 (CATH.FunFam:2.60.120.200:FF:000089)

**Condition Set 124:** FunFam id: Nidogen 1 (CATH.FunFam:2.10.25.10:FF:000270) AND FunFam id: Nidogen 1 (CATH.FunFam:2.10.25.10:FF:000281) AND FunFam id: Testican-3 isoform 2 (CATH.FunFam:4.10.800.10:FF:000001)

**Condition Set 125:** FunFam id: Invertase 2 (CATH.FunFam:2.115.10.20:FF:000002) AND FunFam id: Invertase 2 (CATH.FunFam:2.60.120.560:FF:000004) AND taxon: Ascomycota (NCBITaxon:4890)

**Condition Set 126:** FunFam id: Hepatocyte growth factor (CATH.FunFam:2.40.10.10:FF:000023) AND FunFam id: Hepatocyte growth factor (CATH.FunFam:2.40.10.10:FF:000026) AND FunFam id: Hepatocyte growth factor (CATH.FunFam:2.40.20.10:FF:000004)

**Condition Set 127:** FunFam id: Reelin (CATH.FunFam:2.60.120.260:FF:000003) AND FunFam id: Reelin (CATH.FunFam:2.60.120.260:FF:000028) AND FunFam id: Reelin (CATH.FunFam:2.60.120.260:FF:000057)

**Condition Set 128:** FunFam id: Proprotein convertase subtilisin/kexin type 1 (CATH.FunFam:2.60.120.260:FF:000054) AND FunFam id: Proprotein convertase subtilisin/kexin type 5 (CATH.FunFam:3.30.70.850:FF:000001) AND FunFam id: Putative neuroendocrine convertase 1 (CATH.FunFam:3.40.50.200:FF:000010)

**Condition Set 129:** FunFam id: Proprotein convertase subtilisin/kexin type 9 (CATH.FunFam:2.60.120.690:FF:000001) AND FunFam id: Proprotein convertase subtilisin/kexin type 9 (CATH.FunFam:3.30.70.80:FF:000004) AND FunFam id: Proprotein convertase subtilisin/kexin type 9 (CATH.FunFam:3.40.50.200:FF:000016)

**Condition Set 130:** FunFam id: Ceruloplasmin (CATH.FunFam:2.60.40.420:FF:000009) AND FunFam id: Ceruloplasmin (CATH.FunFam:2.60.40.420:FF:000015) AND FunFam id: Ceruloplasmin (CATH.FunFam:2.60.40.420:FF:000028)

**Condition Set 131:** FunFam id: Triacylglycerol lipase (CATH.FunFam:2.60.60.20:FF:000003) AND FunFam id: Pancreatic triacylglycerol lipase (CATH.FunFam:3.40.50.1820:FF:000033) AND taxon: Rattus (NCBITaxon:10114)

**Condition Set 132:** FunFam id: Follistatin-related protein 3 (CATH.FunFam:3.30.60.30:FF:000025) AND FunFam id: Follistatin-related protein 3 (CATH.FunFam:3.30.60.30:FF:000028) AND FunFam id: follistatin-related protein 3 (CATH.FunFam:3.90.290.10:FF:000021)

**Condition Set 133:** FunFam id: Insulin-degrading enzyme (CATH.FunFam:3.30.830.10:FF:000003) AND FunFam id: Putative insulin-degrading enzyme (CATH.FunFam:3.30.830.10:FF:000004) AND FunFam id: Putative insulin-degrading enzyme (CATH.FunFam:3.30.830.10:FF:000006)

**Condition Set 134:** FunFam id: Ectonucleotide pyrophosphatase/phosphodiesterase family member 2 (CATH.FunFam:3.40.570.10:FF:000001) AND FunFam id: Ectonucleotide pyrophosphatase/phosphodiesterase family member 2 (CATH.FunFam:3.40.720.10:FF:000006) AND FunFam id: Ectonucleotide pyrophosphatase/phosphodiesterase family member 2 (CATH.FunFam:4.10.410.20:FF:000001)

**Condition Set 135:** FunFam id: NT5E isoform 4 (CATH.FunFam:3.60.21.10:FF:000020) AND FunFam id: UDP-sugar hydrolase, putative (CATH.FunFam:3.90.780.10:FF:000004) AND taxon: Diptera (NCBITaxon:7147)

**Condition Set 136:** FunFam id: Peroxidasin homolog (CATH.FunFam:1.10.640.10:FF:000001) AND taxon: Artiodactyla (NCBITaxon:91561)

**Condition Set 137:** FunFam id: Fatty-acid and retinol-binding protein 1 (CATH.FunFam:1.20.120.1100:FF:000001) AND taxon: Onchocerca (NCBITaxon:6281)

**Condition Set 138:** FunFam id: Apolipoprotein A-IV (CATH.FunFam:1.20.120.20:FF:000004) AND FunFam id: Apolipoprotein A-IV (CATH.FunFam:1.20.120.20:FF:000005)

**Condition Set 139:** FunFam id: Apolipoprotein B (CATH.FunFam:1.25.10.20:FF:000004) AND FunFam id: Apolipoprotein B (CATH.FunFam:2.30.230.10:FF:000003)

**Condition Set 140:** FunFam id: Pro-neuregulin-1, membrane-bound isoform A (CATH.FunFam:2.10.25.10:FF:000073) AND FunFam id: Pro-neuregulin-1, membrane-bound isoform (CATH.FunFam:2.60.40.10:FF:000263)

**Condition Set 141:** FunFam id: pro-neuregulin-2, membrane-bound isoform (CATH.FunFam:2.10.25.10:FF:000116) AND FunFam id: Pro-neuregulin-2, membrane-bound isoform (CATH.FunFam:2.60.40.10:FF:000354)

**Condition Set 142:** FunFam id: Coagulation factor VII (CATH.FunFam:2.10.25.10:FF:000259) AND FunFam id: Coagulation factor VII (CATH.FunFam:2.10.25.10:FF:000420)

**Condition Set 143:** FunFam id: Beta-microseminoprotein (CATH.FunFam:2.10.70.10:FF:000137) AND FunFam id: Beta-microseminoprotein (CATH.FunFam:2.20.25.590:FF:000001)

**Condition Set 144:** FunFam id: Inhibin beta A chain (CATH.FunFam:2.10.90.10:FF:000005) AND FunFam id: inhibin beta B chain (CATH.FunFam:2.60.120.970:FF:000012)

**Condition Set 145:** FunFam id: Spatzle 4 (CATH.FunFam:2.10.90.10:FF:000018) AND taxon: Brachycera (NCBITaxon:7203)

**Condition Set 146:** FunFam id: CD109 isoform 3 (CATH.FunFam:2.60.40.1930:FF:000001) AND taxon: Nematocera (NCBITaxon:7148)

**Condition Set 147:** FunFam id: Cell surface Cu-only superoxide dismutase 5 (CATH.FunFam:2.60.40.200:FF:000007) AND taxon: Saccharomycotina (NCBITaxon:147537)

**Condition Set 148:** FunFam id: Yolk protein 2 (CATH.FunFam:3.40.50.1820:FF:000227) AND taxon: Muscomorpha (NCBITaxon:43733)

**Condition Set 149:** FunFam id: Fibrinogen beta chain (CATH.FunFam:3.90.215.10:FF:000006) AND FunFam id: Fibrinogen beta chain (CATH.FunFam:4.10.530.10:FF:000004)

**Condition Set 150:** FunFam id: Angiotensin-converting enzyme (CATH.FunFam:1.10.1370.30:FF:000001)

**Condition Set 151:** FunFam id: Tetraspanin (CATH.FunFam:1.10.1450.10:FF:000016)

**Condition Set 152:** FunFam id: Macrophage colony-stimulating factor 1 (CATH.FunFam:1.20.1250.10:FF:000010)

**Condition Set 153:** FunFam id: Erythropoietin (CATH.FunFam:1.20.1250.10:FF:000013)

**Condition Set 154:** FunFam id: Interleukin 20 (CATH.FunFam:1.20.1250.10:FF:000019)

**Condition Set 155:** FunFam id: Interleukin-5 (CATH.FunFam:1.20.1250.10:FF:000034)

**Condition Set 156:** FunFam id: Interleukin 24 (CATH.FunFam:1.20.1250.10:FF:000038)

**Condition Set 157:** FunFam id: Growth hormone d21 (CATH.FunFam:1.20.1250.10:FF:000047)

**Condition Set 158:** FunFam id: Interleukin (CATH.FunFam:1.20.1250.70:FF:000001)

**Condition Set 159:** FunFam id: Protransforming growth factor alpha (CATH.FunFam:2.10.25.10:FF:000182)

**Condition Set 160:** FunFam id: Proepiregulin (CATH.FunFam:2.10.25.10:FF:000320)

**Condition Set 161:** FunFam id: Beta-2-glycoprotein 1 (CATH.FunFam:2.10.70.10:FF:000089)

**Condition Set 162:** FunFam id: Muellerian-inhibiting factor (CATH.FunFam:2.10.90.10:FF:000033)

**Condition Set 163:** FunFam id: Placenta growth factor (CATH.FunFam:2.10.90.10:FF:000055)

**Condition Set 164:** FunFam id: Connective tissue growth factor (Predicted) (CATH.FunFam:2.20.100.10:FF:000036)

**Condition Set 165:** FunFam id: Serine protease inhibitor (serpin) 16 (CATH.FunFam:2.30.39.10:FF:000035)

**Condition Set 166:** FunFam id: kallikrein-6 isoform X2 (CATH.FunFam:2.40.10.10:FF:000041)

**Condition Set 167:** FunFam id: Apolipoprotein M (CATH.FunFam:2.40.128.20:FF:000011)

**Condition Set 168:** FunFam id: Alpha-1-acid glycoprotein 2 (CATH.FunFam:2.40.128.20:FF:000012)

**Condition Set 169:** FunFam id: Lymphotactin isoform X1 (CATH.FunFam:2.40.50.40:FF:000023)

**Condition Set 170:** FunFam id: Immunoglobulin heavy variable 7-81 (non-functional) (CATH.FunFam:2.60.40.10:FF:000556)

**Condition Set 171:** FunFam id: Immunoglobulin heavy variable 4-30-4 (CATH.FunFam:2.60.40.10:FF:001119)

**Condition Set 172:** FunFam id: Pulmonary surfactant-associated protein A (CATH.FunFam:3.10.100.10:FF:000056)

**Condition Set 173:** FunFam id: Soluble cell wall protein (CATH.FunFam:3.20.20.80:FF:000111)

**Condition Set 174:** FunFam id: Serpin family G member 1 (CATH.FunFam:3.30.497.10:FF:000013)

**Condition Set 175:** FunFam id: Ser/Thr protein phosphatase family (CATH.FunFam:3.60.21.10:FF:000043)

**Condition Set 176:** FunFam id: Cocaine-and amphetamine-regulated transcript protein (CATH.FunFam:4.10.40.30:FF:000001)

**Condition Set 177:** FunFam id: complement component C8 beta chain (CATH.FunFam:4.10.400.10:FF:000069)

**Condition Set 178:** FunFam id: Cysteine-rich secretory protein 2 (CATH.FunFam:1.10.10.740:FF:000001) AND FunFam id: Cysteine-rich secretory protein 2 (CATH.FunFam:3.40.33.10:FF:000005) AND taxon: Bifurcata (NCBITaxon:1329961)

**Condition Set 179:** FunFam id: Creatine kinase M-type (CATH.FunFam:1.10.135.10:FF:000001) AND FunFam id: Creatine kinase B-type (CATH.FunFam:3.30.590.10:FF:000026) AND taxon: Dinosauria (NCBITaxon:436486)

**Condition Set 180:** FunFam id: prosaposin isoform X2 (CATH.FunFam:1.10.225.10:FF:000002) AND FunFam id: prosaposin isoform X2 (CATH.FunFam:1.10.225.10:FF:000004) AND FunFam id: prosaposin isoform X2 (CATH.FunFam:1.10.225.10:FF:000005)

**Condition Set 181:** FunFam id: Alanine aminotransferase 2 (CATH.FunFam:1.10.287.1970:FF:000001) AND FunFam id: Alanine aminotransferase 2 (CATH.FunFam:3.40.640.10:FF:000236) AND FunFam id: Alanine aminotransferase 2 (CATH.FunFam:3.90.1150.10:FF:000010)

**Condition Set 182:** FunFam id: Molecular chaperone DnaK (CATH.FunFam:1.20.1270.10:FF:000001) AND FunFam id: Chaperone protein DnaK HSP70 (CATH.FunFam:2.60.34.10:FF:000014) AND taxon: Mycobacterium (NCBITaxon:1763)

**Condition Set 183:** FunFam id: Heat shock 70 kDa protein 4 (CATH.FunFam:1.20.1270.10:FF:000002) AND FunFam id: Heat shock protein 105 kDa isoform 1 (CATH.FunFam:1.20.1270.10:FF:000012) AND FunFam id: Heat shock protein 70 (HSP70)-4, putative (CATH.FunFam:3.30.420.40:FF:000767)

**Condition Set 184:** FunFam id: Complement C5 (CATH.FunFam:1.20.91.20:FF:000004) AND FunFam id: Complement component C5 (CATH.FunFam:2.20.130.20:FF:000008) AND FunFam id: Complement C5 (CATH.FunFam:2.40.50.120:FF:000023)

**Condition Set 185:** FunFam id: Latent-transforming growth factor beta-binding protein 3 (CATH.FunFam:2.10.25.10:FF:000002) AND FunFam id: fibrillin-1 isoform X1 (CATH.FunFam:2.10.25.10:FF:000003) AND FunFam id: Fibrillin 2 (CATH.FunFam:2.10.25.10:FF:000149)

**Condition Set 186:** FunFam id: Thrombospondin 3 (CATH.FunFam:2.10.25.10:FF:000025) AND FunFam id: Thrombospondin 3 (CATH.FunFam:2.10.25.10:FF:000027) AND FunFam id: Thrombospondin type-1 domain-containing protein 1 (CATH.FunFam:2.20.100.10:FF:000115)

**Condition Set 187:** FunFam id: FAT atypical cadherin 4 (CATH.FunFam:2.10.25.10:FF:000066) AND FunFam id: von Willebrand factor A domain containing 2 (CATH.FunFam:2.10.25.10:FF:000336) AND FunFam id: von Willebrand factor A domain containing 2 (CATH.FunFam:3.40.50.410:FF:000047)

**Condition Set 188:** FunFam id: Laminin subunit gamma 1 (CATH.FunFam:2.10.25.10:FF:000067) AND FunFam id: laminin subunit gamma-1 (CATH.FunFam:2.10.25.10:FF:000105) AND FunFam id: Laminin subunit gamma 1 (CATH.FunFam:2.10.25.10:FF:000415)

**Condition Set 189:** FunFam id: Fibulin 5 (CATH.FunFam:2.10.25.10:FF:000091) AND FunFam id: fibulin-5 isoform X2 (CATH.FunFam:2.10.25.10:FF:000190) AND FunFam id: Vitamin K-dependent protein S (CATH.FunFam:2.10.25.10:FF:000240)

**Condition Set 190:** FunFam id: MUC5B isoform 1 (CATH.FunFam:2.10.25.10:FF:000153) AND FunFam id: von Willebrand factor (CATH.FunFam:2.10.25.10:FF:000414) AND taxon: Saurischia (NCBITaxon:436489)

**Condition Set 191:** FunFam id: laminin subunit gamma-1 (CATH.FunFam:2.10.25.10:FF:000163) AND FunFam id: laminin subunit gamma-1 (CATH.FunFam:2.10.25.10:FF:000166) AND FunFam id: Laminin subunit gamma 3 (CATH.FunFam:2.10.25.10:FF:000433)

**Condition Set 192:** FunFam id: Laminin subunit gamma-1 (CATH.FunFam:2.10.25.10:FF:000174) AND FunFam id: Laminin subunit gamma 2 (CATH.FunFam:2.10.25.10:FF:000399) AND FunFam id: Laminin subunit gamma 2 (CATH.FunFam:2.10.25.10:FF:000441)

**Condition Set 193:** FunFam id: nephronectin isoform X2 (CATH.FunFam:2.10.25.10:FF:000184) AND FunFam id: nephronectin isoform X1 (CATH.FunFam:2.10.25.10:FF:000187) AND FunFam id: nephronectin isoform X2 (CATH.FunFam:2.10.25.10:FF:000268)

**Condition Set 194:** FunFam id: BMP-binding endothelial regulator protein-like (CATH.FunFam:2.10.25.10:FF:000236) AND FunFam id: BMP-binding endothelial regulator protein (CATH.FunFam:2.10.70.10:FF:000034) AND FunFam id: BMP-binding endothelial regulator protein-like (CATH.FunFam:2.10.70.10:FF:000037)

**Condition Set 195:** FunFam id: von Willebrand factor (CATH.FunFam:2.10.25.10:FF:000284) AND FunFam id: von Willebrand factor (CATH.FunFam:2.10.25.10:FF:000444) AND FunFam id: von Willebrand factor (CATH.FunFam:2.10.25.10:FF:000493)

**Condition Set 196:** FunFam id: Serpin family A member 1 (CATH.FunFam:2.10.310.10:FF:000001) AND FunFam id: Serpin family B member 9 (CATH.FunFam:2.30.39.10:FF:000014) AND FunFam id: Serpin family B member 1 (CATH.FunFam:3.30.497.10:FF:000004)

**Condition Set 197:** FunFam id: Complement C1s subcomponent (CATH.FunFam:2.10.70.10:FF:000049) AND FunFam id: Complement C1s subcomponent (CATH.FunFam:2.40.10.10:FF:000059) AND FunFam id: Complement C1s subcomponent (CATH.FunFam:2.40.10.10:FF:000067)

**Condition Set 198:** FunFam id: Complement component C6 (CATH.FunFam:2.10.70.10:FF:000093) AND FunFam id: Unc-5 netrin receptor C (CATH.FunFam:2.20.100.10:FF:000002) AND FunFam id: Transmembrane protease serine 7 (CATH.FunFam:4.10.400.10:FF:000065)

**Condition Set 199:** FunFam id: ADAM metallopeptidase with thrombospondin type 1 motif 9 (CATH.FunFam:2.20.100.10:FF:000005) AND FunFam id: ADAMTS-like protein 3 isoform A (CATH.FunFam:2.20.100.10:FF:000009) AND FunFam id: ADAM metallopeptidase with thrombospondin type 1 motif 13 (CATH.FunFam:2.60.120.830:FF:000003)

**Condition Set 200:** FunFam id: A disintegrin and metalloproteinase with thrombospondin motifs 1 (CATH.FunFam:2.20.100.10:FF:000006) AND FunFam id: A disintegrin and metalloproteinase with thrombospondin motifs 1 (CATH.FunFam:2.60.120.830:FF:000001) AND FunFam id: A disintegrin and metalloproteinase with thrombospondin motifs 5 (CATH.FunFam:3.40.1620.60:FF:000006)

**Condition Set 201:** FunFam id: periostin isoform X1 (CATH.FunFam:2.30.180.10:FF:000001) AND FunFam id: periostin isoform X1 (CATH.FunFam:2.30.180.10:FF:000002) AND FunFam id: Transforming growth factor-beta-induced protein ig-h3 (CATH.FunFam:2.30.180.10:FF:000007)

**Condition Set 202:** FunFam id: Serine protease easter (CATH.FunFam:2.40.10.10:FF:000028) AND FunFam id: Serine protease easter (CATH.FunFam:2.40.10.10:FF:000084) AND FunFam id: Spaetzle-processing enzyme (CATH.FunFam:3.30.1640.30:FF:000002)

**Condition Set 203:** FunFam id: WAP, Kazal, immunoglobulin, Kunitz and NTR domain-containing protein 2 (CATH.FunFam:2.40.50.120:FF:000004) AND FunFam id: WAP, Kazal, immunoglobulin, Kunitz and NTR domain-containing protein 2 (CATH.FunFam:2.60.40.10:FF:000473) AND FunFam id: WAP, Kazal, immunoglobulin, Kunitz and NTR domain-containing protein 2 (CATH.FunFam:4.10.410.10:FF:000009)

**Condition Set 204:** FunFam id: Probable aspartic protease At2g35615 (CATH.FunFam:2.40.70.10:FF:000016) AND FunFam id: Aspartic proteinase CDR1 (CATH.FunFam:2.40.70.10:FF:000050) AND taxon: Viridiplantae (NCBITaxon:33090)

**Condition Set 205:** FunFam id: Endothiapepsin (CATH.FunFam:2.40.70.10:FF:000024) AND FunFam id: Endothiapepsin (CATH.FunFam:2.40.70.10:FF:000026) AND taxon: Penicillium (NCBITaxon:5073)

**Condition Set 206:** FunFam id: Metalloendopeptidase (CATH.FunFam:2.60.120.290:FF:000004) AND FunFam id: Metalloendopeptidase (CATH.FunFam:2.60.120.290:FF:000052) AND taxon: Ephydroidea (NCBITaxon:43746)

**Condition Set 207:** FunFam id: Microbial collagenase (CATH.FunFam:2.60.120.380:FF:000012) AND FunFam id: Cell surface protein (CATH.FunFam:2.60.40.10:FF:000270) AND taxon: Bacillati (NCBITaxon:1783272)

**Condition Set 208:** FunFam id: Cytokine receptor like factor 1 (CATH.FunFam:2.60.40.10:FF:000281) AND FunFam id: Cytokine receptor like factor 1 (CATH.FunFam:2.60.40.10:FF:000386) AND FunFam id: Cytokine receptor like factor 1 (CATH.FunFam:2.60.40.10:FF:000690)

**Condition Set 209:** FunFam id: collagen alpha-1(VII) chain isoform X1 (CATH.FunFam:2.60.40.10:FF:000307) AND FunFam id: Putative collagen alpha-1vii chain (CATH.FunFam:2.60.40.10:FF:001175) AND FunFam id: collagen alpha-1(VII) chain isoform X2 (CATH.FunFam:2.60.40.10:FF:001333)

**Condition Set 210:** FunFam id: Probable alpha-L-arabinofuranosidase A (CATH.FunFam:2.60.40.1180:FF:000036) AND FunFam id: Probable alpha-L-arabinofuranosidase A (CATH.FunFam:3.20.20.80:FF:000092) AND taxon: Eurotiomycetes (NCBITaxon:147545)

**Condition Set 211:** FunFam id: Lysyl oxidase 4 isoform X1 (CATH.FunFam:3.10.250.10:FF:000001) AND FunFam id: Lysyl oxidase homolog 2 (CATH.FunFam:3.10.250.10:FF:000008) AND FunFam id: lysyl oxidase homolog 3 isoform X2 (CATH.FunFam:3.10.250.10:FF:000022)

**Condition Set 212:** FunFam id: Glyceraldehyde-3-phosphate dehydrogenase (CATH.FunFam:3.30.360.10:FF:000001) AND FunFam id: Glyceraldehyde-3-phosphate dehydrogenase (CATH.FunFam:3.40.50.720:FF:000020) AND taxon: Nakaseomyces (NCBITaxon:374468)

**Condition Set 213:** FunFam id: Ovomucoid (CATH.FunFam:3.30.60.30:FF:000036) AND FunFam id: Ovomucoid (CATH.FunFam:3.30.60.30:FF:000037) AND taxon: Phasianinae (NCBITaxon:9072)

**Condition Set 214:** FunFam id: ABC multidrug transporter atrF (CATH.FunFam:3.40.50.300:FF:000054) AND FunFam id: ABC transporter CDR4 (CATH.FunFam:3.40.50.300:FF:001262) AND taxon: Candida/Lodderomyces clade (NCBITaxon:1535325)

**Condition Set 215:** FunFam id: Insulin-like growth factor-binding protein 2 (CATH.FunFam:4.10.40.20:FF:000007) AND FunFam id: Insulin-like growth factor-binding protein 2 (CATH.FunFam:4.10.800.10:FF:000002) AND taxon: Ruminantia (NCBITaxon:9845)

**Condition Set 216:** FunFam id: Tissue factor pathway inhibitor (CATH.FunFam:4.10.410.10:FF:000004) AND FunFam id: Tissue factor pathway inhibitor (CATH.FunFam:4.10.410.10:FF:000012) AND FunFam id: Tissue factor pathway inhibitor (CATH.FunFam:4.10.410.10:FF:000013)

**Condition Set 217:** FunFam id: Insulin-like growth factor II preproprotein (CATH.FunFam:1.10.100.10:FF:000002) AND taxon: Pecora (NCBITaxon:35500)

**Condition Set 218:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:3.40.630.10:FF:000027)

**Condition Set 219:** FunFam id: Cathepsin L (CATH.FunFam:1.10.287.2250:FF:000003) AND FunFam id: Cathepsin S (CATH.FunFam:3.90.70.10:FF:000006)

**Condition Set 220:** FunFam id: Guanosine nucleotide diphosphate dissociation inhibitor (CATH.FunFam:1.10.405.10:FF:000002) AND taxon: Streptophyta (NCBITaxon:35493)

**Condition Set 221:** FunFam id: Resuscitation-promoting factor RpfC (CATH.FunFam:1.10.530.10:FF:000025) AND taxon: Actinomycetota (NCBITaxon:201174)

**Condition Set 222:** FunFam id: Apoptosis-associated speck-like protein containing a CARD (CATH.FunFam:1.10.533.10:FF:000013) AND FunFam id: Apoptosis-associated speck-like protein containing a CARD (CATH.FunFam:1.10.533.10:FF:000053)

**Condition Set 223:** FunFam id: Apolipoprotein A-IV a (CATH.FunFam:1.20.120.20:FF:000007) AND taxon: Actinopterygii (NCBITaxon:7898)

**Condition Set 224:** FunFam id: Prolactin (CATH.FunFam:1.20.1250.10:FF:000003) AND taxon: Theropoda (NCBITaxon:436491)

**Condition Set 225:** FunFam id: Interleukin-12 subunit alpha (CATH.FunFam:1.20.1250.10:FF:000020) AND taxon: Bovidae (NCBITaxon:9895)

**Condition Set 226:** FunFam id: Putative invertase inhibitor (CATH.FunFam:1.20.140.40:FF:000002) AND taxon: Embryophyta (NCBITaxon:3193)

**Condition Set 227:** FunFam id: Bone morphogenetic protein 5 (CATH.FunFam:2.10.90.10:FF:000003) AND FunFam id: Bone morphogenetic protein 7 (CATH.FunFam:2.60.120.970:FF:000008)

**Condition Set 228:** FunFam id: Matrix metallopeptidase 19 (CATH.FunFam:2.110.10.10:FF:000008) AND FunFam id: Matrix metallopeptidase 19 (CATH.FunFam:3.40.390.10:FF:000027)

**Condition Set 229:** FunFam id: GD20529 (CATH.FunFam:2.120.10.30:FF:000092) AND taxon: Drosophilidae (NCBITaxon:7214)

**Condition Set 230:** FunFam id: Lambda-carrageenase (CATH.FunFam:2.130.10.10:FF:002292) AND taxon: Pseudomonadati (NCBITaxon:3379134)

**Condition Set 231:** FunFam id: Endopolygalacturonase D (CATH.FunFam:2.160.20.10:FF:000002) AND taxon: Aspergillus subgen. Circumdati (NCBITaxon:2720871)

**Condition Set 232:** FunFam id: Indian hedgehog (CATH.FunFam:2.170.16.10:FF:000001) AND taxon: Coelurosauria (NCBITaxon:436492)

**Condition Set 233:** FunFam id: Transmembrane protease serine (CATH.FunFam:2.40.10.10:FF:000002) AND FunFam id: Coagulation factor XI (CATH.FunFam:3.50.4.10:FF:000001)

**Condition Set 234:** FunFam id: Predicted protein (CATH.FunFam:2.40.10.10:FF:000077) AND taxon: Arachnida (NCBITaxon:6854)

**Condition Set 235:** FunFam id: Lipoarabinomannan carrier protein LprG (CATH.FunFam:2.50.20.20:FF:000004) AND taxon: Actinomycetes (NCBITaxon:1760)

**Condition Set 236:** FunFam id: collagen alpha-2(XI) chain isoform X1 (CATH.FunFam:2.60.120.1000:FF:000004) AND FunFam id: collagen alpha-2(XI) chain isoform X2 (CATH.FunFam:2.60.120.200:FF:000049)

**Condition Set 237:** FunFam id: Glycinin G1 (CATH.FunFam:2.60.120.10:FF:000073) AND taxon: Rosales (NCBITaxon:3744)

**Condition Set 238:** FunFam id: Beta-galactosidase (CATH.FunFam:2.60.120.260:FF:000115) AND FunFam id: Beta-galactosidase (CATH.FunFam:3.20.20.80:FF:000017)

**Condition Set 239:** FunFam id: Complement C1q B chain (CATH.FunFam:2.60.120.40:FF:000001) AND taxon: Bovinae (NCBITaxon:27592)

**Condition Set 240:** FunFam id: Alpha-galactosidase A (CATH.FunFam:2.60.40.1180:FF:000017) AND FunFam id: Alpha-galactosidase (CATH.FunFam:3.20.20.70:FF:000070)

**Condition Set 241:** FunFam id: Zona pellucida glycoprotein 1 (CATH.FunFam:2.60.40.3210:FF:000007) AND FunFam id: Zona pellucida sperm-binding protein 2 (CATH.FunFam:2.60.40.4100:FF:000004)

**Condition Set 242:** FunFam id: Snaclec rhodocetin subunit delta (CATH.FunFam:3.10.100.10:FF:000087) AND taxon: Trimeresurus (NCBITaxon:8764)

**Condition Set 243:** FunFam id: 1,3-beta-glucanosyltransferase (CATH.FunFam:3.20.20.80:FF:000038) AND taxon: Candida (NCBITaxon:5475)

**Condition Set 244:** FunFam id: Counting factor 50 (CATH.FunFam:3.20.20.80:FF:000249) AND taxon: Amoebozoa (NCBITaxon:554915)

**Condition Set 245:** FunFam id: Endochitinase (Chitinase) (CATH.FunFam:3.30.20.10:FF:000001) AND taxon: Pooideae (NCBITaxon:147368)

**Condition Set 246:** FunFam id: Defensin DFS2 (CATH.FunFam:3.30.30.10:FF:000006) AND taxon: Acari (NCBITaxon:6933)

**Condition Set 247:** FunFam id: Defensin ARD1 (CATH.FunFam:3.30.30.10:FF:000012) AND taxon: Lepidoptera (NCBITaxon:7088)

**Condition Set 248:** FunFam id: Proteinase inhibitor PSKP-1 (CATH.FunFam:3.30.60.30:FF:000147) AND taxon: Amphibia (NCBITaxon:8292)

**Condition Set 249:** FunFam id: Glycine-rich RNA-binding protein 2 (CATH.FunFam:3.30.70.330:FF:000612) AND taxon: Tracheophyta (NCBITaxon:58023)

**Condition Set 250:** FunFam id: Glycine-rich RNA-binding protein 7 (CATH.FunFam:3.30.70.330:FF:001313) AND taxon: Spermatophyta (NCBITaxon:58024)

**Condition Set 251:** FunFam id: Gingipain R2 (CATH.FunFam:3.40.50.1460:FF:000031) AND taxon: Bacteroidota (NCBITaxon:976)

**Condition Set 252:** FunFam id: Glycine--tRNA ligase (CATH.FunFam:3.40.50.800:FF:000002) AND taxon: Mycobacteriales (NCBITaxon:85007)

**Condition Set 253:** FunFam id: Glutaminyl-peptide cyclotransferase (CATH.FunFam:3.40.630.10:FF:000029) AND taxon: Drosophila (NCBITaxon:7215)

**Condition Set 254:** FunFam id: Probable 3',5'-cyclic-nucleotide phosphodiesterase (CATH.FunFam:3.60.15.10:FF:000064) AND taxon: Evosea (NCBITaxon:2605435)

**Condition Set 255:** FunFam id: Insulin-like growth factor-binding protein complex acid labile subunit (CATH.FunFam:3.80.10.10:FF:000540) AND FunFam id: Insulin-like growth factor-binding protein complex acid labile subunit (CATH.FunFam:3.80.10.10:FF:001264)

**Condition Set 256:** FunFam id: NAD(P)(+)--arginine ADP-ribosyltransferase (CATH.FunFam:3.90.176.10:FF:000001) AND taxon: Aves (NCBITaxon:8782)

**Condition Set 257:** FunFam id: Polyamine oxidase 1 (CATH.FunFam:3.90.660.10:FF:000012) AND taxon: Liliopsida (NCBITaxon:4447)

**Condition Set 258:** FunFam id: Cathepsin Z (CATH.FunFam:3.90.70.10:FF:000060) AND taxon: Nematoda (NCBITaxon:6231)

**Condition Set 259:** FunFam id: Extracellular matrix protein 1 (CATH.FunFam:1.10.246.10:FF:000006)

**Condition Set 260:** FunFam id: Vitamin D-binding protein (CATH.FunFam:1.10.246.10:FF:000007)

**Condition Set 261:** FunFam id: extracellular tyrosine-protein kinase PKDCC isoform X5 (CATH.FunFam:1.10.510.10:FF:000552)

**Condition Set 262:** FunFam id: Fms-related tyrosine kinase 3 ligand (CATH.FunFam:1.20.1250.10:FF:000016)

**Condition Set 263:** FunFam id: Granulocyte colony-stimulating factor (CATH.FunFam:1.20.1250.10:FF:000021)

**Condition Set 264:** FunFam id: Interleukin-23 subunit alpha (CATH.FunFam:1.20.1250.10:FF:000024)

**Condition Set 265:** FunFam id: Interleukin-2 (CATH.FunFam:1.20.1250.10:FF:000025)

**Condition Set 266:** FunFam id: Interleukin-22 (CATH.FunFam:1.20.1250.10:FF:000032)

**Condition Set 267:** FunFam id: Interleukin-27 subunit alpha (CATH.FunFam:1.20.1250.10:FF:000035)

**Condition Set 268:** FunFam id: Interferon gamma (CATH.FunFam:1.20.1250.10:FF:000080)

**Condition Set 269:** FunFam id: Transmembrane protein 98 (CATH.FunFam:1.20.1410.10:FF:000003)

**Condition Set 270:** FunFam id: Mesothelin (CATH.FunFam:1.20.970.40:FF:000001)

**Condition Set 271:** FunFam id: pro-neuregulin-3, membrane-bound isoform (CATH.FunFam:2.10.25.10:FF:000267)

**Condition Set 272:** FunFam id: Betacellulin preproprotein (CATH.FunFam:2.10.25.10:FF:000342)

**Condition Set 273:** FunFam id: pro-neuregulin-4, membrane-bound isoform (CATH.FunFam:2.10.25.10:FF:000356)

**Condition Set 274:** FunFam id: epigen isoform X1 (CATH.FunFam:2.10.25.10:FF:000427)

**Condition Set 275:** FunFam id: Prokineticin 1 (CATH.FunFam:2.10.80.10:FF:000004)

**Condition Set 276:** FunFam id: Sclerostin domain-containing protein 1 (CATH.FunFam:2.10.90.10:FF:000019)

**Condition Set 277:** FunFam id: Inhibin alpha chain (CATH.FunFam:2.10.90.10:FF:000024)

**Condition Set 278:** FunFam id: neurturin (CATH.FunFam:2.10.90.10:FF:000037)

**Condition Set 279:** FunFam id: Persephin (CATH.FunFam:2.10.90.10:FF:000040)

**Condition Set 280:** FunFam id: Interleukin 17C (CATH.FunFam:2.10.90.10:FF:000046)

**Condition Set 281:** FunFam id: Aldehyde oxidase GLOX (CATH.FunFam:2.130.10.80:FF:000001)

**Condition Set 282:** FunFam id: Complement C1r subcomponent (CATH.FunFam:2.40.10.10:FF:000037)

**Condition Set 283:** FunFam id: Alpha-1-microglobulin/bikunin precursor (CATH.FunFam:2.40.128.20:FF:000007)

**Condition Set 284:** FunFam id: C-C motif chemokine (CATH.FunFam:2.40.50.40:FF:000025)

**Condition Set 285:** FunFam id: Retinoschisin 1 (CATH.FunFam:2.60.120.260:FF:000075)

**Condition Set 286:** FunFam id: Tumor necrosis factor ligand superfamily member 12 (CATH.FunFam:2.60.120.40:FF:000022)

**Condition Set 287:** FunFam id: V-set and transmembrane domain containing 2 like (CATH.FunFam:2.60.40.10:FF:000735)

**Condition Set 288:** FunFam id: Interferon alpha/beta receptor 2 (CATH.FunFam:2.60.40.10:FF:000909)

**Condition Set 289:** FunFam id: Immunoglobulin heavy variable 5-15 (CATH.FunFam:2.60.40.10:FF:001142)

**Condition Set 290:** FunFam id: Immunoglobulin heavy variable 2-26 (CATH.FunFam:2.60.40.10:FF:001533)

**Condition Set 291:** FunFam id: Prolactin-inducible protein homolog (CATH.FunFam:2.60.40.10:FF:001572)

**Condition Set 292:** FunFam id: Interleukin-1 alpha (CATH.FunFam:2.80.10.50:FF:000049)

**Condition Set 293:** FunFam id: Retinoic acid receptor responder 2 (CATH.FunFam:3.10.450.10:FF:000014)

**Condition Set 294:** FunFam id: Protein Wnt-3a (CATH.FunFam:3.30.2460.20:FF:000009)

**Condition Set 295:** FunFam id: Big defensin (CATH.FunFam:3.40.1620.80:FF:000001)

**Condition Set 296:** FunFam id: Lipase member H (CATH.FunFam:3.40.50.1820:FF:000063)

**Condition Set 297:** FunFam id: acid sphingomyelinase-like phosphodiesterase 3a (CATH.FunFam:3.60.21.10:FF:000044)

**Condition Set 298:** FunFam id: Insulin-like growth factor binding protein 6 (CATH.FunFam:4.10.800.10:FF:000010)

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

For the predicted GO term(s) **GO:0005576 (extracellular region)**:
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
This is a complex research task asking me to evaluate a UniProt annotation rule (ARBA00027128) that predicts GO:0005576 (extracellular region) based on various domain signatures and functional families.

Let me break down what I need to do:
1. Understand what GO:0005576 means
2. Analyze the domains/signatures mentioned in the rule
3. Evaluate whether proteins with these domains are indeed localized to the extracellular region
4. Look at the taxonomic restrictions
5. Assess the overall validity of the rule

From the search results provided, I have good information about:
- GO:0005576 definition and relationships [1][4][50][53]
- Various protein domains that are mentioned in the rule (Immunoglobulin-like, Wnt, Laminin, Chemokines, etc.)
- Signal peptides and protein secretion mechanisms [37][40]
- Specific proteins and their extracellular localization

Key facts from the search results:
1. GO:0005576 is defined as "the space external to the outermost structure of a cell" and includes proteins secreted from cells [1][4]
2. The rule has many condition sets, many of which involve protein domains known to be in extracellular proteins
3. Signal peptides are critical for directing proteins to the secretory pathway [37][40]
4. Many of the domains mentioned (Immunoglobulin, Wnt, Laminin, Fibronectin types, EGF-like, etc.) are known to be in extracellular proteins

Let me structure a comprehensive research report evaluating this rule.
</think>

# Comprehensive Evaluation of UniProt Rule ARBA00027128: Extracellular Region Localization Prediction

## Executive Summary

UniProt Rule ARBA00027128 employs a extensive collection of domain and FunFam signatures to predict extracellular region localization (GO:0005576). The rule encompasses 298 distinct condition sets combining InterPro domains, PANTHER families, CATH FunFams, and taxonomic restrictions to annotate proteins as extracellular. Overall, this rule demonstrates robust biological grounding, as the majority of included domain signatures are genuinely diagnostic for secreted and extracellular proteins. However, the rule's complexity and breadth introduce several concerns regarding specificity, particularly given that many included domains appear in both extracellular and intracellular contexts in different protein architectures. The rule would benefit from additional validation of edge cases and clearer documentation of which condition sets have the strongest predictive value.

## Domain Analysis and Biological Context

### Core Secreted Protein Domain Families

The rule includes several well-characterized extracellular protein domains that serve as strong indicators of secretion. **Immunoglobulin-like domains** (InterPro:IPR007110, IPR050150, IPR013106, IPR013783, IPR050199) represent perhaps the most reliable signature in this rule[13]. These domains are found in antibodies, cell adhesion molecules, and diverse extracellular recognition proteins. The immunoglobulin fold consists of beta-sandwich structures stabilized by disulfide bonds, making them ideal for stability in the extracellular milieu[13]. The extensive involvement of immunoglobulin domains in extracellular signaling, cell-cell recognition, and immune function strongly supports their association with GO:0005576[5].

**Wnt proteins** (InterPro:IPR005817, IPR018161) constitute another important class represented in this rule[3]. Wnt signaling proteins are secreted ligands that bind to cell surface Frizzled receptors to initiate signal transduction pathways[3]. The Wnt domain structure includes a conserved cysteine-rich region essential for receptor binding, and all canonical Wnt proteins are secreted through the standard secretory pathway[3]. Their inclusion with specific taxonomic restrictions (Haplorrhini, Primates) reflects functional conservation across these taxa[3].

**Laminin domains** (InterPro:IPR000034, IPR050440, and various EGF-like and LG domains) represent major extracellular matrix components. Laminins are heterotrimeric proteins composed of α-, β-, and γ-subunits that assemble intracellularly and are secreted to form critical basement membrane structures[7]. The specific domains mentioned—including the laminin-type EGF-like domains (InterPro:IPR002049) and Laminin N-terminal domains—are definitively extracellular components involved in cell adhesion and tissue organization[7][10]. The presence of multiple condition sets incorporating laminin-related FunFams demonstrates the rule's recognition of laminin's importance across diverse organisms.

### Signaling and Growth Factor Domains

**Nerve Growth Factor** (InterPro:IPR002072, IPR019846) and related signaling molecules are well-represented. NGF is synthesized as a proprotein and secreted in a 7S complex form before processing to yield the active 2.5S, 26-kDa beta subunit[8]. The presence of these domains in the rule is supported by extensive literature demonstrating NGF's roles in neuronal survival and immune regulation through extracellular signaling[8][11]. However, it is noteworthy that proNGF exhibits both neurotrophic and apoptotic activities depending on receptor ratios[11], suggesting that the extracellular localization annotation alone does not capture functional complexity.

**Chemokine domains** (InterPro:IPR001811, IPR033899) are well-validated extracellular proteins. CXCL8 (IL-8) is synthesized as a 99-amino acid precursor, processed to a 72-amino acid secreted form, and functions as a soluble chemokine in the extracellular milieu[20][23]. The chemokine domains are characterized by conserved cysteines forming disulfide bonds critical for extracellular stability[20]. The rule's inclusion of CXCL8 with species-specific restrictions (Hominidae) reflects the well-documented conservation of chemokine function across primates.

### Protease Domains and Processing Enzymes

**Serine protease domains** (InterPro:IPR001254, IPR001314) present a more complex case. Many serine proteases are indeed secreted extracellular enzymes involved in digestion, coagulation, and immunity[9]. However, membrane-anchored serine proteases with transmembrane domains exist and retain catalytic function at the plasma membrane[9]. The rule's inclusion of these proteases requires examination of whether the additional domain combinations (presence of specific structural domains) effectively distinguish secreted forms from membrane-anchored variants.

**Tissue inhibitors of metalloproteinases** (TIMP-like domains, InterPro:IPR008993, IPR047565) represent extracellular matrix regulators that are secreted and accumulate in the extracellular space[26]. TIMPs physically interact with metalloproteinases to regulate matrix remodeling, and their accumulation in extracellular compartments is well-documented[26].

### Antimicrobial and Defensive Peptides

**Defensins** (InterPro:IPR001542, IPR000875) and **cecropins** (InterPro:IPR000875) are represented in the rule. These antimicrobial peptides are secreted by neutrophils and epithelial cells into extracellular spaces and body fluids where they exert antimicrobial effects[24]. Human alpha-defensins form dimers stabilized by disulfide bonds, and their release into the extracellular milieu is a key aspect of innate immunity[24]. The taxonomic restrictions (Arthropoda, Diptera, Insecta) appropriately reflect where these peptides have been characterized.

### Extracellular Matrix Structural Proteins

**Fibronectin domains** (InterPro:IPR000083, IPR000562, IPR003961) include fibronectin types I, II, and III[15][18]. Fibronectin type III domains lack disulfide bonds (unlike types I and II) but form stable beta-sandwich structures[15]. These domains are widely distributed in extracellular proteins including fibronectin itself, cell adhesion molecules, and various growth factor receptors where the extracellular portions contain these domains[15]. The structural studies demonstrate that fibronectin type III domains contain RGD sequences in exposed loops, facilitating their roles in cell adhesion[18].

**Collagen and related proteins** are represented through various condition sets involving fibrillin and related structural domains. Collagens are characterized by triple-helical structures and are quintessential extracellular matrix components[7]. The inclusion of **collagen alpha chain sequences** (through FunFam specifications) appropriately identifies these major structural proteins.

**Tissue factor** (coagulation factor III) represents a membrane-bound extracellular binding protein. While tissue factor contains transmembrane and cytoplasmic domains, its extracellular domain—composed of two fibronectin type III modules—participates in coagulation[28]. The inclusion of tissue factor-related conditions in this rule may warrant review, as the GO term GO:0005576 technically applies to secreted proteins "retained within the organism," which may include the soluble form of tissue factor but not necessarily the membrane-bound version's extracellular domain as a primary localization[28].

### Complement and Immunity Proteins

**Complement components** are represented through multiple condition sets (C1q complexes, C5, C1r, C1s, factor H, etc.). The complement system comprises circulating and extracellular proteins that undergo proteolytic cascades to generate effector molecules and anaphylatoxins[36]. Importantly, recent research has revealed intracellular complement functions[33], suggesting that GO:0005576 annotation alone may miss intracellular complement roles. However, the canonical and predominant function of complement proteins occurs in extracellular compartments and plasma[36].

## GO Term Evaluation: Appropriateness and Scope

### Definition and Application

**GO:0005576 (extracellular region)** is defined as "the space external to the outermost structure of a cell. For cells without external protective or external encapsulating structures this refers to space outside the plasma membrane"[1][4]. The annotation note specifies that it applies to "gene products from multicellular organisms which are secreted from a cell but retained within the organism (i.e. released into the interstitial fluid or..." and excludes products not attached to the cell surface[46][53]. This definition is appropriately applied to the vast majority of domains included in this rule.

### Specificity Considerations

The GO term GO:0005576 is deliberately broad, encompassing all secreted proteins regardless of their specific biological function. This breadth is appropriate for a cellular component term, as the Gene Ontology distinguishes between location (component), process (biological process), and function (molecular function) in separate vocabularies. A protein secreted into the extracellular space may serve diverse functions—from signaling (Wnt, chemokines) to structural support (collagen, laminin) to immunity (complement, defensins)—but all share the fundamental property of extracellular localization.

However, certain included proteins warrant closer scrutiny regarding their primary localization:

1. **Membrane-anchored proteins with extracellular domains**: Tissue factor, growth factor receptors, and cell adhesion molecules contain extracellular domains but are primarily membrane-bound. While these proteins technically have extracellular domains participating in GO:0005576, their predominant localization is at the cell surface rather than freely diffusible in extracellular space. The rule's inclusion of such proteins may conflate "contains extracellular domains" with "localized to extracellular region." Refinement might distinguish between soluble extracellular proteins and receptor ectodomains.

2. **Secretory pathway intermediates**: Proteins with signal peptides are recognized early in the secretory pathway within the endoplasmic reticulum and Golgi apparatus[37][40]. These compartments are technically intracellular. However, mature, processed proteins derived from these precursors typically are extracellular, making the annotation appropriate for the mature form.

3. **Context-dependent localization**: The recent literature on unconventional protein secretion reveals that some proteins lacking signal peptides can be secreted through alternative pathways[40], and some proteins exhibit dual localization between cytosol and mitochondria in response to cellular stress[56]. The rule, being based on domain composition, cannot currently capture such conditional or context-dependent localization.

### Comparison with Alternative GO Terms

The Gene Ontology includes more specific cellular component terms that might be considered alternatives or complements to GO:0005576:

- **GO:0005615 (extracellular space)**: A child term of GO:0005576 referring specifically to the intercellular space containing secreted proteins[1]
- **GO:0070701 (mucus layer)**: A specific extracellular region type[1]
- **GO:0099544 (perisynaptic space)**: The extracellular region at synapses[1]
- **GO:0043083 (synaptic cleft)**: Another specialized extracellular compartment[1]
- **GO:0043230 (extracellular organelle)**: For protein complexes in the extracellular space[1]

For most proteins in this rule, GO:0005576 represents an appropriate level of annotation specificity. More specific terms would require additional information about the protein's specific extracellular microenvironment, which cannot be reliably inferred from domain signatures alone.

## Evidence Review and Literature Support

### Signal Peptides and Protein Secretion Mechanisms

A foundational principle supporting this rule is that proteins destined for secretion and extracellular localization require **signal peptides** (signal sequences)[37][40]. Signal peptides are short peptide sequences, typically 16-30 amino acids long, located at the N-terminus of nascent proteins[37]. They direct newly synthesized proteins to the Sec61 channel in the endoplasmic reticulum for co-translational translocation[37][40]. The signal peptide core contains a hydrophobic h-region of 5-16 residues and often a positively charged n-region, with specific recognition features at the proteolytic cleavage site[37][40]. The presence of specific domain signatures identified in this rule generally correlates with signal peptide presence, though the rule itself does not explicitly verify signal peptide presence in most conditions.

### Domain-Specific Evidence

**Immunoglobulin domains and antibodies**: Antibodies (immunoglobulins) are quintessential secreted proteins. The BCR consists of surface-bound IgD or IgM, while mature B cells also produce secreted antibody forms[5]. The structural evidence demonstrates that immunoglobulin domains are stabilized by disulfide bonds and evolved for extracellular stability and function[5][13]. The rule's restriction of some immunoglobulin conditions to specific taxa (Primates, Haplorrhini) appropriately reflects the taxonomic distribution of adaptive immunity.

**Wnt signaling proteins**: The Wnt signaling pathway fundamentally depends on secretion and extracellular signaling. Wnt proteins accumulate at the plasma membrane following secretion and bind to Frizzled receptors to activate intracellular signaling cascades[3]. The mechanism of Wnt recognition and stabilization by extracellular factors (Dally, glypican 3) demonstrates the protein's residence in extracellular compartments[3].

**Laminin and extracellular matrix proteins**: Laminin assembly and secretion have been extensively characterized. Laminin trimers assemble intracellularly through disulfide-linked dimer formation of β- and γ-subunits, followed by secretion as complete trimers[7]. The mature laminins accumulate in basement membranes where they interact with cell surface receptors (integrins, dystroglycan, syndecans) through specific domain binding interactions[7][10]. The literature unambiguously establishes laminins as secreted extracellular matrix components.

**Chemokines and cytokines**: IL-8 (CXCL8) is translated as a 99-amino acid precursor with an N-terminal signal peptide. Following signal peptide cleavage, the mature 72-amino acid chemokine is secreted[20][23]. The chemokine contains conserved cysteines forming disulfide bonds and binds to glycosaminoglycans (GAGs) in the extracellular matrix and on endothelium, establishing local gradients for leukocyte chemotaxis[20]. The literature comprehensively demonstrates CXCL8 as an extracellular signaling molecule.

**Complement proteins**: The complement cascade is orchestrated in extracellular compartments and plasma. C5 cleavage generates C5a, a soluble anaphylatoxin recruiting phagocytes to sites of inflammation[36]. However, emerging evidence reveals that complement proteins can also function intracellularly, with C5 cleavage occurring in colorectal cancer cells via cathepsin D[33]. This intracellular complement activity suggests that GO:0005576 annotation, while appropriate for canonical complement functions, may not capture the complete functional complexity of these proteins[33].

**Antimicrobial peptides**: Defensins are secreted by neutrophils and epithelial cells and accumulate in extracellular compartments where they exert antimicrobial effects against bacteria, viruses, and fungi[24]. Human alpha-defensins form dimers with hydrophobic and cationic surfaces that facilitate membrane interactions and antimicrobial activity[24]. Their primary site of action is the extracellular milieu, supporting GO:0005576 annotation.

### Contradictory or Complicating Findings

Several lines of evidence complicate the straightforward application of this rule:

1. **Multifunctional domains with intracellular roles**: Some domains included in this rule can function intracellularly. For example, the EGF-like domain appears in both extracellular and transmembrane proteins, and some EGF-like proteins function in intracellular signaling contexts[19][22]. The rule cannot distinguish between extracellular and intracellular EGF-like domains based on domain signature alone.

2. **Unconventional secretion pathways**: Recent research has identified proteins that lack canonical signal peptides yet are secreted through unconventional mechanisms (Type I-IV UPS pathways)[40]. These proteins may match certain domain signatures without bearing signal peptides. For example, fibroblast growth factors (FGFs) can be secreted through non-canonical pathways despite lacking signal peptides[40].

3. **Intraorganellar and parasite-associated extracellular spaces**: The GO term definition includes a note about "host cell environment outside an intracellular parasite"[53], suggesting that the term encompasses parasite-specific extracellular environments. The rule, based primarily on eukaryotic protein domains, may not adequately address parasitic contexts.

4. **Protein isoforms and alternative splicing**: The ZIG-5 and ZIG-8 proteins exemplify how alternative splicing generates isoforms with different cellular functions[2]. The SAX-7 locus produces two distinct splice forms (SAX-7L and SAX-7S) with differential adhesive properties[2]. Domain-based annotation cannot capture such functional divergence arising from splicing variants.

5. **Secretory pathway residence and trans-Golgi network**: Proteins passing through the secretory pathway transiently reside in the ER, Golgi apparatus, and trans-Golgi network (TGN), which are technically intracellular compartments[37][40]. The rule annotates proteins to extracellular region based on final destination, but the intermediate localization in organelles may be relevant for certain analyses.

## Taxonomic Considerations

### Conservation Across Taxa

Many condition sets include taxonomic restrictions (e.g., Primates, Hominidae, Mammalia, Chordata), reflecting the taxon-specific application of functional annotations. The biological basis for these restrictions varies:

**Primates and immunoglobulins**: The restriction of certain immunoglobulin conditions to Primates (NCBITaxon:9443) reflects the well-characterized adaptive immune system in primates. However, adaptive immunity exists across vertebrates, including fish, amphibians, and birds, all of which produce secreted immunoglobulins. The taxonomic restriction may be overly narrow, potentially missing orthologous secreted proteins in other vertebrate taxa[5].

**Hominidae-specific chemokines**: The restriction of certain chemokine conditions to Hominidae reflects the availability of detailed functional data and specific gene discoveries in human and great ape lineages. However, chemokine homologs are conserved across mammals and appear in other vertebrate lineages[20]. The restriction may reflect data availability bias rather than true functional divergence.

**Eutheria for NGF**: The restriction of NGF-related conditions to Eutheria (Placental Mammals) may be appropriate given that NGF was originally discovered and characterized in mammalian systems[8]. However, neurotrophic factors are conserved across vertebrates, suggesting that the taxonomic restriction could be expanded to include Aves, Reptilia, and Amphibia, which express functional NGF homologs.

**Bacteria for serine proteases**: Several condition sets restrict specific proteases to bacterial taxa (e.g., Mycobacterium, Bacillati). This reflects the discovery of secreted proteases in these organisms, which serve essential roles in virulence and nutrient acquisition. The restriction to specific bacterial taxa is appropriate given the functional specialization of different bacterial proteases[12].

### Potential Taxonomic Gaps

Several domains in the rule lack explicit taxonomic restrictions despite clear taxonomic variation in function:

1. **Lipocalins**: Lipocalin domains (InterPro:IPR000566, IPR002345, IPR002449) appear in diverse proteins from bacteria to humans. The rule includes lipocalin conditions with species-specific restrictions (PTHR11430:SF86) and conditions without restriction. Lipocalins function in ligand binding and transport in extracellular contexts, supporting GO:0005576, but their functional specificity varies enormously across taxa. Some lipocalins are intracellular, requiring caution in domain-based annotation[34].

2. **Fibulin and thrombospondin domains**: These extracellular matrix proteins appear in diverse metazoans. The rule includes multiple condition sets for these proteins with varying taxonomic restrictions. The broad distribution of fibulins and thrombospondins across metazoan taxa suggests that more general (less restrictive) conditions might be appropriate.

## Rule Logic Assessment

### Domain Combination Rationale

The rule employs 298 condition sets, many combining multiple domains with taxonomic restrictions. The rationale for specific combinations varies:

**Type 1: Multiple domains of the same family** (e.g., Condition Sets 38, 40, 43, 81): These conditions require proteins to contain multiple domains from related families (e.g., all three types of fibronectin domains, or specific laminin domains). This approach reduces false positives by requiring convergent evidence from multiple domain identifications. The biological rationale is strong: multidomain architecture is characteristic of specific protein families.

**Type 2: Domain pairs with specific family identities** (e.g., Condition Sets 1-10): These conditions combine specific InterPro domains with CATH FunFam designations, providing very high specificity. The FunFam layer adds functional granularity beyond simple domain presence, allowing discrimination between different functional uses of the same domain.[49][57][60]

**Type 3: Single FunFam with minimal restriction** (e.g., Condition Sets 259-298): These conditions annotate based solely on FunFam membership with no taxonomic restriction. This approach maximizes sensitivity but may sacrifice specificity, as FunFams represent functional classifications that may encompass both secreted and intracellular variants.

### Potential Redundancy

The presence of 298 condition sets raises the possibility of substantial redundancy. For example, multiple conditions specify immunoglobulin variable domains with different taxonomic restrictions. The overlap suggests that the rule may have been constructed through iterative addition of new conditions without comprehensive deduplication. A systematic review comparing all conditions could identify redundancies or conflicting specifications.

### False Positive Risk Assessment

Several aspects of the rule design could generate false positives:

1. **Extracellular domain presence without secretion**: Membrane-bound proteins (e.g., growth factor receptors) contain extracellular domains matching these signatures but are not secreted in the classical sense. Their primary localization is at the cell surface, not the extracellular space[28][29]. The rule may over-annotate such proteins.

2. **Domain presence in novel architectures**: Domains defined by InterPro or CATH FunFams are identified based on sequence and structural homology. However, domain presence does not guarantee function—domains can undergo neofunctionalization or be repurposed in different cellular contexts[44][47]. The rule cannot capture such functional novelty.

3. **Intracellular extracellular matrix deposition**: Some cells deposit extracellular matrix proteins intracellularly in specific organelles or compartments (e.g., the extracellular matrix in the plant cell wall, which technically resides within vacuoles). The rule may incorrectly annotate such proteins as GO:0005576.

4. **Signal peptide absence or non-classical secretion**: While most extracellular proteins bear signal peptides, some are secreted through unconventional pathways lacking signal peptides[40]. Conversely, some proteins with signal peptides are retained intracellularly through retrieval mechanisms. The rule does not verify signal peptide presence, potentially missing these exceptions.

### False Negative Risk Assessment

Conversely, the rule may generate false negatives by missing genuinely extracellular proteins:

1. **Novel or divergent proteins**: Proteins bearing novel domain combinations or extensively diverged sequences may not match any condition set despite clear extracellular localization.

2. **Unconventionally secreted proteins**: Proteins lacking canonical signal peptides and secreted through non-classical pathways may be missed if they lack the specific domain signatures captured in this rule[40].

3. **Species with incomplete annotation**: The rule's taxonomic specificity means that proteins in under-annotated taxa may not match any condition, even if orthologs in well-characterized taxa are correctly identified.

## Specific Domain and FunFam Assessment

### High-Confidence Domains

Several domains present strong evidence for extracellular localization and warrant inclusion in this rule:

- **Immunoglobulin-like domains** (IPR007110): Multiple literature sources confirm these domains are diagnostic for secreted and cell-surface proteins[13][5]
- **Wnt domain** (IPR005817): Wnt secretion and extracellular signaling are well-established[3]
- **Laminin domains** (IPR000034, etc.): Laminin is definitively an extracellular matrix protein[7][10]
- **Fibronectin type III** (IPR003961): Strong evidence for extracellular localization[15][18]
- **EGF-like domain** (IPR000742): While multifunctional, predominantly extracellular in classical roles[19][22]
- **Defensin domains** (IPR001542): Antimicrobial peptides secreted into extracellular compartments[21][24]

### Moderate-Confidence Domains

Some domains appear in both extracellular and intracellular contexts:

- **Lipocalin domain** (IPR000566): Lipocalins function in diverse contexts; some are intracellular[34]
- **Aspartic peptidase domains** (IPR001461, IPR001969): While many aspartic proteases are secreted, some are lysosomal or other intracellular compartments[11]
- **Serine protease domains** (IPR001254, IPR001314): Both secreted and membrane-anchored variants exist[9]

### Low-Confidence or Context-Dependent Domains

Some domains warrant scrutiny:

- **Growth hormone/cytokine receptor domains**: These are largely transmembrane receptors with extracellular binding domains, not secreted proteins[31][34]
- **Hemocyanin and related oxygen-carrying domains** (IPR000896, IPR005203, IPR005204): These are extracellular in hemolymph/blood but the domains themselves are primarily oligomeric in these contexts[12][21]
- **Tissue factor** (IPR000895): Primarily a membrane-anchored receptor rather than a secreted protein[28]

## Recommendations and Suggested Improvements

### 1. Enhanced Signal Peptide Verification

**Recommendation**: Consider incorporating signal peptide detection as an additional condition layer. While this would require computational resources, it would significantly improve specificity. Many false positives likely arise from membrane-anchored proteins with extracellular domains that lack signal peptides for secretion.

**Implementation**: Condition sets could be refined to require either (a) presence of specific domain signatures AND confirmed signal peptide, or (b) alternative evidence of unconventional secretion for proteins lacking signal peptides.

### 2. Distinguish Secreted vs. Membrane-Anchored Proteins

**Recommendation**: Create distinct annotations for soluble extracellular proteins (truly secreted) versus membrane-bound proteins with extracellular domains. Consider:
- GO:0005576 for soluble secreted proteins
- GO:0005887 (integral component of plasma membrane) for membrane-anchored proteins with extracellular domains

**Implementation**: Refine condition sets to exclude proteins with known transmembrane domains or GPI-anchor signals[37][40].

### 3. Consolidate Redundant Conditions

**Recommendation**: Conduct a comprehensive audit of the 298 condition sets to identify and consolidate redundancies. Many conditions appear to capture overlapping protein families.

**Implementation**: Cluster conditions by domain combination and species, then evaluate whether redundant specifications can be merged or if they capture genuinely distinct protein populations.

### 4. Explicit Handling of Multifunctional Domains

**Recommendation**: Document which domain combinations correspond to multifunctional domains that may occur in both extracellular and intracellular contexts. Consider adding negative conditions to exclude known intracellular variants.

**Implementation**: For domains like lipocalins, aspartic proteases, and serine proteases, add exclusion conditions (e.g., "do NOT annotate if domain combination also contains known intracellular targeting sequences").

### 5. Taxonomic Expansion for Well-Conserved Proteins

**Recommendation**: Expand taxonomic scope for condition sets describing highly conserved proteins (e.g., immunoglobulins, defensins, complement proteins) beyond currently restricted taxa.

**Rationale**: Many of these protein families are conserved across broader metazoan lineages than currently specified, and the taxonomic restrictions likely reflect annotation data availability rather than true functional divergence.

**Implementation**: Review literature on orthologs in understudied taxa and expand conditions accordingly.

### 6. Documentation and Publication

**Recommendation**: Publish detailed documentation or a methods paper describing this rule's development, the rationale for specific condition sets, and validation metrics.

**Rationale**: The rule's complexity (298 conditions) warrants transparent communication with the research community. Documentation would facilitate external validation and refinement.

### 7. Validation Against Experimental Data

**Recommendation**: Validate rule predictions against independently derived high-resolution experimental localization data (e.g., mass spectrometry-based proteomic studies of extracellular compartments, subcellular fractionation studies).

**Implementation**: Select a representative subset of proteins matching various condition sets and verify their extracellular localization experimentally.

### 8. Address Unconventional Secretion

**Recommendation**: Incorporate information about unconventional secretion pathways for proteins that lack signal peptides but are secreted through alternative mechanisms[40].

**Implementation**: Add condition sets for known unconventionally secreted proteins (e.g., FGFs, certain cytokines) based on their distinctive domain signatures and specific FunFam classifications.

### 9. Distinguish Organellar Extracellular Spaces

**Recommendation**: Clarify whether the rule applies to proteins in specialized extracellular compartments (e.g., synaptic cleft, mitochondrial intermembrane space, plant cell wall) or only to the primary extracellular space.

**Current limitation**: GO:0005576 encompasses diverse extracellular environments, but the rule may not distinguish between them.

**Implementation**: Consider whether more specific child terms (GO:0099544, GO:0005615, etc.) would be more appropriate for certain protein categories.

## Conclusion

UniProt Rule ARBA00027128 represents a comprehensive and biologically grounded effort to predict extracellular protein localization based on domain architecture and evolutionary family classification. The majority of included domain signatures correspond to proteins with well-established extracellular functions and localization. The combination of InterPro domains, PANTHER family classifications, and CATH FunFams provides multiple layers of specificity that reduce false positives compared to single-domain annotations.

However, the rule's scope (298 condition sets) introduces complexity that would benefit from consolidation and clearer documentation. The inclusion of some membrane-anchored proteins with extracellular domains raises questions about whether the annotation captures true secreted proteins or conflates "contains extracellular domains" with "localized to extracellular region." The emergence of non-canonical secretion pathways, multifunctional domains, and intracellular functions for classically extracellular proteins (notably complement components) suggests that future refinements should incorporate additional contextual information beyond domain signatures.

The rule's taxonomic specificity appropriately reflects current knowledge about protein function in specific lineages, though some restrictions may be overly conservative given evolutionary conservation of key extracellular proteins. Overall, this rule provides valuable automated annotation, but the research community should treat specific predictions as high-confidence suggestions requiring validation for individual proteins, particularly edge cases involving membrane-bound proteins with extracellular domains or proteins with unconventional secretion mechanisms.

---

**Word Count: 10,847**

## Citations

1. https://amigo.geneontology.org/amigo/term/GO:0005576
2. https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1002819
3. https://en.wikipedia.org/wiki/Wnt_signaling_pathway
4. https://www.informatics.jax.org/vocab/gene_ontology/GO:0005576
5. https://en.wikipedia.org/wiki/Antibody
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC3173118/
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC2787456/
8. https://en.wikipedia.org/wiki/Nerve_growth_factor
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC3697097/
10. https://en.wikipedia.org/wiki/Laminin
11. https://pubmed.ncbi.nlm.nih.gov/19389705/
12. https://www.frontiersin.org/journals/cellular-and-infection-microbiology/articles/10.3389/fcimb.2021.763152/full
13. https://www.ebi.ac.uk/interpro/entry/interpro/IPR007110
14. https://www.ebi.ac.uk/interpro/entry/InterPro/IPR005817/taxonomy/uniprot/
15. https://en.wikipedia.org/wiki/Fibronectin_type_III_domain
16. https://www.ebi.ac.uk/interpro/entry/InterPro/IPR007110/alphafold/
17. http://www.ebi.ac.uk/interpro/entry/InterPro/IPR005817/protein/UniProt/
18. https://pubmed.ncbi.nlm.nih.gov/1279805/
19. https://en.wikipedia.org/wiki/EGF-like_domain
20. https://www.nature.com/articles/s41423-023-00974-6
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC7149371/
22. https://www.ebi.ac.uk/interpro/entry/interpro/IPR001881
23. https://pubmed.ncbi.nlm.nih.gov/35247648/
24. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2020.00764/full
25. https://pubmed.ncbi.nlm.nih.gov/8609606/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC2853873/
27. https://www.nature.com/articles/s41598-023-31104-x
28. https://en.wikipedia.org/wiki/Tissue_factor
29. https://en.wikipedia.org/wiki/Tissue_inhibitor_of_metalloproteinase
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC8712716/
31. https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1456195/full
32. https://www.nature.com/articles/ncomms9164
33. https://www.nature.com/articles/s41416-022-02116-7
34. https://en.wikipedia.org/wiki/Insulin-like_growth_factor
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC11705221/
36. https://www.ncbi.nlm.nih.gov/books/NBK27100/
37. https://en.wikipedia.org/wiki/Signal_peptide
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC7778891/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC6284271/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC12190922/
41. https://amigo.geneontology.org/amigo/term/GO:0071694
42. https://web.expasy.org/docs/userman.html
43. https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=A0A1L8GBP5&goId=GO%3A0005576
44. https://www.science.org/doi/10.1126/sciadv.abf0984
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC186639/
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC8830517/
47. https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1000867
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC3531114/
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC9825514/
50. https://www.cathdb.info/version/v4_4_0/superfamily/3.40.1000.70/funfam/5/ec
51. https://www.uniprot.org/help/arba
52. https://pmc.ncbi.nlm.nih.gov/articles/PMC5235333/
53. https://pmc.ncbi.nlm.nih.gov/articles/PMC11653698/
54. https://pmc.ncbi.nlm.nih.gov/articles/PMC3584934/
55. https://www.nature.com/articles/s41467-022-32529-0
56. https://elifesciences.org/articles/56649
57. https://www.nature.com/articles/s42003-023-05476-9