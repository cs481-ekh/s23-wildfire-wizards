/**
 * CSV Download button test suite
 */
/// <reference types="cypress" />

import { elements } from "../../fixtures/data-cy.json";
const url = "http://localhost:3000/f22-fires-wild/Data";
const django_url = "http://localhost:8000/f22-fires-wild/api/subset_csv/?FIRE_YEAR=2018&DISCOVERY_DOY__gte=1&DISCOVERY_DOY__lte=366&STATE=AK&CATEGORIES=FPA_FOD";

/*
const idahoString0 = "400308148,W-720453,FED,DOI-WFMI,BLM,USIDBOD,Boise District,IDBPD,Boise District,651.0,,L146,OTR 3,,,,,,2018,2018-04-13,103,1553.0,"
const idahoString1 = "Human,Firearms and explosives use,,4/13/2018 0:00:00,103.0,1553.0,0.1,A,43.2431,-116.0436,BLM,ID,Ada,16001.0,Ada County,Idaho,Ada,2.0,FED,BLM,NCA,2.0,8.0,"
const idahoString2 = "330(16%) / 329(15%) / 331(14%),9307(62%) / 7123(23%) / 7080(7%),9336.0,222.0,202.0,302(86%) / 208(5%) / 63(3%),Snake River Plain,"
const idahoString3 = "'0.33' '0.29' '0.28' '0.24' '0.22' '0.24' '0.23' '0.26' '0.38' '0.46','0.18' '0.14' '0.13' '0.14' '0.13' '0.15' '0.15' '0.17' '0.24' '0.29',52.0,71(97%) / 52(1%) / 21(1%),"
const idahoString4 = "558,836.2818847818847,0.0,0.0,24883.0,9.0,10.0,0.0,12.0,SACC,2.0,426.0,14.0,10.0,0.0,0.0,0.0,0.0,,41841.418,0.89,274.5,289.20001220703125,29.8,85.8,0.004,231.0,13.9,16.5,"
const idahoString5 = "25.200000762939453,0.7,32.599998474121094,0.04,0.18,0.04,0.08,0.08,0.7,0.95,0.21,0.19,0.45,0.73,0.11,0.69,0.21,0.03,0.16,0.12,0.06,0.15,0.69,0.48,4512.0,0.34,0.52,0.54,0.0,0.0,"
const idahoString6 = "0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,"
const idahoString7 = "0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,,,,0.0,0.0,,0.07,0.92,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,Nation,21.0,,,,9.0,4(99%) / 3(1%) / 132(0%),4.0,1.569,3.0,"
const idahoString8 = "-1.0,761.797520661157,963.0,2.0,0.509641873278237,-0.1136363636363636,0.11,-0.0,-0.125,10503.0,0.3165,0.1605,0.1015,0.4219,0.2977,0.0691,0.2561,0.113,0.9313,0.2474,0.3431,0.5762,0.4399,"
const idahoString9 = "0.6611,0.5368,0.7519,0.7653,0.0,0.5118,0.3791,,,33.1,,,,12h,12.0,10.1.8,10.1,10.0,0.09,1954.0,256.0,284.0,0.13,,0.0,275.8999938964844,286.1000061035156,32.400001525878906,71.5,"
const idahoString10 = "0.0035999999381601,5.3,308.0,227.8000030517578,5.0,13.6,17.2,36.0,0.59,34.0,1.46,276.94,288.44,32.8,77.9,0.0042580003,5.36,174.8,229.12003,5.1,13.8,17.2,12.4,0.67,27.8,0.0,2.7,279.4,"
const idahoString11 = "293.4,27.6,66.700005,0.0034299998,10.0,308.0,238.2,6.6,12.2,16.7,36.0,0.92,37.0,>90%,>90%,30-50%,50-70%,50-70%,50-70%,30-50%,50-70%,"
const idahoString12 = "'0.01' '0.0' '-0.01' '-0.02' '-0.0' '0.02' '0.01' '0.04' '0.1' '0.0' '0.01' '0.0','0.41' '0.37' '0.29' '0.26' '0.28' '0.25' '0.27' '0.32' '0.32' '0.34' '0.52' '0.59','0.22' '0.18' '0.11' '0.08' '0.11' '0.19' '0.2' '0.22' '0.26' '0.23' '0.33' '0.3',0.07"

const alaskaString = "400381951,SFO-2018AKFAS811423,NONFED,ST-NASF,ST/C&L,USAKFAS,Fairbanks Area,AKFAS,Fairbanks Area Forestry,,811423,,TWO RIVERS LOGGING ROAD,,,,,,2018,2018-10-16,289,,Human,Debris and open burning,,10/13/2100 0:00:00,286.0,,0.1,A,64.9104,-147.06835,STATE,AK,,,,Alaska,Fairbanks North Star,1.0,,,,,,,,,,,,,'0.64' '0.83' '0.82' '0.8' '0.42' '0.12' '0.0' '-0.03' '-0.01' '0.6','0.27' '0.41' '0.45' '0.4' '0.19' '0.11' '0.0' '-0.03' '-0.01' '0.21',0.0,,0,0.0,0.0085,0.0085,75535.0,0.0,0.0,0.0,0.0,RMCC,1.0,3.0,0.0,0.0,0.0,0.0,0.0,0.0,,58023.367,,,,,,,,,,,,,0.07,0.46,0.13,0.0,0.61,0.34,0.01,0.0,0.31,0.23,0.12,0.37,0.64,,0.03,0.26,0.18,0.1,0.48,0.09,0.13,10918.0,0.06,0.8,,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,,,,0.0,0.0,,0.05,0.94,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,Nation,21.0,,,,14.0,,32767.0,,,32767.0,0.0,32767.0,32767.0,0.0,0.0,0.1,,,1900.0,0.2591,0.3052,0.1942,0.8068,0.1832,0.1601,0.1318,0.2885,0.3164,0.5224,0.2332,0.1186,0.2743,0.0,0.6559,0.2726,0.7033,0.94,0.0,0.7594,,,62.3,,,,,,,,,,0.0,0.0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'0.0' '-0.0' '0.02' '0.03' '-0.05' '-0.02' '-0.01' '-0.02' '-0.11' 'nan' '-0.2' '-0.02','0.71' '0.74' '1.3' '1.16' '0.77' '0.31' '0.23' '0.18' '0.09' 'nan' '0.04' '0.85','0.25' '0.2' '0.59' '0.61' '0.29' '0.12' '0.1' '0.07' '-0.02' 'nan' '-0.03' '0.13',1.23"

const floridaString0 = "400332717,SFO-2018FLFLS2018080228,NONFED,ST-NASF,ST/C&L,USFLFLS,Florida Forest Service,FLFLS,Florida Forest Service,,2018080228,,NE 103RD TERR(38),,,,,,2018,2018-05-01,121,1530.0,Human,Recreation and ceremony,,5/1/2018 0:00:00,121.0,1732.0,4.0,B,29.4091,-82.6002,PRIVATE,FL,Levy,12075.0,Levy County,2.0,UNK,UNK,UNK,4.0,0.0,17(13%) / 25(11%) / 22(11%),7997(22%) / 7919(13%) / 7299(11%),7299.0,25.0,25.0,310(20%) / 17(13%) / 25(11%),Florida Flatwoods/Okefenokee Swamp and Plains,'0.6' '0.54' '0.55' '0.58' '0.59' '0.66' '0.73' '0.72' '0.63' '0.57','0.38' '0.31' '0.31' '0.29' '0.32' '0.34' '0.44' '0.44' '0.44' '0.4',23.0,21(29%) / 81(28%) / 22(14%),0.4963,0.3335,33026.0,0.0,0.0,0.0,0.0,SACC,2.0,47.0,1.0,1.0,1.0,0.0,0.0,0.0,,50122.594,2.16,288.29998779296875,302.70001220703125,37.5,92.6,0.0108,285.0,14.8,16.3,23.200000762939453,1.23,32.29999923706055,0.78,0.52,0.86,0.1,0.75,0.55,0.76,0.35,0.37,0.85,0.47,0.76,0.14,0.24,0.17,0.52,0.8,0.13,0.26,0.04,0.05,8508.0,0.12,0.72,,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,,,,1.0,0.0,,0.06,0.93,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,Nation,21.0,,1.0,4.0,21.0,1(100%),1.0,2.365,2.646,-1.0,21.356749311294767,30.0,2.0,1.0273186409550046,13.11317722681359,0.41,0.0,-0.625,970102.0,0.7638,0.748,0.5565,0.6284,0.837,0.7635,0.8411,0.758,0.4713,0.8647,0.4921,0.4633,0.386,0.5286,0.6846,0.3217,0.9981,0.498,0.1722,0.7502,,,,,,12.0,75c,75.0,8.5.3,8.5,8.0,0.04,2027.0,2003.0,295.0,0.99,,0.0,286.5,302.79998779296875,35.20000076293945,100.0,0.0102699995040893,4.4,107.0,329.5,8.0,13.2,15.0,36.0,1.18,40.0,0.0,287.48,302.91998,32.1,89.9,0.009438,3.94,140.0,313.56,8.04,12.8,15.1,34.2,1.38,40.4,0.0,0.0,289.7,304.1,26.2,68.1,0.00835,4.9,300.0,334.7,8.4,11.5,15.0,39.0,1.83,42.0,>90%,>90%,30-50%,70-90%,10-30%,>90%,30-50%,70-90%,'-0.0' '-0.01' '0.0' '-0.0' '-0.02' '0.02' '0.02' '-0.0' '-0.02' '-0.01' '0.0' '-0.0','0.64' '0.57' '0.54' '0.57' '0.59' '0.61' '0.66' '0.73' '1.07' '0.64' '0.73' '0.64','0.34' '0.34' '0.23' '0.31' '0.32' '0.44' '0.35' '0.32' '0.32' '0.21' '0.25' '0.43',0.32"
const floridaString1 = "400344220,SFO-2018FLFLS2018170172,NONFED,ST-NASF,ST/C&L,USFLFLS,Florida Forest Service,FLFLS,Florida Forest Service,,2018170172,,HAMILTON AVE (36),,,,,,2018,2018-05-02,122,1137.0,Human,Debris and open burning,,5/2/2018 0:00:00,122.0,1232.0,0.3,B,26.7127,-81.6178,PRIVATE,FL,Lee,12071.0,Lee County,2.0,UNK,UNK,UNK,4.0,0.0,25(12%) / 355(11%) / 11(8%),7997(13%) / 7299(12%) / 7446(9%),7916.0,14.0,14.0,25(12%) / 303(11%) / 310(10%),Florida Flatwoods/Okefenokee Swamp and Plains,'0.6' '0.6' '0.62' '0.66' '0.69' '0.71' '0.72' '0.73' '0.66' '0.58','0.34' '0.34' '0.34' '0.37' '0.41' '0.4' '0.5' '0.5' '0.44' '0.41',21.0,90(27%) / 21(18%) / 81(17%),0.8523,0.1104,33494.0,0.0,0.0,0.0,0.0,SACC,3.0,71.0,3.0,1.0,1.0,1.0,0.0,0.0,,50122.594,2.12,290.29998779296875,304.6000061035156,39.3,98.5,0.0129,285.0,16.3,17.7,18.39999961853028,1.23,26.39999961853028,0.69,0.22,0.84,0.18,0.21,0.9,0.96,0.45,0.02,,0.49,0.08,0.72,0.2,0.11,0.34,0.25,0.36,0.03,0.54,0.06,3070.0,0.27,0.29,,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,,,,1.0,0.0,,0.06,0.93,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,Nation,21.0,,1.0,8.0,45.0,1(49%) / 2(18%) / 5(17%),1.0,0.924,2.0,-1.0,2.337995337995338,4.0,0.0,-0.3505827505827505,-0.3666666666666666,0.58,-0.0,0.5,30300.0,0.4214,0.251,0.2654,0.1943,0.1936,0.5248,0.4336,0.9602,0.0548,0.7101,0.2017,0.5832,0.4045,0.7085,0.5717,0.0,0.8522,0.2418,0.5314,0.8588,,,8.4,,,,75b,75.0,8.5.3,8.5,8.0,0.1,2040.0,1375.0,297.0,0.67,,0.0,288.79998779296875,304.1000061035156,40.79999923706055,100.0,0.0128999995067715,5.7,100.0,235.5,7.2,14.7,15.8,39.0,1.03,35.0,0.16,289.54,304.5,35.7,96.0,0.011782,4.92,103.0,275.58002,8.2,14.1,15.8,30.0,1.32,34.2,0.0,0.8,291.1,305.3,27.6,79.8,0.010129999,5.7,114.0,361.6,10.4,13.2,15.8,39.0,1.79,38.0,>90%,>90%,30-50%,>90%,<10%,>90%,20-30%,>90%,'0.06' '-0.0' '0.04' '0.01' '0.02' '-0.0' '-0.01' '-0.01' '0.02' '-0.02' '-0.02' '0.08','0.65' '0.66' '0.62' '0.64' '0.68' '0.72' '0.75' '0.72' '0.78' '0.78' '0.69' '0.68','0.42' '0.45' '0.3' '0.32' '0.45' '0.43' '0.36' '0.34' '0.35' '0.27' '0.24' '0.44',0.35"
const floridaString2 = "400344301,SFO-2018FLFLS2018040422,NONFED,ST-NASF,ST/C&L,USFLFLS,Florida Forest Service,FLFLS,Florida Forest Service,,2018040422,,ATWATER RD FIRE *NOV* (20)-0422,,,,,,2018,2018-05-02,122,1630.0,Human,Debris and open burning,,5/2/2018 0:00:00,122.0,1807.0,1.0,B,30.689,-84.7352,PRIVATE,FL,Gadsden,12039.0,Gadsden County,2.0,UNK,UNK,UNK,4.0,0.0,25(6%) / 64(6%) / 145(4%),9322(26%) / 7330(12%) / 9321(11%),7330.0,177.0,118.0,118(11%) / 116(10%) / 115(10%),\"Atlantic Southern Loam Plains, Sand Hills, and Red Uplands\",'0.73' '0.65' '0.65' '0.69' '0.74' '0.77' '0.83' '0.79' '0.78' '0.75','0.44' '0.29' '0.32' '0.32' '0.36' '0.38' '0.45' '0.53' '0.49' '0.47',42.0,42(46%) / 90(13%) / 82(12%),0.2604,0.189,33452.0,0.0,0.0,0.0,0.0,SACC,3.0,71.0,3.0,1.0,1.0,1.0,0.0,0.0,,50122.594,3.25,287.5,301.5,39.8,91.7,0.0103,282.0,15.1,17.4,20.700000762939453,1.14,29.299999237060547,0.95,0.75,0.93,0.19,0.83,0.92,0.96,0.75,0.62,0.83,0.49,0.8,0.05,0.65,0.24,0.88,0.87,0.57,0.3,0.04,0.03,4808.0,0.16,0.9,0.93,1.0,1.0,1.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,0.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,0.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,0.0,1.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,6.0,4.0,0.0,0.0,0.0,,,,1.0,0.0,,0.03,0.96,1.0,1.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,Nation,21.0,,1.0,9.0,31.0,1(92%) / 3(6%) / 5(2%),1.0,3.78,8.775,201.0,65.3911421911422,75.0,7.0,1.843589743589744,61.95034965034965,0.33,0.0,0.125,20400.0,0.9586,0.9525,0.9347,0.8917,0.8984,0.8886,0.8529,0.5816,0.1654,0.9946,0.8702,0.6745,0.739,0.5416,0.9235,0.2956,0.9081,0.4815,0.7975,0.9746,,,3.9,,,,65h,65.0,8.3.5,8.3,8.0,0.25,1755.0,1944.0,293.0,1.11,,0.0,287.0,302.8999938964844,36.0,100.0,0.010420000180602,3.0,61.0,318.3999938964844,7.1,13.0,16.2,29.0,1.21,37.0,0.0,287.46002,302.8,32.2,88.1,0.009384001,2.94,89.8,318.76,7.48,12.4,16.1,29.4,1.39,38.4,0.0,0.0,289.8,303.9,29.6,78.700005,0.0079499995,3.6,154.0,333.6,8.1,12.1,15.9,32.0,1.47,39.0,>90%,>90%,30-50%,30-50%,10-30%,70-90%,50-70%,70-90%,'0.0' '-0.01' '-0.01' '-0.01' '-0.0' '0.01' '-0.03' '-0.02' '-0.01' '-0.01' '-0.01' '-0.01','0.79' '0.71' '0.65' '0.69' '0.7' '0.76' '0.79' '0.87' '1.7' '0.86' '0.77' '0.8','0.49' '0.47' '0.25' '0.46' '0.39' '0.53' '0.45' '0.4' '0.44' '0.39' '0.28' '0.48',0.78"
*/

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
      cy.request({
        method: "GET",
        url: django_url,
      }).then((response) => {
        expect(response.status).to.eq(200);
        expect(response.headers?.["content-type"]).to.eq("text/csv");
        expect(response.headers?.["content-disposition"]).to.contain(`filename="export.csv"`);
        expect(response.body).to.be.a("string");
      });
    })
    /*
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
        expect(response.headers?.["content-disposition"]).to.contain(`filename="export.csv"`);
        expect(response.body).to.be.a("string");
        expect(response.body.includes(idahoString0)).to.be.true
        expect(response.body.includes(idahoString1)).to.be.true
        expect(response.body.includes(idahoString2)).to.be.true
        expect(response.body.includes(idahoString3)).to.be.true
        expect(response.body.includes(idahoString4)).to.be.true
        expect(response.body.includes(idahoString5)).to.be.true
        expect(response.body.includes(idahoString6)).to.be.true
        expect(response.body.includes(idahoString7)).to.be.true
        expect(response.body.includes(idahoString8)).to.be.true
        expect(response.body.includes(idahoString9)).to.be.true
        expect(response.body.includes(idahoString10)).to.be.true
        expect(response.body.includes(idahoString11)).to.be.true
        expect(response.body.includes(idahoString12)).to.be.true
      })
    });
    it("alaska csv is correct", () => {
      cy.get('.css-1hb7zxy-IndicatorsContainer').eq(1).click()
      cy.get('div[id="react-select-5-listbox"] >> div[id="react-select-5-option-0"]').click();
      cy.get('.css-sghohy-MuiButtonBase-root-MuiButton-root').eq(0).click()
      cy.request({
        method: 'GET',
        url: django_url,
      }).then((response) => {
        expect(response.status).to.eq(200);
        expect(response.headers?.["content-type"]).to.eq("text/csv");
        expect(response.headers?.["content-disposition"]).to.contain(`filename="export.csv"`);
        expect(response.body).to.be.a("string");
        expect(response.body.includes(alaskaString)).to.be.true
      })
    });
    it("florida csv is correct", () => {
      cy.get('.css-1hb7zxy-IndicatorsContainer').eq(1).click()
      cy.get('div[id="react-select-5-listbox"] >> div[id="react-select-5-option-9"]').click();
      cy.get('.css-sghohy-MuiButtonBase-root-MuiButton-root').eq(0).click()
      cy.request({
        method: 'GET',
        url: django_url,
      }).then((response) => {
        expect(response.status).to.eq(200);
        expect(response.headers?.["content-type"]).to.eq("text/csv");
        expect(response.headers?.["content-disposition"]).to.contain(`filename="export.csv"`);
        expect(response.body).to.be.a("string");
        expect(response.body.includes(floridaString0)).to.be.true
        expect(response.body.includes(floridaString1)).to.be.true
        expect(response.body.includes(floridaString2)).to.be.true
      })
    });
    */
})