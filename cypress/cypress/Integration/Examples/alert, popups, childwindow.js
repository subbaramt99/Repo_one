///*******************************Alerts************************************
describe('My Alerts test', function() {
    it('test with Alerts', function() {
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/')
        cy.get('#alertbtn').click()
        cy.wait(3)
        // Cypress will auto accept the alerts
        cy.get('#confirmbtn').click()
       
    })

} )
/*
///*******************************Dropdowns************************************

describe('My dropdowns test', function() {
    it('test with dropdowns', function() {
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/')
        // for dropdowns cypress have select mehtod to select static dropdown
        cy.get('select').select('option2').should('have.value', 'option2')
//**************Dynamic dropdown********************** 
        cy.get('#autocomplete').type('ind')
        cy.get('.ui-menu-item').each(($ele, index, $list) => {
            const country = $ele.text()
            cy.log(country)
            if(country === 'India'){
                cy.wrap($ele).click()
            }
        })
        cy.get('#autocomplete').should('have.value', 'India')
        
    })

} )

//**************Visible and Invisible of elements********************** 

describe('My visiblity test', function(){
    it('My visibility test', function() {
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/')
        cy.get('#show-textbox').click() // making the element visible
        cy.get('#displayed-text').should('be.visible')
        cy.get('#hide-textbox').click() // making the element invisible
        cy.get('#displayed-text').should('not.be.visible')

        // check the visibility of Radio buttons

        cy.get("[value = 'radio1']").check().should('be.checked')
    })
    
}) */

