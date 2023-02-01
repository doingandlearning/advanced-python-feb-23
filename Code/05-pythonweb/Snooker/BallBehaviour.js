// ----------------------------------------------------------------------------------------------
// BallBehaviour object.
// ----------------------------------------------------------------------------------------------
var BallBehaviour = function (coefficientOfFriction, cushionDampingEffect) {
    this.tPrev = null;
    this.coefficientOfFriction = coefficientOfFriction;
    this.cushionDampingEffect = cushionDampingEffect;

    return this;
};


BallBehaviour.prototype = {

    doBehaviour: function (ball, tNow, ctx) {

        // How much time has elapsed since the last time the ball was drawn?
        var tDelta = (tNow - (this.tPrev || tNow)) / 1000;
        this.tPrev = tNow;

        // Calculate the loss of velocity due to friction, during the elapsed time.
        ball.v -= this.coefficientOfFriction * g * tDelta;

        // Move the ball by the correct amount in the x and y directions, in metres.
        ball.cx += ball.v * Math.cos(ball.angle) * tDelta;
        ball.cy += ball.v * Math.sin(ball.angle) * tDelta;

        // If the ball has hit the left or right cushion, flip its x direction (and damp its speed).
        if (ball.cx + ball.r > ball.table.width) {
            this.cushionBounceX(ball, ball.table.width - ball.r);
        }
        else if (ball.cx - ball.r < 0) {
            this.cushionBounceX(ball, ball.r);
        }

        // If the ball has hit the bottom or top cushion, flip its y direction (and damp its speed).
        if (ball.cy + ball.r >= ball.table.height) {
            this.cushionBounceY(ball, ball.table.height - ball.r);
        }
        else if (ball.cy - ball.r < 0) {
            this.cushionBounceY(ball, ball.r);
        }

        // If the ball is in the pocket, set important properties to record this fact.
        if (ball.table.isBallInPocket(ball)) {
            ball.isPocketed = true;
            ball.isVisible = false;
            ball.v = 0;
        }

        // If the ball has stopped, reset important properties.
        if (ball.v <= 0) {
            ball.v = 0;
            this.tPrev = null;
        }
    },

    // Helper method, to bounce the ball off a vertical cushion.
    cushionBounceX: function (ball, newCx) {
        ball.cx = newCx;
        ball.angle = Math.PI - ball.angle;
        ball.v *= this.cushionDampingEffect;
    },

    // Helper method, to bounce the ball off a horizontal cushion.
    cushionBounceY: function (ball, newCy) {
        ball.cy = newCy;
        ball.angle = -ball.angle;
        ball.v *= this.cushionDampingEffect;
    }
};
