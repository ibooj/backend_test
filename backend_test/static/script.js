$(function () {
    $("form").submit(function (e) {
        e.preventDefault();
        var form = $(this);
        $.post(form.attr('action'), form.serialize(), function (data) {
            $('#result_' + form.attr('id')).text(JSON.stringify(data));
        });
    });
});