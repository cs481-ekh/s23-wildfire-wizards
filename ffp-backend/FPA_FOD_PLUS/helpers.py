

def categoryHelper(categories):
    rtVal = []
    for c in categories:
        for f in fields(c):
            rtVal.append(f)
    if len(categories)==0:
        for f in defaultFields():
            rtVal.append(f)
    return rtVal

def defaultFields():
    rtVal = ["FOD_ID", "FPA_ID", "FIRE_NAME", "FIRE_SIZE", "DISCOVERY_DATE", 
    "LATITUDE", "LONGITUDE", "NWCG_CAUSE_CLASSIFICATION"]
    rtVal.reverse()
    return rtVal

def addAllCategories():
    rtVal = ["FPA_FOD", "Climate and Economic Justice Screening Tool", 
    "Annual Climate", "Cheat Grass", "Climate Normals", "GRIDMET", 
    "Climate Percentiles", "Ecoregions", "Topography", "Vegetation",
    "Risk Management Assistance", "Fire Regime Groups", "Fire Stations", 
    "Geographic Area Coordination Centers", "Gap Analysis Project", 
    "Gross Domestic Product", "Global Human Modification", "MODIS NDVI", 
    "NOAA NDVI", "National Land Cover Database", "Population", "Pyrome", "Road", 
    "Social Vulnerability Index", "Rangeland Production Monitoring Service"]
    return rtVal

def postalToState(s):
    rtVal = ''
    if s=='AK':
        rtVal='Alaska'
    elif s=='AL':
        rtVal='Alabama'
    elif s=='AR':
        rtVal='Arkansas'
    elif s=='AZ':
        rtVal='Arizona'
    elif s=='CA': 
        rtVal='California'
    elif s=='CO': 
        rtVal='Colorado'
    elif s=='CT': 
        rtVal='Connecticut'
    elif s=='DC': 
        rtVal='District of Columbia'
    elif s=='DE':
        rtVal='Deleware'
    elif s=='FL':
        rtVal='Florida'
    elif s=='GA':
        rtVal='Georgia'
    elif s=='HI':
        rtVal='Hawaii'
    elif s=='IA':
        rtVal='Iowa'
    elif s=='ID':
        rtVal='Idaho'
    elif s=='IL':
        rtVal='Illinois'
    elif s=='IN':
        rtVal='Indiana'
    elif s=='KS':
        rtVal='Kansas'
    elif s=='KY':
        rtVal='Kentucky'
    elif s=='LA':
        rtVal='Louisiana'
    elif s=='MA':
        rtVal='Massachusetts'
    elif s=='MD':
        rtVal='Maryland'
    elif s=='ME':
        rtVal='Maine'
    elif s=='MI':
        rtVal='Michigan'
    elif s=='MN':
        rtVal='Minnesota'
    elif s=='MO':
        rtVal='Missouri'
    elif s=='MS':
        rtVal='Mississippi'
    elif s=='MT':
        rtVal='Montana'
    elif s=='NC':
        rtVal='North Carolina'
    elif s=='ND':
        rtVal='North Dakota'
    elif s=='NE':
        rtVal='Nebraska'
    elif s=='NH':
        rtVal='New Hampshire'
    elif s=='NJ':
        rtVal='New Jersey'
    elif s=='NM':
        rtVal='New Mexico'
    elif s=='NV':
        rtVal='Nevada'
    elif s=='NY':
        rtVal='New York'
    elif s=='OH':
        rtVal='Ohio'
    elif s=='OK': 
        rtVal='Oklahoma'
    elif s=='OR': 
        rtVal='Oregon'
    elif s=='PA': 
        rtVal='Pennsylvania'
    elif s=='PR': 
        rtVal='Puerto Rico'
    elif s=='RI': 
        rtVal='Rhode Island'
    elif s=='SC': 
        rtVal='South Carolina'
    elif s=='SD': 
        rtVal='South Dakota'
    elif s=='TN': 
        rtVal='Tennessee'
    elif s=='TX': 
        rtVal='Texas'
    elif s=='UT': 
        rtVal='Utah'
    elif s=='VA': 
        rtVal='Virginia'
    elif s=='VT':
        rtVal='Vermont'
    elif s=='WA': 
        rtVal='Washington'
    elif s=='WI': 
        rtVal='Wisconsin'
    elif s=='WV': 
        rtVal='West Virginia'
    elif s=='WY':
        rtVal='Wyoming'
    return rtVal

def stateList():
    rtVal = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 
    'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 
    'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 
    'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 
    'VT','WA', 'WI', 'WV', 'WY']
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
        rtVal.append('LOCAL_INCIDENT_ID')
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
        #rtVal.append('Year')
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
    elif category=='GRIDMET' :
        rtVal.append('pr')
        rtVal.append('tmmn')
        rtVal.append('tmmx')
        rtVal.append('rmin')
        rtVal.append('rmax')
        rtVal.append('sph')
        rtVal.append('vs')
        rtVal.append('th')
        rtVal.append('srad')
        rtVal.append('etr')
        rtVal.append('fm100')
        rtVal.append('fm1000')
        rtVal.append('bi')
        rtVal.append('vpd')
        rtVal.append('erc')
        rtVal.append('pr_5D_mean')
        rtVal.append('tmmn_5D_mean')
        rtVal.append('tmmx_5D_mean')
        rtVal.append('rmin_5D_mean')
        rtVal.append('rmax_5D_mean')
        rtVal.append('sph_5D_mean')
        rtVal.append('vs_5D_mean')
        rtVal.append('th_5D_mean')
        rtVal.append('srad_5D_mean')
        rtVal.append('etr_5D_mean')
        rtVal.append('fm100_5D_mean')
        rtVal.append('fm1000_5D_mean')
        rtVal.append('bi_5D_mean')
        rtVal.append('vpd_5D_mean')
        rtVal.append('erc_5D_mean')
        rtVal.append('pr_5D_min')
        rtVal.append('pr_5D_max')
        rtVal.append('tmmn_5D_max')
        rtVal.append('tmmx_5D_max')
        rtVal.append('rmin_5D_min')
        rtVal.append('rmax_5D_min')
        rtVal.append('sph_5D_min')
        rtVal.append('vs_5D_max')
        rtVal.append('th_5D_max')
        rtVal.append('srad_5D_max')
        rtVal.append('etr_5D_max')
        rtVal.append('fm100_5D_min')
        rtVal.append('fm1000_5D_min')
        rtVal.append('bi_5D_max')
        rtVal.append('vpd_5D_max')
        rtVal.append('erc_5D_max')
    elif category=='Climate Percentiles' :
        rtVal.append('tmmn_Percentile')
        rtVal.append('tmmx_Percentile')
        rtVal.append('sph_Percentile')
        rtVal.append('vs_Percentile')
        rtVal.append('fm100_Percentile')
        rtVal.append('bi_Percentile')
        rtVal.append('vpd_Percentile')
        rtVal.append('erc_Percentile')
    elif category=='Ecoregions' :
        rtVal.append('Ecoregion_US_L4CODE')
        rtVal.append('Ecoregion_US_L3CODE')
        rtVal.append('Ecoregion_NA_L3CODE')
        rtVal.append('Ecoregion_NA_L2CODE')
        rtVal.append('Ecoregion_NA_L1CODE')
    elif category=='Topography' :
        rtVal.append('Elevation')
        rtVal.append('Aspect')
        rtVal.append('Slope')
        rtVal.append('TPI')
        rtVal.append('TRI')
        rtVal.append('Elevation_1km')
        rtVal.append('Aspect_1km')
        rtVal.append('Slope_1km')
        rtVal.append('TPI_1km')
        rtVal.append('TRI_1km')
    elif category=='Vegetation' :
        rtVal.append('EVC')
        rtVal.append('EVC_1km')
        rtVal.append('EVH')
        rtVal.append('EVH_1km')
        rtVal.append('EVT')
        rtVal.append('EVT_1km')
    elif category=='Risk Management Assistance' :
        rtVal.append('Evacuation')
        rtVal.append('SDI')
    elif category=='Fire Regime Groups' :
        rtVal.append('FRG')
        rtVal.append('FRG_1km')
    elif category=='Fire Stations' :
        rtVal.append('No_FireStation_10km')
        rtVal.append('No_FireStation_50km')
        rtVal.append('No_FireStation_100km')
        rtVal.append('No_FireStation_200km')
    elif category=='Geographic Area Coordination Centers' :
        rtVal.append('GACCAbbrev')
        rtVal.append('GACC_PL')
        rtVal.append('GACC_New_fire')
        rtVal.append('GACC_New_LF')
        rtVal.append('GACC_Uncont_LF')
        rtVal.append('GACC_Type_1_IMTs')
        rtVal.append('GACC_Type_2_IMTs')
        rtVal.append('GACC_NIMO_Teams')
        rtVal.append('GACC_Area_Command_Teams')
        rtVal.append('GACC_Fire_Use_Teams')
    elif category=='Gap Analysis Project' :
        rtVal.append('Mang_Type')
        rtVal.append('Mang_Name')
        rtVal.append('Des_Tp')
        rtVal.append('GAP_Sts')
        rtVal.append('GAP_Prity')
    elif category=='Gross Domestic Product' :
        rtVal.append('GDP')
    elif category=='Global Human Modification' :
        rtVal.append('GHM')
    elif category=='MODIS NDVI' :
        rtVal.append('MOD_NDVI_12m')
        rtVal.append('MOD_EVI_12m')
    elif category=='NOAA NDVI' :
        rtVal.append('NDVI_min')
        rtVal.append('NDVI_max')
        rtVal.append('NDVI_mean')
        rtVal.append('NDVI1day')
    elif category=='National Land Cover Database' :
        rtVal.append('Land_Cover')
        rtVal.append('Land_Cover_1km')
    elif category=='National Preparedness Level' :
        rtVal.append('NPL')
    elif category=='Population' :
        rtVal.append('Population')
        rtVal.append('Popo_1km')
    elif category=='Pyrome' :
        rtVal.append('NAME')
    elif category=='Road' :
        rtVal.append('road_county_dis')
        rtVal.append('road_interstate_dis')
        rtVal.append('road_common_name_dis')
        rtVal.append('road_other_dis')
        rtVal.append('road_state_dis')
        rtVal.append('road_US_dis')
    elif category=='Social Vulnerability Index' :
        rtVal.append('RPL_THEMES')
        rtVal.append('RPL_THEME1')
        rtVal.append('EPL_POV')
        rtVal.append('EPL_UNEMP')
        rtVal.append('EPL_PCI')
        rtVal.append('EPL_NOHSDP')
        rtVal.append('RPL_THEME2')
        rtVal.append('EPL_AGE65')
        rtVal.append('EPL_AGE17')
        rtVal.append('EPL_DISABL')
        rtVal.append('EPL_SNGPNT')
        rtVal.append('RPL_THEME3')
        rtVal.append('EPL_MINRTY')
        rtVal.append('EPL_LIMENG')
        rtVal.append('RPL_THEME4')
        rtVal.append('EPL_MUNIT')
        rtVal.append('EPL_MOBILE')
        rtVal.append('EPL_CROWD')
        rtVal.append('EPL_NOVEH')
        rtVal.append('EPL_GROUPQ')
    elif category=='Rangeland Production Monitoring Service' :
        rtVal.append('rpms')
        rtVal.append('rpms_1km')
    return rtVal