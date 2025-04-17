
function validateForm(event) {
    event.preventDefault();

    const nameInput = document.getElementById("name");
    const platformInput = document.getElementById("platform");
    const yearInput = document.getElementById("release_year");
    const fileInput = document.getElementById("game_file");
    const errorMessage = document.getElementById("errorMessage");

    let isValid = true;
    let messages = [];

    errorMessage.style.display = "none";
    errorMessage.textContent = "";

    nameInput.style.borderColor = "";
    platformInput.style.borderColor = "";
    yearInput.style.borderColor = "";
    fileInput.style.borderColor = "";

    if (!nameInput.value.trim()) {
        isValid = false;
        nameInput.style.borderColor = "red";
        messages.push("Name is required.");
    }

    if (!platformInput.value.trim()) {
        isValid = false;
        platformInput.style.borderColor = "red";
        messages.push("Platform is required.");
    }

    const currentYear = new Date().getFullYear();
    const releaseYear = parseInt(yearInput.value, 10);
    if (isNaN(releaseYear) || releaseYear < 1950 || releaseYear > currentYear) {
        isValid = false;
        yearInput.style.borderColor = "red";
        messages.push(`Release year must be between 1950 and ${currentYear}.`);
    }

    const file = fileInput.files[0];
    if (file) {
        const validExtensions = ["jpg", "jpeg", "png"];
        const fileSizeLimit = 2 * 1024 * 1024;
        const fileExt = file.name.split('.').pop().toLowerCase();

        if (!validExtensions.includes(fileExt)) {
            isValid = false;
            fileInput.style.borderColor = "red";
            messages.push("Only JPG, JPEG, and PNG files are allowed.");
        }

        if (file.size > fileSizeLimit) {
            isValid = false;
            fileInput.style.borderColor = "red";
            messages.push("File must be less than 2MB.");
        }
    }

    if (!isValid) {
        errorMessage.textContent = messages.join(" ");
        errorMessage.style.display = "block";
    } else {
        document.getElementById("gameForm").submit();
    }
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("gameForm").addEventListener("submit", validateForm);
});