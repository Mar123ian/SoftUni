function pointsValidation(points){
    points=[[points[0], points[1]], [points[2], points[3]]];
    let pointsToCompare=[[0,0],[points[1][0], points[1][1]]];
    let comparisons=0;

    for (let group of pointsToCompare){
        let pointToComparex=group[0];
        let pointToComparey=group[1];

        for (let group2 of points){
            
            comparisons++;
            if (comparisons>3){               
                break;
            }

            let pointx=group2[0];
            let pointy=group2[1];
            if (Number.isInteger(Math.sqrt((pointToComparex-pointx)**2+(pointToComparey-pointy)**2))){
                console.log(`{${pointx}, ${pointy}} to {${pointToComparex}, ${pointToComparey}} is valid`);
            }
            
            else{
                console.log(`{${pointx}, ${pointy}} to {${pointToComparex}, ${pointToComparey}} is invalid`);
            }
        }       
    }   
}

pointsValidation([2, 1, 1, 1]);