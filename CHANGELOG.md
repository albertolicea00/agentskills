# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `dl-mtv` — download, organize, and manage video from HLS/M3U8 streams, direct MP4/AVI URLs, and full seasons from directory-style servers. Includes subtitle retrieval (subliminal/VLC), filename normalization for Plex/Jellyfin/Kodi, metadata scraping (TMDB/TVDB), and integrity verification.
- `commit-all` — groups the working tree into Conventional Commits with flag-based control; never pushes unless `--push` or an explicit instruction is given.
- Initial repository setup with base file structure.
- `timesheet-description-generator` — converts git commits, PRs, or informal task notes into tab-delimited timesheet log entries, consolidated into 1-4 blocks per day.
- Per-project context discovery for `timesheet-description-generator`: reads `.timesheet-context.md` from the consuming repo, with a fill-in template shipped under `references/`.
- `apple-design` — comprehensive Apple HIG reference (2025) with 12 on-demand reference files: app icons (all platform sizes + Icon Composer workflow), accessibility, typography, color, layout, Liquid Glass navigation, motion & haptics, inputs & gestures, components (lists/alerts/widgets/Live Activities), patterns (permissions/notifications/onboarding), SF Symbols 6, and platform-specific guidelines (iOS/iPadOS/macOS/watchOS/tvOS/visionOS).