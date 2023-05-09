import decimal
from django.db import models
from django.utils import timezone

# Create your models here.
class Data(models.Model):   
    FOD_ID = models.IntegerField(primary_key=True)
    FPA_ID = models.CharField(max_length=30, null=True)
    SOURCE_SYSTEM_TYPE = models.CharField(max_length=6, null=True)
    SOURCE_SYSTEM = models.CharField(max_length=11, null=True)
    NWCG_REPORTING_AGENCY = models.CharField(max_length=6, null=True)
    NWCG_REPORTING_UNIT_ID = models.CharField(max_length=8, null=True)
    NWCG_REPORTING_UNIT_NAME = models.CharField(max_length=69, null=True)
    SOURCE_REPORTING_UNIT = models.CharField(max_length=7, null=True)
    SOURCE_REPORTING_UNIT_NAME = models.CharField(max_length=69, null=True)
    LOCAL_FIRE_REPORT_ID = models.IntegerField(null=True)
    LOCAL_INCIDENT_ID = models.CharField(max_length=16, null=True)
    FIRE_CODE = models.CharField(max_length=4, null=True)
    FIRE_NAME = models.CharField(max_length=42, null=True)
    ICS_209_PLUS_INCIDENT_JOIN_ID = models.CharField(max_length=25, null=True)
    ICS_209_PLUS_COMPLEX_JOIN_ID = models.CharField(max_length=30, null=True)
    MTBS_ID = models.CharField(max_length=21, null=True)
    MTBS_FIRE_NAME = models.CharField(max_length=9, null=True)
    COMPLEX_NAME = models.CharField(max_length=30, null=True)
    FIRE_YEAR = models.IntegerField(null=True)
    DISCOVERY_DATE = models.DateField(null=True)
    DISCOVERY_DOY = models.IntegerField(null=True)
    DISCOVERY_TIME = models.IntegerField(null=True)
    NWCG_CAUSE_CLASSIFICATION = models.CharField(max_length=39, null=True)
    NWCG_GENERAL_CAUSE = models.CharField(max_length=42, null=True)
    NWCG_CAUSE_AGE_CATEGORY = models.CharField(max_length=5, null=True)
    CONT_DATE = models.CharField(max_length=11, null=True)
    CONT_DOY = models.IntegerField(null=True)
    CONT_TIME = models.IntegerField(null=True)
    FIRE_SIZE = models.DecimalField(max_digits=12,decimal_places=5, null=True)
    FIRE_SIZE_CLASS = models.CharField(max_length=1, null=True)
    LATITUDE = models.DecimalField(max_digits=10,decimal_places=7, null=True)
    LONGITUDE = models.DecimalField(max_digits=10,decimal_places=6, null=True)
    OWNER_DESCR = models.CharField(max_length=21, null=True)
    STATE = models.CharField(max_length=2, null=True)
    COUNTY = models.CharField(max_length=15,null=True)
    FIPS_CODE = models.IntegerField(null=True)
    FIPS_NAME = models.CharField(max_length=33, null=True)
    Year = models.IntegerField(null=True)
    Annual_etr = models.IntegerField(null=True)
    Annual_precipitation = models.IntegerField(null=True)
    Annual_tempreture = models.IntegerField(null=True)
    Aridity_index = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    CheatGrass = models.IntegerField(null=True)
    ExoticAnnualGrass = models.IntegerField(null=True)
    Medusahead = models.IntegerField(null=True)
    PoaSecunda = models.IntegerField(null=True)
    pr_Normal = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    tmmn_Normal = models.DecimalField(max_digits=10,decimal_places=6, null=True)
    tmmx_Normal = models.DecimalField(max_digits=10,decimal_places=6, null=True)
    rmin_Normal = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    rmax_Normal = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    sph_Normal = models.DecimalField(max_digits=10,decimal_places=4, null=True)
    srad_Normal = models.IntegerField(null=True)
    fm100_Normal = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    fm1000_Normal = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    bi_Normal = models.DecimalField(max_digits=10,decimal_places=7, null=True)
    vpd_Normal = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    erc_Normal = models.DecimalField(max_digits=10,decimal_places=7, null=True)
    pr = models.DecimalField(max_digits=10,decimal_places=8, null=True)
    tmmn = models.DecimalField(max_digits=10,decimal_places=6, null=True)
    tmmx = models.DecimalField(max_digits=10,decimal_places=6, null=True)
    rmin = models.DecimalField(max_digits=10,decimal_places=8, null=True)
    rmax = models.DecimalField(max_digits=10,decimal_places=7, null=True)
    sph = models.DecimalField( max_digits=10,decimal_places=5, null=True)
    vs = models.DecimalField( max_digits=10,decimal_places=1, null=True)
    th = models.IntegerField(null=True)
    srad = models.DecimalField(max_digits=10,decimal_places=6, null=True)
    etr = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    fm100 = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    fm1000 = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    bi = models.IntegerField(null=True)
    vpd = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    erc = models.IntegerField(null=True)
    pr_5D_mean = models.DecimalField( max_digits=10,decimal_places=2, null=True)
    tmmn_5D_mean = models.DecimalField( max_digits=10,decimal_places=5, null=True)
    tmmx_5D_mean = models.DecimalField( max_digits=10,decimal_places=5, null=True)
    rmin_5D_mean = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    rmax_5D_mean = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    sph_5D_mean = models.DecimalField(max_digits=12,decimal_places=6, null=True)
    vs_5D_mean = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    th_5D_mean = models.DecimalField( max_digits=10,decimal_places=1, null=True)
    srad_5D_mean = models.DecimalField( max_digits=10,decimal_places=5, null=True)
    etr_5D_mean = models.DecimalField( max_digits=10,decimal_places=2, null=True)
    fm100_5D_mean = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    fm1000_5D_mean = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    bi_5D_mean = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    vpd_5D_mean = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    erc_5D_mean = models.DecimalField( max_digits=10,decimal_places=1, null=True)
    pr_5D_min = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    pr_5D_max = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    tmmn_5D_max = models.DecimalField( max_digits=10,decimal_places=1, null=True)
    tmmx_5D_max = models.DecimalField( max_digits=10,decimal_places=1, null=True)
    rmin_5D_min = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    rmax_5D_min = models.DecimalField( max_digits=10,decimal_places=6, null=True)
    sph_5D_min = models.DecimalField( max_digits=10,decimal_places=5, null=True)
    vs_5D_max = models.DecimalField( max_digits=10,decimal_places=1, null=True)
    th_5D_max = models.IntegerField(null=True)
    srad_5D_max = models.DecimalField( max_digits=10,decimal_places=5, null=True)
    etr_5D_max = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    fm100_5D_min = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    fm1000_5D_min = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    bi_5D_max = models.IntegerField(null=True)
    vpd_5D_max = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    erc_5D_max = models.IntegerField(null=True)
    tmmn_Percentile = models.CharField(max_length=4, null=True)
    tmmx_Percentile = models.CharField(max_length=4, null=True)
    sph_Percentile = models.CharField(max_length=6, null=True)
    vs_Percentile = models.CharField(max_length=6, null=True)
    fm100_Percentile = models.CharField(max_length=6, null=True)
    bi_Percentile = models.CharField(max_length=6, null=True)
    vpd_Percentile = models.CharField(max_length=6, null=True)
    erc_Percentile = models.CharField(max_length=6, null=True)
    Ecoregion_US_L4CODE = models.CharField(max_length=30, null=True)
    Ecoregion_US_L3CODE = models.CharField(max_length=30, null=True)
    Ecoregion_NA_L3CODE = models.CharField(max_length=30, null=True)
    Ecoregion_NA_L2CODE = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    Ecoregion_NA_L1CODE  = models.CharField(max_length=30, null=True)
    Aspect_1km = models.DecimalField(max_digits=11,decimal_places=8, null=True)
    Aspect = models.IntegerField(null=True)
    Elevation_1km = models.DecimalField(max_digits=12,decimal_places=8, null=True)
    Elevation = models.IntegerField(null=True)
    Slope_1km = models.DecimalField(max_digits=10,decimal_places=8, null=True)
    Slope = models.IntegerField(null=True)
    EVC_1km = models.CharField(max_length=33, null=True)
    EVC = models.IntegerField(null=True)
    EVH_1km = models.CharField(max_length=33, null=True)
    EVH = models.IntegerField(null=True)
    EVT_1km = models.CharField(max_length=33, null=True)
    EVT = models.IntegerField(null=True)
    Evacuation = models.IntegerField(null=True)
    FRG_1km = models.CharField(max_length=27, null=True)
    FRG = models.IntegerField(null=True)
    No_FireStation_1km = models.IntegerField(null=True)
    No_FireStation_5km = models.IntegerField(null=True)
    No_FireStation_10km = models.IntegerField(null=True)
    No_FireStation_20km = models.IntegerField(null=True)
    GACCAbbrev = models.CharField(max_length=4, null=True)
    GACC_PL = models.IntegerField(null=True, blank=True)
    GACC_New_fire = models.IntegerField(null=True, blank=True)
    GACC_New_LF = models.IntegerField(null=True, blank=True)
    GACC_Uncont_LF = models.IntegerField(null=True, blank=True)
    GACC_Type_1_IMTs = models.IntegerField(null=True, blank=True)
    GACC_Type_2_IMTs = models.IntegerField(null=True, blank=True)
    GACC_NIMO_Teams = models.IntegerField(null=True, blank=True)
    GACC_Area_Command_Teams = models.IntegerField(null=True, blank=True)
    GACC_Fire_Use_Teams = models.CharField(max_length=30, null=True)
    Mang_Type = models.CharField(max_length=4, null=True)
    Mang_Name = models.CharField(max_length=4, null=True)
    Des_Tp = models.CharField(max_length=5, null=True)
    GAP_Sts = models.IntegerField(null=True)
    GAP_Prity = models.IntegerField(null=True)
    GDP = models.DecimalField( max_digits=10,decimal_places=3, null=True)
    GHM = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    MOD_NDVI_12m = models.CharField(max_length=71, null=True)
    MOD_EVI_12m = models.CharField(max_length=71, null=True)
    NDVI1day = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    NDVI_min = models.CharField(max_length=166, null=True)
    NDVI_max = models.CharField(max_length=143, null=True)
    NDVI_mean = models.CharField(max_length=164, null=True)
    Land_Cover_1km = models.CharField(max_length=27, null=True)
    Land_Cover = models.IntegerField(null=True)
    rpms = models.IntegerField(null=True)
    rpms_1km = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    NPL = models.IntegerField(null=True)
    Popo_1km = models.DecimalField( max_digits=10,decimal_places=4, null=True)
    Population = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    NAME = models.CharField(max_length=58, null=True)
    road_county_dis = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    road_interstate_dis = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    road_common_name_dis = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    road_other_dis = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    road_state_dis = models.DecimalField(max_digits=10,decimal_places=1, null=True)
    road_US_dis = models.CharField(max_length=30, null=True)
    SDI = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    TRACT = models.IntegerField(null=True)
    RPL_THEMES = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    RPL_THEME1 = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_POV = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_UNEMP = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_PCI = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_NOHSDP = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    RPL_THEME2 = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_AGE65 = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_AGE17 = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_DISABL = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_SNGPNT = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    RPL_THEME3 = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_MINRTY = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_LIMENG = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    RPL_THEME4 = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_MUNIT = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_MOBILE = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_CROWD = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_NOVEH = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    EPL_GROUPQ = models.DecimalField(max_digits=12,decimal_places=4, null=True)
    TPI_1km = models.DecimalField( max_digits=10,decimal_places=2, null=True)
    TPI = models.DecimalField(max_digits=10,decimal_places=3, null=True)
    TRI_1km = models.DecimalField(max_digits=10,decimal_places=3, null=True)
    TRI = models.DecimalField(max_digits=10,decimal_places=3, null=True)
    LatLong_State = models.CharField(max_length=15, null=True)
    LatLong_County = models.CharField(max_length=30, null=True)
    geometry = models.CharField(max_length=100, null=True)
    Land_cover = models.IntegerField(null=True)
    DF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    AF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    HDF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    DSF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    EBF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    EALR_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    EBLR_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    EPLR_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    HBF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    LLEF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    LIF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    LMI_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    MHVF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    PM25F_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    HSEF = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    P100_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    P200_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    LPF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    NPL_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    RMP_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    TSDF_PFS  = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    TPF = models.IntegerField(null=True)
    TF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    UF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    WF_PFS = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    M_WTR = models.BooleanField(null=True)
    M_WKFC = models.BooleanField(null=True)
    M_CLT = models.BooleanField(null=True)
    M_ENY = models.BooleanField(null=True)
    M_TRN = models.BooleanField(null=True)
    M_HSG = models.BooleanField(null=True)
    M_PLN = models.BooleanField(null=True)
    M_HLTH = models.BooleanField(null=True)
    SM_C = models.BooleanField(null=True)
    SM_PFS = models.BooleanField(null=True)
    EPLRLI = models.BooleanField(null=True)
    EALRLI = models.BooleanField(null=True)
    EBLRLI = models.BooleanField(null=True)
    PM25LI = models.BooleanField(null=True)
    EBLI = models.BooleanField(null=True)
    DPMLI = models.BooleanField(null=True)
    TPLI = models.BooleanField(null=True)
    LPMHVLI = models.BooleanField(null=True)
    HBLI = models.BooleanField(null=True)
    RMPLI = models.BooleanField(null=True)
    SFLI = models.BooleanField(null=True)
    HWLI = models.BooleanField(null=True)
    WDLI = models.BooleanField(null=True)
    DLI = models.BooleanField(null=True)
    ALI = models.BooleanField(null=True)
    HDLI = models.BooleanField(null=True)
    LLELI = models.BooleanField(null=True)
    LILHSE = models.BooleanField(null=True)
    PLHSE = models.BooleanField(null=True)
    LMILHSE = models.BooleanField(null=True)
    ULHSE = models.BooleanField(null=True)
    EPL_ET = models.BooleanField(null=True)
    EAL_ET = models.BooleanField(null=True)
    EBL_ET = models.BooleanField(null=True)
    EB_ET = models.BooleanField(null=True)
    PM25_ET = models.BooleanField(null=True)
    DS_ET = models.BooleanField(null=True)
    TP_ET = models.BooleanField(null=True)
    LPP_ET = models.BooleanField(null=True)
    HB_ET = models.BooleanField(null=True)
    RMP_ET = models.BooleanField(null=True)
    NPL_ET = models.BooleanField(null=True)
    TSDF_ET = models.BooleanField(null=True)
    WD_ET = models.BooleanField(null=True)
    DB_ET = models.BooleanField(null=True)
    A_ET = models.BooleanField(null=True)
    HD_ET = models.BooleanField(null=True)
    LLE_ET = models.BooleanField(null=True)
    UN_ET = models.BooleanField(null=True)
    LISO_ET = models.BooleanField(null=True)
    POV_ET = models.BooleanField(null=True)
    LMI_ET = models.BooleanField(null=True)
    IA_LMI_ET = models.BooleanField(null=True)
    IA_UN_ET = models.BooleanField(null=True)
    IA_POV_ET = models.BooleanField(null=True)
    TC = models.IntegerField(null=True)
    CC = models.IntegerField(null=True)
    IAULHSE = models.BooleanField(null=True)
    IAPLHSE = models.BooleanField(null=True)
    IALMILHSE = models.BooleanField(null=True)
    IALMIL_87 = models.CharField(max_length=30, null=True)
    IAPLHS_88 = models.CharField(max_length=30, null=True)
    IAULHS_89 = models.CharField(max_length=30, null=True)
    LHE = models.BooleanField(null=True)
    IALHE = models.BooleanField(null=True)
    IAHSEF = models.CharField(max_length=30, null=True)
    CA = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    NCA = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    CA_LT20 = models.BooleanField(null=True)
    M_CLT_EOMI = models.BooleanField(null=True)
    M_ENY_EOMI = models.BooleanField(null=True)
    M_TRN_EOMI = models.BooleanField(null=True)
    M_HSG_EOMI = models.BooleanField(null=True)
    M_PLN_EOMI = models.BooleanField(null=True)
    M_WTR_EOMI = models.BooleanField(null=True)
    M_HLTH_102 = models.BooleanField(null=True)
    M_WKFC_103 = models.BooleanField(null=True)
    FPL200S = models.BooleanField(null=True)
    M_WKFC_105 = models.BooleanField(null=True)
    M_EBSI = models.BooleanField(null=True)
    UI_EXP = models.CharField(max_length=6, null=True)
    THRHLD = models.IntegerField(null=True)
    def __str__(self):
        return str(self.FOD_ID)

    class Meta:
            managed = False
            db_table = 'FPA_FOD_PLUS'