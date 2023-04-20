const allCategories = ["FPA_FOD", 
  "Annual Climate", "Cheat Grass", "Climate Normals", "GRIDMET", 
  "Climate Percentiles", "Ecoregions", "Topography", "Vegetation",
  "Risk Management Assistance", "Fire Regime Groups", "Fire Stations", 
  "Geographic Area Coordination Centers", "Gap Analysis Project", 
  "Gross Domestic Product", "Global Human Modification", "MODIS NDVI", 
  "NOAA NDVI", "National Land Cover Database", "National Preparedness Level", "Population", "Pyrome", "Road", 
  "Social Vulnerability Index", "Rangeland Production Monitoring Service", "Climate and Economic Justice Screening Tool"];

export function getFields(categories) {
    var rtVal = new Array();
    allCategories.forEach(c => {
        if(categories.indexOf(c)>=0){
            var fields = fieldsFromCategory(c);
            fields.forEach(f => {rtVal.push(f);});
        }
        
    });
    return rtVal;
}

export function getAllCategories() {
    let rtVal = new Array();
    allCategories.forEach(c => {
        rtVal.push(c);
    })
    return rtVal;
}

function fieldsFromCategory(category) {
    var rtVal = new Array();
    if(category=='FPA_FOD'){
        rtVal.push('FOD_ID');
        rtVal.push('FPA_ID');
        rtVal.push('SOURCE_SYSTEM_TYPE');
        rtVal.push('SOURCE_SYSTEM');
        rtVal.push('NWCG_REPORTING_AGENCY');
        rtVal.push('NWCG_REPORTING_UNIT_ID');
        rtVal.push('SOURCE_REPORTING_UNIT');
        rtVal.push('SOURCE_REPORTING_UNIT_NAME');
        rtVal.push('LOCAL_FIRE_REPORT_ID');
        rtVal.push('LOCAL_INCIDENT_ID');
        rtVal.push('FIRE_CODE');
        rtVal.push('FIRE_NAME');
        rtVal.push('ICS_209_PLUS_INCIDENT_JOIN_ID');
        rtVal.push('ICS_209_PLUS_COMPLEX_JOIN_ID');
        rtVal.push('MTBS_ID');
        rtVal.push('MTBS_FIRE_NAME');
        rtVal.push('COMPLEX_NAME');
        rtVal.push('FIRE_YEAR');
        rtVal.push('DISCOVERY_DATE');
        rtVal.push('DISCOVERY_DOY');
        rtVal.push('DISCOVERY_TIME');
        rtVal.push('NWCG_CAUSE_CLASSIFICATION');
        rtVal.push('NWCG_GENERAL_CAUSE');
        rtVal.push('NWCG_CAUSE_AGE_CATEGORY');
        rtVal.push('CONT_DATE');
        rtVal.push('CONT_DOY');
        rtVal.push('CONT_TIME');
        rtVal.push('FIRE_SIZE');
        rtVal.push('FIRE_SIZE_CLASS');
        rtVal.push('LATITUDE');
        rtVal.push('LONGITUDE');
        rtVal.push('OWNER_DESCR');
        rtVal.push('STATE');
        rtVal.push('COUNTY');
        rtVal.push('FIPS_CODE');
        rtVal.push('FIPS_NAME');
        //rtVal.push('Year');
    }else if(category=='Climate and Economic Justice Screening Tool'){
        rtVal.push('DF_PFS');
        rtVal.push('AF_PFS');
        rtVal.push('HDF_PFS');
        rtVal.push('DSF_PFS');
        rtVal.push('EBF_PFS');
        rtVal.push('EALR_PFS');
        rtVal.push('EBLR_PFS');
        rtVal.push('EPLR_PFS');
        rtVal.push('HBF_PFS');
        rtVal.push('LLEF_PFS');
        rtVal.push('LIF_PFS');
        rtVal.push('LMI_PFS');
        rtVal.push('MHVF_PFS');
        rtVal.push('PM25F_PFS');
        rtVal.push('HSEF');
        rtVal.push('P100_PFS');
        rtVal.push('P200_PFS');
        rtVal.push('LPF_PFS');
        rtVal.push('NPL_PFS');
        rtVal.push('RMP_PFS');
        rtVal.push('TSDF_PFS');
        rtVal.push('TPF');
        rtVal.push('TF_PFS');
        rtVal.push('UF_PFS');
        rtVal.push('WF_PFS');
        rtVal.push('M_WTR');
        rtVal.push('M_WKFC');
        rtVal.push('M_CLT');
        rtVal.push('M_ENY');
        rtVal.push('M_TRN');
        rtVal.push('M_HSG');
        rtVal.push('M_PLN');
        rtVal.push('M_HLTH');
        rtVal.push('SM_C');
        rtVal.push('SM_PFS');
        rtVal.push('EPLRLI');
        rtVal.push('EALRLI');
        rtVal.push('EBLRLI');
        rtVal.push('PM25LI');
        rtVal.push('EBLI');
        rtVal.push('DPMLI');
        rtVal.push('TPLI');
        rtVal.push('LPMHVLI');
        rtVal.push('HBLI');
        rtVal.push('RMPLI');
        rtVal.push('SFLI');
        rtVal.push('HWLI');
        rtVal.push('WDLI');
        rtVal.push('DLI');
        rtVal.push('ALI');
        rtVal.push('HDLI');
        rtVal.push('LLELI');
        rtVal.push('LILHSE');
        rtVal.push('PLHSE');
        rtVal.push('LMILHSE');
        rtVal.push('ULHSE');
        rtVal.push('EPL_ET');
        rtVal.push('EAL_ET');
        rtVal.push('EBL_ET');
        rtVal.push('EB_ET');
        rtVal.push('PM25_ET');
        rtVal.push('DS_ET');
        rtVal.push('TP_ET');
        rtVal.push('LPP_ET');
        rtVal.push('HB_ET');
        rtVal.push('RMP_ET');
        rtVal.push('NPL_ET');
        rtVal.push('TSDF_ET');
        rtVal.push('WD_ET');
        rtVal.push('DB_ET');
        rtVal.push('A_ET');
        rtVal.push('HD_ET');
        rtVal.push('LLE_ET');
        rtVal.push('UN_ET');
        rtVal.push('LISO_ET');
        rtVal.push('POV_ET');
        rtVal.push('LMI_ET');
        rtVal.push('IA_LMI_ET');
        rtVal.push('IA_UN_ET');
        rtVal.push('IA_POV_ET');
        rtVal.push('TC');
        rtVal.push('CC');
        rtVal.push('IAULHSE');
        rtVal.push('IAPLHSE');
        rtVal.push('IALMILHSE');
        rtVal.push('IALMIL_87');
        rtVal.push('IAPLHS_88');
        rtVal.push('IAULHS_89');
        rtVal.push('LHE');
        rtVal.push('IALHE');
        rtVal.push('IAHSEF');
        rtVal.push('CA');
        rtVal.push('NCA');
        rtVal.push('CA_LT20');
        rtVal.push('M_CLT_EOMI');
        rtVal.push('M_ENY_EOMI');
        rtVal.push('M_TRN_EOMI');
        rtVal.push('M_HSG_EOMI');
        rtVal.push('M_PLN_EOMI');
        rtVal.push('M_WTR_EOMI');
        rtVal.push('M_HLTH_102');
        rtVal.push('M_WKFC_103');
        rtVal.push('FPL200S');
        rtVal.push('M_WKFC_105');
        rtVal.push('M_EBSI');
        rtVal.push('UI_EXP');
        rtVal.push('THRHLD');
    }else if(category=='Annual Climate'){
        rtVal.push('Annual_etr');
        rtVal.push('Annual_precipitation');
        rtVal.push('Annual_tempreture');
        rtVal.push('Aridity_index');
    }else if(category=='Cheat Grass'){
        rtVal.push('CheatGrass');
        rtVal.push('ExoticAnnualGrass');
        rtVal.push('Medusahead');
        rtVal.push('PoaSecunda');
    }else if(category=='Climate Normals'){
        rtVal.push('pr_Normal');
        rtVal.push('tmmn_Normal');
        rtVal.push('tmmx_Normal');
        rtVal.push('rmin_Normal');
        rtVal.push('rmax_Normal');
        rtVal.push('sph_Normal');
        rtVal.push('srad_Normal');
        rtVal.push('fm100_Normal');
        rtVal.push('fm1000_Normal');
        rtVal.push('bi_Normal');
        rtVal.push('vpd_Normal');
        rtVal.push('erc_Normal');
    }else if(category=='GRIDMET'){
        rtVal.push('pr');
        rtVal.push('tmmn');
        rtVal.push('tmmx');
        rtVal.push('rmin');
        rtVal.push('rmax');
        rtVal.push('sph');
        rtVal.push('vs');
        rtVal.push('th');
        rtVal.push('srad');
        rtVal.push('etr');
        rtVal.push('fm100');
        rtVal.push('fm1000');
        rtVal.push('bi');
        rtVal.push('vpd');
        rtVal.push('erc');
        rtVal.push('pr_5D_mean');
        rtVal.push('tmmn_5D_mean');
        rtVal.push('tmmx_5D_mean');
        rtVal.push('rmin_5D_mean');
        rtVal.push('rmax_5D_mean');
        rtVal.push('sph_5D_mean');
        rtVal.push('vs_5D_mean');
        rtVal.push('th_5D_mean');
        rtVal.push('srad_5D_mean');
        rtVal.push('etr_5D_mean');
        rtVal.push('fm100_5D_mean');
        rtVal.push('fm1000_5D_mean');
        rtVal.push('bi_5D_mean');
        rtVal.push('vpd_5D_mean');
        rtVal.push('erc_5D_mean');
        rtVal.push('pr_5D_min');
        rtVal.push('pr_5D_max');
        rtVal.push('tmmn_5D_max');
        rtVal.push('tmmx_5D_max');
        rtVal.push('rmin_5D_min');
        rtVal.push('rmax_5D_min');
        rtVal.push('sph_5D_min');
        rtVal.push('vs_5D_max');
        rtVal.push('th_5D_max');
        rtVal.push('srad_5D_max');
        rtVal.push('etr_5D_max');
        rtVal.push('fm100_5D_min');
        rtVal.push('fm1000_5D_min');
        rtVal.push('bi_5D_max');
        rtVal.push('vpd_5D_max');
        rtVal.push('erc_5D_max');
    }else if(category=='Climate Percentiles'){
        rtVal.push('tmmn_Percentile');
        rtVal.push('tmmx_Percentile');
        rtVal.push('sph_Percentile');
        rtVal.push('vs_Percentile');
        rtVal.push('fm100_Percentile');
        rtVal.push('bi_Percentile');
        rtVal.push('vpd_Percentile');
        rtVal.push('erc_Percentile');
    }else if(category=='Ecoregions'){
        rtVal.push('Ecoregion_US_L4CODE');
        rtVal.push('Ecoregion_US_L3CODE');
        rtVal.push('Ecoregion_NA_L3CODE');
        rtVal.push('Ecoregion_NA_L2CODE');
        rtVal.push('Ecoregion_NA_L1CODE');
    }else if(category=='Topography'){
        rtVal.push('Elevation');
        rtVal.push('Aspect');
        rtVal.push('Slope');
        rtVal.push('TPI');
        rtVal.push('TRI');
        rtVal.push('Elevation_1km');
        rtVal.push('Aspect_1km');
        rtVal.push('Slope_1km');
        rtVal.push('TPI_1km');
        rtVal.push('TRI_1km');
    }else if(category=='Vegetation'){
        rtVal.push('EVC');
        rtVal.push('EVC_1km');
        rtVal.push('EVH');
        rtVal.push('EVH_1km');
        rtVal.push('EVT');
        rtVal.push('EVT_1km');
    }else if(category=='Risk Management Assistance'){
        rtVal.push('Evacuation');
        rtVal.push('SDI');
    }else if(category=='Fire Regime Groups'){
        rtVal.push('FRG');
        rtVal.push('FRG_1km');
    }else if(category=='Fire Stations'){
        rtVal.push('No_FireStation_10km');
        rtVal.push('No_FireStation_50km');
        rtVal.push('No_FireStation_100km');
        rtVal.push('No_FireStation_200km');
    }else if(category=='Geographic Area Coordination Centers'){
        rtVal.push('GACCAbbrev');
        rtVal.push('GACC_PL');
        rtVal.push('GACC_New_fire');
        rtVal.push('GACC_New_LF');
        rtVal.push('GACC_Uncont_LF');
        rtVal.push('GACC_Type_1_IMTs');
        rtVal.push('GACC_Type_2_IMTs');
        rtVal.push('GACC_NIMO_Teams');
        rtVal.push('GACC_Area_Command_Teams');
        rtVal.push('GACC_Fire_Use_Teams');
    }else if(category=='Gap Analysis Project'){
        rtVal.push('Mang_Type');
        rtVal.push('Mang_Name');
        rtVal.push('Des_Tp');
        rtVal.push('GAP_Sts');
        rtVal.push('GAP_Prity');
    }else if(category=='Gross Domestic Product'){
        rtVal.push('GDP');
    }else if(category=='Global Human Modification'){
        rtVal.push('GHM');
    }else if(category=='MODIS NDVI'){
        rtVal.push('MOD_NDVI_12m');
        rtVal.push('MOD_EVI_12m');
    }else if(category=='NOAA NDVI'){
        rtVal.push('NDVI_min');
        rtVal.push('NDVI_max');
        rtVal.push('NDVI_mean');
        rtVal.push('NDVI1day');
    }else if(category=='National Land Cover Database'){
        rtVal.push('Land_Cover');
        rtVal.push('Land_Cover_1km');
    }else if(category=='National Preparedness Level'){
        rtVal.push('NPL');
    }else if(category=='Population'){
        rtVal.push('Population');
        rtVal.push('Popo_1km');
    }else if(category=='Pyrome'){
        rtVal.push('NAME');
    }else if(category=='Road'){
        rtVal.push('road_county_dis');
        rtVal.push('road_interstate_dis');
        rtVal.push('road_common_name_dis');
        rtVal.push('road_other_dis');
        rtVal.push('road_state_dis');
        rtVal.push('road_US_dis');
    }else if(category=='Social Vulnerability Index'){
        rtVal.push('RPL_THEMES');
        rtVal.push('RPL_THEME1');
        rtVal.push('EPL_POV');
        rtVal.push('EPL_UNEMP');
        rtVal.push('EPL_PCI');
        rtVal.push('EPL_NOHSDP');
        rtVal.push('RPL_THEME2');
        rtVal.push('EPL_AGE65');
        rtVal.push('EPL_AGE17');
        rtVal.push('EPL_DISABL');
        rtVal.push('EPL_SNGPNT');
        rtVal.push('RPL_THEME3');
        rtVal.push('EPL_MINRTY');
        rtVal.push('EPL_LIMENG');
        rtVal.push('RPL_THEME4');
        rtVal.push('EPL_MUNIT');
        rtVal.push('EPL_MOBILE');
        rtVal.push('EPL_CROWD');
        rtVal.push('EPL_NOVEH');
        rtVal.push('EPL_GROUPQ');
    }else if(category=='Rangeland Production Monitoring Service'){
        rtVal.push('rpms');
        rtVal.push('rpms_1km');
    }else if(category=='National Preparedness Level'){
        rtVal.push('NPL');
    }
    return rtVal;
}