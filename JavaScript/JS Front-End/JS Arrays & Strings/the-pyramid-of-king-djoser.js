function thePyramidOfKingDjoser(size, step){
    let stone=0;
    let marble=0;
    let lapisLazuli=0;
    let floor=0;
    for (i=size-2;i>0;i-=2){
        floor++;
        stone+=i**2*step;
        if (floor%5!=0){
            marble+=(i*4+4)*step;
        }
        else{
            lapisLazuli+=(i*4+4)*step;
        }
        
    }

    console.log("Stone required: "+Math.ceil(stone))
    console.log("Marble required: "+Math.ceil(marble))
    console.log("Lapis Lazuli required: "+Math.ceil(lapisLazuli))

    if (size%2==0){
        console.log("Gold required: "+Math.ceil(4*step))
    }

    else{
        console.log("Gold required: "+Math.ceil(1*step))
    }

    console.log("Final pyramid height: "+Math.floor((floor+1)*step))

}

thePyramidOfKingDjoser(13,1);