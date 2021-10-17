from pathlib import Path
import pytest
import utils.directories as dirs

def test_project_root():
    dir = dirs.project_root()
    assert isinstance(dir, Path)
    assert str(dir).endswith('Health-Monitor')

def test_join_dir():
    dir = dirs.join_dir('directory')
    assert isinstance(dir, Path)
    assert str(dir).endswith('directory')

def test_sqlite_dir():
    dir = dirs.sqlite_dir()
    assert isinstance(dir, Path)
    assert str(dir).endswith('sqlite')

def test_utils_dir():
    dir = dirs.utils_dir()
    assert isinstance(dir, Path)
    assert str(dir).endswith('utils')

def test_sqlqueries_dir():
    dir = dirs.sqlqueries_dir()
    assert isinstance(dir, Path)
    assert str(dir).endswith('sql_queries')