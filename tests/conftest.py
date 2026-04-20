"""
Shared pytest fixtures for RDD projects.
"""
import sys
from pathlib import Path

import pytest

# Ensure src/ is importable
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))


@pytest.fixture
def project_root():
    """Provide the project root path."""
    return PROJECT_ROOT


@pytest.fixture
def requirements_dir():
    """Provide the requirements directory path."""
    req_dir = PROJECT_ROOT / "docs" / "requirements"
    if not req_dir.exists():
        req_dir = PROJECT_ROOT / "文档" / "需求"
    return req_dir


@pytest.fixture
def src_dir():
    """Provide the source directory path."""
    return PROJECT_ROOT / "src"
