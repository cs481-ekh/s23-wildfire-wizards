/// <reference types="cypress" />

const url = "http://localhost:8000/f23-wildfire-wizards/api/subset_csv/?FIRE_YEAR=2018&DISCOVERY_DOY__gte=1&DISCOVERY_DOY__lte=366&STATE=AK&CATEGORIES=FPA_FOD";

describe("API test suite for the endpoint handling csv conversion", () => {
  const filename = "export.csv";

  it("csv should be returned with a GET request to /csv", () => {
    cy.request({
      method: "GET",
      url,
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.headers?.["content-type"]).to.eq("text/csv");
      expect(response.headers?.["content-disposition"]).to.contain(
        `filename="${filename}`
      );
      expect(response.body).to.be.a("string");
    });
  });
});
