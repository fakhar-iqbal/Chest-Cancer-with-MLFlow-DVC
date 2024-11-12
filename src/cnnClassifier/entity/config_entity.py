from dataclasses import dataclass
from pathlib import Path

# we are making an entity for data ingestion which we will return later from other class
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    