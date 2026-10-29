# AS1 (ASYMMETRIC LEAVES1, MYB91, At2g37630; UniProt O80931) - manual literature synthesis

No deep-research API was available for this review; this synthesis was written by the
reviewer from the cached publications in `publications/` and the UniProt record
(`AS1-uniprot.txt`). Every claim carries its provenance.

## Identity and domain architecture

- AS1 is a 367-aa R2R3-type MYB-domain protein, the Arabidopsis ortholog of Antirrhinum
  PHANTASTICA and maize ROUGH SHEATH2 [PMID:11882937 "The AS1 gene encodes a MYB-domain
  protein that is homologous to the Antirrhinum PHANTASTICA ( PHAN) and maize ROUGH SHEATH2
  ( RS2) genes"]. UniProt annotates two HTH myb-type domains (residues 1-53 and 54-108;
  PROSITE PS51294, Pfam PF13921) and places AS1 in PANTHER PTHR47214 (PROTEIN ROUGH SHEATH 2
  HOMOLOG), subfamily SF3 (TRANSCRIPTION FACTOR AS1).
- The MYB domain is diverged: "several of the amino acids in the third helix of the R3 MYB
  motif that are critical for MYB-DNA interaction are not conserved in AS1, and attempts to
  demonstrate binding of this protein to DNA in vitro have thus far been unsuccessful"
  [PMID:18203921].
- A conserved C-terminal domain mediates homodimerization [PMID:12750468 "A conserved
  C-terminal domain (CTD) mediates homodimerization of both RS2 and AS1"].

## Molecular function: DNA-binding repressor acting with AS2

- AS1 and the LOB-domain protein AS2 (LBD6) form a repressor complex that binds two sites
  (motifs CWGTTD and KMKTTGAHW) in the BP/KNAT1 and KNAT2 promoters; ChIP shows in vivo
  occupancy [PMID:18203921 "AS1 and AS2 form a repressor complex that binds directly to the
  regulatory motifs CWGTTD and KMKTTGAHW"].
- AS1 alone and AS2 alone do not bind in EMSA; only co-translated AS1+AS2 bind
  [PMID:18203921 "When translated separately, neither AS1 nor AS2 was able to bind fragment X
  in vitro"; "when AS1 and AS2 were cotranslated, these proteins were able to bind as a
  complex to site X of the BP promoter"]. DNA binding is therefore a property of the
  heterodimer, to which AS1 contributes.
- AS1 interacts with HDA6 and with HIRA; HDA6 and AS1 both occupy KNAT1, KNAT2 and KNATM
  chromatin, and KNOX loci are hyperacetylated in hda6 [PMID:23271976 "Chromatin
  immunoprecipitation assays revealed that HDA6 and AS1 bound directly to KNAT1, KNAT2, and
  KNATM chromatin"; PMID:16243907 "RS2/AS1 can form conserved protein complexes through
  interaction with the DNA binding factor ASYMMETRIC LEAVES2, a predicted RNA binding protein
  (RIK, for RS2-Interacting KH protein), and a homologue of the chromatin-remodeling protein
  HIRA"].
- AS1 also acts as an activator in at least one context: it complexes with CONSTANS and binds
  the FT promoter in vivo; as1 mutants have reduced FT and delayed flowering
  [PMID:21950734 "Moreover, AS1 bound directly to the specific regions of the FT promoter in
  vivo."].
- AS1 binds promoters of jasmonate-responsive genes and dampens necrotroph defense
  [PMID:18003921 "AS1 operates as a negative regulator of inducible resistance against these
  pathogens by selectively binding to the promoters of genes controlled by the immune
  activator, jasmonic acid (JA), damping the defense response"].
- High-throughput yeast one-hybrid screens recorded AS1 binding to promoters of
  glucosinolate, secondary-cell-wall, nitrogen-metabolism and vascular genes
  (PMID:25352272, PMID:25533953, PMID:30356219, PMID:31806676); these are unvalidated for AS1.

## Localization

- Nuclear [PMID:23271976, BiFC "HDA6 interacted with AS1 in the nucleus of as2-1 mutants"].
- YFP-AS1 alone is predominantly nucleolar; with AS2 the two co-localize in nucleolus and
  nucleoplasm; AS1 associates with condensed metaphase chromosomes [PMID:18713400 "AS1 and AS2
  alone were predominantly localized in the nucleolus and the nucleoplasm, respectively";
  "AS1 alone was able to associate with the condensed chromosome in the metaphase cell"].
  AS1/AS2 co-localize in subnuclear bodies adjacent to the nucleolus [PMID:17293570].

## Biological roles

- Represses class I KNOX genes (BP/KNAT1, KNAT2, KNAT6, KNATM) in leaf primordia, separating
  organ founder cells from stem cells [PMID:11140682 "AS1 negatively regulates the homeobox
  genes KNAT1 and KNAT2"; PMID:11076771 "AS1 and AS2 promote leaf differentiation through
  repression of knox expression in leaves"].
- Leaf adaxial-abaxial polarity, with AS2, ERECTA, HDACs and the nucleolar RH10 helicase,
  through repression of abaxial genes ETT/ARF3 and ARF4 [PMID:12874130; PMID:17293570;
  PMID:27334696 "the epigenetic repressor complex of ASYMMETRIC-LEAVES1 (AS1) and AS2 (AS1-AS2)
  is critical to repress abaxial (ventral) genes ETT/ARF3 and ARF4"].
- Leaf morphogenesis/proximodistal patterning and leaf initiation in combination with auxin
  [PMID:11882937; PMID:16971475 "auxin and AS1 pathways converge to repress expression of the
  KNOX gene BREVIPEDICELLUS (BP) and thus promote leaf fate"].
- Fruit mediolateral patterning as a lateral factor repressing BP [PMID:23133401 "ASYMMETRIC
  LEAVES1 (AS1), previously shown to repress BP both in leaves and ovaries, collaborates with
  JAG/FIL activity"].
- Pathogen responses independent of AS2: negative regulator of JA-dependent resistance to
  necrotrophic fungi, positive regulator of SA-independent defense to bacteria [PMID:18003921].
- Target of the geminivirus betaC1 pathogenicity factor [PMID:18794352 "betaC1 binds directly
  to AS1, elicits morphological and gene expression changes dependent on AS1 but not AS2"].
