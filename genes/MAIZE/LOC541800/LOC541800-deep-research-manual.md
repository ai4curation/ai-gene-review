# LOC541800 (ZmYS1, Yellow stripe 1) -- manual literature synthesis

No deep-research API was available for this session; this synthesis was written by hand from
cached publications (publications/PMID_*.md) and PubMed metadata. All statements carry
inline provenance.

## Identity

- UniProtKB A0A1D6HET4 (TrEMBL, B73 RefGen_v5 model Zm00001eb249020_P001), 682 aa, NCBI GeneID
  541800. NCBI Gene names this locus "yellow stripe 1" with aliases ys1, zmYS1, GRMZM2G156599 and
  Zm00001d017429 (NCBI Gene esummary for 541800, retrieved 2026-10-28).
- The reviewed Swiss-Prot entry for the same gene is YS1_MAIZE (Q9AY27), 682 aa; the two
  sequences differ at 4 positions (cultivar/allelic differences; pairwise identity check in this
  session).
- The anti-ZmYS1 antibody of Ueno et al. 2009 was raised against peptide "DEMAALDDLQRDEI
  (positions 377-390 of ZmYS1)" [PMID:19549626]; this peptide occurs exactly at residues 377-390
  of A0A1D6HET4, confirming the identity of the reviewed entry with the experimentally studied
  protein.
- Family: OPT superfamily (TIGR00728, Pfam PF03169 OPT), YSL subfamily (IPR045035, TC 2.A.67.2);
  PANTHER PTHR31645:SF17 "IRON-PHYTOSIDEROPHORE TRANSPORTER YSL15". 13 predicted TM helices
  (Phobius) and a disordered N-terminal region (residues 1-36) (UniProt A0A1D6HET4 features).

## Molecular function: proton-coupled metal-chelate (phytosiderophore / nicotianamine) uptake

- Cloning of ys1: "Here we show that ys1 is a membrane protein that mediates iron uptake.
  Expression of YS1 in a yeast iron uptake mutant restores growth specifically on
  Fe(III)-phytosiderophore media." [PMID:11201743]
- Mechanism: "Electrophysiological analysis in oocytes demonstrated that Fephytosiderophore
  transport depends on proton cotransport and on the membrane potential" and "ZmYS1 encodes a
  proton-coupled broad-range metal-phytosiderophore transporter that additionally transports Fe-
  and Ni-nicotianamine" [PMID:14699112]. Substrates in oocytes included Zn-, Cu-, Ni-PS and, at
  lower rate, Mn- and Cd-PS [PMID:14699112].
- Roberts et al.: "YS1 is able to translocate iron that is bound either by PS or by the related
  compound, nicotianamine"; "Our data provide no support for the idea that YS1 is a transporter of
  zinc-PS"; "YS1 is capable of transporting copper-PS" [PMID:15107503]. So the zinc-PS activity is
  disputed between the two labs, whereas Fe(III)-PS and Fe-NA transport are agreed.
- Substrate specificity determinant: chimera work with barley HvYS1 showed "the outer membrane
  loop between the sixth and seventh transmembrane regions is essential for substrate
  specificity", ZmYS1 having broad specificity [PMID:17707820].
- Note: phytosiderophores (mugineic acids) and nicotianamine are non-proteinogenic amino acids,
  not oligopeptides. The InterPro2GO assignment of "oligopeptide transmembrane transporter
  activity" reflects the fungal OPT members of the superfamily, not the YSL clade.

## Localization

- Immunostaining with an anti-ZmYS1 antibody: in Fe-deficient maize "ZmYS1 was found to be
  localized at the epidermal cells of crown and lateral roots", with "polar localization at the
  distal side of the epidermal cells"; in leaves it "was detected on the peripheries of all
  mesophyll cells", the figure legend marking "ZmYS1 localization at the plasma membrane of the
  mesophyll cell" [PMID:19549626].

## Physiology and regulation

- ys1 mutant: "The maize yellow stripe1 (ys1) mutant is deficient in Fe(III)-phytosiderophore
  uptake" [PMID:11201743]; ys1 roots have low Fe and constitutively induced Fe-deficiency genes
  [PMID:23667491].
- Expression: "Under iron-deficient conditions, ys1 messenger RNA levels increase in both roots
  and shoots." [PMID:11201743]; "Ys1 expression at both the mRNA and protein levels responds
  rapidly to changes in iron availability but is not strongly affected by limitation of copper or
  zinc." [PMID:15107503]. ZmYS1 is expressed in leaf blades and sheaths, crown and seminal roots,
  higher in chlorotic young leaves, without a diurnal rhythm [PMID:19549626].
- Ueno et al. conclude "ZmYS1 is involved in both primary Fe acquisition and intracellular
  transport of iron and other metals in maize" [PMID:19549626].
- Applied: ZmYS1 expressed from the OsHMA2 promoter raised polished rice grain Fe up to 4.8-fold
  [PMID:35648686].

## Family context (for evaluating IBA rows)

- Arabidopsis YSL2 transports Fe- and Cu-NA and is plasma membrane-localized [PMID:15255869],
  although Schaaf et al. could not reproduce AtYSL2 transport [PMID:15753101].
- Arabidopsis ysl1 ysl3 double mutants have Fe-deficiency chlorosis, low seed Fe/Zn/Cu, and
  "reduced fertility due to defective anther and embryo development" [PMID:16815956]. This is the
  source of the PAINT "seed development" propagation; no seed-development data exist for ZmYS1.
- Maize has 18 YSL genes and a grass-specific clade [PMID:21831857].

## Open questions

- In vivo substrate range in maize (is Zn-PS uptake physiologically relevant?).
- Function of the shoot/mesophyll pool (Fe-NA or Fe-PS uptake into mesophyll cells?).
- Mechanism of the distal polar localization in root epidermis.
