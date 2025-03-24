import 'cypress-iframe'  // for handeling frame need to import 'cypress-iframe' package from npm
import 'cypress-xpath'  // Importing xpath


describe('My iFrames test', function() {
    it('test with iFrames', function() {
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/')
        cy.wait(10)
        cy.frameLoaded('#courses-iframe') // To identify the frames nee dto use frameLoaded method and we passing the frame ID

        cy.iframe().find("a[href*='mentorship']").eq(0).click()

        //cy.iframe().xpath("//a[@href='mentorship']").eq(0).click() // using Xpath to locate the elements

        //cy.iframe().find("h1[class*='pricing-title text-white ls-1']").should('have.length',2)
        cy.iframe().get("h1[class*='pricing-title text-white ls-1']").eq(0).contains('BRONZE')
        cy.iframe().find("h1[class*='pricing-title text-white ls-1']").eq(0).contains('BRONZE')
    
    })

    it ('my calender test', ()=>{
        cy.visit('https://rahulshettyacademy.com/seleniumPractise/#/offers')
        

    })
} )