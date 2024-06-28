// Define the confirmDownload function
function confirmDownload(fileUrl, fileName) {
    // Set a default message if fileName is undefined or empty
    var message = fileName ? 'Download "' + fileName + '"?' : "Download file?";

    var userConfirmed = window.confirm(message);
    if (userConfirmed) {
        // Proceed with the download
        window.location.href = fileUrl;
    }
    // User canceled, do nothing
}

// Attach the confirmDownload function to the desired element
document.addEventListener("DOMContentLoaded", function () {
    var downloadButton = document.getElementById("downloadButton");
    if (downloadButton) {
        downloadButton.addEventListener("click", function (event) {
        event.preventDefault();
        confirmDownload(
            downloadButton.getAttribute("data-fileurl"),
            downloadButton.getAttribute("data-filename")
        );
        });
    }
});