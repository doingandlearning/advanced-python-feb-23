// Global constants.
var BALL_RADIUS = 8;
var BRICK_HEIGHT = 20;
var BRICKS_PER_ROW = 15;
var BRICK_ROWS = 10;
var SCROLL_INTERVAL = 3000;

// Global variables.
var canvas, context;
var raf;
var ball;
var bricks = [];

function init() {

    // Get the <canvas> and its 2d context.
    canvas  = document.getElementById("myCanvas");
    context = canvas.getContext("2d");

    // Get the appropriate requestAnimationFrame function.
    raf = window.requestAnimationFrame       ||
          window.mozRequestAnimationFrame    ||
          window.webkitRequestAnimationFrame ||
          window.msRequestAnimationFrame     ||
          window.oRequestAnimationFrame;

    // Create all the bricks.
    for (var r = 0; r < BRICK_ROWS; r++) {
        for (var c = 0; c < BRICKS_PER_ROW; c++) {
            bricks.push(new Brick('brick_' + r + '_' + c,
                                   new BrickPainter(),
                                   [new BrickBehaviour(SCROLL_INTERVAL)],
                                   r,
                                   c,
                                   canvas.width / BRICKS_PER_ROW,
                                   BRICK_HEIGHT));
        }
    }

    // Create the ball.
    ball = new Ball('ball',
                     new BallPainter(),
                     [new BallBehaviour(bricks)],
                     canvas.width / 2,
                     canvas.height - BALL_RADIUS,
                     BALL_RADIUS);

    // Start drawing!
    raf(draw);
}

function draw(tNow) {

    raf(draw);      

    context.clearRect(0, 0, canvas.width, canvas.height);

    for (var b = 0; b < bricks.length; b++) {
        bricks[b].paint(context);
        bricks[b].update(tNow, context);
    }

    ball.paint(context);
    ball.update(tNow, context);
}
