var modal = `
                <div class="modal fade" id="deleteItemModal" tabindex="-1" role="dialog" aria-labelledby="deleteItemModalLabel" aria-hidden="true">
                    <div class="modal-dialog" role="document">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="deleteItemModalLabel">Delete Item</h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div class="modal-body">
                                Are you sure you want to delete this item?
                            </div>
                            <div class="modal-footer">
                                <input type="hidden" id="item_id" value="">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                <button type="submit" id="delete_button" class="btn btn-danger">Delete</button>
                            </div>
                        </div>
                    </div>
                </div>
            `;
$('body').append(modal);

$('#myTable').on('click', '.btn-danger', function () {
    $('#item_id').val($(this).val());
    $('#deleteItemModal').modal('show');
    $('#deleteItemModal').css('padding-right', '0px');
});

$('#delete_button').on('click', function () {
    var item_id = $('#item_id').val();
    var buttonWidth = $(this).css('width');
    var buttonHeight = $(this).css('height');

    $(this).prop('disabled', true);
    $(this).html('<i class="fa fa-spinner fa-spin"></i>');
    $(this).css('width', buttonWidth);
    $(this).css('height', buttonHeight);
    $(this).css('cursor', 'not-allowed');

    $.ajax({
        url: item_id + '/delete/',
        success: function () {
            location.reload();
        },
        error: function (error) {
            alert('Error deleting item!');
            $(this).prop('disabled', false);
            $(this).html('Delete');
            $(this).css('cursor', 'pointer');
        }
    });
});

$('#reset-database').on('click', function () {
    $(this).prop('disabled', true);
    $(this).html('<i class="fa fa-spinner fa-spin"></i>');
    $(this).css('cursor', 'not-allowed');

    $.ajax({
        url: window.location.href + 'api/',
        success: function () {
            $(this).html('Reset Database');
            location.reload();
        },
        error: function (error) {
            alert('Error resetting database!');
            $(this).html('Reset Database');
            $(this).prop('disabled', false);
            $(this).css('cursor', 'pointer');
        }
    });
});

$('#search').on('click', function () {
    var query = $('#myInput').val().toLowerCase();

    if (query == '') {
        return;
    }

    $.ajax({
        url: 'search/' + query + '/',
        success: function () {
            console.log('Search successful');
            window.location.href = 'search/' + query + '/';
        },
        error: function (error) {
            console.log('Error searching! ' + error);
        }
    });
});

var input = document.getElementById("myInput");
$(input).keyup(function (event) {
    if (event.keyCode === 13) {
        validate(event);
    }
});

function validate(event) {
    event.preventDefault();
}