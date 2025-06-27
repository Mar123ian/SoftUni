function spiceMustFlow(yield){

    let total=0;
    let days=0;
    
    while (true){
        if (yield<100 && days==0){
            break;
        }

        if (yield<100 && days!=0){
            total-=26;
            break;
        }

        days++;     
        total+=yield-26;
        yield-=10;
    }
       
    console.log(days);
    console.log(total);
       
    }

spiceMustFlow(111);