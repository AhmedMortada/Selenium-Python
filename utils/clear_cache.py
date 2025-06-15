import os
import shutil
from pathlib import Path

def clear_reports():
    """Clear the reports directory"""
    reports_dir = Path(__file__).parent.parent / 'reports'
    if reports_dir.exists():
        shutil.rmtree(reports_dir)
    reports_dir.mkdir(exist_ok=True)

def clear_logs():
    """Clear the logs directory"""
    logs_dir = Path(__file__).parent.parent / 'logs'
    if logs_dir.exists():
        shutil.rmtree(logs_dir)
    logs_dir.mkdir(exist_ok=True)

def clear_pytest_cache():
    """Clear pytest cache"""
    cache_dir = Path(__file__).parent.parent / '.pytest_cache'
    if cache_dir.exists():
        shutil.rmtree(cache_dir)

def clear_python_cache():
    """Clear Python cache files and directories"""
    project_root = Path(__file__).parent.parent
    
    # List of cache patterns to remove
    cache_patterns = [
        '**/__pycache__',
        '**/*.pyc',
        '**/*.pyo',
        '**/*.pyd',
        '.coverage',
        'htmlcov',
        '.mypy_cache',
        '.ruff_cache',
        '.hypothesis'
    ]
    
    for pattern in cache_patterns:
        for cache_path in project_root.glob(pattern):
            if cache_path.is_file():
                cache_path.unlink()
            elif cache_path.is_dir():
                shutil.rmtree(cache_path)

def clear_all():
    """Clear all cache directories and files"""
    clear_reports()
    clear_logs()
    clear_pytest_cache()
    clear_python_cache()

if __name__ == "__main__":
    clear_all() 