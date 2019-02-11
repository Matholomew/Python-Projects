
function decodeHTMLEntities(text) {
    var entities = [
        ['amp', '&'],
        ['apos', '\''],
        ['#x27', '\''],
        ['#x2F', '/'],
        ['#39', '\''],
        ['#47', '/'],
        ['lt', '<'],
        ['gt', '>'],
        ['nbsp', ' '],
        ['#039', '\''],
        ['ouml', 'ö'],
        ['aring', 'å'],
        ['auml', 'ä'],
        ['quot', '"']
    ];

    for (var i = 0, max = entities.length; i < max; ++i)
        text = text.replace(new RegExp('&'+entities[i][0]+';', 'g'), entities[i][1]);
    return text;
}

function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}


function getCheckedRdb(rdbs) {
    for (var i = 0; i < rdbs.length; i++) {
        if (rdbs[i].checked) {
            return rdbs[i].id;
        }
    }
}



function submitQuestion() {
    var chosenAnswer = getCheckedRdb(document.getElementsByName('choice'))
    chosenAnswer = chosenAnswer[chosenAnswer.length - 1]
    chosenAnswer = choices[chosenAnswer - 1]
    console.log(chosenAnswer)
    var currentScore = parseInt(localStorage.getItem("score"))
    var firstQ = localStorage.getItem("firstQ")

    var currentQuestion = window.location.href
    currentQuestion = currentQuestion.substring(currentQuestion.indexOf('polls/'))
    currentQuestion = currentQuestion.substring(6)
    currentQuestion = currentQuestion.substring(currentQuestion.indexOf('/'), -1)


    if(firstQ === '0'){
        localStorage.setItem("firstQ", currentQuestion)
        firstQ = localStorage.getItem("firstQ")
    }


    if(chosenAnswer === correctAnswer) {
        runSnackBar()


        currentQuestion = parseInt(currentQuestion) + 1
        var stopQ = parseInt(firstQ) + 10
        if(currentQuestion <= stopQ) {
            currentScore += 1
            localStorage.setItem("score", currentScore)
            window.location = "/polls/" + currentQuestion
        }
        else {
            // Record highscore and save it to the tournament/questions db table
            // Redirect to home page
            currentScore = parseInt(localStorage.getItem("score"))
            console.log("Highscore: " + currentScore)

            $.ajax({
                url: "/polls/score/",
                type:"GET",
                data: {'total':currentScore,'userid':"{{ user.id }}"}
            }).done(function(data){
                document.getElementById("score").textContent = "Your score: " + currentScore

            });

        }
    }
    else {
        runSnackBar2()

        currentQuestion = parseInt(currentQuestion) + 1
        var stopQ = parseInt(firstQ) + 10
        console.log(currentQuestion)
        console.log(stopQ)
        if(currentQuestion <= stopQ) {
            console.log(stopQ)
            window.location = "/polls/" + currentQuestion
        }
        else {
            // Record highscore and save it to the tournament/questions db table
            // Redirect to home page
            currentScore = parseInt(localStorage.getItem("score"))
            console.log("Highscore: " + currentScore)

            $.ajax({
                url: "/polls/score/",
                type:"GET",
                data: {'total':currentScore,'userid':"{{ user.id }}"}
            }).done(function(data){
                document.getElementsByClassName("container")[0].textContent = "<h1>Your score: " + currentScore + "</h1>"
            });

        }
    }
}


function runSnackBar2() {
    var x = document.getElementById("snackbar2");
    x.style.display="block"
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

function runSnackBar() {
    var x = document.getElementById("snackbar");
    x.style.display="block"
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}
