function roadRadar(speed, area){
    let maxSpeed={
        motorway:130,
        interstate:90,
        city:50,
        residential:20

    };

    if (speed<=maxSpeed[area]){
        console.log(`Driving ${speed} km/h in a ${maxSpeed[area]} zone`);
    }

    else{
        
        let difference=speed-maxSpeed[area];
        let status;

        if (difference<=20){
            status="speeding";
        }

        else if (difference<=40){
            status="excessive speeding";
        }

        else{
            status="reckless driving";
        }

        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${maxSpeed[area]} - ${status}`);
    }
}

roadRadar(120, 'interstate');