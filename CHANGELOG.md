# Changelog

## [v0.2.0]

### Added

- Added `uv` as the primary package manager and build tool.
- Added GitHub Action for automated PyPI releases on tag push.
- Added `ruff` for extremely fast linting and formatting.

### Changed

- Migrated project configuration from `poetry` to standard `pyproject.toml` (PEP 621).
- Switched from `black` and `flake8` to `ruff` (configured to 88 line-length).
- Improved `_TwitchHandlerGrabber` robustness:
  - Renamed `_ffmpeg_thread` to `_ffmpeg_process` for clarity.
  - Improved subprocess lifecycle management with better cleanup in `terminate()` and `_reader()`.
  - Added safety checks to prevent `AttributeError` during early termination.
- Updated type hints to use `np.ndarray` instead of `np.array`.

### Fixed

- Fixed a bug where the reader thread could enter an infinite loop during termination.
- Fixed a typo in `ValueError` message in `twitchhandler.py`.
- Fixed various linting issues (B904, B018).
