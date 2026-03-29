"""
src/opensak/lang/en.py — English language file for OpenSAK.

All UI strings in one place.
To add a new language: copy this file, rename it (e.g. de.py), translate the values.
Keys (left side) must NEVER be changed — they are used in the code.
"""

STRINGS: dict[str, str] = {

    # ── General ───────────────────────────────────────────────────────────────
    "app_name":                     "OpenSAK",
    "ok":                           "OK",
    "cancel":                       "Cancel",
    "close":                        "Close",
    "yes":                          "Yes",
    "no":                           "No",
    "save":                         "Save",
    "delete":                       "Delete",
    "add":                          "Add",
    "edit":                         "Edit",
    "error":                        "Error",
    "warning":                      "Warning",
    "info":                         "Information",
    "confirm":                      "Confirm",
    "search":                       "Search",
    "status_ready":                 "Ready",
    "restart_required":             "Restart required",
    "restart_message":              "The language change will take effect the next time OpenSAK is started.",

    # ── Main window — title bar ───────────────────────────────────────────────
    "window_title":                 "OpenSAK",
    "window_title_with_db":         "OpenSAK — {db_name}",

    # ── Quick filter bar ──────────────────────────────────────────────────────
    "search_label":                 "Search:",
    "search_placeholder":           "Name or GC code…",
    "show_label":                   "Show:",
    "quick_all":                    "All caches",
    "quick_not_found":              "Not found",
    "quick_found":                  "Found",
    "quick_available":              "Available (not found)",
    "quick_traditional_easy":       "Traditional — easy (D≤2, T≤2)",
    "quick_archived":               "Archived",
    "count_caches":                 "{count} caches",
    "count_cache_single":           "1 cache",
    "filter_active_label":          "🔍 Filter active",

    # ── Menu bar ──────────────────────────────────────────────────────────────
    "menu_file":                    "&File",
    "menu_waypoint":                "&Waypoint",
    "menu_view":                    "&View",
    "menu_tools":                   "&Tools",
    "menu_help":                    "&Help",

    # File menu
    "action_db_manager":            "&Manage databases…",
    "action_import":                "&Import GPX / PQ zip…",
    "action_quit":                  "&Quit",

    # Waypoint menu
    "action_wp_add":                "&Add cache…",
    "action_wp_edit":               "&Edit cache…",
    "action_wp_delete":             "&Delete cache…",

    # View menu
    "action_refresh":               "&Refresh list",
    "action_filter":                "🔍  &Set filter…",
    "action_clear_filter":          "❌  &Clear filter",
    "action_columns":               "&Choose columns…",

    # Tools menu
    "action_settings":              "&Settings…",
    "action_found_update":          "⟳  Update finds from reference database…",
    "action_gps_export":            "📤  Send to GPS…",

    # Help menu
    "action_about":                 "About &OpenSAK…",

    # ── Toolbar ───────────────────────────────────────────────────────────────
    "toolbar_import":               "Import",
    "toolbar_filter":               "Filter",
    "toolbar_clear_filter":         "Clear filter",
    "toolbar_gps":                  "Send to GPS",
    "toolbar_refresh":              "Refresh",

    # ── Status bar ────────────────────────────────────────────────────────────
    "status_filter_reset":          "Filter cleared",
    "status_filter_result":         "Filter: {count} caches",
    "status_cache_added":           "Cache {gc_code} added",
    "status_cache_updated":         "Cache {gc_code} updated",
    "status_cache_deleted":         "Cache {gc_code} deleted",
    "status_db_name":               "Database: {db_name}",

    # ── Waypoint dialog ───────────────────────────────────────────────────────
    "wp_dialog_title_add":          "Add cache",
    "wp_dialog_title_edit":         "Edit cache",
    "wp_already_exists_title":      "Already exists",
    "wp_already_exists_msg":        "{gc_code} already exists in the database.",
    "wp_delete_title":              "Delete cache",
    "wp_delete_msg":                "Are you sure you want to delete:\n{gc_code} — {name}?",

    # ── Import dialog ─────────────────────────────────────────────────────────
    "import_dialog_title":          "Import GPX / PQ Zip",
    "import_drop_hint":             "Drag GPX or ZIP files here",
    "import_browse":                "Browse…",
    "import_start":                 "Start import",
    "import_running":               "Importing…",
    "import_done":                  "Import complete: {count} caches imported",
    "import_error":                 "Import failed: {error}",

    # ── Filter dialog ─────────────────────────────────────────────────────────
    "filter_dialog_title":          "Set filter",
    "filter_tab_general":           "General",
    "filter_tab_dates":             "Dates",
    "filter_tab_attributes":        "Attributes",
    "filter_apply":                 "Apply filter",
    "filter_reset":                 "Reset",
    "filter_save_profile":          "Save profile…",
    "filter_load_profile":          "Load profile…",

    # ── GPS dialog ────────────────────────────────────────────────────────────
    "gps_dialog_title":             "Send to GPS",
    "gps_caches_ready":             "<b>{count} caches</b> ready for export (currently filtered/visible caches)",
    "gps_dest_group":               "Destination",
    "gps_rb_device":                "Send directly to GPS device:",
    "gps_rb_file":                  "Save as GPX file:",
    "gps_scan_btn":                 "🔍 Scan",
    "gps_scan_scanning":            "⏳",
    "gps_devices_found":            "✓ {count} Garmin device(s) found",
    "gps_no_device":                "(No GPS device found)",
    "gps_no_device_hint":           "No Garmin device found — connect your GPS and click Scan again, or use 'Save as GPX file'",
    "gps_browse":                   "Browse…",
    "gps_file_placeholder":         "Choose location…",
    "gps_opt_group":                "Options",
    "gps_filename_label":           "Filename:",
    "gps_max_label":                "Max caches:",
    "gps_max_all":                  "All",
    "gps_max_hint":                 "(0 = all)",
    "gps_delete_cb":                "Delete existing GPX files on GPS before upload",
    "gps_export_btn":               "📤  Send to GPS",
    "gps_exporting":                "Exporting {count} caches…",
    "gps_deleting":                 "🗑️  Deleting existing GPX files from GPS device…",
    "gps_confirm_delete_title":     "Confirm deletion",
    "gps_confirm_delete_msg":       "<b>{count} GPX file(s)</b> will be deleted from the GPS device before upload.\n\nAre you sure?",
    "gps_confirm_no_files_msg":     "No existing GPX files found on the device.\nDo you want to continue with the upload?",
    "gps_delete_file_list":         "Files to be deleted:\n{files}",
    "gps_no_dest":                  "Please select a destination first.",

    # ── Settings dialog ───────────────────────────────────────────────────────
    "settings_dialog_title":        "Settings",
    "settings_group_location":      "Home coordinates",
    "settings_lat_label":           "Latitude:",
    "settings_lon_label":           "Longitude:",
    "settings_group_display":       "Display",
    "settings_use_miles":           "Show distances in miles (instead of km)",
    "settings_show_archived":       "Show archived caches",
    "settings_show_found":          "Show found caches",
    "settings_map_label":           "Map app:",
    "settings_map_google":          "Google Maps",
    "settings_map_osm":             "OpenStreetMap",
    "settings_group_language":      "Language",
    "settings_language_label":      "Language:",
    "settings_language_hint":       "Change takes effect on next restart",

    # ── Database dialog ───────────────────────────────────────────────────────
    "db_dialog_title":              "Manage databases",
    "db_add":                       "Create new…",
    "db_open":                      "Open existing…",
    "db_delete":                    "Delete",
    "db_activate":                  "Activate",
    "db_active_marker":             "(active)",
    "db_delete_confirm_title":      "Delete database",
    "db_delete_confirm_msg":        "Are you sure you want to delete the database '{name}'?\nThe file will be permanently deleted.",
    "db_cannot_delete_active":      "The active database cannot be deleted.\nSwitch to another database first.",

    # ── Found updater dialog ──────────────────────────────────────────────────
    "found_dialog_title":           "Update finds from reference database",
    "found_start":                  "Start update",
    "found_running":                "Updating…",
    "found_done":                   "{count} caches marked as found",

    # ── Column chooser dialog ─────────────────────────────────────────────────
    "column_dialog_title":          "Choose columns",
    "column_available":             "Available columns",
    "column_visible":               "Visible columns",

    # ── About dialog ──────────────────────────────────────────────────────────
    "about_title":                  "About OpenSAK",
    "about_text":
        "<h3>OpenSAK 0.1.0</h3>"
        "<p>An open source geocaching management tool "
        "for Linux and Windows.</p>"
        "<p>Built with Python and PySide6.</p>"
        "<p><a href='https://github.com/AgreeDK/opensak'>"
        "github.com/AgreeDK/opensak</a></p>",
}
