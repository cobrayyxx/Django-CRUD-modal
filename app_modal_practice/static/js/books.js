$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-book").modal("show");
      },
      success: function (data) {
        $("#modal-book .modal-content").html(data.html_form);
      }
    });
  };
  

  var saveForm = function ()  {
    var form = $(this); //selecting actual form in class js-book-create-form
    $.ajax({
      url: form.attr("action"), //The action here refers to the action attribute in the form or /books/create
      data: form.serialize(),//we are serializing all the data from the form, and posting it to the server.
      type: form.attr("method"),//
      dataType: 'json',
      success: function (data) {
        
        if (data.form_is_valid) {
          $("#book-table tbody").html(data.html_book_list);  // <-- Replace the table body
          $("#modal-book").modal("hide"); 
        }
        else {
   
          $("#modal-book .modal-content").html(data.html_form);
        }
      }
    });
    return false; //avoid the browser to perform a full HTTP POST to the server because form submission event
  };

  /* Binding */

  // Create book
  $(".js-create-book").click(loadForm);
  $("#modal-book").on("submit", ".js-book-create-form", saveForm);

  // Update book
  $("#book-table").on("click", ".js-update-book", loadForm);
  $("#modal-book").on("submit", ".js-book-update-form", saveForm);

});

