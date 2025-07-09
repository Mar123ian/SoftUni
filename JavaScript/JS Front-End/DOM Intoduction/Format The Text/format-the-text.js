function solve() {
  let sentenses=document.querySelector("#input").value.split(". ");
  let output=document.querySelector("#output");
  let paragraph=[];
  
  sentenses.forEach((el, idx) => {
    
    paragraph.push(el.trim());

    if ((idx+1)%3==0 || idx+1==sentenses.length){
      output.innerHTML+=`<p>${paragraph.join(". ")}</p>`;
      paragraph=[];
    }

  });
}