// Global constants.
var LIVES_PER_GAME = 5;
var BALL_INITIAL_INTERVAL = 3000;
var SCORE_BUMP_PER_SECOND = 10;
var SCORE_BUMP_PER_CATCH  = 100;
var BUCKET_DELTA = 40;
var BALL_COLOURS = ['red', 'green', 'blue'];

// The game itself.
var game = new Game('Hello World Game', 'gameCanvas');

// Global variables, for easy access to HTML elements.
var loadingPanel   = document.getElementById('loadingPanel');
var scorePanel     = document.getElementById('scorePanel');
var pausedPanel    = document.getElementById('pausedPanel');
var gameOverPanel  = document.getElementById('gameOverPanel');
var loadDiv        = document.getElementById('loadDiv');
var progressDiv    = document.getElementById('progressDiv');
var scoresListDiv  = document.getElementById('scoresListDiv');
var nameTextBox    = document.getElementById('nameTextBox');
var livesContext   = document.getElementById('livesCanvas').getContext('2d');

// Miscellaneous useful global variables.
var name = '';
var isLoading = true;
var score = 0;
var livesLeft = LIVES_PER_GAME;
var bucket = null;

var tLastScoreUpdate = undefined;
var tLastBall = undefined;
var tBallInterval = BALL_INITIAL_INTERVAL;

var translateOffset = 0; 
var currentBallColourIndex = 0;


// Scroll the canvas a little bit, to create the illusion of a moving backdrop.
function scrollBackground() {
    translateOffset = (translateOffset + 0.1) % (game.ctx.canvas.width + 110);
    game.ctx.translate(-translateOffset, 0);  
}


// Draw the sky as a blue-to-red gradient, like a sunset.
function drawSky(context) {

    context.save();

    var grad = context.createLinearGradient(0, 0, 0, context.canvas.height);
    grad.addColorStop(0.0,  'rgba(0,0,150,1.0)'); 
    grad.addColorStop(0.6,  'rgba(0,0,135,0.3)'); 
    grad.addColorStop(0.8,  'rgba(242,167,18,0.7)'); 
    grad.addColorStop(1.0,  'rgba(242,44,11,0.9)'); 
    context.fillStyle = grad;
    context.fillRect(0, 
                    0, 
                    context.canvas.width, 
                    context.canvas.height);

    context.restore();
}


// Draw a big moon in the top-right corner of the canvas.
function drawMoon(context) {

    context.save();

    context.fillStyle = 'white';
    context.strokeStyle = 'rgba(255, 255, 0, 0.25)';
    context.lineWidth = 2;
    context.beginPath();
    context.arc(400, 130, 90, 0, 2 * Math.PI, true);
    context.fill();
    context.stroke();

    context.restore();
}


// Draw a yellow bird in the background.
function drawFarBird(context, x, y) {

    context.save();
    scrollBackground();

    context.fillStyle='yellow';
    context.beginPath();
    context.arc(x, y, 20, 0, 2 * Math.PI, true);
    context.arc(x-20, y-10, 10, 0, 2 * Math.PI, true);
    context.fill();

    context.fillStyle='orange';
    context.beginPath();
    context.moveTo(x-26, y-10);
    context.lineTo(x-38, y-10);
    context.lineTo(x-26, y-15);
    context.fill();

    context.restore();
}


// Draw an orange bird in the foreground.
function drawNearBird(context, x, y) {

    context.save();

    scrollBackground();
    scrollBackground();

    context.fillStyle='orange';
    context.beginPath();
    context.arc(x, y, 40, 0, 2 * Math.PI, true);
    context.arc(x-40, y-20, 20, 0, 2 * Math.PI, true);
    context.fill();

    context.fillStyle='yellow';
    context.beginPath();
    context.moveTo(x-56, y-17);
    context.lineTo(x-80, y-17);
    context.lineTo(x-56, y-24);
    context.fill();

    context.restore();
}


// Start a new game - reset important variables, delete all sprites, and create a new bucket sprite.
function startNewGame() {
    game.reset();
    livesLeft = LIVES_PER_GAME;
    score = 0;
    scorePanel.innerText = '0'; 

    bucket = new Sprite('bucket', new BucketPainter(), []);
    bucket.width = 60;
    bucket.height = 10;
    bucket.left = game.ctx.canvas.width / 2 - bucket.width / 2;
    bucket.top  = game.ctx.canvas.height - bucket.height;

    game.addSprite(bucket);
}


// Update the score by SCORE_BUMP_PER_SECOND every second. 
function updateScore() {
    if (!isLoading && tLastScoreUpdate !== undefined) {
        if (game.tGame - tLastScoreUpdate > 1000) {
            score += SCORE_BUMP_PER_SECOND;
            scorePanel.style.display = 'inline';
            scorePanel.innerHTML = score;
            tLastScoreUpdate = game.tGame;
        }
    }
    else {
        tLastScoreUpdate = game.tGame;
    }
}


// Update the canvas that displays the lives left.
function updateLivesDisplay() {

    livesContext.clearRect(0, 0, livesCanvas.width, livesCanvas.height);
    livesContext.strokeStyle = 'blue';
    livesContext.fillStyle = 'yellow';

    for (var i = 0; i < livesLeft; ++i) {
        var x = 10 + i*25;
        var y = 10;

        livesContext.strokeRect(x, y, 20, 20);
        livesContext.fillRect(x, y, 20, 20);
        livesContext.strokeText(parseInt(i+1), x+7, y+12);
    }
}


// Move the bucket to the new X coordinate.
function moveBucketTo(newX) {
    if (newX >= 0 && newX <= game.ctx.canvas.width - bucket.width) {
        bucket.left = newX;
    }
}


// Pause the game if it's playing, or resume the game if it's paused.
function togglePaused() {
    game.togglePaused();
    pausedPanel.style.display = game.isPaused ? 'inline' : 'none';
}


// Lose a life. If that was the last life, trigger the game-over actions.
function loseLife() {
    livesLeft--;
    game.playSound('LoseLife');

    if (livesLeft === 0) {
        gameOverPanel.style.display = 'block';
        gameOver();
    }
}


// Game-over actions.
function gameOver() {
    var scoresInfo = game.saveScore({name: name, value: score});
    var startScoreIndex = Math.max(0, scoresInfo.thisScoreIndex - 3);
    var endScoreIndex   = Math.min(scoresInfo.scores.length, scoresInfo.thisScoreIndex + 3);

    var scoresHTML = '';
    for (var i = startScoreIndex; i < endScoreIndex; i++) {
        if (i == scoresInfo.thisScoreIndex) 
            scoresHTML += '<p style="color:orange">';
        else
           scoresHTML += '<p>';   
        scoresHTML += '[' + i + '] ' + scoresInfo.scores[i].value + ': ' + scoresInfo.scores[i].name + '</p>' 
    }
    scoresListDiv.innerHTML = scoresHTML;  
    game.isGameOver = true;
}


// Event handler: If the user leaves the window, pause the game.
window.onblur = function windowOnBlur() { 
    if (!isLoading && !game.isGameOver && !game.isPaused) {
        togglePaused();
    }
};


// Event handler: If the user re-enters the window, resume the game.
window.onfocus = function windowOnFocus() {
    if (game.isPaused) {
        togglePaused();
    }
};


// Event handler: When the user clicks the "New Game" button, start a new game.
newGameButton.onclick = function (e) {
    gameOverPanel.style.display = 'none';
    startNewGame();
};


// Event handler: When the user clicks the "Load" button, load all the images.
loadButton.onclick = function (e) {
    var interval;
    var loadingPercentComplete = 0;

    e.preventDefault();

    name = nameTextBox.value;
    loadDiv.style.display = 'none';

    game.loadImages([
                    'images/001.jpg',
                    'images/002.jpg',
                    'images/003.jpg',
                    'images/004.jpg',
                    'images/005.jpg',
                    'images/006.jpg',
                    'images/007.jpg',
                    'images/008.jpg',
                    'images/009.jpg',
                    'images/010.jpg',
                    'images/011.jpg',
                    'images/012.jpg',
                    'images/013.jpg',
                    'images/014.jpg',
                    'images/015.jpg',
                    'images/016.jpg',
                    'images/017.jpg',
                    'images/018.jpg',
                    'images/019.jpg',
                    'images/020.jpg',
                    'images/021.jpg',
                    'images/022.jpg',
                    'images/023.jpg',
                    'images/024.jpg',
                    'images/025.jpg',
                    'images/026.jpg',
                    'images/027.jpg',
                    'images/028.jpg',
                    'images/029.jpg',
                    'images/030.jpg',
                    'images/031.jpg',
                    'images/032.jpg',
                    'images/033.jpg',
                    'images/034.jpg',
                    'images/035.jpg',
                    'images/036.jpg',
                    'images/037.jpg',
                    'images/038.jpg',
                    'images/039.jpg',
                    'images/040.jpg',
                    'images/041.jpg',
                    'images/042.jpg',
                    'images/043.jpg',
                    'images/044.jpg',
                    'images/045.jpg',
                    'images/046.jpg',
                    'images/047.jpg',
                    'images/048.jpg',
                    'images/049.jpg',
                    'images/050.jpg',
                    ]);

    interval = setInterval( function (e) {
        if (game.getImageLoadingProgress() === 100) {
            clearInterval(interval);
            isLoading = false;
            loadingPanel.style.display = 'none';
            scorePanel.style.display = 'inline';
            startNewGame();
        }
    }, 100);
};


// Game method: Initialize a new animation frame.
game.preDrawFrame = function (tNow, tGame) {

    if (!isLoading && !game.isGameOver) {
        if (!tLastBall || tGame - tLastBall > tBallInterval) {

            currentBallColourIndex = ++currentBallColourIndex % BALL_COLOURS.length;
            var painter = new BallPainter(BALL_COLOURS[currentBallColourIndex]);

            var behaviour = new BallBehaviour(1 + Math.random());

            var sprite = new Sprite('ball', painter, [behaviour]);
            sprite.velocityX = 2 + 12 * Math.random();
            game.addSprite(sprite);

            tLastBall = tGame;
            tBallInterval = Math.max(1000, tBallInterval - 200);
        }
    }
}


// Game method: Draw the background.
game.drawUnderLayer = function () { 
    drawSky(game.ctx);
    drawMoon(game.ctx);
    drawFarBird(game.ctx, game.ctx.canvas.width + 50, 50);

    if (!game.isGameOver) {
        updateScore();
    }
    updateLivesDisplay();
};


// Game method: Draw the foreground.
game.drawOverLayer = function () {
    drawNearBird(game.ctx, game.ctx.canvas.width + 90, 150);
    drawNearBird(game.ctx, game.ctx.canvas.width*2 + 180, 150);
}


// Game method: When a sprite is deleted, either increment the score or lose a life.
game.onDeleteSprite = function (sprite) {
    if (sprite.left >= bucket.left && 
        sprite.left <= bucket.left + bucket.width) {

        this.playSound('CatchBall');
        score += SCORE_BUMP_PER_CATCH;
    }
    else {
        loseLife();
    }

}


// Game method: Display visual feedback about image-loading progress.
game.imageLoadingProgress = function (percent) { 
    progressDiv.innerHTML = Math.ceil(percent) + '%';
    progressDiv.style.width = percent + '%';
}


// Game method: Handle mouse event, to move the bucket.
game.handleMouseMoveEvent = function (e) {
    moveBucketTo(e.clientX);
}


// Game method: Handle keyboard event, to pause/unpause the game.
game.addKeyListener(game.KEY_P, 
                    function () {
                        togglePaused();
                    });


// Game method: Handle keyboard event, to move the bucket left.
game.addKeyListener(game.KEY_ARROW_LEFT, 
                    function () {
                        moveBucketTo(bucket.left - BUCKET_DELTA);
                    });


// Game method: Handle keyboard event, to move the bucket right.
game.addKeyListener(game.KEY_ARROW_RIGHT, 
                    function () {
                        moveBucketTo(bucket.left + BUCKET_DELTA);
                    });


// Start the game!
game.start();
