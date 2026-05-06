# SNIPE Gene Notes

## Key Paper: Saxton et al. (2026) Nature

**Title**: A membrane-bound nuclease directly cleaves phage DNA during genome injection
**Authors**: Saxton DS, DeWeirdt PC, Doering CR, Roney IJ & Laub MT
**DOI**: 10.1038/s41586-026-10207-1
**PMID**: 41741653

### Identification

- Originally identified as PD-lambda-1 in a functional genetic screen for anti-phage defence systems in the *E. coli* pangenome [PMID:36123438 "A functional selection reveals previously undetected anti-phage defence systems in the *E. coli* pangenome"]
- Renamed SNIPE: Surface-associated Nuclease Inhibiting Phage Entry [PMID:41741653 "we renamed this system surface-associated nuclease inhibiting phage entry (SNIPE)"]
- Found in wild *E. coli* strains (ECOR collection, strain MOD1-ECOR26); NOT present in K-12 MG1655
- UniProt: A0A8T9CRB7 (TrEMBL, ECOLX; from strain T0181B.E-10, same RefSeq WP_001606968.1)

### Protein Architecture (500 aa)

Three domains confirmed by AlphaFold, HHpred, and DeepTMHMM:

1. **N-terminal transmembrane domain** (aa 5-24): single-pass TM helix anchoring to inner membrane. N-terminus is periplasmic, rest of protein is cytoplasmic [PMID:41741653 "PhoA was functional only when inserted at the N terminus of SNIPE, and LacZalpha was functional only when inserted downstream of the transmembrane domain"]
2. **DUF4041 domain** (aa 144-262, now IPR025280/PF13250 "SNIPE associated domain"): positively charged surface facilitates DNA binding; also interacts with phage tape measure proteins (TMPs) [PMID:41741653 "the DUF4041 domain contains a positively charged surface that might facilitate DNA binding"]
3. **GIY-YIG nuclease domain** (aa 357-450): catalytic DNA endonuclease; E414 is catalytic residue [PMID:41741653 "Substituting a predicted catalytic residue in the nuclease domain (E414A) and deletion of the DUF4041 domain both abolished defence"]

### Mechanism of Action

SNIPE provides **direct defence** (infected cell survives), distinct from abortive infection:

- SNIPE pre-associates with ManYZ (mannose permease) in the inner membrane BEFORE infection [PMID:41741653 "SNIPE interacts with ManYZ independently of SNIPE... SNIPE interacts with ManYZ before and during lambda infection"]
- During phage genome injection through ManYZ, DUF4041 domain binds the phage tape measure protein (TMP), positioning the nuclease to cleave incoming DNA [PMID:41741653 "SNIPE associates with ManYZ before infection, positioning it to also associate with the TMP during infection, and DUF4041 binds to the TMP complex and phage DNA, positioning the nuclease domain to cleave the phage DNA"]
- 32P-labelled phage DNA is cleaved from ~42,000 bp down to <100 bp fragments during injection [PMID:41741653 "infection of SNIPE-containing cells yielded a smear of DNA fragment sizes ranging from more than 4,000 bp to less than 100 bp, as well as the band that probably corresponded to mononucleotides"]
- SNIPE does NOT affect phage adsorption [PMID:41741653 "SNIPE does not affect the adsorption of phage lambda"]
- SNIPE does NOT target pre-existing phage genomes (lysogens) [PMID:41741653 "SNIPE did not qualitatively affect the dynamics of CFP-ParB foci or cell lysis, nor did it affect the number of phage particles produced by prophage induction"]
- SNIPE does NOT block plasmid DNA transformation [PMID:41741653 "SNIPE did not block plasmid DNA transformation, indicating that its activity is specific to phage infection"]

### Auto-inhibition

- Membrane-localized SNIPE does NOT cleave host DNA [PMID:41741653 "SNIPE is not intrinsically toxic to cells"]
- SNIPE(deltaTM) localizes to nucleoid and IS toxic — cleaves host DNA [PMID:41741653 "SNIPE(deltaTM) no longer localized to the cell membrane and instead associated with bacterial DNA"]
- The TM domain prevents autoimmunity by anchoring SNIPE away from chromosomal DNA

### ManYZ Interaction

- ManYZ = mannose permease inner membrane complex, required for lambda genome injection
- SNIPE pre-associates with ManYZ (TurboID proximity labelling) [PMID:41741653 "ManX, SNIPE-GFP, and the lambda tape measure protein were enriched only in the TurboID-ManZ samples"]
- Robust defence requires ManYZ against lambda and related phages
- ManYZ-independent defence: SNIPE provides moderate defence against siphoviruses independently of ManYZ [PMID:41741653 "SNIPE offers broad defence against most siphoviruses independently of ManYZ"]

### TMP Interaction

- DUF4041 interacts with phage tape measure proteins physically [PMID:41741653 "The only phage protein recovered across both replicates was the tape measure protein"]
- UV crosslinking + mass spec confirms SNIPE-TMP direct contact via pBPA at residue N250 (adjacent to W257R mutation site) [PMID:41741653 "recovery of phage proteins... was dependent on the W257R I308V mutations"]
- SNIPE gain-of-function mutations (L253H, E264K, K305N; E223K, T319A; W257R, I308V) enhance binding to Bas14 TMP [PMID:41741653 "Each of these SNIPE mutants had at least two point mutations that mapped to the DUF4041 and the downstream alpha-helix"]
- Phage escape mutations map exclusively to TMP gene [PMID:41741653 "Strikingly, the only mutations found in escape phages mapped to the TMP"]

### Evolutionary Diversity

- ~500 curated SNIPE homologues across many bacterial phyla [PMID:41741653 "a set of around 500 homologues distributed across many bacterial phyla"]
- 33% of well-sequenced bacterial clades harbour at least one SNIPE homologue [PMID:36123438, PMID:41741653]
- GIY-YIG nuclease domain: most conserved region
- DUF4041: moderate conservation, positively charged DNA-binding interface conserved
- N-terminal region: highest variability — functions as adapter for phage specificity
  - 59% have 1 TM domain
  - 7% have 2 TM domains
  - 34% lack TM domains — use alternative membrane-targeting strategies:
    - DivIVA domains (negative membrane curvature binding)
    - Type III secretion system domains
    - Pleckstrin homology domains (phospholipid binding)
    - Phage tail protein fusions [PMID:41741653 "SNIPE homologues lacking predicted transmembrane domains frequently harbour domains from proteins such as DivIVA and type III secretion system ATPases"]

### Self/Non-Self Discrimination

SNIPE represents a novel strategy distinct from:
- **CRISPR-Cas**: sequence-specific recognition via guide RNAs
- **Restriction-modification**: recognition of DNA methylation marks
- **SNIPE**: exploits spatial organization — phage DNA must pass through the membrane during injection, and SNIPE is positioned there to intercept it [PMID:41741653 "SNIPE as a widespread bacterial defence system that exploits the spatial organization of phage genome injection to specifically target viral DNA, representing a previously unknown strategy for distinguishing self from non-self"]

### Comparison to Other Systems

- Zorya: also localizes to membrane at genome injection sites, but senses perturbations rather than directly cleaving DNA [PMID:41741653 ref 34,35]
- Kiwa: membrane-embedded defence supercomplex at phage attachment sites [PMID:41741653 ref 37]
- IFITM proteins (eukaryotic): block viral membrane fusion — conceptual parallel [PMID:41741653 ref 38,39]

### Key References

1. PMID:41741653 - Saxton et al. 2026, Nature. SNIPE characterization.
2. PMID:36123438 - Vassallo et al. 2022, Nat Microbiol. Original identification as PD-lambda-1.
3. PMID:37460672 - Georjon & Bernheim 2023, Cell Host Microbe. Systematic exploration of E. coli phage-host interactions (BASEL collection).
4. PMID:31857715 - Makarova et al. 2020. Classification of CRISPR-Cas systems.
5. PMID:36880887 - Branon et al. 2018, Nat Biotechnol. TurboID proximity labelling.
