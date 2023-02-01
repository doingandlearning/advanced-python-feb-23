// ----------------------------------------------------------------------------------------------
// Table object, inherits from Sprite.
// ----------------------------------------------------------------------------------------------
var Table = function (name, tablePainter, tableBehaviours) {
    
    // Call the Sprite (i.e. base-object) constructor.
    Sprite.call(this, name, tablePainter, tableBehaviours);

    // Components of a snooker table.
    this.pockets = [];         
    this.spots = {};            
    this.balls = [];

    // Official dimensions of a snooker table. All measurements are in metres.
    this.width = 3.569;     
    this.height = 1.778;
    this.rBall = 0.04;          // In a real game, the ball radius is 0.0262 (but that makes the game too hard!)
    this.rPocket = this.rBall * 2;
    this.xBaulk = 0.737;
    this.rBaulk = 0.292;
    this.xPink = this.width * 0.75;
    this.xBlack = 3.245;

    // Additional properties to help us manage game strategy.
    this.numRedRows = 3;        // In a real game, there are 5 rows of reds.
    this.redsRemaining = 0;     // Keep count of the number of reds remaining, so we can decide whether to respot colour balls.

    // Create all the table components.
    this.createPockets();
    this.createSpots();
    this.createBalls();

    return this;
};

// Table inherits all the methods from Sprite.
Table.prototype = new Sprite();

// Additional Table method, to create all the pockets for the table.
Table.prototype.createPockets = function () {

    this.pockets = [
        {
            cx: 0,
            cy: 0
        },
        {
            cx: this.width / 2,
            cy: 0
        },
        {
            cx: this.width,
            cy: 0
        },
        {
            cx: 0,
            cy: this.height
        },
        {
            cx: this.width / 2,
            cy: this.height
        },
        {
            cx: this.width,
            cy: this.height
        }
    ];
};

// Additional Table method, to create the spots for the colour balls.
Table.prototype.createSpots = function () {

    this.spots = {
        cue: {
            colour: 'white',
            cx: this.xBaulk - 0.1,
            cy: (this.height / 2 - 0.1),
        },
        yellow: {
            colour: 'yellow',
            cx: this.xBaulk,
            cy: (this.height / 2 + this.rBaulk)
        },
        green: {
            colour: 'darkgreen',
            cx: this.xBaulk,
            cy: (this.height / 2 - this.rBaulk),
        },
        brown: {
            colour: 'brown',
            cx: this.xBaulk,
            cy: (this.height / 2)
        },
        blue: {
            colour: 'blue',
            cx: this.width / 2,
            cy: (this.height / 2)
        },
        pink: {
            colour: 'pink',
            cx: this.xPink,
            cy: (this.height / 2)
        },
        black: {
            colour: 'black',
            cx: this.xBlack,
            cy: (this.height / 2)
        }
    };
};

// Additional Table method, to create all the Ball objects for the game.
Table.prototype.createBalls = function () {

    // Create the white ball, plus all the colour balls.
    for (var key in this.spots) {
        var spot = this.spots[key];
        this.balls.push(new Ball(key, new BallPainter(), [new BallBehaviour(0.1, 0.9)], this, spot.colour, spot.cx, spot.cy, this.rBall));
    }

    // Create all the red balls behind the pink ball, in rows of 1, 2, 3, 4, 5, etc.
    var cxInit = this.xPink + (2 * this.rBall);
    for (var r = 0; r < this.numRedRows; r++) {

        var cx = cxInit + (r * 2 * this.rBall);
        var cyInit = (this.height / 2) - (r * this.rBall);

        for (var b = 0; b <= r; b++) {
            var cy = cyInit + (b * 2 * this.rBall);
            this.redsRemaining++;
            this.balls.push(new Ball('red', new BallPainter(), [new BallBehaviour(0.1, 0.9)], this, 'red', cx, cy, this.rBall));
        }
    }
};

// Additional Table method, to start the cue ball moving.
Table.prototype.hitCueBall = function (speed, angleDegrees) {
    var cueBall = this.balls[0];
    cueBall.v = speed;
    cueBall.angle = angleDegrees * Math.PI / 180;
};

// Additional Table method, to test if a ball is in a pocket.
Table.prototype.isBallInPocket = function (ball) {

    // Loop through all the pockets, to see if the ball is in a pocket.
    for (var p = 0; p < this.pockets.length; p++) {
        
        var dx = ball.cx - this.pockets[p].cx;
        var dy = ball.cy - this.pockets[p].cy;
        var distanceToPocket = Math.sqrt(dx * dx + dy * dy);
        
        if (distanceToPocket < this.rPocket) {
            if (ball.name == 'red') {
                this.redsRemaining--;
            }
            return true;
        }
    }
    return false;
}

// Additional Table method, to respot any balls that should be respotted (if no balls are moving).
Table.prototype.respotBalls = function () {

    // If any balls are moving, we can't respot anything else.
    for (var b = 0; b < this.balls.length; b++) {
        if (this.balls[b].v != 0) {
            return;
        }
    }

    // If there are any reds remaining, respot any colour balls (including the cue ball) if they are in a pocket.
    if (this.redsRemaining > 0) {
        for (var b = 0; b < 6; b++) {
            var ball = this.balls[b];
            if (ball.isPocketed) {
                var spot = this.spots[ball.name];
                ball.respot(spot.cx, spot.cy);
            }
        }
    }
};

// Additional Table method, to test for any ball collisions.
Table.prototype.testForCollisions = function () {

    for (var b1 = 0; b1 < this.balls.length - 1; b1++) {
        for (var b2 = b1 + 1; b2 < this.balls.length; b2++) {
            if (this.balls[b1].v != 0 || this.balls[b2].v != 0) {
                this.handlePossibleCollision(b1, b2);
            }
        }
    }
};

// Additional Table method, to test for a collision between two specific balls.
Table.prototype.handlePossibleCollision = function (b1, b2) {

    var ball1 = this.balls[b1];
    var ball2 = this.balls[b2];

    // Calculate the magnitude of the separation of the two balls, using Pythagoras' Theorem.
    var dx = ball2.cx - ball1.cx;
    var dy = ball2.cy - ball1.cy;
    var d = Math.sqrt(dx * dx + dy * dy);

    if (d > ball1.r + ball2.r) {
        // The balls are too far apart, so set a flag to indicate "no collision".
        ball1.isColliding[b2] = false;
    }
    else if (!ball1.isColliding[b2]) {

        // The balls are close enough, and we haven't already detected this collision.
        ball1.isColliding[b2] = true;

        // Calculate the angle at which the balls are colliding.
        var collisionAngle = Math.atan2(dy, dx);

        // Calculate the initial velocities in the transformed coordinate system (where the new x axis is along the direction of the collision).
        var ux1 = ball1.v * Math.cos(ball1.angle - collisionAngle);
        var uy1 = ball1.v * Math.sin(ball1.angle - collisionAngle);
        var ux2 = ball2.v * Math.cos(ball2.angle - collisionAngle);
        var uy2 = ball2.v * Math.sin(ball2.angle - collisionAngle);

        // Calculate the final velocities in the transformed coordinate system (in an elastic collision, the x velocities are simply exchanged).
        var vx1 = ux2;
        var vx2 = ux1;
        var vy1 = uy1;
        var vy2 = uy2;

        // Split the final velocities back into components in the normal coordinate system.
        var fx1 = vx1 * Math.cos(collisionAngle) - vy1 * Math.sin(collisionAngle);
        var fy1 = vx1 * Math.sin(collisionAngle) + vy1 * Math.cos(collisionAngle);
        var fx2 = vx2 * Math.cos(collisionAngle) - vy2 * Math.sin(collisionAngle);
        var fy2 = vx1 * Math.sin(collisionAngle) + vy2 * Math.cos(collisionAngle);

        // Use Pythagoras' Theorem to calculate final velocity magnitudes for the two balls.
        ball1.v = Math.sqrt(fx1 * fx1 + fy1 * fy1);
        ball2.v = Math.sqrt(fx2 * fx2 + fy2 * fy2);

        // Use trigonometry to calculate the final angles of movement for the two balls.
        ball1.angle = Math.atan2(fy1, fx1);
        ball2.angle = Math.atan2(fy2, fx2);
    }
};
