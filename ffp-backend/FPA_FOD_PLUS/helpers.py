

def categoryHelper(*categories):
    rtVal = []
    for c in categories:
        for f in fields(c):
            rtVal.append(f)
    return rtVal

def fields(category):
    rtVal = []
    if category=='FPA_FOD' :
        rtVal.append('FOD_ID')
        rtVal.append('FPA_ID')
        rtVal.append('SOURCE_SYSTEM_TYPE')
        rtVal.append('SOURCE_SYSTEM')
        rtVal.append('NWCG_REPORTING_AGENCY')
        rtVal.append('NWCG_REPORTING_UNIT_ID')
        rtVal.append('SOURCE_REPORTING_UNIT')
        rtVal.append('SOURCE_REPORTING_UNIT_NAME')
        rtVal.append('LOCAL_FIRE_REPORT_ID')
        rtVal.append('LOCAL_INCEDENT_ID')
        rtVal.append('FIRE_CODE')
        rtVal.append('FIRE_NAME')
        rtVal.append('ICS_209_PLUS_INCIDENT_JOIN_ID')
        rtVal.append('ICS_209_PLUS_COMPLEX_JOIN_ID')
        rtVal.append('MTBS_ID')
        rtVal.append('MTBS_FIRE_NAME')
        rtVal.append('COMPLEX_NAME')
        rtVal.append('FIRE_YEAR')
        rtVal.append('DISCOVERY_DATE')
        rtVal.append('DISCOVERY_DOY')
        rtVal.append('DISCOVERY_TIME')
        rtVal.append('NWCG_CAUSE_CLASSIFICATION')
        rtVal.append('NWCG_GENERAL_CAUSE')
        rtVal.append('NWCG_CAUSE_AGE_CATEGORY')
        rtVal.append('CONT_DATE')
        rtVal.append('CONT_DOY')
        rtVal.append('CONT_TIME')
        rtVal.append('FIRE_SIZE')
        rtVal.append('FIRE_SIZE_CLASS')
        rtVal.append('LATITUDE')
        rtVal.append('LONGITUDE')
        rtVal.append('OWNER_DESCR')
        rtVal.append('STATE')
        rtVal.append('COUNTY')
        rtVal.append('FIPS_CODE')
        rtVal.append('FIPS_NAME')
        rtVal.append('Year')
    elif category=='CLimate and Economic Justice Screening Tool' :
        rtVal.append('DF_PFS')
        rtVal.append('AF_PFS')
        rtVal.append('HDF_PFS')
        rtVal.append('DSF_PFS')
        rtVal.append('EBF_PFS')
        rtVal.append('EALR_PFS')
        rtVal.append('EBLR_PFS')
        rtVal.append('EPLR_PFS')
        rtVal.append('HBF_PFS')
        rtVal.append('LLEF_PFS')
        rtVal.append('LIF_PFS')
        rtVal.append('LMI_PFS')
        rtVal.append('MHVF_PFS')
        rtVal.append('PM25F_PFS')
        rtVal.append('HSEF')
        rtVal.append('P100_PFS')
        rtVal.append('P200_PFS')
        rtVal.append('LPF_PFS')
        rtVal.append('NPL_PFS')
        rtVal.append('RMP_PFS')
        rtVal.append('TSDF_PFS')
        rtVal.append('TPF')
        rtVal.append('TF_PFS')
        rtVal.append('UF_PFS')
        rtVal.append('WF_PFS')
        rtVal.append('M_WTR')
        rtVal.append('M_WKFC')
        rtVal.append('M_CLT')
        rtVal.append('M_ENY')
        rtVal.append('M_TRN')
        rtVal.append('M_HSG')
        rtVal.append('M_PLN')
        rtVal.append('M_HLTH')
        rtVal.append('SM_C')
        rtVal.append('SM_PFS')
        rtVal.append('EPLRLI')
        rtVal.append('EALRLI')
        rtVal.append('EBLRLI')
        rtVal.append('PM25LI')
        rtVal.append('EBLI')
        rtVal.append('DPMLI')
        rtVal.append('TPLI')
        rtVal.append('LPMHVLI')
        rtVal.append('HBLI')
        rtVal.append('RMPLI')
        rtVal.append('SFLI')
        rtVal.append('HWLI')
        rtVal.append('WDLI')
        rtVal.append('DLI')
        rtVal.append('ALI')
        rtVal.append('HDLI')
        rtVal.append('LLELI')
        rtVal.append('LILHSE')
        rtVal.append('PLHSE')
        rtVal.append('LMILHSE')
        rtVal.append('ULHSE')
        rtVal.append('EPL_ET')
        rtVal.append('EAL_ET')
        rtVal.append('EBL_ET')
        rtVal.append('EB_ET')
        rtVal.append('PM25_ET')
        rtVal.append('DS_ET')
        rtVal.append('TP_ET')
        rtVal.append('LPP_ET')
        rtVal.append('HB_ET')
        rtVal.append('RMP_ET')
        rtVal.append('NPL_ET')
        rtVal.append('TSDF_ET')
        rtVal.append('WD_ET')
        rtVal.append('DB_ET')
        rtVal.append('A_ET')
        rtVal.append('HD_ET')
        rtVal.append('LLE_ET')
        rtVal.append('UN_ET')
        rtVal.append('LISO_ET')
        rtVal.append('POV_ET')
        rtVal.append('LMI_ET')
        rtVal.append('IA_LMI_ET')
        rtVal.append('IA_UN_ET')
        rtVal.append('IA_POV_ET')
        rtVal.append('TC')
        rtVal.append('CC')
        rtVal.append('IAULHSE')
        rtVal.append('IAPLHSE')
        rtVal.append('IALMILHSE')
        rtVal.append('IALMIL_87')
        rtVal.append('IAPLHS_88')
        rtVal.append('IAULHS_89')
        rtVal.append('LHE')
        rtVal.append('IALHE')
        rtVal.append('IAHSEF')
        rtVal.append('CA')
        rtVal.append('NCA')
        rtVal.append('CA_LT20')
        rtVal.append('M_CLT_EOMI')
        rtVal.append('M_ENY_EOMI')
        rtVal.append('M_TRN_EOMI')
        rtVal.append('M_HSG_EOMI')
        rtVal.append('M_PLN_EOMI')
        rtVal.append('M_WTR_EOMI')
        rtVal.append('M_HLTH_102')
        rtVal.append('M_WKFC_103')
        rtVal.append('FPL200S')
        rtVal.append('M_WKFC_105')
        rtVal.append('M_EBSI')
        rtVal.append('UI_EXP')
        rtVal.append('THRHLD')
    elif category=='Annual Climate' :
        rtVal.append('Annual_etr')
        rtVal.append('Annual_precipitation')
        rtVal.append('Annual_tempreture')
        rtVal.append('Aridity_index')
    elif category=='Cheat Grass' :
        rtVal.append('CheatGrass')
        rtVal.append('ExoticAnnualGrass')
        rtVal.append('Medusahead')
        rtVal.append('PoaSecunda')
    elif category=='Climate Normals' :
        rtVal.append('pr_Normal')
        rtVal.append('tmmn_Normal')
        rtVal.append('tmmx_Normal')
        rtVal.append('rmin_Normal')
        rtVal.append('rmax_Normal')
        rtVal.append('sph_Normal')
        rtVal.append('srad_Normal')
        rtVal.append('fm100_Normal')
        rtVal.append('fm1000_Normal')
        rtVal.append('bi_Normal')
        rtVal.append('vpd_Normal')
        rtVal.append('erc_Normal')
    elif category=='GRIDMENT' :
        rtVal.append()
    elif category=='Climate Percentiles' :
        rtVal.append()
    elif category=='Ecoregions' :
        rtVal.append()
    elif category=='Digital Elevation Map' :
        rtVal.append()
    elif category=='Vegetation' :
        rtVal.append()
    elif category=='Risk Management Assistance' :
        rtVal.append()
    elif category=='Fire Regime Groups' :
        rtVal.append()
    elif category=='Fire Stations' :
        rtVal.append()
    elif category=='Geographic Area Coordination Centers' :
        rtVal.append()
    elif category=='Gap Analysis Project' :
        rtVal.append()
    elif category=='Gross Domestic Product' :
        rtVal.append()
    elif category=='Global Human Modification' :
        rtVal.append()
    elif category=='MODIS NDVI' :
        rtVal.append()
    elif category=='NOAA NDVI' :
        rtVal.append()
    elif category=='National Land Cover Database' :
        rtVal.append()
    elif category=='National Preparedness Level' :
        rtVal.append()
    elif category=='Population' :
        rtVal.append()
    elif category=='Pyrome' :
        rtVal.append()
    elif category=='Road' :
        rtVal.append()
    elif category=='Social Vulnerability Index' :
        rtVal.append()
    elif category=='Rangeland Production Monitoring Service' :
        rtVal.append()
    return rtVal
pr
tmmn
tmmx
rmin
rmax
sph
vs
th
srad
etr
fm100
fm1000
bi
vpd
erc
pr_5D_mean
tmmn_5D_mean
tmmx_5D_mean
rmin_5D_mean
rmax_5D_mean
sph_5D_mean
vs_5D_mean
th_5D_mean
srad_5D_mean
etr_5D_mean
fm100_5D_mean
fm1000_5D_mean
bi_5D_mean
vpd_5D_mean
erc_5D_mean
pr_5D_min
pr_5D_max
tmmn_5D_max
tmmx_5D_max
rmin_5D_min
rmax_5D_min
sph_5D_min
vs_5D_max
th_5D_max
srad_5D_max
etr_5D_max
fm100_5D_min
fm1000_5D_min
bi_5D_max
vpd_5D_max
erc_5D_max
tmmn_Percentile
tmmx_Percentile
sph_Percentile
vs_Percentile
fm100_Percentile
bi_Percentile
vpd_Percentile
erc_Percentile
Ecoregion_US_L4CODE
Ecoregion_US_L3CODE
Ecoregion_NA_L3CODE
Ecoregion_NA_L2CODE
Ecoregion_NA_L1CODE
Elevation
Aspect
Slope
TPI
TRI
Elevation_1km
Aspect_1km
Slope_1km
TPI_1km
TRI_1km
EVC
EVC_1km
EVH
EVH_1km
EVT
EVT_1km
Evacuation
SDI
FRG
FRG_1km
No_FireStation_1.0km
No_FireStation_5.0km
No_FireStation_10.0km
No_FireStation_20.0km
GACCAbbrev
GACC_PL
GACC_New fire
GACC_New LF
GACC_Uncont LF
GACC_Type 1 IMTs
GACC_Type 2 IMTs
GACC_NIMO Teams
GACC_Area Command Teams
GACC_Fire Use Teams
Mang_Type
Mang_Name
Des_Tp
GAP_Sts
GAP_Prity
GDP
GHM
MOD_NDVI_12m
MOD_EVI_12m
NDVI_min
NDVI_max
NDVI_mean
NDVI-1day
Land_cover
Land_Cover_1km
NPL
Population
Popo_1km
NAME
road_county_dis
road_interstate_dis
road_common_name_dis
road_other_dis
road_state_dis
road_US_dis
RPL_THEMES
RPL_THEME1
EPL_POV
EPL_UNEMP
EPL_PCI
EPL_NOHSDP
RPL_THEME2
EPL_AGE65
EPL_AGE17
EPL_DISABL
EPL_SNGPNT
RPL_THEME3
EPL_MINRTY
EPL_LIMENG
RPL_THEME4
EPL_MUNIT
EPL_MOBILE
EPL_CROWD
EPL_NOVEH
EPL_GROUPQ
rpms
rpms_1km