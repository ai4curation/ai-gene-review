# LPA literature and evidence notes

## Research provenance

- Falcon deep research was attempted but timed out after 600 seconds.
- Perplexity fallback returned HTTP 401 because quota was unavailable.
- Neither failure produced a provider deep-research artifact. This manual notes file records the evidence review instead.

## Protein product and allele boundaries

Human LPA encodes apo(a), the distinctive glycoprotein component of lipoprotein(a). The foundational cDNA paper describes a plasminogen-related architecture: "It contains a serine protease domain and two types of plasminogen-like kringle domains, one of which is present in 37 copies." [PMID:3670400] That 37-repeat clone is one allele, not a universal protein length. Direct mapping across alleles found that KIV types 3-10 are invariant in count while KIV-2 varies: "Our analysis demonstrates that the number of kringles IV 3-10 is invariable in the human apo(a) gene, suggesting that the 3'domain of Apo(a) is functionally important." [PMID:9524278] UniProt likewise states that individuals may encode 2-43 KIV-2 copies and that the P08519 reference allele contains 15 KIV-2 copies. Therefore all residue numbers and the 16 total KIV fragments in the cached P08519 record are reference-allele-specific.

## Protease-like domain: conflicting activity evidence

The original biochemical sequence analysis identified the decisive activation-site difference: "Plasminogen is activated by the cleavage of a specific arginine residue by urokinase and tissue plasminogen activator; however, the corresponding site in apo(a) is a serine that would not be cleaved by tissue plasminogen activator or urokinase." It also reported: "Using a plasmin-specific assay, no proteolytic activity could be demonstrated for lipoprotein(a) particles." [PMID:3472206]

The later recombinant study tested the issue more directly. Restoring arginine permitted tPA cleavage, but "both wildtype r-apo(a) and the mutant, either free or incorporated into r-Lp(a) particles, were uniformly inactive against a variety of chromogenic serine protease tripeptide substrates." The authors concluded that substitutions beyond the activation-site change render apo(a) inactive. [PMID:7495809]

In tension with those studies, the GOA source paper reports fibronectin fragmentation and says: "The proteolytic activity of Lp(a) was localized to apo(a) and experiments with inhibitors indicated that the proteolytic activity was of serine proteinase-type." [PMID:2531657] The cached record is abstract-only even though a PMCID is present, so purification, activation, inhibitor, and contamination controls cannot be reassessed here. This experimental annotation must receive curator deference rather than a claim of curator error, but the conflicting primary evidence and the activation-defective sequence make apo(a) serine endopeptidase/autoproteolytic activity disputed and unsuitable as an unqualified core function.

The local reproducible analysis independently maps an intact H1861/D1904/S1990 charge relay but a noncanonical S1819|I1820 activation junction. Its own limit is explicit: "This sequence result cannot establish absolute inactivity." [file:human/LPA/LPA-bioinformatics/RESULTS.md]

## Lp(a) particle assembly and APOB linkage

Recombinant particle experiments localized assembly to extracellular material and identified the covalent linkage: "Using site-directed mutagenesis, we demonstrated that Cys4057 in apo(a) is involved in disulfide linkage with apoB-100 in Lp(a) particles." [PMID:8366120] An independent HepG2 mutagenesis study found that Cys4057 substitutions yielded free apo(a) without detectable lipoprotein-associated apo(a), supporting an essential disulfide-mediated assembly step. [PMID:7505444] Historical residue number Cys4057 is allele-dependent; it denotes the homologous unpaired cysteine in apo(a), not residue 4057 of the shorter P08519 reference sequence.

## Kringle-mediated binding

The canonical strong lysine-binding site is in KIV-10, with weaker sites in other kringles. Direct recombinant-domain measurements found KIV-7 affinity for lysine analogues about tenfold weaker than KIV-10 (epsilon-aminocaproic acid Kd 230 +/- 42 versus 33 +/- 4 micromolar). [PMID:11802713] A natural Trp-to-Arg human variant in the historically numbered kringle 4-37 abolished lysine-Sepharose binding, independently tying this kringle site to Lp(a) lysine binding. [PMID:7918682]

The fibronectin paper directly states: "The binding of Lp(a) was localized to the C-terminal heparin-binding domain of fibronectin." [PMID:2531657] This supports fibronectin binding. It does **not** demonstrate that apo(a) itself binds free heparin; "heparin-binding domain" names the region of fibronectin. The GOA heparin-binding NAS annotation therefore lacks direct support in the cached source.

The KIV-2 yeast two-hybrid screen and coimmunoprecipitation study confirmed APOH interaction in human plasma and recombinant cell supernatants: "Coimmunoprecipitation experiments confirmed that beta-2 glycoprotein I and apo(a)/Lp(a) interact in human plasma and in cell culture supernatants of COS-1 cells, which ectopically expressed apo(a)." [PMID:9269765] This is a real interaction but does not by itself define the core function of apo(a).

## tPA/plasminogen interference

Surface context matters. One study explicitly reports failure to demonstrate direct tPA inhibition by Lp(a) in solution, but shows that surface-bound Lp(a) binds tPA and reduces plasminogen activation. [PMID:1829635] A later recombinant domain-dissection study found strong inhibition on native and degraded fibrin cofactors and showed that deleting the protease domain did not abolish inhibition: "A variant lacking the protease domain also exhibited strong inhibition, indicating that the apo(a)-plasminogen binding interaction mediated by the apo(a) protease domain does not ultimately inhibit plasminogen activation." [PMID:12697748] This supports a kringle/template-dependent, noncatalytic antifibrinolytic mechanism rather than direct catalytic protease inhibition.

The transgenic-mouse paper provides in vivo-context corroboration: "We show here that the activation of TGF-beta is inhibited in the aortic wall and serum of mice expressing apolipoprotein(a), as a consequence of apolipoprotein(a) inhibition of plasminogen activation." [PMID:8047165] It does not establish generic endopeptidase-inhibitor activity as a molecular function.

## Reference-access limitations

All newly fetched decisive primary papers are abstract-only in the local cache, including the PMC-indexed PMID:3472206 and PMID:7505444. Findings in the review use verbatim cached excerpts and set `full_text_unavailable: true`. PMID:2531657 remains especially important but disputed: the curator may have read assay detail not present in the cache, while independent primary experiments argue against a catalytically active apo(a) protease domain.
