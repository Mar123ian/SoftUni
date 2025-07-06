function solve() {
    let data =(document.querySelector("textarea").value.replaceAll('["',"").replaceAll('"]',""))
    data=data.split('","')
    let best=document.querySelector("#bestRestaurant p")
    let workers=document.querySelector("#workers p")
    let avs={}
    let top={}
    let restaurants={};
    const regexName = /(.+) - /m;
    const regexWorker = /(\w+ \d+)/gm;

    for (el of data){
        let name=el.match(regexName)[1];
        
        let workers=Array.from(el.match(regexWorker))
        workers.forEach((el ,idx)=>{workers[idx]=el.split(" ")});
        
        if (name in restaurants){
            restaurants[name]=restaurants[name].concat(workers)
        }

        else{
            restaurants[name]=workers
        }       
    }
    let bestrs=0;
    let bestr;
    for (let [k,v] of Object.entries(restaurants)){
        let avg=0;
        let sals=[]
        for (let [, sal] of v){
            avg+=Number(sal)
            sals.push(Number(sal))
        }
        top[k]=Math.max(...sals);
        avg/=v.length
        avs[k]=avg
        if (avg>bestrs){
            bestrs=avg;
            bestr=k
        }
        v.sort((a, b)=>b[1]-a[1])
    }


    let ws=[]
    for (let [w, s] of restaurants[bestr]){
        ws.push(`Name: ${w} With Salary: ${s}`)
    }

    let wst=ws.join(" ")
    best.textContent=`Name: ${bestr} Average Salary: ${bestrs.toFixed(2)} Best Salary: ${top[bestr].toFixed(2)}`
    workers.textContent=wst

}