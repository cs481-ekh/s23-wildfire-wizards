CREATE TABLE IF NOT EXISTS FPA_FOD_PLUS(
   FOD_ID                        INTEGER NOT NULL PRIMARY KEY 
  ,FPA_ID                        VARCHAR(55)
  ,SOURCE_SYSTEM_TYPE            VARCHAR(15)
  ,SOURCE_SYSTEM                 VARCHAR(25)
  ,NWCG_REPORTING_AGENCY         VARCHAR(25)
  ,NWCG_REPORTING_UNIT_ID        VARCHAR(25)
  ,NWCG_REPORTING_UNIT_NAME      VARCHAR(125)
  ,SOURCE_REPORTING_UNIT         VARCHAR(25)
  ,SOURCE_REPORTING_UNIT_NAME    VARCHAR(100)
  ,LOCAL_FIRE_REPORT_ID          INTEGER 
  ,LOCAL_INCIDENT_ID             VARCHAR(50)
  ,FIRE_CODE                     VARCHAR(25)
  ,FIRE_NAME                     VARCHAR(100)
  ,ICS_209_PLUS_INCIDENT_JOIN_ID VARCHAR(75)
  ,ICS_209_PLUS_COMPLEX_JOIN_ID  VARCHAR(75)
  ,MTBS_ID                       VARCHAR(75)
  ,MTBS_FIRE_NAME                VARCHAR(75)
  ,COMPLEX_NAME                  VARCHAR(50)
  ,FIRE_YEAR                     INTEGER 
  ,DISCOVERY_DATE                DATE 
  ,DISCOVERY_DOY                 INTEGER 
  ,DISCOVERY_TIME                INTEGER 
  ,NWCG_CAUSE_CLASSIFICATION     VARCHAR(75)
  ,NWCG_GENERAL_CAUSE            VARCHAR(75)
  ,NWCG_CAUSE_AGE_CATEGORY       VARCHAR(25)
  ,CONT_DATE                     VARCHAR(50)
  ,CONT_DOY                      INTEGER 
  ,CONT_TIME                     INTEGER 
  ,FIRE_SIZE                     NUMERIC(15,4)
  ,FIRE_SIZE_CLASS               VARCHAR(5)
  ,LATITUDE                      NUMERIC(15,8)
  ,LONGITUDE                     NUMERIC(15,8)
  ,OWNER_DESCR                   VARCHAR(35)
  ,STATE                         VARCHAR(5)
  ,COUNTY                        VARCHAR(50)
  ,FIPS_CODE                     INTEGER 
  ,FIPS_NAME                     VARCHAR(50)
  ,LatLong_State                 VARCHAR(15)
  ,LatLong_County                VARCHAR(30)
  ,NPL                           INTEGER
  ,Mang_Type                     VARCHAR(10)
  ,Mang_Name                     VARCHAR(10)
  ,Des_Tp                        VARCHAR(10)
  ,GAP_Sts                       INTEGER 
  ,GAP_Prity                     INTEGER
  ,EVH                           INTEGER
  ,EVT                           INTEGER
  ,EVH_1km                       VARCHAR(50)
  ,EVT_1km                       VARCHAR(50)
  ,EVC                           INTEGER 
  ,EVC_1km                       VARCHAR(50)
  ,NAME                          VARCHAR(100)
  ,MOD_NDVI_12m                  VARCHAR(100)
  ,MOD_EVI_12m                   VARCHAR(100)
  ,Land_over                    INTEGER
  ,Land_Cover_1km                VARCHAR(75)
  ,rpms				                   INTEGER
  ,rpms_1km                      NUMERIC(12,8)
  ,Population                    NUMERIC(12,4)
  ,Popo_1km                      NUMERIC(8,4)
  ,GACCAbbrev                    VARCHAR(10)
  ,GACC_PL                       INTEGER 
  ,GACC_New_fire                 INTEGER 
  ,GACC_New_LF                   INTEGER 
  ,GACC_Uncont_LF                INTEGER 
  ,GACC_Type_1_IMTs              INTEGER 
  ,GACC_Type_2_IMTs              INTEGER 
  ,GACC_NIMO_Teams               BIT 
  ,GACC_Area_Command_Teams       BIT 
  ,GACC_Fire_Use_Teams           VARCHAR(50)
  ,GDP                           NUMERIC(12,3)
  ,pr_Normal                     NUMERIC(6,2)
  ,tmmn_Normal                   NUMERIC(15,7)
  ,tmmx_Normal                   NUMERIC(15,7)
  ,rmin_Normal                   NUMERIC(6,1)
  ,rmax_Normal                   NUMERIC(6,1)
  ,sph_Normal                    NUMERIC(6,4)
  ,srad_Normal                   NUMERIC(6,1) 
  ,fm100_Normal                  NUMERIC(6,1)
  ,fm1000_Normal                 NUMERIC(6,1)
  ,bi_Normal                     NUMERIC(16,9)
  ,vpd_Normal                    NUMERIC(5,2)
  ,erc_Normal                    NUMERIC(15,9)     
  ,DF_PFS                        NUMERIC(5,2)
  ,AF_PFS                        NUMERIC(5,2)
  ,HDF_PFS                       NUMERIC(5,2)
  ,DSF_PFS                       NUMERIC(5,2)
  ,EBF_PFS                       NUMERIC(5,2)
  ,EALR_PFS                      NUMERIC(5,2)
  ,EBLR_PFS                      NUMERIC(5,2)
  ,EPLR_PFS                      NUMERIC(5,2)
  ,HBF_PFS                       NUMERIC(5,2)
  ,LLEF_PFS                      NUMERIC(5,2)
  ,LIF_PFS                       NUMERIC(5,2)
  ,LMI_PFS                       NUMERIC(5,2)
  ,MHVF_PFS                      NUMERIC(5,2)
  ,PM25F_PFS                     NUMERIC(5,2)
  ,HSEF                          NUMERIC(5,2)
  ,P100_PFS                      NUMERIC(5,2)
  ,P200_PFS                      NUMERIC(5,2)
  ,LPF_PFS                       NUMERIC(5,2)
  ,NPL_PFS                       NUMERIC(5,2)
  ,RMP_PFS                       NUMERIC(5,2)
  ,TSDF_PFS                      NUMERIC(5,2)
  ,TPF                           INTEGER 
  ,TF_PFS                        NUMERIC(5,2)
  ,UF_PFS                        NUMERIC(5,2)
  ,WF_PFS                        NUMERIC(5,2)
  ,M_WTR                         BIT 
  ,M_WKFC                        BIT 
  ,M_CLT                         BIT 
  ,M_ENY                         BIT 
  ,M_TRN                         BIT 
  ,M_HSG                         BIT 
  ,M_PLN                         BIT 
  ,M_HLTH                        BIT 
  ,SM_C                          BIT 
  ,SM_PFS                        BIT 
  ,EPLRLI                        BIT 
  ,EALRLI                        BIT 
  ,EBLRLI                        BIT 
  ,PM25LI                        BIT 
  ,EBLI                          BIT 
  ,DPMLI                         BIT 
  ,TPLI                          BIT 
  ,LPMHVLI                       BIT 
  ,HBLI                          BIT 
  ,RMPLI                         BIT 
  ,SFLI                          BIT 
  ,HWLI                          BIT 
  ,WDLI                          BIT 
  ,DLI                           BIT 
  ,ALI                           BIT 
  ,HDLI                          BIT 
  ,LLELI                         BIT 
  ,LILHSE                        BIT 
  ,PLHSE                         BIT 
  ,LMILHSE                       BIT 
  ,ULHSE                         BIT 
  ,EPL_ET                        BIT 
  ,EAL_ET                        BIT 
  ,EBL_ET                        BIT 
  ,EB_ET                         BIT 
  ,PM25_ET                       BIT 
  ,DS_ET                         BIT 
  ,TP_ET                         BIT 
  ,LPP_ET                        BIT 
  ,HB_ET                         BIT 
  ,RMP_ET                        BIT 
  ,NPL_ET                        BIT 
  ,TSDF_ET                       BIT 
  ,WD_ET                         BIT 
  ,DB_ET                         BIT 
  ,A_ET                          BIT 
  ,HD_ET                         BIT 
  ,LLE_ET                        BIT 
  ,UN_ET                         BIT 
  ,LISO_ET                       BIT 
  ,POV_ET                        BIT 
  ,LMI_ET                        BIT 
  ,IA_LMI_ET                     BIT 
  ,IA_UN_ET                      BIT 
  ,IA_POV_ET                     BIT 
  ,TC                            INTEGER 
  ,CC                            INTEGER 
  ,IAULHSE                       BIT 
  ,IAPLHSE                       BIT 
  ,IALMILHSE                     BIT 
  ,IALMIL_87                     VARCHAR(50)
  ,IAPLHS_88                     VARCHAR(50)
  ,IAULHS_89                     VARCHAR(50)
  ,LHE                           BIT 
  ,IALHE                         BIT 
  ,IAHSEF                        VARCHAR(50)
  ,CA                            NUMERIC(5,2)
  ,NCA                           NUMERIC(5,2)
  ,CA_LT20                       BIT 
  ,M_CLT_EOMI                    BIT 
  ,M_ENY_EOMI                    BIT 
  ,M_TRN_EOMI                    BIT 
  ,M_HSG_EOMI                    BIT 
  ,M_PLN_EOMI                    BIT 
  ,M_WTR_EOMI                    BIT 
  ,M_HLTH_102                    BIT 
  ,M_WKFC_103                    BIT 
  ,FPL200S                       BIT 
  ,M_WKFC_105                    BIT 
  ,M_EBSI                        BIT 
  ,UI_EXP                        VARCHAR(25)
  ,THRHLD                        INTEGER
  ,No_FireStation_1km           INTEGER 
  ,No_FireStation_5km           INTEGER 
  ,No_FireStation_10km          INTEGER 
  ,No_FireStation_20km          INTEGER
  ,FRG_1km                       VARCHAR(50)
  ,FRG                           INTEGER  
  ,TRI_1km                       NUMERIC(10,3)
  ,TRI                           NUMERIC(10,3)
  ,Aspect_1km                    NUMERIC(16,9)
  ,Elevation_1km                 NUMERIC(16,9)
  ,Elevation                     INTEGER 
  ,Slope_1km                     NUMERIC(16,9)
  ,Aspect                        INTEGER 
  ,Slope                         INTEGER
  ,GHM                           NUMERIC(12,6)
  ,TPI                           NUMERIC(10,3) 
  ,TPI_1km                       NUMERIC(10,2)
  ,TRACT                         INTEGER 
  ,RPL_THEMES                    NUMERIC(10,4)
  ,RPL_THEME1                    NUMERIC(10,4)
  ,EPL_POV                       NUMERIC(10,4)
  ,EPL_UNEMP                     NUMERIC(10,4)
  ,EPL_PCI                       NUMERIC(10,4)
  ,EPL_NOHSDP                    NUMERIC(10,4)
  ,RPL_THEME2                    NUMERIC(10,4)
  ,EPL_AGE65                     NUMERIC(10,4)
  ,EPL_AGE17                     NUMERIC(10,4)
  ,EPL_DISABL                    NUMERIC(10,4)
  ,EPL_SNGPNT                    NUMERIC(10,4)
  ,RPL_THEME3                    NUMERIC(10,4)
  ,EPL_MINRTY                    NUMERIC(10,4)
  ,EPL_LIMENG                    NUMERIC(10,4)
  ,RPL_THEME4                    NUMERIC(10,4)
  ,EPL_MUNIT                     NUMERIC(10,4)
  ,EPL_MOBILE                    NUMERIC(10,4)
  ,EPL_CROWD                     NUMERIC(10,4)
  ,EPL_NOVEH                     NUMERIC(10,4)
  ,EPL_GROUPQ                    NUMERIC(10,4)
  ,road_county_dis               NUMERIC(6,1)
  ,road_interstate_dis           NUMERIC(6,1)
  ,road_common_name_dis          NUMERIC(6,1)
  ,road_other_dis                NUMERIC(6,1)
  ,road_state_dis                NUMERIC(6,1)
  ,road_US_dis                   NUMERIC(6,1)
  ,Ecoregion_US_L4CODE           VARCHAR(10)
  ,Ecoregion_US_L3CODE           VARCHAR(10) 
  ,Ecoregion_NA_L3CODE           VARCHAR(10) 
  ,Ecoregion_NA_L2CODE           NUMERIC(6,1)
  ,Ecoregion_NA_L1CODE           VARCHAR(10)
  ,SDI                           NUMERIC(6,2)
  ,Annual_etr                    INTEGER 
  ,Annual_precipitation          INTEGER 
  ,Annual_tempreture             INTEGER 
  ,Aridity_index                 NUMERIC(5,2)
  ,Evacuation                    INTEGER  
  ,pr                            NUMERIC(12,9)
  ,tmmn                          NUMERIC(12,7)
  ,tmmx                          NUMERIC(12,7)
  ,rmin                          NUMERIC(15,9)
  ,rmax                          NUMERIC(12,8)
  ,sph                           NUMERIC(12,9)
  ,vs                            NUMERIC(5,1)
  ,th                            INTEGER 
  ,srad                          NUMERIC(15,8)
  ,etr                           NUMERIC(6,1)
  ,fm100                         NUMERIC(6,1)
  ,fm1000                        NUMERIC(6,1)
  ,bi                            INTEGER 
  ,vpd                           NUMERIC(6,2)
  ,erc                           INTEGER 
  ,pr_5D_mean                    NUMERIC(6,2)
  ,tmmn_5D_mean                  NUMERIC(10,5)
  ,tmmx_5D_mean                  NUMERIC(10,5)
  ,rmin_5D_mean                  NUMERIC(6,1)
  ,rmax_5D_mean                  NUMERIC(6,1)
  ,sph_5D_mean                   NUMERIC(12,9)
  ,vs_5D_mean                    NUMERIC(6,2)
  ,th_5D_mean                    NUMERIC(6,1)
  ,srad_5D_mean                  NUMERIC(12,6)
  ,etr_5D_mean                   NUMERIC(6,2)
  ,fm100_5D_mean                 NUMERIC(6,1)
  ,fm1000_5D_mean                NUMERIC(6,1)
  ,bi_5D_mean                    NUMERIC(6,1)
  ,vpd_5D_mean                   NUMERIC(5,2)
  ,erc_5D_mean                   NUMERIC(6,1)
  ,pr_5D_min                     NUMERIC(5,1)
  ,pr_5D_max                     NUMERIC(6,1)
  ,tmmn_5D_max                   NUMERIC(6,1)
  ,tmmx_5D_max                   NUMERIC(6,1)
  ,rmin_5D_min                   NUMERIC(5,1)
  ,rmax_5D_min                   NUMERIC(10,6)
  ,sph_5D_min                    NUMERIC(12,9)
  ,vs_5D_max                     NUMERIC(6,1)
  ,th_5D_max                     INTEGER 
  ,srad_5D_max                   NUMERIC(12,6)
  ,etr_5D_max                    NUMERIC(6,1)
  ,fm100_5D_min                  NUMERIC(6,1)
  ,fm1000_5D_min                 NUMERIC(6,1)
  ,bi_5D_max                     INTEGER 
  ,vpd_5D_max                    NUMERIC(6,2)
  ,erc_5D_max                    INTEGER 
  ,tmmn_Percentile               VARCHAR(35) 
  ,tmmx_Percentile               VARCHAR(35) 
  ,sph_Percentile                VARCHAR(10)
  ,vs_Percentile                 VARCHAR(10)
  ,fm100_Percentile              VARCHAR(10)
  ,bi_Percentile                 VARCHAR(10)
  ,vpd_Percentile                VARCHAR(10)
  ,erc_Percentile                VARCHAR(10)
  ,NDVI1day                      NUMERIC(8,2)
  ,NDVI_min                      VARCHAR(225)
  ,NDVI_max                      VARCHAR(225)
  ,NDVI_mean                     VARCHAR(225)
  ,Unnamed_0                     INTEGER 
  ,CheatGrass                    INTEGER 
  ,ExoticAnnualGrass             INTEGER 
  ,Medusahead                    INTEGER 
  ,PoaSecunda                    INTEGER
  ,Land_cover                    INTEGER
  ,geometry                      VARCHAR(100)
);

set @x := (SELECT COUNT(*) FROM information_schema.statistics WHERE table_name = 'FPA_FOD_PLUS' AND index_name = 'fpa_fod_index' AND table_schema = DATABASE());
set @sql := if( @x > 0, 'SELECT ''Index exists.''', 'CREATE INDEX fpa_fod_index ON FPA_FOD_PLUS (FIRE_YEAR, DISCOVERY_DATE, DISCOVERY_DOY, STATE, COUNTY);');
PREPARE stmt FROM @sql;
EXECUTE stmt;



-- SELECT COUNT(1) INTO @IndexExists 
-- FROM INFORMATION_SCHEMA.STATISTICS
-- WHERE table_schema=DATABASE() AND table_name = 'FPA_FOD_PLUS' AND index_name = 'fpa_fod_index';
-- CREATE INDEX fpa_fod_index
-- ON FPA_FOD_PLUS (FIRE_YEAR, DISCOVERY_DATE, DISCOVERY_DOY, STATE, COUNTY);
