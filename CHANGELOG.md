# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial repository setup with base file structure.
- `timesheet-description-generator` — converts git commits, PRs, or informal task notes into tab-delimited timesheet log entries, consolidated into 1-4 blocks per day.
- Per-project context discovery for `timesheet-description-generator`: reads `.timesheet-context.md` from the consuming repo, with a fill-in template shipped under `references/`.