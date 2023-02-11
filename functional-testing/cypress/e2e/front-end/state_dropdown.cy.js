/// <reference types="cypress" />

import { elements } from "../../fixtures/data-cy.json";
const url = "http://localhost:3000/f22-fires-wild/Data";

const possible_states = [
	'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE','FL', 'GA', 'HI',
	'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD','ME','MI', 'MN', 
	'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH',
	'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT',
	'WA', 'WI', 'WV', 'WY'
	]

describe('State Dropdown Menu', () => {
    it('data page loads', () => {
        cy.visit(url)
    })
    it('state dropdown button works', () => {
        cy.get('.css-tlfecz-indicatorContainer').eq(1)
        .should('be.visible')
        .click()
        cy.get('div[id="react-select-5-listbox"]')
        .should('be.visible')
    })
    it('dropdown menu has length 52', () => { //50 states plus DC and PR
        cy.get('.css-tlfecz-indicatorContainer').eq(1).click()
        cy.get('div[id="react-select-5-listbox"]')
        .get('.css-4ljt47-MenuList')
        .its('childElementCount').should('eq', '52')
    })
    var i=0;
    for (i=0; i<52; i++){
        it('dropdown menu has correct value '+i+' ('+possible_states[i]+')', () => {
            cy.get('.css-tlfecz-indicatorContainer').eq(1).click()
            cy.get('div[id="react-select-11-option-'+i+'"]')
            .its('textContent').should('eq', possible_states[i]);
        })
    }   
})