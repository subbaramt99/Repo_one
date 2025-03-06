import { number } from "assert-plus"

describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://example.cypress.io')
  })
  it('Does not do much!', () => {
    expect(true).to.equal(true)
  })
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
    
//************************Looping and traverse from one by one element**************************** */
    cy.get('.products').find('.product').each(($el, index, $list) => {
    const vegName= $el.find('h4.product-name').text()
    cy.log(vegName) // Printing the vegetables name as log
    if(vegName.includes("Cashews - 1 Kg"))
          {
              //$el.contains('ADD TO CART').click()
              //$el.find('.product-action > button').click() --> on find method click operation is not passed
              cy.wrap($el).find('.product-action > button').click()
          }
    else
      {
          cy.log("Product is not found") // Print the log in cypress console
      }
      
  })

  // Trying to print text of logo button
      //const logo = cy.get('.brand').text() --> it will not work as the cypress behaviour unable to assign to a variable
    
    cy.get('.brand').then(function(logo)
    {
      cy.log(logo.text()) // As text is not cypress commend, but it supports as is JQuerry (Cy always suppoert jQuery)
    })

    cy.get('.cart-icon > img').click()
    cy.contains('PROCEED TO CHECKOUT').click()
    cy.contains('Place Order').click()

    //cy.url.should('includes', 'anyTEXT in url') // --> it'll get the Url of the open window

  }) 

  it('My test with calender', ()=>{

    const month = "6";
    const date = "15";
    const year = "2027";
    const expectedlist = [month,date,year]
    cy.visit('https://rahulshettyacademy.com/seleniumPractise/#/offers')
    cy.get('.react-date-picker__inputGroup').click()
    cy.get('.react-calendar__navigation__label').click()
    cy.get('.react-calendar__navigation__label').click()

    cy.contains('button', year).click()


    //it get all the elements and type casting the month as string from number and click
    cy.get("button[class='react-calendar__tile react-calendar__year-view__months__month']").eq(Number(month)-1).click()
   
    // it will get the path and check the 'abbr' attribute has value of 'date'
    cy.get("button[class='react-calendar__tile react-calendar__month-view__days__day']").contains('abbr', date).click()
    
    
    //Assertion

    //Taking the date elements iterate to each ele and invoking the value attr and asserting it with expected date 
    cy.get("input[inputmode='numeric']").each(($el, index) =>{
      const dt = cy.wrap($el).invoke('val').should('eq', expectedlist[index])
      //cy.log(dt)
    })

  })

  it.only('My E2E test', ()=>{

    const ProductName = 'Nokia Edge'
    cy.visit('https://rahulshettyacademy.com/loginpagePractise/#')
    cy.get('#username').type('rahulshettyacademy')
    cy.get('#password').type('learning')
    cy.get('#terms').click()
    cy.get('#signInBtn').click()
    cy.contains("Shop Name").should('be.visible')

    cy.get("app-card[class = 'col-lg-3 col-md-6 mb-3']").should('have.length', 4)

    cy.get("app-card[class = 'col-lg-3 col-md-6 mb-3']").filter(`:contains("${ProductName}")`)
      .then($el => {
        cy.wrap($el).should('have.length', 1)
        cy.wrap($el).contains('button', 'Add ').click()
      })

    cy.get("app-card[class = 'col-lg-3 col-md-6 mb-3']").eq(0).contains('button', 'Add ').click()
    cy.contains('a', "Checkout").click()

    }) 
    
})
