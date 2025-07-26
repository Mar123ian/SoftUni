function attachEvents() {

    let loadBtn = document.querySelector("#btnLoad");
    loadBtn.addEventListener('click', loadContacts);

    let pb = document.querySelector("#phonebook");
    pb.addEventListener('click', delContact);

    let createBtn = document.querySelector("#btnCreate");
    createBtn.addEventListener('click', createContact);

}
async function createContact() {
    let person = document.querySelector("#person").value;
    let phone = document.querySelector("#phone").value;

    let url = "http://localhost:3030/jsonstore/phonebook";
    let options = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ person, phone })
    };

    await fetch(url, options);
    loadContacts();

}

async function delContact(ev) {
    let target = ev.target;
    let li = target.parentNode;

    if (target.tagName == "BUTTON") {

        let id = li.id;
        let url = `http://localhost:3030/jsonstore/phonebook/${id}`;
        let options = { method: "DELETE" };

        await fetch(url, options);
        li.remove();

    }

}

async function loadContacts() {

    let url = "http://localhost:3030/jsonstore/phonebook";
    let result = await fetch(url);
    let data = await result.json();

    let phonebook = document.querySelector("#phonebook");
    phonebook.replaceChildren();

    for (let contact in data) {
        let li = document.createElement("li");
        let delBtn = document.createElement("button");

        li.id = data[contact]._id;
        delBtn.textContent = "Delete";
        li.textContent = `${data[contact].person}: ${data[contact].phone}`;
        li.appendChild(delBtn);
        phonebook.appendChild(li);

    }
}

attachEvents();