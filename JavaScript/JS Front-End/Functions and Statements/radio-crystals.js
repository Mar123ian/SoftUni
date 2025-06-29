function radioCrystals(elements){
    const target = elements.shift();
    
    

    let cuts=0;
    let laps=0;
    let grinds=0;
    let etches=0;

    for (let el of elements){
        console.log(`Processing chunk ${el} microns`);

        
            while (el/4 >= target){
                el/=4;               
                cuts++;
            }

            if (cuts>0){
                console.log(`Cut x${cuts}`);
                el=Math.floor(el)
                console.log("Transporting and washing");
            }
            

            while (0.8*el >= target){
                el*=0.8;
                laps++;
            }

            if (laps>0){
                console.log(`Lap x${laps}`);
                el=Math.floor(el)
                console.log("Transporting and washing");
            }
            

            while (el-20 >= target){
                el-=20;
                grinds++;
            }

            if (grinds>0){
                console.log(`Grind x${grinds}`);
                el=Math.floor(el)
                console.log("Transporting and washing");
            }
            

            while (el-2 > target-2){
                el-=2;
                etches++;
            }

            if (etches>0){
                console.log(`Etch x${etches}`);
                el=Math.floor(el)
                console.log("Transporting and washing");
            }

            

            if (el!=target){
                el++;
                console.log("X-ray x1");
            }
            
            console.log(`Finished crystal ${el} microns`);
            

            cuts=0;
            laps=0;
            grinds=0;
            etches=0;
        
    }
}

radioCrystals([1000, 4000, 8100])