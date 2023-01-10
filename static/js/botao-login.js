const botao = $('button')
const login = $('#login')
const senha = $('#password')

login.change(() => {
    senha.keydown(() => {
        botao.removeClass('disabled')
    })
})

senha.mousedown(() => {

})