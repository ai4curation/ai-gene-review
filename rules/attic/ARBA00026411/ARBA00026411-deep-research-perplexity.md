---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-25T19:22:57.743774'
end_time: '2025-11-25T19:26:22.426367'
duration_seconds: 204.68
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00026411
  rule_type: arba
  go_terms: GO:0006520 (amino acid metabolic process)
  conditions_summary: '**Condition Set 1:** InterPro id: Aminoacyl-tRNA synthetase,
    class II (InterPro:IPR006195) AND InterPro id: Class II Aminoacyl-tRNA synthetase/Biotinyl
    protein ligase (BPL) and lipoyl protein ligase (LPL) (InterPro:IPR045864) AND
    taxon: Saccharomycotina (NCBITaxon:147537)


    **Condition Set 2:** InterPro id: Tryptophan synthase beta chain-like, PALP domain
    (InterPro:IPR001926) AND InterPro id: Cysteine synthase/Cystathionine beta-synthase
    (InterPro:IPR050214) AND taxon: Bacteria (NCBITaxon:2)


    **Condition Set 3:** InterPro id: Aspartate/glutamate/uridylate kinase (InterPro:IPR001048)
    AND InterPro id: Glutamate/acetylglutamate kinase (InterPro:IPR001057) AND InterPro
    id: Glutamate 5-kinase/delta-1-pyrroline-5-carboxylate synthase (InterPro:IPR005715)


    **Condition Set 4:** InterPro id: Tryptophan synthase beta chain-like, PALP domain
    superfamily (InterPro:IPR036052) AND taxon: Bacillati (NCBITaxon:1783272)


    **Condition Set 5:** InterPro id: GPR domain (InterPro:IPR000965) AND InterPro
    id: Aldehyde dehydrogenase domain (InterPro:IPR015590) AND InterPro id: Aldehyde/histidinol
    dehydrogenase (InterPro:IPR016161)


    **Condition Set 6:** InterPro id: Aminoacyl-tRNA synthetase, class I, conserved
    site (InterPro:IPR001412) AND InterPro id: Rossmann-like alpha/beta/alpha sandwich
    fold (InterPro:IPR014729) AND taxon: Pseudomonadota (NCBITaxon:1224)


    **Condition Set 7:** InterPro id: Ornithine/putrescine carbamoyltransferase (InterPro:IPR002292)
    AND InterPro id: Aspartate/ornithine carbamoyltransferase (InterPro:IPR006130)
    AND InterPro id: Aspartate/ornithine carbamoyltransferase, Asp/Orn-binding domain
    (InterPro:IPR006131)


    **Condition Set 8:** InterPro id: Aminotransferases, class-I, pyridoxal-phosphate-binding
    site (InterPro:IPR004838) AND InterPro id: Ethylene and sulfur compound biosynthesis-related
    protein (InterPro:IPR050478) AND taxon: eudicotyledons (NCBITaxon:71240)


    **Condition Set 9:** InterPro id: Tryptophan/Indoleamine 2,3-dioxygenase-like
    (InterPro:IPR037217) AND taxon: Metazoa (NCBITaxon:33208)


    **Condition Set 10:** InterPro id: ACT-like domain (InterPro:IPR045865) AND taxon:
    Fungi (NCBITaxon:4751)


    **Condition Set 11:** InterPro id: Aminoacyl-tRNA synthetase, class II (G/ P/
    S/T) (InterPro:IPR002314) AND InterPro id: Anticodon-binding (InterPro:IPR004154)
    AND taxon: Chordata (NCBITaxon:7711)


    **Condition Set 12:** InterPro id: Asparaginase/glutaminase-like (InterPro:IPR006034)
    AND InterPro id: L-asparaginase, C-terminal (InterPro:IPR027473) AND taxon: Eukaryota
    (NCBITaxon:2759)


    **Condition Set 13:** InterPro id: TPP-binding enzyme, conserved site (InterPro:IPR000399)
    AND InterPro id: Thiamine pyrophosphate enzyme, TPP-binding (InterPro:IPR011766)
    AND InterPro id: Acetolactate synthase, large subunit, biosynthetic (InterPro:IPR012846)


    **Condition Set 14:** InterPro id: Semialdehyde dehydrogenase, NAD-binding (InterPro:IPR000534)
    AND InterPro id: NAD(P)-binding domain superfamily (InterPro:IPR036291) AND taxon:
    Dikarya (NCBITaxon:451864)


    **Condition Set 15:** InterPro id: Pyruvate carboxyltransferase (InterPro:IPR000891)
    AND InterPro id: Alpha-isopropylmalate/homocitrate synthase, conserved site (InterPro:IPR002034)
    AND InterPro id: 2-isopropylmalate synthase LeuA, allosteric (dimerisation) domain
    (InterPro:IPR013709)


    **Condition Set 16:** InterPro id: Aromatic amino acid hydroxylase (InterPro:IPR001273)
    AND InterPro id: Aromatic amino acid hydroxylase, iron/copper binding site (InterPro:IPR018301)
    AND PANTHER id: PTHR11473:SF24


    **Condition Set 17:** InterPro id: ATP phosphoribosyltransferase HisG (InterPro:IPR001348)
    AND InterPro id: Nitrogen regulatory PII-like, alpha/beta (InterPro:IPR011322)
    AND InterPro id: Histidine biosynthesis HisG, C-terminal (InterPro:IPR013115)


    **Condition Set 18:** InterPro id: Indole-3-glycerol phosphate synthase, conserved
    site (InterPro:IPR001468) AND InterPro id: Ribulose-phosphate binding barrel (InterPro:IPR011060)
    AND InterPro id: Aldolase-type TIM barrel (InterPro:IPR013785)


    **Condition Set 19:** InterPro id: Anthranilate synthase component I, PabB-like
    (InterPro:IPR005256) AND InterPro id: ADC synthase (InterPro:IPR005801) AND InterPro
    id: Anthranilate synthase component I, N-terminal (InterPro:IPR006805)


    **Condition Set 20:** InterPro id: Homogentisate 1,2-dioxygenase (InterPro:IPR005708)
    AND InterPro id: RmlC-like cupin domain superfamily (InterPro:IPR011051) AND InterPro
    id: RmlC-like jelly roll fold (InterPro:IPR014710)


    **Condition Set 21:** InterPro id: Aconitase A/isopropylmalate dehydratase small
    subunit, swivel domain (InterPro:IPR000573) AND InterPro id: Aconitase/3-isopropylmalate
    dehydratase large subunit, alpha/beta/alpha domain (InterPro:IPR001030) AND InterPro
    id: Isopropylmalate dehydratase and related enzymes (InterPro:IPR050067)


    **Condition Set 22:** InterPro id: Dihydroxy-acid/6-phosphogluconate dehydratase,
    N-terminal (InterPro:IPR000581) AND InterPro id: Dihydroxy-acid dehydratase (InterPro:IPR004404)
    AND InterPro id: Dihydroxy-acid/6-phosphogluconate dehydratase, conserved site
    (InterPro:IPR020558)


    **Condition Set 23:** InterPro id: Aminotransferase class IV (InterPro:IPR001544)
    AND InterPro id: Branched-chain amino acid aminotransferase II (InterPro:IPR005786)
    AND PANTHER id: PTHR11825:SF44


    **Condition Set 24:** InterPro id: Acetylornithine/Succinylornithine transaminase
    family (InterPro:IPR004636) AND InterPro id: Aminotransferase class-III (InterPro:IPR005814)
    AND InterPro id: Pyridoxal phosphate-dependent transferase, major domain (InterPro:IPR015421)


    **Condition Set 25:** InterPro id: Anthranilate synthase/para-aminobenzoate synthase
    like domain (InterPro:IPR006221) AND InterPro id: Glutamine amidotransferase (InterPro:IPR017926)
    AND PANTHER id: PTHR43418:SF4


    **Condition Set 26:** InterPro id: DHS-like NAD/FAD-binding domain superfamily
    (InterPro:IPR029035) AND InterPro id: Thiamin diphosphate-binding fold (InterPro:IPR029061)
    AND PANTHER id: PTHR18968:SF13


    **Condition Set 27:** InterPro id: Aspartate-semialdehyde dehydrogenase, conserved
    site (InterPro:IPR000319) AND InterPro id: Semialdehyde dehydrogenase, dimerisation
    domain (InterPro:IPR012280)


    **Condition Set 28:** InterPro id: Tryptophan 2,3-dioxygenase (InterPro:IPR004981)
    AND PANTHER id: PTHR10138:SF0


    **Condition Set 29:** InterPro id: Aminoacyl-tRNA synthetase, class Ia, anticodon-binding
    (InterPro:IPR009080) AND taxon: Gammaproteobacteria (NCBITaxon:1236)


    **Condition Set 30:** InterPro id: Indoleamine 2,3-dioxygenase (InterPro:IPR000898)


    **Condition Set 31:** InterPro id: Aminotransferase class V domain (InterPro:IPR000192)
    AND InterPro id: Pyridoxal phosphate-dependent transferase, small domain (InterPro:IPR015422)
    AND InterPro id: Phosphoserine aminotransferase (InterPro:IPR022278)


    **Condition Set 32:** InterPro id: Serine/threonine dehydratase, pyridoxal-phosphate-binding
    site (InterPro:IPR000634) AND InterPro id: Threonine dehydratase, ACT-like domain
    (InterPro:IPR001721) AND PANTHER id: PTHR48078:SF11


    **Condition Set 33:** InterPro id: WHEP-TRS domain (InterPro:IPR000738) AND InterPro
    id: uS15/NS1, RNA-binding domain superfamily (InterPro:IPR009068) AND InterPro
    id: Glutathione S-transferase, C-terminal domain superfamily (InterPro:IPR036282)


    **Condition Set 34:** InterPro id: Homoserine kinase (InterPro:IPR000870) AND
    InterPro id: GHMP kinase, ATP-binding, conserved site (InterPro:IPR006203) AND
    InterPro id: GHMP kinase N-terminal domain (InterPro:IPR006204)


    **Condition Set 35:** InterPro id: Cysteine synthase/cystathionine beta-synthase,
    pyridoxal-phosphate attachment site (InterPro:IPR001216) AND InterPro id: Cystathionine
    beta-synthase (InterPro:IPR005857) AND InterPro id: CBS domain superfamily (InterPro:IPR046342)


    **Condition Set 36:** InterPro id: Chorismate mutase II, prokaryotic-type (InterPro:IPR002701)
    AND InterPro id: Chorismate mutase, AroQ class, eukaryotic type (InterPro:IPR008238)
    AND taxon: Ascomycota (NCBITaxon:4890)


    **Condition Set 37:** InterPro id: Acetolactate synthase, small subunit (InterPro:IPR004789)
    AND InterPro id: AHAS, ACT domain (InterPro:IPR039557) AND InterPro id: Acetolactate
    synthase small subunit-like, ACT domain (InterPro:IPR054480)


    **Condition Set 38:** InterPro id: B3/B4 tRNA-binding domain (InterPro:IPR005146)
    AND InterPro id: tRNA synthetase, B5-domain (InterPro:IPR005147) AND InterPro
    id: Putative DNA-binding domain superfamily (InterPro:IPR009061)


    **Condition Set 39:** InterPro id: FAD dependent oxidoreductase (InterPro:IPR006076)
    AND PANTHER id: PTHR11530:SF11 AND taxon: Craniata (NCBITaxon:89593)


    **Condition Set 40:** InterPro id: Tryptophan synthase, alpha chain (InterPro:IPR002028)
    AND InterPro id: Tryptophan synthase, alpha chain, active site (InterPro:IPR018204)


    **Condition Set 41:** FunFam id: 1-aminocyclopropane-1-carboxylate synthase 3
    (CATH.FunFam:3.40.640.10:FF:000051) AND taxon: Eukaryota (NCBITaxon:2759)


    **Condition Set 42:** FunFam id: 5-methyltetrahydropteroyltriglutamate--homocysteine
    methyltransferase (CATH.FunFam:3.20.20.210:FF:000003)


    **Condition Set 43:** FunFam id: Cystathionine beta-synthase (CATH.FunFam:3.40.50.1100:FF:000003)


    **Condition Set 44:** FunFam id: Related to CYS4-cystathionine beta-synthase (CATH.FunFam:3.40.50.1100:FF:000118)


    **Condition Set 45:** FunFam id: Probable aspartate-semialdehyde dehydrogenase
    (CATH.FunFam:3.30.360.10:FF:000016) AND FunFam id: Aspartate-semialdehyde dehydrogenase
    (CATH.FunFam:3.40.50.720:FF:000200) AND taxon: Fungi (NCBITaxon:4751)


    **Condition Set 46:** FunFam id: Glycine--tRNA ligase 2 (CATH.FunFam:3.30.720.200:FF:000001)
    AND FunFam id: Glycyl-tRNA synthetase 1 (CATH.FunFam:3.30.930.10:FF:000010) AND
    FunFam id: Glycyl-tRNA synthetase (CATH.FunFam:3.30.930.10:FF:000158)


    **Condition Set 47:** FunFam id: L-asparaginase 2 (CATH.FunFam:3.40.50.1170:FF:000001)
    AND FunFam id: L-asparaginase I (CATH.FunFam:3.40.50.40:FF:000006) AND taxon:
    Dikarya (NCBITaxon:451864)


    **Condition Set 48:** FunFam id: Chorismate mutase (CATH.FunFam:1.10.590.10:FF:000002)
    AND taxon: Ascomycota (NCBITaxon:4890)


    **Condition Set 49:** FunFam id: Indoleamine 2,3-dioxygenase 1 (CATH.FunFam:1.20.58.480:FF:000003)
    AND taxon: Metazoa (NCBITaxon:33208)


    **Condition Set 50:** FunFam id: D-aspartate oxidase (CATH.FunFam:3.40.50.720:FF:000551)
    AND taxon: Chordata (NCBITaxon:7711)


    **Condition Set 51:** FunFam id: Ornithine carbamoyltransferase, mitochondrial
    (CATH.FunFam:3.40.50.1370:FF:000009)


    **Condition Set 52:** FunFam id: Threonine--tRNA ligase 2, cytoplasmic (CATH.FunFam:3.40.50.800:FF:000003)


    **Condition Set 53:** FunFam id: Methionine synthase (CATH.FunFam:1.10.1240.10:FF:000001)
    AND FunFam id: Methionine synthase (CATH.FunFam:3.20.20.20:FF:000002) AND FunFam
    id: Methionine synthase (CATH.FunFam:3.20.20.330:FF:000001)


    **Condition Set 54:** FunFam id: Hemocyanin subunit 2 (CATH.FunFam:1.10.1280.10:FF:000004)
    AND FunFam id: Hemocyanin subunit 2 (CATH.FunFam:2.60.40.1520:FF:000001) AND taxon:
    Lepidoptera (NCBITaxon:7088)


    **Condition Set 55:** FunFam id: Os03g0824900 protein (CATH.FunFam:1.10.275.10:FF:000014)
    AND FunFam id: Argininosuccinate lyase (CATH.FunFam:1.10.40.30:FF:000001) AND
    FunFam id: argininosuccinate lyase isoform X2 (CATH.FunFam:1.20.200.10:FF:000015)


    **Condition Set 56:** FunFam id: Glutamate synthase, large subunit (CATH.FunFam:2.160.20.60:FF:000001)
    AND FunFam id: Glutamate synthase [NADH], amyloplastic (CATH.FunFam:3.20.20.70:FF:000017)
    AND FunFam id: Glutamate synthase 1 [NADH] (CATH.FunFam:3.20.20.70:FF:000031)


    **Condition Set 57:** FunFam id: Delta-1-pyrroline-5-carboxylate synthase (CATH.FunFam:3.40.1160.10:FF:000013)
    AND FunFam id: Delta-1-pyrroline-5-carboxylate synthase (CATH.FunFam:3.40.309.10:FF:000015)
    AND taxon: Streptophyta (NCBITaxon:35493)


    **Condition Set 58:** FunFam id: Alcohol dehydrogenase AdhP (CATH.FunFam:3.40.50.720:FF:000039)
    AND FunFam id: Alcohol dehydrogenase AdhP (CATH.FunFam:3.90.180.10:FF:000002)
    AND taxon: Saccharomycetes (NCBITaxon:4891)


    **Condition Set 59:** FunFam id: Acetolactate synthase (CATH.FunFam:3.40.50.970:FF:000007)
    AND FunFam id: Acetolactate synthase (CATH.FunFam:3.40.50.970:FF:000016) AND taxon:
    Bacteria (NCBITaxon:2)


    **Condition Set 60:** FunFam id: Pyruvate decarboxylase isozyme (CATH.FunFam:3.40.50.970:FF:000019)
    AND FunFam id: Pyruvate decarboxylase isozyme (CATH.FunFam:3.40.50.970:FF:000024)
    AND taxon: Saccharomyces (NCBITaxon:4930)


    **Condition Set 61:** FunFam id: Branched-chain-amino-acid aminotransferase, mitochondrial
    (CATH.FunFam:3.20.10.10:FF:000007) AND FunFam id: Branched-chain-amino-acid aminotransferase
    (CATH.FunFam:3.30.470.10:FF:000002)


    **Condition Set 62:** FunFam id: Alpha-aminoadipic semialdehyde synthase, mitochondrial
    (CATH.FunFam:3.30.360.10:FF:000008) AND FunFam id: Saccharopine dehydrogenase
    [NADP(+), L-glutamate-forming] (CATH.FunFam:3.40.50.720:FF:000072)


    **Condition Set 63:** FunFam id: Aspartate aminotransferase (CATH.FunFam:3.90.1150.10:FF:000001)
    AND taxon: Rodentia (NCBITaxon:9989)


    **Condition Set 64:** FunFam id: Tryptophan 2,3-dioxygenase (CATH.FunFam:1.10.287.3810:FF:000001)


    **Condition Set 65:** FunFam id: 3-isopropylmalate dehydratase small subunit (CATH.FunFam:3.20.19.10:FF:000003)


    **Condition Set 66:** FunFam id: Indole-3-glycerol phosphate synthase (CATH.FunFam:3.20.20.70:FF:000024)


    **Condition Set 67:** FunFam id: 2-isopropylmalate synthase (CATH.FunFam:3.20.20.70:FF:000045)


    **Condition Set 68:** FunFam id: ATP phosphoribosyltransferase (CATH.FunFam:3.30.70.120:FF:000003)


    **Condition Set 69:** FunFam id: Acetolactate synthase, small subunit (CATH.FunFam:3.30.70.260:FF:000001)


    **Condition Set 70:** FunFam id: Anthranilate phosphoribosyltransferase (CATH.FunFam:3.40.1030.10:FF:000002)


    **Condition Set 71:** FunFam id: L-asparaginase 1 (CATH.FunFam:3.40.50.40:FF:000001)


    **Condition Set 72:** FunFam id: Asparagine synthase B (CATH.FunFam:3.40.50.620:FF:000031)


    **Condition Set 73:** FunFam id: Phosphoserine aminotransferase (CATH.FunFam:3.40.640.10:FF:000010)


    **Condition Set 74:** FunFam id: O-succinylhomoserine sulfhydrylase (CATH.FunFam:3.40.640.10:FF:000035)


    **Condition Set 75:** FunFam id: 3-isopropylmalate dehydrogenase (CATH.FunFam:3.40.718.10:FF:000004)


    **Condition Set 76:** FunFam id: Anthranilate synthase component 1 (CATH.FunFam:3.60.120.10:FF:000003)


    **Condition Set 77:** FunFam id: Phosphoserine aminotransferase (CATH.FunFam:3.90.1150.10:FF:000006)


    **Condition Set 78:** FunFam id: Glutamate dehydrogenase (CATH.FunFam:1.10.285.10:FF:000001)
    AND FunFam id: Glutamate dehydrogenase (CATH.FunFam:3.40.50.10860:FF:000002) AND
    taxon: Pseudomonadati (NCBITaxon:3379134)


    **Condition Set 79:** FunFam id: Bifunctional glutamate/proline--tRNA ligase (CATH.FunFam:1.10.287.10:FF:000006)
    AND FunFam id: Bifunctional glutamate/proline--tRNA ligase (CATH.FunFam:3.30.110.30:FF:000001)
    AND FunFam id: Bifunctional glutamate/proline--tRNA ligase (CATH.FunFam:3.30.930.10:FF:000007)


    **Condition Set 80:** FunFam id: Arginine--tRNA ligase, cytoplasmic (CATH.FunFam:1.10.730.10:FF:000016)
    AND FunFam id: arginine--tRNA ligase, cytoplasmic (CATH.FunFam:3.30.1360.70:FF:000002)
    AND FunFam id: arginine--tRNA ligase, cytoplasmic (CATH.FunFam:3.40.50.620:FF:000084)


    **Condition Set 81:** FunFam id: Aminomethyltransferase (CATH.FunFam:2.40.30.110:FF:000002)
    AND FunFam id: Aminomethyltransferase (CATH.FunFam:3.30.1360.120:FF:000014) AND
    taxon: Craniata (NCBITaxon:89593)


    **Condition Set 82:** FunFam id: Alanyl-tRNA synthetase (CATH.FunFam:2.40.30.130:FF:000026)
    AND FunFam id: alanine--tRNA ligase, cytoplasmic (CATH.FunFam:3.10.310.40:FF:000002)
    AND FunFam id: Alanine--tRNA ligase, cytoplasmic (CATH.FunFam:3.30.930.10:FF:000011)


    **Condition Set 83:** FunFam id: Carnosine synthase 1 (CATH.FunFam:3.30.470.20:FF:000040)
    AND FunFam id: Carnosine synthase 1 (CATH.FunFam:3.40.50.20:FF:000018) AND taxon:
    Euteleostomi (NCBITaxon:117571)


    **Condition Set 84:** FunFam id: D-amino-acid oxidase (CATH.FunFam:3.30.9.10:FF:000004)
    AND FunFam id: D-amino acid oxidase (CATH.FunFam:3.40.50.720:FF:000641) AND taxon:
    Mammalia (NCBITaxon:40674)


    **Condition Set 85:** FunFam id: Lysine decarboxylase, inducible (CATH.FunFam:3.40.640.10:FF:000008)
    AND FunFam id: Lysine decarboxylase, inducible (CATH.FunFam:3.90.1150.10:FF:000016)
    AND taxon: Pseudomonadota (NCBITaxon:1224)


    **Condition Set 86:** FunFam id: 4-aminobutyrate aminotransferase (CATH.FunFam:3.40.640.10:FF:000013)
    AND FunFam id: 4-aminobutyrate aminotransferase (CATH.FunFam:3.90.1150.10:FF:000022)
    AND taxon: Gammaproteobacteria (NCBITaxon:1236)


    **Condition Set 87:** FunFam id: Glutamate decarboxylase like 1 (CATH.FunFam:3.40.640.10:FF:000016)
    AND FunFam id: Glutamate decarboxylase 1 (CATH.FunFam:3.90.1150.170:FF:000003)
    AND taxon: Eutheria (NCBITaxon:9347)


    **Condition Set 88:** FunFam id: tyrosine aminotransferase (CATH.FunFam:3.40.640.10:FF:000048)
    AND FunFam id: Tyrosine aminotransferase (CATH.FunFam:3.90.1150.10:FF:000040)
    AND taxon: Euarchontoglires (NCBITaxon:314146)


    **Condition Set 89:** FunFam id: Homocitrate synthase, mitochondrial (CATH.FunFam:1.10.238.260:FF:000002)
    AND FunFam id: Homocitrate synthase, mitochondrial (CATH.FunFam:3.20.20.70:FF:000032)


    **Condition Set 90:** FunFam id: Pyrroline-5-carboxylate reductase 1, mitochondrial
    (CATH.FunFam:1.10.3730.10:FF:000003) AND taxon: Primates (NCBITaxon:9443)


    **Condition Set 91:** FunFam id: Chorismate mutase (CATH.FunFam:1.10.590.10:FF:000001)
    AND taxon: rosids (NCBITaxon:71275)


    **Condition Set 92:** FunFam id: Isoleucyl-tRNA synthetase, cytoplasmic (CATH.FunFam:1.10.730.10:FF:000004)
    AND FunFam id: Isoleucyl-tRNA synthetase,cytoplasmic (CATH.FunFam:3.40.50.620:FF:000050)


    **Condition Set 93:** FunFam id: Arginine biosynthesis bifunctional protein ArgJ,
    mitochondrial (CATH.FunFam:3.10.20.340:FF:000002) AND FunFam id: Arginine biosynthesis
    bifunctional protein ArgJ, mitochondrial (CATH.FunFam:3.30.2330.10:FF:000001)


    **Condition Set 94:** FunFam id: Glutamine synthetase (CATH.FunFam:3.10.20.70:FF:000004)
    AND FunFam id: Glutamine synthetase (CATH.FunFam:3.30.590.10:FF:000004)


    **Condition Set 95:** FunFam id: Branched-chain-amino-acid aminotransferase (CATH.FunFam:3.20.10.10:FF:000004)
    AND FunFam id: Branched-chain-amino-acid aminotransferase (CATH.FunFam:3.30.470.10:FF:000005)


    **Condition Set 96:** FunFam id: Phosphoribosylanthranilate isomerase (CATH.FunFam:3.20.20.70:FF:000199)
    AND taxon: Saccharomycotina (NCBITaxon:147537)


    **Condition Set 97:** FunFam id: L-serine ammonia-lyase 1 (CATH.FunFam:3.30.1330.90:FF:000001)
    AND taxon: Enterobacterales (NCBITaxon:91347)


    **Condition Set 98:** FunFam id: Pterin-4-alpha-carbinolamine dehydratase 2 (CATH.FunFam:3.30.1360.20:FF:000001)
    AND taxon: Glires (NCBITaxon:314147)


    **Condition Set 99:** FunFam id: Homoaconitase, mitochondrial (CATH.FunFam:3.30.499.10:FF:000013)
    AND FunFam id: Homoaconitase, mitochondrial (CATH.FunFam:3.30.499.10:FF:000016)


    **Condition Set 100:** FunFam id: L-threonine dehydratase (CATH.FunFam:3.40.1020.10:FF:000001)
    AND FunFam id: L-threonine dehydratase (CATH.FunFam:3.40.50.1100:FF:000008)


    **Condition Set 101:** FunFam id: Cysteine synthase (CATH.FunFam:3.40.50.1100:FF:000002)
    AND FunFam id: Cysteine synthase (CATH.FunFam:3.40.50.1100:FF:000006)


    **Condition Set 102:** FunFam id: Acetolactate synthase (CATH.FunFam:3.40.50.1220:FF:000008)
    AND FunFam id: Acetolactate synthase, mitochondrial (CATH.FunFam:3.40.50.970:FF:000053)


    **Condition Set 103:** FunFam id: Sarcosine/dimethylglycine N-methyltransferase
    (CATH.FunFam:3.40.50.150:FF:000461) AND taxon: Bacillati (NCBITaxon:1783272)


    **Condition Set 104:** FunFam id: Shikimate kinase, chloroplastic (CATH.FunFam:3.40.50.300:FF:000822)
    AND taxon: Liliopsida (NCBITaxon:4447)


    **Condition Set 105:** FunFam id: Sorbitol dehydrogenase (CATH.FunFam:3.40.50.720:FF:000068)
    AND taxon: Archaea (NCBITaxon:2157)


    **Condition Set 106:** FunFam id: Anthranilate synthase beta subunit 1 (CATH.FunFam:3.40.50.880:FF:000027)
    AND taxon: Embryophyta (NCBITaxon:3193)


    **Condition Set 107:** FunFam id: Aspartate aminotransferase (CATH.FunFam:3.40.640.10:FF:000015)
    AND taxon: Enterobacteriaceae (NCBITaxon:543)


    **Condition Set 108:** FunFam id: Histidine biosynthesis bifunctional protein
    HisIE (CATH.FunFam:1.10.287.1080:FF:000002)


    **Condition Set 109:** FunFam id: Phenylalanine-4-hydroxylase (CATH.FunFam:1.10.800.10:FF:000003)


    **Condition Set 110:** FunFam id: Cysteine dioxygenase 1 (CATH.FunFam:2.60.120.10:FF:000045)


    **Condition Set 111:** FunFam id: D-alanine aminotransferase (CATH.FunFam:3.20.10.10:FF:000002)


    **Condition Set 112:** FunFam id: D-serine dehydratase (CATH.FunFam:3.20.20.10:FF:000016)


    **Condition Set 113:** FunFam id: 3-isopropylmalate dehydratase large subunit
    (CATH.FunFam:3.30.499.10:FF:000006)


    **Condition Set 114:** FunFam id: Gamma-glutamyl phosphate reductase (CATH.FunFam:3.40.309.10:FF:000006)


    **Condition Set 115:** FunFam id: Carnosine N-methyltransferase 1 (CATH.FunFam:3.40.50.150:FF:000094)


    **Condition Set 116:** FunFam id: Histidinol dehydrogenase (CATH.FunFam:3.40.50.1980:FF:000001)


    **Condition Set 117:** FunFam id: D-3-phosphoglycerate dehydrogenase (CATH.FunFam:3.40.50.720:FF:000041)


    **Condition Set 118:** FunFam id: Glutamate dehydrogenase (CATH.FunFam:3.40.50.720:FF:001273)


    **Condition Set 119:** FunFam id: Kynureninase (CATH.FunFam:3.40.640.10:FF:000031)


    **Condition Set 120:** FunFam id: Aspartate aminotransferase (CATH.FunFam:3.40.640.10:FF:000044)


    **Condition Set 121:** FunFam id: Arginase (CATH.FunFam:3.40.800.10:FF:000005)


    **Condition Set 122:** FunFam id: phenylalanine--tRNA ligase beta subunit (CATH.FunFam:3.50.40.10:FF:000002)


    **Condition Set 123:** FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:1.10.1030.10:FF:000001)
    AND FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:3.20.20.140:FF:000036)
    AND FunFam id: CAD protein-like isoform X1 (CATH.FunFam:3.40.50.20:FF:000011)


    **Condition Set 124:** FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:1.10.1030.10:FF:000002)
    AND FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:3.30.1490.20:FF:000001)
    AND FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:3.40.50.1380:FF:000004)


    **Condition Set 125:** FunFam id: Glutamine--tRNA ligase (CATH.FunFam:1.10.1160.10:FF:000001)
    AND FunFam id: Glutamine--tRNA ligase (CATH.FunFam:3.90.800.10:FF:000001) AND
    taxon: Saccharomycetales (NCBITaxon:4892)


    **Condition Set 126:** FunFam id: Glutaminase kidney isoform, mitochondrial (CATH.FunFam:1.10.238.210:FF:000001)
    AND FunFam id: Glutaminase liver isoform, mitochondrial (CATH.FunFam:1.25.40.20:FF:000019)
    AND taxon: Haplorrhini (NCBITaxon:376913)


    **Condition Set 127:** FunFam id: 2-isopropylmalate synthase 1 chloroplastic (CATH.FunFam:1.10.238.260:FF:000003)
    AND FunFam id: 2-isopropylmalate synthase (CATH.FunFam:3.20.20.70:FF:000010) AND
    FunFam id: 2-isopropylmalate synthase B (CATH.FunFam:3.30.160.270:FF:000004)


    **Condition Set 128:** FunFam id: Tyrosine--tRNA ligase (CATH.FunFam:1.10.240.10:FF:000001)
    AND FunFam id: Tyrosine--tRNA ligase (CATH.FunFam:3.10.290.10:FF:000017) AND FunFam
    id: Tyrosine--tRNA ligase (CATH.FunFam:3.40.50.620:FF:000107)


    **Condition Set 129:** FunFam id: Argininosuccinate lyase (CATH.FunFam:1.10.275.10:FF:000002)
    AND FunFam id: Argininosuccinate lyase (CATH.FunFam:1.20.200.10:FF:000002) AND
    taxon: Phasianinae (NCBITaxon:9072)


    **Condition Set 130:** FunFam id: Histidine ammonia-lyase (CATH.FunFam:1.10.275.10:FF:000005)
    AND FunFam id: Tyrosine ammonia-lyase (CATH.FunFam:1.20.200.10:FF:000012) AND
    taxon: Cyanobacteriota (NCBITaxon:1117)


    **Condition Set 131:** FunFam id: Histidine ammonia-lyase (CATH.FunFam:1.10.275.10:FF:000007)
    AND FunFam id: Histidine ammonia-lyase (CATH.FunFam:1.20.200.10:FF:000003) AND
    taxon: Myomorpha (NCBITaxon:1963758)


    **Condition Set 132:** FunFam id: Glutamate dehydrogenase (CATH.FunFam:1.10.285.10:FF:000003)
    AND FunFam id: Glutamate dehydrogenase (CATH.FunFam:3.40.50.720:FF:000030) AND
    taxon: Saccharomycetaceae (NCBITaxon:4893)


    **Condition Set 133:** FunFam id: Methionine--tRNA ligase, cytoplasmic (CATH.FunFam:1.10.287.10:FF:000009)
    AND FunFam id: methionine--tRNA ligase, cytoplasmic (CATH.FunFam:1.10.730.10:FF:000010)
    AND FunFam id: Methionine--tRNA ligase, cytoplasmic (CATH.FunFam:1.20.1050.10:FF:000026)


    **Condition Set 134:** FunFam id: Glutamate dehydrogenase 1, mitochondrial (CATH.FunFam:1.10.287.140:FF:000001)
    AND FunFam id: Glutamate dehydrogenase 1, mitochondrial (CATH.FunFam:3.40.50.10860:FF:000007)
    AND taxon: Catarrhini (NCBITaxon:9526)


    **Condition Set 135:** FunFam id: Amine oxidase (CATH.FunFam:1.10.405.10:FF:000004)
    AND FunFam id: Amine oxidase (CATH.FunFam:3.50.50.60:FF:000450) AND FunFam id:
    Amine oxidase (CATH.FunFam:3.90.660.10:FF:000011)


    **Condition Set 136:** FunFam id: Methylenetetrahydrofolate dehydrogenase (NADP+
    dependent) 1 like (CATH.FunFam:1.10.8.770:FF:000001) AND FunFam id: Putative formate--tetrahydrofolate
    ligase (CATH.FunFam:3.10.410.10:FF:000001) AND FunFam id: C-1-tetrahydrofolate
    synthase, cytoplasmic (CATH.FunFam:3.40.50.300:FF:000245)


    **Condition Set 137:** FunFam id: Tyrosine 3-monooxygenase (CATH.FunFam:1.10.800.10:FF:000002)
    AND FunFam id: Tyrosine 3-monooxygenase (CATH.FunFam:3.30.70.260:FF:000024) AND
    taxon: Muroidea (NCBITaxon:337687)


    **Condition Set 138:** FunFam id: Bifunctional protein PutA (CATH.FunFam:1.20.5.460:FF:000001)
    AND FunFam id: Bifunctional protein PutA (CATH.FunFam:1.20.5.550:FF:000001) AND
    FunFam id: Bifunctional protein PutA (CATH.FunFam:3.20.20.220:FF:000004)


    **Condition Set 139:** FunFam id: Methionine synthase reductase (CATH.FunFam:1.20.990.10:FF:000007)
    AND FunFam id: methionine synthase reductase (CATH.FunFam:3.40.50.360:FF:000025)
    AND FunFam id: NADPH--cytochrome P450 reductase (CATH.FunFam:3.40.50.80:FF:000018)


    **Condition Set 140:** FunFam id: Alanine racemase (CATH.FunFam:2.40.37.10:FF:000002)
    AND FunFam id: Alanine racemase (CATH.FunFam:3.20.20.10:FF:000002) AND taxon:
    Escherichia (NCBITaxon:561)


    **Condition Set 141:** FunFam id: 4-hydroxyproline betaine 2-epimerase (CATH.FunFam:3.20.20.120:FF:000020)
    AND FunFam id: Hydrophobic dipeptide epimerase (CATH.FunFam:3.30.390.10:FF:000009)
    AND taxon: Hyphomicrobiales (NCBITaxon:356)


    **Condition Set 142:** FunFam id: Putative selenophosphate synthetase (CATH.FunFam:3.30.1330.10:FF:000023)
    AND FunFam id: Selenide, water dikinase (CATH.FunFam:3.90.650.10:FF:000010) AND
    taxon: Discoba (NCBITaxon:2611352)


    **Condition Set 143:** FunFam id: D-3-phosphoglycerate dehydrogenase (CATH.FunFam:3.30.1330.90:FF:000005)
    AND FunFam id: D-3-phosphoglycerate dehydrogenase (CATH.FunFam:3.40.50.720:FF:000021)
    AND taxon: Muridae (NCBITaxon:10066)


    **Condition Set 144:** FunFam id: beta-citrylglutamate synthase B isoform X1 (CATH.FunFam:3.30.1490.20:FF:000011)
    AND FunFam id: beta-citrylglutamate synthase B isoform X1 (CATH.FunFam:3.30.470.20:FF:000022)
    AND taxon: Hominidae (NCBITaxon:9604)


    **Condition Set 145:** FunFam id: Bifunctional acetylglutamate kinase/N-acetyl-gamma-glutamyl-phosphate
    reductase (CATH.FunFam:3.30.360.10:FF:000019) AND FunFam id: N-acetyl-gamma-glutamyl-phosphate
    reductase, variant (CATH.FunFam:3.40.1160.10:FF:000011) AND FunFam id: Bifunctional
    acetylglutamate kinase/N-acetyl-gamma-glutamyl-phosphate reductase (CATH.FunFam:3.40.630.30:FF:000029)


    **Condition Set 146:** FunFam id: Glycine N-methyltransferase (CATH.FunFam:3.30.46.10:FF:000001)
    AND FunFam id: Glycine N-methyltransferase (CATH.FunFam:3.40.50.150:FF:000113)
    AND taxon: Murinae (NCBITaxon:39107)


    **Condition Set 147:** FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:3.30.470.20:FF:000001)
    AND FunFam id: Carbamoyl-phosphate synthase (glutamine-hydrolyzing) (CATH.FunFam:3.30.470.20:FF:000004)
    AND taxon: Taphrinomycotina (NCBITaxon:451866)


    **Condition Set 148:** FunFam id: Inositol-1-monophosphatase (CATH.FunFam:3.30.540.10:FF:000003)
    AND FunFam id: Histidinol phosphatase (CATH.FunFam:3.40.190.80:FF:000010) AND
    taxon: Actinomycetota (NCBITaxon:201174)


    **Condition Set 149:** FunFam id: ATP phosphoribosyltransferase, chloroplastic
    (CATH.FunFam:3.30.70.120:FF:000007) AND FunFam id: ATP phosphoribosyltransferase
    2, chloroplastic (CATH.FunFam:3.40.190.10:FF:000118) AND taxon: Spermatophyta
    (NCBITaxon:58024)


    **Condition Set 150:** FunFam id: Probable histidine--tRNA ligase, mitochondrial
    (CATH.FunFam:3.30.930.10:FF:000021) AND FunFam id: histidine--tRNA ligase, cytoplasmic
    isoform X1 (CATH.FunFam:3.40.50.800:FF:000008) AND taxon: Homo (NCBITaxon:9605)


    **Condition Set 151:** FunFam id: Threonine--tRNA ligase (CATH.FunFam:3.30.930.10:FF:000076)
    AND FunFam id: Threonine--tRNA ligase (CATH.FunFam:3.40.50.800:FF:000001) AND
    FunFam id: Threonine--tRNA ligase (CATH.FunFam:3.50.80.10:FF:000004)


    **Condition Set 152:** FunFam id: Glutamate dehydrogenase (CATH.FunFam:3.40.50.10860:FF:000008)
    AND FunFam id: Glutamate dehydrogenase (CATH.FunFam:3.40.50.720:FF:000212) AND
    taxon: Bacillota (NCBITaxon:1239)


    **Condition Set 153:** FunFam id: Tryptophan synthase beta chain (CATH.FunFam:3.40.50.1100:FF:000001)
    AND FunFam id: Tryptophan synthase beta chain (CATH.FunFam:3.40.50.1100:FF:000004)
    AND taxon: Magnoliopsida (NCBITaxon:3398)


    **Condition Set 154:** FunFam id: 2-oxoisovalerate dehydrogenase subunit beta
    1, mitochondrial (CATH.FunFam:3.40.50.920:FF:000004) AND FunFam id: Pyruvate dehydrogenase
    E1 beta subunit (CATH.FunFam:3.40.50.970:FF:000001) AND taxon: eudicotyledons
    (NCBITaxon:71240)


    **Condition Set 155:** FunFam id: 4-aminobutyrate aminotransferase, mitochondrial
    (CATH.FunFam:3.40.640.10:FF:000029) AND FunFam id: 4-aminobutyrate aminotransferase,
    mitochondrial (CATH.FunFam:3.90.1150.10:FF:000191) AND taxon: Laurasiatheria (NCBITaxon:314145)


    **Condition Set 156:** FunFam id: probable low-specificity L-threonine aldolase
    1 (CATH.FunFam:3.40.640.10:FF:000063) AND FunFam id: Low-specificity L-threonine
    aldolase (CATH.FunFam:3.90.1150.10:FF:000041) AND taxon: Gunneridae (NCBITaxon:91827)


    **Condition Set 157:** FunFam id: Serine hydroxymethyltransferase (CATH.FunFam:3.40.640.10:FF:000097)
    AND FunFam id: Serine hydroxymethyltransferase (CATH.FunFam:3.90.1150.10:FF:000005)
    AND FunFam id: Serine hydroxymethyltransferase, mitochondrial (CATH.FunFam:3.90.1150.10:FF:000048)


    **Condition Set 158:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1
    (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase
    PM20D1 (CATH.FunFam:3.40.630.10:FF:000027)


    **Condition Set 159:** FunFam id: Phenylalanine aminomutase (L-beta-phenylalanine
    forming) (CATH.FunFam:1.10.274.20:FF:000003) AND taxon: Pinopsida (NCBITaxon:58019)


    **Condition Set 160:** FunFam id: Prephenate dehydrogenase [NADP(+)] (CATH.FunFam:1.10.3660.10:FF:000004)
    AND FunFam id: Prephenate dehydrogenase [NADP(+)] (CATH.FunFam:3.40.50.720:FF:000339)


    **Condition Set 161:** FunFam id: Pyrroline-5-carboxylate reductase (CATH.FunFam:1.10.3730.10:FF:000001)
    AND FunFam id: Pyrroline-5-carboxylate reductase (CATH.FunFam:3.40.50.720:FF:000105)


    **Condition Set 162:** FunFam id: Cytochrome P450 9 (CATH.FunFam:1.10.630.10:FF:000037)
    AND taxon: malvids (NCBITaxon:91836)


    **Condition Set 163:** FunFam id: Tyrosine 3-monooxygenase (CATH.FunFam:1.10.800.10:FF:000004)
    AND taxon: Nematoda (NCBITaxon:6231)


    **Condition Set 164:** FunFam id: Solute carrier family 25 member 44 (CATH.FunFam:1.50.40.10:FF:000033)
    AND FunFam id: Solute carrier family 25 member 44 (CATH.FunFam:1.50.40.10:FF:000108)


    **Condition Set 165:** FunFam id: GD20529 (CATH.FunFam:2.120.10.30:FF:000092)
    AND taxon: Ecdysozoa (NCBITaxon:1206794)


    **Condition Set 166:** FunFam id: Lysine--tRNA ligase (CATH.FunFam:2.40.50.140:FF:000024)
    AND FunFam id: Lysine--tRNA ligase (CATH.FunFam:3.30.930.10:FF:000001)


    **Condition Set 167:** FunFam id: Homogentisate 1,2-dioxygenase (CATH.FunFam:2.60.120.10:FF:000036)
    AND taxon: Pseudomonadales (NCBITaxon:72274)


    **Condition Set 168:** FunFam id: Homogentisate 1,2-dioxygenase (CATH.FunFam:2.60.120.10:FF:000053)
    AND taxon: Pezizomycotina (NCBITaxon:147538)


    **Condition Set 169:** FunFam id: 4-hydroxyphenylpyruvate dioxygenase (CATH.FunFam:3.10.180.10:FF:000008)
    AND FunFam id: 4-hydroxyphenylpyruvate dioxygenase (CATH.FunFam:3.10.180.10:FF:000022)


    **Condition Set 170:** FunFam id: Branched-chain-amino-acid aminotransferase (CATH.FunFam:3.20.10.10:FF:000009)
    AND taxon: Actinomycetes (NCBITaxon:1760)


    **Condition Set 171:** FunFam id: Ornithine decarboxylase 1 (CATH.FunFam:3.20.20.10:FF:000006)
    AND taxon: Mus (NCBITaxon:862507)


    **Condition Set 172:** FunFam id: Homocysteine S-methyltransferase (CATH.FunFam:3.20.20.330:FF:000002)
    AND taxon: Camelineae (NCBITaxon:980083)


    **Condition Set 173:** FunFam id: Tryptophan biosynthesis protein TRP1 (CATH.FunFam:3.20.20.70:FF:000075)
    AND taxon: Pentapetalae (NCBITaxon:1437201)


    **Condition Set 174:** FunFam id: Tryptophan synthase alpha chain, chloroplastic
    (CATH.FunFam:3.20.20.70:FF:000107) AND taxon: Brassicales (NCBITaxon:3699)


    **Condition Set 175:** FunFam id: Multifunctional tryptophan biosynthesis protein
    (CATH.FunFam:3.20.20.70:FF:000136) AND FunFam id: Multifunctional tryptophan biosynthesis
    protein (CATH.FunFam:3.40.50.880:FF:000031)


    **Condition Set 176:** FunFam id: selenide, water dikinase 2 (CATH.FunFam:3.30.1330.10:FF:000018)
    AND FunFam id: Selenide, water dikinase 1 (CATH.FunFam:3.90.650.10:FF:000003)


    **Condition Set 177:** FunFam id: Malate/L-lactate family dehydrogenase (CATH.FunFam:3.30.1370.60:FF:000002)
    AND taxon: Pseudomonadaceae (NCBITaxon:135621)


    **Condition Set 178:** FunFam id: Bifunctional aspartokinase/homoserine dehydrogenase
    (CATH.FunFam:3.30.2130.10:FF:000001) AND FunFam id: Probable aspartokinase (CATH.FunFam:3.40.1160.10:FF:000023)


    **Condition Set 179:** FunFam id: Imidazoleglycerol-phosphate dehydratase HisB
    (CATH.FunFam:3.30.230.40:FF:000001) AND FunFam id: Imidazoleglycerol-phosphate
    dehydratase (CATH.FunFam:3.30.230.40:FF:000005)


    **Condition Set 180:** FunFam id: Enterobactin synthetase component F (CATH.FunFam:3.30.300.30:FF:000010)
    AND FunFam id: Non-ribosomal peptide synthetase (CATH.FunFam:3.40.50.12780:FF:000012)


    **Condition Set 181:** FunFam id: N-acetyldiaminopimelate deacetylase (CATH.FunFam:3.30.70.360:FF:000001)
    AND taxon: Bacilli (NCBITaxon:91061)


    **Condition Set 182:** FunFam id: phenylalanine--tRNA ligase, mitochondrial (CATH.FunFam:3.30.70.380:FF:000002)
    AND FunFam id: Phenylalanyl-tRNA synthetase mitochondrial (CATH.FunFam:3.30.930.10:FF:000053)


    **Condition Set 183:** FunFam id: Threonine dehydratase (CATH.FunFam:3.40.1020.10:FF:000003)
    AND taxon: Solanum subgen. Lycopersicon (NCBITaxon:49274)


    **Condition Set 184:** FunFam id: Delta-1-pyrroline-5-carboxylate synthase (CATH.FunFam:3.40.1160.10:FF:000010)
    AND FunFam id: Delta-1-pyrroline-5-carboxylate synthase (CATH.FunFam:3.40.309.10:FF:000011)


    **Condition Set 185:** FunFam id: THR4p Threonine synthase (CATH.FunFam:3.40.50.1100:FF:000046)
    AND FunFam id: THR4p Threonine synthase (CATH.FunFam:3.90.1380.10:FF:000003)


    **Condition Set 186:** FunFam id: (R)-2-hydroxyisocaproyl-CoA dehydratase beta
    subunit (CATH.FunFam:3.40.50.11890:FF:000002) AND taxon: Clostridia (NCBITaxon:186801)


    **Condition Set 187:** FunFam id: Argininosuccinate synthase (CATH.FunFam:3.40.50.620:FF:000019)
    AND FunFam id: Argininosuccinate synthase (CATH.FunFam:3.90.1260.10:FF:000003)


    **Condition Set 188:** FunFam id: Glutamine-dependent NAD(+) synthetase (CATH.FunFam:3.40.50.620:FF:000036)
    AND FunFam id: Glutamine-dependent NAD(+) synthetase (CATH.FunFam:3.60.110.10:FF:000007)


    **Condition Set 189:** FunFam id: Saccharopine dehydrogenase [NAD(+), L-lysine-forming]
    (CATH.FunFam:3.40.50.720:FF:000217) AND FunFam id: Saccharopine dehydrogenase
    [NAD(+), L-lysine-forming] (CATH.FunFam:3.40.50.720:FF:000423)


    **Condition Set 190:** FunFam id: N5-(Carboxyethyl)ornithine synthase (CATH.FunFam:3.40.50.720:FF:000488)
    AND FunFam id: N(5)-(Carboxyethyl)ornithine synthase (CATH.FunFam:3.40.50.720:FF:000489)


    **Condition Set 191:** FunFam id: Glycine--tRNA ligase (CATH.FunFam:3.40.50.800:FF:000002)
    AND taxon: Mycobacteriales (NCBITaxon:85007)


    **Condition Set 192:** FunFam id: Carbamoyl-phosphate synthase arginine-specific
    small chain (CATH.FunFam:3.40.50.880:FF:000016) AND FunFam id: Carbamoyl-phosphate
    synthase arginine-specific small chain (CATH.FunFam:3.50.30.20:FF:000003)


    **Condition Set 193:** FunFam id: 2-oxoisovalerate dehydrogenase subunit alpha
    (CATH.FunFam:3.40.50.970:FF:000015) AND taxon: Brassicaceae (NCBITaxon:3700)


    **Condition Set 194:** FunFam id: Serine hydroxymethyltransferase (CATH.FunFam:3.40.640.10:FF:000001)
    AND taxon: Mycobacteriaceae (NCBITaxon:1762)


    **Condition Set 195:** FunFam id: Acetylornithine aminotransferase (CATH.FunFam:3.40.640.10:FF:000004)
    AND FunFam id: Succinylornithine transaminase (CATH.FunFam:3.90.1150.10:FF:000009)


    **Condition Set 196:** FunFam id: Kynurenine--oxoglutarate transaminase 3 (CATH.FunFam:3.40.640.10:FF:000024)
    AND FunFam id: Kynurenine--oxoglutarate transaminase 3 (CATH.FunFam:3.90.1150.10:FF:000021)


    **Condition Set 197:** FunFam id: Cystathionine gamma-lyase (CATH.FunFam:3.40.640.10:FF:000046)
    AND taxon: Arabidopsis (NCBITaxon:3701)


    **Condition Set 198:** FunFam id: Valine--tRNA ligase, mitochondrial (CATH.FunFam:3.90.740.10:FF:000005)
    AND taxon: Schizosaccharomycetales (NCBITaxon:34346)


    **Condition Set 199:** FunFam id: Tryptophan 2,3-dioxygenase (CATH.FunFam:1.20.58.480:FF:000001)


    **Condition Set 200:** FunFam id: Serine acetyltransferase (CATH.FunFam:2.160.10.10:FF:000007)


    **Condition Set 201:** FunFam id: Homogentisate 1,2-dioxygenase (CATH.FunFam:2.60.120.10:FF:000026)


    **Condition Set 202:** FunFam id: Histidine biosynthesis bifunctional protein
    HisIE (CATH.FunFam:3.10.20.810:FF:000001)


    **Condition Set 203:** FunFam id: 2-amino-3-carboxymuconate-6-semialdehyde decarboxylase
    (CATH.FunFam:3.20.20.140:FF:000029)


    **Condition Set 204:** FunFam id: Methylenetetrahydrofolate reductase (CATH.FunFam:3.20.20.220:FF:000003)


    **Condition Set 205:** FunFam id: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]
    imidazole-4-carboxamide isomerase (CATH.FunFam:3.20.20.70:FF:000009)


    **Condition Set 206:** FunFam id: Tryptophan synthase alpha chain (CATH.FunFam:3.20.20.70:FF:000037)


    **Condition Set 207:** FunFam id: Imidazole glycerol phosphate synthase hisHF
    (CATH.FunFam:3.20.20.70:FF:000094)


    **Condition Set 208:** FunFam id: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino]
    imidazole-4-carboxamide isomerase, chloroplastic (CATH.FunFam:3.20.20.70:FF:000110)


    **Condition Set 209:** FunFam id: Homoserine kinase (CATH.FunFam:3.30.230.10:FF:000068)


    **Condition Set 210:** FunFam id: Homoserine dehydrogenase (CATH.FunFam:3.30.360.10:FF:000005)


    **Condition Set 211:** FunFam id: Amino-acid acetyltransferase (CATH.FunFam:3.40.1160.10:FF:000005)


    **Condition Set 212:** FunFam id: Cysteine synthase (o-acetylserine) (CATH.FunFam:3.40.50.1100:FF:000011)


    **Condition Set 213:** FunFam id: Cysteine synthase (CATH.FunFam:3.40.50.1100:FF:000067)


    **Condition Set 214:** FunFam id: Ornithine carbamoyltransferase (CATH.FunFam:3.40.50.1370:FF:000004)


    **Condition Set 215:** FunFam id: Tyrosine--tRNA ligase (CATH.FunFam:3.40.50.620:FF:000008)


    **Condition Set 216:** FunFam id: L-2-aminoadipate reductase (CATH.FunFam:3.40.50.720:FF:000787)


    **Condition Set 217:** FunFam id: Amino-acid acetyltransferase, mitochondrial
    (CATH.FunFam:3.40.630.30:FF:000049)


    **Condition Set 218:** FunFam id: Aminotransferase (CATH.FunFam:3.40.640.10:FF:000126)


    **Condition Set 219:** FunFam id: HISTIDINE BIOSYNTHESIS 6B (CATH.FunFam:3.40.640.10:FF:000131)


    **Condition Set 220:** FunFam id: N-succinylarginine dihydrolase (CATH.FunFam:3.75.10.20:FF:000001)


    **Condition Set 221:** FunFam id: Cystathionine gamma-synthase (CATH.FunFam:3.90.1150.10:FF:000033)


    **Condition Set 222:** FunFam id: Probable cystathionine gamma-synthase (CATH.FunFam:3.90.1150.10:FF:000063)


    **Condition Set 223:** FunFam id: kynurenine--oxoglutarate transaminase 1 (CATH.FunFam:3.90.1150.10:FF:000275)


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
citation_count: 59
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00026411
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0006520 (amino acid metabolic process)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** InterPro id: Aminoacyl-tRNA synthetase, class II (InterPro:IPR006195) AND InterPro id: Class II Aminoacyl-tRNA synthetase/Biotinyl protein ligase (BPL) and lipoyl protein ligase (LPL) (InterPro:IPR045864) AND taxon: Saccharomycotina (NCBITaxon:147537)

**Condition Set 2:** InterPro id: Tryptophan synthase beta chain-like, PALP domain (InterPro:IPR001926) AND InterPro id: Cysteine synthase/Cystathionine beta-synthase (InterPro:IPR050214) AND taxon: Bacteria (NCBITaxon:2)

**Condition Set 3:** InterPro id: Aspartate/glutamate/uridylate kinase (InterPro:IPR001048) AND InterPro id: Glutamate/acetylglutamate kinase (InterPro:IPR001057) AND InterPro id: Glutamate 5-kinase/delta-1-pyrroline-5-carboxylate synthase (InterPro:IPR005715)

**Condition Set 4:** InterPro id: Tryptophan synthase beta chain-like, PALP domain superfamily (InterPro:IPR036052) AND taxon: Bacillati (NCBITaxon:1783272)

**Condition Set 5:** InterPro id: GPR domain (InterPro:IPR000965) AND InterPro id: Aldehyde dehydrogenase domain (InterPro:IPR015590) AND InterPro id: Aldehyde/histidinol dehydrogenase (InterPro:IPR016161)

**Condition Set 6:** InterPro id: Aminoacyl-tRNA synthetase, class I, conserved site (InterPro:IPR001412) AND InterPro id: Rossmann-like alpha/beta/alpha sandwich fold (InterPro:IPR014729) AND taxon: Pseudomonadota (NCBITaxon:1224)

**Condition Set 7:** InterPro id: Ornithine/putrescine carbamoyltransferase (InterPro:IPR002292) AND InterPro id: Aspartate/ornithine carbamoyltransferase (InterPro:IPR006130) AND InterPro id: Aspartate/ornithine carbamoyltransferase, Asp/Orn-binding domain (InterPro:IPR006131)

**Condition Set 8:** InterPro id: Aminotransferases, class-I, pyridoxal-phosphate-binding site (InterPro:IPR004838) AND InterPro id: Ethylene and sulfur compound biosynthesis-related protein (InterPro:IPR050478) AND taxon: eudicotyledons (NCBITaxon:71240)

**Condition Set 9:** InterPro id: Tryptophan/Indoleamine 2,3-dioxygenase-like (InterPro:IPR037217) AND taxon: Metazoa (NCBITaxon:33208)

**Condition Set 10:** InterPro id: ACT-like domain (InterPro:IPR045865) AND taxon: Fungi (NCBITaxon:4751)

**Condition Set 11:** InterPro id: Aminoacyl-tRNA synthetase, class II (G/ P/ S/T) (InterPro:IPR002314) AND InterPro id: Anticodon-binding (InterPro:IPR004154) AND taxon: Chordata (NCBITaxon:7711)

**Condition Set 12:** InterPro id: Asparaginase/glutaminase-like (InterPro:IPR006034) AND InterPro id: L-asparaginase, C-terminal (InterPro:IPR027473) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 13:** InterPro id: TPP-binding enzyme, conserved site (InterPro:IPR000399) AND InterPro id: Thiamine pyrophosphate enzyme, TPP-binding (InterPro:IPR011766) AND InterPro id: Acetolactate synthase, large subunit, biosynthetic (InterPro:IPR012846)

**Condition Set 14:** InterPro id: Semialdehyde dehydrogenase, NAD-binding (InterPro:IPR000534) AND InterPro id: NAD(P)-binding domain superfamily (InterPro:IPR036291) AND taxon: Dikarya (NCBITaxon:451864)

**Condition Set 15:** InterPro id: Pyruvate carboxyltransferase (InterPro:IPR000891) AND InterPro id: Alpha-isopropylmalate/homocitrate synthase, conserved site (InterPro:IPR002034) AND InterPro id: 2-isopropylmalate synthase LeuA, allosteric (dimerisation) domain (InterPro:IPR013709)

**Condition Set 16:** InterPro id: Aromatic amino acid hydroxylase (InterPro:IPR001273) AND InterPro id: Aromatic amino acid hydroxylase, iron/copper binding site (InterPro:IPR018301) AND PANTHER id: PTHR11473:SF24

**Condition Set 17:** InterPro id: ATP phosphoribosyltransferase HisG (InterPro:IPR001348) AND InterPro id: Nitrogen regulatory PII-like, alpha/beta (InterPro:IPR011322) AND InterPro id: Histidine biosynthesis HisG, C-terminal (InterPro:IPR013115)

**Condition Set 18:** InterPro id: Indole-3-glycerol phosphate synthase, conserved site (InterPro:IPR001468) AND InterPro id: Ribulose-phosphate binding barrel (InterPro:IPR011060) AND InterPro id: Aldolase-type TIM barrel (InterPro:IPR013785)

**Condition Set 19:** InterPro id: Anthranilate synthase component I, PabB-like (InterPro:IPR005256) AND InterPro id: ADC synthase (InterPro:IPR005801) AND InterPro id: Anthranilate synthase component I, N-terminal (InterPro:IPR006805)

**Condition Set 20:** InterPro id: Homogentisate 1,2-dioxygenase (InterPro:IPR005708) AND InterPro id: RmlC-like cupin domain superfamily (InterPro:IPR011051) AND InterPro id: RmlC-like jelly roll fold (InterPro:IPR014710)

**Condition Set 21:** InterPro id: Aconitase A/isopropylmalate dehydratase small subunit, swivel domain (InterPro:IPR000573) AND InterPro id: Aconitase/3-isopropylmalate dehydratase large subunit, alpha/beta/alpha domain (InterPro:IPR001030) AND InterPro id: Isopropylmalate dehydratase and related enzymes (InterPro:IPR050067)

**Condition Set 22:** InterPro id: Dihydroxy-acid/6-phosphogluconate dehydratase, N-terminal (InterPro:IPR000581) AND InterPro id: Dihydroxy-acid dehydratase (InterPro:IPR004404) AND InterPro id: Dihydroxy-acid/6-phosphogluconate dehydratase, conserved site (InterPro:IPR020558)

**Condition Set 23:** InterPro id: Aminotransferase class IV (InterPro:IPR001544) AND InterPro id: Branched-chain amino acid aminotransferase II (InterPro:IPR005786) AND PANTHER id: PTHR11825:SF44

**Condition Set 24:** InterPro id: Acetylornithine/Succinylornithine transaminase family (InterPro:IPR004636) AND InterPro id: Aminotransferase class-III (InterPro:IPR005814) AND InterPro id: Pyridoxal phosphate-dependent transferase, major domain (InterPro:IPR015421)

**Condition Set 25:** InterPro id: Anthranilate synthase/para-aminobenzoate synthase like domain (InterPro:IPR006221) AND InterPro id: Glutamine amidotransferase (InterPro:IPR017926) AND PANTHER id: PTHR43418:SF4

**Condition Set 26:** InterPro id: DHS-like NAD/FAD-binding domain superfamily (InterPro:IPR029035) AND InterPro id: Thiamin diphosphate-binding fold (InterPro:IPR029061) AND PANTHER id: PTHR18968:SF13

**Condition Set 27:** InterPro id: Aspartate-semialdehyde dehydrogenase, conserved site (InterPro:IPR000319) AND InterPro id: Semialdehyde dehydrogenase, dimerisation domain (InterPro:IPR012280)

**Condition Set 28:** InterPro id: Tryptophan 2,3-dioxygenase (InterPro:IPR004981) AND PANTHER id: PTHR10138:SF0

**Condition Set 29:** InterPro id: Aminoacyl-tRNA synthetase, class Ia, anticodon-binding (InterPro:IPR009080) AND taxon: Gammaproteobacteria (NCBITaxon:1236)

**Condition Set 30:** InterPro id: Indoleamine 2,3-dioxygenase (InterPro:IPR000898)

**Condition Set 31:** InterPro id: Aminotransferase class V domain (InterPro:IPR000192) AND InterPro id: Pyridoxal phosphate-dependent transferase, small domain (InterPro:IPR015422) AND InterPro id: Phosphoserine aminotransferase (InterPro:IPR022278)

**Condition Set 32:** InterPro id: Serine/threonine dehydratase, pyridoxal-phosphate-binding site (InterPro:IPR000634) AND InterPro id: Threonine dehydratase, ACT-like domain (InterPro:IPR001721) AND PANTHER id: PTHR48078:SF11

**Condition Set 33:** InterPro id: WHEP-TRS domain (InterPro:IPR000738) AND InterPro id: uS15/NS1, RNA-binding domain superfamily (InterPro:IPR009068) AND InterPro id: Glutathione S-transferase, C-terminal domain superfamily (InterPro:IPR036282)

**Condition Set 34:** InterPro id: Homoserine kinase (InterPro:IPR000870) AND InterPro id: GHMP kinase, ATP-binding, conserved site (InterPro:IPR006203) AND InterPro id: GHMP kinase N-terminal domain (InterPro:IPR006204)

**Condition Set 35:** InterPro id: Cysteine synthase/cystathionine beta-synthase, pyridoxal-phosphate attachment site (InterPro:IPR001216) AND InterPro id: Cystathionine beta-synthase (InterPro:IPR005857) AND InterPro id: CBS domain superfamily (InterPro:IPR046342)

**Condition Set 36:** InterPro id: Chorismate mutase II, prokaryotic-type (InterPro:IPR002701) AND InterPro id: Chorismate mutase, AroQ class, eukaryotic type (InterPro:IPR008238) AND taxon: Ascomycota (NCBITaxon:4890)

**Condition Set 37:** InterPro id: Acetolactate synthase, small subunit (InterPro:IPR004789) AND InterPro id: AHAS, ACT domain (InterPro:IPR039557) AND InterPro id: Acetolactate synthase small subunit-like, ACT domain (InterPro:IPR054480)

**Condition Set 38:** InterPro id: B3/B4 tRNA-binding domain (InterPro:IPR005146) AND InterPro id: tRNA synthetase, B5-domain (InterPro:IPR005147) AND InterPro id: Putative DNA-binding domain superfamily (InterPro:IPR009061)

**Condition Set 39:** InterPro id: FAD dependent oxidoreductase (InterPro:IPR006076) AND PANTHER id: PTHR11530:SF11 AND taxon: Craniata (NCBITaxon:89593)

**Condition Set 40:** InterPro id: Tryptophan synthase, alpha chain (InterPro:IPR002028) AND InterPro id: Tryptophan synthase, alpha chain, active site (InterPro:IPR018204)

**Condition Set 41:** FunFam id: 1-aminocyclopropane-1-carboxylate synthase 3 (CATH.FunFam:3.40.640.10:FF:000051) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 42:** FunFam id: 5-methyltetrahydropteroyltriglutamate--homocysteine methyltransferase (CATH.FunFam:3.20.20.210:FF:000003)

**Condition Set 43:** FunFam id: Cystathionine beta-synthase (CATH.FunFam:3.40.50.1100:FF:000003)

**Condition Set 44:** FunFam id: Related to CYS4-cystathionine beta-synthase (CATH.FunFam:3.40.50.1100:FF:000118)

**Condition Set 45:** FunFam id: Probable aspartate-semialdehyde dehydrogenase (CATH.FunFam:3.30.360.10:FF:000016) AND FunFam id: Aspartate-semialdehyde dehydrogenase (CATH.FunFam:3.40.50.720:FF:000200) AND taxon: Fungi (NCBITaxon:4751)

**Condition Set 46:** FunFam id: Glycine--tRNA ligase 2 (CATH.FunFam:3.30.720.200:FF:000001) AND FunFam id: Glycyl-tRNA synthetase 1 (CATH.FunFam:3.30.930.10:FF:000010) AND FunFam id: Glycyl-tRNA synthetase (CATH.FunFam:3.30.930.10:FF:000158)

**Condition Set 47:** FunFam id: L-asparaginase 2 (CATH.FunFam:3.40.50.1170:FF:000001) AND FunFam id: L-asparaginase I (CATH.FunFam:3.40.50.40:FF:000006) AND taxon: Dikarya (NCBITaxon:451864)

**Condition Set 48:** FunFam id: Chorismate mutase (CATH.FunFam:1.10.590.10:FF:000002) AND taxon: Ascomycota (NCBITaxon:4890)

**Condition Set 49:** FunFam id: Indoleamine 2,3-dioxygenase 1 (CATH.FunFam:1.20.58.480:FF:000003) AND taxon: Metazoa (NCBITaxon:33208)

**Condition Set 50:** FunFam id: D-aspartate oxidase (CATH.FunFam:3.40.50.720:FF:000551) AND taxon: Chordata (NCBITaxon:7711)

**Condition Set 51:** FunFam id: Ornithine carbamoyltransferase, mitochondrial (CATH.FunFam:3.40.50.1370:FF:000009)

**Condition Set 52:** FunFam id: Threonine--tRNA ligase 2, cytoplasmic (CATH.FunFam:3.40.50.800:FF:000003)

**Condition Set 53:** FunFam id: Methionine synthase (CATH.FunFam:1.10.1240.10:FF:000001) AND FunFam id: Methionine synthase (CATH.FunFam:3.20.20.20:FF:000002) AND FunFam id: Methionine synthase (CATH.FunFam:3.20.20.330:FF:000001)

**Condition Set 54:** FunFam id: Hemocyanin subunit 2 (CATH.FunFam:1.10.1280.10:FF:000004) AND FunFam id: Hemocyanin subunit 2 (CATH.FunFam:2.60.40.1520:FF:000001) AND taxon: Lepidoptera (NCBITaxon:7088)

**Condition Set 55:** FunFam id: Os03g0824900 protein (CATH.FunFam:1.10.275.10:FF:000014) AND FunFam id: Argininosuccinate lyase (CATH.FunFam:1.10.40.30:FF:000001) AND FunFam id: argininosuccinate lyase isoform X2 (CATH.FunFam:1.20.200.10:FF:000015)

**Condition Set 56:** FunFam id: Glutamate synthase, large subunit (CATH.FunFam:2.160.20.60:FF:000001) AND FunFam id: Glutamate synthase [NADH], amyloplastic (CATH.FunFam:3.20.20.70:FF:000017) AND FunFam id: Glutamate synthase 1 [NADH] (CATH.FunFam:3.20.20.70:FF:000031)

**Condition Set 57:** FunFam id: Delta-1-pyrroline-5-carboxylate synthase (CATH.FunFam:3.40.1160.10:FF:000013) AND FunFam id: Delta-1-pyrroline-5-carboxylate synthase (CATH.FunFam:3.40.309.10:FF:000015) AND taxon: Streptophyta (NCBITaxon:35493)

**Condition Set 58:** FunFam id: Alcohol dehydrogenase AdhP (CATH.FunFam:3.40.50.720:FF:000039) AND FunFam id: Alcohol dehydrogenase AdhP (CATH.FunFam:3.90.180.10:FF:000002) AND taxon: Saccharomycetes (NCBITaxon:4891)

**Condition Set 59:** FunFam id: Acetolactate synthase (CATH.FunFam:3.40.50.970:FF:000007) AND FunFam id: Acetolactate synthase (CATH.FunFam:3.40.50.970:FF:000016) AND taxon: Bacteria (NCBITaxon:2)

**Condition Set 60:** FunFam id: Pyruvate decarboxylase isozyme (CATH.FunFam:3.40.50.970:FF:000019) AND FunFam id: Pyruvate decarboxylase isozyme (CATH.FunFam:3.40.50.970:FF:000024) AND taxon: Saccharomyces (NCBITaxon:4930)

**Condition Set 61:** FunFam id: Branched-chain-amino-acid aminotransferase, mitochondrial (CATH.FunFam:3.20.10.10:FF:000007) AND FunFam id: Branched-chain-amino-acid aminotransferase (CATH.FunFam:3.30.470.10:FF:000002)

**Condition Set 62:** FunFam id: Alpha-aminoadipic semialdehyde synthase, mitochondrial (CATH.FunFam:3.30.360.10:FF:000008) AND FunFam id: Saccharopine dehydrogenase [NADP(+), L-glutamate-forming] (CATH.FunFam:3.40.50.720:FF:000072)

**Condition Set 63:** FunFam id: Aspartate aminotransferase (CATH.FunFam:3.90.1150.10:FF:000001) AND taxon: Rodentia (NCBITaxon:9989)

**Condition Set 64:** FunFam id: Tryptophan 2,3-dioxygenase (CATH.FunFam:1.10.287.3810:FF:000001)

**Condition Set 65:** FunFam id: 3-isopropylmalate dehydratase small subunit (CATH.FunFam:3.20.19.10:FF:000003)

**Condition Set 66:** FunFam id: Indole-3-glycerol phosphate synthase (CATH.FunFam:3.20.20.70:FF:000024)

**Condition Set 67:** FunFam id: 2-isopropylmalate synthase (CATH.FunFam:3.20.20.70:FF:000045)

**Condition Set 68:** FunFam id: ATP phosphoribosyltransferase (CATH.FunFam:3.30.70.120:FF:000003)

**Condition Set 69:** FunFam id: Acetolactate synthase, small subunit (CATH.FunFam:3.30.70.260:FF:000001)

**Condition Set 70:** FunFam id: Anthranilate phosphoribosyltransferase (CATH.FunFam:3.40.1030.10:FF:000002)

**Condition Set 71:** FunFam id: L-asparaginase 1 (CATH.FunFam:3.40.50.40:FF:000001)

**Condition Set 72:** FunFam id: Asparagine synthase B (CATH.FunFam:3.40.50.620:FF:000031)

**Condition Set 73:** FunFam id: Phosphoserine aminotransferase (CATH.FunFam:3.40.640.10:FF:000010)

**Condition Set 74:** FunFam id: O-succinylhomoserine sulfhydrylase (CATH.FunFam:3.40.640.10:FF:000035)

**Condition Set 75:** FunFam id: 3-isopropylmalate dehydrogenase (CATH.FunFam:3.40.718.10:FF:000004)

**Condition Set 76:** FunFam id: Anthranilate synthase component 1 (CATH.FunFam:3.60.120.10:FF:000003)

**Condition Set 77:** FunFam id: Phosphoserine aminotransferase (CATH.FunFam:3.90.1150.10:FF:000006)

**Condition Set 78:** FunFam id: Glutamate dehydrogenase (CATH.FunFam:1.10.285.10:FF:000001) AND FunFam id: Glutamate dehydrogenase (CATH.FunFam:3.40.50.10860:FF:000002) AND taxon: Pseudomonadati (NCBITaxon:3379134)

**Condition Set 79:** FunFam id: Bifunctional glutamate/proline--tRNA ligase (CATH.FunFam:1.10.287.10:FF:000006) AND FunFam id: Bifunctional glutamate/proline--tRNA ligase (CATH.FunFam:3.30.110.30:FF:000001) AND FunFam id: Bifunctional glutamate/proline--tRNA ligase (CATH.FunFam:3.30.930.10:FF:000007)

**Condition Set 80:** FunFam id: Arginine--tRNA ligase, cytoplasmic (CATH.FunFam:1.10.730.10:FF:000016) AND FunFam id: arginine--tRNA ligase, cytoplasmic (CATH.FunFam:3.30.1360.70:FF:000002) AND FunFam id: arginine--tRNA ligase, cytoplasmic (CATH.FunFam:3.40.50.620:FF:000084)

**Condition Set 81:** FunFam id: Aminomethyltransferase (CATH.FunFam:2.40.30.110:FF:000002) AND FunFam id: Aminomethyltransferase (CATH.FunFam:3.30.1360.120:FF:000014) AND taxon: Craniata (NCBITaxon:89593)

**Condition Set 82:** FunFam id: Alanyl-tRNA synthetase (CATH.FunFam:2.40.30.130:FF:000026) AND FunFam id: alanine--tRNA ligase, cytoplasmic (CATH.FunFam:3.10.310.40:FF:000002) AND FunFam id: Alanine--tRNA ligase, cytoplasmic (CATH.FunFam:3.30.930.10:FF:000011)

**Condition Set 83:** FunFam id: Carnosine synthase 1 (CATH.FunFam:3.30.470.20:FF:000040) AND FunFam id: Carnosine synthase 1 (CATH.FunFam:3.40.50.20:FF:000018) AND taxon: Euteleostomi (NCBITaxon:117571)

**Condition Set 84:** FunFam id: D-amino-acid oxidase (CATH.FunFam:3.30.9.10:FF:000004) AND FunFam id: D-amino acid oxidase (CATH.FunFam:3.40.50.720:FF:000641) AND taxon: Mammalia (NCBITaxon:40674)

**Condition Set 85:** FunFam id: Lysine decarboxylase, inducible (CATH.FunFam:3.40.640.10:FF:000008) AND FunFam id: Lysine decarboxylase, inducible (CATH.FunFam:3.90.1150.10:FF:000016) AND taxon: Pseudomonadota (NCBITaxon:1224)

**Condition Set 86:** FunFam id: 4-aminobutyrate aminotransferase (CATH.FunFam:3.40.640.10:FF:000013) AND FunFam id: 4-aminobutyrate aminotransferase (CATH.FunFam:3.90.1150.10:FF:000022) AND taxon: Gammaproteobacteria (NCBITaxon:1236)

**Condition Set 87:** FunFam id: Glutamate decarboxylase like 1 (CATH.FunFam:3.40.640.10:FF:000016) AND FunFam id: Glutamate decarboxylase 1 (CATH.FunFam:3.90.1150.170:FF:000003) AND taxon: Eutheria (NCBITaxon:9347)

**Condition Set 88:** FunFam id: tyrosine aminotransferase (CATH.FunFam:3.40.640.10:FF:000048) AND FunFam id: Tyrosine aminotransferase (CATH.FunFam:3.90.1150.10:FF:000040) AND taxon: Euarchontoglires (NCBITaxon:314146)

**Condition Set 89:** FunFam id: Homocitrate synthase, mitochondrial (CATH.FunFam:1.10.238.260:FF:000002) AND FunFam id: Homocitrate synthase, mitochondrial (CATH.FunFam:3.20.20.70:FF:000032)

**Condition Set 90:** FunFam id: Pyrroline-5-carboxylate reductase 1, mitochondrial (CATH.FunFam:1.10.3730.10:FF:000003) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 91:** FunFam id: Chorismate mutase (CATH.FunFam:1.10.590.10:FF:000001) AND taxon: rosids (NCBITaxon:71275)

**Condition Set 92:** FunFam id: Isoleucyl-tRNA synthetase, cytoplasmic (CATH.FunFam:1.10.730.10:FF:000004) AND FunFam id: Isoleucyl-tRNA synthetase,cytoplasmic (CATH.FunFam:3.40.50.620:FF:000050)

**Condition Set 93:** FunFam id: Arginine biosynthesis bifunctional protein ArgJ, mitochondrial (CATH.FunFam:3.10.20.340:FF:000002) AND FunFam id: Arginine biosynthesis bifunctional protein ArgJ, mitochondrial (CATH.FunFam:3.30.2330.10:FF:000001)

**Condition Set 94:** FunFam id: Glutamine synthetase (CATH.FunFam:3.10.20.70:FF:000004) AND FunFam id: Glutamine synthetase (CATH.FunFam:3.30.590.10:FF:000004)

**Condition Set 95:** FunFam id: Branched-chain-amino-acid aminotransferase (CATH.FunFam:3.20.10.10:FF:000004) AND FunFam id: Branched-chain-amino-acid aminotransferase (CATH.FunFam:3.30.470.10:FF:000005)

**Condition Set 96:** FunFam id: Phosphoribosylanthranilate isomerase (CATH.FunFam:3.20.20.70:FF:000199) AND taxon: Saccharomycotina (NCBITaxon:147537)

**Condition Set 97:** FunFam id: L-serine ammonia-lyase 1 (CATH.FunFam:3.30.1330.90:FF:000001) AND taxon: Enterobacterales (NCBITaxon:91347)

**Condition Set 98:** FunFam id: Pterin-4-alpha-carbinolamine dehydratase 2 (CATH.FunFam:3.30.1360.20:FF:000001) AND taxon: Glires (NCBITaxon:314147)

**Condition Set 99:** FunFam id: Homoaconitase, mitochondrial (CATH.FunFam:3.30.499.10:FF:000013) AND FunFam id: Homoaconitase, mitochondrial (CATH.FunFam:3.30.499.10:FF:000016)

**Condition Set 100:** FunFam id: L-threonine dehydratase (CATH.FunFam:3.40.1020.10:FF:000001) AND FunFam id: L-threonine dehydratase (CATH.FunFam:3.40.50.1100:FF:000008)

**Condition Set 101:** FunFam id: Cysteine synthase (CATH.FunFam:3.40.50.1100:FF:000002) AND FunFam id: Cysteine synthase (CATH.FunFam:3.40.50.1100:FF:000006)

**Condition Set 102:** FunFam id: Acetolactate synthase (CATH.FunFam:3.40.50.1220:FF:000008) AND FunFam id: Acetolactate synthase, mitochondrial (CATH.FunFam:3.40.50.970:FF:000053)

**Condition Set 103:** FunFam id: Sarcosine/dimethylglycine N-methyltransferase (CATH.FunFam:3.40.50.150:FF:000461) AND taxon: Bacillati (NCBITaxon:1783272)

**Condition Set 104:** FunFam id: Shikimate kinase, chloroplastic (CATH.FunFam:3.40.50.300:FF:000822) AND taxon: Liliopsida (NCBITaxon:4447)

**Condition Set 105:** FunFam id: Sorbitol dehydrogenase (CATH.FunFam:3.40.50.720:FF:000068) AND taxon: Archaea (NCBITaxon:2157)

**Condition Set 106:** FunFam id: Anthranilate synthase beta subunit 1 (CATH.FunFam:3.40.50.880:FF:000027) AND taxon: Embryophyta (NCBITaxon:3193)

**Condition Set 107:** FunFam id: Aspartate aminotransferase (CATH.FunFam:3.40.640.10:FF:000015) AND taxon: Enterobacteriaceae (NCBITaxon:543)

**Condition Set 108:** FunFam id: Histidine biosynthesis bifunctional protein HisIE (CATH.FunFam:1.10.287.1080:FF:000002)

**Condition Set 109:** FunFam id: Phenylalanine-4-hydroxylase (CATH.FunFam:1.10.800.10:FF:000003)

**Condition Set 110:** FunFam id: Cysteine dioxygenase 1 (CATH.FunFam:2.60.120.10:FF:000045)

**Condition Set 111:** FunFam id: D-alanine aminotransferase (CATH.FunFam:3.20.10.10:FF:000002)

**Condition Set 112:** FunFam id: D-serine dehydratase (CATH.FunFam:3.20.20.10:FF:000016)

**Condition Set 113:** FunFam id: 3-isopropylmalate dehydratase large subunit (CATH.FunFam:3.30.499.10:FF:000006)

**Condition Set 114:** FunFam id: Gamma-glutamyl phosphate reductase (CATH.FunFam:3.40.309.10:FF:000006)

**Condition Set 115:** FunFam id: Carnosine N-methyltransferase 1 (CATH.FunFam:3.40.50.150:FF:000094)

**Condition Set 116:** FunFam id: Histidinol dehydrogenase (CATH.FunFam:3.40.50.1980:FF:000001)

**Condition Set 117:** FunFam id: D-3-phosphoglycerate dehydrogenase (CATH.FunFam:3.40.50.720:FF:000041)

**Condition Set 118:** FunFam id: Glutamate dehydrogenase (CATH.FunFam:3.40.50.720:FF:001273)

**Condition Set 119:** FunFam id: Kynureninase (CATH.FunFam:3.40.640.10:FF:000031)

**Condition Set 120:** FunFam id: Aspartate aminotransferase (CATH.FunFam:3.40.640.10:FF:000044)

**Condition Set 121:** FunFam id: Arginase (CATH.FunFam:3.40.800.10:FF:000005)

**Condition Set 122:** FunFam id: phenylalanine--tRNA ligase beta subunit (CATH.FunFam:3.50.40.10:FF:000002)

**Condition Set 123:** FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:1.10.1030.10:FF:000001) AND FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:3.20.20.140:FF:000036) AND FunFam id: CAD protein-like isoform X1 (CATH.FunFam:3.40.50.20:FF:000011)

**Condition Set 124:** FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:1.10.1030.10:FF:000002) AND FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:3.30.1490.20:FF:000001) AND FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:3.40.50.1380:FF:000004)

**Condition Set 125:** FunFam id: Glutamine--tRNA ligase (CATH.FunFam:1.10.1160.10:FF:000001) AND FunFam id: Glutamine--tRNA ligase (CATH.FunFam:3.90.800.10:FF:000001) AND taxon: Saccharomycetales (NCBITaxon:4892)

**Condition Set 126:** FunFam id: Glutaminase kidney isoform, mitochondrial (CATH.FunFam:1.10.238.210:FF:000001) AND FunFam id: Glutaminase liver isoform, mitochondrial (CATH.FunFam:1.25.40.20:FF:000019) AND taxon: Haplorrhini (NCBITaxon:376913)

**Condition Set 127:** FunFam id: 2-isopropylmalate synthase 1 chloroplastic (CATH.FunFam:1.10.238.260:FF:000003) AND FunFam id: 2-isopropylmalate synthase (CATH.FunFam:3.20.20.70:FF:000010) AND FunFam id: 2-isopropylmalate synthase B (CATH.FunFam:3.30.160.270:FF:000004)

**Condition Set 128:** FunFam id: Tyrosine--tRNA ligase (CATH.FunFam:1.10.240.10:FF:000001) AND FunFam id: Tyrosine--tRNA ligase (CATH.FunFam:3.10.290.10:FF:000017) AND FunFam id: Tyrosine--tRNA ligase (CATH.FunFam:3.40.50.620:FF:000107)

**Condition Set 129:** FunFam id: Argininosuccinate lyase (CATH.FunFam:1.10.275.10:FF:000002) AND FunFam id: Argininosuccinate lyase (CATH.FunFam:1.20.200.10:FF:000002) AND taxon: Phasianinae (NCBITaxon:9072)

**Condition Set 130:** FunFam id: Histidine ammonia-lyase (CATH.FunFam:1.10.275.10:FF:000005) AND FunFam id: Tyrosine ammonia-lyase (CATH.FunFam:1.20.200.10:FF:000012) AND taxon: Cyanobacteriota (NCBITaxon:1117)

**Condition Set 131:** FunFam id: Histidine ammonia-lyase (CATH.FunFam:1.10.275.10:FF:000007) AND FunFam id: Histidine ammonia-lyase (CATH.FunFam:1.20.200.10:FF:000003) AND taxon: Myomorpha (NCBITaxon:1963758)

**Condition Set 132:** FunFam id: Glutamate dehydrogenase (CATH.FunFam:1.10.285.10:FF:000003) AND FunFam id: Glutamate dehydrogenase (CATH.FunFam:3.40.50.720:FF:000030) AND taxon: Saccharomycetaceae (NCBITaxon:4893)

**Condition Set 133:** FunFam id: Methionine--tRNA ligase, cytoplasmic (CATH.FunFam:1.10.287.10:FF:000009) AND FunFam id: methionine--tRNA ligase, cytoplasmic (CATH.FunFam:1.10.730.10:FF:000010) AND FunFam id: Methionine--tRNA ligase, cytoplasmic (CATH.FunFam:1.20.1050.10:FF:000026)

**Condition Set 134:** FunFam id: Glutamate dehydrogenase 1, mitochondrial (CATH.FunFam:1.10.287.140:FF:000001) AND FunFam id: Glutamate dehydrogenase 1, mitochondrial (CATH.FunFam:3.40.50.10860:FF:000007) AND taxon: Catarrhini (NCBITaxon:9526)

**Condition Set 135:** FunFam id: Amine oxidase (CATH.FunFam:1.10.405.10:FF:000004) AND FunFam id: Amine oxidase (CATH.FunFam:3.50.50.60:FF:000450) AND FunFam id: Amine oxidase (CATH.FunFam:3.90.660.10:FF:000011)

**Condition Set 136:** FunFam id: Methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 1 like (CATH.FunFam:1.10.8.770:FF:000001) AND FunFam id: Putative formate--tetrahydrofolate ligase (CATH.FunFam:3.10.410.10:FF:000001) AND FunFam id: C-1-tetrahydrofolate synthase, cytoplasmic (CATH.FunFam:3.40.50.300:FF:000245)

**Condition Set 137:** FunFam id: Tyrosine 3-monooxygenase (CATH.FunFam:1.10.800.10:FF:000002) AND FunFam id: Tyrosine 3-monooxygenase (CATH.FunFam:3.30.70.260:FF:000024) AND taxon: Muroidea (NCBITaxon:337687)

**Condition Set 138:** FunFam id: Bifunctional protein PutA (CATH.FunFam:1.20.5.460:FF:000001) AND FunFam id: Bifunctional protein PutA (CATH.FunFam:1.20.5.550:FF:000001) AND FunFam id: Bifunctional protein PutA (CATH.FunFam:3.20.20.220:FF:000004)

**Condition Set 139:** FunFam id: Methionine synthase reductase (CATH.FunFam:1.20.990.10:FF:000007) AND FunFam id: methionine synthase reductase (CATH.FunFam:3.40.50.360:FF:000025) AND FunFam id: NADPH--cytochrome P450 reductase (CATH.FunFam:3.40.50.80:FF:000018)

**Condition Set 140:** FunFam id: Alanine racemase (CATH.FunFam:2.40.37.10:FF:000002) AND FunFam id: Alanine racemase (CATH.FunFam:3.20.20.10:FF:000002) AND taxon: Escherichia (NCBITaxon:561)

**Condition Set 141:** FunFam id: 4-hydroxyproline betaine 2-epimerase (CATH.FunFam:3.20.20.120:FF:000020) AND FunFam id: Hydrophobic dipeptide epimerase (CATH.FunFam:3.30.390.10:FF:000009) AND taxon: Hyphomicrobiales (NCBITaxon:356)

**Condition Set 142:** FunFam id: Putative selenophosphate synthetase (CATH.FunFam:3.30.1330.10:FF:000023) AND FunFam id: Selenide, water dikinase (CATH.FunFam:3.90.650.10:FF:000010) AND taxon: Discoba (NCBITaxon:2611352)

**Condition Set 143:** FunFam id: D-3-phosphoglycerate dehydrogenase (CATH.FunFam:3.30.1330.90:FF:000005) AND FunFam id: D-3-phosphoglycerate dehydrogenase (CATH.FunFam:3.40.50.720:FF:000021) AND taxon: Muridae (NCBITaxon:10066)

**Condition Set 144:** FunFam id: beta-citrylglutamate synthase B isoform X1 (CATH.FunFam:3.30.1490.20:FF:000011) AND FunFam id: beta-citrylglutamate synthase B isoform X1 (CATH.FunFam:3.30.470.20:FF:000022) AND taxon: Hominidae (NCBITaxon:9604)

**Condition Set 145:** FunFam id: Bifunctional acetylglutamate kinase/N-acetyl-gamma-glutamyl-phosphate reductase (CATH.FunFam:3.30.360.10:FF:000019) AND FunFam id: N-acetyl-gamma-glutamyl-phosphate reductase, variant (CATH.FunFam:3.40.1160.10:FF:000011) AND FunFam id: Bifunctional acetylglutamate kinase/N-acetyl-gamma-glutamyl-phosphate reductase (CATH.FunFam:3.40.630.30:FF:000029)

**Condition Set 146:** FunFam id: Glycine N-methyltransferase (CATH.FunFam:3.30.46.10:FF:000001) AND FunFam id: Glycine N-methyltransferase (CATH.FunFam:3.40.50.150:FF:000113) AND taxon: Murinae (NCBITaxon:39107)

**Condition Set 147:** FunFam id: Carbamoyl-phosphate synthase large chain (CATH.FunFam:3.30.470.20:FF:000001) AND FunFam id: Carbamoyl-phosphate synthase (glutamine-hydrolyzing) (CATH.FunFam:3.30.470.20:FF:000004) AND taxon: Taphrinomycotina (NCBITaxon:451866)

**Condition Set 148:** FunFam id: Inositol-1-monophosphatase (CATH.FunFam:3.30.540.10:FF:000003) AND FunFam id: Histidinol phosphatase (CATH.FunFam:3.40.190.80:FF:000010) AND taxon: Actinomycetota (NCBITaxon:201174)

**Condition Set 149:** FunFam id: ATP phosphoribosyltransferase, chloroplastic (CATH.FunFam:3.30.70.120:FF:000007) AND FunFam id: ATP phosphoribosyltransferase 2, chloroplastic (CATH.FunFam:3.40.190.10:FF:000118) AND taxon: Spermatophyta (NCBITaxon:58024)

**Condition Set 150:** FunFam id: Probable histidine--tRNA ligase, mitochondrial (CATH.FunFam:3.30.930.10:FF:000021) AND FunFam id: histidine--tRNA ligase, cytoplasmic isoform X1 (CATH.FunFam:3.40.50.800:FF:000008) AND taxon: Homo (NCBITaxon:9605)

**Condition Set 151:** FunFam id: Threonine--tRNA ligase (CATH.FunFam:3.30.930.10:FF:000076) AND FunFam id: Threonine--tRNA ligase (CATH.FunFam:3.40.50.800:FF:000001) AND FunFam id: Threonine--tRNA ligase (CATH.FunFam:3.50.80.10:FF:000004)

**Condition Set 152:** FunFam id: Glutamate dehydrogenase (CATH.FunFam:3.40.50.10860:FF:000008) AND FunFam id: Glutamate dehydrogenase (CATH.FunFam:3.40.50.720:FF:000212) AND taxon: Bacillota (NCBITaxon:1239)

**Condition Set 153:** FunFam id: Tryptophan synthase beta chain (CATH.FunFam:3.40.50.1100:FF:000001) AND FunFam id: Tryptophan synthase beta chain (CATH.FunFam:3.40.50.1100:FF:000004) AND taxon: Magnoliopsida (NCBITaxon:3398)

**Condition Set 154:** FunFam id: 2-oxoisovalerate dehydrogenase subunit beta 1, mitochondrial (CATH.FunFam:3.40.50.920:FF:000004) AND FunFam id: Pyruvate dehydrogenase E1 beta subunit (CATH.FunFam:3.40.50.970:FF:000001) AND taxon: eudicotyledons (NCBITaxon:71240)

**Condition Set 155:** FunFam id: 4-aminobutyrate aminotransferase, mitochondrial (CATH.FunFam:3.40.640.10:FF:000029) AND FunFam id: 4-aminobutyrate aminotransferase, mitochondrial (CATH.FunFam:3.90.1150.10:FF:000191) AND taxon: Laurasiatheria (NCBITaxon:314145)

**Condition Set 156:** FunFam id: probable low-specificity L-threonine aldolase 1 (CATH.FunFam:3.40.640.10:FF:000063) AND FunFam id: Low-specificity L-threonine aldolase (CATH.FunFam:3.90.1150.10:FF:000041) AND taxon: Gunneridae (NCBITaxon:91827)

**Condition Set 157:** FunFam id: Serine hydroxymethyltransferase (CATH.FunFam:3.40.640.10:FF:000097) AND FunFam id: Serine hydroxymethyltransferase (CATH.FunFam:3.90.1150.10:FF:000005) AND FunFam id: Serine hydroxymethyltransferase, mitochondrial (CATH.FunFam:3.90.1150.10:FF:000048)

**Condition Set 158:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:3.40.630.10:FF:000027)

**Condition Set 159:** FunFam id: Phenylalanine aminomutase (L-beta-phenylalanine forming) (CATH.FunFam:1.10.274.20:FF:000003) AND taxon: Pinopsida (NCBITaxon:58019)

**Condition Set 160:** FunFam id: Prephenate dehydrogenase [NADP(+)] (CATH.FunFam:1.10.3660.10:FF:000004) AND FunFam id: Prephenate dehydrogenase [NADP(+)] (CATH.FunFam:3.40.50.720:FF:000339)

**Condition Set 161:** FunFam id: Pyrroline-5-carboxylate reductase (CATH.FunFam:1.10.3730.10:FF:000001) AND FunFam id: Pyrroline-5-carboxylate reductase (CATH.FunFam:3.40.50.720:FF:000105)

**Condition Set 162:** FunFam id: Cytochrome P450 9 (CATH.FunFam:1.10.630.10:FF:000037) AND taxon: malvids (NCBITaxon:91836)

**Condition Set 163:** FunFam id: Tyrosine 3-monooxygenase (CATH.FunFam:1.10.800.10:FF:000004) AND taxon: Nematoda (NCBITaxon:6231)

**Condition Set 164:** FunFam id: Solute carrier family 25 member 44 (CATH.FunFam:1.50.40.10:FF:000033) AND FunFam id: Solute carrier family 25 member 44 (CATH.FunFam:1.50.40.10:FF:000108)

**Condition Set 165:** FunFam id: GD20529 (CATH.FunFam:2.120.10.30:FF:000092) AND taxon: Ecdysozoa (NCBITaxon:1206794)

**Condition Set 166:** FunFam id: Lysine--tRNA ligase (CATH.FunFam:2.40.50.140:FF:000024) AND FunFam id: Lysine--tRNA ligase (CATH.FunFam:3.30.930.10:FF:000001)

**Condition Set 167:** FunFam id: Homogentisate 1,2-dioxygenase (CATH.FunFam:2.60.120.10:FF:000036) AND taxon: Pseudomonadales (NCBITaxon:72274)

**Condition Set 168:** FunFam id: Homogentisate 1,2-dioxygenase (CATH.FunFam:2.60.120.10:FF:000053) AND taxon: Pezizomycotina (NCBITaxon:147538)

**Condition Set 169:** FunFam id: 4-hydroxyphenylpyruvate dioxygenase (CATH.FunFam:3.10.180.10:FF:000008) AND FunFam id: 4-hydroxyphenylpyruvate dioxygenase (CATH.FunFam:3.10.180.10:FF:000022)

**Condition Set 170:** FunFam id: Branched-chain-amino-acid aminotransferase (CATH.FunFam:3.20.10.10:FF:000009) AND taxon: Actinomycetes (NCBITaxon:1760)

**Condition Set 171:** FunFam id: Ornithine decarboxylase 1 (CATH.FunFam:3.20.20.10:FF:000006) AND taxon: Mus (NCBITaxon:862507)

**Condition Set 172:** FunFam id: Homocysteine S-methyltransferase (CATH.FunFam:3.20.20.330:FF:000002) AND taxon: Camelineae (NCBITaxon:980083)

**Condition Set 173:** FunFam id: Tryptophan biosynthesis protein TRP1 (CATH.FunFam:3.20.20.70:FF:000075) AND taxon: Pentapetalae (NCBITaxon:1437201)

**Condition Set 174:** FunFam id: Tryptophan synthase alpha chain, chloroplastic (CATH.FunFam:3.20.20.70:FF:000107) AND taxon: Brassicales (NCBITaxon:3699)

**Condition Set 175:** FunFam id: Multifunctional tryptophan biosynthesis protein (CATH.FunFam:3.20.20.70:FF:000136) AND FunFam id: Multifunctional tryptophan biosynthesis protein (CATH.FunFam:3.40.50.880:FF:000031)

**Condition Set 176:** FunFam id: selenide, water dikinase 2 (CATH.FunFam:3.30.1330.10:FF:000018) AND FunFam id: Selenide, water dikinase 1 (CATH.FunFam:3.90.650.10:FF:000003)

**Condition Set 177:** FunFam id: Malate/L-lactate family dehydrogenase (CATH.FunFam:3.30.1370.60:FF:000002) AND taxon: Pseudomonadaceae (NCBITaxon:135621)

**Condition Set 178:** FunFam id: Bifunctional aspartokinase/homoserine dehydrogenase (CATH.FunFam:3.30.2130.10:FF:000001) AND FunFam id: Probable aspartokinase (CATH.FunFam:3.40.1160.10:FF:000023)

**Condition Set 179:** FunFam id: Imidazoleglycerol-phosphate dehydratase HisB (CATH.FunFam:3.30.230.40:FF:000001) AND FunFam id: Imidazoleglycerol-phosphate dehydratase (CATH.FunFam:3.30.230.40:FF:000005)

**Condition Set 180:** FunFam id: Enterobactin synthetase component F (CATH.FunFam:3.30.300.30:FF:000010) AND FunFam id: Non-ribosomal peptide synthetase (CATH.FunFam:3.40.50.12780:FF:000012)

**Condition Set 181:** FunFam id: N-acetyldiaminopimelate deacetylase (CATH.FunFam:3.30.70.360:FF:000001) AND taxon: Bacilli (NCBITaxon:91061)

**Condition Set 182:** FunFam id: phenylalanine--tRNA ligase, mitochondrial (CATH.FunFam:3.30.70.380:FF:000002) AND FunFam id: Phenylalanyl-tRNA synthetase mitochondrial (CATH.FunFam:3.30.930.10:FF:000053)

**Condition Set 183:** FunFam id: Threonine dehydratase (CATH.FunFam:3.40.1020.10:FF:000003) AND taxon: Solanum subgen. Lycopersicon (NCBITaxon:49274)

**Condition Set 184:** FunFam id: Delta-1-pyrroline-5-carboxylate synthase (CATH.FunFam:3.40.1160.10:FF:000010) AND FunFam id: Delta-1-pyrroline-5-carboxylate synthase (CATH.FunFam:3.40.309.10:FF:000011)

**Condition Set 185:** FunFam id: THR4p Threonine synthase (CATH.FunFam:3.40.50.1100:FF:000046) AND FunFam id: THR4p Threonine synthase (CATH.FunFam:3.90.1380.10:FF:000003)

**Condition Set 186:** FunFam id: (R)-2-hydroxyisocaproyl-CoA dehydratase beta subunit (CATH.FunFam:3.40.50.11890:FF:000002) AND taxon: Clostridia (NCBITaxon:186801)

**Condition Set 187:** FunFam id: Argininosuccinate synthase (CATH.FunFam:3.40.50.620:FF:000019) AND FunFam id: Argininosuccinate synthase (CATH.FunFam:3.90.1260.10:FF:000003)

**Condition Set 188:** FunFam id: Glutamine-dependent NAD(+) synthetase (CATH.FunFam:3.40.50.620:FF:000036) AND FunFam id: Glutamine-dependent NAD(+) synthetase (CATH.FunFam:3.60.110.10:FF:000007)

**Condition Set 189:** FunFam id: Saccharopine dehydrogenase [NAD(+), L-lysine-forming] (CATH.FunFam:3.40.50.720:FF:000217) AND FunFam id: Saccharopine dehydrogenase [NAD(+), L-lysine-forming] (CATH.FunFam:3.40.50.720:FF:000423)

**Condition Set 190:** FunFam id: N5-(Carboxyethyl)ornithine synthase (CATH.FunFam:3.40.50.720:FF:000488) AND FunFam id: N(5)-(Carboxyethyl)ornithine synthase (CATH.FunFam:3.40.50.720:FF:000489)

**Condition Set 191:** FunFam id: Glycine--tRNA ligase (CATH.FunFam:3.40.50.800:FF:000002) AND taxon: Mycobacteriales (NCBITaxon:85007)

**Condition Set 192:** FunFam id: Carbamoyl-phosphate synthase arginine-specific small chain (CATH.FunFam:3.40.50.880:FF:000016) AND FunFam id: Carbamoyl-phosphate synthase arginine-specific small chain (CATH.FunFam:3.50.30.20:FF:000003)

**Condition Set 193:** FunFam id: 2-oxoisovalerate dehydrogenase subunit alpha (CATH.FunFam:3.40.50.970:FF:000015) AND taxon: Brassicaceae (NCBITaxon:3700)

**Condition Set 194:** FunFam id: Serine hydroxymethyltransferase (CATH.FunFam:3.40.640.10:FF:000001) AND taxon: Mycobacteriaceae (NCBITaxon:1762)

**Condition Set 195:** FunFam id: Acetylornithine aminotransferase (CATH.FunFam:3.40.640.10:FF:000004) AND FunFam id: Succinylornithine transaminase (CATH.FunFam:3.90.1150.10:FF:000009)

**Condition Set 196:** FunFam id: Kynurenine--oxoglutarate transaminase 3 (CATH.FunFam:3.40.640.10:FF:000024) AND FunFam id: Kynurenine--oxoglutarate transaminase 3 (CATH.FunFam:3.90.1150.10:FF:000021)

**Condition Set 197:** FunFam id: Cystathionine gamma-lyase (CATH.FunFam:3.40.640.10:FF:000046) AND taxon: Arabidopsis (NCBITaxon:3701)

**Condition Set 198:** FunFam id: Valine--tRNA ligase, mitochondrial (CATH.FunFam:3.90.740.10:FF:000005) AND taxon: Schizosaccharomycetales (NCBITaxon:34346)

**Condition Set 199:** FunFam id: Tryptophan 2,3-dioxygenase (CATH.FunFam:1.20.58.480:FF:000001)

**Condition Set 200:** FunFam id: Serine acetyltransferase (CATH.FunFam:2.160.10.10:FF:000007)

**Condition Set 201:** FunFam id: Homogentisate 1,2-dioxygenase (CATH.FunFam:2.60.120.10:FF:000026)

**Condition Set 202:** FunFam id: Histidine biosynthesis bifunctional protein HisIE (CATH.FunFam:3.10.20.810:FF:000001)

**Condition Set 203:** FunFam id: 2-amino-3-carboxymuconate-6-semialdehyde decarboxylase (CATH.FunFam:3.20.20.140:FF:000029)

**Condition Set 204:** FunFam id: Methylenetetrahydrofolate reductase (CATH.FunFam:3.20.20.220:FF:000003)

**Condition Set 205:** FunFam id: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase (CATH.FunFam:3.20.20.70:FF:000009)

**Condition Set 206:** FunFam id: Tryptophan synthase alpha chain (CATH.FunFam:3.20.20.70:FF:000037)

**Condition Set 207:** FunFam id: Imidazole glycerol phosphate synthase hisHF (CATH.FunFam:3.20.20.70:FF:000094)

**Condition Set 208:** FunFam id: 1-(5-phosphoribosyl)-5-[(5-phosphoribosylamino)methylideneamino] imidazole-4-carboxamide isomerase, chloroplastic (CATH.FunFam:3.20.20.70:FF:000110)

**Condition Set 209:** FunFam id: Homoserine kinase (CATH.FunFam:3.30.230.10:FF:000068)

**Condition Set 210:** FunFam id: Homoserine dehydrogenase (CATH.FunFam:3.30.360.10:FF:000005)

**Condition Set 211:** FunFam id: Amino-acid acetyltransferase (CATH.FunFam:3.40.1160.10:FF:000005)

**Condition Set 212:** FunFam id: Cysteine synthase (o-acetylserine) (CATH.FunFam:3.40.50.1100:FF:000011)

**Condition Set 213:** FunFam id: Cysteine synthase (CATH.FunFam:3.40.50.1100:FF:000067)

**Condition Set 214:** FunFam id: Ornithine carbamoyltransferase (CATH.FunFam:3.40.50.1370:FF:000004)

**Condition Set 215:** FunFam id: Tyrosine--tRNA ligase (CATH.FunFam:3.40.50.620:FF:000008)

**Condition Set 216:** FunFam id: L-2-aminoadipate reductase (CATH.FunFam:3.40.50.720:FF:000787)

**Condition Set 217:** FunFam id: Amino-acid acetyltransferase, mitochondrial (CATH.FunFam:3.40.630.30:FF:000049)

**Condition Set 218:** FunFam id: Aminotransferase (CATH.FunFam:3.40.640.10:FF:000126)

**Condition Set 219:** FunFam id: HISTIDINE BIOSYNTHESIS 6B (CATH.FunFam:3.40.640.10:FF:000131)

**Condition Set 220:** FunFam id: N-succinylarginine dihydrolase (CATH.FunFam:3.75.10.20:FF:000001)

**Condition Set 221:** FunFam id: Cystathionine gamma-synthase (CATH.FunFam:3.90.1150.10:FF:000033)

**Condition Set 222:** FunFam id: Probable cystathionine gamma-synthase (CATH.FunFam:3.90.1150.10:FF:000063)

**Condition Set 223:** FunFam id: kynurenine--oxoglutarate transaminase 1 (CATH.FunFam:3.90.1150.10:FF:000275)

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

For the predicted GO term(s) **GO:0006520 (amino acid metabolic process)**:
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
This is a complex query about UniProt annotation rule ARBA00026411 that predicts GO:0006520 (amino acid metabolic process) based on a large set of domain and family signatures. Let me break down what I need to do:

1. Understand the search results provided - they contain information about various amino acid metabolic enzymes
2. Evaluate whether the rule's condition sets make biological sense
3. Assess whether GO:0006520 is the appropriate annotation
4. Provide literature support for the functions described

Let me review the key search results:

From [1]: Definition of GO:0006520 - "The chemical reactions and pathways involving amino acids, carboxylic acids containing one or more amino groups"

From [2]: Information about aminoacyl-tRNA synthetases - class II enzymes that activate amino acids and transfer them to tRNA molecules

From [3]: Asparaginyl-tRNA synthetase - involved in amino acid activation/protein synthesis

From [5]: Aminoacyl-tRNA synthetases - responsible for activating specific amino acids and transferring them onto cognate tRNA molecules

From [6]: Proline-tRNA ligase - catalyzes attachment of proline to tRNA(Pro)

From [7]: Tryptophan synthase - catalyzes final steps in tryptophan biosynthesis

From [8]: Cysteine synthase - key enzyme in cysteine biosynthetic pathway

From [9]: Aspartate-derived amino acid pathway - responsible for biosynthesis of lysine, threonine, methionine, and isoleucine

From [10]: Tryptophan synthase - commonly found in bacteria, archaea, protista, fungi, and plants but absent from animals

And many more sources about various amino acid biosynthetic and catabolic enzymes.

Let me now structure a comprehensive response about this rule...

The rule has 223 condition sets, each combining various InterPro domain IDs, PANTHER IDs, and/or FunFam IDs with sometimes additional taxonomic restrictions. 

The rule aims to capture proteins functioning in amino acid metabolism through a comprehensive set of domain and family combinations. It encompasses aminoacyl-tRNA synthetases, biosynthetic enzymes for specific amino acids, catabolic pathways, and related metabolic proteins. Each condition set targets specific protein families through their diagnostic domain architecture, with some conditions further refined by taxonomic constraints. The breadth of GO:0006520 allows this single term to encompass all these diverse metabolic processes involving amino acids.

To evaluate this rule effectively, I need to organize the analysis into distinct sections: first, clarifying what the rule attempts to capture across its many conditions; second, breaking down the major protein categories and their metabolic roles; third, assessing whether GO:0006520 appropriately represents this diversity; fourth, examining the supporting evidence for each protein category; and finally, identifying any gaps or potential misclassifications the rule might introduce.
</think>

# Comprehensive Evaluation of UniProt Annotation Rule ARBA00026411 for GO:0006520 (Amino Acid Metabolic Process)

This report presents a detailed analysis of UniProt rule ARBA00026411, which predicts the Gene Ontology term GO:0006520 (amino acid metabolic process) for proteins matching 223 distinct condition sets based on InterPro domain signatures, PANTHER families, and Functional Families (FunFam) classifications. The rule currently has zero annotated proteins, indicating this is a recently developed or revised annotation strategy.

## Executive Summary

The ARBA00026411 rule represents a comprehensive, multi-faceted approach to annotating proteins involved in amino acid metabolism across diverse organisms. The rule encompasses a remarkably broad scope, targeting enzymes involved in amino acid biosynthesis, degradation, aminoacylation, and intercellular transport of amino acids and related metabolites. While the GO term GO:0006520 is appropriately broad for capturing the general metabolic category, the rule's 223 condition sets reveal a well-researched landscape of protein domain architecture associated with amino acid metabolism. The combination of InterPro signatures, PANTHER families, and FunFam identifiers demonstrates sophisticated knowledge of protein evolution and functional conservation. However, the rule's breadth raises questions about whether GO:0006520, being a parent term encompassing all amino acid metabolic processes, represents the most informative annotation choice compared to more specific child terms. The rule demonstrates strong biological coherence across most condition sets, with only minor concerns regarding taxonomic restrictions and potential neofunctionalization events that might warrant condition-specific refinement.

## Domain Analysis and Functional Classification

### Category 1: Aminoacyl-tRNA Synthetases and Related Proteins

The most extensively represented category in this rule encompasses aminoacyl-tRNA synthetases (aaRS), which catalyze one of the most fundamental reactions in amino acid metabolism—the activation and transfer of amino acids to their cognate transfer RNA molecules[5][6]. These enzymes are essential for translating the genetic code and represent a critical nexus between amino acid metabolism and protein synthesis. The rule includes multiple condition sets targeting both Class I and Class II aaRS enzymes across various organisms, employing distinct domain signatures such as IPR001412 (aminoacyl-tRNA synthetase, class I, conserved site), IPR002314 (aminoacyl-tRNA synthetase, class II G/P/S/T), and IPR006195 (aminoacyl-tRNA synthetase, class II).

The inclusion of specific aminoacyl-tRNA synthetases for individual amino acids represents a refinement of the rule. Condition set 46, for example, targets glycine-tRNA ligases using three distinct FunFam identifiers (3.30.720.200:FF:000001, 3.30.930.10:FF:000010, and 3.30.930.10:FF:000158), demonstrating recognition that different evolutionary lineages have evolved distinct structural solutions for the same catalytic problem. Similar specificity appears in condition sets targeting lysine-tRNA ligase, methionine-tRNA ligase, phenylalanine-tRNA ligase, and other aminoacyl-tRNA synthetases. This specificity approach aligns with established evolutionary understanding of aaRS proteins, which have diversified substantially even while maintaining core catalytic function[5].

Research on aminoacyl-tRNA synthetases has revealed that these enzymes possess complex editing mechanisms to maintain fidelity[2]. Lysyl-tRNA synthetase, a Class II enzyme, performs post-transfer editing by converting homocysteine into homocysteine thiolactone, demonstrating that these enzymes function as proofreading devices ensuring only cognate amino acids are incorporated into proteins[2]. This editing function, while primarily serving protein synthesis fidelity, clearly qualifies these enzymes as participants in amino acid metabolism according to the definition of GO:0006520.

### Category 2: Amino Acid Biosynthetic Enzymes

The rule extensively targets enzymes involved in de novo synthesis of amino acids, particularly those from the aspartate family pathway and branched-chain amino acid (BCAA) biosynthesis. The aspartate-derived amino acid pathway is exceptionally well-represented, with multiple condition sets targeting pathway-specific enzymes. This pathway synthesizes four essential amino acids—lysine, threonine, methionine, and isoleucine—which cannot be synthesized by humans and must be obtained from diet or microbial sources[9][12][45].

Condition sets 12 and 13 specifically target key pathway enzymes. Condition set 12 identifies asparaginase/glutaminase-like proteins through domain combinations including IPR006034 and IPR027473, targeting L-asparaginase enzymes in eukaryotes. These enzymes catalyze the hydrolysis of L-asparagine to L-aspartate and ammonia, representing a critical entry point into amino acid catabolism and interconnecting with the aspartate biosynthetic pathway[38][41]. The therapeutic importance of these enzymes cannot be overstated—bacterial L-asparaginases are key components of acute lymphoblastic leukemia treatment, demonstrating that the compounds produced or consumed by these enzymes have profound biological significance[41].

The branched-chain amino acid biosynthesis pathway receives substantial attention in the rule. Acetolactate synthase (ALS), also known as acetohydroxyacid synthase, catalyzes the first committed step in BCAA biosynthesis, combining two pyruvate molecules to form acetolactate (for valine and leucine biosynthesis) or combining 2-ketobutyrate with pyruvate to form acetohydroxybutyrate (for isoleucine biosynthesis)[28]. The rule includes multiple condition sets targeting ALS, including condition set 13 (combining IPR000399, IPR011766, and IPR012846) and condition sets 25, 26, and 37 targeting different aspects of this enzyme through various domain architectures.

The evolutionary conservation of ALS is reflected in its presence across bacteria, fungi, and plants, with evidence that feedback inhibition by valine and leucine represents an allosteric regulatory mechanism that evolved to prevent overproduction of these amino acids[28]. The rule's inclusion of specific PANTHER families for ALS (such as PTHR18968:SF13) demonstrates recognition that this enzyme family contains distinct functional lineages that have diverged following duplication events.

### Category 3: Tryptophan Biosynthesis and Metabolism

Tryptophan biosynthesis represents one of the most thoroughly characterized amino acid biosynthetic pathways, beginning with the shikimate pathway intermediate chorismate and proceeding through a series of well-defined enzymatic steps. The rule includes multiple condition sets targeting distinct enzymes in this pathway, reflecting comprehensive coverage of tryptophan metabolism[7][10][15][18][39][42].

Tryptophan synthase, the penultimate enzyme in tryptophan biosynthesis, appears in multiple forms within the rule. This enzyme catalyzes the condensation of indole and serine to form tryptophan, utilizing pyridoxal phosphate as a cofactor[7][10]. The enzyme exists as an α2β2 heterotetrameric complex, with the two subunits connected by a remarkable 25 Ångstrom hydrophobic channel that facilitates substrate channeling of the hydrophobic intermediate indole[10]. This substrate channeling mechanism represents an elegant solution to the problem of maintaining bioavailability of a hydrophobic intermediate in aqueous cytoplasm. Condition sets 40, 153, and others target tryptophan synthase through various domain signatures and taxonomic contexts, including restriction to plants and specific bacterial lineages.

Recent structural and kinetic investigations of tryptophan synthase have revealed an atypical mechanism for achieving substrate specificity[7]. Native tryptophan synthase can catalyze productive reactions not only with its natural substrate L-serine but also with L-threonine, yielding (2S,3S)-β-methyltryptophan as a product. Remarkably, while threonine binds efficiently to the enzyme with nearly equal affinity to serine, the enzyme demonstrates >82,000-fold preference for serine when competing for the indole nucleophile using the natural substrate indole-3-glycerol phosphate. This specificity arises not from differential substrate binding but from allosteric effects and disruption of the catalytic cycle when threonine occupies the active site[7]. This finding demonstrates that the rule's annotation must account for proteins that have evolved substrate specificity mechanisms beyond simple active site architecture.

The kynurenine pathway of tryptophan degradation receives substantial attention in the rule through multiple condition sets targeting indoleamine 2,3-dioxygenase (IDO) and tryptophan 2,3-dioxygenase (TDO). These enzymes catalyze the first and rate-limiting step in tryptophan catabolism, accounting for approximately 95% of dietary tryptophan degradation[39][42]. The kynurenine pathway exists primarily in the liver (accounting for ~90% of overall tryptophan degradation) but becomes more active extrahepatically during immune activation[39]. Beyond its role in tryptophan degradation, the kynurenine pathway produces immunoregulatory and neuroactive metabolites and serves as the source of the vitamin B3 precursor nicotinic acid. Recent research has revealed that IDO plays complex roles in metabolic health by modulating the composition and function of the gut microbiota through effects on tryptophan availability and indole metabolism[14].

### Category 4: Serine and Threonine Metabolism

Serine represents a conditionally essential amino acid with multiple biosynthetic sources and critical roles in cellular metabolism[43][46]. The rule includes several condition sets targeting serine biosynthesis and metabolism. Serine is synthesized de novo from 3-phosphoglycerate, an intermediate of glycolysis, through a three-step pathway beginning with oxidation by 3-phosphoglycerate dehydrogenase[43]. Alternatively, serine can be synthesized from glycine through the reverse reaction catalyzed by serine hydroxymethyltransferase[43]. The tryptophan synthase example mentioned above demonstrates the importance of distinguishing between threonine and serine, as while both are hydroxyl-containing amino acids, their distinct metabolic roles necessitate precise substrate specificity.

Condition sets 31, 32, and 157 target various aspects of serine metabolism through distinct domain architectures. These condition sets capture serine/threonine dehydratases, phosphoserine aminotransferases, and serine hydroxymethyltransferases. The integration of L-serine into folate and methionine cycles represents a crucial connection between amino acid metabolism and one-carbon metabolism, enabling methylation reactions essential for DNA synthesis, histone modification, and neurotransmitter synthesis[43].

### Category 5: Histidine Biosynthesis

Histidine biosynthesis, while absent from humans, represents an important pathway in microorganisms and plants[26]. The rule includes multiple condition sets targeting histidine biosynthetic enzymes through domain signatures such as IPR001348 (ATP phosphoribosyltransferase HisG), IPR001468 (indole-3-glycerol phosphate synthase, conserved site), and various FunFam identifiers. Histidine biosynthesis is tightly linked to nucleotide metabolism, as the pathway utilizes PRPP (5-phosphoribosyl 1-pyrophosphate), which also serves as a precursor for purine and pyrimidine biosynthesis[26].

The regulation of histidine biosynthesis occurs at ATP-phosphoribosyltransferase (ATP-PRT), which catalyzes the first committed step, through feedback inhibition by the end product histidine[26]. However, evidence suggests that over-expression of ATP-PRT is sufficient to overcome negative feedback inhibition in plants, indicating that allosteric regulation alone does not determine overall flux through the pathway[26]. The discovery of HISN7 enzyme in Arabidopsis, which catalyzes dephosphorylation of histidinol-phosphate to histidinol, revealed previously unknown links between histidine biosynthesis and other plant metabolic pathways[26].

### Category 6: Cysteine and Methionine Biosynthesis

Cysteine biosynthesis represents a particularly interesting case for rule evaluation, as cysteine is synthesized through transsulfuration from serine via the intermediate homocysteine. The rule targets cysteine biosynthetic enzymes including cysteine synthase (CysK/CysM) through multiple condition sets. Cysteine synthase catalyzes the final step of cysteine biosynthesis, combining serine with inorganic sulfide or thiosulfate to form cysteine[8]. The crucial role of cysteine synthase in cysteine synthesis makes it a promising target for antimicrobial agents and new herbicides[8].

An elegant study conducted through protein engineering demonstrated a fascinating aspect of amino acid metabolism relevant to this rule's design[11]. Researchers constructed biosynthetic enzymes for cysteine biosynthesis that lacked cysteine and methionine residues themselves, solving what they termed the "chicken-and-egg problem" of amino acid biosynthesis—the apparent paradox that enzymes must contain amino acids to synthesize those same amino acids. By engineering cysteine-free versions of cysteine synthase, the research team showed that the catalytic mechanism does not absolutely require the amino acid product, suggesting that early in evolutionary time, primitive metabolic enzymes might have functioned with a reduced alphabet of amino acids[11]. This finding has profound implications for understanding amino acid metabolism evolution and suggests that the specificity of the rule's condition sets must account for proteins that have acquired or lost biosynthetic capacity through evolutionary time.

The methionine biosynthetic pathway culminates in the action of methionine synthase, which regenerates methionine from homocysteine in a vitamin B12-dependent reaction[52]. The rule includes multiple condition sets targeting methionine synthase, recognizing that this enzyme catalyzes one of the most important connections between amino acid metabolism and one-carbon metabolism, as methionine is the precursor of S-adenosylmethionine (SAMe), the universal methyl donor for numerous cellular methylation reactions.

### Category 7: Arginine and Proline Biosynthesis

Arginine biosynthesis occurs through the urea cycle in mammals and through distinct pathways in other organisms. The rule targets ornithine transcarbamylase (OTC), a key enzyme catalyzing the second step of the urea cycle[19][22]. This enzyme transfers the carbamoyl group from carbamoyl phosphate to the amino group of L-ornithine, yielding citrulline and inorganic phosphate. The urea cycle ensures conversion of toxic ammonia into urea for excretion and maintains arginine pools[19]. Interestingly, OTC expression is dysregulated in tumors, where it participates in rewiring nitrogen metabolism to support cancer growth and aggressiveness[19]. This demonstrates that the rule's scope must encompass both normal metabolic functions and pathophysiological manifestations of amino acid metabolism.

Proline biosynthesis begins with the action of pyrroline-5-carboxylate synthase (P5CS), a bifunctional enzyme exhibiting both glutamate kinase and γ-glutamyl phosphate reductase activities[21]. This enzyme is highly relevant to humans because mutations in P5CS are associated with rare inherited metabolic diseases, and in plants, proline accumulation in response to osmotic stress represents a critical adaptive mechanism. The rule includes condition sets targeting P5CS through FunFam identifiers, recognizing the evolutionary conservation of this enzyme across diverse organisms[21].

### Category 8: Tyrosine and Phenylalanine Biosynthesis

The aromatic amino acid biosynthetic pathway culminates in the divergence of chorismate into three distinct branches leading to phenylalanine, tyrosine, and tryptophan biosynthesis. Chorismate mutase catalyzes the committed step for phenylalanine and tyrosine synthesis through a remarkable pericyclic Claisen rearrangement—the single known example of a naturally occurring enzyme catalyzing a pericyclic reaction[50][53]. This enzyme exists at a branch point, channeling chorismate away from tryptophan biosynthesis toward the phenylalanine/tyrosine branch[50].

The regulation of chorismate mutase demonstrates sophisticated allosteric control mechanisms that vary across organisms[53]. Structural and biochemical studies of three Arabidopsis thaliana chorismate mutase isoforms revealed distinct sets of allosteric effectors—while AtCM1 is activated by tryptophan with phenylalanine and tyrosine acting as negative effectors, AtCM3 shows activation by tryptophan, cysteine, and histidine[53]. The identification of specific residues (particularly Asp132 in AtCM3) that are critical for determining effector specificity suggests that neofunctionalization has occurred within this enzyme family, requiring the rule to account for variant functions within domain families[53].

Tyrosine hydroxylase catalyzes the first committed step in catecholamine biosynthesis, converting tyrosine to L-DOPA[16]. This enzyme is subject to sophisticated regulation through multiple mechanisms, including feedback inhibition by dopamine, phosphorylation by multiple protein kinases, and protein-protein interactions with regulatory proteins like 14-3-3 proteins[16]. Recent research demonstrates that tyrosine hydroxylase undergoes post-translational modifications including nitration and glutathionylation in the presence of nitric oxide, indicating that the metabolic function of this enzyme is modulated by reactive nitrogen species[16]. This finding emphasizes that amino acid metabolism encompasses not only catalytic function but also regulation through post-translational modification and protein-protein interactions.

## GO Term Evaluation

### Appropriateness of GO:0006520

The Gene Ontology term GO:0006520 "amino acid metabolic process" is defined as "The chemical reactions and pathways involving amino acids, carboxylic acids containing one or more amino groups"[1][4]. This definition directly encompasses all 223 condition sets represented in the rule, as each targeted enzyme catalyzes reactions or participates in pathways involving amino acids as substrates, products, or both.

The GO term hierarchy provides important context for evaluating the specificity of this annotation. GO:0006520 is classified as a biological process term under the parent term "primary metabolic process"[31][34]. Within the aminoacyl-tRNA synthetase category alone, more specific child terms exist, including GO:0006418 (aminoacyl-tRNA biosynthesis) and even more specific terms for individual amino acids. Similarly, amino acid biosynthetic processes can be annotated to terms such as GO:0008652 (cellular amino acid biosynthetic process) or even more specific terms like GO:0006526 (arginine biosynthesis), GO:0006568 (tryptophan biosynthesis), or GO:0006565 (threonine biosynthesis).

A critical assessment of the rule reveals a fundamental tension in annotation design. The term GO:0006520 represents an appropriate parent-level annotation for proteins involved in diverse amino acid metabolic functions. However, the specificity of many proteins in the rule would permit annotation to multiple, more informative child terms. For instance, a protein annotated only as participating in GO:0006520 loses the information that it specifically participates in lysine biosynthesis (GO:0009758) or tryptophan degradation (GO:0006571). From a functional annotation perspective, the rule prioritizes broad coverage—ensuring that all proteins involved in amino acid metabolism receive consistent annotation—over functional specificity.

### Considerations for Alternative GO Terms

The analysis of condition sets reveals that several alternative or additional GO annotations would be more informative for specific proteins. For instance, condition sets targeting aminoacyl-tRNA synthetases (condition sets 2, 11, 29, 38, 46, 79, 80, 82, 92, 122, 128, 133, 151, 166, 182, 191, 198) could appropriately be annotated to GO:0006418 (aminoacyl-tRNA biosynthesis), which more specifically captures the function of transferring amino acids to tRNA molecules. This more specific annotation would distinguish aaRS proteins from biosynthetic and catabolic enzymes.

Similarly, the numerous condition sets targeting amino acid biosynthetic enzymes could be annotated to GO:0008652 (cellular amino acid biosynthetic process), which is more specific than the parent term GO:0006520. This would allow distinction between anabolic and catabolic amino acid metabolism. The rule's current design essentially treats biosynthesis, degradation, aminoacylation, and intercellular metabolism as equivalent categories, which, while not incorrect, obscures important functional distinctions.

### Potential for Neofunctionalization and Moonlighting Functions

A critical consideration in evaluating the appropriateness of GO:0006520 involves recognition of neofunctionalization events and moonlighting functions that some proteins in these families have acquired. The tryptophan synthase example discussed earlier demonstrates that proteins annotated as amino acid metabolic enzymes may have additional functions beyond their canonical roles. Similarly, several proteins identified through InterPro domain signatures may have evolved functions distinct from the original function of the domain.

For instance, glutamine synthetase (GS), while primarily serving nitrogen assimilation and glutamine biosynthesis, has recently been identified as possessing additional "moonlighting" functions in palmitoylation, cell cycle regulation, and ion channel modulation[54]. While these moonlighting functions are performed by the same protein, they extend beyond traditional amino acid metabolism. The rule's design appropriately annotates GS to GO:0006520 based on its primary catalytic function, but this annotation would not capture the protein's broader biochemical repertoire.

## Evidence Review and Literature Support

### Experimental Evidence for Enzymatic Function

The search results provide strong experimental support for the functions represented in the rule. Research on aminoacyl-tRNA synthetases has characterized their catalytic mechanisms, proofreading functions, and evolutionary relationships in considerable detail[2][5]. The discovery of specific editing mechanisms, such as the conversion of homocysteine to homocysteine thiolactone by lysyl-tRNA synthetase, demonstrates sophisticated proofreading mechanisms evolved to maintain translational accuracy[2].

Biochemical investigations of amino acid biosynthetic enzymes have revealed regulatory mechanisms including feedback inhibition, allosteric activation, and protein-protein interactions. The aspartate-derived amino acid pathway has been extensively characterized through metabolic flux analysis and regulatory mutation studies, revealing complex allosteric control mechanisms that maintain metabolic balance across the pathway's multiple branches[9]. For instance, the regulation of aspartate kinase by multiple amino acids simultaneously (threonine, lysine) demonstrates synergistic allosteric effects that require multiple molecular interactions within the protein structure[9].

The tryptophan biosynthetic pathway has been thoroughly investigated, with recent structural studies revealing details of substrate binding, catalytic mechanism, and allosteric regulation. The discovery that tryptophan synthase can efficiently catalyze β-substitution of threonine despite >82,000-fold preference for serine in competition experiments reveals sophisticated allosteric specificity mechanisms that extend beyond traditional active site considerations[7].

### Taxonomic Conservation and Distribution

The rule includes 56 condition sets with specific taxonomic restrictions, reflecting recognition that certain protein families and functions exhibit differential distribution across organisms. For instance, condition set 10 restricts to Fungi and identifies ACT-like domain proteins, while condition set 36 restricts chorismate mutase II to Ascomycota fungi, and condition set 40 identifies tryptophan synthase in all domains of life where it is found—which notably excludes animals that obtain tryptophan through diet[10].

The restriction of tryptophan synthase to bacteria, archaebacteria, protista, fungi, and plants, explicitly excluding animals, represents accurate biological knowledge[10]. Humans and other animals have lost tryptophan biosynthetic capacity through evolution and instead obtain tryptophan as an essential dietary amino acid. This restriction demonstrates that the rule designers have incorporated sophisticated knowledge of metabolic evolution and the acquisition and loss of biosynthetic pathways across the tree of life.

However, certain taxonomic restrictions warrant closer examination. For instance, several condition sets include restrictions to specific bacterial phyla (Pseudomonadota, Bacillati, etc.) or fungal lineages (Ascomycota, Taphrinomycotina, Dikarya). While these restrictions reflect the known distribution of specific enzyme variants, they carry an implicit risk of excluding organisms that have evolved alternative solutions to similar metabolic problems through convergent evolution. The rule's design demonstrates awareness of this concern through the inclusion of multiple condition sets targeting functionally equivalent enzymes across different organismal lineages.

### Known Multifunctionality and Pathway Interconnections

Amino acid metabolism is deeply interconnected with multiple other metabolic pathways, and several proteins in the rule participate in multiple metabolic processes. Serine, for instance, serves as a substrate for multiple biosynthetic pathways, including sphingolipid synthesis, phospholipid synthesis, and nucleotide synthesis[43]. The inclusion of serine-metabolizing enzymes in this rule captures only their amino acid metabolic functions, potentially obscuring their roles in other pathways.

Glutaminase enzymes occupy an interesting position in amino acid metabolism, functioning both in amino acid catabolism and nitrogen metabolism[37]. The rule targets these enzymes through multiple condition sets (condition sets 37, 47, and 126), recognizing their central role in glutamine metabolism and their contributions to amino acid homeostasis.

The interconnection between amino acid metabolism and energy metabolism represents another important consideration. Several amino acids serve as gluconeogenic substrates or enter the tricarboxylic acid cycle as anaplerotic substrates. The aspartate family pathway demonstrates particularly tight coupling to energy metabolism, with some research indicating that metabolic engineering approaches designed to increase lysine biosynthesis inadvertently disrupt tricarboxylic acid cycle metabolism and impair stress responses[45]. This finding suggests that annotation of biosynthetic enzymes to GO:0006520 must be understood as capturing only the amino acid biosynthetic function, not the broader metabolic consequences of altered enzyme expression.

### Clinical and Biotechnological Significance

Several proteins in the rule have substantial clinical significance, which contextualizes the importance of accurate functional annotation. L-asparaginase enzymes have been extensively studied because bacterial L-asparaginases serve as key components of chemotherapy regimens for acute lymphoblastic leukemia[38][41]. The selective depletion of asparagine by these enzymes preferentially affects leukemic cells, which often require external asparagine supply[38][41]. Recent structural studies have elucidated the catalytic mechanism and specificity determinants of these enzymes, revealing that different asparaginase classes employ distinct catalytic strategies to achieve the same overall reaction[38][41].

The study of cysteine synthase has expanded due to its potential applications in antimicrobial therapy and herbicide development, reflecting industrial and medical interest in this enzyme[8]. The successful protein engineering of cysteine-free cysteine synthase variants demonstrates possibilities for rational enzyme design applied to proteins within this rule[11].

Tyrosine hydroxylase dysfunction underlies genetic forms of dopamine deficiency and has been investigated for gene therapy applications to treat Parkinson's disease[13][16]. Understanding the catalytic mechanism, regulation, and protein-protein interactions of tyrosine hydroxylase has directly contributed to rational approaches for genetic therapy.

## Domain Architecture Assessment

### InterPro Domain Signature Specificity

The 223 condition sets employ diverse strategies for identifying proteins involved in amino acid metabolism through InterPro domain signatures. Some condition sets utilize single highly specific domain signatures—for instance, condition set 30 identifies all indoleamine 2,3-dioxygenase proteins through a single domain signature (IPR000898). This approach assumes that the domain is diagnostic for the function, which appears justified given that IDO is fundamentally defined by its ability to open the indole ring of tryptophan.

Other condition sets employ combinations of multiple domain signatures to enhance specificity. For instance, condition set 7 combines three domain signatures (IPR002292, IPR006130, IPR006131) all related to ornithine/aspartate carbamoyltransferase to identify proteins participating in the urea cycle and arginine biosynthesis. This combinatorial approach reduces false positives by requiring proteins to match multiple functional signatures simultaneously.

The inclusion of PANTHER superfamily and subfamily identifiers introduces another layer of specificity. PANTHER families represent evolutionary relationships inferred from phylogenetic trees and are often more specific than InterPro domains alone. For instance, condition set 16 combines InterPro domain identifiers for aromatic amino acid hydroxylase with a specific PANTHER subfamily identifier (PTHR11473:SF24), which narrows the identification to specific variant forms of the enzyme.

### Functional Family (FunFam) Approach

The inclusion of 120 condition sets employing Functional Families (FunFam) from CATH represents a sophisticated approach to identifying proteins based on evolutionary relationships and inferred function. FunFams represent clusters of proteins within CATH superfamilies that likely share similar functions based on evolutionary distance and sequence conservation[57]. This approach recognizes that proteins with similar three-dimensional structures and evolutionary relationships often share functional properties despite limited sequence identity.

The FunFam approach appears particularly valuable for identifying proteins with multifunctional capabilities or those that have undergone neofunctionalization. For instance, condition set 43 identifies cystathionine beta-synthase (CBS) through FunFam 3.40.50.1100:FF:000003, while condition set 44 identifies "Related to CYS4-cystathionine beta-synthase" through a different FunFam (3.40.50.1100:FF:000118). This distinction within the same CATH superfamily suggests recognition that different evolutionary lineages of CBS-like proteins may have diverged in function.

Similarly, condition set 53 identifies methionine synthase through three distinct FunFam identifiers (1.10.1240.10:FF:000001, 3.20.20.20:FF:000002, and 3.20.20.330:FF:000001), recognizing that methionine synthase appears in multiple CATH structural classes despite performing similar biochemical function.

## Potential Issues and Limitations

### Rule Breadth and Potential for False Positives

The rule encompasses 223 distinct condition sets targeting proteins involved in amino acid metabolism across the three domains of life. While this breadth reflects genuine diversity in amino acid metabolic pathways and proteins, it carries inherent risks of false positives—proteins that match the condition sets but lack the predicted metabolic function due to neofunctionalization, domain shuffling, or other evolutionary processes.

For instance, several proteins possess domains characteristic of amino acid metabolic enzymes but have been repurposed for different functions. A hypothetical protein containing a pyridoxal phosphate binding domain combined with an aldehyde dehydrogenase domain (as specified in condition set 5) would be predicted as involved in amino acid metabolism, yet such domain combinations might also appear in proteins with distinct functions. The rule's designers attempted to mitigate this concern through specific domain combinations rather than single domain matches, but the risk remains for condition sets employing very specific or limited domain combinations.

### Taxonomic Restriction Considerations

Several condition sets include taxonomic restrictions that might exclude proteins performing similar functions in organisms outside the specified taxa. For instance, condition set 96 restricts anthranilate phosphoribosyltransferase identification to Saccharomycotina (budding yeasts), yet this enzyme likely performs identical functions in other fungal lineages outside this restriction. The restriction presumably reflects the availability of validated training data from well-characterized yeast genomes, but it risks excluding functionally equivalent proteins in under-studied organisms.

Similarly, condition set 104 restricts shikimate kinase identification to Liliopsida (monocots), a restriction that seems overly narrow given that shikimate kinase functions identically across all plants. This restriction likely reflects practical considerations in rule development—focusing on well-annotated reference organisms—but represents a potential source of false negatives in less-studied organismal groups.

### Neofunctionalization and Context-Dependent Function

The rule assumes that the presence of specific domain architectures reliably predicts participation in amino acid metabolism. However, several proteins targeted by this rule have evolved additional functions that extend beyond traditional amino acid metabolism. Glutamine synthetase's moonlighting functions in palmitoylation and cell cycle regulation occur through the same protein utilized for glutamine biosynthesis[54]. While the rule appropriately annotates GS to GO:0006520 based on its amino acid metabolic function, this annotation might insufficiently capture the protein's full biological role.

The discovery that tyrosine hydroxylase undergoes modification by reactive nitrogen species and that these modifications alter its catalytic properties raises questions about whether the functional annotation should encompass regulatory mechanisms alongside catalytic function[16]. If protein nitration and glutathionylation alter tyrosine hydroxylase activity, does annotation to GO:0006520 capture these regulatory dimensions?

### Potential Overestimation of Consensus Function

Several condition sets employ multiple domain signatures with OR logic—meaning proteins matching ANY of the conditions receive the annotation. For instance, condition sets combining multiple FunFam identifiers for the same enzyme (such as condition set 53 with three methionine synthase FunFams) likely represent equivalent annotations, but they increase the overall specificity of the condition set. However, if one of these FunFams has undergone neofunctionalization or if classification errors have led to misassignment of proteins to a FunFam, false annotations could result.

## Recommendations

### Refinement of GO Term Granularity

The analysis reveals that while GO:0006520 appropriately captures all proteins matched by the rule, greater biological informativeness could be achieved through annotation to more specific child terms. A tiered annotation strategy would provide:

1. **Primary annotation to GO:0006520** for all amino acid metabolic enzymes, ensuring consistent coverage
2. **Secondary annotations to specific child terms** capturing more precise metabolic functions:
   - GO:0006418 for aminoacyl-tRNA synthetases
   - GO:0008652 for amino acid biosynthesis
   - GO:0006571 for tryptophan degradation
   - GO:0006565 for specific amino acid biosynthesis pathways (threonine, lysine, etc.)

This approach would preserve the rule's comprehensive coverage while enabling biological databases to support more specific queries about particular metabolic processes.

### Expansion of Taxonomic Coverage

Several condition sets employing taxonomic restrictions would benefit from validation and potential expansion to broader taxonomic groups. For instance, the restriction of shikimate kinase identification to Liliopsida should be reconsidered given that this enzyme performs identical functions across all plants. Expanding such restrictions would improve sensitivity for identifying functionally equivalent proteins in less-studied organisms.

### Incorporation of Regulatory and Post-Translational Modification Data

Several proteins in this rule are regulated through post-translational modifications, protein-protein interactions, and allosteric effects. Integrating information about these regulatory mechanisms into the rule design could enhance the accuracy of functional predictions. For instance, annotating tyrosine hydroxylase could incorporate information about its regulation through phosphorylation by multiple kinases, which fundamentally alters the enzyme's kinetic properties and catalytic efficiency[16].

### Validation Against Structural Genomics and Proteomics Data

The rule would benefit from validation against recent structural biology databases and large-scale proteomics studies. The application of AlphaFold structure prediction to entire proteomes might reveal novel domain architectures or functional relationships not captured by current InterPro, PANTHER, and FunFam classifications. Integration of high-resolution mass spectrometry-based proteomics data could help identify proteins being enzymatically modified (through phosphorylation, ubiquitination, etc.) under conditions of amino acid stress or abundance.

### Monitoring of Recent Literature

Given the rapid pace of discovery in amino acid metabolism, the rule would benefit from regular literature review to incorporate new findings about enzymatic mechanisms, evolutionary relationships, and potential neofunctionalization events. Recent publications on specific enzyme families should be systematically evaluated for evidence of functions not currently captured in the rule.

## Conclusion

ARBA00026411 represents a well-researched and comprehensive annotation rule for identifying proteins involved in amino acid metabolic processes. The rule's 223 condition sets demonstrate sophisticated knowledge of protein domain architecture, evolutionary relationships, and enzymatic function across diverse organisms. The inclusion of InterPro domain signatures, PANTHER families, and Functional Family identifiers reflects multiple complementary approaches to protein function prediction, each with distinct advantages and limitations.

The predicted GO term GO:0006520 (amino acid metabolic process) is appropriately broad and accurately captures the functions of all proteins matched by the condition sets. However, the rule's design reflects a deliberate choice to prioritize comprehensive coverage over functional specificity—proteins that could be annotated to more specific child terms like GO:0006418 (aminoacyl-tRNA biosynthesis) or GO:0006565 (specific amino acid biosynthesis pathways) are instead annotated only to the parent term GO:0006520. This design choice appropriately emphasizes the importance of consistent, broad-coverage annotation while sacrificing maximal functional specificity.

The rule demonstrates strong alignment with current understanding of amino acid metabolism biochemistry, with support from extensive experimental literature characterizing enzymatic mechanisms, regulation, and evolutionary relationships. Potential limitations primarily concern the breadth of the rule—the 223 condition sets must necessarily make assumptions about the relationship between protein domain architecture and function, assumptions that generally hold but which may produce false positives in cases of neofunctionalization, domain shuffling, or evolutionary adaptation. Nevertheless, the rule's careful design, incorporating specific domain combinations and, in many cases, taxonomic restrictions, represents a sophisticated effort to balance sensitivity and specificity in functional annotation.

Future refinement of this rule would benefit from expansion of GO term granularity to capture more specific metabolic processes, validation of taxonomic restrictions against recent genomic and proteomics data, and systematic incorporation of newly discovered enzymatic functions and regulatory mechanisms revealed by ongoing research in amino acid metabolism biochemistry.

## Citations

1. https://amigo.geneontology.org/amigo/term/GO:0006520
2. https://pubs.acs.org/doi/abs/10.1021/bi970589n
3. https://suba.live/factsheet/AT4G17300.1.html
4. https://www.pombase.org/term/GO:0006520
5. https://pubmed.ncbi.nlm.nih.gov/14530268/
6. https://www.uniprot.org/uniprotkb/Q81WL6
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC5207025/
8. https://pubmed.ncbi.nlm.nih.gov/41176792/
9. https://www.embopress.org/doi/10.1038/msb.2009.29
10. https://en.wikipedia.org/wiki/Tryptophan_synthase
11. https://www.nature.com/articles/s41598-018-19920-y
12. https://pubmed.ncbi.nlm.nih.gov/11352712/
13. https://pubmed.ncbi.nlm.nih.gov/9349551/
14. https://www.nature.com/articles/s41574-018-0063-8
15. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1625337/full
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC3065393/
17. https://www.ncbi.nlm.nih.gov/gene/3620
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC10520873/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC8517447/
20. https://en.wikipedia.org/wiki/Homogentisate_1,2-dioxygenase
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC2866264/
22. https://www.uniprot.org/uniprotkb/Q9N1U7/entry
23. https://www.ncbi.nlm.nih.gov/gene/3081
24. https://www.uniprot.org/uniprotkb/P32296/entry
25. https://pubmed.ncbi.nlm.nih.gov/28388946/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC3266711/
27. https://pubmed.ncbi.nlm.nih.gov/27137927/
28. https://passel2.unl.edu/view/lesson/504781cce66a/2
29. https://www.uniprot.org/uniprotkb/P60757/entry
30. https://nph.onlinelibrary.wiley.com/doi/10.1111/j.1469-8137.2010.03460.x
31. https://www.informatics.jax.org/vocab/gene_ontology/GO:0006520
32. https://www.ebi.ac.uk/interpro/
33. https://www.uniprot.org/help/automatic_annotation
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC10468136/
35. https://www.uniprot.org/help/arba
36. https://www.publish.csiro.au/ch/CH22264
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC8948990/
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC5398323/
39. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC214962/pdf/jbacter00225-0343.pdf
40. https://www.nature.com/articles/s41598-022-19689-1
41. https://www.nature.com/articles/s12276-023-01028-7
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC9105362/
43. https://journals.asm.org/doi/10.1128/mbio.00395-22
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC3121977/
45. https://www.frontiersin.org/journals/cellular-and-infection-microbiology/articles/10.3389/fcimb.2025.1518659/full
46. https://pubmed.ncbi.nlm.nih.gov/789352/
47. https://onlinelibrary.wiley.com/doi/abs/10.1128/9781555818388.ch18
48. https://pubmed.ncbi.nlm.nih.gov/4517673/
49. https://en.wikipedia.org/wiki/Chorismate_mutase
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC99658/
51. https://en.wikipedia.org/wiki/Methionine_synthase
52. https://pmc.ncbi.nlm.nih.gov/articles/PMC4192511/
53. https://pubs.acs.org/doi/10.1021/acs.biochem.4c00763
54. https://en.wikipedia.org/wiki/False_positives_and_false_negatives
55. https://pmc.ncbi.nlm.nih.gov/articles/PMC9743508/
56. https://academic.oup.com/nar/article/53/D1/D444/7905301
57. https://arxiv.org/html/2509.20491v1
58. https://pmc.ncbi.nlm.nih.gov/articles/PMC9825450/
59. the definition of GO:0006520