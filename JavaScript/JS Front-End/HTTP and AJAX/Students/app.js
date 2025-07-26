function displayStudentRow(studentInfo) {
    let tr = document.createElement("tr");

    for (let info in studentInfo) {
        if (info != "_id") {
            let td = document.createElement("td");
            td.textContent = studentInfo[info];
            tr.appendChild(td);
        }
    }

    tbody.appendChild(tr);
}

async function showStudents() {

    let url = "http://localhost:3030/jsonstore/collections/students";
    let data;

    try {
        let result = await fetch(url);
        if (!result.ok) {
            throw new Error(`Error ${result.status} ${result.statusText}`);
        }

        data = await result.json();
    }
    catch (err) {
        console.error(err);
        return;
    }

    tbody.replaceChildren();

    for (let student in data) {

        let studentInfo = data[student];
        displayStudentRow(studentInfo);

    }
}

async function addStudent(e) {
    e.preventDefault();
    let formData = new FormData(form);
    formData = Object.fromEntries(formData.entries());

    let url = "http://localhost:3030/jsonstore/collections/students";
    let options = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
    };

    try {
        let result = await fetch(url, options);
        if (!result.ok) {
            throw new Error(`Error ${result.status} ${result.statusText}`);
        }
    }
    catch (err) {
        console.error(err);
        return;
    }

    displayStudentRow(formData);
}

let tbody = document.querySelector("tbody");
let form = document.querySelector("#form");

form.addEventListener('submit', addStudent);
showStudents();