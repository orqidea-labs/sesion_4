describe("Pruebas E2E – Conversor de Temperatura", () => {

  it("Carga la página principal", () => {
    cy.visit("http://localhost:5001/react.html");
    cy.contains("Conversión de Temperaturas").should("be.visible");
  });

  it("Convierte de Celsius a Fahrenheit", () => {
    cy.visit("http://localhost:5001/react.html");

    cy.get("input[type='number']").type("100");

    cy.contains("Celsius → Fahrenheit").click();

    cy.contains("100°C equivalen a").should("be.visible");
  });

  it("Convierte de Fahrenheit a Celsius", () => {
    cy.visit("http://localhost:5001/react.html");

    cy.get("input[type='number']").type("212");

    cy.contains("Fahrenheit → Celsius").click();

    cy.contains("212°F equivalen a").should("be.visible");
  });

  it("Limpia los campos correctamente", () => {
    cy.visit("http://localhost:5001/react.html");

    cy.get("input[type='number']").type("50");
    cy.contains("Limpiar").click();

    cy.get("input[type='number']").should("have.value", "");
    cy.get("div[style]").last().should("contain", "");
  });

});
