$("#contactoNav").click(function () {
    $('html,body').animate(
        {
            scrollTop: $('#contacto').offset().top - 30
        },
        'slow'
    );
});

function initSelectAjax(select) {
    var placeholder = select.attr('data-placeholder');
    select.append("<option selected disabled>" + placeholder + "</option>");

    if(select.attr("data-source") === "") {
        select.attr("disabled", true);
    } else {
        select.attr("disabled", false);
        $.ajax({
            url: select.attr('data-source')
        }).then(function (options) {
            options.map(function (option) {
                var $option = $("<option>");
                $option
                    .val(option[select.attr("data-valueKey")])
                    .text(option[select.attr("data-displayKey")]);
                select.append($option)
            });
        });
    }
}

$(document).ready(function () {

    $('select[data-source]').each(function () {
        var $select = $(this);
        initSelectAjax($select);
    });

});