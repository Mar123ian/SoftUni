document.addEventListener('DOMContentLoaded', solve);

function solve() {
  let generate=document.querySelector('#input input[type="submit"]');
  generate.addEventListener('click', generateRow);
  let input=document.querySelector('#input textarea')
  let body=document.querySelector('table tbody')

  let buyButton=document.querySelector('#shop input[type="submit"]');
  buyButton.addEventListener('click', buy);

  function generateRow(e){
    e.preventDefault();
    let data=(JSON.parse(input.value));
    
    
    console.log(data);
    for (el of data){
      console.log(el);
      let row = document.createElement("tr");
      let {decFactor, img, name, price}=el;
      let td = document.createElement("td");
      let image= document.createElement("img")
      image.src=img;
      td.appendChild(image)
      row.appendChild(td)

      td = document.createElement("td");
      let p= document.createElement("p")
      p.textContent=name;
      td.appendChild(p)
      row.appendChild(td)
      

      td = document.createElement("td");
      p= document.createElement("p")
      p.textContent=price;
      td.appendChild(p)
      row.appendChild(td)
      
      td = document.createElement("td");
      p= document.createElement("p")
      p.textContent=decFactor;
      td.appendChild(p)
      row.appendChild(td)

      td = document.createElement("td");
      let input= document.createElement("input")  
      input.type="checkbox"
      
      td.appendChild(input)
      row.appendChild(td)

      body.appendChild(row)

    }
    
  }

  function buy(e){
    e.preventDefault();
    let cart=[];
    let total=0;
    let adc=0;
    let pr=0;
    let els=Array.from(document.querySelectorAll("tr"));
    els.shift()
    for (el of els){
      let checkbox=el.querySelector('input[type="checkbox"]')
      console.log(el,checkbox);
      if (checkbox.checked){
        console.log(checkbox.parentNode.parentNode.querySelector("td:nth-child(2) p"));
        let name=checkbox.parentNode.parentNode.querySelector("td:nth-child(2) p").textContent;
        let price=Number(checkbox.parentNode.parentNode.querySelector("td:nth-child(3) p").textContent);
        let dc=Number(checkbox.parentNode.parentNode.querySelector("td:nth-child(4) p").textContent);
        adc+=dc
        cart.push(name);
        total+=price;
        pr++;

   
      }

    }
    let output=document.querySelector("#shop textarea")
    console.log(cart, total);
    let bf=cart.join(", ")
    let out=[]
    out.push("Bought furniture: "+bf)
    out.push(`Total price: ${total}`)
    if (adc!=0){
      out.push(`Average decoration factor: ${adc/pr}`)
    }
    else{
      out.push('Average decoration factor: 0')
    }

    output.textContent=out.join("\n")
    
  }

}