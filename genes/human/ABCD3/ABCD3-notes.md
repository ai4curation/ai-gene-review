# ABCD3 (PMP70) Research Notes

## Gene Overview
ABCD3 (ATP-binding cassette sub-family D member 3), also known as PMP70, is a peroxisomal ABC half-transporter that forms homodimers to catalyze ATP-dependent import of fatty acid substrates into peroxisomes for beta-oxidation.

## Key Literature Findings

### Substrate Specificity
- ABCD3 has broad substrate specificity, preferring hydrophilic substrates: long-chain unsaturated fatty acids, branched-chain fatty acids (pristanic acid), dicarboxylic acids, and bile acid CoA-esters [PMID:24333844 "most hydrophilic substrates like long-chain unsaturated-, long branched-chain- and long-chain dicarboxylic fatty acids by HsABCD3"]
- Substrate specificity overlaps with ABCD1 and ABCD2, but ABCD3 is distinct in preferring hydrophilic substrates [PMID:24333844]
- Each half-transporter can function as a homodimer [PMID:24333844 "each peroxisomal half-transporter can function as homodimer"]

### Bile Acid Transport - Critical Evidence
- ABCD3-deficient patient: accumulation of peroxisomal C27-bile acid intermediates (DHCA, THCA) in plasma, establishing ABCD3 role in bile acid biosynthesis [PMID:25168382 "ABCD3 is involved in transport of branched-chain fatty acids and C27 bile acids into the peroxisome and that this is a crucial step in bile acid biosynthesis"]
- Abcd3 knockout mice: accumulation of phytanic acid after phytol loading; reduction of C24 bile acids with increased C27 bile acid intermediates [PMID:25168382]
- This causes CBAS5 (Congenital bile acid synthesis defect 5) [PMID:25168382]
- NOTE: The bile acid transport evidence is primarily from patient/mouse studies (loss-of-function), not direct in vitro transport assays with bile acid substrates

### Dicarboxylic Acid Transport
- Abcd3 knockout mice show increased hepatic long-chain DCAs (C14-C18) and urinary medium-chain DCAs [PMID:34564857 "ABCD3 mediates transport of dicarboxylic acids into peroxisomes"]
- Knockout mice show hepatomegaly, lipodystrophy, elevated C27 bile acid precursors [PMID:34564857]

### ATPase and Thioesterase Activities
- Purified NBF of PMP70: KM for ATP = 8.2 uM; ATP-specific, no GTPase activity [PMID:11248239]
- G478R mutation decreased ATP binding; S572I decreased ATPase activity [PMID:11248239]
- Reconstituted in proteoliposomes: displays stable ATPase activity (inhibited by AlF3) and acyl-CoA thioesterase activity [PMID:29397936 "ABCD1-4 were found to possess equal levels of acyl-CoA thioesterase activity"]

### Cryo-EM Structural Studies
1. **Xu et al. 2024 (PMID:39223112)** - Cell Discovery
   - Two cryo-EM structures: phytanoyl-CoA-bound (2.9 A) and ATP-bound (3.2 A)
   - Inward-facing (substrate-bound) and outward-facing (ATP-bound) conformations
   - Two phytanoyl-CoA molecules bind individually to each TMD (distinct from ABCD1)
   - Bile acid intermediates DHCA-CoA and THCA-CoA are ABCD3-specific substrates
   - ATP binding causes "scissor-like movement" expanding translocation cavity exit by ~13.7 A
   - PDB: 8Z0F, 8Z9X

2. **2025 PNAS paper (PMID:40501884)**
   - Full-length ABCD3: apo (3.33 A) and phytanoyl-CoA-bound (3.13 A) structures
   - Both inward-facing conformations
   - Substrate binding induces ~5-fold increase in ATPase activity
   - Substrate binding reduces NBD separation (38.18 to 34.28 A)
   - Proposed cycle: substrate binding -> NBD closure -> ATP binding -> outward-open -> substrate release -> ATP hydrolysis -> reset

### Direct Evidence for ATP-dependent Bile Acid Transport
- The Xu et al. 2024 cryo-EM paper (PMID:39223112) tested bile acid intermediates DHCA-CoA and THCA-CoA and found them to be ABCD3-specific substrates
- However, the primary in vivo evidence comes from loss-of-function studies (patient + KO mice) showing bile acid intermediate accumulation [PMID:25168382]
- Direct in vitro reconstitution assays demonstrating ATP-dependent transport of bile salt CoA esters specifically by ABCD3 proteoliposomes have not been published as of this review

### Dimerization and Interactions
- Forms homodimers (FRET microscopy) [PMID:17609205]
- Can form heterodimers with ABCD1 and ABCD2 [PMID:10551832, PMID:17609205]
- Interacts with PEX19 for peroxisomal targeting [PMID:10704444, PMID:16344115, PMID:17761678]

### Peroxisome Organization
- Overexpression of PMP70 can suppress PEX2 deficiency and restore peroxisome biogenesis [PMID:9425230, PMID:9765053]
- This likely reflects the importance of ABC transporters in peroxisomal membrane organization

### Key Questions for Review
1. Is "fatty acid biosynthetic process" (GO:0006633) annotated via PMID:25168382 appropriate? The paper describes bile acid biosynthesis defect, not fatty acid biosynthesis per se.
2. "Peroxisomal matrix" localization (GO:0005782) - ABCD3 is a transmembrane protein; matrix localization seems incorrect unless referring to the NBD domain orientation.
3. Multiple "protein binding" (GO:0005515) annotations - per curation guidelines, these are uninformative and should be replaced with specific binding terms.
4. "Identical protein binding" (GO:0042802) via IEA - should be replaced by the IDA-supported "protein homodimerization activity" annotation.
5. Mitochondrial localization (GO:0005739) - IEA transferred from rat; ABCD3 is well-established as peroxisomal.
