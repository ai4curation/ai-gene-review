# E. coli ssuD: manual source-based review

SsuD is the FMNH2-dependent alkanesulfonate monooxygenase of Escherichia coli. It uses reduced flavin and molecular oxygen to cleave diverse aliphatic sulfonates into the corresponding aldehydes and sulfite, supplying sulfur for assimilation during sulfate or cysteine limitation. SsuD forms a homotetramer and interacts with the flavin reductase SsuE; the efficiency of reduced-flavin transfer depends on protein interactions and assay conditions. Loss of ssuD also compromises heat-shock survival in a native deletion screen, a contextual role distinct from its established desulfonation chemistry.

## Evidence and decisions

- Row 1, GO:0005515 (IPI; PMID:16997955): **MODIFY**. PMID:16997955 directly detects pair-specific coelution, cross-linking and fluorescence changes between the purified catalytic partners. Enzyme binding is a supported informative descendant of bare protein binding. PMID:26634408 further connects the interface to efficient flavin transfer but permits diffusion under specified conditions; binding is not equated with an obligatory permanent channel.
- Row 2, GO:0008726 (IBA; GO_REF:0000033): **ACCEPT**. Purified target SsuD converts pentanesulfonate to aldehyde and sulfite, requires reduced FMN and oxygen, and accepts multiple aliphatic substrates (PMID:10480865). This independently grounds the PAINT node PTN000768559; the target in its descendant evidence is expected, not circular. Retain the specific catalytic claim across experimental and inferred rows.
- Row 3, GO:0008726 (IDA; PMID:10480865): **ACCEPT**. Purified target SsuD converts pentanesulfonate to aldehyde and sulfite, requires reduced FMN and oxygen, and accepts multiple aliphatic substrates (PMID:10480865). This independently grounds the PAINT node PTN000768559; the target in its descendant evidence is expected, not circular. Retain the specific catalytic claim across experimental and inferred rows.
- Row 4, GO:0008726 (IEA; GO_REF:0000120): **ACCEPT**. Purified target SsuD converts pentanesulfonate to aldehyde and sulfite, requires reduced FMN and oxygen, and accepts multiple aliphatic substrates (PMID:10480865). This independently grounds the PAINT node PTN000768559; the target in its descendant evidence is expected, not circular. Retain the specific catalytic claim across experimental and inferred rows.
- Row 5, GO:0009408 (IMP; PMID:24580753): **KEEP_AS_NON_CORE**. Full PMID:24580753 Figure 5A explicitly includes ssuD: its deletion reduces heat survival, with complementation restoring survival near wild type while the oxidative/osmotic controls differ. The figure was inspected directly and retained in source-analysis. This supports a contextual heat-response annotation, not a new heat-protection catalytic mechanism or the core purpose of sulfonate oxidation.
- Row 6, GO:0010438 (NAS; PMID:10480865): **ACCEPT**. PMID:10480865 directly connects sulfur-limited expression with the characterized flavin-reduction/desulfonation activities. SsuD executes the reaction that releases sulfite from alternative sulfur sources, providing more than expression-only evidence.
- Row 7, GO:0016705 (IEA; GO_REF:0000002): **MODIFY**. Purified target SsuD converts pentanesulfonate to aldehyde and sulfite, requires reduced FMN and oxygen, and accepts multiple aliphatic substrates (PMID:10480865). This independently grounds the PAINT node PTN000768559; the target in its descendant evidence is expected, not circular. Refine the broad oxidoreductase class to the exact monooxygenase activity already represented.
- Row 8, GO:0042802 (IDA; PMID:10480865): **ACCEPT**. PMID:10480865 reports native homotetrameric SsuD, and the independent structure PMID:12445781 resolves intersubunit contacts. These support self-association, assembly and complex membership; the complex term is not interpreted as a fixed SsuD–SsuE heteromeric stoichiometry.
- Row 9, GO:0046306 (IBA; GO_REF:0000033): **ACCEPT**. The purified-enzyme products directly establish catabolic participation, corroborating the native operon phenotype and PAINT propagation. The annotation is about substrate breakdown, not carbon-source mineralization or downstream sulfite assimilation.
- Row 10, GO:0046306 (IDA; PMID:10480865): **ACCEPT**. The purified-enzyme products directly establish catabolic participation, corroborating the native operon phenotype and PAINT propagation. The annotation is about substrate breakdown, not carbon-source mineralization or downstream sulfite assimilation.
- Row 11, GO:0046306 (IMP; PMID:10506196): **ACCEPT**. The purified-enzyme products directly establish catabolic participation, corroborating the native operon phenotype and PAINT propagation. The annotation is about substrate breakdown, not carbon-source mineralization or downstream sulfite assimilation.
- Row 12, GO:0051289 (IDA; PMID:10480865): **ACCEPT**. PMID:10480865 reports native homotetrameric SsuD, and the independent structure PMID:12445781 resolves intersubunit contacts. These support self-association, assembly and complex membership; the complex term is not interpreted as a fixed SsuD–SsuE heteromeric stoichiometry.
- Row 13, GO:1990201 (IDA; PMID:10480865): **ACCEPT**. PMID:10480865 reports native homotetrameric SsuD, and the independent structure PMID:12445781 resolves intersubunit contacts. These support self-association, assembly and complex membership; the complex term is not interpreted as a fixed SsuD–SsuE heteromeric stoichiometry.
- Row 14, GO:1990201 (IPI; PMID:12445781): **ACCEPT**. PMID:10480865 reports native homotetrameric SsuD, and the independent structure PMID:12445781 resolves intersubunit contacts. These support self-association, assembly and complex membership; the complex term is not interpreted as a fixed SsuD–SsuE heteromeric stoichiometry.

## Acquisition and provenance

All original ordered annotation payloads and both raw files are retained. No NEW annotations were proposed. The genuine Falcon and perplexity-lite attempts failed authentication; actual FEBA attempts returned no usable mapped data (foundation job logs). These failures are not evidence about function. Publication caches were read as retrieved, never hand-edited. Primary abstracts are distinguished from normally recovered full PMC URL text. No GOA assertion or protein name is cited as biological support. Ordinary relationship fields were not used to reject a complex contribution.

PMID:24580753 Figure 5A was downloaded from the public PMC image link and inspected directly; ssuD is an explicit plotted mutant with heat sensitivity and complemented rescue. See ssuD-source-analysis/README.md and the unmodified image. This is retained as a non-core phenotype, not promoted into a catalytic mechanism. PMID:26634408 explicitly permits reduced-flavin diffusion under specified experimental conditions, qualifying the stronger exclusionary wording in the 2006 interaction paper.

## Source findings

- [PMID:10480865] SsuD directly oxygenolyzes alkanesulfonates using FMNH2. “The pure enzyme catalyzed the conversion of pentanesulfonic acid
to sulfite and pentaldehyde and was able to desulfonate a wide range of
sulfonated substrates including C-2 to C-10 unsubstituted linear
alkanesulfonates, substituted ethanesulfonic acids and sulfonated buffers.”
- [PMID:10480865] SsuD directly oxygenolyzes alkanesulfonates using FMNH2. “SsuD
catalysis was absolutely dependent on FMNH(2) and oxygen,”
- [PMID:12445781] SsuD forms the homotetrameric monooxygenase assembly. “The X-ray crystal
structure of SsuD shows a homotetrameric state for the enzyme, each subunit
being composed of a TIM-barrel fold enlarged by four insertion regions that
contribute to intersubunit interactions.”
- [PMID:16997955] SsuD and SsuE form a specific enzyme–enzyme interaction. “The results showed that His-tagged SsuD and native SsuE coeluted from the column with 300 mM imidazole buffer (Fig. 2 , lane 4).”
- [PMID:24580753] SsuD contributes to survival after heat shock in a native deletion screen. “For both thermotolerance and osmotic stress resistance, expressing the deleted genes from a plasmid reversed the phenotype of all mutants; average survival was 93.3% and 91.7% of the wild type for the 23 and 6 complemented mutants, respectively (compared with average 37.4% and 67.4% for the deletion mutants) (Figure 5A, B).”
- [PMID:26634408] SsuD and SsuE form a specific enzyme–enzyme interaction. “The results from these studies suggest that optimal transfer of reduced flavin
from SsuE to SsuD requires defined protein-protein interactions, but diffusion
can occur under specified conditions.”

### PR 5593 source-audit follow-up (2026-10-26)

Re-inspected the committed Figure 5A image. Neighbor labels are clpS, oppA and tig; the ssuD bar position and heat-survival/complementation interpretation are unchanged. Added the corrected figure-analysis trace to the non-core heat-response support. All original annotation payloads, actions and source-cache bytes are preserved.
