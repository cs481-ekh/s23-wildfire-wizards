const url = "localhost:8000/s23-wildfire-wizards/api/distinct_counties_list/";
let tmp_url = "";

const possible_states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 
	'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 
	'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 
	'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 
	'VT','WA', 'WI', 'WV', 'WY']
	
describe("distinct_counties_list.cy.js", () => {
	it("should be visitable", () => {
		cy.visit(url);
	})	
	it("should be visitable via STATE query string", () => {
		possible_states.forEach((obj) => {
			cy.visit(url.concat("?STATE=", obj));
		})
	})
	it("COUNTY should not be null for each STATE", () => {
		possible_states.forEach((state) => {
			tmp_url = url.concat("?STATE=", state)
			cy.request({
				method: "GET",
				tmp_url,
			}).then((response) => {
				let distinct_counties = response.body;
				distinct_counties.forEach((county) => {
					expect(county).to.not.be.null;
				})
			})
		})
	})
	it("COUNTY should not be named null for each STATE", () => {
		possible_states.forEach((state) => {
			tmp_url = url.concat("?STATE=", state)
			cy.request({
				method: "GET",
				tmp_url,
			}).then((response) => {
				let distinct_counties = response.body;
				distinct_counties.forEach((county) => {
					expect(county.toLowerCase()).to.not.eql("null");
				})
			})
		})
	})
	it("COUNTY should not be named none for each STATE", () => {
		possible_states.forEach((state) => {
			tmp_url = url.concat("?STATE=", state)
			cy.request({
				method: "GET",
				tmp_url,
			}).then((response) => {
				let distinct_counties = response.body;
				distinct_counties.forEach((county) => {
					expect(county.toLowerCase()).to.not.eql("none");
				})
			})
		})
	})
	it("COUNTY should not be empty for each STATE", () => {
		possible_states.forEach((state) => {
			tmp_url = url.concat("?STATE=", state)
			cy.request({
				method: "GET",
				tmp_url,
			}).then((response) => {
				let distinct_counties = response.body;
				distinct_counties.forEach((county) => {
					expect(county).to.not.be.empty;
				})
			})
		})
	})
	it("COUNTY - each option should be unique for each STATE (case-sensitive)", () => {
		possible_states.forEach((state) => {
			tmp_url = url.concat("?STATE=", state)
			cy.request({
				method: "GET",
				tmp_url,
			}).then((response) => {
				let distinct_counties = response.body;
				distinct_counties.forEach((county) => {
					expect(Cypress._.uniq(county.toLowerCase()));
				})
			})
		})
	})
	it("COUNTY name should be string", () => {
		possible_states.forEach((state) => {
			tmp_url = url.concat("?STATE=", state)
			cy.request({
				method: "GET",
				tmp_url,
			}).then((response) => {
				let distinct_counties = response.body;
				distinct_counties.forEach((county) => {
					expect(county).to.match(/[\s\S]*/);
				})
			})
		})
	})
})