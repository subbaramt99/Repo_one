describe('test fixture', () =>{


    it('fixture testing', function(){
        cy.fixture('data').as('data')

        cy.get('@data').then(function(data){
           cy.wrap(data).as('credentials')
           this.data = data;
        })
    })

    it('count the vowels', function() {
        let str = "JavaScript";
        const count = str.match(/[aeiou]/gi)?.length || 0;
        cy.log(count)
    })

    it('removing duplicates in array', function() {
        const arr = [1, 2, 3, 4, 1, 2, 3];
        const unique = [...new Set(arr)];
        cy.log(unique)
    })



    it('fixture testing', function() {
        cy.log(this.credentials);
        cy.log(this.data);
    })
})