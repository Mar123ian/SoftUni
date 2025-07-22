document.addEventListener('DOMContentLoaded', solve);

function solve() {
  let points=0;
  let correctAnswers=["onclick", "JSON.stringify()", "A programming API for HTML and XML documents"];
  let main =document.querySelector("main")
  main.addEventListener('click', checkAnswer);
  let sections=Array.from(document.querySelectorAll("section"));
  let results=document.querySelector("#results")
  
  function checkAnswer(ev){
    
    let target=ev.target;
    
    if (target.classList.value.includes("quiz-answer")){
      
      if (correctAnswers.includes(target.textContent)){
        points++;      
      }     
    }

    target.parentNode.parentNode.classList.add("hidden");
    sections.shift()
    if (sections[0]){
      sections[0].classList.remove("hidden");
    }
    else{
      showResult();
    }
  }
  
  function showResult(){
    if (points==3){
      results.textContent="You are recognized as top JavaScript fan!"
    }
    
    else if (points==1){
      results.textContent="You have 1 right answer"
    }
    
    else{
      results.textContent=`You have ${points} right answers`
    }
    
  }
}
