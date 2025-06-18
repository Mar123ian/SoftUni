function extractText() {
    let liElements = Array.from(document.getElementsByTagName ('li'));
    let textarea=document.getElementById ('result')
    let text=""
    for (let i = 0; i < liElements.length; i++) {
        let element = liElements[i];
        text+=(element.innerText+"\n");
    }

    textarea.textContent=text
    

}
