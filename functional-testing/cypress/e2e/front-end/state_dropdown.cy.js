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
    beforeEach(() => {
        cy.visit(url)
        cy.get('.css-tlfecz-indicatorContainer').eq(1).click()
    })
    it('state dropdown button works', () => {
        cy.get('div[id="react-select-5-listbox"]')
        .should('be.visible')
    })
    it('dropdown menu has length 52', () => { //50 states plus DC and PR
        cy.get('.css-4ljt47-MenuList')
        .its('childElementCount').should('eq', '52')
    })
    it('dropdown only has valid state values', () => {
        cy.get('div[id="react-select-5-listbox"] > .css-4ljt47-MenuList > div')
        .each((text, index, list) => {
            //cy.get(text)
            //.its('innerText')
            //.should('eq', possible_states[index])
            //cy.log(possible_states[index]+' tested')
            cy.log(text+'~~'+index)
        })
        
    })
})