$(document).ready(function () {

    var baseUrl = 'http://127.0.0.1:8000/';
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter');
    var insumovar = $('#insumoselect');
        $options=$insumovar.find('option');
        $insumovar.on('change', function()
        {
            $insumovar.html($options.filter('[value= "' + this.value + '"]'))

        }).trigger('change');

    $(deleteBtn).on('click', function (e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar esta tarefa?');

        if (result) {
            window.location.href = delLink;
        }

    });

    $(searchBtn).on('click', function () {
        searchForm.submit();
    });

    $(filter).change(function () {
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    });






});

