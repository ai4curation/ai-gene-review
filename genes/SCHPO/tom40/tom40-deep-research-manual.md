# tom40 manual deep research

S. pombe tom40 (PomBase:SPBC27B12.13; UniProt O13656) encodes the conserved
Tom40 beta-barrel channel of the mitochondrial outer membrane TOM complex.
UniProt annotates it as a multi-pass mitochondrial outer membrane protein and
assigns it to the Tom40 family, and PomBase transfers the precise TOM-complex
component term from budding-yeast TOM40.

Dekker et al. dissected the budding-yeast TOM core and identified Tom40 as the
main component of the general import pore. The Tom40/Tom22/small-Tom GIP
complex forms the central outer membrane import machinery [PMID:9774667]. van
Wilpe et al. described Tom40 as the channel protein stably associated with the
central receptor Tom22 and showed that loss of Tom22 disrupts higher-order TOM
organization and channel gating, reinforcing that Tom40 is the conducting pore
whose activity is organized by receptor and small-Tom subunits [PMID:10519552].

Annotation decisions: `GO:0008320 protein transmembrane transporter activity` is
the core Tom40 molecular function and is accepted for both PAINT and InterPro
rows. The TOM complex and outer membrane component terms are accepted. Matrix,
IMS, TIM22, TIM23-SORT, and beta-barrel outer-membrane route rows are correct
but non-core because Tom40 is the general TOM pore used by all of them. Generic
`GO:0055085 transmembrane transport` and the ARBA mitochondrial membrane
organization row are over-broad.

GO-CAM consistency notes for 69729a3800007453: the model's tom40 activity uses
`GO:0008320 protein transmembrane transporter activity`, occurs in
`GO:0005741 mitochondrial outer membrane`, is part of the TOM complex, and is
part_of `GO:0030150`. That agrees with this review.
