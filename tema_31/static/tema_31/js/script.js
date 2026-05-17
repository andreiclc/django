const editForm = document.getElementById("editForm");


if (editForm) {
    const nameInput = document.getElementById("bookName");
    const nameError = document.querySelector(".nameError");

    editForm.addEventListener("submit", (e) => {
        let nameStatus = true;

        if (!Empty(nameInput, "Name", nameError)) nameStatus = false;
        else if (!MinLen(nameInput, "Name", nameError, 2)) nameStatus = false;
        else if (!MaxLen(nameInput, "Name", nameError, 255)) nameStatus = false;

        if (!nameStatus) {
            e.preventDefault();
            return;
        }
    });
}


function Empty(input, label, errorClass) {
    const fieldName = input.value.trim();
    if (fieldName == '') {
        errorClass.innerHTML = `${label} is required`;
        input.classList.add("border-danger");
        return false;
    } else {
        errorClass.innerHTML = "";
        input.classList.remove("border-danger");
        return true;
    }   
}


function MinLen(input, label, errorClass, min) {
    const fieldName = input.value.trim();
    if (fieldName.length < min) {
        errorClass.innerHTML = `${label} must be at least ${min} characters`;
        input.classList.add("border-danger");
        return false;
    } else {
        errorClass.innerHTML = "";
        input.classList.remove("border-danger");
        return true;
    }
}


function MaxLen(input, label, errorClass, max) {
    const fieldName = input.value.trim();
    if (fieldName.length > max) {
        errorClass.innerHTML = `${label} must not exceed ${max} characters`;
        input.classList.add("border-danger");
        return false;
    } else {
        errorClass.innerHTML = "";
        input.classList.remove("border-danger");
        return true;
    }
}