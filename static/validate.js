
function validateForm(event) {

    event.preventDefault();

    const nameInput = document.getElementById("name");
    const platformInput = document.getElementById("platform");
    const yearInput = document.getElementById("release_year");
    const errorMessage = document.getElementById("errorMessage");

    let isValid = true;

    errorMessage.style.display = "none";
    nameInput.style.borderColor = "";
    platformInput.style.borderColor = "";
    yearInput.style.borderColor = "";

    if (!nameInput.value.trim()) {
        isValid = false;
        nameInput.style.borderColor = "red";
    }

    if (!platformInput.value.trim()) {
        isValid = false;
        platformInput.style.borderColor = "red";
    }

    const currentYear = new Date().getFullYear();
    const releaseYear = parseInt(yearInput.value, 10);
    if (isNaN(releaseYear) || releaseYear < 1950 || releaseYear > currentYear) {
        isValid = false;
        yearInput.style.borderColor = "red";
    }

    if (!isValid) {
        errorMessage.style.display = "block";
    } else {
        document.getElementById("gameForm").submit();
    }
}

document.getElementById("gameForm").addEventListener("submit", validateForm);
