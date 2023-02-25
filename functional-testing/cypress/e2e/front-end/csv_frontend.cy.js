/**
 * CSV Download button test suite
 */
/// <reference types="cypress" />

import { elements } from "../../fixtures/data-cy.json";
const url = "http://localhost:3000/f22-fires-wild/Data";
const django_url = "http://localhost:8000/f22-fires-wild/api/subset_csv/";

const idahoString = "400308148,W-720453,FED,DOI-WFMI,BLM,USIDBOD,Boise District,IDBPD,Boise District,651.0,,L146,OTR 3,,,,,,2018,2018-04-13,103,1553.0,Human,Firearms and explosives use,,4/13/2018 0:00:00,103.0,1553.0,0.1,A,43.2431,-116.0436,BLM,ID,Ada,16001.0,Ada County,Idaho,Ada,2.0,FED,BLM,NCA,2.0,8.0,330(16%) / 329(15%) / 331(14%),9307(62%) / 7123(23%) / 7080(7%),9336.0,222.0,202.0,302(86%) / 208(5%) / 63(3%),Snake River Plain,'0.33' '0.29' '0.28' '0.24' '0.22' '0.24' '0.23' '0.26' '0.38' '0.46','0.18' '0.14' '0.13' '0.14' '0.13' '0.15' '0.15' '0.17' '0.24' '0.29',52.0,71(97%) / 52(1%) / 21(1%),558,836.2818847818847,0.0,0.0,24883.0,9.0,10.0,0.0,12.0,SACC,2.0,426.0,14.0,10.0,0.0,0.0,0.0,0.0,,41841.418,0.89,274.5,289.20001220703125,29.8,85.8,0.004,231.0,13.9,16.5,25.200000762939453,0.7,32.599998474121094,0.04,0.18,0.04,0.08,0.08,0.7,0.95,0.21,0.19,0.45,0.73,0.11,0.69,0.21,0.03,0.16,0.12,0.06,0.15,0.69,0.48,4512.0,0.34,0.52,0.54,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,,,,0.0,0.0,,0.07,0.92,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,Nation,21.0,,,,9.0,4(99%) / 3(1%) / 132(0%),4.0,1.569,3.0,-1.0,761.797520661157,963.0,2.0,0.509641873278237,-0.1136363636363636,0.11,-0.0,-0.125,10503.0,0.3165,0.1605,0.1015,0.4219,0.2977,0.0691,0.2561,0.113,0.9313,0.2474,0.3431,0.5762,0.4399,0.6611,0.5368,0.7519,0.7653,0.0,0.5118,0.3791,,,33.1,,,,12h,12.0,10.1.8,10.1,10.0,0.09,1954.0,256.0,284.0,0.13,,0.0,275.8999938964844,286.1000061035156,32.400001525878906,71.5,0.0035999999381601,5.3,308.0,227.8000030517578,5.0,13.6,17.2,36.0,0.59,34.0,1.46,276.94,288.44,32.8,77.9,0.0042580003,5.36,174.8,229.12003,5.1,13.8,17.2,12.4,0.67,27.8,0.0,2.7,279.4,293.4,27.6,66.700005,0.0034299998,10.0,308.0,238.2,6.6,12.2,16.7,36.0,0.92,37.0,>90%,>90%,30-50%,50-70%,50-70%,50-70%,30-50%,50-70%,'0.01' '0.0' '-0.01' '-0.02' '-0.0' '0.02' '0.01' '0.04' '0.1' '0.0' '0.01' '0.0','0.41' '0.37' '0.29' '0.26' '0.28' '0.25' '0.27' '0.32' '0.32' '0.34' '0.52' '0.59','0.22' '0.18' '0.11' '0.08' '0.11' '0.19' '0.2' '0.22' '0.26' '0.23' '0.33' '0.3',0.07"

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
          expect(response.body).to.contain(idahoString);
        })
      });
})