$.tablesorter.addParser({
        id: 'status',
        is: function(s) {
            return false;
        },
        format: function(s) {
            return s.toLowerCase().replace(/no progress/,0).replace(/in progress/,1).replace(/achieved/,2).replace(/broken/,3);
        },
        type: 'numeric'
});

$.tablesorter.addParser({
        id: 'category',
        is: function(s) {
            return false;
        },
        format: function(s) {
            return s.toLowerCase().replace(/culture/,0).replace(/defense/,1).replace(/economy/,2).replace(/education/,3).replace(/environment/,4).replace(/general/,5).replace(/immigration/,6).replace(/justice/,7).replace(/security/,8).replace(/welfare/,9);
        },
        type: 'numeric'
});

$(document).ready(function()
    {
        $("#policyTable").tablesorter({
          headers: {
            2: {
              sorter: 'status'
            },
            3: {
              sorter: 'category'
            }
          }
        });
    }
);

$("#id_startDate").attr('maxlength', '10');
$("#id_startDate").on('keyup', function(){
  var inp = $('#id_startDate').val();
  var n = inp.indexOf("-");
  if ((inp.length == 4) || (inp.length == 7) && inp.length < 9) {
    $('#id_startDate').val(inp + '-');
  }
});
