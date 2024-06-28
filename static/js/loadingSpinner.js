function showSpinner() {
    $('#loadingSpinnerModal').modal('show');
    var submitBtns = document.getElementsByClassName("submit-btn");
    for (var i = 0; i < submitBtns.length; i++) {
        submitBtns[i].setAttribute("disabled", "disabled");
    }
}