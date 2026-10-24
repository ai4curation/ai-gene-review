"""Keep architecture and subunit errors distinct from pseudoenzyme assertions."""

from pathlib import Path

import pytest
import yaml
from ai_gene_review.datamodel.gene_review_model import PredictionErrorTypeEnum


@pytest.mark.parametrize(
    "value", ["DOMAIN_ARCHITECTURE_MISMATCH", "COMPLEX_ACTIVITY_TRANSFER"]
)
def test_prediction_error_types_round_trip(value: str) -> None:
    """Both the validation schema and generated runtime accept the diagnostic."""
    schema = yaml.safe_load(
        Path("src/ai_gene_review/schema/gene_review.yaml").read_text()
    )
    assert value in schema["enums"]["PredictionErrorTypeEnum"]["permissible_values"]
    assert PredictionErrorTypeEnum(value).value == value
