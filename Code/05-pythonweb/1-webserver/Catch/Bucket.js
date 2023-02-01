// Bucket painter.
var BucketPainter = function () {
};

BucketPainter.prototype = {

    doPaint: function (sprite, ctx) {
        ctx.save();
        ctx.strokeStyle = 'darkblue';
        ctx.lineWidth = 5;  
        
        ctx.beginPath();
        ctx.moveTo(sprite.left, sprite.top);
        ctx.lineTo(sprite.left, sprite.top + sprite.height);
        ctx.lineTo(sprite.left + sprite.width, sprite.top + sprite.height);
        ctx.lineTo(sprite.left + sprite.width, sprite.top);
        ctx.stroke();
        
        ctx.restore();
    }
};

