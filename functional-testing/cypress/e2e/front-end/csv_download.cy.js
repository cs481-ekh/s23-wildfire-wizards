/**
 * CSV Download button test suite
 */
/// <reference types="cypress" />

import { elements } from "../../fixtures/data-cy.json";
const url = "http://localhost:3000/f22-fires-wild/Data";

describe('CSV Download', () => {
    beforeEach(() => {
        cy.visit(url)
        cy.get('.css-1hb7zxy-IndicatorsContainer').eq(1).click() //year dropdown
        cy.get('div[id="react-select-3-listbox"] > .css-4ljt47-MenuList > div[id="react-select-3-option-0"]').click(); //select first year, should be 2018
    })
    it('csv dowload button returns a csv file', () => {
        cy.get('.css-tlfecz-indicatorContainer').eq(1).click()
        cy.get('div[id="react-select-5-listbox"] > .css-4ljt47-MenuList > div[id="react-select-5-option-13"]').click();
        cy.get('.css-sghohy-MuiButtonBase-root-MuiButton-root').eq(0).click()
        cy.get('.css-sghohy-MuiButtonBase-root-MuiButton-root').eq(1).click()
        cy.verifyDownload('export.csv');
    })
})