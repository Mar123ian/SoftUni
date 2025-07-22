document.addEventListener('DOMContentLoaded', solve);

function solve() {
  let generate=document.querySelector('#input input[type="submit"]');
  generate.addEventListener('click', generateRow);
  let input=document.querySelector('#input textarea');
  let body=document.querySelector('table tbody');
  let row;
  let buyButton=document.querySelector('#shop input[type="submit"]');
  buyButton.addEventListener('click', buy);
  
  
  function createTd(type, info=undefined){
    
    if (type=="text"){
      td = document.createElement("td");
      let p= document.createElement("p");
      p.textContent=info;
      td.appendChild(p);
      row.appendChild(td);
    }
    
    if (type=="img"){
      let td = document.createElement("td");
      let image= document.createElement("img");
      image.src=info;
      td.appendChild(image);
      row.appendChild(td);
    }
    
    if (type=="checkbox"){
      td = document.createElement("td");
      let input= document.createElement("input");
      input.type="checkbox";
      
      td.appendChild(input);
      row.appendChild(td);
    }
    
    
  }
  
  function generateRow(e){
    e.preventDefault();
    let data=(JSON.parse(input.value));
    
    for (el of data){
      
      row = document.createElement("tr");
      let {decFactor, img, name, price}=el;
      
      createTd("img", img);
      createTd("text", name);
      createTd("text", price);
      createTd("text", decFactor);
      createTd("checkbox");
      
      body.appendChild(row);
      
    }
    
  }
  
  let tbody=document.querySelector('tbody');
  tbody.addEventListener('change', addToCart);
  
  let cart=[];
  let totalPrice=0;
  let totalDecFactor=0;

  function addToCart(e){
    
    let checkbox=e.target;
    if (checkbox.tagName=="INPUT"){
      let name=checkbox.parentNode.parentNode.querySelector("td:nth-child(2) p").textContent;
      let price=Number(checkbox.parentNode.parentNode.querySelector("td:nth-child(3) p").textContent);
      let decFactor=Number(checkbox.parentNode.parentNode.querySelector("td:nth-child(4) p").textContent);
      
      if (checkbox.checked){
        
        cart.push(name);
        totalPrice+=price;
        totalDecFactor+=decFactor;
      }
      
      else{
        cart.splice(cart.indexOf(name), 1);
        totalPrice-=price;
        totalDecFactor-=decFactor;
      }
    }
    
  }
  
  
  function buy(e){
    e.preventDefault(); 
    let outputArea=document.querySelector("#shop textarea");
    let cartToString=cart.join(", ");
    let output=`Bought furniture: ${cartToString}\nTotal price: ${totalPrice}\n`;
    
    if (totalDecFactor!=0){
      output+=`Average decoration factor: ${totalDecFactor/cart.length}`;
    }
    else{
      output+='Average decoration factor: 0';
    }
    
    outputArea.textContent=output;
    
  }
  
}