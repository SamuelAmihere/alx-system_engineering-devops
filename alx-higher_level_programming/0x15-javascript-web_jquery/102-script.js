$('document').ready(function () {
  const x = $.param({ lang: $('INPUT#language_code').val() });
  const url = 'https://www.fourtonfish.com/hellosalut/?' + x;
  $('INPUT#btn_translate').click(function () {
    $.get(url, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
