from pathlib import Path
from src.cnnClassifier.utils.common import save_json

save_json(Path("test_scores.json"), {"test_loss": 0.5, "test_accuracy": 0.9})
