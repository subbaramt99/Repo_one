///*******************************Alerts and Popups************************************
describe('My Alerts test', function () {
    it('test with Alerts', function () {
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/')
        cy.get('#alertbtn').click()
        // Cypress will auto accept the alerts
        // Cypress have the capability of  browser event "Windows alert" is event which get fired on alert opens
        // So we can fire the event through cypress get access to the alerts
        // But in cypress it'll not be visible
        cy.on('window:alert', (str) => {
            // assertion of two sting
            expect(str).to.equal('Hello , share this practice page and share your knowledge')
        })

        cy.get('#confirmbtn').click()
        cy.on('window:confirm', (str) => {
            // assertion of two sting
            expect(str).to.equal('Hello , Are you sure you want to confirm?')
        })


    })

})

///*******************************Child windows************************************

describe('My Child window test', function () {
    it('test with Child window', function () {
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/')
        // Cypress not having capability to handle child windows
        // So we have option to manupulate the Html dome with "invoke" method
        // using it i'm removing the "target = "_blank" attribute so the new tab link will launch in same tab
        cy.get('.btn-style.class1.class2').invoke('removeAttr', 'target').click()
        // Cross domain working with cypress
        //cy.get("div[class = 'button float-left'] a[class = 'main-btn']").should('be.visible')
        cy.origin('https://www.qaclickacademy.com/', ()=> {
            cy.get("div[class = 'button float-left'] a[class = 'main-btn']").click()

        })

    })

})


//**************Visible and Invisible of elements********************** 

describe('My visiblity test', function () {
    it('My visibility test', function () {
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/')
        cy.get('#show-textbox').click() // making the element visible
        cy.get('#displayed-text').should('be.visible')
        cy.get('#hide-textbox').click() // making the element invisible
        cy.get('#displayed-text').should('not.be.visible')

        // check the visibility of Radio buttons

        cy.get("[value = 'radio1']").check().should('be.checked')
    })

})

describe('My Web table test', function () {
    it('Test with Web tables', function () {
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/')
        // very important consept to take CSS selector it will select all rows with second coloum alone
        // ex in Xpath tr/td[2] in css tr td:nth-child(2)
        cy.get('tr td:nth-child(2)').each(($ele, index, list) => {
            const Courses = $ele.text()
            //cy.log( Courses)
            if (Courses === 'Master Selenium Automation in simple Python Language'){
                cy.log(Courses)
            }
            if (index === 3){
                cy.log(Courses)
            }
            //cy.log(list)
            cy.pause()
            
        })
    })

})

