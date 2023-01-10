const menusidebar = $('.botao-esconder')
const menusidebar_voltar = $('.botao-mostrar')

menusidebar_voltar.css('display', 'none')

menusidebar.on("click", function () {
    $('[atributo-hide]').hide(2000)
    menusidebar.css('display', 'none')
    menusidebar_voltar.css('display', 'block')
})

menusidebar_voltar.click(function () {
    $('[atributo-hide]').show(2000)
    menusidebar.css('display', 'block')
    menusidebar_voltar.css('display', 'none')
})