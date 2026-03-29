"""
src/opensak/lang/da.py — Dansk sprogfil for OpenSAK.

Alle UI-strenge samlet ét sted.
Kopiér denne fil til en ny fil (fx en.py) og oversæt værdierne.
Nøglerne (venstre side) må ALDRIG ændres — de bruges i koden.
"""

STRINGS: dict[str, str] = {

    # ── Generelt ──────────────────────────────────────────────────────────────
    "app_name":                     "OpenSAK",
    "ok":                           "OK",
    "cancel":                       "Annuller",
    "close":                        "Luk",
    "yes":                          "Ja",
    "no":                           "Nej",
    "save":                         "Gem",
    "delete":                       "Slet",
    "add":                          "Tilføj",
    "edit":                         "Rediger",
    "error":                        "Fejl",
    "warning":                      "Advarsel",
    "info":                         "Information",
    "confirm":                      "Bekræft",
    "search":                       "Søg",
    "status_ready":                 "Klar",
    "restart_required":             "Genstart kræves",
    "restart_message":              "Sprog-ændringen træder i kraft ved næste opstart af OpenSAK.",

    # ── Hovedvindue — titellinje ──────────────────────────────────────────────
    "window_title":                 "OpenSAK",
    "window_title_with_db":         "OpenSAK — {db_name}",

    # ── Hurtigfilter-bar ──────────────────────────────────────────────────────
    "search_label":                 "Søg:",
    "search_placeholder":           "Navn eller GC kode…",
    "show_label":                   "Vis:",
    "quick_all":                    "Alle caches",
    "quick_not_found":              "Ikke fundne",
    "quick_found":                  "Fundne",
    "quick_available":              "Tilgængelige (ikke fundne)",
    "quick_traditional_easy":       "Traditional — let (D≤2, T≤2)",
    "quick_archived":               "Arkiverede",
    "count_caches":                 "{count} caches",
    "count_cache_single":           "1 cache",
    "filter_active_label":          "🔍 Filter aktivt",

    # ── Menulinje ─────────────────────────────────────────────────────────────
    "menu_file":                    "&Fil",
    "menu_waypoint":                "&Waypoint",
    "menu_view":                    "&Vis",
    "menu_tools":                   "F&unktioner",
    "menu_help":                    "&Hjælp",

    # Fil-menu
    "action_db_manager":            "&Administrer databaser…",
    "action_import":                "&Importer GPX / PQ zip…",
    "action_quit":                  "&Afslut",

    # Waypoint-menu
    "action_wp_add":                "&Tilføj cache…",
    "action_wp_edit":               "&Rediger cache…",
    "action_wp_delete":             "&Slet cache…",

    # Vis-menu
    "action_refresh":               "&Opdater liste",
    "action_filter":                "🔍  &Sæt filter…",
    "action_clear_filter":          "❌  &Nulstil filter",
    "action_columns":               "&Vælg kolonner…",

    # Funktioner-menu
    "action_settings":              "&Indstillinger…",
    "action_found_update":          "⟳  Opdater fund fra reference database…",
    "action_gps_export":            "📤  Send til GPS…",

    # Hjælp-menu
    "action_about":                 "Om &OpenSAK…",

    # ── Toolbar ───────────────────────────────────────────────────────────────
    "toolbar_import":               "Importer",
    "toolbar_filter":               "Filter",
    "toolbar_clear_filter":         "Nulstil filter",
    "toolbar_gps":                  "Send til GPS",
    "toolbar_refresh":              "Opdater",

    # ── Statusbar ─────────────────────────────────────────────────────────────
    "status_filter_reset":          "Filter nulstillet",
    "status_filter_result":         "Filter: {count} caches",
    "status_cache_added":           "Cache {gc_code} tilføjet",
    "status_cache_updated":         "Cache {gc_code} opdateret",
    "status_cache_deleted":         "Cache {gc_code} slettet",
    "status_db_name":               "Database: {db_name}",

    # ── Waypoint dialog ───────────────────────────────────────────────────────
    "wp_dialog_title_add":          "Tilføj cache",
    "wp_dialog_title_edit":         "Rediger cache",
    "wp_already_exists_title":      "Allerede eksisterer",
    "wp_already_exists_msg":        "{gc_code} findes allerede i databasen.",
    "wp_delete_title":              "Slet cache",
    "wp_delete_msg":                "Er du sikker på at du vil slette:\n{gc_code} — {name}?",

    # ── Import dialog ─────────────────────────────────────────────────────────
    "import_dialog_title":          "Importer GPX / PQ Zip",
    "import_drop_hint":             "Træk GPX eller ZIP filer hertil",
    "import_browse":                "Vælg filer…",
    "import_start":                 "Start import",
    "import_running":               "Importerer…",
    "import_done":                  "Import færdig: {count} caches importeret",
    "import_error":                 "Import fejlede: {error}",

    # ── Filter dialog ─────────────────────────────────────────────────────────
    "filter_dialog_title":          "Sæt filter",
    "filter_tab_general":           "Generelt",
    "filter_tab_dates":             "Datoer",
    "filter_tab_attributes":        "Attributter",
    "filter_apply":                 "Anvend filter",
    "filter_reset":                 "Nulstil",
    "filter_save_profile":          "Gem profil…",
    "filter_load_profile":          "Indlæs profil…",

    # ── GPS dialog ────────────────────────────────────────────────────────────
    "gps_dialog_title":             "Send til GPS",
    "gps_caches_ready":             "<b>{count} caches</b> klar til eksport (de aktuelt filtrerede/viste caches)",
    "gps_dest_group":               "Destination",
    "gps_rb_device":                "Send direkte til GPS enhed:",
    "gps_rb_file":                  "Gem som GPX fil:",
    "gps_scan_btn":                 "🔍 Scan",
    "gps_scan_scanning":            "⏳",
    "gps_devices_found":            "✓ {count} Garmin enhed(er) fundet",
    "gps_no_device":                "(Ingen GPS enhed fundet)",
    "gps_no_device_hint":           "Ingen Garmin enhed fundet — tilslut din GPS og klik Scan igen, eller brug 'Gem som GPX fil'",
    "gps_browse":                   "Vælg…",
    "gps_file_placeholder":         "Vælg placering…",
    "gps_opt_group":                "Indstillinger",
    "gps_filename_label":           "Filnavn:",
    "gps_max_label":                "Max antal caches:",
    "gps_max_all":                  "Alle",
    "gps_max_hint":                 "(0 = alle)",
    "gps_delete_cb":                "Slet eksisterende GPX filer på GPS inden upload",
    "gps_export_btn":               "📤  Send til GPS",
    "gps_exporting":                "Eksporterer {count} caches…",
    "gps_deleting":                 "🗑️  Sletter eksisterende GPX filer fra GPS enheden…",
    "gps_confirm_delete_title":     "Bekræft sletning",
    "gps_confirm_delete_msg":       "<b>{count} GPX fil(er)</b> vil blive slettet fra GPS enheden inden upload.\n\nEr du sikker?",
    "gps_confirm_no_files_msg":     "Ingen eksisterende GPX filer fundet på enheden.\nVil du fortsætte med upload?",
    "gps_delete_file_list":         "Filer der slettes:\n{files}",
    "gps_no_dest":                  "Vælg en destination først.",

    # ── Indstillinger dialog ──────────────────────────────────────────────────
    "settings_dialog_title":        "Indstillinger",
    "settings_group_location":      "Hjemkoordinat",
    "settings_lat_label":           "Breddegrad:",
    "settings_lon_label":           "Længdegrad:",
    "settings_group_display":       "Visning",
    "settings_use_miles":           "Vis afstande i miles (i stedet for km)",
    "settings_show_archived":       "Vis arkiverede caches",
    "settings_show_found":          "Vis fundne caches",
    "settings_map_label":           "Kortapp:",
    "settings_map_google":          "Google Maps",
    "settings_map_osm":             "OpenStreetMap",
    "settings_group_language":      "Sprog / Language",
    "settings_language_label":      "Sprog:",
    "settings_language_hint":       "Ændring træder i kraft ved næste opstart",

    # ── Database dialog ───────────────────────────────────────────────────────
    "db_dialog_title":              "Administrer databaser",
    "db_add":                       "Opret ny…",
    "db_open":                      "Åbn eksisterende…",
    "db_delete":                    "Slet",
    "db_activate":                  "Aktiver",
    "db_active_marker":             "(aktiv)",
    "db_delete_confirm_title":      "Slet database",
    "db_delete_confirm_msg":        "Er du sikker på at du vil slette databasen '{name}'?\nFilen slettes permanent.",
    "db_cannot_delete_active":      "Den aktive database kan ikke slettes.\nSkift til en anden database først.",

    # ── Fund-opdater dialog ───────────────────────────────────────────────────
    "found_dialog_title":           "Opdater fund fra reference database",
    "found_start":                  "Start opdatering",
    "found_running":                "Opdaterer…",
    "found_done":                   "{count} caches markeret som fundne",

    # ── Kolonne-vælger dialog ─────────────────────────────────────────────────
    "column_dialog_title":          "Vælg kolonner",
    "column_available":             "Tilgængelige kolonner",
    "column_visible":               "Viste kolonner",

    # ── Om dialog ─────────────────────────────────────────────────────────────
    "about_title":                  "Om OpenSAK",
    "about_text":
        "<h3>OpenSAK 0.1.0</h3>"
        "<p>Et open source geocaching-styringsværktøj "
        "til Linux og Windows.</p>"
        "<p>Bygget med Python og PySide6.</p>"
        "<p><a href='https://github.com/AgreeDK/opensak'>"
        "github.com/AgreeDK/opensak</a></p>",
}
