const regexStudent = /(.+)\[(25)\] with email (.+) joins (.+)/gm;
const regexCourse = /([A-Za-z]+): ([0-9]+)/gm;

let name=regexCourse.exec('JavaBa@sics: 1^^5')[2];
console.log(name);