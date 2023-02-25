/**
 * CSV Download button test suite
 */
/// <reference types="cypress" />

import { elements } from "../../fixtures/data-cy.json";
const url = "http://localhost:3000/f22-fires-wild/Data";
const django_url = "http://localhost:8000/f22-fires-wild/api/subset_csv/";

const idahoString = "FOD_ID,FPA_ID,SOURCE_SYSTEM_TYPE,SOURCE_SYSTEM,NWCG_REPORTING_AGENCY,NWCG_REPORTING_UNIT_ID,NWCG_REPORTING_UNIT_NAME,SOURCE_REPORTING_UNIT,SOURCE_REPORTING_UNIT_NAME,LOCAL_FIRE_REPORT_ID,LOCAL_INCIDENT_ID,FIRE_CODE,FIRE_NAME,ICS_209_PLUS_INCIDENT_JOIN_ID,ICS_209_PLUS_COMPLEX_JOIN_ID,MTBS_ID,MTBS_FIRE_NAME,COMPLEX_NAME,FIRE_YEAR,DISCOVERY_DATE,DISCOVERY_DOY,DISCOVERY_TIME,NWCG_CAUSE_CLASSIFICATION,NWCG_GENERAL_CAUSE,NWCG_CAUSE_AGE_CATEGORY,CONT_DATE,CONT_DOY,CONT_TIME,FIRE_SIZE,FIRE_SIZE_CLASS,LATITUDE,LONGITUDE,OWNER_DESCR,STATE,COUNTY,FIPS_CODE,FIPS_NAME,NPL,Mang_Type,Mang_Name,Des_Tp,GAP_Sts,GAP_Prity,EVC_1km,EVT_1km,EVT,EVC,EVH,EVH_1km,NAME,MOD_NDVI_12m,MOD_EVI_12m,Land_Cover,Land_Cover_1km,Popo_1km,Population,Unnamed: 0,CheatGrass,ExoticAnnualGrass,Medusahead,PoaSecunda,GACCAbbrev,GACC_PL,GACC_New fire,GACC_New LF,GACC_Uncont LF,GACC_Type 1 IMTs,GACC_Type 2 IMTs,GACC_NIMO Teams,GACC_Area Command Teams,GACC_Fire Use Teams,GDP,pr_Normal,tmmn_Normal,tmmx_Normal,rmin_Normal,rmax_Normal,sph_Normal,srad_Normal,fm100_Normal,fm1000_Normal,bi_Normal,vpd_Normal,erc_Normal,DF_PFS,AF_PFS,HDF_PFS,DSF_PFS,EBF_PFS,EALR_PFS,EBLR_PFS,EPLR_PFS,HBF_PFS,LLEF_PFS,LIF_PFS,LMI_PFS,MHVF_PFS,PM25F_PFS,HSEF,P100_PFS,P200_PFS,LPF_PFS,NPL_PFS,RMP_PFS,TSDF_PFS,TPF,TF_PFS,UF_PFS,WF_PFS,M_WTR,M_WKFC,M_CLT,M_ENY,M_TRN,M_HSG,M_PLN,M_HLTH,SM_C,SM_PFS,EPLRLI,EALRLI,EBLRLI,PM25LI,EBLI,DPMLI,TPLI,LPMHVLI,HBLI,RMPLI,SFLI,HWLI,WDLI,DLI,ALI,HDLI,LLELI,LILHSE,PLHSE,LMILHSE,ULHSE,EPL_ET,EAL_ET,EBL_ET,EB_ET,PM25_ET,DS_ET,TP_ET,LPP_ET,HB_ET,RMP_ET,NPL_ET,TSDF_ET,WD_ET,DB_ET,A_ET,HD_ET,LLE_ET,UN_ET,LISO_ET,POV_ET,LMI_ET,IA_LMI_ET,IA_UN_ET,IA_POV_ET,TC,CC,IAULHSE,IAPLHSE,IALMILHSE,IALMIL_87,IAPLHS_88,IAULHS_89,LHE,IALHE,IAHSEF,CA,NCA,CA_LT20,M_CLT_EOMI,M_ENY_EOMI,M_TRN_EOMI,M_HSG_EOMI,M_PLN_EOMI,M_WTR_EOMI,M_HLTH_102,M_WKFC_103,FPL200S,M_WKFC_105,M_EBSI,UI_EXP,THRHLD,No_FireStation_1.0km,No_FireStation_5.0km,No_FireStation_10.0km,No_FireStation_20.0km,FRG_1km,FRG,TRI_1km,TRI,Aspect,Elevation_1km,Elevation,Slope,Slope_1km,Aspect_1km,GHM,TPI_1km,TPI,TRACT,RPL_THEMES,RPL_THEME1,EPL_POV,EPL_UNEMP,EPL_PCI,EPL_NOHSDP,RPL_THEME2,EPL_AGE65,EPL_AGE17,EPL_DISABL,EPL_SNGPNT,RPL_THEME3,EPL_MINRTY,EPL_LIMENG,RPL_THEME4,EPL_MUNIT,EPL_MOBILE,EPL_CROWD,EPL_NOVEH,EPL_GROUPQ,road_county_dis,road_interstate_dis,road_common_name_dis,road_other_dis,road_state_dis,road_US_dis,Ecoregion_US_L4CODE,Ecoregion_US_L3CODE,Ecoregion_NA_L3CODE,Ecoregion_NA_L2CODE,Ecoregion_NA_L1CODE,SDI,Annual_etr,Annual_precipitation,Annual_tempreture,Aridity_index,Evacuation,pr,tmmn,tmmx,rmin,rmax,sph,vs,th,srad,etr,fm100,fm1000,bi,vpd,erc,pr_5D_mean,tmmn_5D_mean,tmmx_5D_mean,rmin_5D_mean,rmax_5D_mean,sph_5D_mean,vs_5D_mean,th_5D_mean,srad_5D_mean,etr_5D_mean,fm100_5D_mean,fm1000_5D_mean,bi_5D_mean,vpd_5D_mean,erc_5D_mean,pr_5D_min,pr_5D_max,tmmn_5D_max,tmmx_5D_max,rmin_5D_min,rmax_5D_min,sph_5D_min,vs_5D_max,th_5D_max,srad_5D_max,etr_5D_max,fm100_5D_min,fm1000_5D_min,bi_5D_max,vpd_5D_max,erc_5D_max,tmmn_Percentile,tmmx_Percentile,sph_Percentile,vs_Percentile,fm100_Percentile,bi_Percentile,vpd_Percentile,erc_Percentile,NDVI_min,NDVI_max,NDVI_mean,NDVI-1day\n400308148,W-720453,FED,DOI-WFMI,BLM,USIDBOD,Boise District,IDBPD,Boise District,651.0,,L146,OTR 3,,,,,,2018,2018-04-13,103,1553.0,Human,Firearms and explosives use,,4/13/2018 0:00:00,103.0,1553.0,0.1,A,43.2431,-116.0436,BLM,ID,Ada,16001.0,Ada County,Idaho,Ada,2.0,FED,BLM,NCA,2.0,8.0,330(16%) / 329(15%) / 331(14%),9307(62%) / 7123(23%) / 7080(7%),9336.0,222.0,202.0,302(86%) / 208(5%) / 63(3%),Snake River Plain,'0.33' '0.29' '0.28' '0.24' '0.22' '0.24' '0.23' '0.26' '0.38' '0.46','0.18' '0.14' '0.13' '0.14' '0.13' '0.15' '0.15' '0.17' '0.24' '0.29',52.0,71(97%) / 52(1%) / 21(1%),558,836.2818847818847,0.0,0.0,24883.0,9.0,10.0,0.0,12.0,SACC,2.0,426.0,14.0,10.0,0.0,0.0,0.0,0.0,,41841.418,0.89,274.5,289.20001220703125,29.8,85.8,0.004,231.0,13.9,16.5,25.200000762939453,0.7,32.599998474121094,0.04,0.18,0.04,0.08,0.08,0.7,0.95,0.21,0.19,0.45,0.73,0.11,0.69,0.21,0.03,0.16,0.12,0.06,0.15,0.69,0.48,4512.0,0.34,0.52,0.54,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,,,,0.0,0.0,,0.07,0.92,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,Nation,21.0,,,,9.0,4(99%) / 3(1%) / 132(0%),4.0,1.569,3.0,-1.0,761.797520661157,963.0,2.0,0.509641873278237,-0.1136363636363636,0.11,-0.0,-0.125,10503.0,0.3165,0.1605,0.1015,0.4219,0.2977,0.0691,0.2561,0.113,0.9313,0.2474,0.3431,0.5762,0.4399,0.6611,0.5368,0.7519,0.7653,0.0,0.5118,0.3791,,,33.1,,,,12h,12.0,10.1.8,10.1,10.0,0.09,1954.0,256.0,284.0,0.13,,0.0,275.8999938964844,286.1000061035156,32.400001525878906,71.5,0.0035999999381601,5.3,308.0,227.8000030517578,5.0,13.6,17.2,36.0,0.59,34.0,1.46,276.94,288.44,32.8,77.9,0.0042580003,5.36,174.8,229.12003,5.1,13.8,17.2,12.4,0.67,27.8,0.0,2.7,279.4,293.4,27.6,66.700005,0.0034299998,10.0,308.0,238.2,6.6,12.2,16.7,36.0,0.92,37.0,>90%,>90%,30-50%,50-70%,50-70%,50-70%,30-50%,50-70%,'0.01' '0.0' '-0.01' '-0.02' '-0.0' '0.02' '0.01' '0.04' '0.1' '0.0' '0.01' '0.0','0.41' '0.37' '0.29' '0.26' '0.28' '0.25' '0.27' '0.32' '0.32' '0.34' '0.52' '0.59','0.22' '0.18' '0.11' '0.08' '0.11' '0.19' '0.2' '0.22' '0.26' '0.23' '0.33' '0.3',0.07"

describe('CSV Download', () => {
    beforeEach(() => {
        cy.visit(url)
        cy.get('.css-1hb7zxy-IndicatorsContainer').eq(0).click() //year dropdown
        cy.get('div[id="react-select-3-listbox"] >> div[id="react-select-3-option-0"]').click(); //select first year, should be 2018
    })
    it('csv dowload button returns a csv file', () => {
        cy.get('.css-1hb7zxy-IndicatorsContainer').eq(1).click()
        cy.get('div[id="react-select-5-listbox"] >> div[id="react-select-5-option-13"]').click();
        cy.get('.css-sghohy-MuiButtonBase-root-MuiButton-root').eq(0).click()
        cy.get('.css-sghohy-MuiButtonBase-root-MuiButton-root').eq(1).click()
        cy.verifyDownload('export.csv');
    })
    it("idaho csv is correct", () => {
        cy.get('.css-1hb7zxy-IndicatorsContainer').eq(1).click()
        cy.get('div[id="react-select-5-listbox"] >> div[id="react-select-5-option-13"]').click();
        cy.get('.css-sghohy-MuiButtonBase-root-MuiButton-root').eq(0).click()
        cy.request({
          method: 'GET',
          url: django_url,
        }).then((response) => {
          expect(response.status).to.eq(200);
          expect(response.headers?.["content-type"]).to.eq("text/csv");
          expect(response.headers?.["content-disposition"]).to.contain(
            `filename="${filename}`
          );
          expect(response.body).to.be.a("string");
          expect(response.body).to.eq(idahoString);
        })
      });
})