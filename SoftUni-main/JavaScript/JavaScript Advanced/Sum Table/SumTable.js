function sumTable() {
let liElements = Array.from(document.querySelectorAll ("table tr td:nth-child(2)")).map((el=>{return Number(el.innerText)}));
let sumElement = document.getElementById ('sum');
liElements.pop();
sumElement.innerText=liElements.reduce((sum,currentEl)=>{return sum+currentEl});
}
