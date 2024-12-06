describe('My Alias Test', () => {
    it('test with alias', () => {
        cy.visit('https://rahulshettyacademy.com/seleniumPractise/#/');  //cy is like driver in selenium
        cy.get('input.search-keyword').type('ca')
        cy.wait(2000)

        cy.get('.product:visible').should('have.length', 4)
        cy.get('.products').find('.product').should('have.length', 4)
        // Instead of using cy.get('.products') every time we can assign it to varialble called Alias
        cy.get('.products').as('ProductLocator') //--> as is keyword of alias "ProductLocator" is varaiable name
        // we can use any where the ProductLocator Alias
        cy.get('@ProductLocator').find('.product').eq(1).contains('ADD TO CART').click()
        
    //**********************************Console Log***********************************
        console.log('logs') // it will print the logs in browser console tab

    // This will printing the logs
        cy.get('.brand').then(function(logelement){
            cy.log("The brand is", logelement.text())
        })
    // asset the log text
        cy.get('.brand').should('have.text', 'GREENKART')
    })
  })