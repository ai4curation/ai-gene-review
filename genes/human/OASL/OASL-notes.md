# OASL notes

OASL is the catalytic-loss paralog in human PTHR11258. The original cloning
paper showed p56 can bind dsRNA and DNA in vitro while being "devoid of
2'-5'OAS activity" [PMID:9826176]. PAINT already has an IRD at the mammalian
OASL clade for GO:0001730, and the OASL review accepts the curated NOT IDA row.

The core OASL mechanism is RIG-I enhancement, not 2-5A synthesis. The OAS-like
domain binds dsRNA, and mutations in that positively charged groove abolish
OASL enhancement of RIG-I signaling [PMID:25925578, "These results show that
OASL binds dsRNA through the positively charged groove and that dsRNA binding is
important for OASL to enhance RIG-I signaling."].

The InterPro IPR006116 -> `GO:0016779 nucleotidyltransferase activity` mapping is
right for catalytic OAS paralogs but over-propagates to human OASL. This review
therefore removes the IEA nucleotidyltransferase row and records an InterPro
source defect for that specific signature mapping.
