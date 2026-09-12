# cnp1 (SpCENP-A / CENP-A homolog) — review notes

UniProt: Q9Y812 (CENPA_SCHPO); PomBase SPBC1105.17; synonym sim2. 120 aa, histone H3 family.

## Summary of function
Cnp1 is the fission-yeast CENP-A: the centromere-specific histone H3 variant that replaces canonical H3 in
centromeric (CENP-A) nucleosomes restricted to the central core/inner-repeat (cnt/imr) "central domain" of all
three centromeres. It epigenetically defines centromere identity, is the structural foundation of subkinetochore
chromatin, and is required for kinetochore assembly and accurate chromosome segregation.

## Key evidence

- Essential CENP-A function / kinetochore / segregation; localizes to nonrepetitive inner centromere; Mis6-dependent:
  [PMID:10864871 "the fission yeast homolog SpCENP-A is essential for establishing centromere chromatin associated with equal chromosome segregation. SpCENP-A binding to the nonrepetitious inner centromeres depended on Mis6"]
  UniProt FUNCTION (from PMID:10864871): "Required for recruitment and assembly of kinetochore proteins, mitotic progression and chromosome segregation. May serve as an epigenetic mark that propagates centromere identity"

- Restricted to central core (cnt/imr), not flanking repeats; domain structure:
  [PMID:11553715 "The centromere-associated proteins, Mis6p and Cnp1p (SpCENP-A), associate exclusively with central core DNA, whereas the Swi6 protein binds the surrounding repeats."]
  [PMID:11553715 "Cnp1 ( S. pombe CENP-A) and Mis6 proteins both bind to the central core region but not the flanking regions."]

- CENP-A nucleosome / replaces H3 / structural constituent; H3:H4 ratio plasticity:
  [PMID:17677001 "Within the central domain most histone H3 is replaced by the centromere-specific H3 variant CENP-ACnp1 to form the unusual chromatin that occupies most of the 10–12 kb comprising imr and cnt"]
  [PMID:17677001 "CENP-A is essential for the assembly of a functional kinetochore and as such must represent a key component in establishing and/or maintaining the site of kinetochore assembly at the centromere"]
  [PMID:17677001 "excess H3 interferes with the localization of CENP-ACnp1 at centromeres resulting in defective kinetochore function during mitosis"]

- CENP-A nucleosome composition (two H4 per particle, H3 absent from central domain):
  [PMID:26275423 "H3 nucleosomes are nearly absent from the central domain, which is occupied by centromere-specific H3 (cenH3 or CENP-A) nucleosomes with two H4s per particle"]
  [PMID:26275423 "Inner kinetochore proteins CENP-A, CENP-C, CENP-T, CENP-I, and Scm3 are highly enriched throughout the central domain"]

- Biphasic (S and G2) deposition, essential for kinetochore formation:
  [PMID:18077559 "CENP-A is a centromere-specific histone H3 variant that is essential for kinetochore formation."]
  [PMID:18077559 "CENP-A is normally localized to centromeres in S phase in an Ams2-dependent manner and that the G2 pathway may salvage CENP-A assembly to promote genome stability."]

- Scm3 is the CENP-A receptor/assembly factor (IPI with scm3/sim1 = SPAPB1A10.02):
  [PMID:19217404 "Scm3(Sp) coaffinity purifies with CENP-A(Cnp1) and associates with CENP-A(Cnp1) in vitro"]
  [PMID:19217404 "Scm3Sp acts to receive CENP-ACnp1 at centromeres and, in cooperation with Mis16 and Mis18, mediates its incorporation into nucleosomes in place of H3."]

- Sim3 (NASP) escort binds CENP-A NTD (IPI with sim3 = SPBC577.15c):
  [PMID:29194511 "identified the SpCENP-A-localizing chaperone Sim3 as a SpCENP-A NTD interacting protein"]

- Mis6 dependence (IPI WITH=SPAC1687.20c = mis6):
  [PMID:10864871 "SpCENP-A binding to the nonrepetitious inner centromeres depended on Mis6, an essential centromere connector protein"]

- Meiotic kinetochore - Cnp1 (Mis6-like group) remains at centromere throughout meiosis (condensed chromosome centromeric region IDA):
  [PMID:17035632 "Mis6-like group proteins remain at the centromere throughout meiosis ... Mis6-like group proteins constitute the structural basis of the centromere"]

- Centromere clustering at nuclear envelope; Cnp1 used as centromere marker (IDA chromatin/condensed chromosome):
  [PMID:23166349 "the centromeres of each chromosome are clustered together and attached to the nuclear envelope near the site of the spindle pole body during interphase"]

- Teb1 controls histone levels and centromeric Cnp1 incorporation (Cnp1 IDA chromatin):
  [PMID:23314747 "we examined localization of the centromeric histone H3 variant Cnp1 and found reduced centromeric binding along with reduced centromeric silencing"]

- Pcs1/Mde4 localize to central core (IPI WITH=Q9Y738; merotely prevention):
  [PMID:17627824 "Both Pcs1 and Mde4 localize to the central core of centromeres."]

- Mis12/Ppe1 kinetochore (IPI WITH=Q9Y738; PMID:12773390): Mis12 is independent of CENP-A pathway, but both reside in central centromere; physical interaction recorded by IntAct.
  [PMID:12773390 "In fission yeast, spCENP-A is located to central centromere regions in a Mis6-dependent manner"]

## Annotation review notes
- Core MF: structural constituent of chromatin (GO:0030527) — ACCEPT (IBA + IEA). This is the principal MF.
- nucleosomal DNA binding (GO:0031492) IBA — ACCEPT/keep non-core; centromeric DNA binding (GO:0019237 ISM) — keep as non-core (sequence non-specific; CENP-A deposition is sequence-independent per PMID:17677001). DNA binding (GO:0003677) IEA — general parent, MARK_AS_OVER_ANNOTATED / keep non-core.
- protein heterodimerization activity (GO:0046982) IEA InterPro — heterotetramer with H4 (CENP-A-H4), so heterodimerization is supported; keep non-core.
- protein binding (GO:0005515) bare — uninformative; MARK_AS_OVER_ANNOTATED across the IPI rows (mis6, sim3, scm3, Pcs1/Mde4/Mis12). Better captured by specific assembly/structural terms.
- CC: CENP-A containing nucleosome (GO:0043505), nucleosome (GO:0000786), CENP-A containing chromatin (GO:0061638), chromosome centromeric core domain (GO:0034506), chromosome centromeric region (GO:0000775), condensed chromosome centromeric region (GO:0000779), kinetochore (GO:0000776), chromatin (GO:0000785) — all ACCEPT (well supported). nucleus (GO:0005634) — broad but correct; keep non-core.
- BP: CENP-A containing chromatin assembly (GO:0034080) IMP — ACCEPT core. kinetochore assembly (GO:0051382) IBA — ACCEPT core. heterochromatin formation (GO:0031507) IBA — MARK_AS_OVER_ANNOTATED (Cnp1 occupies central core, NOT flanking heterochromatin; Swi6/Clr4 do heterochromatin). mitotic metaphase chromosome alignment (GO:0007080) IBA — KEEP_AS_NON_CORE (downstream consequence). chromatin organization (GO:0006325) IEA ARBA — general parent, KEEP_AS_NON_CORE.
