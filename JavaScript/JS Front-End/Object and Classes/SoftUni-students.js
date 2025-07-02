function softUniStudents(data){

    const regexStudent = /(.+)\[(.+)\] +with +email (.+) joins (.+)/m;
    const regexCourse = /(.+): +([-0-9]+)/m;    
    let softUniCourses={};

    for (let info of data){
        info=info.trim()
        if (regexCourse.test(info)){
            let name=(regexCourse.exec(String(info))[1]).trim();
            let capacity=Number((regexCourse.exec(info)[2]).trim());

            if(softUniCourses.hasOwnProperty(name)){
                softUniCourses[name].capacity+=capacity;
            }
            else{
                softUniCourses[name]={capacity, students:{}, countOfStudents:0};
            }
            
        }

        else if (regexStudent.test(info)){
            
            let [matchInfo, username, credits, email, course]=regexStudent.exec(info);

            if (softUniCourses.hasOwnProperty(course) && softUniCourses[course].capacity>0){
           
                softUniCourses[course].capacity-=1;
                softUniCourses[course].countOfStudents++;
           
                if (softUniCourses[course].students.hasOwnProperty(username)){
                    softUniCourses[course].students[username+"   "]={credits,email}; 
                }
                else{
                    softUniCourses[course].students[username]={credits,email};  
                }
            }
        } 
    }
   
    let softUniCoursesEntries=Object.entries(softUniCourses);
    softUniCoursesEntries.sort((a,b)=>b[1].countOfStudents-a[1].countOfStudents)

    for (let [k,v] of (softUniCoursesEntries)){
 
        let {capacity, students, countOfStudents}=v;
        
        console.log(`${k}: ${capacity} places left`);
        
        let studentsEntries=Object.entries(students)
        studentsEntries.sort((a,b)=>Number(b[1].credits)-Number(a[1].credits))
        
        for (let [username, info] of studentsEntries){
            
            console.log(`--- ${info.credits}: ${username.trim()}, ${info.email}`);
        }
    }
}

softUniStudents(['JavaBasics: 2', 'user1[25] with email user1@user.com joins C#Basics', 'C#Advanced: 3','C++ Advanced: 3', 'JSCore: 4', 'user2[30] with email user2@user.com joins C#Basics','user13[50] with email user13@user.com joins JSCore','user1[25] with email user1@user.com joins JSCore', 'user8[18] with email user8@user.com joins C#Advanced','user6[85] with email user6@user.com joins JSCore', 'JSCore: 2', 'user11[3] with email user11@user.com joins JavaBasics', 'user45[105] with email user45@user.com joins JSCore', 'user007[20] with email user007@user.com joins JSCore', 'user700[29] with email user700@user.com joins JSCore', 'user900[88] with email user900@user.com joins JSCore']);