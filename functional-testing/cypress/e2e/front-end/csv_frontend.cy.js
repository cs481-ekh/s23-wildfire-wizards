/**
 * CSV Download button test suite
 */
/// <reference types="cypress" />

import { elements } from "../../fixtures/data-cy.json";
const url = "http://localhost:3000/f22-fires-wild/Data";
const django_url = "http://localhost:8000/f22-fires-wild/api/subset_csv/";

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
})