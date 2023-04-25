import sys
import pandas as pd

if len(sys.argv) != 2:
    print('Usage: <path_to_csv_file>')
    sys.exit(1)

# Columns in csv
desired_columns = set([
    "FOD_ID", "FPA_ID", "SOURCE_SYSTEM_TYPE", "SOURCE_SYSTEM", "NWCG_REPORTING_AGENCY", "NWCG_REPORTING_UNIT_ID",
    "NWCG_REPORTING_UNIT_NAME", "SOURCE_REPORTING_UNIT", "SOURCE_REPORTING_UNIT_NAME", "LOCAL_FIRE_REPORT_ID",
    "LOCAL_INCIDENT_ID", "FIRE_CODE", "FIRE_NAME", "ICS_209_PLUS_INCIDENT_JOIN_ID", "ICS_209_PLUS_COMPLEX_JOIN_ID",
    "MTBS_ID", "MTBS_FIRE_NAME", "COMPLEX_NAME", "FIRE_YEAR", "DISCOVERY_DATE", "DISCOVERY_DOY", "DISCOVERY_TIME",
    "NWCG_CAUSE_CLASSIFICATION", "NWCG_GENERAL_CAUSE", "NWCG_CAUSE_AGE_CATEGORY", "CONT_DATE", "CONT_DOY", "CONT_TIME",
    "FIRE_SIZE", "FIRE_SIZE_CLASS", "LATITUDE", "LONGITUDE", "OWNER_DESCR", "STATE", "COUNTY", "FIPS_CODE", "FIPS_NAME",
    "LatLong_State", "LatLong_County", "NPL", "Mang_Type", "Mang_Name", "Des_Tp", "GAP_Sts", "GAP_Prity", "EVH", "EVT",
    "EVH_1km", "EVT_1km", "EVC", "EVC_1km", "NAME", "MOD_NDVI_12m", "MOD_EVI_12m", "Land_Cover", "Land_Cover_1km",
    "rpms", "rpms_1km", "Population", "Popo_1km", "GACCAbbrev", "GACC_PL", "GACC_New fire", "GACC_New LF",
    "GACC_Uncont LF", "GACC_Type 1 IMTs", "GACC_Type 2 IMTs", "GACC_NIMO Teams", "GACC_Area Command Teams",
    "GACC_Fire Use Teams", "GDP", "pr_Normal", "tmmn_Normal", "tmmx_Normal", "rmin_Normal", "rmax_Normal",
    "sph_Normal", "srad_Normal", "fm100_Normal", "fm1000_Normal", "bi_Normal", "vpd_Normal", "erc_Normal", "DF_PFS",
    "AF_PFS", "HDF_PFS", "DSF_PFS", "EBF_PFS", "EALR_PFS", "EBLR_PFS", "EPLR_PFS", "HBF_PFS", "LLEF_PFS", "LIF_PFS",
    "LMI_PFS", "MHVF_PFS", "PM25F_PFS", "HSEF", "P100_PFS", "P200_PFS", "LPF_PFS", "NPL_PFS", "RMP_PFS", "TSDF_PFS",
    "TPF", "TF_PFS", "UF_PFS", "WF_PFS", "M_WTR", "M_WKFC", "M_CLT", "M_ENY", "M_TRN", "M_HSG", "M_PLN", "M_HLTH",
    "SM_C", "SM_PFS", "EPLRLI", "EALRLI", "EBLRLI", "PM25LI", "EBLI", "DPMLI", "TPLI", "LPMHVLI", "HBLI", "RMPLI", "SFLI", "HWLI",
    "WDLI", "DLI", "ALI", "HDLI", "LLELI", "LILHSE", "PLHSE", "LMILHSE", "ULHSE", "EPL_ET", "EAL_ET", "EBL_ET", "EB_ET",
    "PM25_ET", "DS_ET", "TP_ET", "LPP_ET", "HB_ET", "RMP_ET", "NPL_ET", "TSDF_ET", "WD_ET", "DB_ET", "A_ET", "HD_ET",
    "LLE_ET", "UN_ET", "LISO_ET", "POV_ET", "LMI_ET", "IA_LMI_ET", "IA_UN_ET", "IA_POV_ET", "TC", "CC", "IAULHSE",
    "IAPLHSE", "IALMILHSE", "IALMIL_87", "IAPLHS_88", "IAULHS_89", "LHE", "IALHE", "IAHSEF", "CA", "NCA", "CA_LT20",
    "M_CLT_EOMI", "M_ENY_EOMI", "M_TRN_EOMI", "M_HSG_EOMI", "M_PLN_EOMI", "M_WTR_EOMI", "M_HLTH_102", "M_WKFC_103",
    "FPL200S", "M_WKFC_105", "M_EBSI", "UI_EXP", "THRHLD", "No_FireStation_1.0km", "No_FireStation_5.0km",
    "No_FireStation_10.0km", "No_FireStation_20.0km", "FRG_1km", "FRG", "TRI_1km", "TRI", "Aspect_1km", "Elevation_1km",
    "Elevation", "Slope_1km", "Aspect", "Slope", "GHM", "TPI", "TPI_1km", "TRACT", "RPL_THEMES", "RPL_THEME1", "EPL_POV",
    "EPL_UNEMP", "EPL_PCI", "EPL_NOHSDP", "RPL_THEME2", "EPL_AGE65", "EPL_AGE17", "EPL_DISABL", "EPL_SNGPNT",
    "RPL_THEME3", "EPL_MINRTY", "EPL_LIMENG", "RPL_THEME4", "EPL_MUNIT", "EPL_MOBILE", "EPL_CROWD", "EPL_NOVEH",
    "EPL_GROUPQ", "road_county_dis", "road_interstate_dis", "road_common_name_dis", "road_other_dis", "road_state_dis",
    "road_US_dis", "Ecoregion_US_L4CODE", "Ecoregion_US_L3CODE", "Ecoregion_NA_L3CODE", "Ecoregion_NA_L2CODE",
    "Ecoregion_NA_L1CODE", "SDI", "Annual_etr", "Annual_precipitation", "Annual_tempreture", "Aridity_index", "Evacuation", "pr", "tmmn", "tmmx",
    "rmin", "rmax", "sph", "vs", "th", "srad", "etr", "fm100", "fm1000", "bi", "vpd", "erc", "pr_5D_mean", "tmmn_5D_mean",
    "tmmx_5D_mean", "rmin_5D_mean", "rmax_5D_mean", "sph_5D_mean", "vs_5D_mean", "th_5D_mean", "srad_5D_mean",
    "etr_5D_mean", "fm100_5D_mean", "fm1000_5D_mean", "bi_5D_mean", "vpd_5D_mean", "erc_5D_mean", "pr_5D_min",
    "pr_5D_max", "tmmn_5D_max", "tmmx_5D_max", "rmin_5D_min", "rmax_5D_min", "sph_5D_min", "vs_5D_max", "th_5D_max",
    "srad_5D_max", "etr_5D_max", "fm100_5D_min", "fm1000_5D_min", "bi_5D_max", "vpd_5D_max", "erc_5D_max",
    "tmmn_Percentile", "tmmx_Percentile", "sph_Percentile", "vs_Percentile", "fm100_Percentile", "bi_Percentile",
    "vpd_Percentile", "erc_Percentile", "NDVI-1day", "NDVI_min", "NDVI_max", "NDVI_mean", "CheatGrass",
    "ExoticAnnualGrass", "Medusahead", "PoaSecunda", "Land_cover", "geometry", "Year"
])

# Get the path to the CSV file from the command line argument
csv_file_path = sys.argv[1]

# Read only the first row (header) of the CSV file to get column names
header = pd.read_csv(csv_file_path, nrows=0)
csv_columns = set(header.columns)

# Find the missing and extra columns
missing_columns = desired_columns - csv_columns
extra_columns = csv_columns - desired_columns

# Print the results
if not missing_columns and not extra_columns:
    print('The CSV file has the correct columns.')
else:
    if missing_columns:
        print('Missing columns:', ', '.join(missing_columns))
    if extra_columns:
        print('Extra columns:', ', '.join(extra_columns))







