"""Test GOA data sorting with IBA prioritization."""

from unittest.mock import Mock, patch


from ai_gene_review.etl.gene import fetch_goa_data


def test_goa_sorting_iba_first():
    """Test that IBA annotations are sorted first, then by date, then by GO ID."""

    # Mock response with various evidence codes and dates
    mock_data = {
        "results": [
            {
                "geneProductId": "UniProtKB:TEST",
                "symbol": "TEST",
                "goId": "GO:0005515",
                "goName": "protein binding",
                "goEvidence": "IPI",
                "date": "20200101",
                "goAspect": "F",
                "evidenceCode": "ECO:0000353",
                "reference": "PMID:12345",
                "assignedBy": "UniProt",
                "taxonId": 9606,
                "taxonName": "Homo sapiens",
                "name": "Test protein",
            },
            {
                "geneProductId": "UniProtKB:TEST",
                "symbol": "TEST",
                "goId": "GO:0005737",
                "goName": "cytoplasm",
                "goEvidence": "IBA",  # IBA should come first
                "date": "20190101",  # Even though it's older
                "goAspect": "C",
                "evidenceCode": "ECO:0000318",
                "reference": "GO_REF:0000033",
                "assignedBy": "GO_Central",
                "taxonId": 9606,
                "taxonName": "Homo sapiens",
                "name": "Test protein",
            },
            {
                "geneProductId": "UniProtKB:TEST",
                "symbol": "TEST",
                "goId": "GO:0005634",
                "goName": "nucleus",
                "goEvidence": "IDA",
                "date": "20210101",  # Most recent non-IBA
                "goAspect": "C",
                "evidenceCode": "ECO:0000314",
                "reference": "PMID:67890",
                "assignedBy": "UniProt",
                "taxonId": 9606,
                "taxonName": "Homo sapiens",
                "name": "Test protein",
            },
            {
                "geneProductId": "UniProtKB:TEST",
                "symbol": "TEST",
                "goId": "GO:0003677",
                "goName": "DNA binding",
                "goEvidence": "IBA",  # Another IBA
                "date": "20220101",  # More recent IBA
                "goAspect": "F",
                "evidenceCode": "ECO:0000318",
                "reference": "GO_REF:0000033",
                "assignedBy": "GO_Central",
                "taxonId": 9606,
                "taxonName": "Homo sapiens",
                "name": "Test protein",
            },
            {
                "geneProductId": "UniProtKB:TEST",
                "symbol": "TEST",
                "goId": "GO:0000001",  # Lower GO ID
                "goName": "test function",
                "goEvidence": "IEA",
                "date": "20210101",  # Same date as nucleus
                "goAspect": "F",
                "evidenceCode": "ECO:0000501",
                "reference": "InterPro:IPR000001",
                "assignedBy": "InterPro",
                "taxonId": 9606,
                "taxonName": "Homo sapiens",
                "name": "Test protein",
            },
        ]
    }

    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Fetch and parse the TSV result
        tsv_result = fetch_goa_data("TEST")
        lines = tsv_result.strip().split("\n")

        # Skip header
        data_lines = lines[1:]

        # Extract GO IDs and evidence codes
        annotations = []
        for line in data_lines:
            parts = line.split("\t")
            go_id = parts[4]  # GO TERM column
            evidence = parts[8]  # GO EVIDENCE CODE column
            date = parts[15]  # DATE column
            annotations.append((go_id, evidence, date))

        # Check ordering
        assert len(annotations) == 5

        # First two should be IBA (more recent IBA first)
        assert annotations[0] == ("GO:0003677", "IBA", "20220101")  # More recent IBA
        assert annotations[1] == ("GO:0005737", "IBA", "20190101")  # Older IBA

        # Then non-IBA by date (most recent first)
        assert annotations[2] == (
            "GO:0000001",
            "IEA",
            "20210101",
        )  # Same date as next, lower GO ID
        assert annotations[3] == (
            "GO:0005634",
            "IDA",
            "20210101",
        )  # Same date, higher GO ID
        assert annotations[4] == ("GO:0005515", "IPI", "20200101")  # Oldest non-IBA


def test_goa_sorting_no_iba():
    """Test sorting when there are no IBA annotations."""

    mock_data = {
        "results": [
            {
                "geneProductId": "UniProtKB:TEST",
                "symbol": "TEST",
                "goId": "GO:0005515",
                "goName": "protein binding",
                "goEvidence": "IPI",
                "date": "20200101",
                "goAspect": "F",
                "evidenceCode": "ECO:0000353",
                "reference": "PMID:12345",
                "assignedBy": "UniProt",
                "taxonId": 9606,
                "taxonName": "Homo sapiens",
                "name": "Test protein",
            },
            {
                "geneProductId": "UniProtKB:TEST",
                "symbol": "TEST",
                "goId": "GO:0005737",
                "goName": "cytoplasm",
                "goEvidence": "IDA",
                "date": "20210101",  # More recent
                "goAspect": "C",
                "evidenceCode": "ECO:0000314",
                "reference": "PMID:67890",
                "assignedBy": "UniProt",
                "taxonId": 9606,
                "taxonName": "Homo sapiens",
                "name": "Test protein",
            },
        ]
    }

    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        tsv_result = fetch_goa_data("TEST")
        lines = tsv_result.strip().split("\n")
        data_lines = lines[1:]

        annotations = []
        for line in data_lines:
            parts = line.split("\t")
            go_id = parts[4]
            date = parts[15]
            annotations.append((go_id, date))

        # Should be sorted by date (most recent first)
        assert annotations[0] == ("GO:0005737", "20210101")  # More recent
        assert annotations[1] == ("GO:0005515", "20200101")  # Older


def test_goa_deduplicates_identical_projected_rows():
    """Annotation extensions must not create duplicate rows in the TSV projection."""

    base_result = {
        "geneProductId": "UniProtKB:TEST",
        "symbol": "TEST",
        "goId": "GO:0034506",
        "goName": "chromosome, centromeric core domain",
        "goEvidence": "IDA",
        "date": "20091201",
        "goAspect": "C",
        "evidenceCode": "ECO:0000314",
        "reference": "PMID:19217403",
        "assignedBy": "PomBase",
        "taxonId": 4896,
        "taxonName": "Schizosaccharomyces pombe",
        "name": "Centromere protein Scm3",
    }
    mock_data = {
        "results": [
            {
                **base_result,
                "id": "annotation-1",
                "extensions": [
                    {
                        "relation": "existence_overlaps",
                        "connectedXrefs": [{"db": "GO", "id": "0000088"}],
                    }
                ],
            },
            {
                **base_result,
                "id": "annotation-2",
                "extensions": [
                    {
                        "relation": "existence_overlaps",
                        "connectedXrefs": [{"db": "GO", "id": "0000093"}],
                    }
                ],
            },
            {
                **base_result,
                "id": "annotation-3",
                "withFrom": [
                    {"connectedXrefs": [{"db": "PomBase", "id": "SPAC25G10.01"}]}
                ],
            },
        ],
        "numberOfHits": 3,
    }

    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        data_lines = fetch_goa_data("TEST").strip().split("\n")[1:]

    assert len(data_lines) == 2
    assert {line.split("\t")[10] for line in data_lines} == {
        "",
        "PomBase:SPAC25G10.01",
    }
