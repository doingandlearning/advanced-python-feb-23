// Ball painter.
var BallPainter = function (color) {
    this.color = color;
};

BallPainter.prototype = {

    doPaint: function (sprite, ctx) {
        ctx.save();
        ctx.beginPath();
        ctx.fillStyle = this.color;
        ctx.arc(sprite.left + sprite.width/2, 
                sprite.top  + sprite.height/2, 
                sprite.width/2, 
                0, 
                Math.PI*2);

        ctx.fill();
        ctx.restore();
    }    
};


// Ball behaviour.
var BallBehaviour = function (warpFactor) {
    this.tPrev = undefined;
    this.warpFactor = warpFactor;
};


// Useful constants for calculating ball movement under gravity.
var GRAVITY = 9.81;
var CANVAS_LOGICAL_HEIGHT = 100;

BallBehaviour.prototype = {
    doBehaviour: function (sprite, tNow, ctx) {

        if (!sprite.tStart) {
            sprite.tStart = tNow;
        }

        if (this.tPrev) {
            // Calculate new Y velocity for sprite, based on total time it's been moving.
            var tMoving = (tNow - sprite.tStart) / 1000;
            sprite.velocityY = GRAVITY * tMoving * this.warpFactor;

            // Calculate new sprite position, based on time since last frame and current velocity.
            var tDelta = (tNow - this.tPrev) / 1000;
            var pixelsPerMetre = ctx.canvas.height / CANVAS_LOGICAL_HEIGHT;
            sprite.left += sprite.velocityX * tDelta * pixelsPerMetre;
            sprite.top  += sprite.velocityY * tDelta * pixelsPerMetre;

            // Has the sprite reached the bottom of the canvas?
            if (sprite.top >= ctx.canvas.height) {
                sprite.isVisible = false;
                sprite.isRunning = false;
            }
        }
        this.tPrev = tNow;
    }
};
