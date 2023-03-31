/**
 * State Dropdown Menu Test Suite
 */

/// <reference types="cypress" />

import { elements } from "../../fixtures/data-cy.json";
const url = "http://localhost:3000/f23-wildfire-wizards/Data";

const possible_states = [
	'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE','FL', 'GA', 'HI',
	'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD','ME','MI', 'MN', 
	'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH',
	'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT',
	'WA', 'WI', 'WV', 'WY'
	] // 50 states + DC and PR in alphabetical order by code

describe('State Dropdown Menu', () => { //test suite name
    beforeEach(() => { //refreshes page and selects state dropdown
        cy.visit(url)
        cy.get('.css-tlfecz-indicatorContainer').eq(1).click()
    })
    it('state dropdown button works', () => {
        cy.get('div[id="react-select-5-listbox"]')
        .should('be.visible') //checks state dropdown is visible
    })
    it('dropdown menu has length 52', () => { //50 states plus DC and PR
        cy.get('div[id="react-select-5-listbox"] > .css-4ljt47-MenuList > div')
        .each(($div, index, $lis) => {
            /*This is probably not the optimal way of doing this but is the
              only way I could make it work. It just checks the length of 
              the array returned by the each method. */
            expect($lis).to.have.length(52)
        })
    })
    it('dropdown only has valid state values', () => {
        cy.get('div[id="react-select-5-listbox"] > .css-4ljt47-MenuList > div')
        .each(($div, index, $lis) => {
            expect($div.html()).equal(possible_states[index]) //check value in dropdown aligns with value in states array
        })   
    })
})