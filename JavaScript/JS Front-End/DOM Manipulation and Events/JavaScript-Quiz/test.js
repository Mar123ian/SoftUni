document.body.innerHTML = `
<main>

    <h1>JavaScript Quiz</h1>

    <section class="question">
        <h2><span>Question #1:</span> Which event occurs when the user clicks on an HTML element?</h2>
        <ul class="quiz-step">
            <li class="quiz-answer">onclick</li>
            <li class="quiz-answer">onmouseclick</li>
        </ul>
    </section>

    <section class="question hidden">
        <h2><span>Question #2:</span> Which function converting JSON to string?</h2>
        <ul class="quiz-step">
            <li class="quiz-answer">JSON.toString()</li>
            <li class="quiz-answer">JSON.stringify()</li>
        </ul>
    </section>

    <section class="question hidden">
        <h2><span>Question #3:</span> What is DOM?</h2>
        <ul class="quiz-step">
            <li class="quiz-answer">A programming API for HTML and XML documents</li>
            <li class="quiz-answer">The DOM is your source HTML</li>
        </ul>
    </section>

    <div id="results"></div>
    
</main>
`;

result();

let sections = document.getElementsByTagName('section');
let results = document.getElementById('results');

sections[0].querySelectorAll('.quiz-answer')[0].click(); // Correct
sections[1].querySelectorAll('.quiz-answer')[1].click(); // Correct
sections[2].querySelectorAll('.quiz-answer')[1].click(); // Incorrect

assert.equal(results.textContent.trim(), 'You have 2 right answers', 'The expected output is different');
