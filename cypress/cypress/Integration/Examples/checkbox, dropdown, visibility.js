///*******************************Check boxes************************************
describe('My check boxes test', function() {
    it('test with check boxes', function() {
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/')
        // check is the method to check similer to click
        // should method we can assert with tproperty ('have.text') and behaviour ('be.checked')
        // and to assert the method Assertions are automatically retried as part of the previous command until they pass or time out.
        cy.get('#checkBoxOption1').check().should('be.checked').and('have.value', 'option1')
        // be is behaviour level of assertion
        cy.get('#checkBoxOption1').uncheck().should('not.be.checked').and('have.value', 'option1')

        cy.get('input[type="checkbox"]').check(['option1', 'option2'])
    })

} )

///*******************************Dropdowns************************************

describe('My dropdowns test', function() {
    it('test with dropdowns', function() {
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/')
        // for dropdowns cypress have select mehtod to select static dropdown
        cy.get('select').select('option2').should('have.value', 'option2')
//**************Dynamic dropdown********************** */
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

//**************Visible and Invisible of elements********************** */

describe('My visiblity test', function(){
    it('test with visibility', function() {
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/')
        cy.get('#show-textbox').click() // making the element visible
        cy.get('#displayed-text').should('be.visible')
        cy.get('#hide-textbox').click() // making the element invisible
        cy.get('#displayed-text').should('not.be.visible')

        // check the visibility of Radio buttons

        cy.get("[value = 'radio1']").check().should('be.checked')
    })
    
})

