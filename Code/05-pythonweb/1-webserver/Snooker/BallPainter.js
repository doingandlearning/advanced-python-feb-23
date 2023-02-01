// ----------------------------------------------------------------------------------------------
// BallPainter object.
// ----------------------------------------------------------------------------------------------
var BallPainter = function () {
    return this;
};


BallPainter.prototype = {

    doPaint: function (ball, ctx) {

        // Calculate the pixels per metre.
        var ppm = ctx.canvas.width / ball.table.width;

        ctx.save();
        ctx.beginPath();

        // Shift the coordinate system temporarily to the centre of the ball, to simplify the maths!
        ctx.translate(ball.cx * ppm, ball.cy * ppm);

        // Create a radial gradient, to give the ball a 3D-style appearance.
        var spotlight = -0.5 * ball.r * ppm;
        var radialGradient = ctx.createRadialGradient(spotlight, spotlight, 0, spotlight, spotlight, ball.r * 2 * ppm);
        radialGradient.addColorStop(0, 'antiquewhite');
        radialGradient.addColorStop(0.2, ball.colour);
        radialGradient.addColorStop(0.9, 'gray');

        // Paint the ball as a circle, using the radial gradient.
        ctx.fillStyle = radialGradient;
        ctx.arc(0, 0, ball.r * ppm, 0, Math.PI * 2);
        ctx.fill();

        ctx.restore();
    }
};