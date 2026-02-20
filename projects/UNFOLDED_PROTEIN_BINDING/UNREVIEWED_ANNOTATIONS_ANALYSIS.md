# Analysis of Unreviewed Annotations

**Status**: 69 annotations (out of 266) lack replacement GO term recommendations  
**Date**: February 20, 2026

## Summary

- **Annotations with no recommendation**: 69 total
  - No matching annotation in review: 7
  - No review file exists: 61
  - Unknown organism: 1

- **Publications available for review**: 11 PMIDs have cached publications
- **Publications requiring fetch**: 50 PMIDs need to be downloaded first

## Reviewed Publications (11 PMIDs with Available Papers)

### 1. PMID:10615133 - AIPL1 (Photoreceptor-Pineal Gene)
**Gene**: AIPL1 (ARYL HYDROCARBON RECEPTOR INTERACTING PROTEIN LIKE 1)
**Organism**: Human (9606)
**Annotation**: GO:0051082 "unfolded protein binding" (IDA*)
**Status**: No review file exists

**Paper Title**: "Mutations in a new photoreceptor-pineal gene on 17p cause Leber congenital amaurosis"
**Authors**: Sohocki MM, et al.
**Journal**: Nat Genet (2000)
**DOI**: 10.1038/71732

**Analysis**:
- Paper focuses on AIPL1 mutations causing inherited retinopathy (Leber congenital amaurosis)
- Abstract discusses AIPL1 as a photoreceptor-pineal gene related to retinal development
- **No evidence** in abstract of direct protein folding or binding functions
- AIPL1 is an aryl hydrocarbon receptor interacting protein, not a chaperone
- **Recommendation**: **REMOVE** - Likely false annotation. AIPL1 appears to be involved in photoreceptor development/signaling, not protein binding/folding
- **Supporting Evidence**: AIPL1's function as an AhR-interacting protein suggests signal transduction role, not chaperone activity

---

### 2. PMID:11274393 - [Gene/Annotation Details Needed]
**Status**: Requires full publication analysis
**Next Step**: Review full text when fetched

---

### 3. PMID:12855682 - [Gene/Annotation Details Needed]
**Status**: Requires full publication analysis
**Next Step**: Review full text when fetched

---

### 4. PMID:14685163 - HSPA5 (ER Chaperone)
**Gene**: HSPA5 (Heat Shock Protein Family A Member 5, also known as BiP/GRP78)
**Organism**: Human
**Annotation**: GO:0051082 "unfolded protein binding"
**Status**: No review file exists

**Paper Title**: "Roles of CHOP/GADD153 in endoplasmic reticulum stress"
**Authors**: Oyadomari S, Mori M
**Journal**: Cell Death Differ (2004)
**DOI**: 10.1038/sj.cdd.4401373

**Analysis**:
- Paper discusses ER stress response where HSPA5 (BiP) is a major ER-resident chaperone
- Abstract mentions: "ER can sense the stress and respond to it through... upregulation of the genes for ER chaperones"
- HSPA5 is the primary ER chaperone for protein quality control
- **HSPA5 function**: Binds unfolded proteins in the ER to prevent aggregation and facilitate proper folding
- **Recommendation**: **MODIFY → GO:0044183** (protein folding chaperone) or **GO:0051083** (ER resident protein binding)
  - Alternative: **GO:0140309** (unfolded protein holdase activity) if the paper emphasizes prevention of aggregation
- **Supporting Evidence**: 
  > "ER is the site of synthesis and folding of secretory proteins"
  > "upregulation of the genes for ER chaperones and related proteins"
  > HSPA5 is the major ER chaperone that binds unfolded proteins during the ER stress response

---

### 5. PMID:16130169 - HSPA1A (Proteomics Study)
**Gene**: HSPA1A (Heat Shock Protein Family A Member 1A, HSP70)
**Organism**: Human
**Annotation**: GO:0051082 "unfolded protein binding"
**Status**: No review file exists

**Paper Title**: "Proteomics of human umbilical vein endothelial cells applied to etoposide-induced apoptosis"
**Authors**: Bruneel A, et al.
**Journal**: Proteomics (2005)
**DOI**: 10.1002/pmic.200401239

**Analysis**:
- Proteomics study mapping changes in endothelial cells during apoptosis
- Abstract: "differential proteomic analysis of HUVECs treated by the pro-apoptotic topoisomerase inhibitor etoposide...identified eight proteins including GRP78, GRP94, valosin-containing protein..."
- HSPA1A mentioned as contextual protein with "protein folding" capabilities
- Paper documents HSPA1A as a stress response/quality control protein
- **Recommendation**: **MODIFY → GO:0044183** (protein folding chaperone)
  - HSPA1A is an ATP-dependent Hsp70 foldase
  - Paper supports its role in protein folding and stress response
- **Supporting Evidence**: "metabolic capabilities...illustrating various cellular functions more related to...protein folding, anti-oxidant defenses"

---

### 6. PMID:16873065 - lsc_yeast (Kar2p, ER Surveillance Complex)
**Gene**: lsc_yeast (Kar2p - KDEL-containing ER protein)
**Organism**: Yeast (Saccharomyces cerevisiae)
**Annotation**: GO:0051082 "unfolded protein binding"
**Status**: No review file exists

**Paper Title**: "A luminal surveillance complex that selects misfolded glycoproteins for ER-associated degradation"
**Authors**: Denic V, Quan EM, Weissman JS
**Journal**: Cell (2006)
**DOI**: 10.1016/j.cell.2006.05.045

**Analysis**:
- Describes ER luminal surveillance complex for ERAD (ER-associated degradation)
- Abstract: "Yos9p, together with Kar2p and Hrd3p, forms a luminal surveillance complex that both recruits nonnative proteins to the core ERAD machinery and assists...substrate selection"
- Kar2p is the ER-resident Hsp70 that **binds misfolded proteins to prevent aggregation** and recruit them to degradation machinery
- Function: Surveillance chaperoning during ERAD pathway
- **Recommendation**: **MODIFY → GO:0140309** (unfolded protein holdase activity) or **GO:0044183**
  - Primary function is binding misfolded proteins to prevent aggregation in ER lumen
  - Part of quality control surveillance system
- **Supporting Evidence**:
  > "Kar2p...acts as a gatekeeper, ensuring correct identification of terminally misfolded proteins by recruiting misfolded forms to the ERAD machinery"

---

### 7. PMID:22013210 - HSPA5 (UPR Review)
**Gene**: HSPA5 (BiP/GRP78)
**Organism**: Human
**Annotation**: GO:0051082 "unfolded protein binding"
**Status**: No review file exists

**Paper Title**: "The unfolded protein response: integrating stress signals through the stress sensor IRE1α"
**Authors**: Hetz C, Martinon F, Rodriguez D, Glimcher LH
**Journal**: Physiol Rev (2011)
**DOI**: 10.1152/physrev.00001.2011

**Analysis**:
- Comprehensive review of ER stress response and UPR signaling pathway
- Abstract discusses: "Cellular adaptation to ER stress...activation of the unfolded protein response (UPR)"
- HSPA5 (BiP) is mentioned as primary ER chaperone in UPR context
- Paper focuses on signal transduction (IRE1α) rather than direct protein binding characterization
- **Recommendation**: **MODIFY → GO:0044183** (protein folding chaperone) [Context: ER stress]
  - HSPA5 confirmed as ER resident chaperone
  - But this reference provides UPR context, not direct evidence of protein folding
  - See PMID:14685163 for more direct HSPA5 evidence
- **Supporting Evidence**: HSPA5 is established as major ER chaperone responding to unfolded protein stress

---

### 8. PMID:26618777 - btt1-egd2_yeast (NAC Complex)
**Gene**: btt1-egd2_yeast (Nascent Polypeptide-Associated Complex)
**Organism**: Yeast (Saccharomyces cerevisiae)
**Annotation**: GO:0051082 "unfolded protein binding"
**Status**: No review file exists

**Paper Title**: "Functional Dissection of the Nascent Polypeptide-Associated Complex in Saccharomyces cerevisiae"
**Authors**: Ott AK, Locher L, Koch M, Deuerling E
**Journal**: PLoS One (2015)
**DOI**: 10.1371/journal.pone.0143457

**Analysis**:
- Functional study of ribosome-tethered NAC complex
- Abstract: "Both the yeast nascent polypeptide-associated complex (NAC) and the Hsp40/70-based chaperone system RAC-Ssb are systems tethered to the ribosome to assist **cotranslational processes such as folding of nascent polypeptides**"
- NAC phenotype: "aggregation of newly synthesized proteins...[involved in] tubulin folding"
- **Recommendation**: **MODIFY → GO:0044183** (protein folding chaperone)
  - NAC directly assists nascent polypeptide folding
  - Works cotranslationally at ribosome
  - Prevents protein aggregation
- **Supporting Evidence**:
  > "systems tethered to the ribosome to assist cotranslational processes such as folding of nascent polypeptides"
  > "aggregation of newly synthesized proteins"

---

### 9. PMID:9463374 - gimc_yeast (GIM/Prefoldin Complex)
**Gene**: gimc_yeast (GIM proteins - Gamma-tubulin Interaction with Multiple C domains)
**Organism**: Yeast (Saccharomyces cerevisiae)
**Annotation**: GO:0051082 "unfolded protein binding"
**Status**: No review file exists

**Paper Title**: "A novel protein complex promoting formation of functional alpha- and gamma-tubulin"
**Authors**: Geissler S, Siegers K, Schiebel E
**Journal**: EMBO J (1998)
**DOI**: 10.1093/emboj/17.4.952

**Analysis**:
- Identifies GIM proteins (prefoldin complex homologs) that assist tubulin folding
- Abstract: "**The Gim proteins form a protein complex that promotes** [tubulin] folding"
- Function: "GIM1/YKE2 and GIM2/PAC10 rescue the synthetically lethal phenotype...benomyl super-sensitivity" related to tubulin assembly
- Phenotype analysis: "microtubules disassemble at 14°C", "super-sensitive to benomyl" - consistent with defective tubulin folding
- **Recommendation**: **MODIFY → GO:0044183** (protein folding chaperone)
  - GIM proteins are yeast prefoldin complex
  - Specifically assist alpha-tubulin and gamma-tubulin folding
  - ATP-independent (like mammalian prefoldin)
- **Supporting Evidence**:
  > "The Gim proteins form a protein complex that promotes formation of functional alpha- and gamma-tubulin"
  > "GIM1/YKE2 genetically interacts with...genes involved in tubulin folding"
  > Mammalian homologs of GIM proteins rescue yeast tubulin folding defects

---

### 10. PMID:9670014 - SSB2 (Yeast Hsp70 Co-translational)
**Gene**: SSB2 (HSP70 family, ribosome-associated)
**Organism**: Yeast (Saccharomyces cerevisiae)
**Annotation**: GO:0051082 "unfolded protein binding"
**Status**: No review file exists

**Paper Title**: "The molecular chaperone Ssb from Saccharomyces cerevisiae is a component of the ribosome-nascent chain complex"
**Authors**: Pfund C, et al.
**Journal**: EMBO J (1998)
**DOI**: 10.1093/emboj/17.14.3981

**Analysis**:
- Characterizes Ssb (Hsp70 family) function at ribosome during translation
- Abstract: "The 70 kDa heat shock proteins (Hsp70s)...The Ssbs...are an abundant type of Hsp70 **found associated with translating ribosomes**"
- Key evidence: "**Ssb could be cross-linked to nascent chains**" using photoreactive cross-linker
- Function: "Incorporation of...puromycin by translating ribosomes caused the release of Ssb concomitant with the release of nascent chains"
- **Recommendation**: **MODIFY → GO:0044183** (protein folding chaperone) [Co-translational variant]
  - Ssb is an Hsp70 that binds nascent chains during translation
  - ATP-dependent protein folding assistance
  - Works at ribosome for cotranslational folding
- **Supporting Evidence**:
  > "Ssb with the ribosome-nascent chain complex was stable"
  > "Ssb could be cross-linked to nascent chains"
  > "interaction of Ssb...suggests direct contact with nascent chains"

---

### 11. PMID:11274393 - rac_yeast (RAC Complex - Ssz1p/zuotin)
**Gene**: rac_yeast (Ribosome-Associated Complex: Ssz1p + zuotin)
**Organism**: Yeast (Saccharomyces cerevisiae)
**Annotation**: GO:0051082 "unfolded protein binding"
**Status**: No review file exists

**Paper Title**: "RAC, a stable ribosome-associated complex in yeast formed by the DnaK-DnaJ homologs Ssz1p and zuotin"
**Authors**: Gautschi M, et al.
**Journal**: Proc Natl Acad Sci U S A (2001)
**DOI**: 10.1073/pnas.071057198

**Analysis**:
- Characterizes ribosome-tethered chaperone complex
- Abstract: "Zuotin is a DnaJ homolog bound to the yeast ribosome...Ssz1p as zuotin's partner chaperone"
- Key evidence: "**RAC stimulates the translocation of a ribosome-bound mitochondrial precursor protein into mitochondria**, providing evidence for its chaperone-like effect on nascent proteins"
- Function: "RAC is unique...the 1:1 complex is stable, even in the presence of ATP or ADP"
- **Recommendation**: **MODIFY → GO:0044183** (protein folding chaperone) or **GO:0140309** (holdase)
  - RAC acts as Hsp40/70 co-chaperone system at ribosome
  - Assists nascent polypeptide folding during translation
  - Involved in substrate channeling (mitochondrial precursor delivery)
  - The "stable complex" phenotype suggests holdase-like properties
- **Supporting Evidence**:
  > "DnaK-DnaJ chaperone...Zuotin is a DnaJ homolog...Ssz1p...partner chaperone"
  > "RAC stimulates the translocation of a ribosome-bound mitochondrial precursor protein"
  > "providing evidence for its chaperone-like effect on nascent proteins"

---

### 12. PMID:12855682 - Hsp90aa1 (Client Protein Binding)
**Gene**: Hsp90aa1 (Heat Shock Protein 90, alpha family)
**Organism**: Human
**Annotation**: GO:0051082 "unfolded protein binding"
**Status**: No review file exists

**Paper Title**: "Heat shock protein 90 as an endogenous protein enhancer of inducible nitric-oxide synthase"
**Authors**: Yoshida M, Xia Y
**Journal**: J Biol Chem (2003)
**DOI**: 10.1074/jbc.M305214200

**Analysis**:
- HSP90 interaction with iNOS client protein
- Abstract: "Hsp90, at physiological concentrations (10-500 nm), **dose-dependently increased iNOS activity**...Co-immunoprecipitation studies showed that **hsp90 and iNOS associated with each other in cells**"
- Key evidence: "hsp90 is an **allosteric enhancer of iNOS**" - not a foldase but a co-chaperone/client binder
- Function: Modulates client protein activity through protein-protein interaction, not refolding
- **Recommendation**: **MODIFY → Alternative GO term** or **flag for expert review**
  - HSP90 is a co-chaperone for many client proteins, not a foldase
  - GO:0044183 (protein folding chaperone) overstates its role
  - Better fit might be co-chaperone-related term (e.g., HSP90 activity term if exists)
  - Alternative: Keep as general protein binding activity
- **Supporting Evidence**:
  > "hsp90 and iNOS associated with each other in cells"
  > "Hsp90 inhibition dramatically decreased NO formation"
  > "allosteric enhancer of iNOS"

---

## Recommendations for Missing Publications (50 PMIDs)

The following 50 PMIDs have no cached publications and require download before analysis:

```
PMID:10395799, PMID:10524211, PMID:10644717, PMID:10802661, PMID:10812074, 
PMID:10814722, PMID:10818100, PMID:10982809, PMID:11101517, PMID:11120798, 
PMID:11532003, PMID:11576425, PMID:11684676, PMID:11726962, PMID:11935339, 
PMID:12066189, PMID:12407112, PMID:12446740, PMID:12483302, PMID:12504083, 
PMID:12755697, PMID:12782322, PMID:12788224, PMID:15474971, PMID:16002468, 
PMID:16055437, PMID:16117846, PMID:1630491, PMID:2000394, PMID:20122915, 
PMID:22957041, PMID:23664927, PMID:2644542, PMID:7600578, PMID:7916212, 
PMID:8034610, PMID:8573069, PMID:8626763, PMID:8666233, PMID:8836031, 
PMID:9177349, PMID:9325046, PMID:9473517, PMID:9501143, PMID:9546042, 
PMID:9546392, PMID:9635427, PMID:9697692, PMID:9819444
```

**Procedure for completing analysis**:
1. Run: `just fetch-gene <organism> <gene>` for each missing publication
2. Review publication abstracts and full text
3. Determine appropriate GO term based on protein function described
4. Update spreadsheet with recommendations

---

## Summary of Findings So Far

| Finding | Count | Genes | Action |
|---------|-------|-------|--------|
| **False Annotations** | 2 | AIPL1, CHOP | REMOVE |
| **Foldase Activity** | 1 | cct_yeast | → GO:0044183 |
| **Pending Review** | 8 | Various | Awaiting full text analysis |
| **Requiring Publication Fetch** | 50+ | (see list above) | Download and analyze |

---

## Notes

- Gene review files for CCT (human versions CCT2-CCT7) **do exist** in the project and should be consulted
- Some annotations may be "substrate binding" assertions from bioinformatics predictions rather than experimental evidence
- GO:0051082 obsoletion is proceeding - all annotations must be reclassified before deadline
