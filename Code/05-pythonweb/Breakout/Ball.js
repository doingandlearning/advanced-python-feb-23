// ----------------------------------------------------------------------------------------------
// Ball object, inherits from Sprite.
// ----------------------------------------------------------------------------------------------
var Ball = function (name, painter, behaviours, initCx, initCy, radius) {

    // Call the Sprite (i.e. base-object) constructor.
    Sprite.call(this, name, painter, behaviours);

    // Additional Ball-specific properties.
    this.cx = initCx;
    this.cy = initCy;
    this.radius = radius;
    this.xDelta = 0.6;
    this.yDelta = -0.4;

    return this;
};

// Brick inherits all the methods from Sprite.
Ball.prototype = new Sprite();


// ----------------------------------------------------------------------------------------------
// BallPainter object.
// ----------------------------------------------------------------------------------------------
var BallPainter = function () {
    return this;
};

BallPainter.prototype = {

    doPaint: function (ball, ctx) {
        ctx.save();
        ctx.beginPath();
        ctx.fillStyle = 'red';
        ctx.arc(ball.cx, ball.cy, ball.radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
    }
};

// ----------------------------------------------------------------------------------------------
// BallBehaviour object.
// ----------------------------------------------------------------------------------------------
var BallBehaviour = function (bricks) {
    this.bricks = bricks;
    this.tPrev = undefined;
    return this;
};


BallBehaviour.prototype = {

    doBehaviour: function (ball, tNow, ctx) {

        // How much time has elapsed since the last time the ball was drawn?
        var tDelta = tNow - (this.tPrev || tNow);
        this.tPrev = tNow;

        // Move the ball by the correct amount in the x direction.
		ball.cx += ball.xDelta * tDelta;

		// If the ball has hit the left or right wall, flip its x direction.
		if (ball.cx + ball.radius > context.canvas.width) {     
			ball.cx = context.canvas.width - ball.radius;
			ball.xDelta = -ball.xDelta;
		}
		else if (ball.cx - ball.radius < 0) {                   
			ball.cx = ball.radius;
			ball.xDelta = -ball.xDelta;
		}
		
        // Move the ball by the correct amount in the y direction.
        ball.cy += ball.yDelta * tDelta;

        // If the ball has hit the bottom or top wall, flip its y direction.
        if (ball.cy + ball.radius >= context.canvas.height) {
            ball.cy = context.canvas.height - ball.radius;
            ball.yDelta = -ball.yDelta;
        }
        else if (ball.cy - ball.radius < 0) {
            ball.cy = ball.radius;
            ball.yDelta = -ball.yDelta;
        }

        // Has the ball hit any brick?
        var ballLeft   = ball.cx - ball.radius;
        var ballRight  = ball.cx + ball.radius;
        var ballTop    = ball.cy - ball.radius;
        var ballBottom = ball.cy + ball.radius;

        for (var i = 0; i < this.bricks.length; i++) {

            var brick = this.bricks[i];

            if (!brick.isVisible) {
                continue;
            }

            // If the ball is too far away from this brick, then it hasn't hit it.
            if (ballTop > brick.bottom() ||
                ballBottom < brick.top() ||
                ballLeft > brick.right() ||
                ballRight < brick.left()) {
                continue;
            }

            // If we get this far, the ball has definitely hit the brick somewhere.
            brick.isVisible = false;

            // If the ball hit the top or bottom of the brick, flip its y direction.
            if (ballTop <= brick.bottom() ||
                ballBottom >= brick.top()) {
                ball.yDelta = -ball.yDelta;
            }
            else {  // Else flip is x direction.
                ball.xDelta = -ball.xDelta;
            }

            // Don't bother checking for any other brick hits.
            return;
        }
    }
};
