$(document).ready(function() {
    function getTranslation() {
      var langCode = $('#language_code').val();
      if (langCode !== '') {
        $.ajax({
          url: 'https://www.fourtonfish.com/hellosalut/?lang=' + langCode,
          type: 'GET',
          success: function(response) {
            $('#hello').text(response.hello);
          }
        });
      }
    }
  
    $('#btn_translate').click(getTranslation);
    $('#language_code').on('keypress', function(e) {
      if (e.which == 13) {
        getTranslation();
      }
    });
  });
  