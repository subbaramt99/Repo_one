//  <reference type = "cypress"/>

describe('My First Test', () => {
    it('Does not do much!', () => {
      expect(true).to.equal(true)
    })
  })

  describe('My First Test Suit', function(){
    it('My first testcase', function(){
      cy.visit('https://rahulshettyacademy.com/seleniumPractise/#/');  //cy is like driver in selenium
      cy.get('input.search-keyword').type('ca')
      cy.wait(2000)
      // visible is a function to get only visible elements
      cy.get('.product:visible').should('have.length', 4)  // should is assertion with passing number of element as '4'
      // Parent child chain , It will search in the "products" scope alone so it will not go to invisible items
      cy.get('.products').find('.product').should('have.length', 4)
      // selecting by index, "eq" is function to select by index
      cy.get('.products').find('.product').eq(1).contains('ADD TO CART').click()
        // selecting the element by travers the list of element by "each" function 
      cy.get('.products').find('.product').each(($el, index, $list) => {
        const vegName= $el.find('h4.product-name').text()
        if(vegName.includes("Cashews"))
            {
                //$el.contains('ADD TO CART').click()
                //$el.find('.product-action > button').click() --> on find method click operation is not passed
                cy.wrap($el).find('.product-action > button').click()
                
            }
        else
        {
            cy.log("Product is not found")
        }
    
    })


    }) 
    //it('My second test case', function(){})
  } )