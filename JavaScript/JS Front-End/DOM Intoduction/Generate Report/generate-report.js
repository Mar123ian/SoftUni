function solve() {
    let output=document.querySelector("#output");  
    let data=[];
    let checkedColumns={};
    let headers=Array.from(document.querySelectorAll("tr th input"));
    
    headers.forEach((el, idx)=>{
        if (el.checked){
            checkedColumns[idx]=el.name;        
        }
    });
    
    let rows=Array.from(document.querySelectorAll("tbody tr"));
    let obj;
    let trChildren;

    rows.forEach((tr)=>{
        obj={};
        trChildren=tr.children;
        for (let i=0; i<trChildren.length;i++){
            if (i in checkedColumns){
                obj[checkedColumns[i]]=trChildren[i].textContent;               
            }           
        }
        data.push(JSON.stringify(obj));   
    });
    
    output.textContent="["+data+"]";
    
}